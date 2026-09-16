# Kitchen Inquiry Lab — Canonical Map

**Source lineage:** `Kitchen-Inquiry-Lab.docx` (V1 Measurement-First Architecture) plus `Kitchen-Inquiry-Lab-SixLabs.docx` (Six-Lab Learning Trajectory), recovered from the Intellectual Estate Library on 16 September 2026.  
**Canonical placement:** sibling branch under CORE 10.  
**Governing phrase:** **Seeing the unsee-able through measurement.**

## Central proposition

The kitchen is a precision laboratory hiding in ordinary life.

- an appliance is a power/energy system waiting to be measured;
- a cup of water is a calorimetric system;
- a cooling mug contains a time-dependent thermal model;
- a measuring cup makes a calibration claim;
- an electric bill turns physical energy into household economics.

The program is measurement-first: before a number is used in a model, the learner asks whether the instrument, scale, condition log and procedure make the number trustworthy enough for the decision.

## Core instrument stack

The V1 architecture uses five ordinary instruments rather than specialized laboratory infrastructure:

1. **eThermometer** — approximately 0.1 °C resolution probe/instant-read thermometer.
2. **eScale** — digital kitchen scale, ideally 0.1 g resolution.
3. **eMeasuring Cup** — transparent graduated vessel with mL/cup scale.
4. **WattMinder** — plug-in electrical energy monitor reporting watts, kWh, voltage/current/power factor where available.
5. **eTimer** — simple timer/stopwatch.

The important idea is not the named products. The enduring measurement functions are temperature, mass, volume, electrical power/energy and time.

## V1 progression

### Tier 0 — Orientation: measurement discipline and calibration

**Goal:** establish tare, calibration, condition logging and unit literacy before downstream experiments depend on the instruments.

Experiments:

- 0.1 Scale Repeatability & Tare Discipline
- 0.2 Measuring Cup Calibration
- 0.3 Thermometer Validation

Core distinction set:

- Energy ≠ Power
- Repeatability ≠ Accuracy
- Calibration ≠ Zeroing
- Measurement ≠ Device
- Model ≠ Result

Mass-first rule: for ordinary water work, use `1 g ≈ 1 mL ≈ 1 cm³` as a practical approximation under stated conditions, and test printed volume markings rather than assuming them.

### Tier 1 — Foundations: density, mixing and temperature

**Goal:** connect mass, volume and density, then use measured mass and temperature to predict thermal mixing.

Experiments:

- 1.1 Water Density Baseline
- 1.2 Solution Density
- 1.3 Thermal Mixing

The intended mastery is prediction before measurement, followed by inspection of the gap between ideal prediction and real result.

### Tier 2 — Models: cooling curves and parameter estimation

**Goal:** capture `T(t)`, fit an exponential cooling model and extract a time constant `τ`.

Experiments:

- 2.1 Newton's Cooling
- 2.2 Variable Comparison
- 2.3 Colorimetry

Cooling is used to move from time series to a fitted physical model. Subtract ambient and inspect `ln(ΔT)` versus time; if the Newtonian model is adequate, the slope estimates `-1/τ`.

### Tier 3 — Applied: energy economics and appliance benchmarking

**Goal:** distinguish watts from kWh, connect electrical input to useful thermal output, and express energy use in money.

V1 experiments:

- 3.1 Kettle vs Microwave vs Hot Plate
- 3.2 Phantom Loads
- 3.3 Thermal Efficiency

This tier is where household energy ceases to be an abstract unit. A learner measures appliance power, duration, accumulated electrical energy, useful thermal change and cost.

### Tier 4 — Integration capstone

**Goal:** measure mass, temperature, time and electrical energy in one reproducible run.

Experiments:

- 4.1 True Cost of Boiling 500 mL
- 4.2 Open Design Investigation

The completion test is not merely a numerical answer; it is a complete state/evidence snapshot that another person can independently reproduce.

## Canonical microwave-energy requirement

**Current estate rule:** Microwave Water Heating is a required, first-class Kitchen Inquiry Lab experiment. It is not an optional extension.

Its complete reasoning chain is:

`joules → watts → watt-hours → kilowatt-hours → dollars`

A canonical microwave run should measure or establish:

- water mass;
- initial and final water temperature;
- elapsed heating time;
- appliance electrical input power and/or measured Wh/kWh;
- local electricity cost basis.

Useful thermal energy is estimated separately from electrical input:

`Q_useful = m c ΔT`

Electrical input energy comes from the WattMinder or a defensible power × time measurement.

These quantities **must not be conflated**. Their difference creates the efficiency/system-boundary question.

The electricity-cost study should also use a real electric bill when available. Learners should identify:

- billed kWh;
- energy charges;
- fixed charges;
- riders/taxes or other listed charges;
- effective all-in cost per kWh where that comparison is appropriate.

Then they estimate the actual cost of the microwave heating event.

This preserves the practical question: not only “how much energy entered the water?” but “how much electrical energy did the household buy, what did it cost, and how much produced the intended thermal result?”

## Six-Lab Learning Trajectory

The compact six-lab edition provides a memorable path:

`validate → calibrate/isolate → model → account → calibrate proxy → decide`

Its six activities are:

1. **Measurement Boot Camp — Trust, Repeatability & Claims**
2. **Density Bridge — Mass–Volume Calibration with Water**
3. **Newton's Cooling — Time Constant & Semi-log Linearisation**
4. **Mixing & Energy Accounting — Predict vs Measure**
5. **Concentration from Light — DIY Colorimeter & Standard Curve**
6. **Watts → kWh → $ — Phantom Loads & Household Energy Audit**

A recurring maxim is:

> **The gap is the finding.**

A discrepancy between prediction and measurement is not automatically failure; it is often the evidence that exposes a neglected boundary, bias, loss mechanism, geometry effect or condition.

## Lab 1 — Measurement Boot Camp

The learner validates instruments before trusting them and labels anomalies as:

- random scatter;
- systematic bias;
- procedural blunder.

Typical checks include repeated weighing, mass-versus-volume water checks and ice-slurry thermometer validation.

The aim is the habit: **instrument markings are claims**. Repeatability and bias checks turn those claims into evidence.

## Lab 2 — Density Bridge

Water mass becomes a reference against which container graduations are tested.

Rather than trusting one ratio, the learner collects multiple mass/volume pairs and fits:

`mass = a(volume) + b`

The slope reveals the mass-volume relationship; the intercept can expose tare/zero bias. The fitted model is more informative than a single reading.

## Lab 3 — Newton's Cooling

The learner records ambient temperature and a cooling time series, then examines:

`T(t) = T∞ + ΔT₀ e^(-t/τ)`

and the transformed relation:

`ln(ΔT) = mt + c`, where `τ = -1/m`.

The model becomes a tool for comparing vessels, lids, volume, stirring and other controlled changes. Disturbances and probe placement are logged rather than hidden.

## Lab 4 — Mixing and energy accounting

For equal-specific-heat water portions, the ideal prediction is a mass-weighted average:

`T_pred = (m_hot T_hot + m_cold T_cold) / (m_hot + m_cold)`

The measured mixture temperature usually differs from the idealized result because the cup, air, evaporation and measurement delay participate in the real energy balance.

The instructional move is to investigate the gap rather than force agreement.

## Lab 5 — Colorimetry as calibrated proxy

Tea/dye solutions and a fixed optical geometry are used to teach that a sensor reading has no intrinsic chemical meaning until calibration connects it to concentration.

The crucial design idea is:

> **Geometry is part of the instrument.**

Cup type, fill height, light source, detector position, optical path and camera exposure can all create systematic effects.

A simple calibration relationship is preferred to an unnecessarily elaborate model; transformations such as absorbance or logarithmic/inverse response are introduced only when evidence requires them.

## Lab 6 — Watts → kWh → dollars

Power is a rate; energy is accumulated power over time.

For a roughly constant load:

`kWh = watts × hours / 1000`

The learner measures standby and active loads, estimates use duration, calculates daily/monthly energy and converts the result to cost.

The purpose is decision-making from measured evidence: a learner can rank devices, examine cycling loads, test interventions and estimate savings rather than rely on intuition about what “uses a lot of electricity.”

This compact lab complements—not replaces—the required microwave water-heating/electric-bill sequence above.

## State snapshot / cold-restart principle

The V1 architecture ends with a state snapshot containing at least:

- curriculum/lab version;
- date;
- confirmed instruments;
- calibration status;
- ambient temperature and relevant environment;
- current experiment;
- last dataset identity;
- key results;
- known quirks/issues;
- next step and setup notes.

The criterion is explicit: the snapshot should permit a **full cold restart**.

That principle is larger than this curriculum. It is publication-as-handoff applied at the experiment level.

## Relationship to CORE 10 and sibling branches

Kitchen Inquiry Lab owns the physics and economics of ordinary household processes. It can reuse CORE 10 measurement skills without reteaching them from zero.

Its measured records are intentionally reusable elsewhere:

- One Cup Chemistry may reuse water/brine thermal records for solution questions.
- NOTHING IS FREE may reuse electrical/thermal records for energy accounting and storage burden.
- Personal Energy Laboratory may reuse appliance loads and hot-water demand in finite-energy planning.

This follows the CANONICAL / REVISIT / SYNTHESIS architecture: one physical measurement can have several later intellectual lives without needless repetition.

## Enduring idea

Kitchen Inquiry Lab is not “science with kitchen objects” as a novelty. It is a deliberate attempt to make scientific literacy operational in the environment where people actually consume energy, heat water, cool food, prepare matter, use appliances and pay bills.

**Measure ordinary life well enough that it becomes explainable, comparable and actionable.**
