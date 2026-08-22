# N6-063: the fixed \(K_{3,4}\) rank-nine Fano scheme

## 1. Result and boundary

Let \(A=\langle e_0,e_1,e_2\rangle\),
\(B=\langle f_0,f_1,f_2,f_3\rangle\), and

\[
 V=A\otimes B,
 \qquad
 E_{34}=S_0(A)\otimes S_0(B).
\]

Here \(S_0\) denotes the zero-diagonal quadratic coordinate space.  Let
\(\beta:V\times V\to E_{34}^{*}\) be the polarized evaluation map.  This
note proves two characteristic-zero statements.

1. The six-planes \(L\subset V\) such that
   \(\operatorname{rank}\beta_x\leq9\) for every \(x\in L\) are exactly the
   eighteen coordinate rectangles

   \[
    A_I\otimes B_J,\qquad (|I|,|J|)=(2,3)\text{ or }(3,2).
   \tag{1.1}
   \]

   All eighteen points of this Fano scheme are reduced.

2. Among ordered pairs of these rectangles,

   \[
    \dim\langle\beta(L,M)\rangle\leq3
    \quad\Longleftrightarrow\quad L=M.
   \tag{1.2}
   \]

Consequently, if an **actual fixed** decomposition

\[
 V=L\oplus M,qquad \dim L=\dim M=6
\tag{1.3}
\]

has a cross-free kernel

\[
 D=\{q\in E_{34}:q(L,M)=0\}
\tag{1.4}
\]

of dimension at least fifteen, then a contradiction follows.  Thus no such
pair exists in the fixed \(K_{3,4}\) layer.

The qualification “actual fixed” is essential.  If a general twelve-plane is
degenerated to \(A_3\otimes B_4\), two complementary six-planes can collide
in the special fiber because complementarity is open, not closed.  The
present theorem does not supply the complete-collineation or wedge data
needed to prevent that collision.  It therefore does **not** exclude the
general `b=50` endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\geq28\), or make a border
rank claim.

## 2. The Jacobian map

Write \(x_{ic}\) for the coordinate of \(x\) at \(e_i f_c\).  In the basis
indexed by \(i<j\) and \(c<d\),

\[
 \beta_x(y)_{ij;cd}
 =x_{ic}y_{jd}+x_{jd}y_{ic}
  +x_{id}y_{jc}+x_{jc}y_{id}.
\tag{2.1}
\]

Define the determinantal cone and its six-plane Fano scheme by

\[
 R_9=\{x\in V:\operatorname{rank}\beta_x\leq9\},
 \qquad
 Y=\{L\in\operatorname{Gr}(6,V):L\subset R_9\}.
\tag{2.2}
\]

The second set is a projective closed subscheme: it is the Fano scheme of
linear \(\mathbf P^5\)'s contained in the projective determinantal scheme
\(\mathbf P(R_9)\).

## 3. Classification of torus-fixed points

The row-column torus acts diagonally on the twelve distinct coordinate weight
spaces \(\langle e_i f_c\rangle\).  Formula (2.1) shows that it preserves
\(R_9\) and hence \(Y\).  A torus-fixed point of \(Y\) is therefore a
six-edge subgraph \(F\subset K_{3,4}\).

The following three subgraphs obstruct membership in \(Y\), up to row and
column permutation:

\[
\begin{aligned}
 H_1&=\{00,11,22\},\\
 H_2&=\{00,01,02,13\},\\
 H_3&=\{00,01,02,10,20\}.
\end{aligned}
\tag{3.1}
\]

At their indicator vectors, direct substitution in (2.1) gives

\[
 \operatorname{rank}\beta_{1_{H_1}}=12,
 \qquad
 \operatorname{rank}\beta_{1_{H_2}}=10,
 \qquad
 \operatorname{rank}\beta_{1_{H_3}}=10.
\tag{3.2}
\]

For a short exact check, the last two kernels are respectively

\[
\begin{aligned}
 \ker\beta_{1_{H_2}}
 &=\langle e_0f_3,
 e_0f_0+e_0f_1+e_0f_2-e_1f_3\rangle,\\
 \ker\beta_{1_{H_3}}
 &=\langle e_0f_0,
 e_0f_1+e_0f_2-e_1f_0-e_2f_0\rangle,
\end{aligned}
\tag{3.3}
\]

while the first kernel is zero.  Thus these are characteristic-zero rank
identities, not finite-field evidence.

Now suppose that a six-edge \(F\) contains none of (3.1).  Avoiding \(H_1\)
means that its matching number is at most two.  By König's theorem, it has a
two-vertex cover.  One vertex cannot cover six edges.

* If two rows cover \(F\), their degree profile is either \((4,2)\) or
  \((3,3)\).  The first contains \(H_2\).  In the second, unequal
  neighborhoods contain \(H_2\), while equal neighborhoods give
  \(K_{2,3}\).
* If a row and a column cover \(F\), six edges force the union of both
  complete stars, which contains \(H_3\).
* If two columns cover \(F\), six edges force \(K_{3,2}\).

Conversely, every vector supported on \(K_{2,3}\) has \(\beta\)-rank at most
nine.  For inputs in the two selected rows, the internal three-column output
has dimension at most three and output involving the missing column has
dimension at most two.  Inputs in the missing row contribute at most four
more dimensions, for a total of nine.  For \(K_{3,2}\), inputs in the two
selected columns contribute at most three, and each missing column contributes
at most three, again totaling nine.  Hence the torus-fixed points of \(Y\)
are exactly the twelve \(K_{2,3}\)'s and six \(K_{3,2}\)'s.

## 4. The eighteen fixed points are isolated and reduced

For a coordinate rectangle \(L_0\), a Grassmann tangent vector is

\[
 T\in\operatorname{Hom}(L_0,V/L_0).
\]

If \(x\in L_0\) has \(\operatorname{rank}\beta_x=9\), then tangency to
\(Y\) requires

\[
 \ell\,\beta_{Tx}k=0
 \quad
 (k\in\ker\beta_x,\ \ell\in\ker\beta_x^{\mathsf T}).
\tag{4.1}
\]

This is the standard first-order equation for the rank-nine determinantal
locus.  We now kill the Grassmann tangent weight by weight.  Coordinates below
are ordered

\[
 00,01,02,03,10,11,12,13,20,21,22,23.
\tag{4.2}
\]

### 4.1 A \(2\times3\) rectangle

Take

\[
 L_0=\langle00,01,02,10,11,12\rangle.
\]

The only tangent weight spaces of dimension greater than one are

\[
\begin{aligned}
 X_c&=\langle T_{03\leftarrow0c},T_{13\leftarrow1c}\rangle
 &&(c=0,1,2),\\
 Z_i&=\langle T_{20\leftarrow i0},T_{21\leftarrow i1},
               T_{22\leftarrow i2}\rangle
 &&(i=0,1).
\end{aligned}
\tag{4.3}
\]

There are twenty-four remaining singleton weights.  The stabilizer of the
rectangle reduces them to three orbits.

For \(X_0\), two rank-nine points and kernel/cokernel pairs give the coefficient
rows \((2,0)\) and \((0,2)\):

\[
\begin{array}{c|c|c}
x&k&\ell\\ \hline
00+01+12&10-11&z_{01;03}^{*}-z_{01;13}^{*}\\
01+10+12&00-02&z_{01;03}^{*}-z_{01;23}^{*}.
\end{array}
\tag{4.4}
\]

For \(Z_0\), the following witnesses give

\[
 \begin{pmatrix}1&-1&0\\2&2&0\\1&0&-1\end{pmatrix},
 \qquad \det=-4:
\tag{4.5}
\]

\[
\begin{array}{c|c|c}
x&k&\ell\\ \hline
00+01+12&02&z_{02;02}^{*}-z_{02;12}^{*}\\
00+01+12&00+01-12&z_{02;01}^{*}-z_{12;02}^{*}-z_{12;12}^{*}\\
00+02+11&01&z_{02;01}^{*}-z_{02;12}^{*}.
\end{array}
\tag{4.6}
\]

Representatives of the three singleton orbits have nonzero pairings:

\[
\begin{array}{c|c|c|c|c}
T&x&k&\ell&\ell\beta_{Tx}k\\ \hline
T_{03\leftarrow10}&01+02+10&11-12&z_{01;13}^{*}-z_{01;23}^{*}&2\\
T_{20\leftarrow01}&01+12&02&z_{02;02}^{*}&1\\
T_{23\leftarrow00}&00+11&01&z_{02;13}^{*}&1.
\end{array}
\tag{4.7}
\]

All ranks, kernels, cokernels and pairings in (4.4)--(4.7) follow by direct
substitution in (2.1).  Thus the tangent space is zero at every
\(K_{2,3}\) point.

### 4.2 A \(3\times2\) rectangle

Take

\[
 L_0=\langle00,01,10,11,20,21\rangle.
\]

Its only multiple tangent weights are the four spaces

\[
 Z_{d,c}=\langle T_{0d\leftarrow0c},T_{1d\leftarrow1c},
                 T_{2d\leftarrow2c}\rangle,
 \qquad d=2,3,\quad c=0,1.
\tag{4.8}
\]

The other twenty-four weights form one stabilizer orbit.  For \(Z_{2,0}\),
the following three witnesses give

\[
 \begin{pmatrix}-1&1&0\\2&2&0\\-1&0&1\end{pmatrix},
 \qquad \det=-4:
\tag{4.9}
\]

\[
\begin{array}{c|c|c}
x&k&\ell\\ \hline
00+10+21&01-11&z_{01;12}^{*}\\
00+10+21&00+10-21&z_{01;02}^{*}-z_{02;12}^{*}-z_{12;12}^{*}\\
00+11+20&01-21&z_{02;12}^{*}.
\end{array}
\tag{4.10}
\]

The singleton representative

\[
 T_{02\leftarrow10},\qquad
 x=10+21,\quad k=11,\quad \ell=z_{01;12}^{*}
\]

has pairing one.  Hence the tangent space is also zero at every
\(K_{3,2}\) point.

### 4.3 Globalization

Each irreducible component of the projective torus-stable scheme \(Y\) is
torus-stable because the torus is connected, and every such projective
component contains a torus-fixed point.  Its local dimension at that fixed
point is bounded by the zero-dimensional Zariski tangent space just computed.
Thus every component is zero-dimensional.  A connected torus orbit in a
zero-dimensional scheme is a point, so every point of \(Y\) is fixed.  The
zero tangent spaces also rule out nilpotent thickening.  Therefore

\[
 \boxed{Y=\{12\text{ coordinate }K_{2,3}\text{'s},
              6\text{ coordinate }K_{3,2}\text{'s}\}}
\tag{4.11}
\]

as a reduced scheme.

## 5. Cross-free pair incidence

For two coordinate rectangles, the vectors \(\beta(e_if_c,e_jf_d)\) with
\(i\ne j\), \(c\ne d\) are distinct coordinate vectors of \(E_{34}^{*}\).
Counting these coordinates over all \(18^2=324\) ordered pairs gives

\[
\begin{array}{c|rrrrrr}
\dim\langle\beta(L,M)\rangle&3&6&9&12&15&18\\ \hline
\#(L,M)&18&36&120&6&72&72.
\end{array}
\tag{5.1}
\]

The eighteen pairs in the first column are exactly the diagonal pairs
\(L=M\).  This establishes (1.2).

Now suppose (1.3)--(1.4) hold and \(\dim D\geq15\).  Put

\[
 W=\langle\beta(L,M)\rangle.
\]

Annihilator duality gives \(\dim W\leq18-15=3\).  For \(l\in L\),

\[
 \operatorname{im}\beta_l
 \subseteq \beta(l,L)+W,
 \qquad
 \operatorname{rank}\beta_l\leq6+3=9.
\tag{5.2}
\]

Thus \(L\in Y\), and likewise \(M\in Y\).  Equation (1.2) forces \(L=M\),
contradicting \(V=L\oplus M\).  This proves the fixed-layer exclusion.

## 6. Exact replay

Run

~~~text
python scripts/n6_k34_rank_nine_fano_exclusion.py \
  --verify-json data/n6_k34_rank_nine_fano_exclusion.json
python -m unittest tests/test_n6_k34_rank_nine_fano_exclusion.py -v
~~~

The replay checks all \(924\) coordinate six-plane supports, all displayed
tangent witnesses, and all \(324\) rectangle pairs.  Modular ranks certify
characteristic-zero lower bounds because reduction modulo a prime cannot
increase rank.  The promotion from fixed points to arbitrary points of \(Y\)
is the pure projective argument in Sections 3--4, not an enumeration.
