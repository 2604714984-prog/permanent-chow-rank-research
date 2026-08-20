# N6-122: all unit graph directions at the \(K_{3,2}\) collision

**Status.** EXACT_QQ_RESTRICTED_K32_UNIT_GRAPH_DIRECTION_CLASSIFICATION.
This is a small characteristic-zero calculation for straight graph arcs only.

Let \(W=A_3\otimes P_2\) be the coordinate \(K_{3,2}\) six-plane and let
\(W^c=A_3\otimes Q_2\). For a unit matrix \(E_{t,s}:W\to W^c\), consider

\[
L_t=\operatorname{graph}(tE_{t,s}),\qquad
M_t=\operatorname{graph}(-tE_{t,s}).
\]

The target and source indices each have a row label in \(\{0,1,2\}\) and a
column label in \(\{0,1\}\). There are four symmetry types according to
whether the row labels and column labels agree. Exact symbolic rank over
\(\mathbf Q(t)\), followed by the complete 36-point check at \(t=1\), gives

\[
\begin{array}{c|cc}
 & \text{same column} & \text{different column}\\ \hline
\text{same row} & 7 & 7\\
\text{different row} & 6 & 6
\end{array}
\]

The six same-row and twelve different-row placements in each column class
account for all 36 unit directions. For every nonzero \(t\), \(E_{t,s}\) has
rank one, so

\[
\dim(L_t+M_t)=6+\operatorname{rank}(E_{t,s})=7.
\]

Therefore the 24 unit directions with cross rank six are all
noncomplementary. This completes the exact straight-ray check suggested by
N6-116: the single-cross representative is not an isolated accident, and no
unit straight ray can be an actual complementary Chow pair.

The passage from the symbolic calculation to every nonzero parameter is not a
genericity assumption. The row-column torus acts diagonally on the ambient
coordinates, preserves the zero-diagonal permanent space, preserves the split
\(W\oplus W^c\), and changes the coefficient of a single source-to-target
graph entry by an arbitrary nonzero ratio. Thus every nonzero parameter is
torus-equivalent to \(t=1\), and the cross rank is unchanged.

This does **not** control nonlinear corrections to these rays, arbitrary
\(6\times6\) graph operators, the remaining \(K_{2,3}/K_{3,2}\) formal germ,
ordinary lower 29, or exact unrestricted Chow rank 32. It is a restricted
exact certificate, not a global Chow-rank theorem.

Replay:

~~~text
python scripts/n6_k32_unit_graph_direction.py \
  --verify-json data/n6_k32_unit_graph_direction.json
python -m unittest tests.test_n6_k32_unit_graph_direction -v
~~~
