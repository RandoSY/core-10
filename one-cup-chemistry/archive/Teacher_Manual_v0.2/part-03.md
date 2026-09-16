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
