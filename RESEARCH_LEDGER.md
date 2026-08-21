# Research ledger

## Purpose

This is the high-level ledger for the active permanent Chow-rank repository.
`STATUS.md` and Git history retain the detailed theorem inventory. This file
records current numerical boundaries, active route barriers, pull-request
ancestry, and the next mathematically decisive interfaces.

Last consolidated: **2026-08-21**
Active branch: `research/quartic-six-circuit-compatibility`
Active Draft PR: **#92**.

## 1. Current numerical boundaries

| Object | Current accessible boundary | Status |
|---|---:|---|
| `perm_3` | `ChowRank=4` | accepted baseline |
| `perm_4` | `ChowRank=8` | accepted baseline |
| `perm_5` | `ChowRank=16` | proof draft complete, replayed |
| `perm_6` | `28 <= ChowRank <= 32` | exact value open |
| `perm_7` | `49 <= ChowRank <= 64` | stacked draft |
| `perm_8` | `90 <= ChowRank <= 128` | stacked draft |
| `perm_9` | `164 <= ChowRank <= 256` | stacked draft |
| `perm_10` | `307 <= ChowRank <= 512` | stacked draft |
| `perm_11` | `ChowRank >= 508` | earlier stacked bound |
| `perm_12` | `ChowRank >= 970` | earlier stacked bound |
| `perm_13` | `ChowRank >= 1855` | earlier stacked bound |
| `perm_14` | `ChowRank >= 3570` | earlier stacked bound |
| `perm_15` | `ChowRank >= 6883` | earlier stacked bound |
| `perm_16` | `ChowRank >= 13315` | earlier stacked bound |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition. No
unrestricted exact value is proved for `perm_6` or larger `n`.

## 2. Active quartic literal-block frontier

Let `mu(n,m)` be the least number of degree-`n` Chow derivative blocks whose
literal output-degree-`m` sum meets `D_m(perm_n)` nontrivially. At `(6,4)`,

\[
\boxed{6\le\mu(6,4)\le8}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      OPEN
eight blocks      NONZERO
```

The five-block zero theorem is on PR #89. Restricted thresholds at `(6,4)` are
12 for coordinate blocks and 8 for row-separated, column-separated, and
normalized sign blocks. Any hypothetical six-block witness gives a unique
full-support six-element quotient circuit. Every fixed four-column slice of a
component comes from the same 15-dimensional squarefree factor-label source.

## 3. Coordinate regular two-jet program

### 3.1 Two-supported components

Status:

```text
PROOF_DRAFT_COMPLETE
COMPUTATION_REPLAYED
STRICT_ROUTE_BARRIER
```

If all six leading matching projections are nonzero, supported on exactly two
perfect matchings, and form a support-minimal rank-five circuit, the support
multigraph is a six-cycle, theta, tight handcuff, or loose handcuff. All gain
strata are covered. Exact regular two-jet matching-support maxima are

```text
six-cycle          6
theta               5
loose handcuff      6
tight handcuff      8
perm_4             24
```

Frozen core:

```text
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

### 3.2 Positive-singleton components

A support-minimal rank-five coordinate six-circuit with nonzero leading
matching projection on every component has at most two singleton components.
The exact support families are

```text
one singleton:  square lollipop or double-edge tail
two singletons: endpoint-marked P5
three or more:  impossible
```

Row-column orbit counts are `5`, `29`, and `18`. Each singleton includes all
130 valid unordered repeated-factor frames obtained from two unused factors
chosen with repetition from the sixteen coordinate cells.

For frame `E` and leading support `S`, every second-order matching lies in

\[
\{M:|M\cap E|\ge3\}
\cup
\{M:\exists M_0\in S,\ |M\cap M_0|\ge2\}.
\]

Exact exhaustive maxima are

```text
square lollipop       22
double-edge tail      22
endpoint-marked P5    23
perm_4                24
```

Frozen core:

```text
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### 3.3 Combined consequence

Every regular coordinate six-circuit two-jet with six nonzero leading
matching projections is incompatible with a nonzero diagonal-torus transform
of `perm_4`. The remaining coordinate boundary is a component with zero
leading matching projection.

This result does **not** prove `mu(6,4)>=7`.

## 4. General theorem stack retained

The active repository retains:

- exact product-shadow and derivative-tower bounds;
- the scalar-tower ceiling `O(n^(1/4) binom(n,floor(n/2)))`;
- exact sign-family rank `2^(n-1)` and the continuous affine-slice ceiling `n`;
- apolar subquotient and Boolean term-envelope theorems;
- factor-span zero blocks and recursive polar descent;
- partition-Laplace envelopes and the complete cubic block threshold;
- quartic four-block, order-eight three-block, and order-six five-block zero
  theorems; and
- the coordinate regular two-jet barriers above.

These are stacked drafts where indicated by their original PRs. They are not
canonical on `main` until merged or rebased into a clean main-target PR.

## 5. Closed default routes

Without a new non-scalar or Chow-realizability input, do not return to:

- scalar derivative profiles or the complete scalar tower;
- isolated Boolean coefficient slices with arbitrary continuous ratios;
- bounded two-direction ideal or matrix-image scalarizations;
- raw Fitting/Betti or exact-additive `K_0` scalarizations;
- fixed matching-projected postprocessing;
- direct coordinate, separated, or compressed sign constructions for six
  quartic blocks; or
- additional enumeration inside the now-closed all-positive coordinate
  regular two-jet strata.

A route ceiling is not an upper bound on actual Chow rank.

## 6. Active pull-request ancestry

```text
broad general stack: PR #31 -> #35 -> #38 -> ... -> #56
quartic literal-block tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
```

PR #92 is based on exact PR #89 head
`4804e9a948fa0602c062d167f0474d1346dbcab9`.

## 7. Current open interfaces

Immediate priority:

1. **Zero-leading coordinate components.** Classify coordinate six-factor
   components whose leading perfect-matching projection vanishes. Determine
   the first nonzero valuation grade and whether it forces a proper
   subcircuit, an already excluded separated family, a finite exact survivor,
   or a six-block witness.

After that boundary:

2. **Noncoordinate and multigrade six-circuit compatibility.** Analyze
   noncoordinate initial circuits, leading-dependent collision trees, and the
   repeated-column layers `(2,1,1)`, `(2,2)`, `(3,1)`, `(4)`.
3. **Uniform Chow-realizability defects.** Separate exact-shadow spaces from
   spaces realizable by sums of Chow derivative blocks.
4. **Representation-valued invariants.** Retain `S_n x S_n` isotypes,
   multigraded syzygies, or frame-sensitive information not reducible to
   scalar dimensions.
5. **Cross-`n` recurrence.** A compatible restriction or valuation theorem
   such as `R_n>=2R_(n-1)` remains open; ordinary row expansion is not additive
   enough.

Do not open a broad nonlinear solver or general third-order framework before
the zero-leading coordinate boundary is resolved.

## 8. Validation and promotion boundary

The positive-singleton packet passes exact primary and independent replays in
normal and optimized Python, frozen-payload equality, five focused tests,
`py_compile`, and diff checks. Hosted CI for its theorem head remains pending.

The first PR #92 commit repairs the inherited exact-product-shadow hash
expectation (`3563...` to checked-in `18eb...`) without changing the theorem
payload.

Never promote a finite-field equality without the characteristic-zero
argument, identify a coupled catalectic image with a literal sum without a
theorem, or call an open stacked result canonical on `main`.
