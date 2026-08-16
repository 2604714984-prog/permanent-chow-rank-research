# Research ledger

## Purpose

This is the canonical high-level ledger for the active permanent Chow-rank
research repository. `STATUS.md` remains the detailed theorem inventory. This
file records milestones, numerical boundaries, active stacked branches,
superseded or rejected routes, and the next authorized mathematical
interfaces.

Every result that changes a theorem, numerical bound, counterexample, route
barrier, equality classification, or open frontier must update this file in
the same pull request. This is one Markdown index, not a registry, database,
manager, dispatcher, or second workflow layer.

Last consolidated: **2026-08-16**  
Consolidation base: PR #46 theorem head
`13a9a5911157df7e7fe69df3ee39da0547ff48c4`.

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
| `perm_6` | `28 <= ChowRank <= 32` | lower-bound draft; exact value open in accessible repository | PR #31 |
| `perm_7` | `45 <= ChowRank <= 64` | `STACKED_DRAFT` | current PR |
| `perm_8` | `80 <= ChowRank <= 128` | `STACKED_DRAFT` | current PR |
| `perm_9` | `ChowRank >= 142` | `STACKED_DRAFT` | PR #38 |
| `perm_10` | `ChowRank >= 268` | `STACKED_DRAFT` | PR #38 |
| `perm_11` | `ChowRank >= 508` | `STACKED_DRAFT` | PR #38 |
| `perm_12` | `ChowRank >= 970` | `STACKED_DRAFT` | PR #38 |
| `perm_13` | `ChowRank >= 1855` | `STACKED_DRAFT` | PR #38 |
| `perm_14` | `ChowRank >= 3570` | `STACKED_DRAFT` | PR #38 |
| `perm_15` | `ChowRank >= 6883` | `STACKED_DRAFT` | PR #38 |
| `perm_16` | `ChowRank >= 13315` | `STACKED_DRAFT` | PR #38 |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition. No
unrestricted exact result for `perm_6`, `perm_7`, or `perm_8` is present in the
currently accessible repository state.

## 2. Canonical small-`n` chain

\[
\operatorname{ChowRank}(\operatorname{perm}_3)=4,\qquad
\operatorname{ChowRank}(\operatorname{perm}_4)=8,\qquad
\operatorname{ChowRank}(\operatorname{perm}_5)=16.
\]

The `n=3` proof is linear algebra. The `n=4` proof combines the `560/92`
Koszul baseline, low-rank quadratic classification, the exact `psi_v` chart
and the double-quotient inequality. The repaired `n=5` proof preserves the
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
| `G-FACTOR-SPAN-ZERO` | A joint factor span of dimension `<m^2` has zero intersection with `D_m(perm_n)`; low-span quotient intersections are exact. | stacked draft | PR #45 |
| `G-PERM-CENTER` | For every `m>=3`, the concise Hessian center of `perm_m` is scalar. Minimal-shadow permanent derivatives are direct-sum indecomposable; this closes the `n=8,m=4` transverse two-term boundary. | stacked draft, replayed | PR #46 |
| `G-CROSS-DEGREE-PROJECTION` | Project a term block one derivative degree lower, retain the exact one-term permanent defect, and invert the exact upper shadow. This gives four-term and five-term cubic caps 41 and 112 and the ordinary bounds `perm_7>=45`, `perm_8>=80`. | current stacked draft, primary and independent replay | current PR |

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

The lower-29 program remains partial. Broad scalar state trees, complete sign
families and uncorrected quotient-intersection shortcuts are closed routes.

## 5. Exact shadows, centers and cross-degree projection

PR #35 proves

\[
F_{7,4}(238)=452,\quad F_{7,4}(239)=456,
\]

\[
F_{8,4}(560)=784,\quad F_{8,4}(561)=793.
\]

PR #38 embeds certified zero-intersection blocks. PR #45 closes low joint
factor spans, and PR #46 closes the remaining two-term equality span at the
central `n=8` degree using scalar Hessian centers.

The present theorem descends one derivative degree before applying the block
projection. For four degree-seven Chow terms it proves

\[
\dim\left(
D_3(\operatorname{perm}_7)
\cap\sum_{i=1}^{4}D_3(T_i)
\right)\le41.
\]

For five degree-eight Chow terms it proves

\[
\boxed{
\dim\left(
D_3(\operatorname{perm}_8)
\cap\sum_{i=1}^{5}D_3(T_i)
\right)\le112.
}
\]

The latter is a uniform characteristic-zero theorem, not a coordinate-limit
claim. It improves the previously sufficient lower-80 target 146 and yields
`ChowRank(perm_8)>=80`.

PR #39 separately classifies the reduced tangent cone at the `560/784`
`perm_8` exact-shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

## 6. Pairwise and block-overlap frontier

PR #41 proves the transverse common-factor formula and block-rotation
counterexample. PR #44 gives the sharp same-span dual-frame bound. PR #45
proves that low joint factor-span blocks are invisible to the permanent
space. PR #46 proves every central two-term block for `perm_8` is zero.

The current cross-degree theorem is the first result on the five-term cubic
block strong enough to change the numerical lower bound. It uses only literal
spaces and transfers to a coupled sum by containment.

The complete pairwise central matched-difference problem at `n=8` is closed.
The five-term cap is now 112; lower 81 would follow from the sufficient cap 90.

## 7. Restricted sign-family results

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical one- and two-defect calculations remain diagnostics. Further sign
dictionary enumeration is not active.

## 8. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- The implication from quotient-image overlap to an equally large
  matched-difference space was rejected until literal overlap was included.
- Common primal-factor count alone is rejected as a global overlap parameter.
- PR #43's coordinate five-term cap 40 remains valid but is not used to infer
  a general flat-sum bound. The current cap 112 avoids that transfer problem.

## 9. Active pull-request stack

```text
PR #31 broad n=6/general research head
  -> PR #35 exact product shadows
      -> PR #38 nested zero-intersection removal
          -> PR #39 perm_8 equality tangent cone
              -> PR #41 consolidated ledger + pairwise overlap
                  -> PR #44 dual-frame same-span overlap
                      -> PR #45 factor-span zero blocks
                          -> PR #46 permanent-center equality closure
                              -> current PR cross-degree block projection
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 10. Current open mathematical interfaces

1. **Five-term cubic cap for lower 81.**  
   The uniform cap is now 112. A sufficient next target is 90: with twenty-one
   fixed terms it gives projected capacity 986, while
   `F_(8,4)(773)=987`, and therefore proves `ChowRank(perm_8)>=81`.

2. **Chow realizability of exact-shadow equality spaces.**  
   Determine whether a coupled fourteen-term sum can realize the
   four-dimensional `perm_8` equality locus.

3. **Lower-29 `perm_6` frontier.**  
   Continue only with a theorem acting on the surviving `b=31,...,49`
   geometry; do not recreate a broad scalar state tree.

4. **General correction beyond shadow cardinality.**  
   Iterate cross-degree permanent-relative defects or find a frame-sensitive,
   multigraded or representation-valued invariant beyond the Ferrers minimum.

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
