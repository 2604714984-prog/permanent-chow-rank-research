# N6-116: the (K_{3,2}) single-cross tangent reduction

**Status.** `EXACT_SINGLE_CROSS_LINEAR_AND_QUADRATIC_TANGENT_CONE_REDUCTION`.
The base field has characteristic zero.

N6-115 identifies a smooth common-(A_3) product component through the
rank-three (K_{3,2}) fixed point. The other first-order pattern is a single
cross-row elementary graph direction. This note analyzes one finite point on
that orbit. It proves an exact quadratic tangent-cone upper bound; it does not
yet identify the completed local germ.

## 1. The finite equality point

Use the coordinate (K_{3,2}) six-plane

\[
 W=\langle00,01,10,11,20,21\rangle\subset k^3\otimes k^4.
\tag{1.1}
\]

Let (T:W\to W^c) have the single nonzero entry (00\mapsto12), and put

\[
 L=\operatorname{graph}(T),\qquad M=\operatorname{graph}(-T).
\tag{1.2}
\]

Direct rational calculation gives

\[
 \dim\langle\beta_{E_{34}}(L,M)\rangle=6,
 \qquad \dim(L+M)=7.
\tag{1.3}
\]

Thus (1.2) lies on the rank-six equality locus but is very far from
complementary.

## 2. Exact linear elimination

Work in the two 36-variable Grassmann graph charts. Put the cross matrix into
a rank-six block form and take its Schur complement. Its linear part is a
(360\times72) integer matrix. Reduction modulo (1{,}000{,}003) has rank
64, and eight explicit rational kernel vectors give the reverse inequality.
Hence

\[
 \operatorname{rank}_{\mathbf Q}L_1=64,
 \qquad\dim\ker L_1=8.
\tag{2.1}
\]

In the exact kernel basis (x_0,\ldots,x_7), all directions are anti-diagonal
between the two Grassmann factors. Their nonzero graph entries are

\[
\begin{array}{c|l}
x_0&00\mapsto12\\
x_1&00\mapsto13\\
x_2&00\mapsto22\\
x_3&01\mapsto12\\
x_4&01\mapsto22\\
x_5&00\mapsto02,\ 10\mapsto12\\
x_6&20\mapsto12\\
x_7&21\mapsto12.
\end{array}
\tag{2.2}
\]

Signs depend on the chosen anti-diagonal convention and do not affect the
monomial ideal below.

## 3. The quadratic tangent-cone support

Substitute the eight exact kernel vectors into the quadratic Schur term, then
reduce its 36 coefficient columns modulo the full linear image. The quotient
has exact rank seven, with reduced generators

\[
 J=(x_1x_2,x_1x_4,x_1x_5,x_2x_5,x_4x_5,x_4x_6,x_4x_7).
\tag{3.1}
\]

The ideal (J) is the squarefree edge ideal of a seven-edge graph. Its four
maximal independent sets are

\[
 \begin{aligned}
 &(0,1,3,6,7),\qquad (0,2,3,4),\\
 &(0,2,3,6,7),\qquad (0,3,5,6,7).
 \end{aligned}
\tag{3.2}

Therefore the reduced quadratic tangent-cone support is contained in the
union of these four coordinate linear spaces.

More importantly, every facet of (3.2), together with the base direction
(00\mapsto12), uses only two coordinates outside (W). The four outside
sets are

\[
 \{12,13\},\quad\{12,22\},\quad\{12,22\},\quad\{02,12\}.
\tag{3.3}

Thus every tangent-cone facet changes both six-planes inside a common
eight-dimensional coordinate ambient. No facet itself contains a
complementary tangent model.

This is an exact statement about the reduced quadratic tangent-cone support,
not a claim that the full formal branch remains in the same eight-space.

## 4. Boundary and next step

The missing step is all-order: one must prove either that the completed germ
is contained in the union of the four relative eight-space incidences, or
that every branch which exits that union acquires cross rank greater than six.
The three facets that do not integrate by straight graph lines may require
higher-order corrections, so quadratic data alone cannot decide this.

N6-116 therefore does not finish the (K_{3,2}) normal cone, exclude the
(K_{2,3}) germ, close the six-color \(\kappa_2=0\) endpoint, prove ordinary
lower 29, determine exact unrestricted rank 32, or make a border-rank claim.

Replay with

```text
python scripts/n6_product_32_single_cross_tangent_reduction.py \
  --verify-json data/n6_product_32_single_cross_tangent_reduction.json
python -m unittest tests.test_n6_product_32_single_cross_tangent_reduction -v
```
