# `perm_7` lower-51 v7 execution ledger

## Scope

This ledger executes
`docs/n7_lower51_decisive_near_equality_program_v7.md`.  Every statement
concerns ordinary Chow rank over an algebraically closed field of
characteristic zero.  No border-rank, positive-characteristic, exact-rank-64,
or general-`n` conclusion is included.

## Wave 0 -- handoff freeze

Status: `WAVE0-PASS`.

### Immutable lower-50 input

| object | immutable receipt |
|---|---|
| proof/evidence commit | `4f93d26dc2bed2fd6a5d121ed62b90df29beb75b` |
| proof/evidence tree | `85030c9110cf08a534bdd5ab8f6ee9ae60dd3614` |
| promotion commit | `199a99abc80e72084d3a3d81c71a54957b680288` |
| promotion tree | `8b513f4b5af2631788b63250aef203449aa0120a` |
| v7 package commit | `7b0a6ce63be063ee26ee445d540eaa4d89f5f4af` |
| v7 package tree | `a35c2334d389c68d28b26eec3aa75cf5bd61cb50` |
| main proof Git blob | `492e41a788df0f0a47543268e8bbbc2e7bdfbbac` |
| evidence-manifest Git blob | `e908a0c8f466baecbcd51435d2191cb4acf1f803` |
| canonical proof SHA-256 | `e9a2b1f2e23f261585f16251d708ec1ada6d19c9456a99710067e9e8e697c61c` |
| proof-head workflow | GitHub Actions run `32582021981`, success |
| promotion-head workflow | GitHub Actions run `32583906985`, success |

The imported second-pass audit is
`docs/n7_lower50_v6_second_pass_audit_20260823.md`, with verdict
`FATAL=0`, `MAJOR=0`, `MINOR_MATHEMATICAL=0`, `PASS`.  V6 Modules 00--08
are frozen proof history.  V6 Modules 09--12 are superseded by v7 and are
not independently executable gates.

### Accepted lower-51 inputs

1. `ChowRank(perm_7) >= 50`; hence a hypothetical 50-term identity is
   minimal.
2. For every ordering of its factor spans, the exact slack budget is 35.
3. A rank-seven atom with quotient increment `d=0,...,7` has minimum local
   surplus `(0,22,29,26,17,14,7,0)`.
4. The simple all-rank-seven direct-basis branch is excluded by
   `docs/rethlas_perm7_20260822/round2_quartic_code/simple_n50_exclusion.md`.
5. In the all-rank-seven no-direct-basis lane, every ordering has positive
   increment profile `(1,6,7,7,7,7,7,7)`, and the rank-one quotient
   functional has actual-factor support at most two.
6. The exact representable scalar countermodel consuming all 35 units is a
   `COUNTERMODEL`, not a permanent decomposition.

### Frozen vocabulary and two-lane frontier

`FULL-IDENTITY-SURVIVOR` means all 50 products, coefficients, and the exact
permanent residual are verified.  `STRUCTURAL-SURVIVOR` retains factor-plane
and module data but not the identity.  `PROJECTED-SURVIVOR` satisfies only a
selected quotient system.  `COUNTERMODEL` falsifies a proposed route without
claiming Chow realizability.  Only a `FULL-IDENTITY-SURVIVOR` can refute the
lower-51 target.

The active frontier has two independent rows:

- all-rank-seven packets;
- packets containing a rank-six or lower-rank term.

The preferred dependency path is exact defect classification, subset floors,
an exhaustive represented packet table, and then the residual middle-module
obstruction.  Section and universal-invariant lanes retain their v7 value
gates.

### External-source gate

No external theorem beyond the two already frozen for lower 50 is used at
Wave 0: Shafiei's quadratic generation of the generic permanent apolar ideal
and Bukh's multidimensional shadow theorem with its compression lemmas.  Any
new theorem must be source-checked before it becomes load bearing.

Decisive markers:

```text
V7-INPUT-FROZEN
LOWER50-AUDIT-IMPORTED
V6-L50-COMPLETE
V6-L51-SKELETON-SUPERSEDED
L51-INPUT-LEDGER
SCALAR-SLOPE-BARRIER-FROZEN
SURVIVOR-VOCABULARY
V7-SCOPE-FROZEN
TWO-LANE-FRONTIER
V7-DEPENDENCY-MINIMUM
V7-SOURCE-GATE
V7-HANDOFF-PASS
WAVE0-PASS
```

## Wave 1 -- exact general-`N` defect identity

Status: `IN_PROGRESS`.

For an `N`-term identity, put

\[
 u_i=\dim\mathcal D_3(T_i)=\dim\mathcal D_4(T_i),
 \qquad \delta_i=35-u_i,
\]

and let `h_3,h_4` be the middle dimensions after quotienting the permanent
inverse-system pieces.  Rectangular Sylvester gives

\[
 h_3+h_4\le
 \sum_i u_i-1225
 =35(N-35)-\sum_i\delta_i.                 \tag{1}
\]

For an ordering, let `d_i` be the successive factor-span increments, so
`sum d_i=49`.  Define the local surplus `sigma_i` by writing the two local
symbol ranks plus `delta_i` as `10 d_i+sigma_i`.  The filtered global symbols
give

\[
 h_3+h_4\ge490-\sum_i\delta_i+\sum_i\sigma_i.       \tag{2}
\]

Define the nonnegative filtration surplus and Sylvester defect by

\[
 \eta=(h_3+h_4)-
       \left(490-\sum_i\delta_i+\sum_i\sigma_i\right),
\]

\[
 \epsilon=35(N-35)-\sum_i\delta_i-(h_3+h_4).
\]

Subtracting the two endpoints proves the exact, order-independent identity

\[
 \boxed{\sum_i\sigma_i+\eta+\epsilon=35(N-49)}.      \tag{3}
\]

Thus every hypothetical 50-term identity satisfies

\[
 \boxed{\sum_i\sigma_i+\eta+\epsilon=35}.           \tag{4}
\]

The global quantities `eta` and the ordered local `sigma_i` may redistribute
when the filtration changes; equation (4), nonnegativity, and the same
`epsilon` hold for every ordering.  This completes D-01 through D-03.  The
remaining Wave-1 gate requires the independently replayed local atom catalog
and the subset-floor table; neither is claimed complete here.

Decisive markers:

```text
GENERAL-N-DEFECT-FORMULA
N50-DEFECT-IDENTITY
ALL-ORDER-DEFECT-IDENTITY
```

### Imported rank-seven atoms

D-04 and D-05 are frozen in `data/n7_lower51_rank7_atoms.json`.  The exact
surplus row for increments `0,...,7` is

```text
(0,22,29,26,17,14,7,0).
```

For a rank-one quotient functional supported on `s=1,...,7` actual Boolean
factors, the exact degree-four/degree-three incidence ranks give certified
surplus floors

```text
(22,22,32,32,38,38,43).
```

The three-dimensional loss used here is the sharp permanent quadratic
intersection cap, not an arbitrary quotient discount.  Hence support at
least three, together with the necessary rank-six increment cost 7, exceeds
the complete budget 35.  An independent closed formula and explicit matrices
over primes `1000003` and `1000033` are retained in the generation-3 replay.

The bounded profile enumeration also reconfirms that eight positive
rank-seven increments have the unique budget-feasible profile
`(1,6,7,7,7,7,7,7)`; nine or more are excluded by the exact minimum
deficiency cost `11/3`.  This does not complete D-06 through D-11 or the
all-factor-rank atom catalog.

Decisive markers:

```text
R7-SURPLUS-ROW
R7-D1-SUPPORT-COST
```

### Exact rank-six endpoint atoms

For the six rank-six support normal forms, the middle dimensions are
`(25,25,31,34,35,35)`.  At increment zero both local symbols vanish, so the
surplus is `delta=35-u`.  At the full rank-six quotient both local symbols
are injective, so the surplus is `2u+delta-60=u-25`.  Therefore the exact
endpoint rows, ordered by support size `1,...,6`, are

```text
d=0: (10,10,4,1,0,0)
d=6: (0,0,6,9,10,10).
```

These rows are frozen in `data/n7_lower51_rank6_endpoint_atoms.json`.  They
show why zero-increment high-support terms cannot be discarded by scalar
budget alone, while only support one and two attain equality at full
increment.  Intermediate increments and orientation jump loci remain open,
so neither `R6-SURPLUS-ATLAS` nor `ZERO-INCREMENT-COSTS` is issued yet.

A bounded exact-rational diagnostic now evaluates both unquotiented symbols
on all `6*2^6=384` coordinate quotients of the six normal forms.  Its minimum
`R=0` surplus rows are

```text
s=1,2: (10,25,29,26,19,10,0)
s=3:   (4,25,33,32,25,16,6)
s=4:   (1,25,35,34,28,19,9)
s=5,6: (0,25,35,35,29,20,10).
```

The payload is
`data/n7_lower51_rank6_coordinate_quotient_diagnostic.json`.  Because the
actual minus target is quotiented by `R_T` of dimension at most three and
the quotient orientation need not be coordinate in this frame, these rows
are `PROJECTED-SURVIVOR` diagnostics only.  They identify the intermediate
jump loci that D-07 must control; they are not inserted into the packet
enumerator as theorem floors.

## Wave 1 -- subset floors and minimality

Status: S-01 through S-04 and the finite S-13 controls are complete.  S-05
through S-12 remain to be derived, so `SECTION-MINIMALITY-GATE-PASS` is not
issued.  The separate defect-calculus gate also remains open.

Let `Q` be a retained subpacket of `k` labels and let its complement contain
`q=50-k` labels.  Since the complete identity is minimal, the retained sum is
nonzero.  Applying the frozen simultaneous section cap to the complementary
sum gives, for `d=4,5,6`,

\[
 \dim\sum_{i\in Q}\mathcal D_d(T_i)
 \ge \dim E_d-C_d(50-k).                              \tag{5}
\]

The degree-six derivative space of a nonzero degree-seven product is its
factor span.  Consequently the complete factor-span floor is

\[
 r(Q)\ge49-C_6(50-k).                                 \tag{6}
\]

The 50-row exact table is frozen in
`data/n7_lower51_subset_floors.json`.  In particular, retained packets of
sizes `1,2,3,4` have factor-span floors `0,5,12,16`, degree-five floors
`0,0,15,36`, and degree-four floors `0,0,0,0`; the first nonzero degree-four
floor is 9 at five retained terms.  A zero floor is only the section
consequence; local derivative spaces remain separately nonzero.

Minimal-subsum noncancellation is immediate but must not be inflated: if a
proper nonempty subpacket summed to zero, deleting it would give an identity
with at most 49 nonzero products, contradicting the promoted lower 50.
This proves only noncancellation; it does not force each derivative map of a
subsum to have maximal rank.

Equal factor planes, proportional terms, and partial intersections remain in
the table.  Equal planes do not imply proportional products, while
proportional products with noncancelling coefficients still count as distinct
labels.  Formulae (5)--(6), submodularity, and valid characteristic-zero
linear-rank inequalities are filters; no abstract polymatroid is promoted to
a subspace representation or Chow identity without a separate certificate.

The table is generated from the already independently audited section caps by
`scripts/n7_lower51_subset_floors.py` and checked against a frozen payload by
`tests/test_n7_lower51_subset_floors.py`.  It enumerates exactly 50 rows and
materializes no combinatorial family.

Decisive markers:

```text
N50-SUBSET-FLOORS
N50-DEGREE5-FLOORS
N50-DEGREE4-FLOORS
MINIMAL-SUBSUM-LEMMA
SUBSET-FLOOR-CONTROLS
```

## Wave 3 -- all-rank-seven direct-basis lane

Status: the simple branch and the larger full-block branch are closed.  The
partial-block branch remains open, so `R7-DIRECT-CLOSED` is not issued.

The theorem in `docs/n7_lower51_rank7_full_block_direct_basis.md` removes
global simplicity from the imported direct-basis argument under the exact
hypothesis that every nonzero basis restriction block is invertible.  It
allows parallel planes.  The three-label span floor permits at most seven
parallel nonbasis labels, leaving at least 36 nonparallel labels on which the
existing residual multiplication propagation applies.  It forces
`(K3,K4)=(0,35)` and one common support.  Full support contradicts the
three-label floor; proper support gives a nontrivial direct-sum decomposition
of the permanent and contradicts its scalar centroid.

Decisive markers:

```text
SIMPLE-R7-IMPORTED
R7-PARALLEL-BRANCH
R7-RESIDUAL-KERNELS-FULL-BLOCK
R7-RESIDUAL-PROPAGATION-FULL-BLOCK
R7-CIRCUIT-SUPPORTS-FULL-BLOCK
R7-FULL-BLOCK-BRANCH-CLOSED
```

The exact remaining direct-basis branch has at least one restriction block of
rank `1,...,6`.  No statement in the full-block theorem is applied to that
partial-block locus.

The exchange theorem in
`docs/n7_lower51_rank7_partial_block_reduction.md` sharpens this frontier.
Every block rank is in `{0,1,6,7}`; ranks `2,...,5` each force exchange cost
43.  Pair exchange forces all rank-one maps to factor through one common
source quotient, forces every rank-one/rank-six pair to have combined rank
seven, and permits two rank-six maps only with combined rank six or seven.
Thus a partial plane without a rank-seven pivot contains either a transverse
`1+6` pair or two rank-six blocks with distinct kernels.

Decisive markers:

```text
R7-BLOCK-RANKS
PAIR-EXCHANGE-BUDGET
R7-PARTIAL-BLOCK-KERNEL-TYPES
R7-PARTIAL-D1-SUPPORT-BOUND
```

The residual multiplication theorem for these two-block injective geometries
is still open.  Every surviving partial exchange has a `(1,6)` completion
order, and the rank-one quotient is supported on at most two actual factors:
support at least three would cost `32+7>35`.  Thus the direct-basis and
no-direct-basis rank-seven lanes now share the same support-one/support-two
cross-degree obstruction.  The direct-basis lane is not yet closed.

## Wave 1 -- low-factor-rank endpoint atoms

Status: exact full-increment floors and immediate subset-floor exclusions are
frozen; equality forms and intermediate increments remain open.

Choosing `r` independent factors and applying a diagonal one-parameter
degeneration sends an essential rank-`r` product to a positive `r`-variable
monomial.  Middle catalectic rank is lower semicontinuous, so enumeration of
the positive exponent partitions of seven gives

```text
factor rank r:             1  2  3  4  5
minimum middle dimension:  1  2  4  8 15
full-increment surplus:    26 17  9  3  0.
```

The exact 13 positive partitions are frozen in
`data/n7_lower51_low_rank_endpoint_atoms.json`.  The pair span floor 5
immediately excludes rank pairs `(1,1)`, `(1,2)`, `(1,3)`, and `(2,2)`.
The triple floor 12 remains active in the packet filter.  These statements do
not classify rank-five equality forms or any intermediate quotient direction,
so `LOW-RANK-SURPLUS-ATLAS` and `LOW-RANK-VERDICT` remain open.

Decisive markers:

```text
LOW-RANK-FULL-ENDPOINT-FLOORS
LOW-RANK-PAIR-FLOOR-FILTER
```

## Wave 3 -- all-rank-seven no-direct-basis lane

Status: the quotient two-plane geometry is exhaustive; its cross-degree graph
compatibility remains open.

After six direct rank-seven increments, quotient by their 42-dimensional sum.
The final two positive labels span a seven-dimensional quotient with
increments `(6,1)`.  Reversing only these labels shows that the second
label's quotient plane has rank exactly one or six.  Hence there are only two
geometries: a direct `6+1` pair with intrinsic roles, or two six-dimensional
hyperplanes meeting in dimension five and swapping roles.  In the first case
the rank-one label has actual-factor support one or two; in the second case
both labels satisfy the support-at-most-two theorem.

The proof and exact enumeration are frozen in
`docs/n7_lower51_rank7_no_basis_two_plane_geometry.md` and
`data/n7_lower51_no_basis_two_plane.json`.

Decisive markers:

```text
R7-D1-TWO-BRANCHES
R7-D6-BLOCK
R7-ROLE-CONSISTENCY
R7-ONE-SIX-GEOMETRY
R7-EIGHT-BLOCK-QUOTIENT-DIMENSIONS
```

The graph maps into the first six blocks and the common degree-two-through-five
coefficient system are not determined by quotient dimensions.  Consequently
`R7-MULTIDEGREE-SYSTEM`, `R7-CONNECTING-MAP`, and the lane verdict remain open.

## Wave 2 -- rank-six/rank-seven mixed scalar count

Status: the direct-basis count layer is exact and independently counted; it
is not a represented packet table.

For a direct basis using only rank-six and rank-seven planes, the dimension
equation is `6a+7b=49`.  Its only solutions are the seven-rank-seven basis and
the mixed basis of seven rank-six planes plus one rank-seven plane.  For the
mixed basis, support types `1,...,6` have full-increment costs
`(0,0,6,9,10,10)`.  The remaining 42 labels have zero increment and rank-six
costs `(10,10,4,1,0,0)`; unused labels are rank seven at cost zero.

There are `C(12,5)=792` six-type basis count vectors before the budget and 272
after it.  A recursion and an independent generating-function DP agree on
exactly `11,683,105` compressed basis/outside count patterns.  The earlier
exploratory count `12,339,014` used 43 outside labels and was rejected: an
eight-plane mixed basis leaves exactly 42 labels.

The DP stores only the 272 basis rows and cost distribution; it never
materializes the 11.7 million patterns.  Its payload is
`data/n7_lower51_rank6_mixed_count_dp.json`.

This large exact scalar frontier proves that defect counts alone are not the
v7 packet table.  Representable factor-plane ranks, subset floors, the true
`R_T` quotient, and residual multiplication must still be imposed.

Decisive markers:

```text
R6-COUNT-TABLE-SCALAR
R6-TYPE-SPLIT-ENDPOINTS
R6-MIXED-BASE-DIMENSIONS
```

## Wave 3/4 shared residual middle budget

The corrected direct-basis localization gives the branch-independent cap

\[
 \dim K_3+\dim K_4\le\sum_i u_i-1225-2M_B.
\]

It is 35 for an all-rank-seven 50-term basis.  For the mixed basis of seven
rank-six terms and one rank-seven term it is exactly
`35-basis_full_cost-outside_zero_cost`.  All 666 possible cost pairs were
checked directly, with the 49-term endpoint recovering cap zero.

The proof and controls are in `docs/n7_lower51_residual_middle_budget.md` and
`data/n7_lower51_residual_budget.json`.

Decisive markers:

```text
RESIDUAL-COMPLEX
RESIDUAL-DIM-IDENTITY
R6-RESIDUAL-BUDGETS
```

The cap alone does not give `RESIDUAL-MULTIPLICATION`,
`RESIDUAL-CONNECTING-MAP`, or `RESIDUAL-THEOREM`; those remain the active
load-bearing tasks.

### Redundant-image residual propagation

For an outside rank-seven term put
`W_tc=im((A_c)_1 -> (A_t)_1)`.  The multiplication proof now extends from
invertible restriction blocks to the exact deletion-spanning hypothesis

```text
sum_{j != c} W_tj = (A_t)_1 for every basis block c.
```

It forces `K4 -> (A_t)_4` onto.  Therefore every residual cap below 35 is
incompatible with such an outside block, while cap 35 forces
`(dim K3,dim K4)=(0,35)` and evaluation is an isomorphism.  This eliminates
the redundant-image portion of every positive-cost mixed row.

The proof and its sharp boundary are in
`docs/n7_lower51_residual_redundancy_theorem.md`; the 36 possible integer
caps are replayed by `scripts/n7_lower51_residual_redundancy.py`.

Decisive scoped markers:

```text
RESIDUAL-MULTIPLICATION-REDUNDANT
RESIDUAL-PROPAGATION-REDUNDANT
RESIDUAL-THRESHOLD-REDUNDANT
```

The unrestricted `RESIDUAL-THEOREM` remains open on essential projection
cores: a rank-seven pivot, a transverse one-six pair, or two rank-six blocks
with distinct kernels.

## Wave 2 -- exhaustive scalar direct-basis compositions

For a direct factor-plane basis, let `n_r` count its rank-`r` planes.  The
dimension equation is

```text
sum(r*n_r) = 49.
```

The universal full-increment surplus floors for ranks one through seven are

```text
(26,17,9,3,0,0,0).
```

Applying the 35-unit budget together with the pair and triple subset floors
to every integer solution leaves exactly 69 rank-count vectors.  Exactly 67
contain a rank-at-most-five block; the other two are the all-rank-seven basis
and the seven-rank-six-plus-one-rank-seven basis already isolated above.

Two independent bounded recursions produce the same ordered table in
`scripts/n7_lower51_direct_basis_compositions.py`, frozen at
`data/n7_lower51_direct_basis_compositions.json`.

Decisive scoped markers:

```text
N50-DIRECT-BASE-RANK-COMPOSITIONS
LOW-RANK-DIRECT-BASE-COMPOSITIONS
DIRECT-BASIS-COMPOSITION-INDEPENDENT
```

These 69 rows are exhaustive for the stated scalar gates.  They are not the
represented packet table: rank-six support costs, intermediate increments,
outside zero placements, and the actual factor maps still refine them.
Each frozen row also records the sharp scalar maximum residual cap
`35-full_increment_surplus_floor`.  Thus every positive-cost row can contain
an outside rank-seven term only if that term has an essential projection
block; otherwise the redundant-image theorem excludes it.

### Rank-five binary equality component

After fixing five independent factors, suppose the two extra factors lie in
one coordinate two-plane.  The exact symbolic `35 by 70` catalectic has rank
15 exactly on the divisor

```text
c*(9*a*b-2*c^2)=0,
```

where `a*x1^2+c*x1*x2+b*x2^2` is the product of the two extra factors.
The two components are the zero-cross family and the conic
`9*a*b=2*c^2`; off their union the rank is 18.  This proves that the
rank-five equality locus is larger than both the triple-parallel monomial
boundary and the diagonal family.  See `docs/n7_lower51_rank5_binary_equality.md` and
`scripts/n7_lower51_rank5_binary_equality.py`.

The ternary `6 by 10` middle catalectic and selected exact `5 by 5` minors
exclude every equality form genuinely using three or more frame directions.
Thus, up to a frame permutation, the displayed binary divisor is the full
middle-dimension-15 equality locus.
After coordinate scaling it consists of three orbit types: the
triple-parallel boundary, the two-square diagonal type, and the conic type
with invariant `c^2/(a*b)=9/2`.  Every other rank-five product has middle
dimension at least 18 and therefore full-increment surplus at least 3.
Splitting each of the 69 direct-basis rank rows by the number of equality
versus near-equality rank-five blocks leaves 240 typed scalar rows; each row
records the maximum allowed number of near-equality blocks in the frozen
direct-basis payload.

Decisive markers:

```text
R5-BINARY-EQUALITY-FAMILY
R5-EQUALITY-FORMS
R5-FULL-INCREMENT-GAP
```

Intermediate quotient directions and full 50-term rank-five packets remain
open; this marker concerns the full-increment equality normal forms only.

## Waves 5 and optional lanes -- value-gate decisions

The exact existing Fitting/Schur replay passes but proves that every tested
bare-presentation universal construction misses either the Glynn retention
gate or the `F2` killing gate.  It is frozen as `UNIVERSAL-STOP`; no variant of
the same functor is reopened.  The exact section Koszul/Young replay has
maximum standard ceiling 60, and the 10,426-case profile diagnostic also
passes.  Since no residual invariant currently transports to the section,
the section lane stops at `STOP-UNTIL-RESIDUAL-TRANSPORT`.

The detailed decision ledger is `docs/n7_lower51_v7_route_decisions.md`.

Decisive markers:

```text
INVARIANT-SHORTLIST
FITTING-DECISION
TOR-COSPAN-DECISION
INVARIANT-STOP-DECISION
UNIVERSAL-BOUNDARY
UNIVERSAL-STOP
SECTION-CEILING
SECTION-CONTROLS
SECTION-ADVANCE-OR-STOP
SECTION-LANE-VERDICT-STOP-UNTIL-RESIDUAL-TRANSPORT
```

The retained active invariant is the true permanent degree-two-through-five
connecting system.  It has not yet been constructed with the required
subadditivity and boundary coverage, so `FINAL-OBSTRUCTION-MAP` is not issued.
