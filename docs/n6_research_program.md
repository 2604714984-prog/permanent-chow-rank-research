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

The lower-26 fixed-count diagnostic, the first alternative-route ceiling
comparison, and the output-degree-two second-Koszul homology diagnostic have
all been completed. None selects a proof route.

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

the torus-block replay and the later homology closure give:

| output degree `m` | permanent rank information | one-term rank information | certified integer ratio |
|---:|---:|---:|---:|
| 2 | `127125` exact | `8730` exact | 15 |
| 3 | `243936` exact | `12066` exact | 21 |
| 4 | `140455` exact | `9235` exact | 16 |

The first-Koszul integer ratios at the same degrees are also `15,21,16`.
Thus the first higher wedge does not improve the base rank-ratio ceiling.
The output-degree-two exactness now follows from N6-17 rather than from a
finite-field equality.

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

## 6. Completed N6-17A: exact second-Koszul homology diagnostic

The output-degree-two complex is

\[
D_3(f)\otimes V
\longrightarrow
D_2(f)\otimes\Lambda^2V
\longrightarrow
D_1(f)\otimes\Lambda^3V.
\]

Its middle homology is dual to `Tor_2(A_f,k)_4` for the apolar algebra. The
published Alper--Rowlands formula gives

\[
\beta_{2,4}(A_{\operatorname{perm}_6})=450.
\]

For one independent six-factor Chow term, the complete-intersection resolution
gives

\[
\beta_{2,4}(A_T)=15.
\]

Consequently the former output-degree-two rank windows close exactly at

\[
\operatorname{rank}\delta_2(\operatorname{perm}_6)=127125,
\qquad
\operatorname{rank}\delta_2(T)=8730.
\]

The integer ratio is still only 15.

To test scalar homology as a possible upper-bound invariant, take

\[
T_i=c\prod_{b\in B_i}b,
\]

where the five-element coordinate blocks `B_i` are pairwise disjoint. The
coupled derivative images are proved to split for this family, and the
second-Koszul images have pairwise intersection dimension 25. Therefore

\[
\operatorname{rank}\delta_2\left(\sum_{i=1}^rT_i\right)
=8730r-25\binom r2
\]

and

\[
h_{2,4}\left(\sum_{i=1}^rT_i\right)
=15r+25\binom r2.
\]

At `r=6`, the scalar homology dimension is 465, already larger than the
permanent's 450. Hence any monotone universal upper bound on scalar homology
for at-most-`r` Chow sums is too large to prove lower 26.

### N6-17A decision

```text
OUTPUT_DEGREE_TWO_RANK_WINDOW=CLOSED_EXACTLY
BASE_RANK_RATIO=15_NO_IMPROVEMENT
SCALAR_HOMOLOGY_UPPER_BOUND=REJECTED_FOR_LOWER_26
MULTIGRADED_OR_REPRESENTATION_STRUCTURE=OPEN_NOT_PROMOTED
ROUTE_SELECTED=NONE
```

This diagnostic does not rule out an exact-value classification, multigraded
homology, representation-theoretic homology, or quotient-coupled homology. It
does show that a scalar upper-cap theorem cannot supply the required margin.

## 7. Next authorized diagnostic: finite column-dependent sign pilot

N6-17A produced an exact structural explanation but no promotable lower-bound
invariant. The only remaining pre-authorized experiment is a small version of
N6-17B.

Enlarge the column-uniform Glynn family to terms of the form

\[
G_A
=
\prod_{j=0}^{5}
\left(
\sum_{i=0}^{5}a_{ij}x_{ij}
\right),
\qquad
a_{ij}\in\{\pm1\}.
\]

The first pilot must not search the full `2^36` family. It must first quotient
by row signs, column signs, row permutations, column permutations,
transposition, and global scaling. It may then test only a finite orbit family
whose representatives and orbit reconstruction are independently checkable.

The pilot asks two exact questions:

1. What is the span dimension of the selected symmetry-reduced orbit family?
2. Does the permanent lie in that span, and if so, what is the minimum support
   found by exact linear algebra inside that finite family?

This is a falsification and construction search, not a lower-bound theorem.
No SAT layer, registry, manager, or broad decomposition solver is authorized.

## 8. Falsification first

Before promoting any route, search for:

- a column-dependent sign decomposition using at most 25 terms;
- orbit reductions that identify fewer classes than the implementation assumes;
- finite-field span equalities that fail over characteristic zero;
- apparent quotient gains destroyed by coupled catalectic cancellation; and
- exact-value scalar homology claims contradicted by another small Chow family.

A dangerous example changes a characteristic-zero conclusion only after exact
rational elimination, an integer minor, or a proved semicontinuity bridge.

## 9. Hidden assumptions

1. A finite column-dependent sign ansatz is broad enough to find a shorter
   decomposition if one exists near Glynn's construction.
2. Symmetry reduction can keep the pilot small enough for independent replay.
3. Exact span membership can reveal a useful constructive route before any
   nonlinear solver is introduced.
4. A new invariant can act on hundreds of fixed-count states simultaneously.
5. The exact value 32 is not contradicted by a shorter decomposition.

None is a theorem.

## 10. Assume every assumption is false

Then lower 25 is the current endpoint of the available method. The correct
repository state is a proved internal lower-25 draft plus an open lower-26
problem, not a larger process architecture.

The completed negative diagnostics remain useful because they prevent four
unproductive expansions: a larger fixed-count state tree, a scalar second
shadow, a base-ratio-only higher-wedge calculation, and a monotone scalar
homology upper-bound program.

## 11. Fail-closed exit criteria

Suspend a route if any of the following occurs:

- it yields only an already-known integer rank ratio;
- it needs hundreds of structural states before a new theorem is stated;
- its shadow dimension is bounded only by the ambient dimension;
- it assumes equality between a coupled catalectic image and a literal sum;
- it relies on finite-field equality without characteristic-zero transfer;
- its structured family is already proved to require all 32 terms;
- its symmetry quotient cannot be reconstructed independently; or
- an exact decomposition or counterexample invalidates its premise.

## 12. Strongest objection

The tested sign families remain highly special. A failure to find a 25-term
column-dependent sign decomposition would not support a general lower bound,
and a successful span calculation might still require almost every orbit term.

That objection is valid. It is why N6-17B is limited to a finite pilot with an
explicit construction-or-falsification objective. It does not justify a broad
nonlinear decomposition program before the pilot supplies exact leverage.
