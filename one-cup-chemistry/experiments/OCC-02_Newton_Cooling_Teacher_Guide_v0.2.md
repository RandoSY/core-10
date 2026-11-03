# OCC-02 — Newton Cooling

**Core 10 / One Cup Chemistry · Author's Teacher Manual v0.2**

This is a faithful, separately discoverable extraction of the original OCC-02 lesson. The authoritative historical source remains [Teacher Manual v0.2, archived part 03](https://github.com/RandoSY/core-10/blob/main/one-cup-chemistry/archive/Teacher_Manual_v0.2/part-03.md). This is an educational protocol, not proof of a completed physical test.

---

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
