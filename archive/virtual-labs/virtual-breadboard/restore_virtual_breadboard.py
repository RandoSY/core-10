#!/usr/bin/env python3
"""Restore the recovered Virtual Breadboard Thermal Control Lab HTML.

The GitHub estate stores the gzip archive as base64 text so it can be written
losslessly through the text-oriented connector. This script reverses that
encoding and verifies the exact recovered HTML before writing it.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

ARCHIVE_B64 = Path(__file__).with_name(
    "virtual_breadboard_thermal_lab_v2_2.html.gz.b64"
)
OUTPUT = Path(__file__).with_name("virtual_breadboard_thermal_lab_v2_2.html")
EXPECTED_SHA256 = "20bfe7fc4dfc3d5f7bbdfad5e96ec76579325138a56077cdb03535750f235b14"
EXPECTED_SIZE = 98066
EXPECTED_GZIP_SHA256 = "2e85f9983975eb57832687f38c633db8f90b174385f359092f92836544da9c3d"
EXPECTED_GZIP_SIZE = 29042


def main() -> None:
    gzip_bytes = base64.b64decode(ARCHIVE_B64.read_text(encoding="ascii"))
    gzip_digest = hashlib.sha256(gzip_bytes).hexdigest()

    if len(gzip_bytes) != EXPECTED_GZIP_SIZE:
        raise SystemExit(
            f"Gzip size mismatch: expected {EXPECTED_GZIP_SIZE}, got {len(gzip_bytes)}"
        )
    if gzip_digest != EXPECTED_GZIP_SHA256:
        raise SystemExit(
            f"Gzip SHA-256 mismatch: expected {EXPECTED_GZIP_SHA256}, got {gzip_digest}"
        )

    data = gzip.decompress(gzip_bytes)
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
