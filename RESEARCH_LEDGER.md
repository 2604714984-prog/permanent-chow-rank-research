# Research ledger

## Purpose

This is the canonical high-level ledger for the active permanent Chow-rank
research repository.

`STATUS.md` remains the detailed theorem inventory.  This file records the
research milestones, numerical boundaries, active branches, rejected routes,
and the next authorized mathematical interfaces.  It is intentionally one
Markdown file rather than a new registry, database, manager, or workflow
layer.

Every future result that changes a theorem, numerical bound, route barrier,
counterexample, equality classification, or open frontier must update this
ledger in the same pull request.

Last consolidated: **2026-08-16**  
Consolidation base: PR #41 head
`56aa9313e7e9524767f8519c86d1d481b3b20fed`.

## Status vocabulary

- `ACCEPTED_BASELINE`: canonical small-`n` result on the merged mainline.
- `PROOF_DRAFT_COMPLETE`: the mathematical argument is written; external
  review may still be pending.
- `COMPUTATION_REPLAYED`: the stated finite interface has deterministic replay.
- `RESTRICTED_FAMILY_THEOREM`: exact only for the named proper subclass.
- `ROUTE_DIAGNOSTIC`: a valid theorem, example, or computation used to select
  or reject a route; not a Chow-rank promotion.
- `STACKED_DRAFT`: valid only on the named open PR stack until merged.
- `SUPERSEDED`: retained for provenance but not canonical.
- `REJECTED`: an attempted implication was found invalid and removed before
  theorem promotion.
- `OPEN`: no theorem has closed the stated frontier.

## 1. Current numerical boundaries

| Object | Current repository boundary | Status | Primary location |
|---|---:|---|---|
| `perm_3` | `ChowRank=4` | `ACCEPTED_BASELINE` | merged small-`n` proof |
| `perm_4` | `ChowRank=8` | `ACCEPTED_BASELINE` | merged exact rational proof |
| `perm_5` | `ChowRank=16` | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | merged PR #30, repaired v14 review boundary |
| `perm_6` | `28 <= ChowRank <= 32` | `PROOF_DRAFT_COMPLETE` lower bound; exact value open in the accessible repository | PR #31 |
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

The universal upper bound in this table is Glynn's
\(2^{n-1}\)-term decomposition.  No unrestricted exact value for
`perm_6`, `perm_7`, or `perm_8` is present in the currently accessible
repository state.

## 2. Canonical small-`n` chain

### `n=3`

\[
\operatorname{ChowRank}(\operatorname{perm}_3)=4.
\]

The proof is pure linear algebra: the permanent first-Koszul rank is 80 and
one Chow term contributes at most 26.

### `n=4`

\[
\operatorname{ChowRank}(\operatorname{perm}_4)=8.
\]

The proof combines the rank-560/92 baseline, the low-rank quadratic
classification, the exact `psi_v` chart, and the double-quotient inequality.

### `n=5`

\[
\operatorname{ChowRank}(\operatorname{perm}_5)=16.
\]

The repaired proof preserves the coupled-catalectic firewall, routes all 58
fixed-six states, and binds the non-finite bridges and exact finite
certificates at the merged PR #30 boundary.  The repository status is a
computer-assisted proof draft with deterministic replay, not a claim that
every step has been proof-assistant formalized.

## 3. General-`n` theorem stack

| ID | Statement | Status | PR / document |
|---|---|---|---|
| `G-PROFILE` | Every lower-bound method that factors only through scalar derivative-space dimensions is capped at `binom(n,floor(n/2))`. | `PROOF_DRAFT_COMPLETE`, merged | PR #32 |
| `G-SIGN` | `ColumnSignRank(perm_n)=RowSignRank(perm_n)=2^(n-1)`. | `RESTRICTED_FAMILY_THEOREM`, merged | PR #33 |
| `G-AFFINE-SLICE` | The same Boolean slice has affine-Segre rank `d+1`; the sign proof does not extend to arbitrary complex diagonal ratios. | `ROUTE_DIAGNOSTIC`, merged | PR #34 |
| `G-KOSZUL` | General first-Koszul, quotient-gain, parity-asymptotic, and fixed-offset multishadow formulas. | `PROOF_DRAFT_COMPLETE` | `STATUS.md`, general docs |
| `G-MACAULAY` | Vector-valued first prolongation satisfies `dim K^(1)<=dim(K)^{<2>}`. | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | general relation docs |
| `G-EXACT-SHADOW` | Exact simultaneous product-shadow minimum is a Ferrers integer program. | `STACKED_DRAFT`, exact independent replay | PR #35 |
| `G-NESTED-SHADOW` | A certified zero-intersection term block can be projected away inside the nonzero-intersection multishadow argument. | `STACKED_DRAFT` | PR #38 |
| `G-PAIR-OVERLAP` | Transverse shared-factor pairs have intersection `binom(s,m)`, but a zero-common-factor block rotation has intersection `2^m binom(r,m)`. | `STACKED_DRAFT`, exact primary and independent replay | PR #41; exact head bound in the PR conversation |
| `G-DUAL-FRAME-OVERLAP` | For same-span independent-factor terms, the quadratic literal overlap is at most `binom(n,2)-ceil((n-s_dual)/2)`, sharply, where `s_dual` counts common projective directions of the dual factor bases; Kruskal--Katona gives higher-degree caps. | `STACKED_DRAFT`, exact primary and independent replay | current PR |

## 4. `perm_6` milestone chain

The detailed sublemma inventory remains in `STATUS.md` and PR #31.  The
high-level ordinary-rank progression is:

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

The lower-29 program is only partial.  The first surviving layer is recorded
at `b=31`, and the current accessible repository does not contain a proof of
ordinary exact rank 32.

The following route barriers are retained because they prevent repeated work:

- scalar central dimensions and scalar homology do not control the required
  coupled collision;
- recursive row expansion does not yield an additive doubling recurrence;
- complete sign families are rigid at 32 but are proper subclasses;
- quotient-image intersection cannot be converted into a permanent
  matched-difference subspace without accounting for the literal intersection
  of the two Chow derivative spaces.

## 5. Exact product-shadow and equality geometry

PR #35 proves the exact product-shadow formula and the finite transitions

\[
F_{7,4}(238)=452,\qquad F_{7,4}(239)=456,
\]

\[
F_{8,4}(560)=784,\qquad F_{8,4}(561)=793.
\]

PR #38 nests the pre-existing zero-intersection theorem into that exact
interface, producing the current lower bounds 43 and 78.

PR #39 studies the `perm_8` equality locus

\[
\mathfrak X=
\{S\in\operatorname{Gr}(560,\mathcal D_4(\operatorname{perm}_8)):
\dim\partial S\le784\}.
\]

At each coordinate flag point:

```text
linear tangent dimension=27
independent quadratic equations=256
reduced tangent-cone support=4 four-planes + 8 three-planes + 7 lines
global equality-locus dimension=4
```

Chow realizability of this equality locus remains open.  PR #39 does not
improve the numerical lower bound 78.

## 6. Pairwise literal-overlap frontier

PR #41 established exact transverse common-factor intersections and a
zero-common-factor block-rotation family with large overlap.  The present
result treats two independent-factor terms with the same factor span.

If `s_dual` is the number of common projective directions of the two dual
factor bases, then

\[
\dim(\mathcal D_2(T)\cap\mathcal D_2(U))
\le
\binom n2-\left\lceil\frac{n-s_{\mathrm{dual}}}{2}\right\rceil,
\]

and the bound is sharp.  The higher-degree overlap is bounded by the inverse
Kruskal--Katona degree-two shadow at that quadratic cap.

The dual count cannot be replaced by the number of common primal factors: an
explicit four-dimensional transition has three common dual directions, only
one common primal factor, and common quadratic dimension five.

This theorem controls only `F_i intersect F_j`.  A numerical rank promotion
still requires simultaneous control of the matched-difference image in the
actual permanent quotient.

## 7. Restricted sign-family results

The sign route is complete as a restricted-family problem:

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

Historical one-defect and two-defect calculations remain valid diagnostics,
but further defect enumeration is not an active route.  The affine-Segre
ceiling shows why the same coefficient slice cannot prove an unrestricted
complex Chow-rank bound.

## 8. Superseded and rejected work

### Superseded

- PR #26: historical `perm_5` v13 candidate; superseded by repaired v14.
- PR #29: stacked v14 repair; superseded by clean merged PR #30.
- PR #36 and PR #37: numerical consequences were valid, but the claimed
  factor-span/hereditary theorem was already canonical.  PR #38 preserves only
  the genuinely new omitted-block projection.

### Rejected before theorem promotion

The attempted implication

```text
large quotient-image intersection
=> equally large matched-difference subspace in D_k(perm_n)
```

is false without controlling the literal intersection of the two Chow
derivative spaces.  The provisional `perm_7>=44` and `perm_8>=79` claims were
removed.  The correct exact sequence is

\[
0\to \rho(F\cap G)
\to \rho(F)\cap\rho(G)
\to \operatorname{im}\Delta
\to0.
\]

`G-PAIR-OVERLAP` and `G-DUAL-FRAME-OVERLAP` study the missing literal term.
Common primal-factor count alone is now also rejected as a quadratic-overlap
parameter; the correct same-span parameter is the intersection geometry of
the dual diagonal-square spaces.

## 9. Active pull-request stack

```text
PR #31  broad n=6/general research head
  -> PR #35 exact product shadows
      -> PR #38 nested zero-intersection removal
          -> PR #39 perm_8 equality tangent cone
              -> PR #41 consolidated ledger + pairwise overlap
                  -> current PR dual-frame same-span overlap
```

These are stacked drafts.  A statement on a later branch is not canonical on
`main` until the stack is merged or rebased into a clean main-target PR.

## 10. Current open mathematical interfaces

Priority order:

1. **Dual-frame literal overlap plus matched difference.**  
   Couple the sharp same-span dual-frame bound with
   \(\operatorname{im}\Delta_{ij}\) in the actual permanent quotient.
   The next theorem must also cover unequal factor spans or prove that
   extremal permanent-relative pairs reduce to the same-span case.

2. **Chow realizability of exact-shadow equality spaces.**  
   Determine whether a coupled fourteen-term sum can realize the four-
   dimensional `perm_8` equality locus.

3. **Lower-29 `perm_6` frontier.**  
   Continue only with a theorem that acts on the surviving `b=31,...,49`
   geometry; do not recreate a broad scalar state tree.

4. **General-`n` correction beyond shadow cardinality.**  
   Seek a frame-sensitive, multigraded, or representation-valued invariant
   that supplies a Chow-realizability defect beyond the exact Ferrers minimum.

## 11. Mandatory update rule

Every meaningful future result must update this file in the same pull request.

A ledger entry must contain:

```text
date
stable result ID
status
precise statement
proof or deterministic evidence path
claim boundary
PR / exact head
CI or replay status
superseded or rejected dependencies
next open interface
```

Promotion rules:

- never call an open stacked result canonical on `main`;
- never promote a finite-field equality without the explicit
  characteristic-zero direction;
- never replace a coupled catalectic image by a literal sum without a theorem;
- include counterexamples and rejected shortcuts, not only positive results;
- do not add a manager, registry, dispatcher, or database for this ledger;
- update one Markdown file and the theorem-specific proof/evidence files.

This policy is a research-discipline rule, not an additional workflow
architecture.
