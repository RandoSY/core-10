# Public PDF preservation policy (CORE 10 / CORE 12)

Every new or replacement PDF must retain the exact original source (not an extracted-text substitute), with an auditable byte count and Git blob SHA-1. The automated PDF gate verifies the repository's **complete** set of PDFs, their immutable hashes, parseability in pypdf, and rasterizability on every page using PyMuPDF.

Before accepting a replacement:
1. Independently open the original local file, inspect all pages visually, confirm the text/tables and expected page count.
2. Calculate SHA-256 and Git blob SHA-1 of the **original bytes**.
3. Publish as a binary blob without UTF-8 conversion; use a leased commit if updating a branch.
4. Fetch the published Git tree and confirm the exact blob SHA and byte count.
5. Add/update the baseline entry in [PDF_INTEGRITY_BASELINE_2026-11-03.json](../measurement-ladder/PDF_INTEGRITY_BASELINE_2026-11-03.json) and run the [PDF Integrity Gate](../.github/workflows/pdf-integrity.yml).
6. Preserve a provenance note for corrections, keep historical editions under versioned filenames, and do not silently rebase old checksums.

The CI gate detects failures; actual prevention of merging failed checks also requires repository branch protection rules. PDFs may contain content that merits scientific or editorial review independently of structural integrity.
