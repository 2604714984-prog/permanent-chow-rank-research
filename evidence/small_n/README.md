# Small-`n` evidence boundary

This directory stores small independent audit artifacts and immutable identities for the reviewed `n=3,4,5` submission. It does not duplicate the large source PDF, the reviewer submission, or the omitted multi-gigabyte SAT layer.

## External source identities

| Artifact | SHA-256 | Embedded here |
|---|---|---|
| `perm345_reviewer_submission_20260802_v9_ams_hardened.zip` | `70b9a059389b6cf7b4c2988f9f012d06a14b86963775df4fe619ddce61016309` | no |
| `perm345_v9_ams_hardened_reviewer.pdf` | `a5d2360b70dc3faba1a6ffcac6dc1345b839214e94b7c8791200ccb3448117de` | no |
| corrected `n=5` C5 character aggregate | `2b254a51d0e641fa60eb0b7ced31f9ea7b299819b9dc49039a27c7a8c58bfb51` | compact summary only |

The exact Git blob identities of the committed audit files are recorded in `CONTENT_IDENTITIES.md`.

## Independent-review status

- `n=3`: accepted.
- `n=4`: independently exact-replayed.
- `n=5`: no new fatal mathematical counterexample found; lower-16 overlay substantially replayed; full external verdict remains conditional because the omitted lower-15 SAT/DRAT layer was not independently regenerated in the review environment.
- The 2026-08-09 C5 character-coordinate erratum withdraws a malformed aggregate and records its corrected finite-field ranks. This is a route diagnostic and does not change the conditional `n=5` theorem status.
