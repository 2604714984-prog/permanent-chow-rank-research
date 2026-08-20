# N6-121: the full average-relative \(K_{3,2}\) graph germ

**Status.** PURE_FORMAL_LOCAL_K32_AVERAGE_RELATIVE_GERM. This is a
characteristic-zero local theorem in the full graph chart.

Let \(A=k^3\), let \(P,Q\) be two-dimensional column spaces, and write
\[
L=\operatorname{graph}(A_0+T),\qquad
M=\operatorname{graph}(A_0-T),
\]
where \(A_0,T\) are \(6\times6\) matrices from \(A\otimes P\) to
\(A\otimes Q\). The base point is \(A_0=0,T=I_6\). This is the full
average-relative chart: \(A_0\) is the common graph direction and \(T\) is
the relative graph direction.

The rectangle cross matrix at the base has size \(36\times18\) and rank six.
After choosing a six-by-six pivot, the Schur complement has size
\(30\times12\). Differentiating all Schur entries with respect to all 72
matrix variables gives an exact rational Jacobian with
\[
\operatorname{rank}J=70,\qquad \dim\ker J=2.
\]
The two kernel vectors are exactly the relative column scalings
\[
\delta T=\operatorname{diag}(s,t,s,t,s,t);
\]
there is no average direction. After taking \(T[0,0]\) and \(T[1,1]\) as free
coordinates, the remaining \(70\times70\) Jacobian minor has determinant
\[
-70368744177664=-2^{46}\ne0.
\]

The family
\[
A_0=0,\qquad T=\operatorname{diag}(s,t,s,t,s,t)
\]
has identically zero Schur complement, with pivot determinant \(-8t^3\).
The formal implicit-function theorem therefore gives the full local result:

> In the completed average-relative graph chart at \((A_0,T)=(0,I_6)\),
> the rank-at-most-six incidence is exactly
> \(A_0=0,\ T=\operatorname{diag}(s,t,s,t,s,t)\).

Equivalently, the full-rank exceptional direction \(T=I_6\) in the diagonal
\(K_{3,2}\) collision has no average deformation and only the matching
two-parameter relative branch. This is stronger than the separate
relative-only N6-120 calculation.

The result remains local. It does not classify lower-rank exceptional
directions, arbitrary invertible \(T\) globally, the six-term Chow cocycle,
ordinary lower 29, or exact unrestricted Chow rank 32. It is a pure formal
graph-incidence theorem, not yet a global ChowRank theorem.

The exact replay is:

~~~text
python scripts/n6_k32_average_relative_germ.py \
  --verify-json data/n6_k32_average_relative_germ.json
python -m unittest tests.test_n6_k32_average_relative_germ -v
~~~
