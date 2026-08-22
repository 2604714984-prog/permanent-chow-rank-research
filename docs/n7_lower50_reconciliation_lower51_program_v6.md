# `perm_7` lower-50 reconciliation and lower-51 launch program v6

## Status and claim boundary

`ACTIVE RECONCILIATION / PROMOTION PROGRAM — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Active PR #31 input HEAD: `8b79743dec8bba93390135e56c23635e86272049`  
Divergent Rethlas candidate HEAD: `107912a550cc4688b160e69008e7f7bb33650447`  
Common merge base: `111a022c8de36619c32a0c2cf660aa4dd5b5aeab`  
Active branch: `agent/general-column-sign-rank`

Two mathematically relevant lines now coexist.

1. The active PR line has completed the v4 common-graph theorem (`B1-CLOSED`)
   and has reduced unrestricted lower 50 to one arbitrary Packet-B
   identifiability problem and one Packet-A refined-representation problem.
2. The independent Rethlas snapshot contains a corrected working proof
   blueprint claiming
   \[
   \operatorname{ChowRank}(\operatorname{perm}_7)\ge 50,
   \]
   by excluding both 49-term endpoint packets in degrees three and four.

The Rethlas commit is **not an ancestor of PR #31**. It has deterministic
subclaim replays and internal model audits, but no whole-proof verification,
no GitHub Actions receipt on that exact commit, and no named independent human
review. Therefore the repository must neither ignore it nor promote it
uncritically.

The first objective of v6 is decisive:

```text
L50-AUDIT-PASS-AND-INTEGRATED
or
L50-EXPLICIT-LOAD-BEARING-GAP
```

Only after the first status is frozen may the lower-51 workstreams activate.
Until then, the active-branch public interval remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

No border-rank, exact-rank-64, positive-characteristic, or general-`n` claim is
made by this package.

## Why v6 supersedes v5 as the immediate execution package

The v5 structural program correctly targeted the two open endpoint packets on
the active branch. The later Rethlas snapshot supplies a substantially shorter
candidate bypass: a direct-basis middle-degree projection theorem followed by
separate contradictions for endpoint A and endpoint B.

Accordingly:

- v5 remains the **fallback repair program** if the Rethlas proof fails;
- v6 is the **immediate audit, reconciliation, and promotion program**;
- lower-51 tasks in v6 are gated and dormant until lower 50 passes.

## Program size

The package contains 15 modules and 208 numbered theorem-facing tasks.

| Module | Tasks | Purpose |
|---|---:|---|
| `00_branch_reconciliation.md` | 12 | freeze the two divergent lines and one proof boundary |
| `01_section_caps_and_span_floors.md` | 14 | independently audit the exact erasure recursion |
| `02_universal_slope_ten_audit.md` | 16 | audit every factor rank and quotient orientation |
| `03_global_endpoint_classification.md` | 14 | rebuild the two exhaustive 49-term packets |
| `04_apolar_middle_projection.md` | 16 | audit the corrected degree-3/4 projection theorem |
| `05_endpoint_a_exclusion.md` | 12 | audit the all-rank-seven matroid contradiction |
| `06_endpoint_b_exclusion.md` | 14 | audit the mixed graph-complement contradiction |
| `07_replay_sources_and_ci.md` | 12 | exact replay, external theorem checks, and CI |
| `08_integration_and_promotion.md` | 14 | selective integration or exact-gap fallback |
| `09_lower51_defect_budget.md` | 16 | derive the complete 35-unit near-equality budget |
| `10_lower51_packet_classification.md` | 18 | classify all feasible 50-term structural packets |
| `11_lower51_permanent_obstructions.md` | 16 | attack the surviving 50-term packets |
| `12_section_route_optional.md` | 10 | optional coordinate-section route after lower 50 |
| `13_execution_waves_and_stop_rules.md` | 12 | continuous execution and hard stop rules |
| `14_evidence_and_adversarial_audit.md` | 12 | evidence scope, survivor schema, and final signoff |

## Required next replanning threshold

Do not replan after a few replays or another interface note. Replanning is
allowed only after at least one of:

```text
L50-AUDIT-PASS
L50-EXPLICIT-LOAD-BEARING-GAP
L50-INTEGRATED-AND-PROMOTED
N50-DEFECT-FRONTIER-FROZEN
N50-PACKET-CLASSIFICATION-COMPLETE
LOWER-51-PROMOTABLE
EXACT-50-TERM-SURVIVOR
```

## Immediate execution order

```text
Wave 0: BR-01..BR-12, SC-01..SC-14
Wave 1: LS-01..LS-16, GE-01..GE-14, MP-01..MP-16
Wave 2: A49-01..A49-12, B49-01..B49-14, EV-01..EV-12
Wave 3: IP-01..IP-14
Wave 4: only after L50 promotion, activate N50/L51 and optional section work
```

The detailed gates and stop rules are in Module 13.
