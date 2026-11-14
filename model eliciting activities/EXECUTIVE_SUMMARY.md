# Executive summary — How Uniform Are These Rocks?

**Project status:** CORE 10 model-eliciting activity, committee proposal, illustrated bench kit, and tested Python prototype. The next milestone is a classroom pilot using physical specimens.

## 1. The educational idea

The lab opens with **“How uniform are these rocks?”** Students are not initially given a definition, metric, or preferred comparison. Their job is to decide what should count as an observation, name a property, devise a measurement procedure, test it against a case that might break it, and explain it well enough for another team to use on a new specimen. This is an application of Richard Lesh’s model-eliciting approach and the CORE 10 principles **Experience Before Equation** and **Need Before Technology**.

The museum scenario gives the inquiry a practical consequence. If a museum must display one representative specimen from each collection, when can another rock stand in for it? “Uniform enough” then needs a defensible purpose and tolerance. A descriptive question, by contrast, can report the spread without declaring a pass or fail.

## 2. The specimens and what students can compare

| Collection | Prototype and role |
| --- | --- |
| A | Smooth, polished, oblong gray metamorphic pebbles. The prototype shows why smoothness, roundness, and sphericity are not interchangeable. |
| B | Small limestone gravel. It makes measurement resolution and choice of vessel consequential. |
| C | Irregular sedimentary fragments with pits, recesses, and tunnel-like openings. The shape challenges simple volume models and forces a boundary decision. Possible insect modification is a hypothesis, not a finding. |

One specimen of each type makes the first comparison tangible. Three collections make it possible to sample several rocks instead of assuming one prototype represents a pile. The illustrations are not measured samples or calibrated scale drawings.

Three inquiry levels emerged:

1. **Within one rock:** Do regions differ in a stated property, such as missing volume fraction?
2. **Among rocks within a pile:** How much does a consistently measured property vary across specimens of the same collection?
3. **Between piles:** Do the collections differ in a typical value, variability, or another explicitly chosen group property?

Repeated instrument readings are a separate source of variation, not additional rocks. A result from the classroom specimens is not automatically a claim about all limestone, metamorphic, or sedimentary rocks.

## 3. The bench and the mathematics

The illustrated bench includes a metric ruler, manual outside caliper, wide-opening digital caliper, nonstretch string, a wide-mouth graduated cylinder, and a digital balance. The cylinder needs clearance, full immersion, and headroom for the largest rock tested one at a time. A narrower cylinder or finer method can be used if gravel displacement is too small to read reliably. A balance adds dry mass and allows density to become a follow-up question rather than a required station.

| Measurement or model | What it contributes |
| --- | --- |
| Caliper spans and string girth | Three perpendicular outside dimensions, or a circumference along a specified path. They are not interchangeable. |
| Box and ellipsoid volume | Geometric predictions from measured dimensions. The ellipsoid uses πLWT/6. |
| Cross-sections | Approximate volume by adding slice contributions, or express it as the integral of occupied cross-sectional area. Subtract resolved voids under the declared boundary convention. |
| Water displacement and dry mass | An independent volume check for compatible specimens, and a route to density. Open passages that fill do not displace their own volume, while trapped air can inflate the reading. |
| Solidity | Occupied volume divided by convex-hull volume. It measures how fully the hull is occupied, not how evenly the missing volume is distributed. |
| Wadell sphericity | Equal-volume sphere area divided by rock surface area. It requires a defensible area and volume for the same boundary. The starter’s shortest-to-longest axis ratio is explicitly a proxy, not Wadell sphericity. |

The key counterexample uses two specimens or models that are both 10% hollow overall. One is 10% hollow in each of four equal-envelope regions. The other is 0%, 0%, 0%, and 40% hollow. Their means tie, but their regional standard deviations are 0 and about 17.3 percentage points. A second example holds mean and range fixed while changing standard deviation. A third shows that the same spread can conceal different spatial arrangements.

## 4. AI and Python

Students write the specification before using AI. They state their question, observation unit, property, units, boundary and measurement rules, treatment of repeated or missing readings, and what result they expect from a test case. They can then ask AI to help implement or modify the rule in Python. They verify a result by hand and give the model and code to another team for an uncoached application.

The published Python 3.10+ starter has no third-party dependencies. It captures bench readings in CSV, calculates axis ratio, ellipsoid volume, displacement and density, and calculates Wadell sphericity when matching volume and surface area are provided. It reports within-rock regional summaries, within-pile statistics, and differences between pile means separately. The kit includes blank sheets, synthetic examples, and six unit tests that passed. The software does not decide what “uniform” means for the student.

## 5. Committee and historical materials

The [committee proposal, edition 1.1](Uniformity_Through_Inquiry_Research_Proposal_v1_1.pdf) includes a two-cycle study design, a three-session protocol, research questions, proposed recruitment and ethics procedures, an analytic plan, student prompts, and a calibration example. It is a proposal, not a completed study. The [original edition](Uniformity_Through_Inquiry_Research_Proposal.pdf) is retained unchanged.

[Appendix C](APPENDIX_C_WADELL.md) documents Hakon Adolf Wadell’s work, the distinction between sphericity and roundness, historical alternatives, and a bench prompt. It links to a verified [portrait in *Jökull*, printed page 136](https://jokull.jorfi.is/wp-content/uploads/2021/11/jokull70p129-138.pdf#page=8), credited there to J. Harlen Bretz’s 1964 memorial.

## 6. What remains

Pilot the smallest useful version first: real rocks, the ambiguous opening, one counterexample, and an uncoached handoff. Have two operators repeat a few measurements to see whether disagreement is large relative to differences among rocks. Add tools only when a team can explain what those tools would settle. The principal success criterion is whether another team can apply the written rule to an unfamiliar specimen and defend what its conclusion does and does not say.
