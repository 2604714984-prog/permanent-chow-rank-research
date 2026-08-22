# N6-114: the rank-five \(3\times4\) normal strata are noncomplementary

## 1. Statement and scope

Let

\[
 V=A_3\otimes B_4,
 \qquad
 E_{34}=S_0(A_3)\otimes S_0(B_4)\subset \operatorname{Sym}^2V,
\]

and write \(\beta_{34}(L,M)\) for the image of the cross-evaluation map
on two six-planes \(L,M\subset V\).  Consider the projective determinantal
locus

\[
 Z_6=\{(L,M):\dim\beta_{34}(L,M)\le 6\}
 \subset \operatorname{Gr}(6,V)^2.
\]

N6-113 proved that a component of \(Z_6\) whose general point is
complementary can specialize only to a coordinate fixed point of cross rank
three or five.  N6-114 proves:

> **Theorem.** No component of \(Z_6\) whose general point satisfies
> \(L\oplus M=V\) can specialize to either rank-five coordinate orbit.

The transpose gives the identical statement in \(A_4\otimes B_3\).  Thus the
only product fixed strata still open after N6-113 and N6-114 are the rank-three
\(K_{2,3}\) and \(K_{3,2}\) strata.

This is not yet an exclusion of the full twelve-dimensional product equality
case and is not a proof of ordinary lower 29, exact unrestricted rank 32, or
border rank.

## 2. The two rank-five fixed orbits

Use coordinates \(0,\ldots,11\), with coordinate \(4i+c\) denoting
\(a_i\otimes b_c\).  N6-108 found exactly two rank-five coordinate orbits:

\[
\begin{aligned}
 \mathrm{R}_{42}&:\quad
 L_0=M_0=\langle e_0,e_1,e_2,e_3,e_4,e_5\rangle,\\
 \mathrm{R}_{33}&:\quad
 L_0=\langle e_0,e_1,e_2,e_4,e_5,e_7\rangle,\qquad
 M_0=\langle e_0,e_1,e_3,e_4,e_5,e_6\rangle.
\end{aligned}
\]

Both lie in the coordinate eight-space formed by rows zero and one.  The 48
normal graph variables have targets in row two.  Since \(E_{34}\) contains no
same-row quadratic, a product of two row-two normal contributions vanishes in
the cross matrix.  Consequently the third-row block is *exactly linear* in
the normal variables.  Scaling row two gives the normal homogeneity used in
Section 5 below; there is no hidden quadratic normal correction.

At a rank-five point the first normal Schur map is a linear map

\[
 N\longrightarrow \operatorname{Mat}_{31\times13}.
\]

The exceptional normal condition for \(Z_6\) is that its image have rank at
most one.

## 3. Exact torus-fixed normal directions

The normal variables split into row-column torus weight spaces.  Their largest
dimension is eight.  For every weight space, the replay streams all
\(2\times2\) minors of the corresponding \(31\times13\) matrix and retains
only an exact rational row basis of their quadratic coefficient span.  At
most

\[
 \binom{8+1}{2}=36
\]

rows are retained.  There is no enumeration of subsets and no growing set or
dictionary.

If the exact minor span contains \(x_i^2\) for every coefficient variable,
then its projective zero locus is empty over every characteristic-zero
algebraically closed field.  This eliminates 19 of the 20 normal weight
spaces at \(\mathrm R_{42}\), and 24 of the 26 normal weight spaces at
\(\mathrm R_{33}\).

### 3.1 The \(\mathrm R_{42}\) exceptional weight

The only surviving weight space has variables

\[
 (x_0,x_1,x_2,x_3)=
 (L_{8\leftarrow4},L_{9\leftarrow5},
   M_{8\leftarrow4},M_{9\leftarrow5}).
\]

The exact quadratic span has rank eight in the ten-dimensional space of
quadrics.  Its reduced row echelon equations are frozen in the JSON.  They
include

\[
 x_0^2=x_3^2,quad x_0x_2=x_3^2,quad x_2^2=x_3^2,
 \quad x_1x_3=x_3^2,
\]

together with the four compatible mixed equations.  If \(x_3=0\), all four
variables vanish.  On the chart \(x_3=1\), the solutions are the two reduced
points

\[
 [1:1:1:1],qquad [1:-1:1:-1].
\]

### 3.2 The \(\mathrm R_{33}\) exceptional weights

There are two surviving six-dimensional weights, exchanged by swapping rows
zero and one and then swapping \(L,M\).  For the first one the variables are

\[
 (L_{8\leftarrow0},L_{9\leftarrow1},L_{10\leftarrow2},
   M_{8\leftarrow0},M_{9\leftarrow1},M_{11\leftarrow3}).
\]

The second is the analogous row-one-to-row-two weight.  In each case the exact
minor span has rank 20 in the 21-dimensional quadratic space.  On the last
coordinate chart its equations force the unique reduced point

\[
 [1:1:1:-1:-1:-1].
\]

Thus the complete characteristic-zero fixed set of the projectivized normal
rank-one locus consists of two points over \(\mathrm R_{42}\) and two points
over \(\mathrm R_{33}\).

## 4. Finite representatives and exact local models

Normal homogeneity lets us replace a nonzero exceptional coefficient by one.
The resulting finite pair has cross rank exactly six.  We now study the full
\(72\)-variable Grassmann graph chart at that finite pair.

For a rank-six cross matrix, put it into the exact modular normal form

\[
 \begin{pmatrix}I_6&0\\0&0\end{pmatrix}.
\]

Its Schur complement has size \(30\times12\).  A nonzero minor modulo
\(1{,}000{,}003\) supplies a characteristic-zero lower bound for the linear
rank, while the displayed integer tangent directions supply the matching
upper bound.  Therefore every tangent dimension below is an exact equality
over \(\mathbf Q\).

### 4.1 The first \(\mathrm R_{42}\) point

For \([1:-1:1:-1]\), the linear rank is 71.  The single tangent direction is
the row-scaling curve

\[
 L_s=M_s=\langle e_0,e_1,e_2,e_3,
 e_4+s e_8,e_5-s e_9\rangle.
\]

Its generic cross rank is six and its sum rank is six.  Hence the completed
local ring is \(k[[s]]\), entirely inside the diagonal.

### 4.2 The second \(\mathrm R_{42}\) point

For \([1:1:1:1]\), the linear rank is 69 and the tangent space has coordinates
\((x_0,x_1,x_2)\).  Here \(x_0\) is the normal scaling direction and
\(x_1,x_2\) are two separating directions.

After linear elimination, the six quadratic Schur columns have cokernel rank
one.  Exactly one column increases rank:

\[
 x_1x_2.
\]

There are two explicit smooth two-parameter families in \(Z_6\), tangent to
\(x_1=0\) and \(x_2=0\); they are exchanged by the local symmetry.  For one
of them, with parameters \(s,c\), the columns are

\[
\begin{aligned}
 L_{s,c}={}&\langle
 e_0+cs e_8, e_1+cs e_9, e_2-c e_6, e_3+cs e_{11},
 e_4+s e_8, e_5+s e_9\rangle,\\
 M_{s,c}={}&\langle
 e_0-cs e_8, e_1-cs e_9, e_2-cs e_{10}, e_3+c e_7,
 e_4+s e_8, e_5+s e_9\rangle.
\end{aligned}
\]

Exact symbolic row reduction over \(k(s,c)\) gives

\[
 \dim\beta_{34}(L_{s,c},M_{s,c})=6,qquad
 \dim(L_{s,c}+M_{s,c})=10.
\]

The displayed graph coordinates recover \(s,c\) themselves, so each family
is a formal closed embedding, not merely a parametrized set.

Let \(I\) be the completed local ideal after eliminating the 69 linear
variables.  The Schur calculation gives \((x_1x_2)\subset\operatorname{in}I\).
The two actual branches give

\[
 \operatorname{in}I\subset (x_1)\cap(x_2)=(x_1x_2).
\]

Thus equality holds.  The usual complete filtered lifting then gives the
scheme-theoretic union of the two smooth branches.  Both have sum rank at
most ten.

### 4.3 The \(\mathrm R_{33}\) endpoints

At the first endpoint the normal pencil direction is

\[
\begin{aligned}
 L(a,b)={}&\langle
 e_0+a e_8, e_1+a e_9, e_2+a e_{10},
 e_4+b e_8, e_5+b e_9, e_7+b e_{11}\rangle,\\
 M(a,b)={}&\langle
 e_0-a e_8, e_1-a e_9, e_3-a e_{11},
 e_4-b e_8, e_5-b e_9, e_6-b e_{10}\rangle.
\end{aligned}
\]

It has generic cross rank six and sum rank ten.  A second branch through the
same endpoint is

\[
\begin{aligned}
 L(a,c)={}&\langle
 e_0+a e_8, e_1+a e_9, e_2+a e_{10},
 e_4+ac e_8, e_5+ac e_9, e_7-c e_3\rangle,\\
 M(a,c)={}&\langle
 e_0-a e_8, e_1-a e_9, e_3-a e_{11},
 e_4+ac e_8, e_5+ac e_9, e_6+c e_2\rangle.
\end{aligned}
\]

It too has generic cross rank six and sum rank ten.  At their common endpoint
the exact linear rank is 69.  With the scaling direction first and the two
branch directions second and third, the quadratic Schur cokernel again has
rank one and the unique forbidden monomial is \(x_1x_2\).  The same initial
sandwich proves that these two smooth, formally embedded surfaces are the complete formal
germ.  The other endpoint follows by the row and \(L,M\) symmetry.

## 5. From the normal cone to components

Let \(C\) be a component of \(Z_6\) through a rank-five coordinate point, and
suppose its general point leaves the common coordinate eight-space.  Blow up
the normal ideal.  A component of the projectivized relative normal cone is a
projective torus variety, hence contains a torus fixed point.  Section 3 lists
all such points.

Because the normal directions all lie in row two and \(E_{34}\) is
squarefree in the row index, the cross matrix has no term containing two
normal contributions.  The relevant blow-up chart is therefore homogeneous
under third-row scaling.  Replacing a nonzero exceptional coefficient by one
identifies its completed branches with the finite representatives of Section
4; no higher normal term is discarded by this re-centering.

Every completed branch at every exceptional fixed point has
\(\dim(L+M)\le10\).  Thus no strict-transform component can have a
complementary general point.  Components contained in the original
eight-space are already noncomplementary.  This proves the theorem.

## 6. Reproduction and evidence labels

Run

```text
python scripts/n6_product_34_rank_five_normal_exclusion.py \
  --verify-json data/n6_product_34_rank_five_normal_exclusion.json
python -m unittest tests.test_n6_product_34_rank_five_normal_exclusion -v
```

The evidence labels are:

- the fixed-direction ideals and symbolic branch ranks are exact
  characteristic-zero computations;
- the modular ranks are used only as lower bounds, paired with explicit
  integer kernels for exact equality over \(\mathbf Q\);
- the formal-ideal conclusion is a proof from the initial sandwich and
  complete filtered lifting;
- no finite-field point count is used to assert characteristic-zero emptiness;
- the rank-three product fixed strata remain open.
