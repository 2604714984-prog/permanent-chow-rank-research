# N6-136: straight exclusion for a row-changing four-clique

**Status.** `EXACT_QQ_ROW_CHANGING_FOUR_CLIQUE_STRAIGHT_EXCLUSION` in
characteristic zero.

Fix two distinct row labels in (A_3).  A linear combination of the four
row-changing N6-135 rays in this ordered row pair is a graph operator (D)
whose only nonzero row block is a (2\times2) column block

\[
 C=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

Set (L=\operatorname{graph}(D)) and
(M=\operatorname{graph}(-D)) over the base (W=A_3\otimes P_2).  The exact
cross matrix has shape (36\times18).

## Exact rank calculation

Over (mathbf Q(a,b,c,d)) its rank is 8.  One exact (8\times8) minor is

\[
 -2b(ad-bc)^2.
\]

On the chart (b=0), a second exact minor is

\[
 -2a^2d^3,
\]

so every (det C\ne0) point has cross rank 8.  On the determinant-zero
hypersurface, the chart (a\ne0) is (d=bc/a), where the symbolic cross
rank is 6.  The two boundary charts (a=b=0) and (a=c=0) also have rank 6.
Since the rank-at-most-six locus is closed and (ad-bc) is irreducible, this
proves

\[
 \det C=0\Longrightarrow \operatorname{rank}(\text{cross})\le6,
 \qquad
 \det C\ne0\Longrightarrow \operatorname{rank}(\text{cross})=8.
\]

The same calculation applies to all 12 ordered row pairs by row permutation.

## Chow consequence for straight arcs

When (det C=0), (D) has rank at most one.  Therefore

\[
 \dim(L+M)=6+\operatorname{rank}(D)\le7,
\]

so the straight pair is never complementary.  Thus every straight graph arc
inside any of the 12 row-changing four-cliques is excluded from an actual
12-dimensional Chow section difference.

## Boundary

This is a pure restricted straight-arc theorem.  It does not classify
nonlinear corrections to these four-cliques, non-graph charts, coupled
six-term cocycles, the full (K_{3,2}) or (K_{2,3}) normal cone, ordinary
lower 29, exact (operatorname{ChowRank}(operatorname{perm}_6)), or border
rank.

Replay:

```text
python scripts/n6_k32_row_changing_four_clique_straight_exclusion.py --verify-json data/n6_k32_row_changing_four_clique_straight_exclusion.json
python -m unittest tests.test_n6_k32_row_changing_four_clique_straight_exclusion -v
```
