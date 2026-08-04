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

The lower-26 fixed-count diagnostic and the first alternative-route ceiling
comparison have both been completed. Neither selects a proof route.

## 1. Exact numerical baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
\operatorname{rank}K_{6,3}(\operatorname{perm}_6)=14175.
\]

One degree-six Chow term contributes at most 20 to the middle catalectic and
at most 705 to the first Koszul flattening.

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

fixed terms. The result is:

| fixed terms | initial states | central-pruned survivors | structural states | maximum relation cap |
|---:|---:|---:|---:|---:|
| 6 | 1,035 | 327 | 269 | 37 |
| 7 | 1,225 | 355 | 290 | 33 |
| 8 | 1,520 | 635 | 584 | 33 |

Six fixed terms are arithmetically smallest, but the frontier is not compact.
No fixed count is selected and the central first-Koszul fixed-count route is
suspended for lower 26.

## 5. Completed N6-16: alternative-route ceiling comparison

The exact comparison in
`docs/n6_alternative_route_ceiling_comparison.md` tests three different
ideas.

### 5.1 First higher-wedge Koszul differential

For

\[
\delta_2:
D_m(f)\otimes\Lambda^2V
\to
D_{m-1}(f)\otimes\Lambda^3V,
\]

the exact torus-block replay gives:

| output degree `m` | permanent rank information | one-term rank information | certified integer ratio |
|---:|---:|---:|---:|
| 2 | `127125..127575` | `8730..8745` | 15 |
| 3 | `243936` | `12066` | 21 |
| 4 | `140455` | `9235` | 16 |

The first-Koszul integer ratios at the same degrees are also `15,21,16`.
Thus the first higher wedge does not improve the base rank-ratio ceiling.
At output degree two the repository records windows, not an unsupported
characteristic-zero equality.

### 5.2 Scalar second shadow

If

\[
b=\binom{x}{3}^2,
\]

then the iterated two-dimensional shadow bound gives

\[
\dim\partial^2S\ge x^2.
\]

For `q>=6`, however,

\[
\dim D_1(R)\le\min(36,6q)=36,
\]

so this yields only `x<=6` and `b<=400`, the full central dimension. A
dimension-only second shadow is therefore vacuous on the tested lower-26
fixed counts.

### 5.3 Structured Glynn-family search

The `2^(n-1)` column-uniform sign products form a Walsh-Hadamard basis of the
row-parity-symmetric subspace. The unique expansion of `perm_n` in that basis
uses every term with nonzero coefficient. Hence for `n=6` the natural Glynn
subfamily requires all 32 terms and contains no 25-term decomposition.

This is a restricted-family theorem, not a Chow-rank lower bound.

### N6-16 decision

```text
HIGHER_WEDGE_P2=NO_RATIO_IMPROVEMENT
SCALAR_SECOND_SHADOW=VACUOUS_FOR_Q_GE_6
COLUMN_UNIFORM_GLYNN_SEARCH=REQUIRES_32_TERMS
ROUTE_SELECTED=NONE
```

No tested route has a strict global ceiling capable of proving lower 26.

## 6. Next authorized milestone: structure, not another scalar ceiling

The next work must use information discarded by the completed diagnostics.
Only two small targets are authorized.

### N6-17A — higher-Koszul homology structure

The `p=2`, output-degree-two audit has a nonzero gap between the modular rank
and the preceding-image upper bound. Determine the characteristic-zero
homology space and whether it carries a representation-theoretic obstruction
that survives subtraction of Chow terms.

The goal is a theorem about the **structure** of the homology, not another
base rank ratio.

### N6-17B — column-dependent sign family

Enlarge the structured search from one row-sign vector shared by all columns
to a finite column-dependent sign ansatz. Before optimization, quotient by
row signs, column signs, row/column permutations, and global scaling. Compute
the exact span dimension and test whether `perm_6` lies in the span of a
small orbit family.

This is a falsification/search program, not a lower-bound theorem. It must
remain finite, symmetry-reduced, and exact.

At most one of N6-17A and N6-17B may be promoted after the first diagnostic.

## 7. Falsification first

Before promotion, search for:

- higher-Koszul homology classes that are already generated by Chow terms;
- column-dependent sign terms giving a decomposition with at most 25 terms;
- finite-field rank patterns that fail over characteristic zero;
- apparent quotient gains destroyed by coupled catalectic cancellation; and
- symmetry reductions that identify fewer orbits than the implementation
  assumes.

A dangerous example changes a characteristic-zero conclusion only after
exact rational elimination, an integer minor, or a proved semicontinuity
bridge.

## 8. Hidden assumptions

1. The higher-Koszul homology has useful structure beyond its dimension.
2. A finite column-dependent sign ansatz is broad enough to find a shorter
   decomposition if one exists nearby.
3. Symmetry reduction can keep the structured search small.
4. A new invariant can act on hundreds of fixed-count states simultaneously.
5. The exact value 32 is not contradicted by a shorter decomposition.

None is a theorem.

## 9. Assume every assumption is false

Then lower 25 is the current endpoint of the available method. The correct
repository state is a proved internal lower-25 draft plus an open lower-26
problem, not a larger process architecture.

The completed negative diagnostics remain useful because they prevent three
unproductive expansions: a larger fixed-count state tree, a scalar second
shadow, and a base-ratio-only higher-wedge calculation.

## 10. Fail-closed exit criteria

Suspend a route if any of the following occurs:

- it yields only the already-known integer rank ratio;
- it needs hundreds of states before a new theorem is stated;
- its shadow dimension is bounded only by the ambient dimension;
- it assumes equality between a coupled catalectic image and a literal sum;
- it relies on finite-field equality without characteristic-zero transfer;
- its structured family is already proved to require all 32 terms; or
- an exact decomposition or counterexample invalidates its premise.

## 11. Strongest objection

The route comparison tests only the first higher wedge, a dimension-only
second shadow, and one structured sign family. A genuinely coupled second
shadow, a higher wedge order, or arbitrary column-dependent linear forms may
still contain substantial information.

That objection is valid. It justifies N6-17A or N6-17B. It does not justify a
new registry or a broad computational workflow before one of those targets
produces an exact structural statement.
