# One Cup Chemistry v0.2 — Complete Teacher Experiment Compendium OCC-00 through OCC-19

This preserved source-text compilation combines the twenty complete teacher experiment sections from the eight-part [Teacher Manual v0.2](https://github.com/RandoSY/core-10/tree/main/one-cup-chemistry/archive/Teacher_Manual_v0.2). It deliberately does not claim visual identity with the illustrated original PDF or independent laboratory verification. The original eight parts, appendices and the branded PDF bundle remain separate preservation assets.

**Provenance:** faithful ordered extraction from the published Markdown archival edition; no experiment was removed or rewritten.

---

**OCC-00 Measure Like a Chemist**

*Can two careful people measure the same thing and disagree?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Distinguish resolution, precision, accuracy, and repeatability.

- Record raw data before calculating derived quantities.

- Estimate measurement uncertainty honestly.

**MATERIALS**

- Cup

- 0.1 g balance

- 100-250 mL graduated cylinder or syringe

- thermometer

- timer

- distilled water

**SAFETY**

Low hazard. Keep electronics dry and wipe spills promptly.

**PROCEDURE**

1.  Zero/tare the balance with the empty cup.

2.  Add a nominal 100 mL water by cylinder; record actual indicated
    volume.

3.  Measure mass and temperature.

4.  Repeat five times, emptying/drying as needed.

5.  Compare class values and calculate mean, range, and optional
    standard deviation.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-00 Measure Like a Chemist**

*Can two careful people measure the same thing and disagree?*

**MAKE MEANING**

**THEORY**

- A measurement is a number plus a unit plus an uncertainty.

- Random variation broadens repeated values; systematic error shifts
  them together.

- Density later links mass and volume, but first treat each instrument
  as an independent witness.

**EXPECTED OBSERVATIONS**

- Small run-to-run differences are normal.

- Students often report more digits than the instrument supports.

**ANALYSIS**

- Graph mass vs. trial.

- Identify which instrument dominates uncertainty.

- Write one sentence separating observation from interpretation.

**REASONING TRAP**

*"The display says 100.0" does not mean the delivered amount is exactly
100.0 mL.*

**UNO/MFS INSTRUMENTED MODE**

MFS optional. Use buttons as event markers and the 4-digit display as a
timer. This establishes the console before chemistry sensors are added.

**AI REASONING CHALLENGE**

Ask AI to critique the data table for false precision and missing
metadata. Require it to identify what it cannot know from the numbers
alone.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*If mass and volume are both measurable, can water itself become a
calibration material?*

**OCC-01 Water as the First Standard**

*How close is 1 mL of water to 1 g in our room?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Determine water density experimentally.

- Use a slope rather than a single ratio.

- Connect a macroscopic property to a reproducible material.

**MATERIALS**

- Cup

- balance

- graduated cylinder/syringes

- distilled water

- thermometer

**SAFETY**

Low hazard; keep balance pan dry.

**PROCEDURE**

1.  Measure 25, 50, 75, 100, 125, and 150 mL portions into a tared cup.

2.  Record total mass and temperature for each.

3.  Plot mass vs. volume and fit a straight line.

4.  Interpret slope as density.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-01 Water as the First Standard**

*How close is 1 mL of water to 1 g in our room?*

**MAKE MEANING**

**THEORY**

- Density is ρ=m/V. For water near room temperature it is close to, but
  not exactly, 1 g/mL.

- A multi-point slope reduces the importance of a single reading error.

**EXPECTED OBSERVATIONS**

- Data should form an almost straight line through the origin.

- The slope should be close to 1 g/mL.

**ANALYSIS**

- Fit m=aV+b. Discuss the meaning of nonzero b.

- Compare individual ratios with the fitted slope.

**REASONING TRAP**

*"1 g = 1 mL" is a useful approximation, not an identity valid at every
temperature.*

**UNO/MFS INSTRUMENTED MODE**

UNO/MFS can display water temperature during the density series. Log
temperature so students can see that density claims always have
conditions.

**AI REASONING CHALLENGE**

Ask AI whether the intercept is evidence of "extra mass." Require at
least three mundane instrumental explanations before any exotic one.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Now that we can measure temperature and time, what does a cup of hot
water do while we simply watch it?*

**OCC-02 Newton Cooling**

*What shape does a cooling curve have?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Collect a time series.

- Recognize exponential approach to ambient temperature.

- Separate temperature from heat.

**MATERIALS**

- Cup

- 150-250 g warm water

- temperature probe

- timer

- room-temperature probe optional

- lid with probe hole optional

**SAFETY**

Use warm water rather than scalding water. Teacher sets a maximum
starting temperature appropriate to the room and vessel.

**PROCEDURE**

1.  Record room temperature.

2.  Prepare water at a convenient elevated temperature, e.g. 45-55°C.

3.  Start logging at fixed intervals for 15-30 min.

4.  Do not move, stir, or relocate the cup during the run unless
    stirring is a defined condition.

5.  Graph T vs. t and also T-Troom vs. t.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-02 Newton Cooling**

*What shape does a cooling curve have?*

**MAKE MEANING**

**THEORY**

- Newton's law of cooling models dT/dt=-k(T-Tenv).

- The model is empirical and approximate: convection, evaporation,
  radiation, vessel heat capacity, and airflow all matter.

**EXPECTED OBSERVATIONS**

- Cooling is fast at first and slows as the sample approaches room
  temperature.

**ANALYSIS**

- Estimate k by fitting T=Tenv+(T0-Tenv)e^(-kt).

- Compare two runs and discuss reproducibility.

**REASONING TRAP**

*An excellent mathematical fit does not prove the mechanism is
complete.*

**UNO/MFS INSTRUMENTED MODE**

Default instrumented mode: DS18B20 on MFS A4, 1 sample/s or slower, S1
start/stop, S2 mark a disturbance, display current °C, USB serial log.

**AI REASONING CHALLENGE**

Before giving the curve to AI, ask it to predict the qualitative shape
and list assumptions. Afterward, ask which assumptions the data cannot
test.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*What happens if we keep the same water but dissolve salt in it?*

**OCC-03 Salt Changes the Curve**

*Does salt water cool differently from pure water?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Prepare a reproducible NaCl solution.

- Compare two cooling curves under matched conditions.

- Identify variables unintentionally changed by adding solute.

**MATERIALS**

- Two identical cups

- 250 g water per trial

- NaCl (example 90 g for the deliberately naive condition)

- balance

- temperature logging

**SAFETY**

Ordinary NaCl is low hazard. Avoid ingestion because laboratory
materials are never food after entering the lab workflow.

**PROCEDURE**

1.  Run pure water as in OCC-02.

2.  Prepare the second cup with the same starting water mass plus
    measured NaCl.

3.  Dissolve completely; allow both samples to reach the same chosen
    starting temperature.

4.  Run the cooling protocol with identical cup geometry and probe
    depth.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-03 Salt Changes the Curve**

*Does salt water cool differently from pure water?*

**MAKE MEANING**

**THEORY**

- Salt changes solution properties including heat capacity, density,
  vapor pressure, and convection.

- But adding salt also changes total mass, so "lower specific heat"
  alone cannot predict total cooling behavior.

**EXPECTED OBSERVATIONS**

- The curve may differ, but the reason is not automatically identifiable
  from one comparison.

**ANALYSIS**

- Record total sample mass.

- Calculate concentration by mass.

- List all variables changed when salt was added.

**REASONING TRAP**

*The classic trap: comparing specific heat while ignoring m in Q=mcΔT.*

**UNO/MFS INSTRUMENTED MODE**

MFS produces identical time-stamped data format for water and brine. Use
a run ID in the host logger so files can be overlaid automatically.

**AI REASONING CHALLENGE**

Ask AI: “NaCl solution has lower specific heat than water. Which cools
faster?” Do not mention the mass change. Score whether AI discovers the
premise defect.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*How do we redesign the comparison so "fair" has an explicit meaning?*

**OCC-04 The Heat-Capacity Trap**

*What does a fair comparison actually hold constant?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Distinguish specific heat c from total heat capacity C=mc.

- Design equal-total-mass and equal-water-mass comparisons.

- Understand that experimental fairness depends on the question.

**MATERIALS**

- Identical cups

- water

- NaCl

- balance

- temperature logger

**SAFETY**

Low hazard; standard hot-water precautions.

**PROCEDURE**

1.  Design Condition A: equal starting water mass, then add salt.

2.  Design Condition B: equal total solution mass, with one sample pure
    water and one brine.

3.  Optionally design Condition C: equal moles of solvent.

4.  Run matched cooling curves from the same starting temperature.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-04 The Heat-Capacity Trap**

*What does a fair comparison actually hold constant?*

**MAKE MEANING**

**THEORY**

- Q=mcΔT. Lower c can be offset by larger m.

- There is no universal "fair test"; the controlled variables must
  correspond to the scientific question.

**EXPECTED OBSERVATIONS**

- Different control choices can legitimately produce different
  comparisons.

**ANALYSIS**

- Calculate approximate total thermal capacitance mc using reference
  specific heats if available.

- Explain which design answers which question.

**REASONING TRAP**

*"Control all variables" is impossible and often meaningless; control
the variables required by the hypothesis.*

**UNO/MFS INSTRUMENTED MODE**

Use MFS buttons to select condition A/B/C before each run; emit a header
line such as META,MODE,EQUAL_MASS to preserve context in the data file.

**AI REASONING CHALLENGE**

Ask AI to propose a "fair" test. Reject answers that do not state what
is held constant and why.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*If different salts are used, does "same amount of salt" mean same grams
or something else?*

**OCC-05 Heat of Dissolution**

*Why can adding a solid make water warmer or cooler?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Observe endothermic/exothermic dissolution.

- Separate preparation heat from later cooling.

- Compare NaCl, CaCl₂, and MgCl₂-based deicer materials.

**MATERIALS**

- Three small cups

- 100 g water each

- 10-20 g NaCl

- 10-20 g CaCl₂ ice-melt pellets

- 10-20 g MgCl₂ hydrate product if available

- balance

- temperature probe

**SAFETY**

Goggles required. CaCl₂ dissolution can become hot; add small portions
gradually to cool/room-temperature water and do not seal the vessel.
Follow each product SDS.

**PROCEDURE**

1.  Measure initial water temperature.

2.  Add one salt gradually while stirring; log temperature continuously.

3.  Repeat with fresh water for each salt and equalize the comparison
    basis.

4.  After the dissolution event, allow samples to return to the same
    starting temperature before any cooling comparison.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-05 Heat of Dissolution**

*Why can adding a solid make water warmer or cooler?*

**MAKE MEANING**

**THEORY**

- Dissolution has an enthalpy change arising from lattice disruption and
  hydration of ions.

- Commercial deicers may be hydrates or blends, so composition must be
  documented.

**EXPECTED OBSERVATIONS**

- CaCl₂ commonly produces a clear temperature rise; NaCl is much less
  dramatic under ordinary conditions. Hydrated MgCl₂ behavior depends on
  form and composition.

**ANALYSIS**

- Measure ΔT from pre-addition baseline to peak/minimum.

- Compare energy per gram cautiously; rigorous molar enthalpy requires
  heat-capacity corrections.

**REASONING TRAP**

*If you begin the cooling run immediately, you are mixing heat of
dissolution with cooling behavior.*

**UNO/MFS INSTRUMENTED MODE**

MFS shines here: 2-5 samples/s captures the transient; S2 marks the
instant of addition; buzzer confirms event marking without taking eyes
off the cup.

**AI REASONING CHALLENGE**

Ask AI to explain the transient. Require it to distinguish "the solution
is hotter" from "the solution cools more slowly."

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Equal grams of NaCl, CaCl₂, and MgCl₂ are not equal chemically. What is
the right counting unit?*

**OCC-06 Grams Are Not Moles**

*What does "the same amount" mean at the particle level?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Use molar mass to convert grams to amount of substance.

- Compare equal-mass and equal-mole preparations.

- Recognize waters of hydration in formula mass.

**MATERIALS**

- NaCl

- CaCl₂

- MgCl₂·6H₂O or labeled MgCl₂ hydrate

- balance

- calculator

- water

- cups

**SAFETY**

Use the same PPE required by the salts. Do not assume commercial deicer
purity; use label/SDS composition in calculations.

**PROCEDURE**

1.  Calculate molar masses from formulas.

2.  Determine moles in a fixed mass, e.g. 10.0 g.

3.  Prepare equal-mole samples where feasible.

4.  Record how much water of crystallization is carried by hydrated
    MgCl₂.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-06 Grams Are Not Moles**

*What does "the same amount" mean at the particle level?*

**MAKE MEANING**

**THEORY**

- n=m/M. A hydrate's formula mass includes its bound water.

- Equal grams can mean very different numbers of formula units and ions.

**EXPECTED OBSERVATIONS**

- MgCl₂·6H₂O devotes a large fraction of its mass to water of
  crystallization.

**ANALYSIS**

- Compare moles of cations, chloride ions, and total ions for each
  preparation.

- State which basis is appropriate for the next experiment.

**REASONING TRAP**

*Chemical formulas are counting statements, not just labels.*

**UNO/MFS INSTRUMENTED MODE**

UNO/MFS is mostly a timer/display here; the host app can calculate
recipe masses from a target molarity and display them before the run.

**AI REASONING CHALLENGE**

Ask AI to design "equal concentration" samples, then audit whether it
used solution volume, solvent mass, or final mass consistently.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*If these salts produce ions, can we detect the ions electrically?*

**OCC-07 Conductivity Reveals Ions**

*Why does salt water conduct while sugar water does not?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Distinguish dissolving from ion formation.

- Compare electrolytes and nonelectrolytes.

- Relate conductivity qualitatively to concentration and ion mobility.

**MATERIALS**

- Distilled water

- NaCl

- sucrose

- CaCl₂

- simple low-voltage conductivity probe or commercial module

- cups

**SAFETY**

Use only low-voltage sensor circuits. Do not use mains-connected
electrodes. Rinse probe between samples.

**PROCEDURE**

1.  Measure baseline distilled-water conductance.

2.  Prepare matched mass or molar solutions of sugar and salts.

3.  Measure each after rinsing the probe.

4.  Make a dilution series for one salt.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-07 Conductivity Reveals Ions**

*Why does salt water conduct while sugar water does not?*

**MAKE MEANING**

**THEORY**

- Ionic solids dissociate into mobile charge carriers; molecular solutes
  such as sucrose dissolve without producing comparable concentrations
  of ions.

- Conductivity depends on concentration, charge, mobility, geometry, and
  temperature.

**EXPECTED OBSERVATIONS**

- Salt solutions conduct strongly relative to distilled water and sugar
  solutions.

- Conductivity typically increases with concentration over a useful
  introductory range.

**ANALYSIS**

- Plot sensor response vs. concentration.

- Do not call the relationship universal unless calibrated for that
  probe and concentration range.

**REASONING TRAP**

*"Dissolved" and "ionized" are not synonyms.*

**UNO/MFS INSTRUMENTED MODE**

Analog conductivity module can use the free analog channel (often A5 on
common MFS revisions) or an external ADC. Log temperature too because
conductivity is temperature dependent.

**AI REASONING CHALLENGE**

Ask AI to predict the order of water, sugar, NaCl, CaCl₂. Then require a
mechanistic explanation in terms of mobile charge carriers.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*If ions change solution properties, why does salt melt ice?*

**OCC-08 Freezing and Deicing**

*Why does road salt work?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Observe freezing-point depression qualitatively.

- Connect deicing to colligative behavior and phase equilibrium.

- Compare deicer formulations.

**MATERIALS**

- Small sealed sample tubes or cups

- water

- NaCl brine

- CaCl₂ brine

- ice-salt bath or freezer

- temperature probes

**SAFETY**

Cold-burn risk from very cold baths. Use gloves/tongs as appropriate.
Keep glass out of student ice baths unless rated for thermal stress.

**PROCEDURE**

1.  Prepare water and two brines of documented composition.

2.  Cool under identical conditions while logging temperature.

3.  Observe onset of freezing/slush and temperature plateaus.

4.  Compare which sample remains liquid longest.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-08 Freezing and Deicing**

*Why does road salt work?*

**MAKE MEANING**

**THEORY**

- Dissolved particles lower the chemical potential of liquid water and
  depress the freezing point.

- The magnitude depends on particle concentration and non-ideal
  behavior; concentrated deicers are not ideal dilute solutions.

**EXPECTED OBSERVATIONS**

- Pure water freezes first under matched conditions; brines remain
  liquid to lower temperatures.

**ANALYSIS**

- Record concentration and approximate freezing onset.

- Discuss why CaCl₂ can be effective beyond NaCl under some conditions.

**REASONING TRAP**

*Deicing performance is not determined by freezing point alone;
dissolution heat, concentration, surface conditions, and practical
formulation matter.*

**UNO/MFS INSTRUMENTED MODE**

MFS can log one probe at a time; multiple samples can be run
sequentially or with a small external sensor multiplexer in advanced
mode.

**AI REASONING CHALLENGE**

Ask AI to rank deicers, then require it to list at least three
performance variables besides eutectic temperature.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*When concentrated solutions lose water, where do the ions go?*

**OCC-09 From Saturated Solution to Crystal**

*How does an invisible solute become a visible crystal?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Create saturated/supersaturated conditions.

- Observe nucleation and crystal growth.

- Relate solubility to temperature and evaporation.

**MATERIALS**

- NaCl or Epsom salt

- warm water

- cup

- balance

- evaporation dish or same cup

- thread/seed crystal optional

**SAFETY**

Use moderate water temperatures. Label solutions and keep them away from
food preparation areas.

**PROCEDURE**

1.  Make a near-saturated solution by adding solute until little more
    dissolves.

2.  Filter/decant undissolved solid if needed.

3.  Allow slow evaporation or controlled cooling.

4.  Photograph crystals daily and record mass/size changes.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-09 From Saturated Solution to Crystal**

*How does an invisible solute become a visible crystal?*

**MAKE MEANING**

**THEORY**

- At saturation, dissolved and solid phases are at equilibrium.
  Supersaturation permits nucleation; crystal growth then lowers
  supersaturation.

**EXPECTED OBSERVATIONS**

- Crystal habit depends on substance and growth conditions.

**ANALYSIS**

- Track mass loss from evaporation and crystal mass gained if separable.

- Compare slow vs. rapid growth conditions.

**REASONING TRAP**

*A crystal's macroscopic shape is not a simple magnified picture of one
molecule.*

**UNO/MFS INSTRUMENTED MODE**

MFS can act as a long-duration room-temperature logger and audible
reminder; host software can time-stamp daily images and observations.

**AI REASONING CHALLENGE**

Ask AI to infer lattice structure from crystal shape alone; then
critique why that inference is limited.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Some salts contain water inside the solid itself. How can a "dry"
crystal contain water?*

**OCC-10 Water Inside a Solid: Hydrates**

*How can a solid crystal contain chemically organized water?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Interpret hydrate formulas.

- Compare hydrated and anhydrous formula masses.

- Connect crystal water to coordination chemistry.

**MATERIALS**

- MgCl₂·6H₂O or MgSO₄·7H₂O

- balance

- sealed storage

- optional gentle teacher demonstration of dehydration for a suitable
  hydrate

**SAFETY**

Hygroscopic salts absorb moisture. Heating/dehydration, if performed, is
teacher controlled and compound-specific; consult SDS and avoid
decomposition conditions.

**PROCEDURE**

1.  Examine the hydrate formula and calculate the mass fraction of
    water.

2.  Compare 10 g hydrate with 10 g nominal anhydrous salt on a mole
    basis.

3.  Use a 3-D structure viewer for MgCl₂·6H₂O.

4.  Identify Mg, Cl, O, H and the repeating unit cell.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-10 Water Inside a Solid: Hydrates**

*How can a solid crystal contain chemically organized water?*

**MAKE MEANING**

**THEORY**

- Hydrate water occupies defined crystallographic positions; it is not
  simply liquid trapped between grains.

- Mg²⁺ commonly exhibits sixfold water coordination in the hexahydrate
  structure.

**EXPECTED OBSERVATIONS**

- The formula implies a large, countable contribution from water to
  crystal mass.

**ANALYSIS**

- Calculate percent water by mass.

- Explain why equal grams of hydrate and anhydrous material produce
  different solution compositions.

**REASONING TRAP**

*Dot notation in a hydrate formula is structural stoichiometry, not
multiplication by "wetness."*

**UNO/MFS INSTRUMENTED MODE**

Use MFS as a temperature/humidity companion if an external humidity
sensor is added; otherwise keep the digital thread by recording sample
IDs and masses through the host.

**AI REASONING CHALLENGE**

Ask AI to draw or describe MgCl₂·6H₂O. Then compare its model with the
actual crystallographic structure rather than accepting a plausible
cartoon.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*How do we know the atoms really occupy those positions?*

**OCC-11 See the Lattice: Diffraction**

*How can a pattern of spots or peaks reveal an atomic lattice?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Load a real CIF structure.

- Connect unit cells to diffraction.

- Understand Bragg's law conceptually.

**MATERIALS**

- Internet-connected computer

- COD MgCl₂·6H₂O entry 9011352

- OpenMX Viewer or equivalent

- XRD simulation tool

**SAFETY**

No chemical hazard if conducted as a digital extension. Actual X-ray
equipment is not part of this curriculum and requires specialized safety
infrastructure.

**PROCEDURE**

1.  Open COD 9011352 in a browser-based structure viewer.

2.  Display the unit cell and expand to a 2×2×2 supercell.

3.  Identify the Mg coordination environment and chloride positions.

4.  Generate or view a simulated powder diffraction pattern.

5.  Relate peak positions qualitatively to lattice spacings using
    Bragg's law.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-11 See the Lattice: Diffraction**

*How can a pattern of spots or peaks reveal an atomic lattice?*

**MAKE MEANING**

**THEORY**

- Periodic arrays scatter X-rays coherently. Bragg's law nλ=2d sinθ
  links wavelength, plane spacing, and diffraction angle.

- X-rays locate electron density well; neutron diffraction is especially
  useful for hydrogen positions.

**EXPECTED OBSERVATIONS**

- The lattice view and diffraction pattern are two representations of
  the same periodic structure.

**ANALYSIS**

- Choose one prominent peak and explain what information its angle
  carries.

- Distinguish structure solution from simply viewing a CIF.

**REASONING TRAP**

*A diffraction pattern is not a photograph of atoms; structure is
inferred from reciprocal-space measurements and models.*

**UNO/MFS INSTRUMENTED MODE**

Host/AI mode: load CIF metadata alongside lab records so students can
ask structural questions grounded in the actual file, not generic
chemistry.

**AI REASONING CHALLENGE**

Ask AI to identify the unit-cell parameters and Mg coordination from the
CIF. Verify every answer against the source record.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*We have explored neutral water and salts. What changes when the
solution becomes acidic or basic?*

**OCC-12 Acid and Base in the Cup**

*Can color reveal hydrogen-ion chemistry?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Use an indicator to classify acids and bases.

- Connect pH to a logarithmic concentration scale.

- Observe neutralization.

**MATERIALS**

- Red cabbage indicator or pH paper

- vinegar/citric acid

- baking soda solution

- washing soda solution optional

- droppers

- cups

**SAFETY**

Household dilute reagents are low hazard but goggles remain standard.
Never mix unknown cleaners or bleach with acids.

**PROCEDURE**

1.  Prepare indicator and a neutral water reference.

2.  Test small equal volumes of acidic and basic household solutions.

3.  Create a stepwise neutralization by adding base to acid in small
    measured increments.

4.  Record color/pH after each increment.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-12 Acid and Base in the Cup**

*Can color reveal hydrogen-ion chemistry?*

**MAKE MEANING**

**THEORY**

- Acid-base chemistry concerns proton transfer and solution equilibria.
  pH=-log10\[H⁺\] in the idealized introductory definition.

**EXPECTED OBSERVATIONS**

- Indicator colors change systematically with pH. Neutralization moves
  the mixture through an intermediate range.

**ANALYSIS**

- Plot pH vs. added volume if a pH probe is available.

- Explain why equal household volumes do not necessarily neutralize.

**REASONING TRAP**

*Color is evidence of indicator equilibrium, not a direct count of "acid
particles."*

**UNO/MFS INSTRUMENTED MODE**

A pH module can use the available analog channel; log pH and
temperature. Buttons mark each addition so the titration trace contains
exact event times.

**AI REASONING CHALLENGE**

Ask AI to predict how many mL of base will neutralize vinegar using only
labels. It should refuse overprecision without concentration data.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*What happens when two clear ionic solutions create an insoluble solid?*

**OCC-13 Make a Solid from Two Clear Solutions**

*Where did the precipitate come from?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Observe precipitation.

- Write complete and net ionic equations.

- Introduce solubility equilibrium and spectator ions.

**MATERIALS**

- Dilute CaCl₂ solution

- dilute Na₂CO₃ solution (washing soda)

- droppers/cylinders

- cup

- filter paper optional

**SAFETY**

Goggles. Use dilute solutions. Dispose according to local classroom
rules; avoid drain disposal of any extension using heavy-metal salts.

**PROCEDURE**

1.  Prepare known dilute solutions, e.g. 0.1 M if quantitative work is
    desired.

2.  Mix equal measured volumes.

3.  Observe turbidity/solid formation.

4.  Filter, rinse, dry, and weigh precipitate in an advanced
    mass-balance version.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-13 Make a Solid from Two Clear Solutions**

*Where did the precipitate come from?*

**MAKE MEANING**

**THEORY**

- Ca²⁺ + CO₃²⁻ → CaCO₃(s).

- Na⁺ and Cl⁻ remain in solution as spectator ions.

- Precipitation reflects a solubility equilibrium, not disappearance of
  ions.

**EXPECTED OBSERVATIONS**

- A white precipitate forms rapidly under suitable concentrations.

**ANALYSIS**

- Predict limiting reagent from moles.

- Compare theoretical and recovered mass if dried quantitatively.

**REASONING TRAP**

*Cloudiness is not "a new element"; it is a new phase with atoms
conserved.*

**UNO/MFS INSTRUMENTED MODE**

Use an LED/light sensor across the cup as a crude turbidity channel;
time the onset and clearing/settling behavior.

**AI REASONING CHALLENGE**

Ask AI to balance molecular and net ionic equations and to identify
spectator ions. Verify charge and atom conservation.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Ions can also transfer electrons through metals. Can the same cup
become an electrochemical cell?*

**OCC-14 Redox and Corrosion**

*Can a cup of salt water reveal electron transfer?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Recognize oxidation and reduction.

- Measure voltage between dissimilar metals.

- Connect corrosion to electrochemical processes.

**MATERIALS**

- NaCl solution

- copper strip

- zinc or galvanized steel strip

- iron nail

- multimeter

- alligator leads

**SAFETY**

Use only passive galvanic measurements. Do not connect mains power or
perform uncontrolled electrolysis. Wash hands after handling metals.

**PROCEDURE**

1.  Place two dissimilar clean metal strips in the electrolyte without
    touching.

2.  Measure open-circuit voltage and polarity.

3.  Try different pairs.

4.  Observe surfaces over hours/days for corrosion products.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-14 Redox and Corrosion**

*Can a cup of salt water reveal electron transfer?*

**MAKE MEANING**

**THEORY**

- Oxidation releases electrons; reduction consumes them. Dissimilar
  electrodes in an electrolyte can establish a potential difference.

- Corrosion is coupled electrochemistry influenced strongly by chloride.

**EXPECTED OBSERVATIONS**

- Different metal pairs produce different voltages and corrosion
  tendencies.

**ANALYSIS**

- Record sign as well as magnitude.

- Relate which electrode is negative to likely oxidation in the simple
  cell.

**REASONING TRAP**

*A voltmeter reading alone does not identify every reaction occurring at
the surfaces.*

**UNO/MFS INSTRUMENTED MODE**

UNO can read a safely scaled low voltage through an analog input, but
the handheld multimeter is preferred for first exposure. MFS remains
timer/event logger.

**AI REASONING CHALLENGE**

Ask AI to predict electrode polarity, then compare with the measured
sign. Require it to explain discrepancies rather than flip labels
silently.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Chemical change can be fast or slow. What controls reaction rate?*

**OCC-15 Rates and Catalysis**

*What changes how fast chemistry happens?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Measure a reaction rate proxy.

- Test concentration or temperature as a variable.

- Observe catalysis using a familiar biological catalyst.

**MATERIALS**

- 3% hydrogen peroxide

- dry yeast suspension (catalase source)

- small cup

- temperature probe

- graduated cylinder

- dish soap optional for visible foam

**SAFETY**

Goggles required. Use only household 3% H₂O₂. Keep volumes small;
reaction foams and releases oxygen. Do not seal the vessel.

**PROCEDURE**

1.  Prepare equal H₂O₂ portions at two temperatures or concentrations.

2.  Add equal yeast suspension and start timing immediately.

3.  Measure foam height, gas volume proxy, mass loss, or time to a
    defined endpoint.

4.  Repeat with one variable changed at a time.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-15 Rates and Catalysis**

*What changes how fast chemistry happens?*

**MAKE MEANING**

**THEORY**

- Catalysts lower the kinetic barrier without being consumed
  stoichiometrically. Reaction rate depends on concentration,
  temperature, catalysts, and mechanism.

**EXPECTED OBSERVATIONS**

- Warmer conditions generally accelerate catalase activity within a
  moderate range; extreme conditions can alter enzyme function.

**ANALYSIS**

- Choose one rate metric before seeing the result.

- Graph metric vs. time and compare initial slopes where meaningful.

**REASONING TRAP**

*Foam height is a proxy influenced by surfactant and bubble stability;
it is not a direct oxygen meter.*

**UNO/MFS INSTRUMENTED MODE**

MFS timer plus event button gives repeatable start marks. A pressure/gas
sensor can be added in advanced mode, but never seal a peroxide reaction
without engineered pressure relief.

**AI REASONING CHALLENGE**

Ask AI to propose the cleanest rate metric using only available
equipment. Score it on measurability and confounding variables.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Can light become a quantitative chemical instrument?*

**OCC-16 Light Becomes Concentration**

*Can a beam of light tell us how much solute is present?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Build a calibration curve.

- Introduce transmittance and absorbance.

- Use Beer-Lambert behavior over a suitable range.

**MATERIALS**

- Food coloring

- water

- identical clear cuvettes/cups or fixed optical path

- LED

- phototransistor/LDR

- resistors

- balance or syringes

**SAFETY**

Use low-voltage LEDs only. Avoid staring into high-intensity sources;
ordinary visible indicator LEDs are sufficient.

**PROCEDURE**

1.  Prepare a serial dilution of one food dye.

2.  Keep path length and detector geometry fixed.

3.  Measure detector response for blank and each concentration.

4.  Convert to relative transmittance; optionally compute A=-log10(T).

5.  Plot absorbance vs. concentration.

|                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** Use the minimum apparatus needed to answer the question. Paper tables and a handheld thermometer are valid. Do not introduce the electronic layer until it improves timing, resolution, repeatability, or data volume. |

**OCC-16 Light Becomes Concentration**

*Can a beam of light tell us how much solute is present?*

**MAKE MEANING**

**THEORY**

- Beer-Lambert law A=εbc predicts absorbance proportional to
  concentration for suitable dilute systems, fixed wavelength, and fixed
  path length.

**EXPECTED OBSERVATIONS**

- Raw detector voltage may be nonlinear, but absorbance often improves
  linearity over a useful range.

**ANALYSIS**

- Build a calibration line, then estimate an unknown concentration.

- Report the range over which calibration is credible.

**REASONING TRAP**

*A pretty straight line outside the instrument's useful range is not
evidence of unlimited linearity.*

**UNO/MFS INSTRUMENTED MODE**

Photodetector can use A5 on common MFS boards when not occupied by
another add-on. MFS buttons step through standards; USB stream labels
each reading with concentration ID.

**AI REASONING CHALLENGE**

Ask AI to infer the unknown from calibration data, then require
uncertainty and detection-range caveats.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*Why do oil and water separate even though both are made of molecules?*

**OCC-17 Measuring a Molecule: Avogadro's Number from a Soap Film
(revised)**

*Can a film one molecule thick let us count Avogadro's number?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Form and measure a monolayer of oleic acid on a water surface.

- Use the monolayer's geometry to estimate the length of a single
  molecule.

- Use molecular volume, molar mass, and density to estimate Avogadro's
  number.

- Distinguish a measured quantity (film diameter) from a model-based
  inference (molecule count).

**MATERIALS**

- Oleic acid

- Isopropyl alcohol (or similar volatile solvent) for dilution

- Large shallow tray or wide cup of water

- Lycopodium powder, fine talc, or chalk dust (to make the film visible)

- Calibrated dropper or syringe (to determine volume per drop)

- Ruler or calipers

- Balance (optional, to confirm oleic acid density)

**SAFETY**

Green band. Oleic acid itself is low hazard. The alcohol diluent is
flammable — keep away from open flame or heat sources and work in a
ventilated space. Label all diluted stock clearly with concentration and
date; the dilution is easy to lose track of and the whole calculation
depends on it.

**PROCEDURE**

1.  Prepare a dilute stock solution of oleic acid in alcohol at a known
    ratio (for example, 1 mL oleic acid brought to 1000 mL with
    alcohol), then dilute that stock again by a known factor (for
    example 1:10) so that a single drop delivers a very small,
    calculable volume of pure oleic acid.

2.  Using a syringe, count how many drops of the final dilute solution
    make up 1.00 mL. Record this to get volume per drop.

3.  Fill the tray with water and lightly and evenly dust the surface
    with powder.

4.  Using the dropper, release exactly one drop of the dilute solution
    gently onto the center of the water surface.

5.  Allow the film to spread fully and the alcohol to evaporate/disperse
    into the water; the powder will be pushed back to the edge of a
    clear circular region.

6.  Measure the diameter of the resulting circle in at least two
    directions and average.

7.  Repeat at least three times and compare diameters.

|                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **KITCHEN TABLE MODE** A cake pan or large mixing bowl, a kitchen dropper calibrated by counting drops per teaspoon, and flour or cocoa powder dusted on the surface all work. The measurement only needs a ruler. |

**OCC-17 Measuring a Molecule: Avogadro's Number from a Soap Film
(revised)**

*Can a film one molecule thick let us count Avogadro's number?*

**MAKE MEANING**

**THEORY**

- Oleic acid is amphiphilic: a polar carboxylic acid head group anchors
  to water while a long nonpolar hydrocarbon tail resists it.

- Spread thin enough on a water surface, the molecules self-organize
  into a film exactly one molecule thick — thicker regions are unstable
  and thin out until a monolayer remains.

- Film volume divided by film area gives molecular length directly: t =
  V / A.

- Treating the molecule as a simple solid of known volume connects that
  length to a molar volume, and from there to Avogadro's number, N_A =
  V_molar / V_molecule.

**EXPECTED OBSERVATIONS**

- The clear circular region should be reasonably reproducible in
  diameter across repeated trials with the same drop.

- Diameter is sensitive to how gently the drop is released and how
  evenly the powder was dusted.

**ANALYSIS**

- Calculate delivered oleic acid volume per drop: (stock concentration)
  × (dilution factor) × (volume per drop).

- Calculate film area from the averaged diameter: A = πr².

- Calculate film thickness t = V / A — this is the estimated molecular
  length.

- Using oleic acid's molar mass (282.46 g/mol) and density (about 0.895
  g/mL), calculate molar volume, then divide by the volume of one
  molecule (estimated from t) to estimate N_A.

- Compare the class's estimate with the accepted value (6.022 × 10²³) as
  an order-of-magnitude check, not a precision check.

**REASONING TRAP**

*This method assumes the film is exactly one molecule thick and that the
molecule's shape can be approximated as a simple cylinder or sphere for
the volume calculation. Both are simplifications. Historically, this
experiment (associated with Rayleigh and later popularized as a
classroom method) was valued for getting the correct order of magnitude
from very simple apparatus — not for matching the modern defined value.
Getting "close" is the win; getting exact is not the point.*

**UNO/MFS INSTRUMENTED MODE**

A fixed-position camera or phone photo with a ruler in frame, analyzed
on the host computer, gives a more repeatable diameter measurement than
eyeballing it over the tray. If a light sensor is used to detect the
powder-free boundary along a fixed scan line, log the crossing points
through the same USB serial stream used elsewhere in the course, so this
dataset lives in the same format as every other OCC run.

**AI REASONING CHALLENGE**

Give the AI only the drop count, dilution factors, and measured
diameter, and ask it to calculate Avogadro's number. Require it to state
every assumption it used (molecule shape, monolayer thickness, density
value) before presenting the result, and to say how sensitive the final
answer is to a small error in the diameter measurement.

**THE QUESTION THAT CREATES THE NEXT EXPERIMENT**

*A soap film estimated how many molecules make up a mole from ordinary
geometry. Earlier, a diffraction pattern located atoms inside a crystal
lattice by an entirely different method. If two unrelated techniques
both point to the same atomic-scale reality, what does that agreement
actually prove — and what would it take for one of them to be wrong?*

**OCC-18 From Ice Melt to Living Molecules**

*Why does biology care about hydrated Mg²⁺?*

**DO THE SCIENCE**

**LEARNING TARGETS**

- Connect inorganic hydration to biochemistry.

- Explain Mg²⁺ roles in ATP and nucleic-acid chemistry.

- Distinguish a conceptual biological extension from a kitchen-table
  biochemical assay.

**MATERIALS**

- MgCl₂·6H₂O structure model/CIF

- molecular visualization resources

- ATP/DNA polymerase diagrams or reputable references

- student lab notebook

**SAFETY**

This is primarily a model-and-evidence lesson. Do not improvise
biological or diagnostic experiments with deicer-grade material.

**PROCEDURE**

1.  Return to the MgCl₂·6H₂O lattice and identify the hydrated Mg²⁺
    environment.

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
