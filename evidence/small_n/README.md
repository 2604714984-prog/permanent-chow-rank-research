# Small-`n` evidence boundary

This directory stores small independent audit artifacts and immutable identities for the reviewed `n=3,4,5` submission. It does not duplicate the large source PDF, the reviewer submission, or the omitted multi-gigabyte SAT layer.

## External source identities

| Artifact | SHA-256 | Embedded here |
|---|---|---|
| `perm345_reviewer_submission_20260802_v9_ams_hardened.zip` | `70b9a059389b6cf7b4c2988f9f012d06a14b86963775df4fe619ddce61016309` | no |
| `perm345_v9_ams_hardened_reviewer.pdf` | `a5d2360b70dc3faba1a6ffcac6dc1345b839214e94b7c8791200ccb3448117de` | no |
| `perm345_reviewer_submission_v13_pure_20260810.zip` | `afa3e8165bb7d7f90de46c983d5de971f38289906735369aac34f4b27f9b7edd` | yes |
| `perm345_chow_rank_v13_pure_reviewer_candidate_20260810.pdf` | `02a08c053375d9cde315073e5f068fcc758e5df9038a228b0f8507882371c61e` | yes |

The Git blob identities of the legacy v9 audit files are recorded in
`CONTENT_IDENTITIES.md`; the v13 files use the SHA-256 release manifest in
`v13_pure/MANIFEST.json`.

## Independent-review status

- `n=3`: accepted.
- `n=4`: independently exact-replayed.
- `n=5`: the v13 internal proof draft establishes lower 16 by finite combinatorics without using program output as a premise. Exact rational programs remain redundant diagnostics. Independent external review is pending.

The v13 binary artifacts, English summary, immutable manifest, and asset verifier
are stored in `v13_pure/`. The original paper is Chinese; the accompanying
English summary satisfies the repository language boundary and states the proof
and evidence limits explicitly.
