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
