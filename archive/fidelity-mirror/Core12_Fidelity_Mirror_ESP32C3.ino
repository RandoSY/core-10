/*
  Core 12 Fidelity Mirror - ESP32-C3 acquisition firmware v1.0
  ------------------------------------------------------------
  Streams four synchronized ADC channels as compact binary C12F/1 packets
  over native USB CDC Serial and/or BLE Nordic UART Service (NUS).

  Default ADC pins (ESP32-C3 ADC1): GPIO0, GPIO1, GPIO3, GPIO4.
  Change ADC_PINS[] if your board wiring differs.

  Host commands (newline terminated):
    START
    STOP
    RATE,200      // 10..5000 samples/s
    PING

  Arduino IDE notes:
    - Board: your ESP32-C3 board
    - USB CDC On Boot: Enabled (for native USB boards)
    - Library: NimBLE-Arduino 2.x (h2zero)
*/

#include <Arduino.h>
#include <NimBLEDevice.h>

static const uint8_t ADC_PINS[4] = {0, 1, 3, 4};
static const uint8_t CHANNEL_MASK = 0x0F;
static const uint8_t BATCH_FRAMES = 8;
static const uint32_t DEFAULT_RATE_HZ = 200;

static const char* NUS_SERVICE = "6e400001-b5a3-f393-e0a9-e50e24dcca9e";
static const char* NUS_RX      = "6e400002-b5a3-f393-e0a9-e50e24dcca9e";
static const char* NUS_TX      = "6e400003-b5a3-f393-e0a9-e50e24dcca9e";

NimBLECharacteristic* txChar = nullptr;
volatile bool bleConnected = false;
volatile bool streaming = true;
uint32_t sampleRateHz = DEFAULT_RATE_HZ;
uint32_t samplePeriodUs = 1000000UL / DEFAULT_RATE_HZ;
uint32_t nextSampleUs = 0;
uint32_t packetSeq = 0;

uint16_t sampleBuf[BATCH_FRAMES][4];
uint8_t batchCount = 0;
uint32_t batchT0Us = 0;

String usbCmd, bleCmd;

static uint16_t crc16ccitt(const uint8_t* data, size_t len) {
  uint16_t crc = 0xFFFF;
  for (size_t i = 0; i < len; ++i) {
    crc ^= (uint16_t)data[i] << 8;
    for (uint8_t b = 0; b < 8; ++b)
      crc = (crc & 0x8000) ? (uint16_t)((crc << 1) ^ 0x1021) : (uint16_t)(crc << 1);
  }
  return crc;
}

static void putU16LE(uint8_t* p, uint16_t v) { p[0]=v & 0xFF; p[1]=(v>>8)&0xFF; }
static void putU32LE(uint8_t* p, uint32_t v) { p[0]=v&0xFF; p[1]=(v>>8)&0xFF; p[2]=(v>>16)&0xFF; p[3]=(v>>24)&0xFF; }

void handleCommand(String cmd) {
  cmd.trim();
  cmd.toUpperCase();
  if (!cmd.length()) return;
  if (cmd == "START") streaming = true;
  else if (cmd == "STOP") streaming = false;
  else if (cmd == "PING") Serial.println("PONG");
  else if (cmd.startsWith("RATE,")) {
    uint32_t r = cmd.substring(5).toInt();
    if (r >= 10 && r <= 5000) {
      sampleRateHz = r;
      samplePeriodUs = 1000000UL / sampleRateHz;
      nextSampleUs = micros() + samplePeriodUs;
      batchCount = 0;
    }
  }
}

class ServerCB : public NimBLEServerCallbacks {
  void onConnect(NimBLEServer*, NimBLEConnInfo&) override { bleConnected = true; }
  void onDisconnect(NimBLEServer*, NimBLEConnInfo&, int) override {
    bleConnected = false;
    NimBLEDevice::startAdvertising();
  }
};

class RxCB : public NimBLECharacteristicCallbacks {
  void onWrite(NimBLECharacteristic* c, NimBLEConnInfo&) override {
    std::string s = c->getValue();
    for (char ch : s) {
      if (ch == '\n' || ch == '\r') {
        if (bleCmd.length()) { handleCommand(bleCmd); bleCmd = ""; }
      } else if (bleCmd.length() < 80) bleCmd += ch;
    }
  }
};

void setupBLE() {
  NimBLEDevice::init("Core12-Fidelity-Mirror");
  NimBLEServer* server = NimBLEDevice::createServer();
  server->setCallbacks(new ServerCB());
  NimBLEService* svc = server->createService(NUS_SERVICE);
  txChar = svc->createCharacteristic(NUS_TX, NIMBLE_PROPERTY::NOTIFY);
  NimBLECharacteristic* rx = svc->createCharacteristic(NUS_RX, NIMBLE_PROPERTY::WRITE | NIMBLE_PROPERTY::WRITE_NR);
  rx->setCallbacks(new RxCB());
  svc->start();
  NimBLEAdvertising* adv = NimBLEDevice::getAdvertising();
  adv->addServiceUUID(NUS_SERVICE);
  adv->setName("Core12-Fidelity-Mirror");
  adv->start();
}

void sendBLEFragmented(const uint8_t* data, size_t len) {
  if (!bleConnected || !txChar) return;
  // Conservative 20-byte chunks work even before a larger MTU is negotiated.
  const size_t CHUNK = 20;
  for (size_t off=0; off<len; off+=CHUNK) {
    size_t n = min(CHUNK, len-off);
    txChar->setValue(data+off, n);
    txChar->notify();
    delayMicroseconds(250);
  }
}

void emitPacket() {
  if (!batchCount) return;
  const uint8_t channels = 4;
  const size_t payload = (size_t)batchCount * channels * 2;
  const size_t total = 20 + payload + 2;
  uint8_t packet[20 + BATCH_FRAMES*4*2 + 2];

  packet[0]='C'; packet[1]='1'; packet[2]='2'; packet[3]='F';
  packet[4]=1;                 // protocol version
  packet[5]=CHANNEL_MASK;
  packet[6]=batchCount;
  packet[7]=0;                 // flags reserved
  putU32LE(packet+8, packetSeq++);
  putU32LE(packet+12, batchT0Us);
  putU32LE(packet+16, samplePeriodUs);

  size_t o=20;
  for (uint8_t s=0; s<batchCount; ++s)
    for (uint8_t ch=0; ch<4; ++ch) {
      putU16LE(packet+o, sampleBuf[s][ch]);
      o += 2;
    }

  uint16_t crc = crc16ccitt(packet, total-2);
  putU16LE(packet+total-2, crc);

  if (Serial) Serial.write(packet, total);
  sendBLEFragmented(packet, total);
  batchCount = 0;
}

void pollUSBCommands() {
  while (Serial.available()) {
    char ch = (char)Serial.read();
    if (ch == '\n' || ch == '\r') {
      if (usbCmd.length()) { handleCommand(usbCmd); usbCmd = ""; }
    } else if (usbCmd.length() < 80) usbCmd += ch;
  }
}

void setup() {
  Serial.begin(921600);
  delay(200);
  analogReadResolution(12);
  for (uint8_t i=0;i<4;i++) pinMode(ADC_PINS[i], INPUT);
  setupBLE();
  nextSampleUs = micros() + samplePeriodUs;
}

void loop() {
  pollUSBCommands();
  if (!streaming) { delay(1); return; }

  uint32_t now = micros();
  // Signed subtraction is wrap-safe for intervals < ~35 min.
  while ((int32_t)(now - nextSampleUs) >= 0) {
    if (batchCount == 0) batchT0Us = nextSampleUs;
    for (uint8_t ch=0; ch<4; ++ch) sampleBuf[batchCount][ch] = analogRead(ADC_PINS[ch]);
    batchCount++;
    nextSampleUs += samplePeriodUs;
    if (batchCount >= BATCH_FRAMES) emitPacket();
    now = micros();
  }
}
