# OCC-16 — Light Becomes Concentration

Source: [One Cup Chemistry Teacher Manual v0.2 experiment compendium](https://github.com/RandoSY/core-10/blob/main/one-cup-chemistry/experiments/Teacher_Experiment_Compendium_OCC00_to_OCC19_v0.2.md); copied from original instructional text. Classroom and hardware validation are separate from preservation.

---

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
