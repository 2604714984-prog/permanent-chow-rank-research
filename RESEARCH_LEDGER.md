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
Consolidation base: PR #50 theorem tree plus the current full-degree envelope.

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
| `perm_7` | `49 <= ChowRank <= 64` | `STACKED_DRAFT` | current PR #51 |
| `perm_8` | `90 <= ChowRank <= 128` | `STACKED_DRAFT` | current PR #51 |
| `perm_9` | `164 <= ChowRank <= 256` | `STACKED_DRAFT` | current PR #51 |
| `perm_10` | `307 <= ChowRank <= 512` | `STACKED_DRAFT` | current PR #51 |
| `perm_11` | `ChowRank >= 508` | `STACKED_DRAFT` | PR #38 |
| `perm_12` | `ChowRank >= 970` | `STACKED_DRAFT` | PR #38 |
| `perm_13` | `ChowRank >= 1855` | `STACKED_DRAFT` | PR #38 |
| `perm_14` | `ChowRank >= 3570` | `STACKED_DRAFT` | PR #38 |
| `perm_15` | `ChowRank >= 6883` | `STACKED_DRAFT` | PR #38 |
| `perm_16` | `ChowRank >= 13315` | `STACKED_DRAFT` | PR #38 |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition. No
unrestricted exact result for `perm_6` or any larger permanent is present in
the currently accessible repository state.

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

The full scalar tower gives only 15 at `n=5`; the separate coupled proof is
still essential for 16. At `n=6` the full scalar tower gives 27, below the
specialized accessible lower bound 28. These regressions are retained as a
fail-closed boundary.

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
| `G-PERM-CENTER` | For every `m>=3`, the concise Hessian center of `perm_m` is scalar. Minimal-shadow permanent derivatives are direct-sum indecomposable. | stacked draft, replayed | PR #46 |
| `G-CROSS-DEGREE-PROJECTION` | Project a term block one derivative degree lower, retain a permanent-relative defect, and invert the exact upper shadow. | stacked draft, independent replay | PR #47 |
| `G-DERIVATIVE-TOWER` | Define permanent-relative block capacities recursively at adjacent derivative degrees using exact shadows and subblock projection. | stacked general-`n` draft | PR #48 |
| `G-TOWER-BOOTSTRAP` | Compose tower capacities with complementary-intersection Koszul residual ranks. The narrow `n=7` sequence is `36 -> 46 -> 47 -> 47`. | stacked route theorem | PR #49 |
| `G-TOWER-SATURATION` | A decomposition by `q` terms forces every evaluated tower row to have saturated at `q`; degrees through `n-2` give `perm_7>=48`. | valid weaker stacked theorem | PR #50 |
| `G-FULL-DEGREE-TOWER-ENVELOPE` | Solve block projection as a prefix min-plus envelope, include every degree through `n-1`, and define the exact saturation recurrence. The exact table gives lower bounds `49,90,164,307` for `n=7,8,9,10`. | current stacked draft; C++ exact replay and independent Python through `n=8` | PR #51 |

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
The full tower value 27 does not replace the specialized lower bound 28.

## 5. Full derivative-tower envelope and saturation

Let

\[
M_{n,d}=\binom nd,
\qquad
A_{n,d}=M_{n,d}^2.
\]

If `C_(n,d)(q)` denotes the minimum of the ambient, literal and lower-degree
exact-shadow caps, then the block recurrence has the exact closed form

\[
B_{n,d}(q)
=
qM_{n,d}
+
\min_{0\le t\le q}
\bigl(C_{n,d}(t)-tM_{n,d}\bigr).
\]

Thus recursive subblock projection is one prefix min-plus envelope. Once

\[
R_{n,d}=\max\{M_{n,d},Q_{n,d-1}\}
\]

has been reached, the row is affine until saturation, and `Q_(n,d)` is
computed from the finite prefix `t<R_(n,d)`.

A real decomposition must cover every permanent derivative space. Therefore

\[
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
\Theta_n,
\qquad
\Theta_n=
\max_{1\le d\le n-1}Q_{n,d}.
\]

The range through `n-1` is essential. The first-Koszul residual machinery
naturally stopped at complementary degree `n-2`, but the tower itself did not.
Output degree `n` has the same saturation threshold as degree `n-1`.

The exact table is

| `n` | `Q_(n,1),...,Q_(n,n-1)` | `Theta_n` |
|---:|---|---:|
| 3 | `3,4` | 4 |
| 4 | `4,7,8` | 8 |
| 5 | `5,11,14,15` | 15 |
| 6 | `6,16,24,26,27` | 27 |
| 7 | `7,22,39,46,48,49` | **49** |
| 8 | `8,29,59,80,87,89,90` | **90** |
| 9 | `9,37,87,136,155,161,163,164` | **164** |
| 10 | `10,46,123,219,280,299,305,307,307` | **307** |

The decisive last-row boundaries include

```text
B_(7,6)(48)=44  <49=B_(7,6)(49)
B_(8,7)(89)=60  <64=B_(8,7)(90)
B_(9,8)(163)=74 <81=B_(9,8)(164).
```

At `n=10`, both degrees eight and nine saturate at 307.

PR #50's lower bound 48 remains valid, but its claim that the complete scalar
tower stopped at 48 is superseded: it evaluated only through `n-2`.

## 6. Equality, overlap and non-scalar frontiers

PR #39 classifies the reduced tangent cone at the `560/784` `perm_8`
exact-shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

PR #41 proves the transverse common-factor formula and block-rotation
counterexample. PR #44 gives the sharp same-span dual-frame bound. PR #45
closes low joint factor spans, and PR #46 proves scalar Hessian centers and
minimal-shadow direct-sum indecomposability.

These results remain candidates for a Chow-realizability correction to the
scalar tower. They are not automatically encoded by the saturation table.

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
  a general flat-sum bound.
- PR #49's fixed point 47 is correct for its narrower partial-term Koszul
  operator, not for the full tower.
- PR #50's lower bound 48 is valid but is superseded as the complete tower
  threshold by the omitted degree-`n-1` row.
- A scalar-route fixed point is not an upper bound on Chow rank.

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
                              -> PR #47 cross-degree block projection
                                  -> PR #48 derivative-tower capacity
                                      -> PR #49 tower bootstrap
                                          -> PR #50 tower saturation through n-2
                                              -> current PR #51 full-degree envelope
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 10. Current open mathematical interfaces

Priority order:

1. **Uniform asymptotics of `Theta_n`.**  
   Determine the exponential and polynomial-scale growth of the full-degree
   saturation threshold. The finite sequence
   `4,8,15,27,49,90,164,307` is evidence, not an asymptotic theorem.

2. **A central-binomial ceiling or a gain toward Glynn.**  
   Prove either a matching upper estimate for the scalar envelope or a uniform
   deficit lower bound that drives `Theta_n` toward `2^(n-1)`.

3. **Uniform Chow-realizability defect.**  
   Lower a capacity `B_(n,d)(q)` by classifying which exact-shadow and
   near-shadow spaces can actually arise from Chow blocks.

4. **A non-scalar general invariant.**  
   Add frame-sensitive, multigraded, syzygetic, or representation-valued
   information rather than another scalar finite table.

5. **Cross-`n` recurrence.**  
   Seek a compatible restriction or valuation theorem implying a relation
   such as `R_n>=2R_(n-1)`. Ordinary row expansion alone is not additive.

6. **Finite regression frontiers.**  
   The `perm_6` lower-29 geometry remains open. Finite instances are testbeds,
   not the main general-`n` objective.

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
