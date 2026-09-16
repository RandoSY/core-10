# One Cup Chemistry — Teacher Manual v0.2

## OCC-17 Revised Canonical Map

**Recovery provenance:** derived from the current selected estate source `One_Cup_Chemistry_Teacher_Manual_v0_2(2).docx`, 56 pages, recovered from the Intellectual Estate Library on 16 September 2026.  
**Status:** canonical searchable handoff of the curriculum engine, experiment sequence, evidence/data architecture, safety structure, AI reasoning rubric, and implementation principles.  
**Tag line:** **How far can one cup take you?**

> Keep the physical system simple. Increase the sophistication of the question.

## Core proposition

A chemistry course should feel like one investigation getting deeper, not a succession of unrelated chapters.

One Cup Chemistry uses a common low-cost physical system and a stable evidence trail to move from ordinary measurement into thermochemistry, solutions, amount of substance, ions, phase behavior, crystal structure, reactions, kinetics, optical measurement, molecular scale, biology, and finally critique of scientific reasoning itself.

The course does **not** claim that every chemical phenomenon literally occurs in one cup. Its claim is that one sufficiently examined physical system can provide a coherent road through a large fraction of introductory chemistry.

## Governing rules

1. **Measure first.**
2. **Explain second.**
3. **Challenge the explanation third.**

Two broader estate rules govern implementation:

- **Experience Before Equation:** the phenomenon earns the mathematics.
- **Need Before Technology:** instrumentation arrives only when it solves a real measurement, timing, resolution, repeatability, or data-volume problem.

Physical evidence remains authoritative. AI is treated as a scientific reasoner whose claims can be audited, not as decorative automation or an oracle.

## Curriculum engine

The sequence grows by asking a new question of the same evidence system.

1. **Measure** — mass, volume, temperature.
2. **Heat** — Newton cooling, heat capacity.
3. **Dissolve** — NaCl, CaCl₂, MgCl₂.
4. **Count** — moles, concentration, ions.
5. **Conduct** — electrolytes, charge, mobility.
6. **Change phase** — freezing, saturation, crystals.
7. **See structure** — hydrates, lattice, diffraction.
8. **React** — acid-base, precipitation, redox.
9. **Measure rates** — kinetics, catalysis.
10. **Use light** — spectroscopy, Beer-Lambert.
11. **Measure a molecule** — monolayer geometry and Avogadro's number.
12. **Cross to life** — Mg²⁺, ATP, DNA/RNA, enzymes.
13. **Challenge reasoning** — AI predictions, assumptions and evidence.

Every guide ends with the question that creates the next guide. Narrative continuity is therefore part of the curriculum architecture, not merely a presentation style.

## Stable experiment IDs

The manual explicitly treats `OCC-00` through `OCC-19` as permanent IDs. Titles may improve; IDs should remain stable so datasets, student sheets, teacher guides, code, prompts and assessments continue to refer to the same intellectual object.

| ID | Experiment | Driving question |
|---|---|---|
| OCC-00 | Measure Like a Chemist | Can two careful people measure the same thing and disagree? |
| OCC-01 | Water as the First Standard | How close is 1 mL of water to 1 g in our room? |
| OCC-02 | Newton Cooling | What shape does a cooling curve have? |
| OCC-03 | Salt Changes the Curve | Does salt water cool differently from pure water? |
| OCC-04 | The Heat-Capacity Trap | What does a fair comparison actually hold constant? |
| OCC-05 | Heat of Dissolution | Why can adding a solid make water warmer or cooler? |
| OCC-06 | Grams Are Not Moles | What does “the same amount” mean at the particle level? |
| OCC-07 | Conductivity Reveals Ions | Why does salt water conduct while sugar water does not? |
| OCC-08 | Freezing and Deicing | Why does road salt work? |
| OCC-09 | From Saturated Solution to Crystal | How does an invisible solute become a visible crystal? |
| OCC-10 | Water Inside a Solid: Hydrates | How can a solid crystal contain chemically organized water? |
| OCC-11 | See the Lattice: Diffraction | How can a pattern of spots or peaks reveal an atomic lattice? |
| OCC-12 | Acid and Base in the Cup | Can color reveal hydrogen-ion chemistry? |
| OCC-13 | Make a Solid from Two Clear Solutions | Where did the precipitate come from? |
| OCC-14 | Redox and Corrosion | Can a cup of salt water reveal electron transfer? |
| OCC-15 | Rates and Catalysis | What changes how fast chemistry happens? |
| OCC-16 | Light Becomes Concentration | Can a beam of light tell us how much solute is present? |
| OCC-17 | Measuring a Molecule: Avogadro's Number from a Soap Film | Can a film one molecule thick let us count Avogadro's number? |
| OCC-18 | From Ice Melt to Living Molecules | Why does biology care about hydrated Mg²⁺? |
| OCC-19 | Can the Reasoner Find the Flaw? | How intelligent is an AI when the experimental premise itself is wrong? |

## Standard two-page experiment structure

### Page A — DO THE SCIENCE

Each experiment begins with:

- driving question;
- learning targets;
- materials and preparation;
- safety band and special cautions;
- numbered procedure;
- **Kitchen Table Mode**, using the minimum apparatus needed to answer the question.

### Page B — MAKE MEANING

Only after observation does the guide add:

- theory;
- expected observations;
- analysis prompts;
- reasoning trap or misconception;
- UNO/MFS Instrumented Mode;
- AI Reasoning Challenge;
- the question that generates the next experiment.

This structure operationalizes Experience Before Equation.

## Evidence vocabulary

The teacher documentation standard keeps different kinds of claims visibly distinct:

- **Raw data:** exactly what an instrument reported.
- **Calculated data:** values produced from raw data by an explicit equation or transform.
- **Inferred result:** interpretation supported by data plus a model.
- **Simulated result:** output of a computational model; not a measurement.
- **External evidence:** literature, database, SDS, crystallographic file, or another outside source.

By the later experiments, a learner should be able to trace a claim from a physical measurement to a molecular model without confusing observation with inference.

## Core kit principle

Start cheap and add only what the question demands.

The minimum system centers on:

- one clear 250–400 mL vessel or equivalent;
- 0.1 g balance;
- graduated cylinder plus syringes;
- digital temperature probe;
- phone or UNO timer;
- droppers/pipettes and stirring tools;
- simple visible LED plus photodetector for optics;
- low-voltage conductivity capability and multimeter;
- pH paper before an electronic pH module;
- ordinary laboratory PPE and labeling discipline.

Commercial materials such as deicers are legitimate experimental materials when brand, ingredient statement, purity and SDS are part of the record. Product variability becomes evidence rather than a nuisance to hide.

## Digital bench — UNO + Multi-Function Shield

The UNO/MFS is a reusable local console, not a requirement for every experiment.

Typical local controls are:

- S1 — start/stop a run;
- S2 — insert event marker;
- S3 — change mode or sample rate;
- display — temperature, pH, conductivity or elapsed time;
- LEDs — running/stable/warning/host-link states;
- buzzer — start, accepted event or threshold indication.

### Host connection

USB serial is the default because it is deterministic, cheap, inspectable and easy to debug. Wireless networking is added only when the science requires it.

The intended data path is:

`CUP → SENSOR → UNO + MFS → USB SERIAL → PC + AI`

Physical data remain primary. AI reasons over evidence rather than replacing observation.

## Human-readable data spine

The protocol is deliberately boring: newline-terminated, comma-separated, human-readable ASCII.

A representative sequence is conceptually:

```text
META,OCC-05,RUN=3,SALT=CaCl2,MASS_WATER_G=100.0,MASS_SALT_G=15.0
T,0,22.84
T,1000,24.11
MARK,5230,SALT_ADDED
T,6000,31.72
```

The reason for simplicity is durability: a student, spreadsheet, Python program or AI system can all inspect the same evidence without a hidden binary protocol.

### Data-integrity rules

- Never overwrite raw data.
- Derived columns live in a separate analysis layer.
- Every run carries experiment ID, sample ID, date/time, sensor ID, units and controlled variables.
- Event markers remain in the same stream as measurements.
- Calibration information is versioned with the data.
- AI receives raw data or an explicitly labeled processed dataset, never an unlabeled mixture.

The minimal Python logger in the manual preserves the **raw incoming line** specifically because parser mistakes can be repaired later if original evidence survives.

## Bring-up order

The manual's engineering rule is to prove one link at a time:

1. verify the sensor locally;
2. verify readable serial output;
3. log the same stream from Python;
4. plot it live;
5. add metadata and event markers;
6. only then connect the stream to the AI/MCP layer.

A sophisticated architecture is still a chain of testable links.

## Safety architecture

Low cost does not mean informal safety.

The manual distinguishes three operational bands:

- **GREEN:** ordinary low-hazard materials such as water, NaCl, sucrose, food color, dilute vinegar/baking soda, and the controlled monolayer materials. Standard goggles and lab hygiene; no tasting.
- **YELLOW:** warm water, deicer salts, 3% H₂O₂, concentrated brines and low-voltage electrochemistry. Additional PPE/SDS/disposal review as appropriate.
- **TEACHER CONTROLLED:** stronger acids/bases, specialty salts, heating/dehydration and advanced electrochemistry under institutional procedures and supervision.

Absolute rule: **nothing that enters the laboratory workflow is tasted, consumed, or returned to food use**, even if it began as a food-grade material.

Electrical work at the cup is low-voltage and current-limited. Mains-connected electrodes are excluded. Passive galvanic measurement is preferred over core electrolysis activities.

## Scientific progression and reasoning traps

The sequence deliberately uses traps where superficially fluent reasoning can fail.

### OCC-00 / 01 — measurement before chemistry

Learners separate resolution, precision, accuracy and repeatability, then use water density as a practical multi-point calibration relationship. “1 g = 1 mL” is treated as a useful room-temperature approximation rather than an exact identity.

### OCC-02 — Newton cooling

Learners encounter the curve before the law. A good exponential fit is not treated as proof of a complete mechanism; convection, evaporation, radiation, vessel heat capacity and airflow remain possible contributors.

### OCC-03 / 04 — the heat-capacity trap

Adding salt changes both properties and total mass. The naive statement “lower specific heat means it cools faster” is therefore not enough. `Q = mcΔT` requires attention to both `m` and `c`.

OCC-04 makes “fair test” explicit: equal water mass and equal total solution mass answer different questions. “Control all variables” is rejected as a meaningless slogan; controls must correspond to the hypothesis.

### OCC-05 / 06 — heat of dissolution and amount of substance

Dissolution heating/cooling is separated from the later cooling curve. Equal grams of NaCl, CaCl₂ and hydrated MgCl₂ are not chemically equal, which creates the need for molar mass, moles and explicit hydrate accounting.

### OCC-07 / 08 — ions, conductivity and deicing

Dissolved does not mean ionized. Conductivity depends on concentration, charge, mobility, geometry and temperature. Deicing performance is not reduced to freezing point alone; dissolution heat, concentration, surface condition and formulation matter.

### OCC-09 / 10 / 11 — crystals to structure

Crystallization makes an invisible solute visible but crystal habit is not a magnified photograph of a molecule. Hydrate dot notation carries stoichiometric/structural meaning. Diffraction is not a photograph of atoms; structure is inferred from periodic scattering plus a model.

### OCC-12 / 13 / 14 — solution reactions

Indicator color is evidence of an indicator equilibrium, not a direct particle counter. Precipitation is a phase change with atom/charge conservation, not disappearance. A galvanic voltage does not by itself identify every surface reaction.

### OCC-15 — rates and catalysis

Rate metrics must be chosen before the result where possible. Foam height in a peroxide/catalase activity is acknowledged as a proxy influenced by bubble/surfactant stability, not a direct oxygen measurement.

### OCC-16 — light becomes concentration

A calibration curve turns an indirect optical signal into a quantitative proxy. Linearity is valid only over the demonstrated range; a visually straight line is not permission to extrapolate indefinitely.

### OCC-17 — measuring a molecule

The revised activity uses an oleic-acid monolayer on water. Measured film geometry plus known dilution and molecular-volume assumptions are used to estimate molecular length and then Avogadro-scale particle count.

The educational value is deliberately order-of-magnitude reasoning, not artificial precision. The calculation depends on simplifying assumptions such as monolayer formation and approximate molecular geometry, and learners must state those assumptions explicitly.

### OCC-18 — crossing to biology

Hydrated Mg²⁺ is followed conceptually from a salt/hydrate environment into Mg-ATP, enzymes and nucleic-acid chemistry using external biochemical evidence. The manual explicitly warns that conceptual continuity does not make deicer-grade material suitable for biological use.

Learners tag each link as observed, calculated, simulated or literature-supported.

### OCC-19 — can the reasoner find the flaw?

The final experiment makes scientific reasoning itself testable. The AI is given prior protocols and datasets containing tempting assumptions and is evaluated on whether it notices defects before being prompted.

The point is not to catch an AI making mistakes. The point is to distinguish fluent completion from disciplined scientific reasoning.

The sequence then loops back to OCC-00: measurement, evidence, uncertainty and inference.

## AI scientific-reasoning rubric

The manual evaluates an AI on six dimensions, each scored 0–3:

1. **Premise checking** — detects changed mass, concentration basis, hydrate state, sensor limits or missing controls.
2. **Physical model** — explanation is compatible with chemistry/thermodynamics at the intended level.
3. **Quantitative consistency** — units, signs, magnitudes and conservation laws are respected.
4. **Uncertainty** — distinguishes what data show from what the model assumes.
5. **Falsifiability** — names an observation that would count against its explanation.
6. **Revision** — explicitly updates the model after correction rather than merely paraphrasing the correction.

Core claim: AI is neither the subject being taught nor merely an automation layer. It is an additional reasoning participant whose assumption-checking can itself be experimentally examined.

## AI bridge contract

When AI is introduced, it should receive:

- declared experiment ID and protocol version;
- units for every variable;
- explicit labels for measured, calculated, simulated and externally sourced fields;
- a requirement to state assumptions before interpreting results.

When AI claims conflict with data, preserve both rather than silently rewriting the experimental record.

## Product and documentation system

Recommended stable package structure is organized by permanent OCC ID, with teacher guide, student lab, Arduino source, logger, AI prompt, sample data, figures and safety material under the same experiment identity.

The manual envisages several transmission formats:

- core book using classroom basics;
- book + physical One Cup kit;
- book + UNO/MFS data kit;
- full SDL edition with logger/dashboard/AI bridge and curated digital structure files;
- editable school materials and professional development.

This is not merely commercialization structure; it is a handoff architecture that keeps experiment identity, evidence, source and teaching materials aligned.

## End state

One Cup Chemistry is a chemistry laboratory that grows by asking better questions:

**Start with water. Measure it. Heat it. Salt it. Count the ions. Grow the crystal. See the lattice. Make it conduct. Make it react. Use light to measure it. Measure a molecule. Follow magnesium into ATP and DNA. Then ask whether the AI understood what actually happened.**

**ONE CUP. ONE EVIDENCE TRAIL. A VERY LARGE PART OF CHEMISTRY.**
