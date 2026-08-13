# N6-068: exclusion of actual pairs in a product \(3\times4\) shadow

**Status.** `PURE_PRODUCT_34_ACTUAL_PAIR_EXCLUSION`,
`EXACT_QQ_SYMBOLIC_REGRESSION` (N6-068).  The base field is algebraically
closed of characteristic zero.

## 1. Statement

Let \(R=C=k^6\), put \(V=R\otimes C\), and write

\[
 E_2=S_0(R)\otimes S_0(C)
 \subset\operatorname{Sym}^2V
\tag{1.1}
\]

for the quadratic permanent space.  Let \(A\subset R\) and \(B\subset C\)
have dimensions three and four, and put \(U=A\otimes B\).

Suppose that \(U=L\oplus M\), with \(\dim L=\dim M=6\), and that

\[
 D\subset E_2\cap\operatorname{Sym}^2U,
 \qquad \dim D=15,
\tag{1.2}
\]

is an **actual section-difference space**.  Thus

\[
 D\subset\operatorname{Sym}^2L\oplus\operatorname{Sym}^2M
\tag{1.3}
\]

and the two block projections of \(D\) are isomorphisms onto the
fifteen-dimensional squarefree quadratic spaces of the two Chow frames.

### Theorem 1.1

No data satisfying (1.2)--(1.3) exist.  The same conclusion holds for a
product \(4\times3\) shadow after row-column transposition.

## 2. The product intersection has only two possible dimensions

Let

\[
 \rho_i=e_i^*|_A\in A^*,\qquad
 \sigma_j=f_j^*|_B\in B^*
 \quad(0\le i,j<6)
\tag{2.1}
\]

be the six coordinate restrictions on each factor.  They span \(A^*\) and
\(B^*\), respectively.  Under the perfect symmetric pairings, put

\[
 \begin{aligned}
 P&=\operatorname{Sym}^2A\cap S_0(R)
   =\langle\rho_0^2,\ldots,\rho_5^2\rangle^\perp,\\
 Q&=\operatorname{Sym}^2B\cap S_0(C)
   =\langle\sigma_0^2,\ldots,\sigma_5^2\rangle^\perp.
 \end{aligned}
\tag{2.2}
\]

The symmetric-symmetric Cauchy summand gives

\[
 E_2\cap\operatorname{Sym}^2(A\otimes B)=P\otimes Q.
\tag{2.3}
\]

Choose three independent \(\rho_i\) and four independent \(\sigma_j\).
Their squares are independent, so, with \(p=\dim P\) and \(q=\dim Q\),

\[
 p\le3,\qquad q\le6.
\tag{2.4}
\]

Since \(D\subset P\otimes Q\) has dimension fifteen, \(pq\ge15\).
Consequently

\[
 \boxed{(p,q)=(3,5)\text{ or }(3,6).}
\tag{2.5}
\]

There are no hidden intersection dimensions sixteen or seventeen: the
ambient product in (2.3) has dimension exactly \(pq\).

The equality \(p=3\) also determines the first factor.  Use three independent
\(\rho_i\) as a basis of \(A^*\).  Every remaining square lies in the span of the
three basis squares.  Comparing cross monomials shows that each remaining
\(\rho_i\) has at most one nonzero basis coordinate.  Hence, in the recovered
basis,

\[
 P=S_0(A),\qquad \dim P=3.
\tag{2.6}
\]

If \(q=6\), the identical argument on \(B\) gives \(Q=S_0(B)\) in a
recovered four-element coordinate basis.

## 3. Every hyperplane of \(S_0(k^4)\) contains an invertible tensor

The branch \(q=5\) makes \(Q\) a hyperplane in \(S_0(B)\): choose four
independent coordinate restrictions as a basis of \(B^*\); their squares
cut out \(S_0(B)\), and (2.2) imposes one further independent equation.

### Lemma 3.1

Every hyperplane of \(S_0(k^4)\) contains an invertible symmetric matrix.

### Proof

Let \(x_{ij}\), \(i<j\), be the six off-diagonal coordinates and let \(F\)
be the determinant of the generic zero-diagonal symmetric matrix.  If a
hyperplane \(\ell=0\) consisted of singular matrices, then
\(F|_{\ell=0}=0\), so the linear form \(\ell\) would divide \(F\).

The connected diagonal torus acts by
\(x_{ij}\mapsto t_it_jx_{ij}\), and \(F\) is a semi-invariant.  A connected
group cannot permute a finite set of irreducible factors nontrivially, so
every irreducible factor of \(F\) is a semi-invariant.  The six degree-one
weights \(e_i+e_j\) are distinct.  Therefore any linear factor of \(F\)
would be a scalar multiple of one coordinate \(x_{ij}\).

But for every edge \(ij\), one of the three perfect-matching-square terms
of \(F\) avoids \(x_{ij}\).  Thus no \(x_{ij}\) divides \(F\), a
contradiction. \(\square\)

## 4. The \(q=5\) branch

In this branch \(\dim(P\otimes Q)=15\), so (1.2) gives

\[
 D=P\otimes Q=S_0(A)\otimes Q.
\tag{4.1}
\]

Lemma 3.1 supplies an invertible \(q_0\in Q\).  Also choose an invertible
\(p_0\in S_0(A)\).  Then

\[
 d_0=p_0\otimes q_0\in D
\tag{4.2}
\]

is invertible on \(U\).  By (1.3), it is block diagonal relative to
\(U=L\oplus M\), so both of its diagonal blocks are invertible.  For every
\(p\in S_0(A)\), the ratio

\[
 (p\otimes q_0)d_0^{-1}=(pp_0^{-1})\otimes I_B
\tag{4.3}
\]

preserves both \(L\) and \(M\).

### Lemma 4.1

For every invertible \(p_0\in S_0(k^3)\),

\[
 \operatorname{Alg}\{pp_0^{-1}:p\in S_0(k^3)\}
 =\operatorname{End}(k^3).
\tag{4.4}
\]

### Proof

Suppose a nonzero proper space \(H\) were invariant and put
\(Z=p_0^{-1}H\).  Then \(S_0(k^3)Z\subset H\).  A vector with three
nonzero coordinates has full three-dimensional \(S_0(k^3)\)-image.  Hence
every vector of \(Z\) has support at most two, and \(Z\) lies in one
coordinate two-plane.  A one-dimensional \(Z\) has image dimension two;
while for a coordinate two-plane, the images of its two coordinate axes
together span all of \(k^3\).  Both possibilities contradict
\(\dim Z=\dim H<3\).  Thus the algebra is irreducible, and Burnside's
theorem proves (4.4). \(\square\)

Equations (4.3)--(4.4) imply that \(L\) and \(M\) are modules for
\(\operatorname{End}(A)\otimes I_B\).  Matrix units give

\[
 L=A\otimes X,\qquad M=A\otimes Y,
 \qquad \dim X=\dim Y=2,\qquad B=X\oplus Y.
\tag{4.5}
\]

The \(L\)-block projection of (4.1) is contained in

\[
 S_0(A)\otimes\operatorname{Sym}^2X,
\tag{4.6}
\]

whose dimension is at most \(3\cdot3=9\).  This contradicts the actual
section-difference hypothesis, under which the projection
\(D\to F_L\subset\operatorname{Sym}^2L\) is an isomorphism of rank fifteen.
Therefore the \(q=5\) branch is impossible.

## 5. The \(q=6\) branch

Here (2.6) and its four-dimensional analogue identify

\[
 P\otimes Q=S_0(k^3)\otimes S_0(k^4)=E_{34}
\tag{5.1}
\]

after changing to the recovered coordinate bases.  Condition (1.3) says
that every tensor of \(D\) vanishes on \(L\times M\).  Hence the cross-free
kernel inside \(E_{34}\) has dimension at least fifteen.  The pure fixed
\(K_{3,4}\) theorem N6-063 says that no complementary six-planes in
\(k^3\otimes k^4\) have such a cross-free kernel.  This excludes the second
branch and completes Theorem 1.1.

## 6. Boundary and replay

This theorem concerns an **actual** complementary pair whose twelve-plane
shadow is a tensor product \(A_3\otimes B_4\), or its transpose.  It does
not classify arbitrary twelve-planes with a fifteen-dimensional quadratic
permanent intersection, exclude the full `b=50` endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a
border-rank claim.

The accompanying script checks the determinant formula, the absence of a
coordinate linear factor, one exact rational ratio-algebra representative,
and the dimension gate.  It is not a substitute for the proof.

```text
python scripts/n6_product_34_actual_pair_exclusion.py \
  --verify-json data/n6_product_34_actual_pair_exclusion.json
python -m unittest tests.test_n6_product_34_actual_pair_exclusion -v
```
