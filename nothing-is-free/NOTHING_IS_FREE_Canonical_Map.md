# NOTHING IS FREE — Canonical Map

## Energy, Flux, Storage, Work, and Cost

**Canonical placement:** sibling branch under CORE 10.  
**Sources recovered:** Curricular Threads Architecture v1.0, organized NOTHING IS FREE visual/comic corpus, STC Energy Explorer v0.2 documentation, and September 2026 kit/cost planning records.  
**Integrative continuation:** Personal Energy Laboratory.

## Central idea

Energy is never just “there.” It comes from somewhere, crosses boundaries, changes form, may be stored, is lost from the intended pathway, performs useful work, and carries a cost.

The curriculum therefore asks learners to make energy physically accountable:

`source → transfer → conversion → storage → useful output → loss → reserve → cost → decision`

The title **NOTHING IS FREE** is both physical and practical: every useful effect requires a real energy flow, and every real system has constraints, conversion losses, finite storage, opportunity costs or economic costs.

## Intellectual ownership

Within the CORE 10 branch architecture, NIF owns **energy accounting and management**, not the first encounter with every underlying phenomenon.

It should reuse earlier measurements rather than duplicate them simply to claim an energy lesson.

Canonical NIF activities identified in the curriculum architecture are:

1. measure USB/device charging — make Wh a real measured quantity;
2. charge a rechargeable battery — storage and state of charge;
3. discharge the same battery — usable capacity and reserve;
4. compare input Wh with output/useful Wh — loss and efficiency;
5. measure a small solar-panel day — variable generation;
6. connect solar generation to battery storage;
7. convert electrical energy into motor/mechanical work;
8. operate a low-cost autonomous robot from a removable rechargeable cell pack;
9. compare robot route/runtime and useful travel against energy consumed;
10. convert Wh/kWh into money and trade-offs.

## Relationship to Kitchen Inquiry Lab

NIF must not re-run Kitchen Inquiry's microwave water-heating experiment merely to introduce energy.

Instead it imports the preserved record and asks a new question:

- how much electrical energy entered the appliance?
- how much became useful thermal energy in the water?
- where did the rest go?
- how much storage/generation capacity would that event consume?
- what did the energy cost?
- was the result sufficient for the need?

Thus one canonical water-heating event has multiple intellectual lives without becoming duplicate curriculum.

## Energy accounting vocabulary

The course should keep these quantities distinct:

- **energy** — accumulated capacity for transfer/work, commonly J, Wh or kWh;
- **power** — rate of energy transfer, W;
- **flux** — transfer rate normalized to an area or other boundary measure where appropriate;
- **storage** — energy retained for later use;
- **useful work/output** — the intended result;
- **loss** — energy transferred into unintended or less useful channels;
- **efficiency** — useful output divided by input on a clearly stated basis;
- **reserve** — deliberately unspent usable storage retained for future uncertainty;
- **cost** — economic or resource burden associated with acquiring and using energy.

A watt is not a watt-hour. Stored capacity is not instantaneous power. A battery's nominal rating is not automatically usable delivered energy. A system boundary must be named before “efficiency” has a defensible meaning.

## The energy ledger

Every NIF investigation should be capable of producing an energy ledger:

| Question | Evidence |
|---|---|
| Where did the energy originate? | source/generation measurement or stated source |
| How much entered the system? | Wh/J input measurement |
| Where was it stored? | battery or other storage state/capacity |
| What useful effect occurred? | light, heat, motion, distance, lifted mass, etc. |
| What was lost from the intended pathway? | input-output difference with stated boundary |
| How long could the system continue? | remaining usable reserve and load estimate |
| What did it cost? | measured kWh/Wh plus rate/cost basis |
| Was that enough? | requirement + margin compared with available resource |

This directly connects the estate's two questions: **How much?** supplies the ledger; **Enough?** turns the ledger into a decision.

## Portable energy architecture

The low-cost NIF hardware uses removable rechargeable AA/AAA NiMH cells as a practical energy store. The educational pattern is intentionally simple:

`use cells → measure energy/work → stop at a conservative limit → remove cells → recharge externally → reuse`

On-device charging is not required for the teaching system. The important measurements are stored energy, delivered energy, voltage/current behavior, useful work and reserve—not charging-circuit complexity.

Intentional deep discharge of a series NiMH pack is excluded. A run should stop at a conservative voltage/behavior limit and the cells should be recharged normally.

## Solar sequence

The small solar-panel activity is valuable because generation is visibly variable.

The learner can measure:

- panel voltage/current/power;
- accumulated Wh over an interval;
- effects of orientation, clouds, shade and temperature;
- energy delivered to a charger/storage path;
- downstream usable battery energy.

The point is not to teach a slogan about renewable energy. It is to create a measured chain from environmental input to stored usable energy, including conversion loss and intermittency.

## The low-cost robot as an energy instrument

The NIF robot is not primarily a robotics product. It is a reference vehicle for turning stored electrical energy into transportation and decision-making.

The surviving **STC Energy Explorer v0.2** uses an intentionally layered architecture:

```text
Rechargeable AA pack
        ↓
STC robot board
motors + ultrasonic + local reflexes
        ↓
human-readable UART
        ↓
M5StickC Plus2
navigation + run memory + logging
        ↓
USB log / later BLE / dashboard
```

Its mission is deliberately modest:

> Drive, avoid obstacles, remember which directions produced long clear runs, and increasingly choose routes that produce useful uninterrupted travel.

This is explicitly **not yet full metric SLAM**. It is heading-sector memory / energy-aware exploration that can later gain richer localization.

### Energy question

The useful educational measure is not simply “did the robot move?” It is something like:

- Wh per meter;
- distance per charge;
- useful uninterrupted motion per Wh;
- effect of payload, surface, route or avoidance behavior;
- reserve remaining at mission stop.

That turns route choice into an energy-management problem.

### Validation boundary

STC Energy Explorer v0.2 is documented as **bench/software ready but not board-map complete**. The exact motor/ultrasonic/line-sensor pin map for the low-cost HU-046BS-like board was not established in the recovered package.

The documented safe order is:

1. flash generic bring-up firmware;
2. discover and record the actual board pin map;
3. complete the board profile;
4. prove `STOP`, `FWD`, `REV`, `LEFT`, `RIGHT`, and `RANGE?` manually;
5. only then run autonomous Energy Explorer behavior.

Do not silently promote this package to physical-board validated status.

## Human-readable command path

The robot work preserves the same estate-wide preference seen in SDL and One Cup Chemistry: simple readable ASCII interfaces rather than opaque binary control when bandwidth permits.

That makes the command/evidence path inspectable by:

- learner;
- serial terminal;
- logger;
- simulator;
- dashboard;
- AI collaborator.

The protocol is part of the teaching surface rather than hidden plumbing.

## Energy economics

NIF completes the chain by converting physical measurements into money and trade-offs.

At the household scale:

`energy cost = kWh × applicable cost basis`

At the device scale the same relationship can be applied to Wh by converting units appropriately.

But the learner should not confuse a simple marginal energy rate with the full bill. Fixed charges, riders/taxes and other charges should be identified where relevant, and any “all-in” rate should be labeled as an analytical construction rather than a utility tariff claim.

The goal is not merely bill arithmetic. It is to connect physical energy demand to resource allocation.

## NOTHING IS FREE as preparation for Personal Energy Laboratory

NIF teaches the ledger. **Personal Energy Laboratory** makes the learner administer the ledger under constraint.

The integrative question is:

> **How do I maintain viable human life when energy is finite?**

The synthesis recruits earlier knowledge to maintain:

- warmth;
- cooling;
- transportation;
- food;
- hydration;
- electrical power.

A scenario can provide a solar forecast, usable battery capacity/state of charge, heating requirement, refrigeration load, transportation need and water-heating demand. The learner must allocate finite energy, retain appropriate reserve, and defend the plan.

The learner is not asked to rediscover watts or heat capacity. Those should already be available as prior evidence and models. The intellectual task is now **operational competence**.

## Web / AI role

Much of the Personal Energy synthesis can be web-native because its learning target is decision-making rather than instrument handling.

A durable implementation should combine:

- authentic preserved load/generation datasets;
- battery and solar models;
- scenario state;
- explicit constraints;
- resource reserve;
- AI critique and adaptation;
- references back to the physical measurements that established the model parameters.

AI may propose plans or point out hidden assumptions, but measured evidence and stated constraints remain authoritative.

A strong scenario includes at least one fault or conceptual trap so the system must question the premise rather than merely optimize arithmetic.

## Minimum complete NIF demonstration

A compact end-to-end demonstration can be:

1. measure one real energy event;
2. preserve its raw data and context;
3. calculate useful output and conversion loss;
4. measure or model storage burden;
5. express the event in Wh/kWh and dollars;
6. place it inside a finite solar/battery budget;
7. require a decision about whether/when to perform it;
8. retain enough reserve for a stated future requirement;
9. have AI critique the decision against the evidence.

This demonstrates the estate's recurring loop:

`physical reality → measurement → record → model → requirement → decision → action → re-measure`

## Enduring idea

NOTHING IS FREE is not an argument for deprivation. It is a discipline of **measured sufficiency**.

Know where energy came from. Measure how much moved. Account for what was stored, lost and usefully transformed. Know the cost. Preserve reserve. Then decide whether the available energy is **enough for the purpose**.
