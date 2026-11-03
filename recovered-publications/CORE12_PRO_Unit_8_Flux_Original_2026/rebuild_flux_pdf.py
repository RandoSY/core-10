#!/usr/bin/env python3
"""Rebuild exact illustrated original Core12 PRO Unit 8 PDF from binary parts."""
from pathlib import Path
from hashlib import sha256
import sys

HERE = Path(__file__).resolve().parent
NAME = "CORE12_PRO_Unit_8_Its_All_About_the_Flux.pdf"
SIZE = 7152568
HASH = "68e58cd5cc4434b7466b32509782b1fe792c9bd1e6caf168d427f0f3a23bc100"
PART_HASHES = [
    "73a760128175baa4f54876ada96f07da70a0fc605c22f8a66a109033ee2d597e",
    "adbb766ab1ade140f52a4817d3e65da3731b1c699069764afd79a58fdcdd6b94",
    "f46b06c56884f286f848fe65961c2edf1f8f154181ca7a4a60e94a4643c95a88",
    "bda8e9935c65d9dd5930eefb1e8ca27ef3228e9bf88a2724b0abf376bea45b18",
    "a3d8f98e094bc370901b0618b5e51effd52f625edd8c3026f1c1b9449ed2a655",
    "41f0a70387bcc05c24d21c4f3d85d0e8c869b775a1aa97b45de0a792f55a52f8",
    "ea7244d825b55ef08a193f2be9b4c62fb85d0afe96572b0f2436c3f7292b0401",
    "7554cfe07bf4b3b9afe918c55c08325e0c8c79d3a482209d1a06f063d65ca96b"
]

def main():
    target = HERE / NAME
    if target.exists():
        print("Refusing to overwrite existing PDF", file=sys.stderr)
        return 2
    digest = sha256()
    length = 0
    for n, expected in enumerate(PART_HASHES, 1):
        part = HERE / "archive-parts" / f"{NAME}.part{n:02d}"
        if not part.is_file() or sha256(part.read_bytes()).hexdigest() != expected:
            print(f"Missing or damaged part: {part}", file=sys.stderr)
            return 2
    with target.open("xb") as out:
        for n in range(1, len(PART_HASHES)+1):
            with (HERE / "archive-parts" / f"{NAME}.part{n:02d}").open("rb") as f:
                while block := f.read(1048576):
                    out.write(block)
                    digest.update(block)
                    length += len(block)
    if length != SIZE or digest.hexdigest() != HASH:
        target.unlink()
        print("Reconstructed PDF failed SHA-256 and/or size; output deleted", file=sys.stderr)
        return 1
    if not target.read_bytes().startswith(b"%PDF-"):
        target.unlink()
        print("Not a valid PDF header", file=sys.stderr)
        return 1
    print(f"Restored {NAME} ({length} bytes, SHA-256 {HASH})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
