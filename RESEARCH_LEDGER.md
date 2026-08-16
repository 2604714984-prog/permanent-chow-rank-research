# Research ledger

## Purpose

This is the canonical high-level ledger for the active permanent Chow-rank
research repository.  `STATUS.md` remains the detailed theorem inventory.
This file records milestones, numerical boundaries, active stacked branches,
superseded or rejected routes, and the next authorized mathematical
interfaces.

Every result that changes a theorem, numerical bound, counterexample, route
barrier, equality classification, or open frontier must update this file in
the same pull request.  This is one Markdown index, not a registry, database,
manager, dispatcher, or second workflow layer.

Last consolidated: **2026-08-16**  
Consolidation base: PR #45 theorem head
`0b7cabcee339207921e0167d699cb0de7eaf38e0`.

## Status vocabulary

- `ACCEPTED_BASELINE`: canonical small-`n` result on merged mainline.
- `PROOF_DRAFT_COMPLETE`: the mathematical argument is written; external
  review may remain pending.
- `COMPUTATION_REPLAYED`: the stated finite interface has deterministic replay.
- `RESTRICTED_FAMILY_THEOREM`: exact only for a named proper subclass.
- `ROUTE_DIAGNOSTIC`: a valid result used to select or reject a route.
- `STACKED_DRAFT`: valid only on the named open PR stack until merged.
- `SUPERSEDED`: retained for provenance but not canonical.
- `REJECTED`: an attempted implication was found invalid before promotion.
- `OPEN`: the stated frontier is not closed.

## 1. Current numerical boundaries

| Object | Current accessible repository boundary | Status | Primary location |
|---|---:|---|---|
| `perm_3` | `ChowRank=4` | `ACCEPTED_BASELINE` | merged small-`n` proof |
| `perm_4` | `ChowRank=8` | `ACCEPTED_BASELINE` | merged exact rational proof |
| `perm_5` | `ChowRank=16` | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | merged PR #30 |
| `perm_6` | `28 <= ChowRank <= 32` | lower bound draft; exact value open in accessible repository | PR #31 |
| `perm_7` | `44 <= ChowRank <= 64` | `STACKED_DRAFT` | PRs #35, #38, #45 and current PR |
| `perm_8` | `79 <= ChowRank <= 128` | `STACKED_DRAFT` | current PR |
| `perm_9` | `ChowRank >= 142` | `STACKED_DRAFT` | PR #38 |
| `perm_10` | `ChowRank >= 268` | `STACKED_DRAFT` | PR #38 |
| `perm_11` | `ChowRank >= 508` | `STACKED_DRAFT` | PR #38 |
| `perm_12` | `ChowRank >= 970` | `STACKED_DRAFT` | PR #38 |
| `perm_13` | `ChowRank >= 1855` | `STACKED_DRAFT` | PR #38 |
| `perm_14` | `ChowRank >= 3570` | `STACKED_DRAFT` | PR #38 |
| `perm_15` | `ChowRank >= 6883` | `STACKED_DRAFT` | PR #38 |
| `perm_16` | `ChowRank >= 13315` | `STACKED_DRAFT` | PR #38 |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition.  No
unrestricted exact result for `perm_6`, `perm_7`, or `perm_8` is present in the
currently accessible repository state.

## 2. Canonical small-`n` chain

\[
\operatorname{ChowRank}(\operatorname{perm}_3)=4,\qquad
\operatorname{ChowRank}(\operatorname{perm}_4)=8,\qquad
\operatorname{ChowRank}(\operatorname{perm}_5)=16.
\]

The `n=3` proof is linear algebra.  The `n=4` proof combines the `560/92`
Koszul baseline, low-rank quadratic classification, the exact `psi_v` chart
and the double-quotient inequality.  The repaired `n=5` proof preserves the
coupled-catalectic firewall, routes all 58 fixed-six states and binds the
non-finite bridges and deterministic certificates at the merged PR #30
boundary.

## 3. General-`n` theorem stack

| ID | Statement | Status | PR / document |
|---|---|---|---|
| `G-PROFILE` | Any lower-bound method factoring only through scalar derivative dimensions is capped at the central binomial coefficient. | merged proof draft | PR #32 |
| `G-SIGN` | `ColumnSignRank(perm_n)=RowSignRank(perm_n)=2^(n-1)`. | merged restricted-family theorem | PR #33 |
| `G-AFFINE-SLICE` | The Boolean slice has affine-Segre rank `d+1`; sign rigidity does not extend to arbitrary complex diagonal ratios. | merged route diagnostic | PR #34 |
| `G-KOSZUL` | General first-Koszul, quotient-gain, parity-asymptotic and fixed-offset multishadow formulas. | proof draft | general docs / `STATUS.md` |
| `G-MACAULAY` | Vector-valued first prolongation satisfies `dim K^(1)<=dim(K)^{<2>}`. | proof draft, replayed | general relation docs |
| `G-EXACT-SHADOW` | Exact simultaneous product-shadow minimum is a Ferrers integer program. | stacked draft, independent replay | PR #35 |
| `G-NESTED-SHADOW` | A zero-intersection block can be projected away inside a nonzero-intersection multishadow proof. | stacked draft | PR #38 |
| `G-PAIR-OVERLAP` | Transverse shared-factor pairs have intersection `binom(s,m)`; a zero-common-factor block rotation has intersection `2^m binom(r,m)`. | stacked draft, replayed | PR #41 |
| `G-DUAL-FRAME-OVERLAP` | For same-span independent frames, quadratic literal overlap is sharply bounded by `binom(n,2)-ceil((n-s_dual)/2)`; KK gives higher-degree caps. | stacked draft, replayed | PR #44 |
| `G-FACTOR-SPAN-ZERO` | A joint factor span of dimension `<m^2` has zero intersection with `D_m(perm_n)`; low-span quotient intersections are exact. Applied to two fixed terms, this gives `ChowRank(perm_7)>=44`. | PR #45 stacked draft | PR #45 |
| `G-PERM-CENTER` | For every `m>=3`, the concise Hessian center of `perm_m` is scalar. Minimal-shadow permanent derivatives are direct-sum indecomposable; this closes the `n=8,m=4` transverse equality span and gives `ChowRank(perm_8)>=79`. | current stacked draft, combinatorial and independent matrix replay | current PR |

## 4. `perm_6` milestone chain

```text
first Koszul / shadow routes     21 -> 22 -> 23
fixed-four and relation routes   24
fixed-six vector Macaulay        25
average-subset closure           26
exact product shadow             27
final all-alpha=3 geometry       28
```

Current accessible frontier:

```text
28 <= ChowRank(perm_6) <= 32
```

The lower-29 program remains partial.  Broad scalar state trees, complete sign
families and uncorrected quotient-intersection shortcuts are closed routes.

## 5. Exact product shadows and equality geometry

PR #35 proves the exact product-shadow transitions

\[
F_{7,4}(238)=452,\quad F_{7,4}(239)=456,
\]

\[
F_{8,4}(560)=784,\quad F_{8,4}(561)=793.
\]

PR #38 embeds certified zero-intersection blocks and yields 43 and 78.  PR #45
removes a universal two-term block at `n=7`, giving 44.  The current center
theorem closes the `n=8` equality-span pair and gives 79.

PR #39 studies

\[
\mathfrak X=
\{S\in\operatorname{Gr}(560,\mathcal D_4(\operatorname{perm}_8)):
\dim\partial S\le784\}.
\]

At each coordinate flag point:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

Chow realizability of this equality locus remains open.

## 6. Pairwise and block-overlap frontier

PR #41 proves the transverse common-factor formula and block-rotation
counterexample.  PR #44 gives the sharp same-span dual-frame bound.  PR #45
proves that a block with joint factor-span dimension `<m^2` is invisible to
the permanent derivative space and that the matched-difference image vanishes
there.

The current theorem computes the concise Hessian center of every `perm_m`,
`m>=3`, and proves it is scalar.  By torus specialization and upper
semicontinuity of the center on the moving essential-space bundle, every
minimal-shadow permanent derivative is direct-sum indecomposable.

For `n=8,m=4`, every pair of Chow factor spans has joint dimension at most 16.
Below 16 PR #45 applies; at 16 the spans are complementary eight-planes and a
nonzero intersection vector would be a nontrivial direct sum with minimal
shadow.  Therefore every two-term block is zero in
`D_4(perm_8)`, including the transverse equality case.

The complete pairwise central matched-difference problem at `n=8` is now
closed.  Five-term flat-sum geometry is not.

## 7. Restricted sign-family results

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical one- and two-defect calculations remain diagnostics.  Further sign
dictionary enumeration is not active.

## 8. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- The implication from quotient-image overlap to an equally large
  matched-difference space was rejected until literal overlap was included.
- Common primal-factor count alone is rejected as a global overlap parameter.

PRs #41, #44 and #45 repair the pair sequence.  The current center theorem
closes the remaining `n=8` equality-span pair.

## 9. Active pull-request stack

```text
PR #31 broad n=6/general research head
  -> PR #35 exact product shadows
      -> PR #38 nested zero-intersection removal
          -> PR #39 perm_8 equality tangent cone
              -> PR #41 consolidated ledger + pairwise overlap
                  -> PR #44 dual-frame same-span overlap
                      -> PR #45 factor-span zero blocks
                          -> current PR permanent-center equality closure
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 10. Current open mathematical interfaces

1. **Five-term valuation-leading flat sums.**  
   The complete two-term `n=8,m=4` boundary is closed.  PR #43 gives a
   coordinate five-term cap 40, while lower 80 requires the general cap 146.
   Control the at least 107 possible nonliteral flat-sum directions.

2. **Chow realizability of exact-shadow equality spaces.**  
   Determine whether a coupled fourteen-term sum can realize the four-
   dimensional `perm_8` equality locus.

3. **Lower-29 `perm_6` frontier.**  
   Continue only with a theorem acting on the surviving `b=31,...,49`
   geometry; do not recreate a broad scalar state tree.

4. **General correction beyond shadow cardinality.**  
   Seek a frame-sensitive, multigraded or representation-valued invariant
   beyond the Ferrers minimum.

## 11. Mandatory update rule

Every meaningful future result must update this file in the same pull request.
Each entry records date, stable ID, status, statement, evidence, boundary,
PR/theorem head, replay status, superseded dependencies and next interface.

Promotion rules:

- never call an open stacked result canonical on `main`;
- never promote finite-field equality without the characteristic-zero
  direction;
- never replace a coupled catalectic image by a literal sum without a theorem;
- include counterexamples and rejected shortcuts;
- do not add a manager, registry, dispatcher or database for this ledger;
- update this one Markdown file and theorem-specific proof/evidence files.
