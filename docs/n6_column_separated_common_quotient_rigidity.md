# N6-070: column-separated common-quotient rigidity

**Status.** PURE_COLUMN_SEPARATED_COMMON_QUOTIENT_RIGIDITY,
EXACT_QQ_BLOCK_REGRESSION, B50_COMMON_SEPARATION_EXCLUDED, N6-070.
The base field is algebraically closed of characteristic zero.

## 1. Statement

Let \(A=C=k^6\), fix the coordinate basis \(f_0,\ldots,f_5\) of \(C\),
and put \(V=A\otimes C\). Consider two actual six-factor Chow frames
separated by these same six ambient columns. Labelling each factor by its
supporting column, write

\[
 \ell_c=p_c\otimes f_c,\qquad m_c=q_c\otimes f_c,
 \qquad 0\le c<6,
\tag{1.1}
\]

where every \(p_c,q_c\in A\) is nonzero. Put

\[
 L=\langle\ell_0,\ldots,\ell_5\rangle,\qquad
 M=\langle m_0,\ldots,m_5\rangle,
\tag{1.2}
\]

and

\[
 F_p=\langle\ell_c\ell_d:c<d\rangle,\qquad
 F_q=\langle m_cm_d:c<d\rangle.
\tag{1.3}
\]

Let

\[
 \pi:\operatorname{Sym}^2V\longrightarrow
 \operatorname{Sym}^2V/E_2,
 \qquad E_2=S_0(A)\otimes S_0(C).
\tag{1.4}
\]

### Theorem 1.1

Assume

\[
 L\cap M=0,\qquad \pi(F_p)=\pi(F_q)=W.
\tag{1.5}
\]

Then there is a two-plane \(P\subset A\) such that

\[
 \boxed{L\oplus M=P\otimes C.}
\tag{1.6}
\]

After transposition, two complementary frames separated by the same six
ambient rows and sharing one quotient satisfy
\(L\oplus M=A\otimes P\) for a two-plane \(P\subset C\).

At the all-alpha-three \(b=50\) endpoint either common-separation case is
impossible: (1.6) supplies the full two-row or two-column projection used by
N6-061; N6-061 propagates separation to all six terms, and N6-059 then gives
\(b\le40\).

## 2. The exact quotient of a column-pair block

The column multigrading decomposes the cross-column part of
\(\operatorname{Sym}^2V\) into fifteen blocks indexed by \(c<d\). The
\((c,d)\)-block is naturally \(A\otimes A\), and its \(E_2\)-part is

\[
 S_0(A)=\langle
 a_i\otimes a_j+a_j\otimes a_i:i<j
 \rangle.
\tag{2.1}
\]

Define

\[
 \rho:A\otimes A\longrightarrow k^6\oplus\Lambda^2A,
 \qquad
 \rho(a\otimes b)=\bigl((a_ib_i)_{i=0}^5,\ a\wedge b\bigr).
\tag{2.2}
\]

For a general matrix tensor the first component records its diagonal and the
second its antisymmetric part. Hence

\[
 \ker\rho=S_0(A),
 \qquad
 (A\otimes A)/S_0(A)\simeq k^6\oplus\Lambda^2A.
\tag{2.3}
\]

Write

\[
 \tau(a,b)=\bigl((a_ib_i)_{i=0}^5,\ a\wedge b\bigr).
\tag{2.4}
\]

If \(a,b\ne0\), then \(\tau(a,b)\ne0\). Indeed, a zero wedge would give
\(b=\lambda a\), with \(\lambda\ne0\), and the diagonal component would be
\((\lambda a_i^2)_i\ne0\).

Each generator of \(F_p\) therefore has a nonzero image in a different
column-pair block, and the same is true for \(F_q\). Equality of their
quotient spaces is consequently equivalent to the fifteen blockwise line
equalities

\[
 \boxed{k\tau(p_c,p_d)=k\tau(q_c,q_d)\quad(c<d).}
\tag{2.5}
\]

Both the diagonal and wedge components in (2.5) are essential. The exact
replay includes a regression where the diagonal components are proportional
but the wedge components are not.

## 3. Pair-plane data

Taking the \(\Lambda^2A\)-component of (2.5) gives

\[
 p_c\wedge p_d=0
 \quad\Longleftrightarrow\quad
 q_c\wedge q_d=0.
\tag{3.1}
\]

When these bivectors are nonzero, they are proportional. A nonzero
decomposable bivector determines its supporting two-plane, so

\[
 \boxed{
 \langle p_c,p_d\rangle=\langle q_c,q_d\rangle
 \quad\text{whenever }p_c,p_d\text{ are independent}.}
\tag{3.2}
\]

Thus the two indexed vector families have the same pair-dependence relation,
and every independent indexed pair spans the same two-plane on both sides.

## 4. Complementarity is coordinatewise

The six ambient column spaces form a direct sum. Hence

\[
 L\cap M
 =\bigoplus_{c=0}^5
   (kp_c\cap kq_c)\otimes f_c.
\tag{4.1}
\]

The assumption \(L\cap M=0\) is therefore equivalent to

\[
 p_c\not\parallel q_c\quad\text{for every }c.
\tag{4.2}
\]

## 5. Rank at least three is impossible

Suppose that \(\langle p_0,\ldots,p_5\rangle\) has dimension at least
three. Choose \(p_a,p_b,p_c\) independent. Equation (3.2) gives

\[
 q_a\in\langle p_a,p_b\rangle
 \cap\langle p_a,p_c\rangle=kp_a,
\]

contradicting (4.2). Therefore

\[
 \dim\langle p_0,\ldots,p_5\rangle\le2.
\tag{5.1}
\]

## 6. The rank-two and rank-one branches

First suppose the span has dimension two. Choose \(p_a,p_b\) independent
and put \(P=\langle p_a,p_b\rangle\). Equation (3.2) also gives
\(P=\langle q_a,q_b\rangle\). For any index \(i\), use the pair
\((p_i,p_a)\) if it is independent, and otherwise use \((p_i,p_b)\).
Equation (3.2) then gives \(q_i\in P\). Thus all \(p_i,q_i\in P\).
By (4.2), every pair \(p_i,q_i\) spans \(P\), and hence

\[
 L\oplus M
 =\bigoplus_{i=0}^5\langle p_i,q_i\rangle\otimes f_i
 =P\otimes C.
\tag{6.1}
\]

Now suppose the \(p_i\) span one line \(P_1\). Equation (3.1) says that
the \(q_i\) span one line \(Q_1\). Equation (4.2) gives \(P_1\ne Q_1\).
With \(P=P_1+Q_1\), every pair \(p_i,q_i\) spans \(P\), so (6.1) again
follows. This proves Theorem 1.1.

## 7. Endpoint consequence and boundary

At the all-alpha-three \(b=50\) endpoint, N6-061 gives for each actual
section-difference graph \(D\)

\[
 \partial D=L\oplus M,\qquad \dim\partial D=12.
\tag{7.1}
\]

If a pair is commonly column-separated, Theorem 1.1 gives
\(\partial D=P\otimes C\). Some two-by-two coordinate minor of \(P\) is
nonzero, so projection to the corresponding two complete rows is an
isomorphism. N6-061 then identifies the pair with common coordinate-column
frames and propagates column separation to all six terms. N6-059 gives
\(b\le40\), contrary to \(b=50\). Transposition handles common row
separation.

The theorem assumes common separation by the same ambient columns, with one
common relabelling by those supports. It does not permit independent
permutations of the ambient columns of the two frames. It does not prove
that an arbitrary common-\(W_{15}\) pair is separated, exclude the remaining
all-singular nonseparated layer, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a
border-rank claim.

## 8. Exact replay

The replay checks the rank and kernel of \(\rho\), exhausts the elementary
identities on nonzero binary vector pairs, checks representatives of the
three rank branches, and records the diagonal-only false positive. These
are regression checks, not a substitute for the proof.

~~~text
python scripts/n6_column_separated_common_quotient_rigidity.py \
  --verify-json data/n6_column_separated_common_quotient_rigidity.json
python -m unittest tests.test_n6_column_separated_common_quotient_rigidity -v
~~~
