# Research ledger

## Purpose

This is the canonical high-level ledger for the active permanent Chow-rank
research repository. `STATUS.md` remains the detailed theorem inventory. This
file records numerical boundaries, theorem milestones, active stacked
branches, superseded or rejected routes, and the next authorized mathematical
interfaces.

Every result that changes a theorem, numerical bound, counterexample, route
barrier, equality classification, or open frontier must update this file in
the same pull request. This is one Markdown index, not a registry, database,
manager, dispatcher, or second workflow layer.

Last consolidated: **2026-08-16**  
Consolidation base: PR #52 theorem head
`fab0e51bda4d04a5af924f191b202c0ac358cc3b`.

## Status vocabulary

- `ACCEPTED_BASELINE`: canonical small-`n` result on merged mainline.
- `PROOF_DRAFT_COMPLETE`: the argument is written; external review may remain.
- `COMPUTATION_REPLAYED`: the finite interface has deterministic replay.
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

The `n=3` proof is linear algebra. The `n=4` proof combines the `560/92`
Koszul baseline, low-rank quadratic classification, the exact `psi_v` chart
and a double-quotient inequality. The repaired `n=5` proof preserves the
coupled-catalectic firewall, routes all 58 fixed-six states and binds the
non-finite bridges and deterministic certificates at merged PR #30.

## 3. General-`n` theorem stack

| ID | Statement | Status | PR / document |
|---|---|---|---|
| `G-PROFILE` | Any lower-bound method factoring only through scalar derivative dimensions is capped at the central binomial coefficient. | merged proof draft | PR #32 |
| `G-SIGN` | `ColumnSignRank(perm_n)=RowSignRank(perm_n)=2^(n-1)`. | merged restricted-family theorem | PR #33 |
| `G-AFFINE-SLICE` | The Boolean slice has affine-Segre rank `d+1`; sign rigidity does not extend to arbitrary complex diagonal ratios. | merged route diagnostic | PR #34 |
| `G-KOSZUL` | General first-Koszul, quotient-gain, parity-asymptotic and fixed-offset multishadow formulas. | proof draft | general docs / `STATUS.md` |
| `G-MACAULAY` | Vector-valued first prolongation satisfies `dim K^(1)<=dim(K)^{<2>}`. | proof draft, replayed | general relation docs |
| `G-EXACT-SHADOW` | Exact simultaneous product-shadow minima are Ferrers integer programs. | stacked draft, independent replay | PR #35 |
| `G-NESTED-SHADOW` | A certified zero-intersection block can be projected away inside a nonzero-intersection multishadow proof. | stacked draft | PR #38 |
| `G-PAIR-OVERLAP` | Transverse shared-factor pairs have intersection `binom(s,m)`; a zero-common-factor block rotation can still have large overlap. | stacked draft, replayed | PR #41 |
| `G-DUAL-FRAME-OVERLAP` | For same-span independent frames, quadratic literal overlap is sharply bounded by a dual-frame support invariant. | stacked draft, replayed | PR #44 |
| `G-FACTOR-SPAN-ZERO` | A joint factor span of dimension `<m^2` has zero intersection with `D_m(perm_n)`; low-span quotient intersections are exact. | stacked draft | PR #45 |
| `G-PERM-CENTER` | For every `m>=3`, the concise Hessian center of `perm_m` is scalar; minimal-shadow permanent derivatives are direct-sum indecomposable. | stacked draft, replayed | PR #46 |
| `G-CROSS-DEGREE-PROJECTION` | Project a term block one derivative degree lower, retain the exact permanent-relative defect, and invert the upper shadow. | stacked draft, independent replay | PR #47 |
| `G-DERIVATIVE-TOWER` | Define permanent-relative capacities `B_(n,d)(q)` recursively across derivative degrees with exact shadows and subblock projection. | stacked general-`n` draft | PR #48 |
| `G-TOWER-BOOTSTRAP` | Compose tower capacities with complementary-intersection Koszul residual ranks. | stacked route theorem | PR #49 |
| `G-TOWER-SATURATION` | A `q`-term decomposition forces every derivative-tower row to have saturated at `q`. | stacked general theorem | PR #50 |
| `G-FULL-DEGREE-ENVELOPE` | The projection recurrence is a prefix min-plus envelope; scanning through degree `n-1` gives the thresholds in PR #51. | stacked general theorem, C++ and Python replay | PR #51 |
| `G-SHADOW-COMPLEMENT` | `Gamma_(n,d)(A_(d-1)-z)=A_d-F_(n,n-d+1)(z)` and the equivalent max-plus deficit recurrence. | stacked general theorem, two independent exact DPs | PR #52 |
| `G-TOWER-TAIL` | Thresholds are nondecreasing; the full scalar bound is the top row; fixed-codimension transitions have universal constants `c_k`; the final row adds at most one and is controlled by bipartite `C4` supersaturation. | current general-`n` stacked draft, two independent exact DPs | current PR #53 |
| `G-SHADOW-ENTROPY-BARRIER` | Product shadows satisfy an exact incidence sandwich and preserve exponential rate at linear degree. Consequently `log Theta_n/n -> log 2`; exponential entropy alone cannot resolve the polynomial gap to Glynn. | current general-`n` route theorem, exact replay | current PR #53 |

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

## 5. Full-degree tower and deficit form

Let

\[
M_{n,d}=\binom nd,\qquad A_{n,d}=M_{n,d}^2.
\]

The exact direct cap and projection closure are

\[
C_{n,d}(q)
=\min\{A_{n,d},qM_{n,d},
\Gamma_{n,d}(B_{n,d-1}(q))\},
\]

\[
B_{n,d}(q)
=qM_{n,d}
+\min_{0\le t\le q}
\bigl(C_{n,d}(t)-tM_{n,d}\bigr).
\]

A decomposition by `q` terms must cover every permanent derivative space.
Writing

\[
Q_{n,d}=\min\{q:B_{n,d}(q)=A_{n,d}\}
\]

gives the scalar lower bound

\[
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge\Theta_n:=\max_{1\le d\le n-1}Q_{n,d}.
\]

PR #51 replays

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

The scalar tower remains weaker than the separate exact `n=5` result and the
specialized `n=6` lower bound.

PR #52 introduces the exact complement identity

\[
\Gamma_{n,d}(A_{n,d-1}-z)
=
A_{n,d}-F_{n,n-d+1}(z).
\]

For

\[
D_{n,d}(q)=A_{n,d}-B_{n,d}(q),
\]

the tower becomes

\[
H_{n,d}(q)
=\max\{0,A_{n,d}-qM_{n,d},
F_{n,n-d+1}(D_{n,d-1}(q))\},
\]

\[
D_{n,d}(q)
=\max_{0\le t\le q}
\bigl(H_{n,d}(t)-(q-t)M_{n,d}\bigr).
\]

## 6. Fixed-codimension tail structure

The current theorem proves

\[
Q_{n,d}\ge Q_{n,d-1},
\qquad
\Theta_n=Q_{n,n-1},
\]

and the row-wise one-term Lipschitz bound

\[
0\le B_{n,d}(q+1)-B_{n,d}(q)\le\binom nd.
\]

For `k>=2`, define

\[
c_k
=
\max_{a\ge k}
\left[
\binom a{k-1}-\binom{a-1}k-1
\right]_+.
\]

For `n>=2k`,

\[
0\le
Q_{n,n-k+1}-Q_{n,n-k}
\le c_k.
\]

The first constants are

```text
c_2,...,c_8 = 1,5,20,83,362,1572,7513.
```

For fixed `K` and `n>=2K`,

\[
0\le
\Theta_n-Q_{n,n-K}
\le
\sum_{k=2}^{K}c_k.
\]

Moreover, for `phi=(1+sqrt(5))/2`,

\[
\lim_{k\to\infty}c_k^{1/k}
=
\phi^{\phi+2}
=
5.7032759559\ldots.
\]

Hence the top `o(n)` codimension tail contributes only `exp(o(n))`
additively. It cannot create a new positive exponential rate absent at degree
`n-o(n)`.

The final transition has the sharper universal bound

\[
Q_{n,n-2}\le\Theta_n\le Q_{n,n-2}+1.
\]

The exact degree-two shadow `F_(n,2)(z)` is the minimum number of edges in an
`n`-by-`n` bipartite graph containing at least `z` copies of `K_(2,2)`.
Thus the last zero-or-one decision is an exact `C4` supersaturation criterion.

This theorem introduces no new numerical Chow-rank bound. It localizes the
unresolved scalar asymptotic to linear codimension.

### Incidence sandwich and entropy-scale barrier

Every coordinate degree-`d` product cell has `d^2` lower neighbors, while
every degree-`d-1` cell has `(n-d+1)^2` upper containers. Double counting gives

\[
\frac{d^2}{(n-d+1)^2}\,b
\le
F_{n,d}(b)
\le
\min\{A_{n,d-1},d^2b\}.
\]

The inverse capacity has the corresponding bounds

\[
\left\lfloor\frac C{d^2}\right\rfloor
\le
\Gamma_{n,d}(C)
\le
\left\lfloor
\frac{C(n-d+1)^2}{d^2}
\right\rfloor
\]

after ambient truncation.

For `d=alpha n+O(1)` and any exponential-size family
`b=exp(zeta n+o(n))`, the shadow has the same exponential rate:

\[
F_{n,d}(b)=\exp(zeta n+o(n)).
\]

Also,

\[
\binom n{\lfloor n/2\rfloor}
\le
\Theta_n
\le
2^{n-1},
\]

so

\[
\lim_{n\to\infty}\frac1n\log\Theta_n=\log2.
\]

The unresolved question is therefore polynomial-scale, not exponential-scale.
A first-order entropy calculation cannot distinguish central-binomial scale
from Glynn scale.

## 7. Finite instances and equality geometry

Finite cases are falsification and regression instances for general theorems,
not the research objective. A finite result is promoted only when it detects a
false implication, validates a uniform theorem against unrestricted rank,
identifies an equality geometry, or certifies a route ceiling.

PR #39 classifies the reduced tangent cone at the `560/784` `perm_8`
exact-shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

Chow realizability of the full equality locus remains open.

## 8. Pairwise and block-overlap frontier

PR #41 proves the transverse common-factor formula and block-rotation
counterexample. PR #44 gives the sharp same-span dual-frame bound. PR #45
proves that low joint factor-span blocks are invisible to the permanent space.
PR #46 proves every central two-term block for `perm_8` is zero. PRs #47--#52
show how these defects feed and reorganize the general tower.

The next numerical improvement cannot come from re-evaluating the same scalar
recurrence. It must lower a capacity through Chow-realizability geometry or
add a non-scalar invariant.

## 9. Restricted sign-family results

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical defect calculations remain diagnostics. Further sign-dictionary
enumeration is not active.

## 10. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- The implication from quotient-image overlap to an equally large
  matched-difference space was rejected until literal overlap was included.
- Common primal-factor count alone is rejected as a global overlap parameter.
- PR #43's coordinate five-term cap 40 remains valid but is not used to infer a
  general flat-sum bound.
- PRs #49 and #50 remain valid weaker stages; PR #51 supersedes their claimed
  stopping points by including the full degree range through `n-1`.
- A scalar-route fixed point is not an upper bound on Chow rank.
- The tail constants are safe universal upper bounds, not exact increments.

## 11. Active pull-request stack

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
                                                      -> current PR #53 fixed-codimension tail constants
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 12. Current open mathematical interfaces

Priority order:

1. **Second-order linear-codimension shadow asymptotics.**  
   The exponential rate is already forced to be the input rate. Determine the
   polynomial prefactor and logarithmic corrections of `F_(n,alpha n)` and
   propagate them through the deficit recurrence.

2. **Scalar polynomial ceiling or strict prefactor gain.**  
   Prove either `Theta_n=O(binom(n,floor(n/2)))` (or another explicit
   polynomial-scale ceiling) or a uniform prefactor gain. First-order entropy
   and finite threshold extrapolation are insufficient.

3. **Uniform Chow-realizability defect.**  
   Prove that exact-shadow or near-shadow Ferrers families cannot arise from
   Chow blocks except in classified cases.

4. **A non-scalar general invariant.**  
   If the scalar ceiling is central-binomial scale, add frame-sensitive,
   multigraded, syzygetic, or representation-valued information.

5. **Cross-`n` recurrence.**  
   Seek a compatible restriction or valuation theorem implying a relation
   such as `R_n>=2R_(n-1)`. Ordinary row expansion is not additive enough.

6. **Finite regression frontiers.**  
   The `perm_6` lower-29 geometry and selected `perm_8` equality questions
   remain testbeds, not the primary general-`n` program.

## 13. Mandatory update rule

Every meaningful future result must update this file in the same pull request.
Each entry records status, statement, evidence, boundary, PR/head, replay
status, superseded dependencies and next interface.

Promotion rules:

- never call an open stacked result canonical on `main`;
- never promote finite-field equality without the characteristic-zero
  direction;
- never replace a coupled catalectic image by a literal sum without a theorem;
- include counterexamples and rejected shortcuts;
- do not add a manager, registry, dispatcher or database for this ledger;
- update this one Markdown file and theorem-specific proof/evidence files.
