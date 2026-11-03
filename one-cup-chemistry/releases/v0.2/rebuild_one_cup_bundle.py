#!/usr/bin/env python3
"""Reconstruct the byte-identical One Cup Chemistry v0.2 archival ZIP."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
import sys

HERE = Path(__file__).resolve().parent
PARTS = HERE / "archive-parts"
NAME = "One_Cup_Chemistry_Complete_Bundle_v0_2.zip"
EXPECTED_SIZE = 4311975
EXPECTED_SHA256 = "047d7bd32a49b7bd78137736b270d699263c8c0ac859424398373988ce86525b"
EXPECTED_PART_SHA256 = [
    "e58c5e014438b1a9b6a93913f953354c8ca5d61966def8e326c5ad32da553a15",
    "f0ff099ea4bd40dd1e926595dd3ebfc9ebc82f2a45e060e40d78f230859f9222",
    "5e6c5ecf176d5374ca434a427b317e5f1bca2a7e8c0996fc5c021c6d88d6ff1c",
    "4de224d0c03a188dec1668f9d44e5fd16a32433a99a0f87cf078703e81d096ca",
    "90022e34048860221f63b1a56757aa54d7a11a89bb68c66ffa3fa65fbda17453",
]

def main() -> int:
    target = HERE / NAME
    if target.exists():
        print(f"Not overwriting existing {target}; move it first if necessary.", file=sys.stderr)
        return 2
    parts = [PARTS / f"{NAME}.part{i:02d}" for i in range(1, 6)]
    for part, expected in zip(parts, EXPECTED_PART_SHA256):
        if not part.is_file():
            print(f"Missing part: {part}", file=sys.stderr)
            return 2
        actual = sha256(part.read_bytes()).hexdigest()
        if actual != expected:
            print(f"SHA-256 mismatch: {part}", file=sys.stderr)
            return 2
    digest = sha256()
    length = 0
    with target.open("xb") as out:
        for part in parts:
            with part.open("rb") as src:
                while block := src.read(1024 * 1024):
                    out.write(block)
                    digest.update(block)
                    length += len(block)
    if length != EXPECTED_SIZE or digest.hexdigest() != EXPECTED_SHA256:
        target.unlink()
        print("Output did not match original. Deleted invalid output.", file=sys.stderr)
        return 1
    with ZipFile(target) as archive:
        bad = archive.testzip()
        if bad is not None:
            target.unlink()
            print(f"ZIP member failed CRC: {bad}", file=sys.stderr)
            return 1
    print(f"Restored original: {target}")
    print(f"SHA-256: {EXPECTED_SHA256}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
