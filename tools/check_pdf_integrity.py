#!/usr/bin/env python3
"""Preflight every published PDF on a GitHub push and in weekly preservation CI.

Fail closed on missing expected PDFs, unexpected new PDFs, byte-level changes,
PDF parse errors, mismatched page counts, or pages that fail to rasterize.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import sys

import fitz  # PyMuPDF, second independent reader and rasterizer
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "measurement-ladder" / "PDF_INTEGRITY_BASELINE_2026-11-03.json"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def check(path: Path, item: dict) -> str:
    data = path.read_bytes()
    if len(data) != item["expected_size_bytes"]:
        raise ValueError(f"byte count mismatch: {len(data)} != {item['expected_size_bytes']}")
    actual = git_blob_sha1(data)
    if actual != item["expected_git_blob_sha1"]:
        raise ValueError(f"Git blob mismatch: {actual} != {item['expected_git_blob_sha1']}")
    expected256 = item.get("expected_sha256")
    if expected256 and hashlib.sha256(data).hexdigest() != expected256:
        raise ValueError("SHA-256 mismatch")
    if not data.startswith(b"%PDF-") or not data.rstrip().endswith(b"%%EOF"):
        raise ValueError("PDF signature or EOF marker invalid")

    reader = PdfReader(io.BytesIO(data), strict=True)
    if reader.is_encrypted:
        raise ValueError("Unexpected encrypted PDF")
    pages = len(reader.pages)
    if pages < 1 or (item.get("expected_pdf_pages") and pages != item["expected_pdf_pages"]):
        raise ValueError(f"Unexpected pypdf page count: {pages}")
    with fitz.open(stream=data, filetype="pdf") as doc:
        if doc.is_encrypted or doc.page_count != pages:
            raise ValueError("Independent PDF parser disagrees on pages")
        for i in range(pages):
            page = doc[i]
            pix = page.get_pixmap(matrix=fitz.Matrix(0.7, 0.7), alpha=False)
            if pix.width < 100 or pix.height < 100 or not pix.samples:
                raise ValueError(f"Page {i+1} cannot render")
    return f"{pages} pages, {len(data)} bytes, both render and hash checks passed"


def main() -> int:
    spec = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = {x["path"]: x for x in spec["pdfs"]}
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.pdf") if ".git" not in p.parts}
    failures = 0
    for rel in sorted(actual - set(expected)):
        print(f"FAIL UNTRACKED PDF: {rel}", file=sys.stderr)
        failures += 1
    for rel in sorted(set(expected) - actual):
        print(f"FAIL MISSING PDF: {rel}", file=sys.stderr)
        failures += 1
    for rel in sorted(actual & set(expected)):
        try:
            print(f"OK {rel}: {check(ROOT / rel, expected[rel])}")
        except Exception as e:
            failures += 1
            print(f"FAIL {rel}: {type(e).__name__}: {e}", file=sys.stderr)
    print(f"PDF archival check: {len(expected)} baseline PDFs, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
