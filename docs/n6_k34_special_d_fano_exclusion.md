# N6-066: a special \(K_{3,4}\) fifteen-plane exclusion

**Status.** `PURE_SPECIAL_D_FANO_EXCLUSION`,
`EXACT_MODULAR_TANGENT_CERTIFICATE` (N6-066).  The base field is
algebraically closed of characteristic zero.

## 1. Statement

Let \(A=\langle e_0,e_1,e_2\rangle\),
\(B=\langle f_0,f_1,f_2,f_3\rangle\), and \(V=A\otimes B\).  Delete the
coordinate column pair \(01\) from the eighteen-dimensional rectangle
space and put

\[
 D=S_0(A)\otimes
 \langle f_cf_d:c<d,\ (c,d)\ne(0,1)\rangle,
 \qquad \dim D=15.
\tag{1.1}
\]

For \(x\in V\), let

\[
 \beta_x^D:V\longrightarrow D^*,
 \qquad y\longmapsto(q\mapsto q(x,y)).
\tag{1.2}
\]

### Theorem 1.1

The Fano scheme

\[
 Y_D=\{L\in\operatorname{Gr}(6,V):
 \operatorname{rank}\beta_x^D\le6\text{ for every }x\in L\}
\tag{1.3}
\]

is the single reduced point

\[
 \boxed{L_0=A\otimes\langle f_0,f_1\rangle.}
\tag{1.4}
\]

Consequently there are no complementary six-planes \(V=L\oplus M\) for
which every quadratic in \(D\) vanishes on \(L\times M\).  The same theorem
holds after row-column transposition and coordinate permutations.

## 2. Torus-fixed points

The row-column torus preserves \(D\) and \(Y_D\).  A fixed point is a
six-edge coordinate support in the \(3\times4\) grid.  If such a support
lies in \(Y_D\), the sum of every two coordinate vectors has
\(\beta^D\)-rank at most six.  Exact integer matrices give

\[
\begin{array}{c|rrrr}
\operatorname{rank}\beta^D_{u+v}&4&6&8&9\\ \hline
\#\{u,v\}&9&27&24&6.
\end{array}
\tag{2.1}
\]

Regard the thirty rank-eight or rank-nine pairs as forbidden edges.  The
maximal independent sets are the three complete rows of size four, the two
complete columns \(2,3\) of size three, and the single six-set
\(A\times\{0,1\}\).  Thus (1.4) is the only six-point fixed candidate.

Conversely, for \(x\in L_0\), the map \(\beta_x^D\) is supported on at most
the six complementary domain coordinates
\(A\otimes\langle f_2,f_3\rangle\), so its rank is at most six.  Hence
\(L_0\in Y_D\).

## 3. The fixed point is reduced

A Grassmann tangent vector at \(L_0\) lies in

\[
 \operatorname{Hom}(L_0,V/L_0),\qquad \dim=36.
\tag{3.1}
\]

At a rank-six point \(x\in L_0\), tangency requires

\[
 \ell\,\beta^D_{Tx}k=0
 \quad
 (k\in\ker\beta_x^D,\ \ell\in\ker(\beta_x^D)^{\mathsf T}).
\tag{3.2}
\]

In coordinates \(00,01,10,11,20,21\), use

\[
 000110,\quad000111,\quad001001,\quad
 001011,\quad010010,\quad100001.
\tag{3.3}
\]

All six points have rank six.  Stacking (3.2) makes the tangent-equation
rank grow as

\[
 6,12,18,24,30,36.
\tag{3.4}
\]

The integral coefficient matrix has rank 36 modulo \(1000003\).  Its
nonzero modular \(36\times36\) minor proves rank at least 36 in
characteristic zero, so the Zariski tangent space is zero.

Every irreducible component of the projective torus-stable scheme \(Y_D\)
contains a fixed point.  Section 2 gives only \(L_0\), and the zero tangent
space shows it is isolated and reduced.  Hence \(Y_D=\{L_0\}\).

## 4. Complementary pairs

Suppose \(V=L\oplus M\) and \(q(L,M)=0\) for every \(q\in D\).  For
\(l\in L\), the map \(\beta_l^D\) vanishes on \(M\), so its rank is at most
six.  Thus \(L\in Y_D\), and likewise \(M\in Y_D\).  The theorem forces
\(L=M=L_0\), contradicting complementarity.

## 5. Boundary and replay

This theorem excludes only the special vertical orbit obtained from a fixed
\(K_{3,4}\) rectangle space by deleting all three rectangles over one column
pair.  It does not classify the other vertical orbits, exclude the full
\(b=50\) endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a
border-rank claim.

```text
python scripts/n6_k34_special_d_fano_exclusion.py \
  --verify-json data/n6_k34_special_d_fano_exclusion.json
python -m unittest tests.test_n6_k34_special_d_fano_exclusion -v
```
