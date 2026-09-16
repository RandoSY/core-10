2.  Trace the conceptual path: hydrated Mg²⁺ → phosphate interactions →
    Mg-ATP → enzymes → DNA/RNA.

3.  Examine a reputable PCR reference showing Mg²⁺ as a DNA-polymerase
    cofactor.

4.  Construct an evidence map separating what was measured in class from
    what comes from structural/biochemical literature.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-18 From Ice Melt to Living Molecules**

*Why does biology care about hydrated Mg²⁺?*

**MAKE MEANING**

**THEORY**

- Mg²⁺ has strong hydration chemistry and is a ubiquitous biological
  cofactor. In PCR, Mg²⁺ is supplied commonly as MgCl₂ and supports DNA
  polymerase chemistry and charge stabilization.

**EXPECTED OBSERVATIONS**

- The same ion can be studied as a deicer component, hydrated crystal
  constituent, solvated species, and biological cofactor.

**ANALYSIS**

- Create a concept map with citations.

- Label each arrow as observed, calculated, simulated, or
  literature-supported.

**REASONING TRAP**

*Conceptual continuity is not proof that a kitchen deicer sample can be
used in biological systems. Purity and context matter.*

**UNO/MFS INSTRUMENTED MODE**

The host/AI layer can now query the entire evidence chain: run data,
formulas, CIF metadata, and curated references. The cup remains the
physical anchor.

**AI REASONING CHALLENGE**

Ask AI to explain the entire chain in 200 words, then force it to tag
every claim as "our measurement," "calculation," "simulation," or
"external evidence."

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Can an AI reason across the whole chain without smuggling in
assumptions?*

**OCC-19 Can the Reasoner Find the Flaw?**

*How intelligent is an AI when the experimental premise itself is
wrong?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Treat AI output as testable scientific reasoning.

- Design prompts that expose assumptions.

- Use physical data to audit explanations.

**MATERIALS**

- Any completed OCC dataset

- PC with AI access

- student prompt log

- rubric

**SAFETY**

No additional chemical hazard. Privacy: do not send student personal
data or restricted information to external systems.

**PROCEDURE**

1.  Choose one prior experiment with a hidden or tempting assumption.

2.  Before showing data, ask AI for a prediction and required
    assumptions.

3.  Provide the actual protocol and ask for a critique.

4.  Provide data and request an explanation.

5.  Score whether it notices mass, concentration, hydrate state, sensor
    limits, or other premise issues before being prompted.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-19 Can the Reasoner Find the Flaw?**

*How intelligent is an AI when the experimental premise itself is
wrong?*

**MAKE MEANING**

**THEORY**

- Scientific intelligence is not just calculation. It includes premise
  checking, model selection, uncertainty, and willingness to revise.

- AI should be evaluated against physical evidence and explicit
  reasoning criteria.

**EXPECTED OBSERVATIONS**

- Different prompts can produce materially different reasoning quality.

**ANALYSIS**

- Use a rubric: assumption detection, physical correctness, quantitative
  consistency, uncertainty, falsifiability, and revision quality.

**REASONING TRAP**

*The goal is not to "catch the AI being wrong." The goal is to
distinguish fluent completion from disciplined scientific reasoning.*

**UNO/MFS INSTRUMENTED MODE**

UNO/MFS + host bridge makes the test unusually clean: the same
machine-readable data stream can be inspected by humans, plotted by
software, and presented to the AI without manual transcription.

**AI REASONING CHALLENGE**

Ask the AI to state what observation would falsify its explanation. A
reasoner that cannot name disconfirming evidence has not finished the
scientific job.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*The curriculum loops back to OCC-00: measurement, evidence,
uncertainty, and disciplined inference.*

**Appendix A – UNO/MFS starter data logger**

This sketch is intentionally simple and readable. It assumes a common
MFS revision with a DS18B20 on A4; verify the shield. It streams
temperature as ASCII over USB serial. Button/display integration can be
added after the sensor path is proven.

\#include \<OneWire.h\>

\#include \<DallasTemperature.h\>

const uint8_t ONE_WIRE_PIN = A4;

const unsigned long SAMPLE_MS = 1000;

OneWire oneWire(ONE_WIRE_PIN);

DallasTemperature sensors(&oneWire);

unsigned long lastSample = 0;

void setup() {

Serial.begin(115200);

sensors.begin();

Serial.println("META,OCC,LOGGER=UNO_MFS,TEMP=DS18B20,UNIT=C");

}

void loop() {

unsigned long now = millis();

if (now - lastSample \>= SAMPLE_MS) {

lastSample = now;

sensors.requestTemperatures();

float tC = sensors.getTempCByIndex(0);

Serial.print("T,");

Serial.print(now);

Serial.print(",");

Serial.println(tC, 2);

}

}

**BRING-UP ORDER**

- 1\. Verify the DS18B20 locally.

- 2\. Verify readable serial output in Arduino Serial Monitor.

- 3\. Log the same stream from Python.

- 4\. Plot it live.

- 5\. Add metadata and event markers.

- 6\. Only then connect the stream to the AI/MCP layer.

|                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ENGINEERING PRINCIPLE** Prove one link at a time: sensor → microcontroller → serial → logger → dashboard → AI. A sophisticated architecture is still just a chain of testable links. |

**Appendix B – Minimal Python logger**

import csv, serial, time

PORT = "COM55" \# change for the classroom PC

BAUD = 115200

OUT = "occ_run.csv"

with serial.Serial(PORT, BAUD, timeout=2) as ser, open(OUT, "w",
newline="") as f:

writer = csv.writer(f)

writer.writerow(\["host_time", "raw_line"\])

while True:

line = ser.readline().decode("utf-8", errors="replace").strip()

if not line:

continue

print(line)

writer.writerow(\[time.time(), line\])

f.flush()

**WHY STORE THE RAW LINE?**

Because parser bugs are recoverable if the original evidence survives. A
second process can parse T records into numeric columns while the first
logger preserves exactly what arrived from the instrument.

**AI BRIDGE CONTRACT**

- The AI receives a declared experiment ID and protocol version.

- The AI receives units with every variable.

- The AI is told which fields are measured, calculated, simulated, or
  externally sourced.

- The AI is asked to list assumptions before explaining results.

- When a claim conflicts with data, the system preserves both rather
  than silently rewriting the record.

**Appendix C – AI scientific-reasoning rubric**

| **Dimension**                | **What to look for**                                                                                 | **Score** |
|------------------------------|------------------------------------------------------------------------------------------------------|-----------|
| **Premise checking**         | Does it notice changed mass, concentration basis, hydrate state, sensor limits, or missing controls? | 0 1 2 3   |
| **Physical model**           | Is the explanation compatible with thermodynamics/chemistry at the level being taught?               | 0 1 2 3   |
| **Quantitative consistency** | Are units, signs, magnitudes, and conservation laws respected?                                       | 0 1 2 3   |
| **Uncertainty**              | Does it distinguish what the data show from what the model assumes?                                  | 0 1 2 3   |
| **Falsifiability**           | Can it state an observation that would count against its explanation?                                | 0 1 2 3   |
| **Revision**                 | When corrected, does it update the model explicitly rather than merely paraphrasing the correction?  | 0 1 2 3   |

|                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CORE CLAIM** The AI is not the subject being taught and is not merely automating the laboratory. It is an additional reasoning participant whose ability to detect questionable assumptions can itself be experimentally examined. |

**Appendix D – Documentation and product system**

**PERMANENT EXPERIMENT IDs**

Use OCC-00 through OCC-19 as stable identifiers. Titles can improve; IDs
should not. Every dataset, student sheet, teacher guide, code file, and
assessment points back to the same ID.

**RECOMMENDED FOLDER STRUCTURE**

/One-Cup-Chemistry/

/OCC-03-Salt-Cooling/

OCC-03-Teacher-Guide.pdf

OCC-03-Student-Lab.pdf

OCC-03-Arduino.ino

OCC-03-Logger.py

OCC-03-AI-Prompt.md

/sample-data/

/figures/

/safety/

/common/

data-schema.md

safety-rules.pdf

mfs-pin-map.pdf

ai-rubric.pdf

**SPIRAL-BINDING SPECIFICATION**

- US Letter, portrait.

- Extra inside/left margin for coil punch.

- Each experiment begins on a fresh page and occupies a predictable
  two-page guide spread.

- Teacher can photocopy a single guide without dismantling the
  conceptual sequence.

- Durable cover stock and tab dividers recommended for Measurement,
  Matter, Energy, Structure, Reactions, Analysis, Biology, AI.

**WHAT TO SELL**

- Core book alone - works with classroom basics.

- Book + One Cup physical kit.

- Book + UNO/MFS data kit.

- Full SDL edition - logger/dashboard/AI bridge and curated digital
  structure files.

- School license - editable worksheets, datasets, teacher slides, and
  professional development.

**Appendix E – Source and resource shelf**

**Arduino UNO R3 official hardware page**

https://docs.arduino.cc/hardware/uno-rev3

**Common Arduino Multi-Function Shield tutorial and pin mapping**

https://arduinogetstarted.com/tutorials/arduino-multi-function-shield

**OpenMX Viewer - browser crystal/CIF viewer**

https://www.openmx-square.org/viewer/

**Crystallography Open Database**

https://www.crystallography.net/cod/

**MgCl₂·6H₂O structure used in this curriculum**

COD 9011352

**Thermo Fisher - PCR component considerations and Mg²⁺ role**
