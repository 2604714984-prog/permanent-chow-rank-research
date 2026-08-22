# N6-069: common-row-block rigidity for an actual pair

**Status.** `PURE_COMMON_ROW_BLOCK_RIGIDITY`,
`EXACT_QQ_LINEAR_ALGEBRA_REGRESSION`, `B50_INVERTIBLE_BLOCK_EXCLUDED`,
`N6-069`.  The base field is algebraically closed of characteristic zero.

## 1. Statement

Put \(R=C=k^6\), \(V=R\otimes C\), and let

\[
 S_0(C)=\langle f_cf_d:c<d\rangle\subset\operatorname{Sym}^2C.
\]

As in N6-061,

\[
 E_2=S_0(R)\otimes S_0(C)\subset\operatorname{Sym}^2V.
\tag{1.1}
\]

Let \(X,Y:k^6\to V\) be injective factor matrices for two actual
six-factor Chow terms, and write their row blocks as

\[
 X_r,Y_r\in\operatorname{Mat}_{6\times6}(k),\qquad 0\le r<6.
\tag{1.2}
\]

Their quadratic derivative spaces are

\[
 F_X=\{XZX^{\mathsf T}:Z\in S_0(C)\},\qquad
 F_Y=\{YZY^{\mathsf T}:Z\in S_0(C)\}.
\tag{1.3}
\]

Assume

\[
 F_X\cap E_2=F_Y\cap E_2=0,
 \qquad q(F_X)=q(F_Y)=W,
 \qquad \dim W=15,
\tag{1.4}
\]

where \(q:\operatorname{Sym}^2V\to\operatorname{Sym}^2V/E_2\), and
assume that the factor spans \(L=\operatorname{im}X\) and
\(M=\operatorname{im}Y\) are complementary.

### Theorem 1.1

If one row block \(X_r\) or \(Y_r\) is invertible, then there are independent
vectors \(p,q\in R\) and one monomial matrix \(H\in\operatorname{GL}(C)\)
such that, after independent permutations and rescalings of the two factor
frames,

\[
 X_s=p_sH,\qquad Y_s=q_sH\qquad(0\le s<6).
\tag{1.5}
\]

Consequently

\[
 L=p\otimes C,\qquad M=q\otimes C,
\tag{1.6}
\]

and the two actual frames are separated by the same six coordinate columns.
The transposed theorem holds for column blocks and common row separation.

At the \(b=50\) endpoint, one such pair propagates column separation (or,
after transposition, row separation) to all six selected terms exactly as in
N6-061, Section 4.  N6-059 then excludes the endpoint.  Hence every pair
surviving N6-069 has all twelve row blocks and, after transposition, all
twelve column blocks singular.

## 2. The common section-difference map

Both restrictions \(q|_{F_X}\) and \(q|_{F_Y}\) are isomorphisms onto \(W\).
There is therefore a unique

\[
 \phi\in\operatorname{GL}(S_0(C))
\]

such that

\[
 Q(Z)=XZX^{\mathsf T}-Y\phi(Z)Y^{\mathsf T}\in E_2
 \qquad(Z\in S_0(C)).
\tag{2.1}
\]

The space \(D=\{Q(Z):Z\in S_0(C)\}\) is the literal
fifteen-dimensional section-difference graph.  Formula (1.1) says that its
same-row blocks vanish and its distinct-row blocks lie in \(S_0(C)\).

Suppose \(X_0\) is invertible.  Choose an invertible \(Z\in S_0(C)\), for
example the adjacency matrix of three disjoint edges.  The \(00\)-block of
(2.1) is

\[
 X_0ZX_0^{\mathsf T}=Y_0\phi(Z)Y_0^{\mathsf T}.
\tag{2.2}
\]

Its left side has rank six, so \(Y_0\) is invertible.  The same argument with
\(X,Y\) exchanged handles the hypothesis that \(Y_0\) is invertible.

Equation (2.2), now for every \(Z\in S_0(C)\), gives

\[
 \phi(Z)=PZP^{\mathsf T},\qquad P=Y_0^{-1}X_0,
\tag{2.3}
\]

and hence \(P S_0(C)P^{\mathsf T}=S_0(C)\).

### Lemma 2.1 -- the congruence normalizer

If \(P\in\operatorname{GL}(C)\) satisfies

\[
 P S_0(C)P^{\mathsf T}=S_0(C),
\]

then \(P\) is monomial.

Indeed, the annihilator of \(S_0(C)\) is the diagonal six-plane in
\(\operatorname{Sym}^2C^*\).  Its projective rank-one locus consists of
exactly the six coordinate squares.  The dual congruence induced by \(P\)
must permute these six points, which is precisely the monomial condition.

Replacing \(Y\) by \(YP\) only permutes and rescales its six factors.  Thus
we may assume

\[
 \phi=1,\qquad X_0=Y_0=:H.
\tag{2.4}
\]

## 3. All row blocks are scalar multiples of one matrix

Put

\[
 \Delta_s=X_s-Y_s.
\]

The \(0s\)-block of (2.1) is exactly

\[
 HZX_s^{\mathsf T}-HZY_s^{\mathsf T}
   =HZ\Delta_s^{\mathsf T}.
\tag{3.1}
\]

There is no omitted second summand: the \(s0\)-block is the transpose of
(3.1).  Since (3.1) belongs to \(S_0(C)\), it is symmetric.  Multiplication
on the left by \(H^{-1}\) and on the right by \(H^{-\mathsf T}\) gives

\[
 T_sZ=ZT_s^{\mathsf T},\qquad T_s=H^{-1}\Delta_s.
\tag{3.2}
\]

### Lemma 3.1

For \(n\ge3\), if \(TZ=ZT^{\mathsf T}\) for every
\(Z\in S_0(k^n)\), then \(T=dI\).

Take \(Z=F_{ij}=E_{ij}+E_{ji}\).  An entry outside rows \(i,j\), together
with column \(j\), kills every off-diagonal entry of \(T\).  The
\(ij\)-entry then gives \(T_{ii}=T_{jj}\).  Varying \(i<j\) proves the
lemma.

It follows that

\[
 \Delta_s=d_sH.
\tag{3.3}
\]

Not all \(d_s\) vanish, because otherwise \(X=Y\) and \(L=M\), contrary to
complementarity.  Fix \(t\) with \(d_t\ne0\).  The zero diagonal in (3.1)
then gives

\[
 H S_0(C)H^{\mathsf T}\subseteq S_0(C).
\]

Both spaces have dimension fifteen, so equality holds.  Lemma 2.1 makes
\(H\) monomial.  Applying the same monomial change to both factor frames
allows us to normalize

\[
 H=I,\qquad X_s-Y_s=d_sI.
\tag{3.4}
\]

If \(d_s\ne0\), the vanishing \(ss\)-block of (2.1) becomes

\[
 (Y_s+d_sI)Z(Y_s+d_sI)^{\mathsf T}-Y_sZY_s^{\mathsf T}=0.
\]

Equivalently,

\[
 R_sZ+ZR_s^{\mathsf T}=0,
 \qquad R_s=Y_s+\frac{d_s}{2}I.
\tag{3.5}
\]

### Lemma 3.2

For \(n\ge3\) in characteristic different from two, if
\(RZ+ZR^{\mathsf T}=0\) for every \(Z\in S_0(k^n)\), then \(R=0\).

Again use \(F_{ij}\).  Entries outside the selected rows kill the
off-diagonal entries of \(R\).  The \(ij\)-entry gives
\(R_{ii}+R_{jj}=0\); three distinct indices and characteristic different
from two kill every diagonal entry.

Thus, whenever \(d_s\ne0\),

\[
 X_s=\frac{d_s}{2}I,\qquad Y_s=-\frac{d_s}{2}I.
\tag{3.6}
\]

If \(d_s=0\), write \(X_s=Y_s=C_s\).  Use the fixed \(t\) from above in
the \(st\)-block.  Formula (3.6) gives

\[
 X_sZX_t^{\mathsf T}-Y_sZY_t^{\mathsf T}=d_tC_sZ\in S_0(C).
\tag{3.7}
\]

N6-061, Lemma 2.2 says that \(C_sZ\in S_0(C)\) for all
\(Z\in S_0(C)\) forces \(C_s\) to be scalar.  Equations (3.6)--(3.7)
prove that every row block of both \(X\) and \(Y\) is scalar.  Undoing the
normalization \(H=I\)
gives (1.5).

Finally, complementarity makes \(p,q\) independent.  Some two-by-two row
minor of the matrix \((p,q)\) is nonzero, so
\(L\oplus M=(\langle p,q\rangle)\otimes C\)
projects isomorphically to the corresponding two complete rows.  This is
consistent with, and strengthens the entry condition used in, N6-061.

## 4. Endpoint consequence and boundary

At the all-alpha-three \(b=50\) endpoint, all six actual quadratic spaces
have the same quotient \(W_{15}\).  If one pair satisfies Theorem 1.1, its
common coordinate-column separation makes \(q^{-1}(W)=E_2+F\) contain no
same-column product.  The domain argument in N6-061, Section 4 then forces
each of the other four actual terms to be column-separated.  N6-059 bounds
the resulting cubic permanent intersection by forty, contradicting
\(b=50\).  The transposed argument handles a column block.

Therefore a surviving endpoint must satisfy

\[
 \det X_{i,r}=0
 \quad\text{for all six terms }i\text{ and all six rows }r,
\]

and the analogous thirty-six determinant equations for column blocks.

This theorem does not exclude that all-singular block layer.  It does not
prove \(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), and it makes
no border-rank claim.  The exact replay below checks only the three elementary
matrix lemmas and one monomial-normalizer sample; the theorem itself is the
characteristic-zero proof above.

## 5. Exact replay

```text
python scripts/n6_common_row_block_rigidity.py \
  --verify-json data/n6_common_row_block_rigidity.json
python -m unittest tests.test_n6_common_row_block_rigidity -v
```
