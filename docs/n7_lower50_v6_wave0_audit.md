# `perm_7` v6 Wave-0 reconciliation and section-cap audit

## Decision

```text
TWO-HEADS-FROZEN
DIVERGENCE-RECEIPT
RECONCILIATION-GATE-PASS
SECTION-CAPS-AUDIT-PASS
WAVE0-DECIDED
```

This note opens the v6 core-proof audit.  It does **not** promote the
lower bound 50.  The active public interval remains `49..64` until Modules
02--08 pass.

## Frozen branch receipt

| role | commit | tree | parent |
|---|---|---|---|
| v6 active input | `8b79743dec8bba93390135e56c23635e86272049` | `468c417253f5196667ba2e43f5c08e53097f6e51` | `b426f462e632ff103d6a9d653a9c7266f1fee393` |
| Rethlas candidate | `107912a550cc4688b160e69008e7f7bb33650447` | `14495e67b2c77046dedb25a7228c68c433c3e99f` | `111a022c8de36619c32a0c2cf660aa4dd5b5aeab` |
| v6 package | `b5c01e6f7ff44a5b616ae4e6b24598ce5bfff865` | `045b7ccf1246fde8bae6a779732d2b28c427e552` | `8b79743dec8bba93390135e56c23635e86272049` |

The exact candidate proof is
`docs/n7_ordinary_chow_rank_lower50.md` at blob
`2e322ccc6b823721244962844e43a0815c804402`.  The merge base of the active
input and candidate is `111a022c8de36619c32a0c2cf660aa4dd5b5aeab`.
The active input has 199 commits not in the candidate; the candidate has one
commit not in the active input.  `git merge-base --is-ancestor` rejects the
candidate as an ancestor of the active input.  These facts give
`DIVERGENCE-RECEIPT`; moving branch names are not used as evidence.

## Claim and dependency maps

The candidate's lower-50 chain is:

1. apolar dimensions and Shafiei quadratic generation;
2. Bukh compression plus the finite Ferrers recursion for section caps;
3. one-term and pair factor-span floors;
4. cubic/quadratic permanent intersection lemmas;
5. rank-six profiles and the universal slope-ten tables;
6. the global filtration and the two exhaustive 49-term endpoints;
7. corrected degree-three/four direct-basis projection;
8. separate endpoint-A and endpoint-B contradictions.

The theorem-facing candidate file is the blob above.  Its supporting source
tree is `docs/rethlas_perm7_20260822/`, with deterministic diagnostics under
`scripts/rethlas_perm7_20260822/`.  The proof also names three load-bearing
replay families under an unpublished `results/perm7_complete_problem/`
path.  Only the section-cap source and payload were present in the local
artifact archive; the rank-six full-profile pair and slope-table pair were
not committed in the candidate.  This is a Wave-1 evidence gap, not a Wave-0
mathematical contradiction.

The active v5 line consists of the audited lower 49, the common-graph
`B1-CLOSED` result, arbitrary Packet-B identifiability modules, Packet-A
Koszul/Pluecker/second-order modules, and the explicit automaticity barriers.
Its compact index is `docs/n7_lower50_structural_closure_program_v5.md` and
`docs/n7_lower50_v5/00_v4_terminal_handoff.md` through
`09_cross_packet_decision_logic.md`.

## Cross-line lemma matrix

| subject | active v5 | candidate | relation |
|---|---|---|---|
| section caps and span floors | used by the lower-49/frontier line | reused as `C6(47)=37`, `C6(48)=44` | same finite recursion, independently replayed below |
| local slope ten | partial endpoint structure | full all-rank/all-quotient lemma | candidate stronger; Wave 1 audit required |
| endpoint classification | Packet-A/Packet-B frontier | two exhaustive equality packets | candidate stronger; Wave 1 audit required |
| plain `2/5`, `3/4` induction | proved automatic/insufficient | not used | consistent |
| middle projection | absent | corrected basis-supported degree `3/4` theorem | new load-bearing bridge |
| endpoint contradictions | branch-specific v5 tools | direct algebra-multiplication bypass | candidate shorter; v5 remains fallback |
| quadratic surjectivity | counterexamples/barrier | explicitly retracted | consistent correction |

Repository-facing status therefore remains `NO-PREMATURE-PROMOTION`.
Only load-bearing proof text, exact compact replays, negative controls, and
source receipts may be imported (`SELECTIVE-INTEGRATION-RULE`).

## Evidence scope and correction digest

- theorem proof: the pure arguments in the frozen candidate blob;
- exact finite certificate: section caps, rank-six profiles, slope tables;
- modular falsifier only: arbitrary-orientation slope search;
- diagnostics only: tangent, Tor, residual-flag, and exact-64 route probes;
- conditional result: simple 50-term branch exclusion;
- route barriers: false quadratic surjectivity and automatic plain induction.

The old reversed apolar degree and the one-term/pair quadratic-surjectivity
claims remain rejected.  The candidate replacement uses degree-three/four
Gorenstein duality and full middle symbols.  Audit outcomes are restricted to
`AUDIT-PASS`, `AUDIT-PASS-WITH-MINOR-REPAIRS`, `MAJOR-GAP`, or `FATAL-GAP`.

## Section-cap proof audit

Let `W` be the intersection of the permanent derivative space `E_d` with
the derivatives of `a` selected Chow terms.  Projection modulo their sum and
the remaining `q-a` terms gives

```text
dim(E intersect (A+B)) <= dim(E intersect A) + dim(B).
```

The row-column torus preserves `E_d`.  Its generic characters distinguish
the row-subset/column-subset basis, so the Grassmann limit of `W` is a
coordinate family with the same dimension.  The derivative-shadow rank can
only drop in the special fibre.  Since the original shadow lies in the
corresponding degree-`d-1` selected-term intersection, the limit shadow has
dimension at most `C_(d-1)(a)`.  Bukh compression then replaces it by a
coordinatewise colex-monotone family of equal size and no larger shadow.
For two coordinates this is a Ferrers diagram, and disjoint shadow fibres
give the exact finite cost used by the dynamic programs.  This proves the
recursion direction and the minimization over `a`.

Dependent or repeated factors cause no exception: each remaining term has
degree-`d` derivative dimension at most `binom(7,d)`, while the selected
intersection is handled directly as the subspace `W`.  No generic
intersection-dimension claim is imported from a specialization.

Bukh's arXiv `1009.2375v2`, Theorem 1, supplies the simultaneous-shadow
inequality; Lemma 2 supplies an equal-size monotone compression with no
larger shadow; Lemma 3 identifies its shadow via one-dimensional colex
shadows.  The finite Ferrers cost and recursion are repository-derived
consequences, not statements attributed verbatim to the paper.

## Exact replay receipt

The active implementation is `scripts/n7_lower50_section_caps_audit.py` and
the frozen payload is `data/n7_lower50_section_caps_audit.json`.

- all `C_d(q)` for `d=1..6`, `q=0..49` are frozen;
- colex shadows agree with explicit subset enumeration;
- area-indexed and budget-indexed Ferrers programs agree at every budget;
- the five degree scans each check all 173,525 integer partitions of 49;
- an independent `n=3`, `r=2` control exhausts all 512 coordinate families;
- focused unit tests replay the payload and negative boundary values;
- the run is streaming/bounded and materializes no million-scale family.

The load-bearing values are

```text
C6(47) = 37
C6(48) = 44
```

Hence a hypothetical 49-term identity forces
`dim L_i >= 49-44 = 5` and
`dim(L_i+L_j) >= 49-37 = 12`.  Consequently either every term has factor
rank six or seven, or there is exactly one rank-five term and all other
terms have rank seven.

No fatal or major Wave-0 finding remains.  Modules 02--04 may now run; the
lower-50 claim itself remains unpromoted.
