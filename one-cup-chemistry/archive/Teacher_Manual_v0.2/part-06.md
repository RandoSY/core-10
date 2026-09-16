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
