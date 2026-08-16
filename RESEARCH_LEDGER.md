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
Consolidation base: PR #48 theorem head
`9683f0373d955e69a968d50d14f59a55e23ff6a3`.

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
| `perm_7` | `47 <= ChowRank <= 64` | `STACKED_DRAFT` | current PR #49 |
| `perm_8` | `80 <= ChowRank <= 128` | `STACKED_DRAFT` | PR #47 and PR #48 regression |
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
| `G-CROSS-DEGREE-PROJECTION` | Project a term block one derivative degree lower, retain the exact one-term permanent defect, and invert the exact upper shadow. This gives cubic caps 41 and 112 and the ordinary bounds `perm_7>=45`, `perm_8>=80`. | stacked draft, independent replay | PR #47 |
| `G-DERIVATIVE-TOWER` | Define a permanent-relative block capacity recursively at every adjacent derivative degree using exact shadows and subblock projection. The first finite rows give `perm_7>=46` and reproduce `perm_8>=80`. | stacked general-`n` draft | PR #48 |
| `G-TOWER-BOOTSTRAP` | If `ChowRank(perm_n)>=L`, the general operator `Phi_n(L)` composes tower capacities with complementary-intersection Koszul residual ranks to promote `L`. Exact closure at `n=7` is `36 -> 46 -> 47 -> 47`. | current general-`n` stacked draft, primary and independent replay | PR #49 |

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

## 5. Exact shadows, the derivative tower and bootstrap closure

PR #35 proves the exact adjacent product-shadow function for every `n,d` and
in particular

\[
F_{7,4}(238)=452,\quad F_{7,4}(239)=456,
\]

\[
F_{8,4}(560)=784,\quad F_{8,4}(561)=793.
\]

PRs #38, #45, #46 and #47 progressively insert permanent-relative defects
before the outer exact-shadow inversion. PR #48 packages that operation into
the derivative-tower recurrence

\[
B_{n,1}(q)=\min(n^2,qn),
\]

\[
\begin{aligned}
B_{n,d}(q)=\min\Bigl\{&\binom nd^2,\ q\binom nd,\\
&\Gamma_{n,d}(B_{n,d-1}(q)),\\
&\min_{1\le s<q}\bigl((q-s)\binom nd+B_{n,d}(s)\bigr)
\Bigr\}.
\end{aligned}
\]

The current theorem promotes any valid lower bound `L` through

\[
\Phi_n(L)
=
\max_{\substack{2\le m\le n-2\\1\le q\le L}}
\left\{
L,
q+
\left\lceil
\frac{A_{n,m}-n^2B_{n,n-m}(q)}{K_{n,m}}
\right\rceil_+
\right\}.
\]

Every iterate is a valid lower bound. For `n=7`, exact reconstruction through
degree five and 47 terms gives

```text
B_(7,4)(20)=341
B_(7,5)(36)=233
B_(7,5)(39)=267
B_(7,5)(46)=405
B_(7,5)(47)=426
```

and the exact closure

```text
36 -> 46 -> 47 -> 47.
```

The decisive second promotion is

\[
A_{7,2}-49B_{7,5}(46)
=20,384-49\cdot405
=539>0.
\]

Thus a hypothetical 46-term decomposition cannot have zero residual after all
46 terms are selected, and

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge47.
\]

The fixed point at 47 closes only the current scalar tower plus first-Koszul
bootstrap. It is not an exact-rank statement.

PR #39 separately classifies the reduced tangent cone at the `560/784`
`perm_8` exact-shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

## 6. Why finite instances are retained

`perm_7` and `perm_8` are falsification and regression instances for general
theorems. They are not the research objective. A finite instance is promoted
only when it does at least one of the following:

1. detects a false general implication;
2. validates a uniform recurrence against an unrestricted rank bound;
3. identifies an equality geometry needed by the next uniform theorem; or
4. certifies the exact stopping point of a named general proof mechanism.

The `n=7` fixed point now shows that further arithmetic iteration of the same
scalar tower/Koszul operator cannot prove 48. The next result must strengthen
a mathematical input rather than extend a finite table.

## 7. Pairwise and block-overlap frontier

PR #41 proves the transverse common-factor formula and block-rotation
counterexample. PR #44 gives the sharp same-span dual-frame bound. PR #45
proves that low joint factor-span blocks are invisible to the permanent
space. PR #46 proves every central two-term block for `perm_8` is zero.

PR #47 gives the first five-term cubic cap strong enough to raise `perm_8` to
80. PR #48 shows that cap is one row of a general adjacent-degree recursion.
PR #49 closes the corresponding first-Koszul bootstrap at 47 for `n=7`.

## 8. Restricted sign-family results

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical one- and two-defect calculations remain diagnostics. Further sign
dictionary enumeration is not active.

## 9. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- The implication from quotient-image overlap to an equally large
  matched-difference space was rejected until literal overlap was included.
- Common primal-factor count alone is rejected as a global overlap parameter.
- PR #43's coordinate five-term cap 40 remains valid but is not used to infer
  a general flat-sum bound.
- A fixed point of `Phi_n` is not an upper bound on Chow rank; interpreting it
  that way is explicitly rejected.

## 10. Active pull-request stack

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
                                      -> current PR #49 tower bootstrap closure
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 11. Current open mathematical interfaces

Priority order:

1. **Uniform asymptotics of the tower and bootstrap.**  
   Determine the polynomial-scale growth of the fixed point of `Phi_n` in the
   central regime. Prove either a uniform gain toward `2^(n-1)` or a ceiling
   theorem for this exact scalar mechanism.

2. **Uniform Chow-realizability defect.**  
   The `n=7` fixed point proves arithmetic iteration is exhausted. Lower a
   capacity `B_(n,d)(q)` using a theorem about which exact-shadow or
   near-shadow spaces can actually arise from Chow blocks.

3. **A non-scalar general invariant.**  
   If the tower fixed point remains on the central-binomial scale, add a
   frame-sensitive, multigraded or representation-valued invariant rather
   than another finite state table.

4. **Cross-`n` recurrence.**  
   Seek a compatible restriction or valuation theorem implying a genuine
   relation such as `R_n>=2R_(n-1)`. Ordinary row expansion alone is not
   additive enough.

5. **Finite regression frontiers.**  
   `perm_8` lower 81 would follow from a five-term cubic cap 90, and the
   `perm_6` lower-29 geometry remains open. These are testbeds, not the main
   general-`n` objective.

## 12. Mandatory update rule

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
