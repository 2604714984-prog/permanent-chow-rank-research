# Two-row and two-column transverse rigidity

**Status.** PURE_TRANSVERSE_PAIR_RIGIDITY_THEOREM,
EXACT_QQ_LINEAR_ALGEBRA_REGRESSION, B50_TRANSVERSE_PAIR_EXCLUDED, N6-061.
The base field is
algebraically closed of characteristic zero.  The theorem classifies a
fifteen-dimensional section-difference space when its twelve-dimensional
linear shadow is transverse to two complete rows, or after transposition to
two complete columns.  The proof is purely mathematical.  The accompanying
script checks only small linear-algebra constants and is not a substitute for
the proof.

## 1. Quadratic permanent space and map conventions

Let \(R=C=k^6\), with bases \(e_0,\ldots,e_5\) and
\(f_0,\ldots,f_5\), and put \(V=R\otimes C\).  We identify a quadratic
tensor \(q\in\operatorname{Sym}^2V\) with its symmetric contraction map

\[
 q:V^*\longrightarrow V.
\tag{1.1}
\]

For \(D\subset\operatorname{Sym}^2V\), its derivative shadow is

\[
 \partial D=\sum_{q\in D}\operatorname{im}(q).
\tag{1.2}
\]

Let

\[
 S_0(C)=\langle f_cf_d:0\le c<d<6\rangle
       \subset\operatorname{Sym}^2C.
\tag{1.3}
\]

Thus \(S_0(C)\) is the fifteen-dimensional space of symmetric
zero-diagonal \(6\times6\) matrices.  In row-major block notation, the
quadratic permanent derivative space
\(E_2=\mathcal D_4(\operatorname{perm}_6)\) consists precisely of
symmetric block matrices \(Q=(Q_{rs})\) satisfying

\[
 Q_{rr}=0,\qquad
 Q_{rs}=Q_{sr}\in S_0(C)\quad(r\ne s).
\tag{1.4}
\]

Equivalently,

\[
 E_2=S_0(R)\otimes S_0(C)
\tag{1.5}
\]

under the natural Cauchy embedding into
\(\operatorname{Sym}^2(R\otimes C)\).  Harmless factors of two depend on
the symmetric-tensor convention and play no role below.

## 2. The transverse shadow theorem

### Theorem 2.1

Let

\[
 D\subset E_2,\qquad \dim D=15,\qquad
 U=\partial D,\qquad \dim U=12.
\tag{2.1}
\]

Suppose the coordinate projection

\[
 \pi_{01}:U\longrightarrow(ke_0\oplus ke_1)\otimes C
\tag{2.2}
\]

is an isomorphism.  Then there are scalars \(a_r,b_r\), \(2\le r<6\),
such that \(a_rb_r=0\), and, with

\[
 u=e_0+\sum_{r=2}^5a_re_r,\qquad
 v=e_1+\sum_{r=2}^5b_re_r,
\tag{2.3}
\]

one has

\[
 \boxed{
 U=\langle u,v\rangle\otimes C,\qquad
 D=(uv+vu)\otimes S_0(C).
 }
\tag{2.4}
\]

The same statement holds for any pair of rows.  Transposition gives the
corresponding statement for any pair of columns.

### Proof

Use (2.2) to write \(U\) as the graph of

\[
 J:C\oplus C\longrightarrow V,
\tag{2.5}
\]

\[
 J(x,y)=e_0\otimes x+e_1\otimes y
 +\sum_{r=2}^5e_r\otimes(X_rx+Y_ry).
\tag{2.6}
\]

Its row blocks are

\[
 J_0=[I,0],\qquad J_1=[0,I],\qquad J_r=[X_r,Y_r].
\tag{2.7}
\]

Let \(P:V\to C\oplus C\) be the top two-row projection.  Then \(PJ=I\),
and \(JP\) is the identity on \(U\).  If \(Q\in D\), then
\(\operatorname{im}Q\subset U\), so \(Q=JPQ\).  Since
\(Q=Q^{\mathsf T}\), transposition gives
\(Q=QP^{\mathsf T}J^{\mathsf T}\).  Consequently

\[
 Q=J(PQP^{\mathsf T})J^{\mathsf T}=:JSJ^{\mathsf T}.
\tag{2.8}
\]

By (1.4), its top block is

\[
 S=\begin{pmatrix}0&B\\ B&0\end{pmatrix},
 \qquad B\in S_0(C).
\tag{2.9}
\]

The map \(D\to S_0(C)\), \(Q\mapsto B\), is injective: \(B=0\)
implies \(S=0\), hence \(Q=0\) by (2.8).  Both spaces have dimension
fifteen, so \(B\) ranges over all of \(S_0(C)\).

For \(r\ge2\), (2.8)--(2.9) give

\[
 Q_{r0}=Y_rB,\qquad Q_{r1}=X_rB.
\tag{2.10}
\]

Both matrices belong to \(S_0(C)\) for every \(B\in S_0(C)\).

### Lemma 2.2

If \(X\in\operatorname{End}(C)\) and

\[
 XB\in S_0(C)\quad\text{for every }B\in S_0(C),
\tag{2.11}
\]

then \(X=\lambda I\).

### Proof

Put \(F_{ij}=E_{ij}+E_{ji}\).  The zero diagonal of \(XF_{ij}\), at
positions \(i\) and \(j\), gives \(X_{ij}=X_{ji}=0\).  Hence \(X\) is
diagonal.  Symmetry of \(XF_{ij}\) then gives \(X_{ii}=X_{jj}\).
Varying \(i<j\) proves the claim. \(\square\)

Lemma 2.2 gives \(X_r=a_rI\) and \(Y_r=b_rI\).  The \(r\)-th diagonal
row block of (2.8) is

\[
 Q_{rr}=X_rBY_r^{\mathsf T}+Y_rBX_r^{\mathsf T}
       =2a_rb_rB.
\tag{2.12}
\]

It must vanish for every \(B\), so \(a_rb_r=0\).  Equations
(2.6) and (2.8) now give (2.3)--(2.4). \(\square\)

## 3. Actual Chow section differences

Let \(L,M\subset U\) be complementary six-planes.  Suppose

\[
 F_L=\langle\ell_a\ell_b:a<b\rangle\subset\operatorname{Sym}^2L,
 \qquad
 F_M=\langle m_am_b:a<b\rangle\subset\operatorname{Sym}^2M,
\tag{3.1}
\]

where each displayed six-tuple is a basis.  Assume that \(D\) is an actual
section-difference graph: its projections to \(F_L\) and \(F_M\) are
isomorphisms.  In particular,

\[
 D\subset\operatorname{Sym}^2L\oplus\operatorname{Sym}^2M.
\tag{3.2}
\]

Equation (3.2) means simultaneous block decomposition of quadratic tensors
relative to \(U=L\oplus M\).  It does **not** invoke an ambient Euclidean
inner product.

### Theorem 3.1

Under Theorem 2.1 and (3.1)--(3.2), there are lines
\(kp,kq\subset\langle u,v\rangle\) such that

\[
 L=p\otimes C,\qquad M=q\otimes C,
\tag{3.3}
\]

and both factor frames are coordinate bases of \(C\), up to permutation
and nonzero rescaling.  Thus the two Chow terms are separated by the same
six columns.  After transposition, full projection to two columns forces
common row separation.

### A common nondegenerate member

Every full-frame squarefree space contains a nondegenerate quadratic tensor:
in its frame basis use

\[
 \ell_0\ell_1+\ell_2\ell_3+\ell_4\ell_5.
\tag{3.4}
\]

Therefore the two determinant polynomials on \(D\), obtained from its
blocks in \(\operatorname{Sym}^2L\) and \(\operatorname{Sym}^2M\), are
both nonzero.  Since \(k\) is infinite, their nonvanishing open subsets
intersect.  Choose

\[
 q_0=A\otimes B_0\in D,\qquad A=uv+vu,
\tag{3.5}
\]

whose two blocks are both nondegenerate.  Then \(q_0:U^*\to U\) is
invertible, and \(B_0\in S_0(C)\) is invertible.  No prescribed matching
matrix is substituted for this \(B_0\).

For \(B\in S_0(C)\), put \(q_B=A\otimes B\).  Since \(q_B\) and \(q_0\)
are block diagonal in (3.2), the endomorphism

\[
 T_B=q_Bq_0^{-1}
     =I_{\langle u,v\rangle}\otimes BB_0^{-1}
\tag{3.6}
\]

preserves \(L\) and \(M\).  The order in (3.6) follows from the convention
\(q:U^*\to U\).

### Lemma 3.2: the general \(B_0\) algebra

For every invertible \(B_0\in S_0(C)\),

\[
 \operatorname{Alg}\{BB_0^{-1}:B\in S_0(C)\}
 =\operatorname{End}(C).
\tag{3.7}
\]

### Proof

We prove irreducibility directly.  If a nonzero proper \(H\subset C\)
were invariant, put \(Z=B_0^{-1}H\).  Then

\[
 \dim Z=\dim H,\qquad S_0(C)Z\subset H.
\tag{3.8}
\]

For \(0\ne z\in C\), direct evaluation gives

\[
 (S_0(C)z)^\perp
 =\{y:y_i z_j+y_j z_i=0\text{ for all }i<j\}.
\tag{3.9}
\]

If \(z\) has at least three nonzero coordinates, three equations in (3.9),
using characteristic different from two, kill the corresponding coordinates
of \(y\), and the remaining equations kill all others.  Thus
\(S_0(C)z=C\), contradicting properness of \(H\).

It follows that every vector of \(Z\) has support at most two.  Over an
infinite field, a linear subspace all of whose vectors have support at most
two is contained in one coordinate two-plane: otherwise a generic linear
combination of two vectors has support at least three.  Hence
\(\dim H=\dim Z\le2\).  On the other hand, for every nonzero \(z\) of
support one or two, (3.9) is one-dimensional, so

\[
 \dim S_0(C)z=5.
\tag{3.10}
\]

Equations (3.8) and (3.10) give \(5\le\dim H\), a contradiction.
The algebra in (3.7) is irreducible.  Burnside's theorem over the
algebraically closed field \(k\) proves (3.7). \(\square\)

The direct irreducibility argument is essential.  Merely computing a scalar
commutant would not suffice for a possibly nonsemisimple algebra.

### Completion of Theorem 3.1

By (3.6)--(3.7), \(L\) and \(M\) are submodules for
\(I\otimes\operatorname{End}(C)\).  Matrix units show that every such
submodule is \(P'\otimes C\): applying \(I\otimes E_{ij}\) isolates and
then propagates each \(C\)-coordinate.  Since both spaces have dimension
six, \(P'\) is a line.  This proves (3.3).

Write

\[
 A=\alpha p^2+\gamma pq+\beta q^2.
\tag{3.11}
\]

Condition (3.2) forces \(\gamma=0\), while
\(\operatorname{rank}A=2\) gives \(\alpha\beta\ne0\).  The projection
of \(D\) to \(\operatorname{Sym}^2L\) is therefore

\[
 \alpha p^2\otimes S_0(C)=F_L.
\tag{3.12}
\]

Write \(\ell_a=p\otimes c_a\).  Then the \(c_a\) form a basis of \(C\),
and (3.12) says

\[
 \langle c_ac_b:a<b\rangle=S_0(C).
\tag{3.13}
\]

Under the perfect pairing with \(\operatorname{Sym}^2C^*\), the
annihilator of the left side is spanned by the six squares of the dual
frame, while the annihilator of the right side is spanned by the six
coordinate squares.  The rank-one locus in a diagonal six-plane consists
exactly of its six coordinate lines.  Equality of the annihilators therefore
recovers the six dual-frame lines as the six coordinate lines.  Thus the
frame is monomial.  The same proof applies to \(M\). \(\square\)

## 4. Propagation to all six terms at the \(b=50\) endpoint

Assume now the full common-\(W_{15}\), all-alpha-three endpoint of N6-058:
six actual factor frames have literal-direct quadratic spaces \(F_i\), all
quotient images \(q(F_i)\) equal the same fifteen-plane \(W\), the cubic
spaces are literal direct, and the claimed intersection is \(b=50\).

Suppose one pair has a full two-row projection.  Theorem 3.1 makes both
members of that pair column-separated with monomial column frames.  For one
of them,

\[
 F_z=\langle p^2\otimes f_cf_d:c<d\rangle .
\tag{4.1}
\]

Consequently

\[
 A_z:=q^{-1}(W)=E_2+F_z
\tag{4.2}
\]

has zero projection to every same-column block
\(\operatorname{Sym}^2(R\otimes f_c)\): both summands in (4.2) use two
distinct columns.

Let \(T_k=\prod_{a=0}^5\ell_a\) be any of the other four terms, and write

\[
 \ell_a=\sum_{c=0}^5\ell_{a,c},
 \qquad \ell_{a,c}\in R\otimes f_c.
\tag{4.3}
\]

The common quotient gives \(F_k\subset q^{-1}(W)=A_z\).  Hence for every
\(a<b\), the same-column component of
\(\ell_a\ell_b\in F_k\) vanishes:

\[
 \ell_{a,c}\ell_{b,c}=0
 \quad\text{in }\operatorname{Sym}^2(R\otimes f_c).
\tag{4.4}
\]

The symmetric algebra is a domain, so (4.4) implies
\(\ell_{a,c}=0\) or \(\ell_{b,c}=0\).  Thus the six nonempty column-support
sets

\[
 S_a=\{c:\ell_{a,c}\ne0\}
\tag{4.5}
\]

are pairwise disjoint.  Six nonempty pairwise-disjoint subsets of a six-set
must all be singletons.  Therefore \(T_k\) is column-separated.  This
applies to every \(k\), so all six terms are column-separated.

N6-059 then gives

\[
 \dim\left(E_3\cap\sum_i\mathcal D_3(T_i)\right)\le40,
\tag{4.6}
\]

contradicting \(b=50\).  The transposed argument handles a full two-column
projection.

### Corollary 4.1

At the \(b=50\) endpoint, for every one of the fifteen term pairs, the
twelve-dimensional pair shadow has singular projection to every complete
row pair and every complete column pair.

## 5. Exact boundary

For an arbitrary actual pair, Theorem 3.1 proves

\[
 \operatorname{rank}(\pi_{rs}|_U)=12
 \quad\Longrightarrow\quad
 \text{the pair is column-separated},
\tag{5.1}
\]

and the transposed implication holds for a column pair.  Hence a genuinely
nonseparated pair must lie in the closed exceptional locus

\[
 \operatorname{rank}(\pi_{rs}|_U)<12,\qquad
 \operatorname{rank}(\pi_{cd}|_U)<12
\tag{5.2}
\]

for all row pairs and all column pairs.

Together with N6-059, Corollary 4.1 excludes the \(b=50\) endpoint whenever
even one term pair has a transverse row-pair or column-pair projection.
It does not classify or exclude the all-pairs, all-projections-singular
closed locus, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a
border-rank claim.

## 6. Exact replay

Run

~~~text
python scripts/n6_two_row_transverse_rigidity.py \
  --verify-json data/n6_two_row_transverse_rigidity.json
python -m unittest tests/test_n6_two_row_transverse_rigidity.py -v
~~~

The replay uses exact rational arithmetic to check Lemma 2.2, the dimensions
in (3.9), nondegeneracy of two representative \(B_0\)'s, and generation of
all \(36\) matrix directions in those sample cases.  Lemma 3.2 for arbitrary
\(B_0\) is the pure argument above, not a finite enumeration.
