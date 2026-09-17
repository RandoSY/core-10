#!/usr/bin/env python3
"""Restore the recovered Virtual Breadboard Thermal Control Lab HTML.

This script intentionally has no third-party dependencies.
"""

from __future__ import annotations

import gzip
import hashlib
from pathlib import Path

ARCHIVE = Path(__file__).with_name("virtual_breadboard_thermal_lab_v2_2.html.gz")
OUTPUT = Path(__file__).with_name("virtual_breadboard_thermal_lab_v2_2.html")
EXPECTED_SHA256 = "20bfe7fc4dfc3d5f7bbdfad5e96ec76579325138a56077cdb03535750f235b14"
EXPECTED_SIZE = 98066


def main() -> None:
    data = gzip.decompress(ARCHIVE.read_bytes())
    digest = hashlib.sha256(data).hexdigest()

    if len(data) != EXPECTED_SIZE:
        raise SystemExit(
            f"Size mismatch: expected {EXPECTED_SIZE}, recovered {len(data)} bytes"
        )
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"SHA-256 mismatch: expected {EXPECTED_SHA256}, recovered {digest}"
        )

    OUTPUT.write_bytes(data)
    print(f"Restored: {OUTPUT.name}")
    print(f"Bytes:    {len(data)}")
    print(f"SHA-256: {digest}")
    print("Open the restored HTML in a modern browser.")


if __name__ == "__main__":
    main()
