# Research ledger

High-level ledger for the active permanent Chow-rank project. `STATUS.md`
retains the detailed historical inventory. This file records only the current
boundaries, active theorem stack, route barriers, and next interfaces.

Last consolidated: **2026-08-21**  
Active branch: `research/quartic-six-circuit-compatibility`.

## Numerical boundaries

| Object | Current boundary | Status |
|---|---:|---|
| `perm_3` | `ChowRank=4` | accepted baseline |
| `perm_4` | `ChowRank=8` | accepted baseline |
| `perm_5` | `ChowRank=16` | proof draft complete, replayed |
| `perm_6` | `28 <= ChowRank <= 32` | exact value open |
| `perm_7` | `49 <= ChowRank <= 64` | stacked draft |
| `perm_8` | `90 <= ChowRank <= 128` | stacked draft |
| `perm_9` | `164 <= ChowRank <= 256` | stacked draft |
| `perm_10` | `307 <= ChowRank <= 512` | stacked draft |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition. No
unrestricted exact value is proved for `perm_6` or larger `n`.

## Active quartic block frontier

Let `mu(n,m)` be the least number of degree-`n` Chow derivative blocks whose
literal output-degree-`m` sum meets `D_m(perm_n)` nontrivially. At `(6,4)`,

\[
\boxed{6\leq\mu(6,4)\leq8}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      OPEN
eight blocks      NONZERO
```

Inherited restricted thresholds at `(6,4)` are 12 for coordinate blocks and 8
for row-separated, column-separated, and normalized sign blocks. Any six-block
witness gives a unique full-support six-element quotient circuit, and all
fixed four-column slices of one component come from the same 15-dimensional
squarefree factor-label source.

## New route barrier

Status:

```text
PROOF_DRAFT_COMPLETE
COMPUTATION_REPLAYED
STRICT_ROUTE_BARRIER
```

For nonzero coordinate leading components supported on exactly two perfect
matchings, every support-minimal rank-five six-circuit has one of four support
types:

```text
six-cycle 13 orbits; theta 1; tight handcuff 5; loose handcuff 18.
```

For the regular common-source first-order map `L`, kernel `K`, and quadratic
term `B(K,K)`, the matching-support maxima are respectively `6, 5, 8, 6`,
while `perm_4` has support 24. Therefore this entire regular two-jet stratum
cannot produce a nonzero diagonal-torus transform of `perm_4`.

Frozen core:

```text
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

It does not prove `mu(6,4)>=7`.

## General theorem stack retained

- exact product-shadow and derivative-tower bounds;
- scalar-tower ceiling `O(n^(1/4) binom(n,floor(n/2)))`;
- exact sign-family rank `2^(n-1)` and continuous affine-slice ceiling `n`;
- apolar subquotient and Boolean term-envelope theorems;
- factor-span zero blocks and recursive polar descent;
- partition-Laplace envelopes and the complete cubic block threshold;
- quartic four-block, order-eight three-block, and order-six five-block zero
  theorems.

These are stacked drafts where indicated by their original PRs; they are not
canonical on `main` until merged.

## Closed default routes

Without a new non-scalar or Chow-realizability input, do not return to:

- scalar derivative profiles or the complete scalar tower;
- isolated Boolean coefficient slices with arbitrary continuous ratios;
- bounded two-direction ideal or matrix-image scalarizations;
- raw Fitting/Betti or exact-additive `K_0` scalarizations;
- fixed matching-projected postprocessing;
- direct coordinate, separated, or compressed sign constructions for six
  quartic blocks.

A route ceiling is not an upper bound on actual Chow rank.

## Next interfaces

1. Complete coordinate two-jet analysis for one- and two-singleton circuits,
   retaining unused coordinate factors.
2. Analyze zero leading matching projection components.
3. Only then move to noncoordinate initial circuits, multigrade collision
   trees, and the simultaneous repeated-column layers `(2,1,1)`, `(2,2)`,
   `(3,1)`, `(4)`.
4. In parallel, seek a uniform Chow-realizability defect or a representation-
   valued invariant that is not reducible to scalar dimensions.
5. A cross-`n` recurrence such as `R_n>=2R_(n-1)` remains open; ordinary row
   expansion is not additive enough.

## Validation and promotion boundary

The current packet checks compressed certificate shards and hashes, replays an
independent exact modular reconstruction at deterministic generic points,
verifies the canonical frozen theorem core, and passes focused tests and
`py_compile`. Hosted CI must finish before the branch is described as green.

Every later mathematical result must update this file and `RESEARCH_HANDOFF.md`
in the same PR. Do not promote finite-field evidence without a characteristic-
zero argument or identify coupled catalectic images with literal sums without a
theorem.
