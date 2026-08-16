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
Consolidation base: PR #44 theorem head
`fa060f7bab09006aa74d8fde21e2ab9f860489f5`.

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
| `perm_7` | `43 <= ChowRank <= 64` | `STACKED_DRAFT` | PRs #35 and #38 |
| `perm_8` | `78 <= ChowRank <= 128` | `STACKED_DRAFT` | PRs #35 and #38 |
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
| `G-FACTOR-SPAN-ZERO` | If the joint factor span of a block has dimension `<m^2`, its output-degree-`m` literal sum has zero intersection with `D_m(perm_n)`; low-span quotient intersections are exact and matched differences vanish. | current stacked draft, primary and independent replay | current PR |

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

PR #38 embeds certified zero-intersection blocks and yields the current
ordinary lower bounds 43 and 78.

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

### Literal overlap

PR #41 proves the transverse common-factor formula and the block-rotation
counterexample.  PR #44 proves the sharp same-span dual-frame quadratic bound
and its higher-degree KK consequences.  Common primal-factor count alone is
not a valid global overlap parameter.

### Factor-span zero blocks

Let `E_m=D_m(perm_n)` and let `L_I` be the sum of the factor spans of a block
of Chow terms.  The current theorem proves

\[
\dim L_I<m^2
\quad\Longrightarrow\quad
E_m\cap\sum_{i\in I}\mathcal D_m(T_i)=0.
\]

Consequences:

1. the whole block can be projected away with zero permanent-relative defect;
2. for two terms with `dim(L_T+L_U)<m^2`,
   \[
   \rho(F)\cap\rho(G)=\rho(F\cap G),
   \]
   so the matched-difference image is zero;
3. for independent frames with
   \(k=\dim(L_T\cap L_U)\), the exact quotient overlap is at most
   \(\binom km\);
4. at the central degree, every same-span cluster is zero for `n=3` and every
   `n>=5`;
5. every pair is quotient-exact for `n=7` and every central `n>=9`;
6. for `n=8,m=4`, every pair with positive factor-span intersection is exact;
   the transverse equality case remains open.

This closes the same-span matched-difference interface left by PR #44.  It
does not control the equality or high-span strata.

## 7. Restricted sign-family results

The complete restricted sign problem is closed:

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

### Superseded

- PR #26: historical `perm_5` v13 candidate; superseded by repaired v14.
- PR #29: stacked v14 repair; superseded by clean merged PR #30.
- PR #36 and #37: valid numerical consequences but duplicate theorem claims;
  PR #38 retains only the genuinely new omitted-block projection.

### Rejected before theorem promotion

The implication

```text
large quotient-image intersection
=> equally large matched-difference subspace in D_m(perm_n)
```

is false without the literal intersection term.  The correct sequence is

\[
0\to\rho(F\cap G)
\to\rho(F)\cap\rho(G)
\to\operatorname{im}\Delta
\to0.
\]

PRs #41 and #44 control literal overlap.  `G-FACTOR-SPAN-ZERO` now proves
\(\operatorname{im}\Delta=0\) on low-total-span strata.  High-span and equality
strata remain open.

Common-factor count alone is also rejected as a global quadratic-overlap
parameter; same-span quadratic overlap is controlled by dual diagonal-square
geometry.

## 9. Active pull-request stack

```text
PR #31 broad n=6/general research head
  -> PR #35 exact product shadows
      -> PR #38 nested zero-intersection removal
          -> PR #39 perm_8 equality tangent cone
              -> PR #41 consolidated ledger + pairwise overlap
                  -> PR #44 dual-frame same-span overlap
                      -> current PR factor-span zero blocks
```

These are stacked drafts.  A later statement is not canonical on `main` until
the stack is merged or rebased into a clean main-target PR.

## 10. Current open mathematical interfaces

Priority order:

1. **Equality-span matched differences.**  
   The low-span case is closed.  The first concrete boundary is
   `n=8,m=4` with two disjoint eight-dimensional factor spans:
   \[
   \dim(L_T+L_U)=16=m^2.
   \]
   Classify or exclude permanent-relative matched differences there.

2. **High-span multi-term flat sums.**  
   PR #43 gives a coordinate five-term cap 40 but identifies at least 107
   possible nonliteral flat-sum directions.  A valid lower-80 theorem must
   control those valuation-leading relation packets.

3. **Chow realizability of exact-shadow equality spaces.**  
   Determine whether a coupled fourteen-term sum can realize the four-
   dimensional `perm_8` equality locus.

4. **Lower-29 `perm_6` frontier.**  
   Continue only with a theorem acting on the surviving `b=31,...,49`
   geometry; do not recreate a broad scalar state tree.

5. **General correction beyond shadow cardinality.**  
   Seek a frame-sensitive, multigraded or representation-valued invariant
   that supplies a Chow-realizability defect beyond the Ferrers minimum.

## 11. Mandatory update rule

Every meaningful future result must update this file in the same pull request.

Each entry must record:

```text
date
stable result ID
status
precise statement
proof or deterministic evidence path
claim boundary
PR / theorem commit or exact head
CI or replay status
superseded or rejected dependencies
next open interface
```

Promotion rules:

- never call an open stacked result canonical on `main`;
- never promote finite-field equality without the characteristic-zero
  direction;
- never replace a coupled catalectic image by a literal sum without a theorem;
- include counterexamples and rejected shortcuts;
- do not add a manager, registry, dispatcher or database for this ledger;
- update this one Markdown file and the theorem-specific proof/evidence files.
