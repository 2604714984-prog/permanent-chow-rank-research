# `perm_7` lower-51 decisive near-equality program v7

## Status and claim boundary

`ACTIVE LOWER-51 THEOREM PROGRAM — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-23  
Frozen input HEAD: `199a99abc80e72084d3a3d81c71a54957b680288`  
Active research PR: `#31`  
Active branch: `agent/general-column-sign-rank`

The promoted ordinary characteristic-zero interval is

\[
\boxed{50\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

The sole promotion target of this package is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq51}.
\]

No border-rank, positive-characteristic, exact-rank-64, or general-`n` claim
is made here.

## Why v7 supersedes the lower-51 portion of v6

V6 completed its primary objective: it independently reconstructed, repaired,
integrated, replayed, and promoted the ordinary lower bound 50.  The second-pass
audit is

```text
docs/n7_lower50_v6_second_pass_audit_20260823.md
```

The old v6 Modules 09--12 were a launch skeleton written before two later
conditional advances were frozen:

1. the simple all-rank-seven direct-basis 50-term branch is impossible;
2. the all-rank-seven no-direct-basis branch has, in every ordering, positive
   increment profile `(1,6,7,7,7,7,7,7)`, and the rank-one quotient functional
   is supported on at most two actual factors.

V7 consumes those results, the exact 35-unit defect identity, and the
lower-50 countermodels.  It does not repeat the lower-50 proof.

## Program size

```text
15 modules
234 theorem-facing tasks
1449 module lines
```

| Module | Tasks | Purpose |
|---|---:|---|
| `00_v6_handoff_and_audit.md` | 12 | v6 handoff and lower-50 audit freeze |
| `01_exact_defect_calculus.md` | 18 | exact 35-unit defect calculus |
| `02_section_floors_and_minimality.md` | 14 | section floors and minimality |
| `03_polymatroid_packet_classification.md` | 20 | polymatroid and packet classification |
| `04_rank7_direct_basis_branches.md` | 18 | all-rank-seven direct-basis branches |
| `05_rank7_no_direct_basis_branch.md` | 20 | all-rank-seven no-direct-basis branch |
| `06_rank6_mixture_branches.md` | 20 | rank-six mixture branches |
| `07_low_factor_rank_branches.md` | 14 | low-factor-rank exceptional branches |
| `08_residual_middle_module.md` | 18 | residual middle module |
| `09_permanent_specific_invariants.md` | 18 | permanent-specific nonlinear invariants |
| `10_exact_elimination_and_survivors.md` | 14 | exact elimination and survivor protocol |
| `11_optional_section_route.md` | 10 | optional coordinate-section route |
| `12_universal_bypass.md` | 12 | universal bypass invariant |
| `13_evidence_audit_and_promotion.md` | 14 | evidence, adversarial audit, and promotion |
| `14_execution_waves_and_stop_rules.md` | 12 | execution waves and stop rules |

## Primary execution strategy

```text
25% exact defect calculus, section floors, and exhaustive packet table
20% all-rank-seven direct-basis and no-direct-basis branches
20% rank-six and low-factor-rank mixture branches
15% residual middle module and multiplication propagation
10% permanent-specific nonlinear invariants / universal bypass
10% exact survivors, independent replay, audit, and promotion
```

This is a mathematical priority allocation, not a scheduler.

## Accepted inputs

- `ChowRank(perm_7) >= 50` is promoted and is not reproved.
- Every hypothetical 50-term identity is minimal.
- The total near-equality budget is 35 units.
- The rank-seven local surplus row is
  `(0,22,29,26,17,14,7,0)`.
- The simple all-rank-seven multilinear-matroid branch is closed.
- The no-direct-basis all-rank-seven branch has profile `1+6+7^6` and
  rank-one support at most two.
- Scalar slope data alone are insufficient: an exact representable
  countermodel saturates the 35-unit budget.
- Plain labelled `2/5` and `3/4` induction maps are not reopened as
  standalone obstructions.

## Required terminal outcomes

The package must return one of:

```text
LOWER-51-PROMOTABLE
EXACT-50-TERM-IDENTITY
LOWER-51-OPEN-AT-ONE-EXPLICIT-THEOREM-GAP
```

The third outcome is acceptable only after the N50 packet table is exhaustive
and every other branch is closed.

## First major checkpoint

The first checkpoint is intentionally large.  It requires all of:

```text
D-01..D-18
S-01..S-14
P-01..P-20
RM-01..RM-08
N7-01..N7-10
```

and at least one of:

```text
R7-DIRECT-CLOSED
R7-NOBASIS-CLOSED
RANK6-MIXTURES-CLOSED
UNIVERSAL-REDUCTION
a verified full 50-term identity
```

Do not replan after one new table, one bounded family, or one finite-field
sample.

## Explicit stop rules

The following do not count as progress:

- rerunning lower-50 section caps or endpoint audits under new names;
- treating scalar or support data as a permanent identity;
- unrestricted random factor searches;
- unrestricted `GL_49` scans;
- enlarging sign, shear, monomial-curve, or transposition boxes without a
  theorem-defined component;
- rebuilding automatic plain `2/5` or `3/4` inclusions;
- inferring termwise splitting from a global exact sequence;
- using target-torus weights without coefficient transport;
- promoting finite-field nonexistence to characteristic zero;
- building schedulers, databases, registries, or experiment-management
  infrastructure.

## Promotion gate

The repository may state

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\geq51
\]

only when:

```text
[ ] the local atom catalog and 35-unit identity are exact;
[ ] the 50-term represented packet table is exhaustive;
[ ] every rank-seven direct-basis branch is closed;
[ ] the rank-seven no-direct-basis support-one and support-two branches are closed;
[ ] every rank-six mixture is closed;
[ ] every low-factor-rank branch is closed;
[ ] all chart and degeneration boundaries are covered;
[ ] no full 50-term identity survives;
[ ] every load-bearing computation has characteristic-zero evidence;
[ ] independent mathematical audit has no fatal or major finding;
[ ] exact-head CI passes.
```

## Post-promotion boundary

After lower 51 is promoted, the next package should analyze a hypothetical
51-term identity with a 70-unit budget.  Exact rank 64 is not automatically
the next executable target.
