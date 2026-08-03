# Small-`n` evidence boundary

This directory stores small independent audit artifacts and immutable identities for the reviewed `n=3,4,5` submission. It does not duplicate the 53 MB PDF, the 102 MB reviewer submission, or the omitted multi-gigabyte SAT layer.

## External source identities

| Artifact | SHA-256 | Embedded here |
|---|---|---|
| `perm345_reviewer_submission_20260802_v9_ams_hardened.zip` | `70b9a059389b6cf7b4c2988f9f012d06a14b86963775df4fe619ddce61016309` | no |
| `perm345_v9_ams_hardened_reviewer.pdf` | `a5d2360b70dc3faba1a6ffcac6dc1345b839214e94b7c8791200ccb3448117de` | no |

## Independent-review status

- `n=3`: accepted.
- `n=4`: independently exact-replayed.
- `n=5`: no new fatal mathematical counterexample found; lower-16 overlay substantially replayed; full external verdict remains conditional because the omitted lower-15 SAT/DRAT layer was not independently regenerated in the review environment.
