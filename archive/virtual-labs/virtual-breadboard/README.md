# Virtual Breadboard Thermal Control Lab

**Recovered lineage:** v2.2 runnable browser simulator + v2.3 interface/programmer documentation  
**Estate status:** recovered, documented, runnable source located in Library; canonical GitHub preservation in progress  
**Curricular role:** CORE 10 / thermal systems / fidelity mirrors / control / executable transparency

## What this laboratory is

The Virtual Breadboard Thermal Control Lab is a deliberately transparent browser laboratory that makes one first-order physical relationship visible in several mutually reinforcing forms.

The central chain is:

**thermal phenomenon → electrical RC analog → firmware measurement/control → mathematical model → live residual → feedback behavior**

The simulator is not intended to be a photorealistic breadboard game. It exposes the causal structure of the system so the learner can trace what the program reads, what it computes, what it commands, and what the plant does in response.

## Surviving runnable artifact

The recovered runnable file is:

`virtual_breadboard_thermal_lab_v2_2.html`

The file is a self-contained browser application. The surviving v2.3 Programmer’s Guide still instructs the learner to open that v2.2 HTML file, while describing v2.3 as a compact-workspace/interface revision. This is important provenance: the estate should not invent a nonexistent `v2_3.html` merely because the documentation carries v2.3 branding.

## v2.3 interface revision

The v2.3 documentation preserves four compact workspaces:

1. **Breadboard** — virtual MCU, programmer, PWM/MOSFET heater interface, thermal RC network, ADC feedback, and live meters.
2. **Program + Diagnose** — source editor, compile/run controls, watches, syntax highlighting, diagnostics, and source-line navigation.
3. **Scope + Data** — oscilloscope-style trace, samples, and export.
4. **Plant + Model** — RC/thermal parameters, abstraction boundary, and model configuration.

Keyboard navigation documented for the interface is `Alt+1` through `Alt+4`.

## Transfer-first programming model

The laboratory intentionally does **not** give firmware a privileged `READTEMP` or `HEATER` command. The learner must perform the same information path used on real hardware:

- read **A0**,
- convert ADC count to voltage,
- convert voltage to temperature,
- calculate a control decision,
- write PWM on **D9**,
- observe the plant response.

The browser interpreter supports deliberately small teaching subsets of Arduino-style C++ and CircuitPython. The point is transfer of structure to real hardware, not emulation of every language feature.

## Electrical/thermal correspondence

| Thermal idea | Electrical analog | Firmware view |
|---|---|---|
| Temperature state | `VTHERM` node voltage | ADC reading converted to volts and temperature |
| Thermal storage | `Cthermal` | state evolves over time |
| Heat loss | `Rloss` toward `VAMB` | visible through plant response |
| Ambient temperature | `VAMB` reference | boundary condition |
| Heater power / flux | PWM-controlled current source | D9 PWM duty |
| Sensor | ADC connected to `VTHERM` | A0 read |
| Controller | MCU program | arithmetic, decisions, timing |

The preserved model is first-order storage plus loss. In the documentation it is expressed in the form

`C · dV/dt = Iheater − (V − Vambient) / Rloss`

with the corresponding time constant

`tau = Rloss · Cthermal`.

## Fidelity-mirror role

This project is one of the clearest implementations of the estate’s multiple-representation strategy. The same relationship can be encountered as:

- a physical cooling/heating process,
- an electrical RC system,
- a differential equation,
- executable firmware,
- a browser simulation,
- measured versus modeled traces,
- a feedback-control problem.

The representations are not substitutes for one another. They are mirrors used to reveal what stays invariant when the embodiment changes.

## Educational IDE

The v2.2/v2.3 line includes:

- synchronized line numbers,
- syntax highlighting,
- execution-line highlighting,
- find/replace,
- indentation support,
- beginner API completion,
- live variable and pin watches,
- clickable diagnostics,
- code-to-breadboard tracing.

The tracing contract is especially important:

- `analogRead(A0)` / `sensor.value` illuminates A0, the ADC feedback path, and `VTHERM`.
- `analogWrite(D9, ...)` / `duty_cycle` illuminates D9, the PWM/gate path, MOSFET, and heater-current source.
- `Serial.println(...)` / `print(...)` illuminates the serial/programmer path.

The editor and breadboard are intended to tell the same causal story.

## Diagnostic philosophy

Diagnostics do **not** silently rewrite source. They identify likely errors, explain why the behavior is suspicious, and point the learner to the relevant source line. The learner remains responsible for the repair.

A recommended debugging sequence preserved in the guide is:

`ADC → voltage → temperature → error/decision → PWM`

The first implausible value usually identifies the layer where the mistake entered.

The system also includes behavior diagnostics for programs that compile correctly but act nonsensically—for example, heater logic reversed relative to the setpoint.

## Control progression

The simulator supports a natural progression:

1. fixed/open-loop PWM,
2. thermostat / bang-bang control with hysteresis,
3. proportional control,
4. model-versus-measurement comparison,
5. parameter changes and residual interpretation.

Hysteresis is treated as intentional memory rather than merely an implementation trick. Proportional control introduces gain, saturation, and steady-state error.

## Evidence and export

The surviving simulator/documentation supports export of:

- source code,
- complete CSV data logs,
- session JSON.

This makes the simulator consistent with the wider estate rule that an experiment should leave behind evidence that can be reopened, replotted, criticized, and reused.

## Real-hardware transfer

The teaching model can be rehearsed in Arduino or CircuitPython form. The documentation explicitly warns that real 3.3 V boards must respect their actual ADC and logic limits rather than blindly inheriting a 5 V Arduino-style reference.

This is a simulation for understanding and rehearsal, not an excuse to erase hardware reality.

## Historical naming

Some source documents refer to **CORE 12**. They are retained as historical lineage. The current canonical curriculum root is **CORE 10**.

## Recovery boundary

Recovered and verified:

- `virtual_breadboard_thermal_lab_v2_2.html` — actual runnable simulator located in the Library.
- `README_virtual_breadboard_v2_2.txt`.
- `README_virtual_breadboard_v2_3.txt`.
- `Virtual_Breadboard_Thermal_Control_Lab_Programmers_Guide_v2_3.pdf` and DOCX.
- earlier v2.1/v2.2 guides.

The v2.3 guide itself names the v2.2 HTML for first-run use. Until contrary evidence is recovered, the estate therefore treats the v2.2 HTML as the surviving runnable artifact for the v2.3 documented interface lineage rather than fabricating a separate v2.3 executable.

## Durable idea

The durable contribution is larger than this particular HTML file:

> A learner should be able to see the same dynamic relationship as physical behavior, circuit behavior, code, mathematics, model prediction, residual error, and feedback action—and be able to move among those representations without losing contact with measurement.

That principle belongs to CORE 10 even if every current browser or microcontroller implementation eventually disappears.
