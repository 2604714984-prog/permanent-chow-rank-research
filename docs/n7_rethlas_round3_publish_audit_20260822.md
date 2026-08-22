# Publication audit — Rethlas `perm_7` generation 3

- Replay start: `2026-08-22T14:23:02Z`
- Replay end: `2026-08-22T14:24:35Z`
- Base repository commit: `107912a550cc4688b160e69008e7f7bb33650447`
- Execution: serial, fail-fast, `python3`

## Repository checks

- English-only proof-tree scan: `ENGLISH_ONLY_TEXT_SCAN_PASS`.
- Full unit suite: 141 tests passed in 54.817 seconds.
- Whitespace check: `git diff --check` passed.

## Rethlas snapshot replay

`python3 scripts/rethlas_perm7_20260822/replay_all.py` completed with `RETHLAS_PERM7_20260822_REPLAY_PASS`.

The newly added structural certificate completed with `N50_RANK_ONE_SUPPORT_AUDIT_PASS`. It checks:

- uniqueness of the positive increment profile `(1,6,7,7,7,7,7,7)` under the exact surplus budget;
- the closed Boolean incidence-rank formula for support sizes one through seven;
- explicit matrix ranks modulo `1000003` and `1000033`;
- the contradiction for rank-one support size at least three after the sharp quadratic-intersection loss.

The replay verifies the stated conditional structural theorem. It does not prove `ChowRank(perm_7)=64`, exclude all 50-term decompositions, or constitute whole-problem verification.
