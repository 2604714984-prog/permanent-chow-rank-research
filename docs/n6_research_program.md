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

## 4. Next milestone: test the 24-term frontier

A lower bound of 25 requires excluding a 24-term decomposition. The previous
four-fixed-term state equations change because the residual now has twenty
terms:

- middle-catalectic capacity `20*20=400`;
- first-Koszul capacity `20*705=14100`;
- the former lower edge `b>=20` disappears for four fixed terms.

Therefore the lower-24 proof cannot be relabelled mechanically as a
lower-25 proof.

The next task is a diagnostic theorem generator for a general number `q` of
fixed terms. It must compute, without guessed states:

1. the projection cap
   \[
   \dim(E_2\cap\sum_{i=1}^qG_i)\le15(q-1)+3;
   \]
2. the exact Bukh shadow cap on the central intersection;
3. the symmetric middle-catalectic state inequalities for a
   `(24-q)`-term residual;
4. the quadratic relation-kernel cap;
5. the componentwise Macaulay cubic-relation cap;
6. the quotient-Koszul gain still required after the central-rank
   exclusions.

The purpose is to choose the smallest mathematically effective fixed-term
count, not to create a generic state-management framework.

## 5. Falsification first

Before promoting a lower-25 route, search for exact counterexamples to its
implicit assumptions:

- structured 24-term decompositions;
- fixed sums with unusually large quadratic relation kernels;
- coupled middle-catalectic rank below the proposed block-Sylvester lower
  bound because one of its hypotheses was misapplied;
- low quadratic derivative profiles that defeat the conservative term-rank
  table;
- quotient gains too small to close the residual budget.

Finite-field examples are diagnostics only. A dangerous example must be
replayed by exact rational elimination, an integer minor, or a proved
semicontinuity bridge before it changes a characteristic-zero statement.

## 6. Recommended minimal sequence

### N6-14 — general fixed-`q` arithmetic diagnostic

Extend the exact integer formulas to a hypothetical 24-term decomposition
for `q=4,5,6`. Record every derived state directly from the inequalities.
Do not import the historical 23-term table.

The output is diagnostic until every shadow separator and term-profile
input is proved.

### N6-15 — select one proof frontier

Choose the smallest `q` for which the arithmetic leaves a strict, small
frontier. Reject any route that leaves a broad positive-dimensional
classification problem with no numerical margin.

### N6-16 — classify only the surviving profiles

If a small frontier exists, classify only the individual quadratic
profiles and component relation spaces actually appearing there. Do not
classify all degree-six Chow terms.

### N6-17 — exact route counterexample search

In parallel, test structured fixed sums and candidate 24-term decompositions.
A reproducible counterexample is a result: it rejects the route and prevents
a speculative proof architecture.

### N6-18 — geometry only after finite reduction

Do not introduce SAT/DRAT, Hilbert schemes, Kuranishi calculations,
managers, registries, dispatchers, or multi-repository orchestration unless
a theorem first reduces the unresolved locus to a finite and small set.

## 7. Hidden assumptions

1. A useful fixed-`q` count exists for the 24-term problem.
2. Componentwise Macaulay growth remains numerically strong when the
   quadratic relation kernel is larger than five.
3. Conservative central-rank lower bounds for low quadratic profiles do not
   erase the margin.
4. The block-Sylvester lower bound is close enough to the actual coupled
   rank to be useful.
5. The exact value 32 is not contradicted by a shorter decomposition.

None of these assumptions is promoted to a theorem.

## 8. Assume every assumption is false

Then the lower-24 argument is a local success rather than the beginning of
a monotone induction. The correct response is to stop extending the same
fixed-four machinery and pivot to one of:

- a different fixed-term count;
- a higher Koszul flattening;
- coupled first and second shadows;
- a border-versus-ordinary rank separation;
- explicit decomposition search.

The repository should not add process complexity merely to preserve the
current route.

## 9. Fail-closed exit criteria

Suspend a lower-25 route if any of the following occurs:

- a reproducible decomposition with at most 24 terms is found;
- every tested fixed-term count leaves a large uncontrolled frontier;
- the componentwise prolongation cap loses all strict central-rank margin;
- the remaining quotient-gain requirement is not structurally linked to the
  surviving profiles;
- exact replay requires a large workflow before a finite theorem has been
  stated;
- a claimed characteristic-zero step depends only on finite-field equality
  or random search.

## 10. Strongest objection

The new lower bound 24 may be an endpoint of this method. In the 24-term
problem the twenty-term residual saturates the permanent's middle
catalectic rank, so the central lower edge that made the 23-term frontier
small disappears. A fixed-`q` refinement may therefore produce many states
without a usable margin.

This objection is strong enough to impose a stopping rule: N6-14 must first
show a compact exact frontier. If it does not, the project should pivot
rather than add a larger classification layer.
