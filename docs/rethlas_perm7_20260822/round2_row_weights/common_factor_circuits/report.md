# Row-restriction zero circuits and their first transverse layer

## Scope and conclusion

Fix the seventh matrix row and write

\[
V=U\oplus W,
\qquad
U=\langle x_{71},\ldots,x_{77}\rangle,
\qquad
W=\langle x_{rc}:1\le r\le6,\ 1\le c\le7\rangle.
\]

This note classifies the smallest constant-layer identities among products of
seven restricted linear forms, including zero restrictions, proportional
products, repeated factors, and gcd-free circuits.  It also gives the exact
first-jet formula for a common-gcd circuit.

The classification does **not** prove rank \(64\).  It exposes a sharp
obstruction: a term having exactly one zero restricted factor contributes an
arbitrary point of \(U\otimes\operatorname{Chow}_6(W)\) to the first layer and
vanishes in every other row weight.  Thus the constant-layer zero identity is
completely silent on a legal subclass that already contains the transposed
64-term Glynn decomposition.  Excluding at most 63 terms in that subclass is
the simultaneous Chow-rank problem for the seven \(6\times6\) cofactors.

## 1. Exact row-weight equations

Let an arbitrary nonzero Chow atom be

\[
T_i=\prod_{a=1}^7\ell_{ia},
\qquad
\ell_{ia}=w_{ia}+u_{ia},\qquad w_{ia}\in W,\qquad u_{ia}\in U.
\]

Scale \(U\) by a parameter \(t\):

\[
T_i(t)=\prod_{a=1}^7(w_{ia}+t u_{ia})
      =\sum_{q=0}^7t^qT_{i,q}.
\]

If

\[
\operatorname{perm}_7=\sum_{i=1}^N T_i,
\]

then, because the permanent has \(U\)-degree exactly one,

\[
\sum_iT_{i,0}=0,
\qquad
\sum_iT_{i,1}=P:=\sum_{j=1}^7x_{7j}\operatorname{perm}_6^{(j)},
\qquad
\sum_iT_{i,q}=0\quad(2\le q\le7).
\tag{1.1}
\]

Here \(\operatorname{perm}_6^{(j)}\) is the permanent on the first six rows
with column \(j\) omitted.  Formula (1.1) is coefficient comparison, so it
includes repeated or dependent factors and vanishing \(W\)-projections.

## 2. Zero-anchor strata

Let

\[
Z_i=\{a:w_{ia}=0\},\qquad z_i=|Z_i|.
\]

Every summand in \(T_{i,q}\) contains \(u_{ia}\) for every \(a\in Z_i\).
Consequently

\[
T_{i,q}=0\quad(q<z_i).
\tag{2.1}
\]

In particular:

* if \(z_i=0\), then \(A_i:=T_{i,0}=\prod_aw_{ia}\ne0\);
* if \(z_i=1\), say \(Z_i=\{a\}\), then
  \[
  T_{i,1}=u_{ia}\prod_{b\ne a}w_{ib};
  \tag{2.2}
  \]
* if \(z_i\ge2\), then \(T_{i,0}=T_{i,1}=0\).

Conversely, every \(uG\) with \(u\in U\) and
\(G\in\operatorname{Chow}_6(W)\) is (2.2), by taking the seven-factor atom
\(uG\).  Such an atom has no row-weight component other than \(q=1\).

Thus, allowing zero restricted factors, the smallest possible
constant-layer zero identity has support one: it is simply \(A_i=0\).
There is no circuit partner to classify.

## 3. Exact minimum supports for nonzero restricted products

All products in this section are nonzero.

### Proposition 3.1 (two terms)

An identity \(c_1A_1+c_2A_2=0\), with \(c_1c_2\ne0\), exists if and only if
\(A_1,A_2\) are proportional.  In that event their multisets of projective
linear factors agree, including multiplicities.

#### Proof

Proportionality is immediate from the displayed identity.  Equality of the
factor multisets follows from unique factorization in the polynomial ring
\(\operatorname{Sym}(W)\).  This proof includes repeated and linearly
dependent factors.  The converse is immediate.  \(\square\)

### Proposition 3.2 (pairwise nonproportional terms)

Over an algebraically closed characteristic-zero field, the minimum support
of an identity among nonzero, pairwise nonproportional degree-seven Chow
products is three.  It can be achieved with gcd one.

#### Proof

One term cannot sum to zero, and Proposition 3.1 excludes two terms.  For
existence, take

\[
F=x^7-y^7,\qquad G=x^7-2y^7,\qquad H=F+G=2x^7-3y^7.
\]

All three binary septics are squarefree, pairwise coprime, and pairwise
nonproportional in characteristic zero.  Every binary form splits into
linear factors over \(k\), so

\[
F+G-H=0
\tag{3.1}
\]

is a three-term identity of degree-seven Chow products.  No two terms are
proportional, so it is minimal, and their gcd is one.  \(\square\)

A repeated-factor version is \(x^7+y^7-\prod_{\rho^7=-1}(x-\rho y)=0\).
Hence squarefreeness or independence of the displayed factors cannot be
silently assumed.

More generally, prescribe a common product \(G_0\) of degree \(g\le6\).
Apply the same binomial construction in degree \(7-g\) and multiply (3.1)
by \(G_0\), chosen coprime to the residual factors.  This gives a three-term
circuit whose gcd is exactly \(G_0\).  When \(g=7\), every term is
proportional to \(G_0\), and the
minimum support is two instead.

The residual factor span of a three-circuit need not be binary.  The
Pluecker identity

\[
(a-b)(c-d)-(a-c)(b-d)+(a-d)(b-c)=0
\tag{3.2}
\]

has residual factor span \(\langle a,b,c,d\rangle\) of dimension four.
Multiplication by any degree-five product turns it into a degree-seven
common-factor circuit.  Thus a binary/Fermat normal form is an example, not
a classification.

## 4. First jet of a common-gcd circuit

Consider a subidentity with all \(A_i\ne0\):

\[
\sum_{i=1}^r c_iA_i=0,
\qquad c_i\ne0.
\tag{4.1}
\]

Let \(G=\gcd(A_1,\ldots,A_r)\) have degree \(g\), with labeled factor copies

\[
G=q_1\cdots q_g,
\]

and write

\[
A_i=G H_i,
\qquad
H_i=h_{i1}\cdots h_{id},\qquad d=7-g.
\]

Unique factorization lets us label the copies even when some \(q_p\)'s are
proportional.  After harmless rescaling of factors, a row lift has the form

\[
T_i(t)=c_i
\prod_{p=1}^g(q_p+t v_{ip})
\prod_{s=1}^d(h_{is}+t z_{is}),
\qquad v_{ip},z_{is}\in U.
\]

Dividing (4.1) by \(G\) gives \(\sum_ic_iH_i=0\).  Direct differentiation at
\(t=0\) gives the exact first-layer formula

\[
\boxed{
\sum_iT'_{i}(0)
=
\sum_{p=1}^g\frac{G}{q_p}
   \left(\sum_i c_i v_{ip}H_i\right)
+G\sum_i c_i\sum_{s=1}^d
   z_{is}\frac{H_i}{h_{is}}.}
\tag{4.2}
\]

This is valid with repeated or dependent factors.  The constant relation
only kills the first sum in (4.2) when the motion of a common factor is
synchronized across the terms, \(v_{ip}=v_p\).  Arbitrary lifts need not be
synchronized, so constant cancellation alone does not annihilate the first
jet.

The sharp two-term example is

\[
(q+t u)q_2\cdots q_7-q q_2\cdots q_7
=t\,u q_2\cdots q_7.
\tag{4.3}
\]

Both restricted products in (4.3) are nonzero and cancel, the first layer is
an arbitrary zero-anchor atom, and every higher layer is zero.  Likewise, in
any three-term circuit one may move a single factor of one summand and keep
all other factors fixed; its quotient product then appears as a nonzero first
jet with no higher correction.  Therefore neither support-minimality nor a
large gcd creates a positive first-jet penalty.

## 5. A sharp seven-term Fourier packet

There is a stronger adversarial packet in which all seven factors move.
For

\[
T(t)=\prod_{a=1}^7(w_a+t u_a)=\sum_{q=0}^7t^qB_q
\]

and a primitive seventh root of unity \(\zeta\), Fourier orthogonality gives

\[
\boxed{
B_1=\frac1{7}\sum_{s=0}^6\zeta^{-s}
       \prod_{a=1}^7(w_a+\zeta^su_a).}
\tag{5.1}
\]

Indeed, the coefficient multiplying \(B_q\) is
\(7^{-1}\sum_s\zeta^{s(q-1)}\), which is one for \(q=1\) and zero for every
other \(q\in\{0,\ldots,7\}\).  All seven atoms in (5.1) have the same
nonzero restricted product \(\prod_aw_a\), up to the displayed external
scalar, yet their total has only row weight one.  The first layer

\[
B_1=\sum_{a=1}^7u_a\prod_{b\ne a}w_b
\tag{5.2}
\]

contains all seven tangent directions.

For a generic path, seven is minimal within this scalar-orbit ansatz.  More
precisely, suppose the nonzero \(B_q\)'s are retained and

\[
B_1=\sum_{s=1}^r d_sT(\lambda_s)
\tag{5.3}
\]

with distinct finite nodes.  Comparing bidegrees says that the coefficient
functional \([t]\) on \(k[t]_{\le7}\) is a linear combination of evaluation
at the \(r\) nodes.  If \(r\le6\) and all nodes are nonzero, the polynomial

\[
t\prod_s(t-\lambda_s)
\]

has degree at most seven, vanishes at every node, but has a nonzero
\(t\)-coefficient.  If one node is zero, then
\(\prod_s(t-\lambda_s)\) itself has a nonzero \(t\)-coefficient.  Both cases
contradict (5.3).  Formula (5.1) attains \(r=7\).

Thus an attempted eight-point interpolation penalty is false, and a
seven-term proportional-anchor packet already transports the complete first
polarization while satisfying every off-weight cancellation equation.

## 6. The all-zero-anchor obstruction is a simultaneous Chow-rank problem

Define

\[
\rho_{U\mid W}(P)=\min\left\{r:
P=\sum_{i=1}^r u_iG_i,
\ u_i\in U,
\ G_i\in\operatorname{Chow}_6(W)\right\}.
\tag{6.1}
\]

Let

\[
\mathcal C=\left\langle
\operatorname{perm}_6^{(1)},\ldots,
\operatorname{perm}_6^{(7)}
\right\rangle\subset\operatorname{Sym}^6W.
\]

Then

\[
\boxed{
\rho_{U\mid W}(P)=\min\left\{r:
\mathcal C\subseteq\langle G_1,\ldots,G_r\rangle,
\ G_i\in\operatorname{Chow}_6(W)\right\}.}
\tag{6.2}
\]

To prove (6.2), compare the seven \(U\)-coefficients in (6.1).  Conversely,
if the seven cofactors lie in the span of the \(G_i\)'s, use their coefficient
matrix to define the vectors \(u_i\in U\).

Every decomposition counted by (6.1) is an ordinary Chow decomposition of
\(P=\operatorname{perm}_7\), and every one of its atoms has exactly one zero
restricted factor.  Conversely every decomposition consisting entirely of
such atoms is counted by (6.1).  The transposed Glynn identity consists of 64
terms of this kind, so

\[
\rho_{U\mid W}(P)\le64.
\]

Contracting (6.1) with any coordinate of \(U^*\) expresses a \(6\times6\)
cofactor as a sum of the same \(r\) degree-six Chow atoms.  The exact theorem
\(\operatorname{ChowRank}(\operatorname{perm}_6)=32\) therefore gives the
unconditional but much weaker bound

\[
\rho_{U\mid W}(P)\ge32.
\tag{6.3}
\]

The repaired lower-50 theorem in the current project raises (6.3) to 50,
because (6.1) is a subclass of ordinary Chow decompositions; it does not
decide (6.2).

For comparison, Han--Ju--Kim, arXiv:2503.12032, Theorem
`thm:PermLower`, prove the complete statement

\[
\underline{\mathbf R}(\operatorname{per}_4)=\mathbf R(\operatorname{per}_4)=8,
\quad
\underline{\mathbf R}(\operatorname{per}_5)\ge15,
\quad
\underline{\mathbf R}(\operatorname{per}_6)\ge29,
\quad
\underline{\mathbf R}(\operatorname{per}_7)\ge55.
\]

Here `paper_id=Han-Ju-Kim-RecursiveKoszul-2503.12032` and
`arXiv id=2503.12032`.  Their atoms are decomposable in all seven row tensor
factors.  A zero-anchor atom in (6.1) has only its \(U\)-factor separated;
its six \(W\)-linear factors may mix all remaining rows.  Hence their theorem
does not apply to (6.2).  The row-separation assumption is exactly what gives
their recursive wedge map its rank-one cap.

## 7. Consequences for the rank-64 route

1. A theorem about nonzero constant-layer circuits alone cannot prove rank
   \(64\): the all-zero-anchor sector makes every equation except the first
   layer vanish termwise.
2. Even among nonzero anchors, minimum circuit support is only two in a
   proportional class and three in a gcd-free simple class.
3. Common factors do not force the first jet to cancel; (4.3) is exact.
4. Seven proportional-anchor atoms can isolate the full seven-direction
   tangent polarization, by (5.1).
5. The first necessary replacement interface is the simultaneous rank
   problem (6.2).  Proving its value is 64 would exclude the all-zero-anchor
   sector, but would still not exclude mixed packets containing nonzero
   constant circuits.

A useful coupled theorem must therefore charge both pieces of the exact
sequence

\[
\{\text{nonzero-anchor constant zero circuits and their jets}\}
\longrightarrow
P
\longleftarrow
U\otimes\operatorname{Chow}_6(W),
\]

with a sum inequality valid for arbitrary mixtures.  Circuit support, gcd
degree, and off-weight support by themselves are insufficient.

## Status

`EXACT CIRCUIT MINIMA AND JET FORMULAS PROVED; EXACT64 NOT PROVED.`
