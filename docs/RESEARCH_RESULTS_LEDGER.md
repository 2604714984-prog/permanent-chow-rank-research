# Permanent Chow-rank research results ledger

## Purpose

This file is the human-readable index of the active mathematical record.  It
separates merged results, stacked proof drafts, route barriers, superseded
experiments, and unresolved interfaces.  Every future theorem, strict route
barrier, counterexample, or improved numerical bound must update this ledger
in the same commit that introduces the result.

The repository is an active pure-mathematics research repository.  A pull
request is not a theorem merely because its exact arithmetic replays.  Each
entry below records both its evidence status and its claim boundary.

Last organized boundary: `2026-08-16`.

## Status vocabulary

- `MERGED_CANONICAL`: present on `main`.
- `PROOF_DRAFT_COMPLETE`: written mathematical chain is internally complete.
- `EXACT_REPLAYED`: the stated finite interface has deterministic exact replay.
- `ROUTE_DIAGNOSTIC`: useful exact information that does not itself improve an
  unrestricted Chow-rank bound.
- `ROUTE_CEILING`: proves that a precisely defined method cannot improve beyond
  a stated value without an additional invariant.
- `SUPERSEDED`: retained only for provenance and must not be cited as active.
- `OPEN`: unresolved.

## Canonical small-degree results

| Object | Current result | Evidence status | Canonical location |
|---|---:|---|---|
| `perm_3` | `ChowRank=4` | merged exact linear-algebra proof | repaired `n=3,4,5` proof boundary on `main` |
| `perm_4` | `ChowRank=8` | merged exact rational/combinatorial proof | repaired `n=3,4,5` proof boundary on `main` |
| `perm_5` | `ChowRank=16` | merged computer-assisted proof draft with exact replay | PR #30 / `main` |
| `perm_6` | `28 <= ChowRank <= 32` on the accessible research branch | lower 28 proof draft; exact value not present in the accessible GitHub boundary | PR #31 |

The `perm_5` proof must retain the coupled/literal firewall: for a fixed sum
`R=sum_i T_i`, the coupled catalectic image is only contained in the literal
sum of the individual derivative spaces unless a separate theorem proves
 equality.

## Merged general results

| ID / PR | Result | Status | Strict boundary |
|---|---|---|---|
| G-022 / PR #32 | every lower-bound functional using only scalar derivative-space dimensions is capped by `binom(n,floor(n/2))` | `MERGED_CANONICAL`, `ROUTE_CEILING` | does not constrain natural Koszul, Young, syzygy, or coupled-module maps |
| G-023 / PR #33 | full normalized column-sign and row-sign rank of `perm_n` is exactly `2^(n-1)` | `MERGED_CANONICAL`, restricted-family theorem | arbitrary complex row-homogeneous and unrestricted Chow rank remain open |
| G-024 / PR #34 | the same Boolean slice has affine-Segre rank `n` in the continuous anchored dictionary | `MERGED_CANONICAL`, `ROUTE_CEILING` | a slice theorem, not an `n`-term decomposition of the full permanent |

## Active stacked general-`n` research

| PR | Exact result at its current boundary | Status | Next dependency |
|---:|---|---|---|
| #35 | exact simultaneous product-shadow formula; `perm_7>=42`, `perm_8>=77`; complete coordinate equality classification at the active `perm_8` threshold | `PROOF_DRAFT_COMPLETE`, `EXACT_REPLAYED` | Chow-realizability of equality families |
| #38 | nests the pre-existing zero-intersection block inside exact/nonzero multishadow bounds; `perm_7>=43`, `perm_8>=78` | `PROOF_DRAFT_COMPLETE`, `EXACT_REPLAYED` | nonzero block-intersection control |
| #39 | at a `perm_8` coordinate flag equality point: tangent dimension 27, 256 independent quadrics, reduced tangent-cone support `4xA^4 + 8xA^3 + 7xA^1`, global equality-locus dimension 4 | `PROOF_DRAFT_COMPLETE`, `ROUTE_DIAGNOSTIC` | restrict the coupled Chow incidence to the explicit branches |
| #40 | exact iterated product shadows plus nonzero block projection; `perm_7>=45`, `perm_8>=79` | `PROOF_DRAFT_COMPLETE`, `EXACT_REPLAYED` | a Chow-specific improvement over arbitrary-subspace block caps |
| #42 | recursively nested one-block route ceiling and consolidated ledger | `ROUTE_CEILING`, exact integer optimization | prove a five-term `perm_8` cubic-intersection cap at most 146 |

## Active `perm_6` frontier

PR #31 contains the long-running `perm_6` branch.  Its current accessible
claim is

```text
28 <= ChowRank(perm_6) <= 32.
```

The branch also contains the lower-29 frontier and many strict sublocus
reductions.  Historical status lines earlier in the PR body are superseded by
its latest lower-28 section.  The full sign-family value 32 is a restricted
family theorem and must not be reported as unrestricted exact rank.

## Superseded or rejected drafts

| PR | Disposition |
|---:|---|
| #26 | rejected historical `perm_5` v13 candidate; superseded by repaired v14 boundary |
| #29 | stacked repair branch; superseded by merged clean PR #30 |
| #36 | closed unmerged after identifying the proposed factor-span theorem as a special case of an existing canonical theorem |
| #37 | closed unmerged after identifying the hereditary-profile theorem and asymptotic as pre-existing repository results |

A correct numerical corollary does not create a new theorem when its
mathematical input is already canonical.  Prior-result attribution must be
checked before promotion.

## Current ordinary lower bounds carried by the active stack

| Degree | Lower bound | Glynn upper bound | Source |
|---:|---:|---:|---|
| 3 | 4 | 4 | canonical small-degree proof |
| 4 | 8 | 8 | canonical small-degree proof |
| 5 | 16 | 16 | canonical small-degree proof |
| 6 | 28 | 32 | PR #31 |
| 7 | 45 | 64 | PR #40 |
| 8 | 79 | 128 | PR #40 |
| 15 | 6883 | 16384 | PR #38 reviewed-certificate reuse |

These are ordinary characteristic-zero statements.  No row in this table is a
border-Chow-rank claim unless separately labelled.

## Closed research routes

The following routes have a proved ceiling or an explicit counterexample and
must not be restarted without a new invariant:

1. scalar derivative-dimension profiles and nonnegative direct sums;
2. uniform, defect, and full normalized sign dictionaries;
3. the single Boolean diagonal slice extended to arbitrary anchored complex
   diagonal ratios;
4. monotone scalar second-Koszul homology upper bounds;
5. mechanical recursive row expansion without a term-allocation theorem;
6. repeated recursive nesting of the current one-block exact-shadow projection
   at `n=7`, and at central output degree for `n=8`, beyond the ceilings recorded
   in PR #42.

## Current primary mathematical target

For `n=8`, let

```text
E_3 = D_3(perm_8).
```

The next finite interface is the Chow-realizable five-term block cap

```text
dim(E_3 intersect sum_{i=1}^5 D_3(T_i)) <= 146.
```

The arbitrary-subspace iterated-shadow cap is 160.  A reduction by fourteen
is sufficient, through the exact outer shadow at fixed count twenty, to prove
`ChowRank(perm_8)>=80`.  This target is strictly stronger than classifying one
compressed equality family and is the first place where a genuine
`Delta_Chow>0` correction can change the current bound.

## Update protocol

Every future research commit must add or update one ledger row containing:

```text
statement
repository/PR boundary
proof status
exact-replay status
claim boundary
superseded dependencies
next unresolved interface
```

Failed attempts that expose a reusable logical barrier must also be recorded.
Numerical experiments, finite-field observations, or solver failures are
`diagnostic` until an exact characteristic-zero transfer and a complete
coverage argument are written.
