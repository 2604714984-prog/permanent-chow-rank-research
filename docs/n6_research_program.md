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

The first lower-26 fixed-count diagnostic has now been completed. It does not
select a fixed count and suspends the current central first-Koszul route.

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

The layers `b=40,41` are already first-Koszul strict. For the other layers,
the vector-valued Macaulay theorem controls the full colored relation module:

\[
\dim\mathcal K^{(1)}
\le
(\dim\mathcal K)^{\langle2\rangle}.
\]

A block-Sylvester inequality then gives

\[
\operatorname{rank}C_{3,3}(R)
\ge
\sum_i\operatorname{rank}C_{3,3}(T_i)
-
2(\dim\mathcal K)^{\langle2\rangle}.
\]

Exact defect arithmetic excludes every `42<=b<=64`. The smallest strict
margins are two at `b=43,44`.

The proof preserves the coupled-catalectic boundary: `D_3(R)` is always the
image of the catalectic of the sum. Literal sums of individual derivative
spaces are used only as ambient spaces and relation modules.

## 3. Reusable vector-valued Macaulay theorem

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

The proof uses a universal Grassmannian kernel, upper semicontinuity, an
explicit colored-monomial one-parameter subgroup, scalar apolar Macaulay
growth, and superadditivity. The small finite-field replay is diagnostic only.

## 4. Completed N6-15: fixed-count lower-26 diagnostic

A lower bound of 26 would require excluding a 25-term decomposition. The
exact diagnostic evaluated

\[
q\in\{6,7,8\}
\]

fixed terms. For each choice it regenerated:

1. the projection cap `15(q-1)+3`;
2. rational Bukh shadow certificates;
3. every symmetric middle-catalectic state;
4. the quadratic relation-module cap;
5. the vector-valued Macaulay cubic-relation cap;
6. conservative individual central-rank profiles; and
7. the remaining quotient-Koszul requirement.

The result is:

| fixed terms | initial states | central-pruned survivors | structural states | maximum relation cap |
|---:|---:|---:|---:|---:|
| 6 | 1,035 | 327 | 269 | 37 |
| 7 | 1,225 | 355 | 290 | 33 |
| 8 | 1,520 | 635 | 584 | 33 |

The exact details are in
`docs/n6_lower26_fixed_q_diagnostic.md` and
`scripts/n6_lower26_fixed_q_diagnostic.py`.

Six fixed terms are arithmetically smallest, but 327 surviving states and 269
structural states are not a compact frontier. Seven fixed terms are slightly
worse. Eight fixed terms are substantially worse and leave every
shadow-permitted `b` layer nonempty.

Therefore:

```text
N6-15=COMPLETED_ROUTE_DIAGNOSTIC
N6-16_FIXED_COUNT_SELECTION=NO_SELECTION
CENTRAL_FIRST_KOSZUL_FIXED_COUNT_ROUTE=SUSPENDED_FOR_LOWER_26
```

This decision is fail-closed. It does not assert that lower 26 is false or
that no stronger bulk theorem can exist.

## 5. Why low-profile classification alone is not the answer

The diagnostic assigns central-rank lower bound zero to every unresolved
individual quadratic profile of dimension at most ten. This is deliberately
conservative.

Nevertheless, among the 31 surviving six-fixed `b` layers, the all-full
profile is the unique minimizing epsilon profile in 29 layers and tied in the
remaining two. For seven fixed terms it is unique in 30 surviving layers and
tied in three.

Thus a classification of low individual profiles cannot by itself remove the
broad six- or seven-fixed frontier. A useful next theorem must act on the full
coupled relation geometry or change the flattening.

## 6. Next authorized milestone: route comparison, not state expansion

### N6-16 — exact alternative-route ceilings

Compare a small number of genuinely different routes before developing any
of them:

1. a higher Koszul flattening;
2. a coupled first- and second-shadow inequality;
3. a different derivative output degree; and
4. exact structured decomposition search.

For each route, first derive an exact global numerical ceiling from existing
permanent ranks and per-term capacities. A route is promoted only if that
ceiling can in principle exclude 25 terms with a nontrivial margin.

The comparison must remain a small deterministic script and proof note. It
must not introduce a manager, dispatcher, ticket system, registry, SAT layer,
or geometric classification.

### N6-17 — select at most one route

Select one route only when it has:

- a stated characteristic-zero theorem target;
- a strict numerical margin before case classification;
- an explicit coupled/uncoupled boundary;
- a finite falsification test; and
- a minimal exact replay.

If no route passes, record the negative result and stop the lower-26 program
until a new mathematical idea appears.

### N6-18 — counterexample and decomposition search

Independently test structured 25-term decompositions and fixed sums with large
relation modules. A reproducible counterexample to a proposed inequality is a
valid result and takes precedence over building a proof workflow.

### N6-19 — geometry only after a finite theorem

Do not introduce Hilbert schemes, Kuranishi calculations, SAT/DRAT, or a large
orbit registry unless a theorem first reduces the unresolved locus to a small
finite family.

## 7. Falsification first

Before promoting any alternative route, search for:

- structured decompositions with at most 25 terms;
- fixed sums saturating the relevant per-term capacity;
- relation modules whose prolongations attain the Macaulay cap;
- examples close to equality in block-Sylvester;
- coupled shadows that fail to add; and
- finite-field artifacts that disappear over characteristic zero.

Finite-field examples are diagnostic only. A dangerous example changes a
characteristic-zero conclusion only after exact rational elimination, an
integer minor, or a proved semicontinuity bridge.

## 8. Hidden assumptions

1. At least one alternative flattening has unused numerical headroom.
2. A useful coupled two-shadow theorem exists.
3. Structured decomposition search can cover a mathematically meaningful
   family without becoming a generic optimizer.
4. A new invariant can act on hundreds of states simultaneously.
5. The exact value 32 is not contradicted by a shorter decomposition.

None is a theorem.

## 9. Assume every assumption is false

Then lower 25 is the current endpoint of the available method. The correct
repository state is a proved internal lower-25 draft plus an open lower-26
problem, not a larger process architecture.

A negative route comparison is acceptable. It would establish that the known
first-order derivative/Koszul information is numerically saturated and would
prevent unproductive classification work.

## 10. Fail-closed exit criteria

Suspend a route if any of the following occurs:

- its global numerical ceiling cannot exceed the 25-term capacity;
- it requires hundreds of states before a new theorem is stated;
- unresolved low profiles determine the result without a tractable bulk
  bound;
- it assumes equality between a coupled catalectic image and a literal sum;
- it relies on finite-field equality without characteristic-zero transfer;
- it needs a large workflow layer before a finite mathematical reduction; or
- an exact decomposition or counterexample invalidates its premise.

## 11. Strongest objection

The fixed-count diagnostic is conservative and may overstate the true
frontier. A new theorem about Chow-realizable relation modules could collapse
hundreds of states at once.

That is the strongest case for revisiting the route. It is also the reason not
to enumerate the states now: the next deliverable must be the bulk theorem or
an alternative flattening ceiling, not a larger state table.
