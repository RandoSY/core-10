#!/usr/bin/env python3
"""Rock inquiry bench and analysis. Python 3.10+, standard library only."""
import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

FIELDS = ("pile", "rock_id", "repeat", "length_mm", "width_mm", "thickness_mm",
          "girth_mm", "dry_mass_g", "initial_ml", "submerged_ml", "volume_method",
          "shape_volume_cm3", "area_cm2", "shape_boundary", "notes")
REGION_FIELDS = ("pile", "rock_id", "scheme", "region", "hull_cm3", "occupied_cm3")
NUMBERS = FIELDS[3:10] + FIELDS[11:13]
METRICS = dict(length_mm="mm", width_mm="mm", thickness_mm="mm", girth_mm="mm",
               dry_mass_g="g", axis_ratio="ratio", ellipsoid_cm3="cm3",
               displacement_cm3="cm3", density_g_cm3="g/cm3", wadell="ratio",
               void_mean_pp="percentage points", void_sd_pp="percentage points")


def rows(path, fields):
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(fields):
            raise ValueError(f"{path}: use the supplied CSV header and field order")
        for index, row in enumerate(reader, 2):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f"{path}:{index}: wrong number of fields")
            yield index, {k: v.strip() for k, v in row.items()}


def number(text, key, allow_zero=False):
    if not text:
        return None
    value = float(text)
    if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"{key} must be {'nonnegative' if allow_zero else 'positive'} and finite")
    return value


def measure(row):
    for name in ("pile", "rock_id", "repeat"):
        if not row[name]:
            raise ValueError(f"{name} is required")
    n = {k: number(row[k], k, k == "initial_ml") for k in NUMBERS}
    out = {k: (n[k], "") for k in ("length_mm", "width_mm", "thickness_mm",
                                   "girth_mm", "dry_mass_g") if n[k] is not None}
    length, width, thickness = (n[k] for k in ("length_mm", "width_mm", "thickness_mm"))
    if None not in (length, width, thickness):
        if not length >= width >= thickness:
            raise ValueError("record perpendicular full dimensions in descending L, W, T order")
        out["axis_ratio"] = (thickness / length, "")
        out["ellipsoid_cm3"] = (math.pi / 6 * length * width * thickness / 1000, "")
    start, end = n["initial_ml"], n["submerged_ml"]
    if (start is None) != (end is None):
        raise ValueError("enter both cylinder readings or neither")
    if start is not None:
        method = row["volume_method"]
        if method not in {"direct", "water-accessible"} or end <= start:
            raise ValueError("cylinder rise must be positive and volume_method direct or water-accessible")
        displacement = end - start
        out["displacement_cm3"] = (displacement, method)
        if n["dry_mass_g"] is not None:
            out["density_g_cm3"] = (n["dry_mass_g"] / displacement, method)
    elif row["volume_method"]:
        raise ValueError("volume_method is only for paired cylinder readings")
    volume, area = n["shape_volume_cm3"], n["area_cm2"]
    if (volume is None) != (area is None) or (volume is not None) != bool(row["shape_boundary"]):
        raise ValueError("Wadell requires shape volume, surface area, and a matching boundary label")
    if volume is not None:
        value = (36 * math.pi * volume ** 2) ** (1 / 3) / area
        if value > 1.000001:
            raise ValueError(f"sphericity {value:.5f} exceeds 1; check units, area and boundary")
        out["wadell"] = (value, row["shape_boundary"])
    if not out:
        raise ValueError("enter at least one measured value")
    return out


def read_measurements(path):
    values, known, seen = defaultdict(list), set(), set()
    for line, row in rows(path, FIELDS):
        try:
            key = (row["pile"], row["rock_id"], row["repeat"])
            if key in seen:
                raise ValueError(f"duplicate reading {key}")
            result = measure(row)
            seen.add(key)
            known.add(key[:2])
            for (metric, (value, convention)) in result.items():
                values[(*key[:2], metric, convention)].append(value)
        except (ValueError, OverflowError) as exc:
            raise ValueError(f"{path}:{line}: {exc}") from exc
    return values, known


def regional_values(path, known):
    groups, seen = defaultdict(list), set()
    for line, row in rows(path, REGION_FIELDS):
        try:
            key = tuple(row[name] for name in REGION_FIELDS[:4])
            if not all(key) or key[:2] not in known or key in seen:
                raise ValueError("region needs a known rock, a scheme, and a unique region ID")
            hull = number(row["hull_cm3"], "hull_cm3")
            occupied = number(row["occupied_cm3"], "occupied_cm3", True)
            if hull is None or occupied is None or occupied > hull:
                raise ValueError("require 0 <= occupied volume <= hull volume and hull > 0")
            seen.add(key)
            groups[key[:3]].append((hull, occupied))
        except (ValueError, OverflowError) as exc:
            raise ValueError(f"{path}:{line}: {exc}") from exc
    for (pile, rock, scheme), regions in sorted(groups.items()):
        if len(regions) < 2:
            raise ValueError(f"{pile}/{rock}/{scheme}: at least two regions are required")
        total = math.fsum(h for h, _ in regions)
        center = 100 * math.fsum(h - o for h, o in regions) / total
        spread = math.sqrt(math.fsum(h * (100 * (h-o)/h - center)**2 for h,o in regions) / total)
        label = f"{scheme}; k={len(regions)}"
        yield (pile, rock, "void_mean_pp", label), [center]
        yield (pile, rock, "void_sd_pp", label), [spread]


def write_rows(path, fields, records):
    with open(path, "w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(fields)
        writer.writerows(records)


def report(args):
    values, known = read_measurements(args.csv)
    if args.regions:
        values.update(regional_values(args.regions, known))
    entries = [(key, statistics.mean(v), len(v), max(v) - min(v)) for key, v in sorted(values.items())]
    if args.output:
        write_rows(args.output, ("pile", "rock_id", "metric", "convention", "value", "reading_n",
                                  "repeat_range"), ((*k, val, n, spread if n > 1 else "")
                                                    for k, val, n, spread in entries))
    print(f"Operational question: {args.question}")
    print(f"Scope: {args.scope}; property: {args.metric}; units: {METRICS[args.metric]}")
    if args.metric == "axis_ratio":
        print("Shortest/longest axis is a shape proxy, not Wadell sphericity.")
    if args.metric == "density_g_cm3":
        print("Dry mass / displaced volume. Water-accessible results are protocol-dependent.")
    chosen = [(key, val, n, r) for key, val, n, r in entries if key[2] == args.metric]
    if not chosen:
        raise ValueError("no valid data for that property; missing values are not zero")
    conventions = sorted({k[3] for k, _, _, _ in chosen})
    for convention in conventions:
        print(f"\nConvention: {convention or 'standard bench measurement'}")
        piles = defaultdict(list)
        for (pile, rock, _, label), val, n, spread in chosen:
            if convention != label:
                continue
            piles[pile].append(val)
            detail = f", {n} repeats, repeat range {spread:.5g}" if n > 1 else ""
            print(f"  {pile}/{rock}: {val:.6g}{detail}")
        if args.scope == "within":
            print("Each value above describes regions of one rock, not spread between rocks.")
            continue
        if args.scope == "within-pile":
            for pile, data in sorted(piles.items()):
                summary = f"range={max(data)-min(data):.6g}, SD={statistics.pstdev(data):.6g}" if len(data)>1 else "spread not assessed (one rock)"
                print(f"  Pile {pile}: n={len(data)}, mean={statistics.mean(data):.6g}, {summary}")
        else:
            centers = [statistics.mean(v) for _, v in sorted(piles.items())]
            for pile, data in sorted(piles.items()):
                print(f"  Pile {pile}: n={len(data)}, mean={statistics.mean(data):.6g}")
            if len(centers) > 1:
                print(f"  Across equally weighted pile means: n={len(centers)}, range={max(centers)-min(centers):.6g}")
            else:
                print("  Between-pile spread not assessed (one pile under this convention).")


def bench(args):
    path = Path(args.csv)
    if path.exists() and path.stat().st_size:
        _, _ = read_measurements(path)
        used = {(r["pile"], r["rock_id"], r["repeat"]) for _, r in rows(path, FIELDS)}
    else:
        write_rows(path, FIELDS, [])
        used = set()
    print("Blank = not measured. Enter mm, g and mL. Press Enter at Pile to stop.")
    while (pile := input("Pile: ").strip()):
        rock = input("Rock ID: ").strip()
        repeat = input("Repeat ID [1]: ").strip() or "1"
        raw = input("L W T in mm (three values or blank): ").split()
        if raw and len(raw) != 3:
            print("Enter exactly three dimensions or leave the field blank.")
            continue
        dims = raw or [""]*3
        mass = input("Dry mass (g): ").strip()
        initial = input("Initial cylinder level (mL): ").strip()
        final = input("Submerged cylinder level (mL): ").strip() if initial else ""
        method = input("Volume method (direct or water-accessible): ").strip() if initial else ""
        girth = input("String girth (mm, optional): ").strip()
        notes = input("Orientation / instrument / notes: ").strip()
        row = dict(zip(FIELDS, [pile, rock, repeat, *dims, girth, mass, initial, final, method,
                                "", "", "", notes]))
        try:
            result = measure(row)
            if (pile, rock, repeat) in used:
                raise ValueError("that rock/repeat ID already exists")
        except (ValueError, OverflowError) as exc:
            print(f"Not saved: {exc}. Try again.")
            continue
        with open(path, "a", encoding="utf-8", newline="") as stream:
            csv.writer(stream).writerow(row.values())
        used.add((pile, rock, repeat))
        for name in ("displacement_cm3", "density_g_cm3"):
            if name in result:
                print(f"  {name}: {result[name][0]:.5g} ({result[name][1]})")
        print("Saved.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    c = sub.add_parser("capture", help="append bench readings interactively")
    c.add_argument("csv")
    r = sub.add_parser("report", help="analyze one explicitly chosen property and scope")
    r.add_argument("csv")
    r.add_argument("--regions", help="CSV of measured or modeled regions")
    r.add_argument("--scope", required=True, choices=["within", "within-pile", "between-piles"])
    r.add_argument("--metric", required=True, choices=METRICS)
    r.add_argument("--question", required=True, help="your team's operational question")
    r.add_argument("--output", help="optional per-rock CSV export")
    args = parser.parse_args()
    try:
        if args.command == "report":
            if args.scope == "within" and args.metric not in {"void_mean_pp", "void_sd_pp"}:
                raise ValueError("within-rock scope requires a regional metric and a region file")
            if args.output and Path(args.output).resolve() in {Path(p).resolve() for p in (args.csv,args.regions) if p}:
                raise ValueError("output must not overwrite an input CSV")
            report(args)
        else:
            bench(args)
    except (ValueError, OverflowError, OSError, csv.Error) as exc:
        parser.exit(2, f"Error: {exc}\n")
    except (EOFError, KeyboardInterrupt):
        parser.exit(0, "\nCapture stopped. Previously accepted rows are saved.\n")


if __name__ == "__main__":
    main()
