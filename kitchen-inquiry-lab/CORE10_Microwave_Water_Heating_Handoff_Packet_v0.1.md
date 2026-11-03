# CORE 10 Handoff Packet: Microwave Water Heating and Energy Cost

**Version:** 0.1-draft  
**Release state:** bounded reference experiment; independent handoff run not yet recorded  
**Canonical home:** https://github.com/RandoSY/core-10

## Purpose

Measure one ordinary heating event well enough to connect thermal physics to household energy economics:

`water mass + temperature rise + elapsed time + electrical input -> useful heat + input energy + cost + efficiency boundary`

The essential comparison is between useful thermal energy in the water, `Q_useful = m c Delta T`, and electrical energy purchased by the appliance. They must remain separate quantities.

## Hardware and materials

| Item | Requirement |
|---|---|
| Water | About 500 g (record actual mass) |
| Vessel | Open, microwave-safe container; never seal it |
| Scale | Digital kitchen scale, preferably 0.1 g resolution |
| Thermometer | Probe/instant-read thermometer, about 0.1 C resolution preferred |
| Timer | Stopwatch or phone timer |
| Electricity measurement | Plug-in energy monitor reporting Wh/kWh, if the microwave outlet is safely accessible |
| Cost basis | Recent electric bill or clearly labeled local rate assumption |

Use normal microwave safety: avoid superheating, use an appropriate open container, handle hot water carefully, and do not access wiring or an inaccessible outlet.

## Source and setup

Primary reference: `kitchen-inquiry-lab/Kitchen_Inquiry_Lab_Canonical_Map.md` in the CORE 10 repository. It establishes Microwave Water Heating as a required experiment and defines the accounting boundary.

1. Tare the vessel; measure and record water mass, `m` in grams.
2. Measure initial water temperature, `T_initial`; record ambient temperature.
3. If safely practical, reset the plug-in energy monitor and connect the microwave through it. Record its final Wh or kWh reading. Otherwise record the appliance rating and label any power-times-time calculation as an estimate.
4. Heat for a measured interval. Record elapsed time and final water temperature, `T_final`. Stir carefully/consistently before final temperature measurement and record the procedure.
5. Calculate:

```text
DeltaT = T_final - T_initial
Q_useful (J) = m(g) x 4.184 J/(g C) x DeltaT(C)
Q_useful (Wh) = Q_useful (J) / 3600
E_input (Wh) = meter reading, preferably
apparent efficiency = Q_useful / E_input
event cost = E_input(kWh) x stated cost basis ($/kWh)
```

6. Record the system boundary: water only for useful heat; appliance/microwave environment for input energy. Do not call the difference a precise microwave efficiency without stating the boundary and measurement limits.

## Expected output

A completed one-run data record should include:

| Field | Required value |
|---|---|
| Version/date/tester | Identification and traceability |
| Mass, temperatures, time, ambient | Raw physical evidence |
| Metered Wh/kWh or stated estimate method | Electrical-input evidence |
| `Q_useful`, `E_input`, ratio, cost | Derived results with units |
| Bill/rate basis | Economic assumption/evidence |
| Vessel, microwave setting, stirring/probe method | Reproduction context |
| Deviations and safety observations | Honest boundary record |

The expected intellectual outcome is not a preselected number. It is a defensible ledger showing that heat in the water and electricity bought by the household differ for understandable physical reasons.

## Test evidence

| Evidence | Status | Meaning |
|---|---|---|
| Canonical CORE 10 rule and complete measurement chain | Documented | Experiment is designated first-class and conceptually specified. |
| Instrument stack, formulas, energy/cost distinction | Documented | Procedure can be executed with ordinary household tools. |
| Clean, independent measured run with raw record | **Not yet recorded in this packet** | Required handoff acceptance evidence. |

**Handoff acceptance:** a second tester uses this packet without verbal coaching, produces the complete data record above, repeats the run once, and identifies at least one plausible reason for the gap between `Q_useful` and `E_input`. PASS requires preserved raw readings, calculations, and stated cost basis—not agreement with any target efficiency.

## Limitations

- A household energy monitor may not fit or accurately capture every microwave installation; never alter fixed wiring to force a measurement.
- Thermometer position, stirring, evaporation, vessel heating, and delay affect the apparent result.
- An all-in cents/kWh figure is an analytical household-cost basis, not necessarily the utility's marginal tariff.
- This is an energy-accounting experiment, not a calibrated appliance certification test.

## Why it matters

This is CORE 10 at its most direct: ordinary life becomes measurable, and measurement becomes decision-making. The learner follows energy from a wall outlet into a cup of water, sees where a simplified model succeeds and fails, and turns joules into watt-hours, kilowatt-hours, and dollars. The microwave is not a novelty laboratory device. It is a familiar system whose hidden flows of energy, money, heat, loss, and usefulness can be made visible with a scale, thermometer, timer, and an honest record.

The experiment teaches more than the formula `Q = mc Delta T`. A mass and temperature rise tell a defensible story about the water, but not the whole appliance. Metered input tells a different story about the household purchase. Their difference is not an embarrassment to be corrected away. It is the finding: the vessel warmed, the oven walls and air participated, heat escaped, readings took time, and every answer depends on a named system boundary.

That habit matters outside school. A person who can distinguish power from energy, joules from kWh, and a marginal rate from an all-in bill can investigate claims about appliances, conservation, solar power, storage, and cost without merely repeating slogans. The final question is practical rather than theatrical: how much did this useful event require, what did it cost, and was the result enough for the purpose? That is science as agency in the place people actually live.