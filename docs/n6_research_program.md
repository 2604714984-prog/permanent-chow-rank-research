# `n=6` research program

## Status

`OPEN`. The current in-repository proof-draft interval is

\[
25
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 25 is the fixed-six relation-module argument in
`docs/n6_fixed_six_lower25.md`. The upper bound is Glynn's 32-term
decomposition. No lower-26, border-lower-25, or exact-32 claim is made.

## 1. Exact numerical baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
\operatorname{rank}K_{6,3}(\operatorname{perm}_6)=14175.
\]

One degree-six Chow term contributes at most

\[
20
\]

to the middle catalectic and at most

\[
705
\]

to the first Koszul flattening.

The current lower-bound history is

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
fixed-four scalar prolongation:         24
fixed-six vector relation module:       25
```

## 2. What closed the 24-term problem

Assume a hypothetical 24-term decomposition and fix six terms. The residual
has eighteen terms. The quadratic projection cap is

\[
5\cdot15+3=78.
\]

Bukh compression and the symmetric middle catalectic give

\[
40\le b\le64,
\]

where

\[
b
=
\dim\left(
\mathcal D_3(\operatorname{perm}_6)
\cap
\mathcal D_3(R)
\right).
\]

The layers `b=40,41` are already first-Koszul strict.

For the other layers, let

\[
\mathcal K
=
\ker\left(
\bigoplus_{i=1}^6\mathcal D_2(T_i)
\longrightarrow
\sum_{i=1}^6\mathcal D_2(T_i)
\right),
\qquad
\kappa=\dim\mathcal K.
\]

The vector-valued Macaulay theorem gives

\[
\dim\mathcal K^{(1)}
\le
\kappa^{\langle2\rangle}.
\]

The full cubic relation module is contained in `K^(1)`. A block-Sylvester
inequality for the six symmetric middle catalectics then gives

\[
\operatorname{rank}C_{3,3}(R)
\ge
\sum_i\operatorname{rank}C_{3,3}(T_i)
-
2\kappa^{\langle2\rangle}.
\]

Exact defect arithmetic excludes all `42<=b<=64`. The smallest strict
margins are two at `b=43,44`. A second implementation independently scans
all

\[
16^6=16,777,216
\]

labelled quadratic-defect tuples.

The proof preserves the coupled-catalectic boundary: `D_3(R)` is always the
image of the catalectic of the sum. Literal sums of individual derivative
spaces are used only as ambient spaces and relation modules.

## 3. The vector-valued Macaulay theorem as a reusable result

For arbitrary finite-dimensional `W,V` and

\[
\mathcal K\subseteq W\otimes\operatorname{Sym}^2V,
\qquad
\dim\mathcal K=k,
\]

the first prolongation satisfies

\[
\boxed{
\dim\mathcal K^{(1)}\le k^{\langle2\rangle}.
}
\]

The proof uses:

1. a universal vector-bundle map over `Gr(k,W tensor Sym^2 V)`;
2. upper semicontinuity of fiber nullity;
3. an explicit one-parameter subgroup separating all colored quadratic
   monomials;
4. splitting of the coordinate limit by color;
5. scalar apolar Macaulay growth; and
6. superadditivity of the degree-two Macaulay successor.

The small finite-field calculation in the audit is only a deterministic
counterexample search. It does not carry the characteristic-zero proof.

## 4. Next milestone: test the 25-term frontier

A lower bound of 26 requires excluding a 25-term decomposition. The lower-25
state equations cannot be relabelled mechanically. For a fixed count `q`,
the residual has `25-q` terms and therefore capacities

\[
20(25-q)
\]

for the middle catalectic and

\[
705(25-q)
\]

for the first Koszul flattening.

The first authorized task is an exact arithmetic diagnostic for a small set
of candidate fixed counts, initially

\[
q\in\{6,7,8\}.
\]

For each `q`, it must derive rather than guess:

1. the projection cap
   \[
   15(q-1)+3;
   \]
2. the exact Bukh central-intersection cap;
3. the symmetric middle-catalectic inequalities;
4. the quadratic relation-module cap;
5. the vector-valued Macaulay cubic-relation cap;
6. conservative individual central-rank profiles; and
7. the remaining quotient-Koszul requirement.

The goal is to select one compact frontier. It is not to create a generic
state-management framework.

## 5. Falsification first

Before promoting a lower-26 route, search for exact counterexamples to its
implicit assumptions:

- structured 25-term decompositions;
- fixed sums with large quadratic relation modules;
- relation modules whose prolongations approach the Macaulay cap;
- coupled middle-catalectic ranks close to the block-Sylvester lower bound;
- low individual quadratic profiles that erase the numerical margin; and
- quotient gains too small to close the residual budget.

Finite-field examples are diagnostics only. Any dangerous example must be
replayed by exact rational elimination, an integer minor, or a proved
semicontinuity bridge before it changes a characteristic-zero conclusion.

## 6. Minimal sequence

### N6-15 — fixed-count arithmetic diagnostic

Evaluate `q=6,7,8` under a hypothetical 25-term decomposition. Record every
state directly from the proved inequalities. If all three leave a broad
frontier, stop extending the current route.

### N6-16 — select one frontier

Choose the smallest `q` with a strict numerical margin and a compact
relation-module range. Do not combine multiple weak frontiers into a larger
workflow.

### N6-17 — classify only surviving term profiles

If a small frontier exists, classify only the individual quadratic and
central profiles that attain its minima. Preserve the conservative zero
lower bound for unresolved low profiles.

### N6-18 — independent route counterexample search

Test structured fixed sums and candidate 25-term decompositions. A
reproducible counterexample is a valid research result because it prevents a
speculative proof architecture.

### N6-19 — geometry only after finite reduction

Do not introduce SAT/DRAT, Hilbert schemes, Kuranishi calculations, managers,
registries, dispatchers, or multi-repository orchestration unless a theorem
first reduces the unresolved locus to a finite and small set.

## 7. Hidden assumptions

1. One of `q=6,7,8` leaves a useful fixed-count frontier.
2. The vector-valued Macaulay cap remains numerically strong for the larger
   relation dimensions in the 25-term problem.
3. Conservative lower bounds for low individual profiles do not erase the
   margin.
4. The block-Sylvester estimate is sufficiently close to the actual coupled
   rank.
5. The exact value 32 is not contradicted by a shorter decomposition.

None of these assumptions is promoted to a theorem.

## 8. Assume every assumption is false

Then lower 25 is an endpoint of this central first-Koszul method rather than
the beginning of a monotone induction. The correct response is to pivot to
one of:

- a higher Koszul flattening;
- coupled first and second shadows;
- a different derivative output degree;
- a border-versus-ordinary rank separation; or
- explicit decomposition search.

The repository must not add process complexity merely to preserve the
current route.

## 9. Fail-closed exit criteria

Suspend the lower-26 route if any of the following occurs:

- a reproducible decomposition with at most 25 terms is found;
- every tested fixed count leaves a large uncontrolled frontier;
- vector-valued Macaulay growth loses all strict central-rank margin;
- unresolved low term profiles determine the minimum without a tractable
  classification;
- exact replay requires a large workflow before a finite theorem has been
  stated; or
- a claimed characteristic-zero step depends only on finite-field equality
  or random search.

## 10. Strongest objection

The relation-module method may now be near saturation. Raising the
hypothetical term count increases the residual capacity while also requiring
more fixed terms and larger relation spaces. Macaulay growth can then consume
the entire block-Sylvester margin.

This objection is decisive enough to impose a stopping rule: the fixed-count
diagnostic must first exhibit a compact strict frontier. Otherwise the
project pivots rather than building a larger classification layer.
