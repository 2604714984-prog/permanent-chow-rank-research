# `perm_3`, `perm_4`, and `perm_5` v13 reviewer artifacts

This directory freezes the 2026-08-10 v13 candidate and its complete reviewer
package.

| File | Bytes | SHA-256 |
|---|---:|---|
| `perm345_chow_rank_v13_pure_reviewer_candidate_20260810.pdf` | 3,356,995 | `02A08C053375D9CDE315073E5F068FCC758E5DF9038A228B0F8507882371C61E` |
| `perm345_reviewer_submission_v13_pure_20260810.zip` | 1,274,242 | `AFA3E8165BB7D7F90DE46C983D5DE971F38289906735369AAC34F4B27F9B7EDD` |

The paper is in Chinese. An English mathematical summary is available at
`docs/perm5_lower16_v13_pure_finite_combinatorial_summary.md`.

The PDF has 47 pages and 101 embedded source or diagnostic files. The ZIP has
105 entries and includes a manifest verifier and clean-build instructions. The
largest unpacked file is the 3.36 MB PDF; no historical 10 GB asset is included.

Run the asset verifier from the repository root:

```text
python evidence/small_n/v13_pure/verify_assets.py
```

Internal status: `PROOF_DRAFT_COMPLETE`. External mathematical review is still
pending. The exact programs in the package are redundant diagnostics rather
than logical premises of the v13 lower bound.
