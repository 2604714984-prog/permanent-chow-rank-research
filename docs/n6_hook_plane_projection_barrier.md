# A hook-contained plane arrangement with no transverse pair

**Status.** `EXACT_QQ_COUNTEREXAMPLE`, `PURE_DIMENSION_ROUTE_BARRIER`
(G-048).  This is an abstract Grassmannian counterexample, not a Chow
configuration.

Let

\[
 M=(R_3\otimes C_6)+(R_4\otimes C_5)
\]

be the standard 23-dimensional hook in a four-by-six matrix space.  The exact
integer witness consists of six subspaces

\[
 L_1,\ldots,L_6\subset M
\]

with

\[
 \dim L_i=6,\qquad
 \dim(L_i+L_j)=12\quad(i\ne j),
 \qquad \dim\sum_iL_i=23.
\tag{1.1}
\]

Only the three row pairs contained in the complete three-row part of the hook
could possibly give a twelve-dimensional two-row projection.  Nevertheless,
for every one of the fifteen plane pairs and all three candidate row pairs,
the projection of \(L_i+L_j\) has rank exactly ten.  All other row-pair and
every column-pair projection is singular already on the ambient hook.

Thus hook containment, individual six-dimensionality, pairwise transversality,
and total span dimension 23 do **not** force a transverse pair to which N6-061
can be applied.

The construction is elementary.  In each \(L_i\), choose one vector in the
kernel of each of the three candidate row-pair projections and add three
generic integer vectors.  The frozen seed gives all the equalities in (1.1)
and rank ten in each of the 45 projection tests over \(\mathbb Q\).

This witness has no spaces \(D_{ij}\subset E_2\), no common quotient \(W\),
no section cocycle, and no Chow factor-frame realization.  It blocks only the
pure dimension argument

\[
 L_i\subset M,\quad L_i\cap L_j=0,\quad \dim\sum_iL_i=23
 \Longrightarrow \text{an N6-061 transverse pair}.
\]

Any successful use of the 23-dimensional equality hook must therefore retain
the actual section-difference spaces, their minimal shadows and cocycle, or the
common-quotient Chow geometry.

Replay with

```text
python scripts/n6_hook_plane_projection_barrier.py \
  --json data/n6_hook_plane_projection_barrier.json
python -m unittest tests.test_n6_hook_plane_projection_barrier -v
```
