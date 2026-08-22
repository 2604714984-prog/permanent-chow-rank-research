# N6-119: common column mixing in the \(K_{3,2}\) graph

**Status.** PURE_QQ_COMMON_COLUMN_MIX_K32_RIGIDITY. This is a small
characteristic-zero lemma retained as an independent replay.  The broader
symmetric graph-pair matching statement is now proved in
`docs/n6_k32_annihilator_reduction.md`; the full Chow-incidence problem
remains open.

Let \(A=k^3\), let \(P,Q\) be two-dimensional column spaces, and let
\(H=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}(P,Q)\). In the
ambient \(A\otimes(P\oplus Q)\), set

\[
T=I_A\otimes H,\qquad L=\operatorname{graph}(T),\qquad
M=\operatorname{graph}(-T).
\]

The exact calculation uses the rectangle map \(\beta\) and separates the
four mixed column edges \(02,03,12,13\) from the two same-class edges
\(01,23\). The mixed part has rank exactly three: every nonzero row is a copy,
up to sign, of

\[
(-b,-d,a,c).
\]

For each of the three row pairs, the same-class part has the row types

\[
(0,-2ac),\qquad (1,-ad-bc),\qquad (0,-2bd).
\]

Consequently its rank is one exactly when \(ac=bd=0\), and is two otherwise.
The three row-pair blocks have disjoint output weights, so

\[
\operatorname{rank}\beta(L,M)=
\begin{cases}
6,& ac=bd=0,\\
9,& \text{otherwise}.
\end{cases}
\]

Since \(H\) is invertible, \(ac=bd=0\) is equivalent to either \(b=c=0\) or
\(a=d=0\). Thus \(H\) is monomial. We obtain the pure restricted theorem:

> If the common-row-factor graph \(T=I_3\otimes H\) has full cross rank at
> most six, then \(H\) is monomial and the graph preserves a \(2+2\) column
> matching.

This removes one natural non-matching subfamily from the
\(K_{3,2}/K_{2,3}\) boundary and agrees with the stronger graph-pair theorem
just cited. It does not by itself settle the full Chow-incidence endpoint,
the \(\kappa_2=0\) layer, ordinary lower 29, unrestricted rank 32, or border
rank.

The exact replay is:

~~~text
python scripts/n6_common_column_mix_k32_rigidity.py \
  --verify-json data/n6_common_column_mix_k32_rigidity.json
python -m unittest tests.test_n6_common_column_mix_k32_rigidity -v
~~~
