# Frobenius/complementary-Tor audit

## Status

`EXACT NO-GO FOR THE CANONICAL LOW/HIGH TOR PAIRING.`

Complementary-degree duality does produce a genuine reverse arrow, but trace
additivity forces that arrow to factor through exactly the sector already
retained by the ordinary Tor pushout.  It cannot recover any of the classes
that the pushout deletes.

For the two-term common-factor collision \(F_2\), the resulting target-map
rank is exactly

\[
 540\le 2\cdot294=588.
\]

Thus it passes the deletion test.  On the actual 64-term Glynn decomposition
of \(\operatorname{perm}_7\), however, its rank is exactly

\[
 6272<18523=63\cdot294+1.
\]

It misses the necessary target by \(12251\), exactly as the ordinary
pushout does.  Hence the canonical Frobenius map, its image, every subquotient
of that image, every target-originating path rank, and the common pulled-back
trace pairing are closed as rank-64 invariants.

The computation is organized so that the decisive upper bound is a
characteristic-zero theorem.  The accompanying prime-field scripts merely
give matching lower ranks for the two examples; since their matrices have
integer entries, these lower ranks are also valid in characteristic zero.

## 1. Shifted Matlis dual and the reverse Tor fork

Let \(S=\operatorname{Sym}(V^*)\), with \(\dim V=49\), and suppose

\[
 f=\sum_{i=1}^N T_i,\qquad
 I=\bigcap_i\operatorname{Ann}(T_i),\qquad
 R=S/I,\qquad
 A=S/\operatorname{Ann}(f),\qquad
 D=\bigoplus_i A_i,\quad A_i=S/\operatorname{Ann}(T_i).
\]

There are canonical maps

\[
 u:R\hookrightarrow D,\qquad v:R\twoheadrightarrow A.
 \tag{1.1}
\]

All forms have degree seven.  For a finite graded module \(Q\) supported in
degrees zero through seven, define its shifted graded dual by

\[
 (Q^\dagger)_d=\operatorname{Hom}_K(Q_{7-d},K).
 \tag{1.2}
\]

Put \(M=R^\dagger\).  Applying \(\dagger\) to (1.1) reverses the arrows:

\[
 D^\dagger\longrightarrow M\longleftarrow A^\dagger.
 \tag{1.3}
\]

Every \(A_i\) and \(A\) is Artinian Gorenstein of socle degree seven.  If
\(\lambda_F:(A_F)_7\to K\) is the apolar trace, multiplication followed by
\(\lambda_F\) gives the degree-preserving Frobenius isomorphism

\[
 \iota_F:A_F\xrightarrow{\sim}A_F^\dagger,\qquad
 \iota_F(a)(b)=\lambda_F(ab).
 \tag{1.4}
\]

After these identifications, (1.3) becomes a canonical cospan

\[
 D\xrightarrow{\beta}M\xleftarrow{\alpha}A.
 \tag{1.5}
\]

On minimal resolutions, ordinary graded duality gives

\[
 \operatorname{Tor}_2^S(M,K)_3^*
 \simeq \operatorname{Tor}_{47}^S(R,K)_{53}.
 \tag{1.6}
\]

Indeed \(47=49-2\) and \(53=(49+7)-3\).  Under (1.6), the transposes of the
maps induced by \(\alpha\) and \(\beta\) are the complementary high-Tor maps
induced by \(v\) and \(u\), respectively.  Thus (1.5) is precisely the
algebraically natural way to add the \(\beta_{47,53}\) data to the
\(\beta_{2,3}\) fork; it is not an ad hoc identification of two vector
spaces.

## 2. Trace-square theorem

Write

\[
 H(Q)=\operatorname{Tor}_2^S(Q,K)_3.
\]

Let

\[
 a=H(v):H(R)\to H(A),\quad b=H(u):H(R)\to H(D),
\]

and

\[
 \bar a=H(\alpha):H(A)\to H(M),\quad
 \bar b=H(\beta):H(D)\to H(M).
\]

### Proposition 2.1 (the Frobenius square)

The module square

\[
\begin{array}{ccc}
R&\xrightarrow{u}&D\\
\downarrow v&&\downarrow\beta\\
A&\xrightarrow{\alpha}&M
\end{array}
\tag{2.1}
\]

commutes.  Consequently

\[
 \bar a\,a=\bar b\,b. \tag{2.2}
\]

#### Proof

For homogeneous \(r\in R_d\), both routes in (2.1) are elements of
\((R^\dagger)_d=\operatorname{Hom}(R_{7-d},K)\).  Evaluate them on
\(s\in R_{7-d}\).  The route through \(A\) gives

\[
 \lambda_f(rs)=(rs)\mathbin{\cdot}f.
\]

The route through \(D\) gives

\[
 \sum_i\lambda_{T_i}(rs)
 =\sum_i(rs)\mathbin{\cdot}T_i
 =(rs)\mathbin{\cdot}f.
\]

The two module maps are equal.  Functoriality of Tor gives (2.2). \(\square\)

### Corollary 2.2 (pushout domination)

Let

\[
 \kappa=\dim H(A)-\dim a(\ker b),
 \tag{2.3}
\]

the target dimension retained by the ordinary module pushout.  Then

\[
 a(\ker b)\subseteq\ker\bar a,\qquad
 \operatorname{rank}\bar a\le\kappa.
 \tag{2.4}
\]

#### Proof

If \(x\in\ker b\), then (2.2) gives

\[
 \bar a(a(x))=\bar b(b(x))=0.
\]

The first inclusion follows, and rank-nullity gives the second inequality.
\(\square\)

This is the decisive obstruction.  The high-Tor arrow is not merely unable
to repair the old kernel by a currently missing argument: trace additivity
forces it to annihilate that entire kernel sector.

There are two immediate stronger no-go consequences.

* The pulled-back Frobenius pairing on common Tor is represented by the
  common path \(\bar a a=\bar b b\), so its rank is at most
  \(\operatorname{rank}b\), even smaller than (2.4).
* Every image, quotient, persistent subspace, or path-rank construction
  factoring through \(\bar a\) has dimension at most \(\kappa\).  The new
  arrow is identically zero on the old lost sector \(a(\ker b)\), so the
  homology-level Frobenius square supplies no selector inside that sector.

## 3. The common-factor collision

Take

\[
 F_2=c\prod_{i=1}^6a_i+c\prod_{j=1}^6b_j.
\]

In its thirteen essential variables, let \(M\) be the shifted inverse-system
module generated by the two displayed terms.  Through derivative degree
three, their derivative monomials are disjoint.  Hence \(M\) agrees in the
entire relevant Koszul strand with the direct sum of the two term modules.

The exact essential Hilbert vectors through degree three are

\[
 h(A_{F_2})=(1,13,42,70),\qquad h(M)=(2,14,42,70).
\]

The internal-degree-two and internal-degree-three Koszul strands give

\[
 \operatorname{rank}\bigl[\operatorname{Tor}_{1,2}(A_{F_2})
 \to\operatorname{Tor}_{1,2}(M)\bigr]=13,
\]

and

\[
 \operatorname{rank}\bigl[\operatorname{Tor}_{2,3}(A_{F_2})
 \to\operatorname{Tor}_{2,3}(M)\bigr]=72.
\]

The other 36 ambient variables act trivially.  The Koszul Kunneth
decomposition therefore gives the ambient rank

\[
 72+36\cdot13=540. \tag{3.1}
\]

This matches the exact pushout value \(\kappa(F_2)=540\), and is below the
two-atom budget 588.  The replay is

```text
python results/perm7_theory_first_20260822/round2_frobenius_tor/f2_dual_cospan.py
```

with final marker `F2_DUAL_COSPAN_PASS`.

## 4. The Glynn packet

For the normalized signs

\[
 \epsilon=(1,\epsilon_1,\ldots,\epsilon_6),\qquad
 \epsilon_i\in\{\pm1\},
\]

write

\[
 T_\epsilon=\prod_{j=1}^7\left(\sum_{a=0}^6
 \epsilon_a x_{aj}\right).
\]

Let \(M\) be the shifted inverse-system module generated by these 64 terms.
Fourier transform in the sign index.  In derivative degree \(d\), and for a
fixed \(d\)-subset \(J\) of removed columns, a basis is

\[
 v_{J,U},\qquad U\subseteq\{1,\ldots,6\},\qquad |U|\le7-d.
 \tag{4.1}
\]

Differentiation in a new column by row zero fixes \(U\), while
differentiation by row \(a>0\) replaces \(U\) by
\(U\mathbin\triangle\{a\}\); a character outside the next size cutoff is
zero.  Glynn's coefficient is the full character
\(U_0=\{1,\ldots,6\}\).  If \(R_0\) is the set of differentiated rows, the
permanent cyclic submodule maps by

\[
 (J,R_0)\longmapsto
 v_{J,U_0\mathbin\triangle(R_0\setminus\{0\})}.
 \tag{4.2}
\]

Equations (4.1)--(4.2) reduce the full Koszul calculation to one integer
matrix in each of the three column-multidegree types.  The target and
term-side image ranks are

\[
\begin{array}{c|c|c|c|c|c|c}
\text{column type}&\text{number of blocks}&
\dim H(A)&\operatorname{rank}\bar a&
\operatorname{rank}\bar b&
\dim(\operatorname{im}\bar a\cap\operatorname{im}\bar b)&
\dim\frac{\operatorname{im}\bar a}
{\operatorname{im}\bar a\cap\operatorname{im}\bar b}\\ \hline
3e_j&7&112&112&384&112&0\\
2e_j+e_k&42&196&119&384&112&7\\
e_j+e_k+e_l&35&280&14&0&0&14.
\end{array}
\tag{4.3}
\]

All five dimension columns in (4.3) are per block.

Thus

\[
 7\cdot112+42\cdot196+35\cdot280=18816,
\]

whereas

\[
 \operatorname{rank}\bar a
 =7\cdot112+42\cdot119+35\cdot14
 =6272. \tag{4.4}
\]

Moreover,

\[
 \operatorname{rank}\bar b=18816,\qquad
 \dim(\operatorname{im}\bar a\cap\operatorname{im}\bar b)=5488,
\qquad
 \dim\frac{\operatorname{im}\bar a}
 {\operatorname{im}\bar a\cap\operatorname{im}\bar b}=784.
 \tag{4.5}
\]

Thus the complementary cospan is an exact dual mirror of the ordinary
pushout data: the \(6272\)-dimensional target image consists of the same
\(5488\) persistent classes plus \(784\) target-only classes.  The
\(12544\)-dimensional sector that must be recovered is the kernel of
\(\bar a\), so it receives no new arrow at all.

The characteristic-zero upper bound in (4.4) is already Corollary 2.2 and
the previously proved exact pushout value \(\kappa=6272\).  The matrices in
(4.1)--(4.2) have integer entries.  Row reduction modulo 1000003 gives the
matching lower ranks in (4.3), hence exhibits nonzero minors and proves the
same lower bound over characteristic zero.  The replay is

```text
python results/perm7_theory_first_20260822/round2_frobenius_tor/glynn_dual_cospan.py
```

with final marker `GLYNN_DUAL_COSPAN_PASS`.

## 5. Sharp no-go theorem and surviving interface

### Theorem 5.1

The canonical complementary-degree construction obtained by

1. identifying \(\beta_{47,53}\) with the dual of
   \(\beta_{2,3}\) of the shifted canonical module,
2. using the Frobenius isomorphisms of the target and term apolar algebras,
   and
3. taking the rank, an image, a subquotient of the image, an image
   intersection, or another target-originating path rank in the resulting
   commutative Tor square,

cannot prove \(\operatorname{ChowRank}(\operatorname{perm}_7)\ge64\).

#### Proof

Every target contribution in the listed class factors through
\(\operatorname{im}\bar a\).  Corollary 2.2 bounds it by the ordinary
pushout survivor.  On the actual Glynn packet this survivor has dimension
6272, whereas any 294-per-atom rank obstruction for 64 requires target at
least 18523.  The pulled-back common pairing is smaller still, with rank at
most the right-arrow rank 5488. \(\square\)

The no-go is sharp in scope.  It does not rule out a secondary operation
that is nonzero on

\[
 a(\ker b)\subset H(A).
\]

But such an operation cannot be the ordinary Frobenius trace, the transpose
of the complementary high-Tor map, or any functorial image/path construction
made from those arrows: Proposition 2.1 forces all of them to vanish there.
Numerically, a successful secondary construction would have to retain at
least 12251 of the 12544 lost Glynn classes while retaining at most 48 of
the 1476 lost \(F_2\) classes.  It would therefore need genuine secondary
chain data---for example a separately proved multiplication homotopy,
extension class, or higher operation---together with a new arbitrary-atom
cap.  Minimal-resolution self-duality and the ordinary Frobenius trace alone
contain no such operation.

## 6. Literature boundary

For background, Miller--Rahmati--Striuli, *Duality for Koszul Homology over
Gorenstein Rings*, `paper_id=Miller-Rahmati-Striuli-1112.3064`,
`arXiv id=1112.3064`, Theorem 1.2, Corollary 1.4, and Theorem 1.6, prove
double-Ext/Koszul-homology duality over a Gorenstein ring and its
canonical-module extension over a Cohen--Macaulay ring.  Their proof uses
the two spectral sequences of

\[
 \operatorname{Hom}_R(K(\mathbf y),J)
\]

and identifies the edge maps after a second canonical-module dual.  The
local source and proof checked here are
`downloads/frobenius_tor/1112.3064.pdf` and
`downloads/frobenius_tor/1112.3064.txt`, especially Construction 1.1 and the
proofs of Theorems 1.2 and 1.6.

That result grounds the use of canonical-module duality, but it does not
compare the images of several distinct apolar Gorenstein quotients inside
the non-Gorenstein common module \(M\).  Proposition 2.1 above is the needed
problem-specific comparison, and it gives a no-go rather than the hoped-for
rank amplification.
