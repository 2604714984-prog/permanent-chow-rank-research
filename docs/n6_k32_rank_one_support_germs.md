# N6-137: two rank-one row-changing support germs

**Status.** `EXACT_QQ_RANK_ONE_SUPPORT_GERMS` in characteristic zero.

N6-136 excludes the straight graph arc in every row-changing four-clique,
but does not by itself analyze nonlinear corrections.  N6-137 computes the
completed graph germ at two of the rank-one coefficient support types.

## Exact local calculation

Fix a row-changing coefficient block and take
(L=\operatorname{graph}(D)), (M=\operatorname{graph}(-D)).  For both the
same-source-column support (left[\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\right])
and the full support
(left[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right]), the exact QQ
Schur Jacobian at the finite pair has shape (360\times72), rank 67, and
kernel dimension 5.  After eliminating the linear variables, the quadratic
initial ideals are respectively

\[
 (x_0-x_1)(x_2,x_3,x_4),
 \qquad
 (x_1-x_2)(x_0-x_2,x_3,x_4).
\]

Each ideal is the intersection of two linear branch ideals.  Direct symbolic
substitution into the full cross matrix shows that both branches in each case
have cross rank at most 6 for all parameters.  Their graph operator (D) has
rank at most 1, so

\[
 \dim(L+M)=6+\operatorname{rank}(D)\le7.
\]

The branch inclusions give the reverse initial-ideal inclusion, while the
quadratic Schur equations give the forward inclusion.  The completed filtered
lifting therefore gives the exact two-branch germ in these two support types;
both branches are noncomplementary.

## Boundary

The single-cell support is covered by N6-123, while the same-target-row
support is not covered by this certificate.  Non-graph charts, coupled
six-term cocycles, the full (K_{3,2}/K_{2,3}) normal cone, ordinary lower 29,
exact \(\operatorname{ChowRank}(\operatorname{perm}_6)\), and border rank
remain open.

Replay:

```text
python scripts/n6_k32_rank_one_support_germs.py --verify-json data/n6_k32_rank_one_support_germs.json
python -m unittest tests.test_n6_k32_rank_one_support_germs -v
```
