# Research ledger

## Purpose

This is the canonical high-level ledger for the active permanent Chow-rank
research repository. `STATUS.md` remains the detailed theorem inventory. This
file records the current numerical boundaries, the general-`n` theorem stack,
strict route ceilings, active pull-request ancestry and the next authorized
mathematical interfaces.

Every result that changes a theorem, numerical bound, counterexample, route
barrier, equality classification or open frontier must update this file in the
same pull request. This is one Markdown index, not a registry, database,
manager, dispatcher or second workflow layer.

Last consolidated: **2026-08-17**  
Consolidation branch: `research/two-direction-power-profiles`.

## Status vocabulary

- `ACCEPTED_BASELINE`: canonical small-`n` result on merged mainline.
- `PROOF_DRAFT_COMPLETE`: the written proof is complete inside its stated
  dependencies; external review or merge may remain pending.
- `COMPUTATION_REPLAYED`: the stated finite interface has deterministic replay.
- `RESTRICTED_FAMILY_THEOREM`: exact only for a named proper subclass.
- `ROUTE_DIAGNOSTIC`: a valid result used to select or reject a route.
- `ROUTE_CEILING`: a proved upper limit on a named lower-bound mechanism; never
  an upper bound on actual Chow rank unless separately stated.
- `STACKED_DRAFT`: valid only on the named open PR stack until merged.
- `SUPERSEDED`: retained for provenance but not canonical.
- `REJECTED`: an attempted implication was found invalid before promotion.
- `OPEN`: the stated frontier is not closed.

## 1. Current numerical boundaries

| Object | Current accessible repository boundary | Status | Primary location |
|---|---:|---|---|
| `perm_3` | `ChowRank=4` | `ACCEPTED_BASELINE` | merged small-`n` proof |
| `perm_4` | `ChowRank=8` | `ACCEPTED_BASELINE` | merged exact-rational proof |
| `perm_5` | `ChowRank=16` | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | merged PR #30 |
| `perm_6` | `28 <= ChowRank <= 32` | specialized lower-bound draft; exact value open | PR #31 |
| `perm_7` | `49 <= ChowRank <= 64` | `STACKED_DRAFT` | PR #51 |
| `perm_8` | `90 <= ChowRank <= 128` | `STACKED_DRAFT` | PR #51 |
| `perm_9` | `164 <= ChowRank <= 256` | `STACKED_DRAFT` | PR #51 |
| `perm_10` | `307 <= ChowRank <= 512` | `STACKED_DRAFT` | PR #51 |
| `perm_11` | `ChowRank >= 508` | earlier stacked bound; full tower not replayed at this size | PR #38 |
| `perm_12` | `ChowRank >= 970` | earlier stacked bound; full tower not replayed at this size | PR #38 |
| `perm_13` | `ChowRank >= 1855` | earlier stacked bound | PR #38 |
| `perm_14` | `ChowRank >= 3570` | earlier stacked bound | PR #38 |
| `perm_15` | `ChowRank >= 6883` | earlier stacked bound | PR #38 |
| `perm_16` | `ChowRank >= 13315` | earlier stacked bound | PR #38 |

The general upper bound remains Glynn's `2^(n-1)`-term decomposition. No
unrestricted exact result for `perm_6` or any larger `n` is present in the
currently accessible repository state.

## 2. Canonical small-`n` chain

\[
\operatorname{ChowRank}(\operatorname{perm}_3)=4,\qquad
\operatorname{ChowRank}(\operatorname{perm}_4)=8,\qquad
\operatorname{ChowRank}(\operatorname{perm}_5)=16.
\]

The `n=3` proof is linear algebra. The `n=4` proof combines the first-Koszul
baseline, low-rank quadratic classification, the exact `psi_v` chart and a
double-quotient inequality. The repaired `n=5` proof preserves the
coupled-catalectic firewall, routes all fixed-six states and binds the
non-finite bridges and deterministic certificates at merged PR #30.

## 3. General-`n` theorem stack

| ID | Statement | Status | PR / document |
|---|---|---|---|
| `G-PROFILE` | Any method factoring only through scalar derivative dimensions is capped at the central binomial coefficient. | merged proof draft | PR #32 |
| `G-SIGN` | `ColumnSignRank(perm_n)=RowSignRank(perm_n)=2^(n-1)`. | merged restricted-family theorem | PR #33 |
| `G-AFFINE-SLICE` | The Boolean slice has affine-Segre rank `d+1`; sign rigidity does not extend to arbitrary complex diagonal ratios. | merged route diagnostic | PR #34 |
| `G-KOSZUL` | General first-Koszul, quotient-gain, parity-asymptotic and fixed-offset multishadow formulas. | proof draft | general docs / `STATUS.md` |
| `G-MACAULAY` | Vector-valued first prolongation satisfies `dim K^(1)<=dim(K)^{<2>}`. | proof draft, replayed | general relation docs |
| `G-EXACT-SHADOW` | Exact simultaneous product-shadow minima are Ferrers integer programs. | stacked draft, independent replay | PR #35 |
| `G-NESTED-SHADOW` | A certified zero-intersection block can be projected away inside a nonzero-intersection multishadow proof. | stacked draft | PR #38 |
| `G-PAIR-OVERLAP` | Transverse shared-factor pairs have intersection `binom(s,m)`; factor count alone does not control arbitrary overlap. | stacked draft, replayed | PR #41 |
| `G-DUAL-FRAME-OVERLAP` | Same-span quadratic literal overlap is sharply bounded by a dual-frame support invariant. | stacked draft, replayed | PR #44 |
| `G-FACTOR-SPAN-ZERO` | A joint factor span of dimension `<m^2` has zero intersection with `D_m(perm_n)`; low-span quotient intersections are exact. | stacked draft | PR #45 |
| `G-PERM-CENTER` | For every `m>=3`, the concise Hessian center of `perm_m` is scalar; minimal-shadow permanent derivatives are direct-sum indecomposable. | stacked draft, replayed | PR #46 |
| `G-CROSS-DEGREE-PROJECTION` | Project a Chow block one derivative degree lower, retain the exact permanent-relative defect and invert the upper shadow. | stacked draft, independent replay | PR #47 |
| `G-DERIVATIVE-TOWER` | Permanent-relative capacities `B_(n,d)(q)` propagate recursively across derivative degrees with exact shadows and subblock projection. | stacked general theorem | PR #48 |
| `G-TOWER-BOOTSTRAP` | Tower capacities compose with complementary-intersection first-Koszul residual ranks. | stacked route theorem | PR #49 |
| `G-TOWER-SATURATION` | A `q`-term decomposition forces every derivative-tower row to have saturated at `q`. | stacked general theorem | PR #50 |
| `G-FULL-DEGREE-ENVELOPE` | The projection recurrence is a prefix min-plus envelope; full degree coverage gives the PR #51 thresholds. | stacked general theorem, C++ and Python replay | PR #51 |
| `G-SHADOW-COMPLEMENT` | `Gamma_(n,d)(A_(d-1)-z)=A_d-F_(n,n-d+1)(z)` and the tower becomes an exact max-plus deficit transport. | stacked general theorem, two independent DPs | PR #52 |
| `G-TOWER-TAIL` | Saturation thresholds are nondecreasing; fixed-codimension transitions have universal constants; the final row adds at most one and is a bipartite `C4` supersaturation decision. | stacked general theorem, replayed | PR #53 |
| `G-SHADOW-ENTROPY-BARRIER` | Product shadows preserve first-order exponential rate at linear degree; entropy alone cannot distinguish central-binomial scale from Glynn scale. | stacked route theorem | PR #53 |
| `G-CENTRAL-WINDOW` | At polynomial precision, only a window `d=n/2+O(sqrt(n log n))` above the center can affect the scalar tower. | stacked general theorem | PR #53 |
| `G-SCALAR-POLYNOMIAL-CEILING` | The complete exact scalar tower satisfies `Theta_n=O(n^(1/4) binom(n,floor(n/2)))=O(2^n/n^(1/4))`. | `ROUTE_CEILING`, exact finite interfaces replayed | PR #55 |
| `G-APOLAR-SUBQUOTIENT` | For any differential two-plane `W`, `A_f` is a `k[W]`-subquotient of the direct sum of termwise apolar algebras. | current stacked general theorem | PR #56 |
| `G-BOOLEAN-TERM-ENVELOPE` | Every Chow-term apolar algebra, including dependent-factor terms, is a quotient of a submodule of the squarefree Boolean envelope. | current stacked general theorem | PR #56 |
| `G-TWO-DIRECTION-POWERS` | Homogeneous profiles `dim((W^pA_f)_d)` are monotone; exact scans through `n=6` do not improve existing unrestricted bounds. | current finite route diagnostic | PR #56 |
| `G-TWO-DIRECTION-PRINCIPAL` | Every principal homogeneous binary ideal profile is capped by `binom(n,floor(n/2))`. | current general-`n` route barrier | PR #56 |

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
28 <= ChowRank(perm_6) <= 32.
```

The lower-29 program remains partial. Broad scalar state trees, complete sign
families and uncorrected quotient-intersection shortcuts are closed routes.

## 5. Complete scalar derivative tower

For

\[
M_{n,d}=\binom nd,\qquad A_{n,d}=M_{n,d}^2,
\]

let `Gamma_(n,d)` be the inverse exact product-shadow capacity. The direct cap
and prefix envelope are

\[
C_{n,d}(q)
=
\min\{A_{n,d},qM_{n,d},\Gamma_{n,d}(B_{n,d-1}(q))\},
\]

\[
B_{n,d}(q)
=
qM_{n,d}
+
\min_{0\le t\le q}
\bigl(C_{n,d}(t)-tM_{n,d}\bigr).
\]

Writing

\[
Q_{n,d}=\min\{q:B_{n,d}(q)=A_{n,d}\}
\]

gives

\[
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
\Theta_n:=\max_dQ_{n,d}.
\]

The exact rows through `n=10` are

```text
n=3:  3,4                                  Theta=4
n=4:  4,7,8                                Theta=8
n=5:  5,11,14,15                           Theta=15
n=6:  6,16,24,26,27                        Theta=27
n=7:  7,22,39,46,48,49                     Theta=49
n=8:  8,29,59,80,87,89,90                  Theta=90
n=9:  9,37,87,136,155,161,163,164          Theta=164
n=10: 10,46,123,219,280,299,305,307,307    Theta=307.
```

PR #52 rewrites the tower in deficit variables:

\[
D_{n,d}(q)=A_{n,d}-B_{n,d}(q),
\]

\[
H_{n,d}(q)
=
\max\{0,A_{n,d}-qM_{n,d},
F_{n,n-d+1}(D_{n,d-1}(q))\},
\]

\[
D_{n,d}(q)
=
\max_{0\le t\le q}
\bigl(H_{n,d}(t)-(q-t)M_{n,d}\bigr).
\]

PRs #53 and #55 then prove the structural stopping point:

\[
\boxed{
\Theta_n
=
O\!\left(
 n^{1/4}\binom n{\lfloor n/2\rfloor}
\right)
=
O\!\left(\frac{2^n}{n^{1/4}}\right).
}
\]

Therefore the complete named scalar tower remains an unbounded polynomial
factor below Glynn for all sufficiently large `n`. This is not an upper bound
on actual Chow rank and does not close a Chow-realizability-enhanced shadow
method.

## 6. Two-direction apolar module program

Fix a differential subspace

\[
W\subseteq S_1,
\qquad
\dim W\le2.
\]

For a decomposition `f=sum_i T_i`, the exact apolar containment gives an
intermediate module which embeds in `direct_sum_i A_(T_i)` and surjects onto
`A_f`. Hence every invariant used in this program must be:

1. additive on direct sums;
2. nonincreasing under submodules; and
3. nonincreasing under quotients.

The homogeneous power profiles

\[
\Lambda_{p,d}(M;W)
=
\dim((W^pM)_d)
\]

satisfy these conditions. Exact finite scans give

```text
n=3: best power-profile lower bound  3, existing boundary  4
n=4: best power-profile lower bound  6, existing boundary  8
n=5: best power-profile lower bound 10, existing boundary 16
n=6: best power-profile lower bound 20, existing boundary 28.
```

For an arbitrary nonzero binary form `g` of degree `p`, the exact one-term
principal envelope is

\[
\beta^{\mathrm{pr}}_{n,p,d}
=
\min\left\{
\binom n{d-p},
\binom nd
\right\}.
\]

The permanent numerator is at most the square of this quantity, so every
principal profile proves at most

\[
\binom n{\lfloor n/2\rfloor}.
\]

Thus the first open ideal-profile interface must have at least two genuinely
active minimal generators.

## 7. Finite instances and equality geometry

Finite cases are falsification and regression instances for general theorems,
not the research objective. A finite result is promoted only when it detects a
false implication, validates a uniform theorem against unrestricted rank,
identifies an equality geometry or certifies a route ceiling.

PR #39 classifies the reduced tangent cone at the `560/784` `perm_8`
exact-shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4.
```

Chow realizability of the full equality locus remains open.

## 8. Restricted sign-family theorem

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical defect calculations remain diagnostics. Further sign-dictionary
enumeration is not active.

## 9. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- Quotient-image overlap cannot be converted into an equally large
  matched-difference space without controlling literal overlap.
- Common primal-factor count alone is rejected as a global overlap parameter.
- Coordinate literal-sum caps are not transferred to moving terms without a
  flat-sum or valuative theorem.
- PRs #49 and #50 remain valid weaker stages; PR #51 supersedes their stopping
  points by including the full degree range.
- A scalar-route fixed point or ceiling is not an upper bound on actual Chow
  rank.
- The scalar tower and the two-direction principal barrier do not close
  Chow-realizability corrections or non-scalar relation modules.

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
                                      -> PR #49 tower bootstrap
                                          -> PR #50 tower saturation
                                              -> PR #51 full-degree envelope
                                                  -> PR #52 shadow-complement deficit duality
                                                      -> PR #53 tail and central-window localization
                                                          -> PR #55 scalar polynomial ceiling
                                                              -> current PR #56 two-direction apolar profiles
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 11. Current open mathematical interfaces

Priority order:

1. **Two-generator homogeneous ideal profiles.**  
   For a canonical ideal `I=(g_1,g_2) subset k[s,t]`, prove an exact one-term
   Boolean envelope for `dim((IA_T)_d)` and compare it with the permanent. A
   candidate is promoted only if the denominator controls all Chow terms,
   including dependent-factor terms through the Boolean subquotient.

2. **Subquotient-monotone relation information.**  
   Identify a relation, Fitting, Loewy or multigraded invariant that is
   additive and monotone under both submodules and quotients. Raw kernel
   dimensions and Betti numbers are not assumed monotone.

3. **Uniform Chow-realizability defect.**  
   Prove that exact-shadow or near-shadow Ferrers spaces cannot arise from
   sums of Chow derivative spaces except in classified cases. This route is
   not covered by the scalar-tower ceiling.

4. **Representation-valued general invariant.**  
   Retain `S_n x S_n` isotypes, multigraded syzygies or frame-sensitive
   information that cannot be reduced to scalar dimensions.

5. **Cross-`n` recurrence.**  
   Seek a compatible restriction or valuation theorem implying a relation
   such as `R_n>=2R_(n-1)`. Ordinary row expansion is not additive enough.

6. **Finite regression frontiers.**  
   The `perm_6` lower-29 geometry and selected `perm_8` equality questions
   remain testbeds, not the primary general-`n` program.

## 12. Mandatory update rule

Every meaningful future result must update this file in the same pull request.
Each entry records status, statement, evidence, boundary, PR/head, replay
status, superseded dependencies and next interface.

Promotion rules:

- never call an open stacked result canonical on `main`;
- never promote finite-field equality without the characteristic-zero
  direction;
- never replace a coupled apolar or catalectic object by a literal direct sum
  without a theorem;
- include counterexamples and rejected shortcuts;
- do not add a manager, registry, dispatcher or database for this ledger;
- update this one Markdown file and theorem-specific proof/evidence files.
