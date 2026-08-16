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
Consolidation base: PR #51 theorem head
`bab95bc412366ac18b5f10089c73ef033bdfa5b0`.

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
| `perm_4` | `ChowRank=8` | `ACCEPTED_BASELINE` | merged exact-rational proof |
| `perm_5` | `ChowRank=16` | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | merged PR #30 |
| `perm_6` | `28 <= ChowRank <= 32` | specialized lower-bound draft; exact value open in accessible repository | PR #31 |
| `perm_7` | `49 <= ChowRank <= 64` | `STACKED_DRAFT` | PR #51 |
| `perm_8` | `90 <= ChowRank <= 128` | `STACKED_DRAFT` | PR #51 |
| `perm_9` | `164 <= ChowRank <= 256` | `STACKED_DRAFT` | PR #51 |
| `perm_10` | `307 <= ChowRank <= 512` | `STACKED_DRAFT` | PR #51 |
| `perm_11` | `ChowRank >= 508` | earlier stacked bound; full tower not yet replayed at this size | PR #38 |
| `perm_12` | `ChowRank >= 970` | earlier stacked bound; full tower not yet replayed at this size | PR #38 |
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
| `G-SHADOW-COMPLEMENT` | `Gamma_(n,d)(A_(d-1)-z)=A_d-F_(n,n-d+1)(z)` and the equivalent max-plus deficit transport recurrence. | current general-`n` stacked draft, two independent exact DPs | PR #52 |

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

## 5. Full-degree tower envelope

For

\[
M_{n,d}=\binom nd,\qquad A_{n,d}=M_{n,d}^2,
\]

let `Gamma_(n,d)` be the inverse exact first-shadow capacity and define

\[
C_{n,d}(q)
=\min\{A_{n,d},qM_{n,d},
\Gamma_{n,d}(B_{n,d-1}(q))\}.
\]

The repeated block-projection closure is the exact prefix envelope

\[
B_{n,d}(q)
=qM_{n,d}
+\min_{0\le t\le q}
\bigl(C_{n,d}(t)-tM_{n,d}\bigr).
\]

A decomposition by `q` terms must cover every permanent derivative space, so
all rows must have saturated at `q`. Writing

\[
Q_{n,d}=\min\{q:B_{n,d}(q)=A_{n,d}\},
\]

gives

\[
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge\Theta_n:=\max_{1\le d\le n-1}Q_{n,d}.
\]

PR #51 replays the exact threshold rows

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
specialized `n=6` lower bound. It does not absorb those coupled geometric
arguments.

### Shadow-complement deficit form

PR #52 replaces the inverse-shadow transition by the exact complementary
identity

\[
\Gamma_{n,d}(A_{n,d-1}-z)
=
A_{n,d}-F_{n,n-d+1}(z).
\]

Writing

\[
D_{n,d}(q)=A_{n,d}-B_{n,d}(q),
\]

the direct deficit and projection closure become

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

This is an exact reformulation, not a new numerical lower bound. It exposes
the scalar tower as complementary-shadow transport and is now the preferred
interface for uniform asymptotic analysis.

## 6. Finite instances and equality geometry

Finite cases are falsification and regression instances for general theorems,
not the research objective. A finite result is promoted only when it detects a
false general implication, validates a uniform theorem against unrestricted
rank, identifies an equality geometry, or certifies a route ceiling.

PR #39 classifies the reduced tangent cone at the `560/784` `perm_8` exact-
shadow flag locus:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent cone=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

Chow realizability of the full equality locus remains open.

## 7. Pairwise and block-overlap frontier

PR #41 proves the transverse common-factor formula and block-rotation
counterexample. PR #44 gives the sharp same-span dual-frame bound. PR #45
proves that low joint factor-span blocks are invisible to the permanent space.
PR #46 proves every central two-term block for `perm_8` is zero. PRs #47--#51
show how these permanent-relative defects feed the general tower.

The next improvement cannot come from re-evaluating the same scalar recurrence;
it must lower a capacity through Chow-realizability geometry or add a
non-scalar invariant.

## 8. Restricted sign-family results

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=2^{n-1}.
\]

Historical one- and two-defect calculations remain diagnostics. Further sign
dictionary enumeration is not active.

## 9. Superseded and rejected work

- PR #26 is superseded by repaired `perm_5` v14.
- PR #29 is superseded by clean merged PR #30.
- PRs #36 and #37 duplicated a canonical theorem; PR #38 retains only the new
  projection step.
- The implication from quotient-image overlap to an equally large matched-
  difference space was rejected until literal overlap was included.
- Common primal-factor count alone is rejected as a global overlap parameter.
- PR #43's coordinate five-term cap 40 remains valid but is not used to infer
  a general flat-sum bound.
- PRs #49 and #50 remain valid weaker stages, but PR #51 supersedes their
  claimed stopping points by including the full degree range through `n-1`.
- A scalar-route fixed point is not an upper bound on Chow rank.

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
                                                  -> current PR #52 shadow-complement deficit duality
```

These are stacked drafts and are not canonical on `main` until merged or
rebased into a clean main-target PR.

## 11. Current open mathematical interfaces

Priority order:

1. **Uniform asymptotics of the deficit transport recurrence.**  
   Analyze the exact complementary-shadow/max-plus system for
   `d=alpha*n` and `q=exp(rho*n+o(n))`. Prove either a strict uniform gain or
   a ceiling theorem for the complete scalar tower.

2. **Uniform Chow-realizability defect.**  
   Lower a capacity `B_(n,d)(q)` by proving that an exact-shadow or near-shadow
   Ferrers family cannot arise from a Chow block except in classified cases.

3. **A non-scalar general invariant.**  
   If the deficit system has a central-binomial ceiling, add a frame-sensitive,
   multigraded or representation-valued invariant rather than another scalar
   finite table.

4. **Cross-`n` recurrence.**  
   Seek a compatible restriction or valuation theorem implying a relation such
   as `R_n>=2R_(n-1)`. Ordinary row expansion alone is not additive enough.

5. **Finite regression frontiers.**  
   The `perm_6` lower-29 geometry and selected `perm_8` equality questions
   remain testbeds, not the primary general-`n` program.

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
