# `n=6` research program

## Status

`OPEN`. The currently proved in-repository interval is

\[
24
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 24 is the internal proof draft in
`docs/n6_component_prolongation_exclusion.md`. The upper bound is Glynn's
32-term decomposition. No exact-32 claim is made.

The first lower-25 route diagnostic is complete. It shows that the existing
fixed-term arithmetic does not produce a compact 24-term frontier.

## 1. Exact numerical baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
\operatorname{rank}K_{6,3}(\operatorname{perm}_6)=14175.
\]

One six-factor Chow term contributes at most

\[
20
\]

to the middle catalectic and at most

\[
705
\]

to the first Koszul flattening.

The proved lower-bound history is

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
fixed-four component prolongation:      24
```

## 2. What closed the 23-term problem

Under a hypothetical 23-term decomposition, fixing four terms gives a
nineteen-term residual. Projection and Bukh compression first reduce the
central intersection to

\[
20\le b\le27.
\]

The layers `b=27,26,25` are excluded by common-quotient, one-relation, and
two-relation coupling arguments.

For the remaining layers, let `kappa` be the quadratic relation-kernel
dimension among the four fixed quadratic derivative spaces. Each component
of a cubic relation lies in the first prolongation of a scalar quadratic
space of dimension at most `kappa`. Macaulay growth gives

\[
\dim P^{(1)}\le\kappa^{\langle2\rangle}.
\]

The four-component cubic relation kernel is therefore at most

\[
3\kappa^{\langle2\rangle}.
\]

A block-Sylvester inequality converts this into minimum coupled central
ranks

```text
b=22: 38 > residual upper bound 24
b=23: 50 > residual upper bound 26
b=24: 56 > residual upper bound 28
```

The three states at `b=20,21` were already strict in the quotient-Koszul
budget. Hence no 23-term decomposition exists.

## 3. Exact residual identity retained for later work

For a fixed partial sum `R`, define

\[
E=\mathcal D_3(\operatorname{perm}_6),
\qquad
H=\mathcal D_3(R),
\qquad
b=\dim(E\cap H).
\]

The exact first-Koszul residual estimate is

\[
\boxed{
\operatorname{rank}K_{6,3}(\operatorname{perm}_6-R)
\ge
14175-36b+\Gamma_E(H).
}
\tag{3.1}
\]

The quotient gain `Gamma` is nonnegative but is not additive term by term
for a coupled sum. The one-term full-gain theorem remains valid and useful,
but it does not by itself address the next lower-bound step.

## 4. Completed N6-14 diagnostic: the 24-term frontier

A lower bound of 25 requires excluding a 24-term decomposition. The exact
fixed-`q` diagnostic tests

\[
q=4,5,6
\]

fixed terms without importing the historical 23-term state table.

It regenerates:

1. the projection cap
   \[
   \dim(E_2\cap\sum_{i=1}^qG_i)\le15(q-1)+3;
   \]
2. 65 exact rational Bukh-shadow certificates;
3. the symmetric middle-catalectic inequalities for a `(24-q)`-term
   residual;
4. the quadratic relation-kernel cap;
5. the componentwise Macaulay cubic-relation cap when it is numerically
   relevant;
6. the quotient-Koszul gain and relative-prolongation cap for every state.

The exact results are:

| fixed terms `q` | initial states | surviving states | structural states | relative-prolongation caps |
|---:|---:|---:|---:|---:|
| 4 | 406 | 260 | 194 | `2,38,74` |
| 5 | 325 | 184 | 147 | `23,59` |
| 6 | 325 | 179 | 141 | `8,44` |

Six fixed terms are numerically smallest, but the improvement over five
fixed terms is only five surviving states and six structural states. Its
relative-prolongation caps are also tighter. Therefore N6-14 does not select
a proof frontier and does not prove a lower bound of 25.

The exact record is

```text
docs/n6_lower25_fixed_q_diagnostic.md
scripts/n6_lower25_fixed_q_diagnostic.py
data/n6_lower25_fixed_q_diagnostic.json
```

## 5. Route decision after N6-14

The fixed-term dimension-only route is suspended. The next result must
reduce many structural states at once. Merely expanding the state table is
not research progress.

The preferred directions are:

1. retain the full projection data
   \[
   P_i=\operatorname{pr}_i(\mathcal K)
   \]
   of the quadratic relation kernel rather than only `dim K`;
2. couple first and second derivative shadows;
3. derive a stronger block inequality using pairwise or higher intersections
   among the central derivative spaces;
4. search exactly for structured decompositions with at most 24 terms;
5. test a different flattening if no bulk structural reduction appears.

No single direction is yet promoted.

## 6. Next minimal sequence

### N6-15 — projection-profile theorem or route rejection

Determine whether the projected relation spaces `P_i` obey a uniform
constraint stronger than

\[
\dim P_i\le\dim\mathcal K.
\]

The target is a theorem that reduces the cubic relation cap across a broad
class of states. A case-by-case registry of 141 structural states is not an
acceptable substitute.

### N6-16 — exact structured-decomposition search

Search sparse, symmetry-reduced, and orbit-compatible 24-term ansatzes. Any
candidate must be reconstructed over `Q` or an explicit algebraic number
field before it changes the characteristic-zero boundary.

A reproducible decomposition is a valid research result because it rejectss
the lower-25 program.

### N6-17 — coupled second-shadow diagnostic

Test whether adding one further derivative layer gives a strict numerical
margin on the surviving fixed-five or fixed-six ranges. This remains a
route diagnostic until the relevant shadow theorem and coupling semantics
are written explicitly.

### N6-18 — geometry only after a bulk reduction

Do not introduce SAT/DRAT, Hilbert schemes, Kuranishi calculations,
managers, registries, dispatchers, or multi-repository orchestration unless
a theorem first reduces the unresolved locus to a finite and small set.

## 7. Falsification first

Before promoting any lower-25 route, search for exact counterexamples to its
implicit assumptions:

- structured 24-term decompositions;
- fixed sums with unusually large or badly projected quadratic relation
  kernels;
- central derivative spaces whose pairwise overlaps make the current
  block-Sylvester estimate very loose;
- low quadratic derivative profiles that erase the expected margin;
- quotient gains too small to close the residual budget.

Finite-field examples are diagnostics only. A dangerous example must be
replayed by exact rational elimination, an integer minor, or a proved
semicontinuity bridge before it changes a characteristic-zero statement.

## 8. Hidden assumptions

1. A useful bulk constraint exists on the projected relation spaces.
2. A higher coupled shadow remains computationally and mathematically
   tractable.
3. Conservative central-rank lower bounds for low quadratic profiles are
   not hiding the decisive geometry.
4. State count is correlated with proof complexity.
5. The exact value 32 is not contradicted by a shorter decomposition.

None of these assumptions is promoted to a theorem.

## 9. Assume every assumption is false

Then the lower bound 24 is an endpoint of the current method. The correct
response is to stop extending the fixed-term machinery and pivot to:

- a different flattening;
- an explicit decomposition program;
- a border-versus-ordinary rank separation;
- a new geometric invariant unrelated to the current defect state table.

The repository should not add process complexity merely to preserve the
current route.

## 10. Fail-closed exit criteria

Suspend a lower-25 route if any of the following occurs:

- a reproducible decomposition with at most 24 terms is found;
- the projection-profile theorem gives no improvement over the scalar
  Macaulay cap;
- coupled second shadows leave a broad uncontrolled frontier;
- the remaining quotient-gain requirement is not structurally linked to the
  surviving profiles;
- exact replay requires a large workflow before a finite theorem has been
  stated;
- a claimed characteristic-zero step depends only on finite-field equality
  or random search.

## 11. Strongest objection

The N6-14 state counts deliberately ignore some Chow-realizability
restrictions and assign central rank zero to every individual quadratic
profile of dimension at most ten. The apparent 179-state frontier may be a
large overestimate.

That objection is valid but does not justify deeper enumeration. It places
the burden on N6-15: prove a structural constraint that removes states in
bulk. Without such a theorem, the lower-25 program remains fail-closed.
