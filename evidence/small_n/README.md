# Small-`n` evidence boundary

This directory stores small independent audit artifacts and immutable identities for the reviewed `n=3,4,5` submission. It does not duplicate the large source PDF, the reviewer submission, or the omitted multi-gigabyte SAT layer.

## External source identities

| Artifact | SHA-256 | Embedded here |
|---|---|---|
| `perm345_reviewer_submission_20260802_v9_ams_hardened.zip` | `70b9a059389b6cf7b4c2988f9f012d06a14b86963775df4fe619ddce61016309` | no |
| `perm345_v9_ams_hardened_reviewer.pdf` | `a5d2360b70dc3faba1a6ffcac6dc1345b839214e94b7c8791200ccb3448117de` | no |
| `perm345_reviewer_submission_v13_pure_20260810.zip` | `afa3e8165bb7d7f90de46c983d5de971f38289906735369aac34f4b27f9b7edd` | yes |
| `perm345_chow_rank_v13_pure_reviewer_candidate_20260810.pdf` | `02a08c053375d9cde315073e5f068fcc758e5df9038a228b0f8507882371c61e` | yes |
| `perm345_reviewer_submission_v14_repaired_20260812.zip` | `8ffd39148549543ee1d9c624ca8dc9dea44209f185800df67dab6c87419f3e51` | yes |
| `perm345_chow_rank_v14_repaired_zh_ams.pdf` | `960402fcb7bf16b51fc7c1fb4e641c5e982583a15ef1f38a9f5e6e866f94a7c8` | yes |

The Git blob identities of the legacy v9 audit files are recorded in
`CONTENT_IDENTITIES.md`; the v13 and v14 files use the SHA-256 release manifests
in `v13_pure/MANIFEST.json` and `v14_repaired/MANIFEST.json`.

## Independent-review status

- `n=3`: accepted.
- `n=4`: independently exact-replayed.
- `n=5`: external audit did not accept v13 as a closed proof. The repaired v14 internal draft supplies the missing characteristic-zero closed-incidence degeneration and replaces the unsupported terminal premise by an exact, independently replayable 886,464-flag certificate. Fresh independent review is pending.

The rejected v13 candidate is retained in `v13_pure/` for history only. The
repaired PDF, reviewer ZIP, immutable manifest, and active verifier are stored
in `v14_repaired/`; the English mathematical repair note is
`docs/perm5_lower16_v14_mathematical_repairs.md`.
