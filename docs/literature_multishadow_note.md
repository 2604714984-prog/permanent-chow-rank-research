# Literature boundary for the multidimensional-shadow argument

## Status

`PRELIMINARY_LITERATURE_CHECK` — this note records the references actually checked. It is not an exhaustive novelty search.

## 1. Combinatorial input

Boris Bukh's *Multidimensional Kruskal--Katona theorem* proves the following Lovasz-type statement.

For

\[
\mathcal F\subseteq\binom Xr^d
\]

with

\[
|\mathcal F|=\binom xr^d
\]

for a real number `x>=r`, the simultaneous lower shadow satisfies

\[
|\partial\mathcal F|
\ge
\binom x{r-1}^d.
\]

The even-degree proof in this repository uses exactly the case `d=2`, after a row-column torus degeneration of a subspace of the permanent's middle derivative space.

Reference:

- Boris Bukh, *Multidimensional Kruskal--Katona theorem*, arXiv:1009.2375.

## 2. Chow/Koszul context

Yonghui Guan developed flattening and Koszul Young flattening equations for Chow varieties and their secant varieties, including applications connected to permanent complexity. Guan also used prolongation to obtain equations for secant varieties of Chow varieties as `GL(V)`-modules.

References checked:

- Yonghui Guan, *Flattenings and Koszul Young flattenings arising in complexity theory*, arXiv:1510.00886.
- Yonghui Guan, *Equations for secant varieties of Chow varieties*, arXiv:1602.04275.

## 3. Current novelty boundary

The repository's new proof draft combines:

1. a self-transpose middle catalecticant for even-degree permanents;
2. a double-quotient residual-rank estimate;
3. a quotient-prolongation injection; and
4. Bukh's two-dimensional shadow theorem applied to a torus-degenerated derivative-space intersection.

The preliminary search did not locate this exact combination or the resulting explicit bound

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge23.
\]

That observation is **not** a novelty claim. Before publication, the search must be expanded to:

- citations of Bukh's theorem in algebraic complexity;
- permanent product-rank and Chow-rank lower bounds;
- middle catalecticant and derivative-space intersection methods;
- recent work on secants of Chow varieties and split rank;
- non-arXiv journal literature and MathSciNet references.

Until that work is complete, the status remains `PROOF_DRAFT_COMPLETE`, not `NEW_THEOREM_VERIFIED_IN_LITERATURE`.
