# The rank-six fixed stratum in the (3\times4) product space

**Status.** EXACT_RANK_SIX_FIXED_STRATUM_COMPLEMENT_EXCLUSION.

Let

\[
 V=A\otimes B,qquad \dim A=3,quad\dim B=4,qquad
 E_{34}=S_0(A)\otimes S_0(B),                           \tag{0.1}
\]

and let (eta(L,M)) be the N6-108 cross image of two six-planes.  N6-108
proves that complementary planes have cross rank at least six.  A
twelve-dimensional cross-free subspace of the eighteen-dimensional
(E_{34}) sits exactly at equality.  This note analyzes every torus-fixed
point whose cross rank is **exactly six**.

The result is a strict reduction, not the final (3\times4) exclusion:

> Every projective component of
> ({(L,M):\dim\beta(L,M)\le6}) whose torus-fixed point has cross rank six
> is contained in the noncomplementary boundary.  Hence a complementary
> component, if one exists, must specialize to one of the rank-three or
> rank-five fixed strata.

The coordinate enumeration and local ranks are deterministic exact
certificates.  Modular nonzero minors are used only as lower bounds over
(mathbf Q), with integer kernels or weight-block dimensions supplying the
matching upper bounds.

## 1. Complete fixed-point classification

There are (924) coordinate six-planes in the twelve coordinates of
(A_3\otimes B_4).  Checking all

\[
 924^2=853,776                                             \tag{1.1}
\]

ordered pairs gives

\[
\begin{array}{c|rrr}
\dim\beta&3&5&6\\ \hline
\#\text{ ordered pairs}&18&72&2424.
\end{array}                                               \tag{1.2}
\]

The rank-six pairs form twenty orbits under row permutations, column
permutations, and swapping (L,M).  Eighteen orbits, containing 2,268
ordered pairs, lie in a common coordinate space

\[
 W=A_{01}\otimes B,qquad \dim W=8.                       \tag{1.3}
\]

The remaining two orbits are diagonal.  Their row profiles are
((4,1,1)) and ((3,2,1)), with orbit sizes twelve and 144.  No coordinate
rank-six pair is complementary.

## 2. The eighteen common-two-row orbits

At any of these fixed pairs, the two Grassmann graph charts have 72
variables.  Exactly 24 graph variables remain inside (W), and 48 point
to the missing row.  Since

\[
 S_0(A_{01})\otimes S_0(B)
\]

has dimension six, every pair of six-planes contained in (W) automatically
has cross rank at most six.  Thus all local determinantal equations vanish
identically when the 48 normal variables vanish.

For every one of the eighteen orbit representatives, the full first Schur
map has exact rank 48, while its restriction to the 24 internal variables
has rank zero.  Therefore one may choose 48 equations with invertible normal
Jacobian.  The formal implicit-function theorem has the unique solution

\[
 \text{all normal variables}=0.                           \tag{2.1}
\]

Every completed local germ remains in the fixed eight-space (W).  Two
six-planes in (W) intersect in dimension at least four, so none is
complementary.

## 3. The diagonal ((4,1,1)) orbit

Take

\[
 F=\langle00,01,02,03,10,20\rangle.                      \tag{3.1}
\]

At ((F,F)), the (360\times72) first Schur system has exact rank 69 and
an explicit three-dimensional integer kernel.  Introduce average and
difference graph variables.  The difference-variable block has full rank
36.  Hence the difference is a unique formal function of the average
variables.

The determinantal equations are invariant under swapping the two planes,
which fixes the average and negates the difference.  Formal uniqueness then
forces the difference to vanish.  Thus the complete germ is diagonal
(L=M), again excluding complementarity.

## 4. The staircase ((3,2,1)) orbit

The last representative is

\[
 F=\langle00,01,02,10,11,20\rangle.                      \tag{4.1}
\]

The first Schur system has exact rank 61.  Its eleven-dimensional integer
kernel consists of nine diagonal directions and two separating directions.
The latter still move inside the coordinate (3\times3) subspace, but a
first-order statement alone does not exclude a higher-order escape.

Put the base cross matrix into the constant normal form

\[
 \begin{pmatrix}I_6&0\\0&0\end{pmatrix}.                \tag{4.2}
\]

For tangent directions (u,v), the degree-two Schur obstruction is

\[
 D_2(u,v)-C_1(u)B_1(v)-C_1(v)B_1(u),                    \tag{4.3}
\]

with the second copy omitted for a square.  Quotienting the 66 quadratic
columns by the 61-dimensional linear image gives exact rank twenty.  In
the eleven tangent coordinates (x_0,\ldots,x_{10}), row reduction gives
the twenty unit monomials

\[
\begin{split}
J=(&x_0x_1,x_0x_3,x_0x_4,x_0x_7,
 x_1x_2,x_1x_4,x_1x_8,x_2x_4,\\
 &x_3x_6,x_3x_{10},x_4x_6,x_4x_8,x_4x_{10},
 x_5x_6,x_5x_8,x_5x_{10},\\
 &x_6x_7,x_7x_8,x_7x_{10},x_9x_{10}).                  \tag{4.4}
\end{split}
\]

The twenty monomials occupy twelve singleton torus-weight blocks and four
two-monomial blocks.  Every block has full rank modulo (1,000,003), hence
also over (mathbf Q).  Thus

\[
 J\subset\operatorname{in}_{\mathfrak m}I                \tag{4.5}
\]

in the completed local determinantal ideal.  No equality of the full
initial ideal is asserted or needed.

The edge ideal (J) has nine maximal independent facets:

\[
\begin{gathered}
0259,quad169,quad13579,quad23579,quad34579,\\
2389,quad02689,quad16,10,quad0268,10.                \tag{4.6}
\end{gathered}
\]

Here a string lists the retained variable indices.

## 5. The complement determinant has no possible initial weight

In the graph chart at ((F,F)), complementarity is the nonvanishing of
(det(M-L)).  Its row-column torus weight relative to (4.1) is

\[
 \chi=(-2,0,2;,-3,-1,1,3).                              \tag{5.1}
\]

Among the eleven tangent weights, only (x_1) has positive last-column
weight, and that weight is (+1).  Any monomial of weight (chi) would
therefore contain (x_1^3).  The only facets of (4.6) containing (x_1)
are

\[
 169,qquad13579,qquad16,10.                            \tag{5.2}
\]

The middle facet has no positive column-two weight after the contribution
of (x_1^3), so it cannot have weight (chi).  In the first facet the
column equations force exponents

\[
 (x_1,x_6,x_9)=(3,4,3),                                  \tag{5.3}
\]

and in the last they force

\[
 (x_1,x_6,x_{10})=(3,1,3).                               \tag{5.4}
\]

All variables in (5.3) and (5.4) have zero row weight, whereas the row part
of (chi) is ((-2,0,2)).  Hence no monomial surviving (J) has weight
(chi).

If the complement determinant were nonzero in the completed local ring,
its lowest (mathfrak m)-adic term would be a nonzero torus semi-invariant
of weight (chi) in the associated graded ring.  Inclusion (4.5) says
that every one of its monomials must survive (J), contradicting the weight
calculation.  Therefore

\[
 \det(M-L)=0                                               \tag{5.5}
\]

on the entire completed staircase germ.

## 6. Projective consequence and boundary

The rank-at-most-six pair incidence is closed, projective, and torus stable.
A connected torus preserves each irreducible component, and every projective
component contains a fixed point.  Sections 2--5 prove that every local
component through a rank-exactly-six fixed point lies in the closed
noncomplementary boundary.  Thus any complementary component must instead
specialize to one of the rank-three or rank-five fixed points in (1.2).

Replay the expensive certificate explicitly:

```text
python scripts/n6_product_34_rank_six_fixed_reduction.py \
  --verify-json data/n6_product_34_rank_six_fixed_reduction.json
python -m unittest tests.test_n6_product_34_rank_six_fixed_reduction -v
```

The larger rank-at-most-six normal cones over the rank-three and rank-five
fixed strata remain open.  Consequently this note does not yet exclude all
twelve-dimensional (3\times4/4\times3) sections, the full
(kappa _2=0) branches, ordinary lower 29, exact unrestricted rank 32, or
border rank.
