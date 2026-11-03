# CORE 10

CORE 10 is the curriculum root for a practical science-and-engineering program built around measurement, experiment, and agency.

## Canonical hierarchy

CORE 10 has three first-level branches:

1. **Kitchen Inquiry Lab**
2. **One Cup Chemistry**
3. **NOTHING IS FREE (NIF) / Personal Energy Laboratory**

These are sibling branches under CORE 10, not independent top-level programs.

## Teaching principles

- **Experience Before Equation** — encounter the phenomenon first, then formalize it.
- **Need Before Technology** — introduce a tool because the investigation requires it.
- **Not talk, do** — learners should leave with practical capability, not only vocabulary.
- **How much? Enough?** — quantify reality, then judge sufficiency against a purpose.

## Kitchen Inquiry Lab

Uses ordinary surroundings and appliances as scientific infrastructure. The microwave-water-heating investigation is a protected first-class experiment. Its energy sequence includes joules, watts, watt-hours, kilowatt-hours, electrical bills, appliance operating cost, and the distinction between electrical input energy and useful thermal energy measured by `Q = mcΔT`.

## One Cup Chemistry

A one-vessel chemistry architecture intended to make real chemistry inexpensive, compact, and repeatable. Themes include cooling and brines, solutions, crystallization, conductivity, acid-base work, colorimetry/spectroscopy, electrochemistry, and related physical science.

The goal is a bounded, spiral-ready set of experiments with explicit theory and low-cost instrumentation.

## NOTHING IS FREE / Personal Energy Laboratory

Makes energy accounting tangible through batteries, charging, motors, robots, heat, transportation, and everyday devices. A low-cost STC15W robot with 4×AA NiMH cells is a reference vehicle for runtime, distance/coverage, and energy-use investigations.

## Instrumentation relationship

CORE 10 uses shared instruments rather than reinventing them. Temperature, mass, distance, conductivity, colorimetry, and browser-based measurement belong technically in the broader measurement/SDL ecosystem while serving CORE 10 experiments.

## Planned repository structure

- `teacher-guide/`
- `student-guide/`
- `kitchen-inquiry-lab/`
- `one-cup-chemistry/`
- `nothing-is-free/`
- `instruments/` — curriculum-facing instrument notes and links
- `media/` — diagrams and publication-ready visuals
- `validation/` — classroom/bench evidence and corrections

## Current state

**Lifecycle:** `active`

**Priority:** P1 finishing work.

This README establishes the canonical hierarchy. Experiment guides and source material still need to be migrated and verified before they are treated as reproducible releases.

## Published curriculum and historical releases

The experiment teaching text, editable origins and preserved original editions now live in separate paths:

- [One Cup Chemistry experiment index (OCC-00 to OCC-19)](one-cup-chemistry/experiments/README.md) and [original illustrated PDFs](one-cup-chemistry/original-editions/).
- [One Cup Chemistry v0.2 complete release](one-cup-chemistry/releases/v0.2/) preserves the exact original publication ZIP as checksum-verified parts with a tested rebuilder.
- [Kitchen Inquiry Lab original editable DOCX and guides](kitchen-inquiry-lab/original-editions/).
- [Nothing Is Free v0.3 phone-first historical source](nothing-is-free/releases/v0.3/), with a development-only security warning.
- [Core12 PRO Unit 8 original Flux PDF](recovered-publications/CORE12_PRO_Unit_8_Flux_Original_2026/), preserved in checksum-verified binary segments with a tested rebuilder.
- [LAB-12/PDP-12-inspired cooling instrumentation](https://github.com/RandoSY/software-defined-laboratory/tree/main/platforms/lab12-pdp12-linc/v1.2) is maintained in the separate SDL repository.

See the [Project Atlas archival progress report](https://github.com/RandoSY/project-atlas/blob/main/baselines/ARCHIVAL_PROGRESS_ADDENDUM_2026-11-03.md) for exact published/remaining status and automated integrity evidence.

**Archival publication is not hardware or classroom validation.** Earlier versions and incomplete prototypes are retained rather than overwritten.
