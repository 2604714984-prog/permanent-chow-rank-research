# Exact no-go theorem for the ordinary Tor-pushout coupling

## Status

`PURE EXACT BARRIER.`

The most direct way to couple the two arrows in the apolar span diagram is
canonical and does delete the bad common-factor classes.  Nevertheless, it
retains only `6272` of the permanent's `18816` linear first syzygies on the
actual 64-term Glynn decomposition.  Hence it misses the threshold `18523`
by `12251`.  Every subspace, quotient, page, image, or persistent subquotient
that factors through this target image is ruled out.

The calculation is symbolic over every characteristic different from two.
The accompanying prime-field matrix replay is only an independent diagnostic.

## 1. The canonical coupled module

Let

\[
 I=\bigcap_i\operatorname{Ann}(T_i),\qquad
 R=S/I,\qquad A=A_f=S/\operatorname{Ann}(f),\qquad
 D=\bigoplus_i A_{T_i},
\]

where \(f=\sum_iT_i\).  The canonical maps are an injection
\(u:R\hookrightarrow D\) and a surjection \(v:R\twoheadrightarrow A\).
Their pushout in graded \(S\)-modules is

\[
 P=D\sqcup_R A
   =\operatorname{coker}\bigl(R\xrightarrow{(u,-v)}D\oplus A\bigr).
 \tag{1.1}
\]

It is coordinate-free and functorial for isomorphisms of the whole apolar
span diagram.  It fits into

\[
 0\longrightarrow R\longrightarrow D\oplus A\longrightarrow P
 \longrightarrow0,
 \tag{1.2}
\]

as well as

\[
 0\longrightarrow A\longrightarrow P\longrightarrow D/R\longrightarrow0
 \quad\text{and}\quad
 0\longrightarrow\ker(v)\longrightarrow D\longrightarrow P
 \longrightarrow0.
 \tag{1.3}
\]

Write, only in bidegree \((2,3)\),

\[
 H_R=\operatorname{Tor}_2^S(R,K)_3,
 \quad H_A=\operatorname{Tor}_2^S(A,K)_3,
 \quad H_D=\operatorname{Tor}_2^S(D,K)_3,
\]

and let \(r:H_R\to H_D\), \(l:H_R\to H_A\) be the induced maps.
Exactness of (1.2) gives

\[
 \ker\bigl(H_A\longrightarrow\operatorname{Tor}_2^S(P,K)_3\bigr)
   =l(\ker r).
 \tag{1.4}
\]

Indeed, \((0,a)\) dies in the middle term of the long exact Tor sequence iff
\((0,a)=(r(x),-l(x))\) for some \(x\in H_R\), which is equivalent, up to the
irrelevant sign, to \(r(x)=0\) and \(a=l(x)\).

Thus the exact retained target dimension of the ordinary pushout is

\[
 \kappa(f;T_1,\ldots,T_s)
   :=\dim\operatorname{im}\left(H_A\to
       \operatorname{Tor}_2^S(P,K)_3\right)
   =\dim H_A-\dim l(\ker r).
 \tag{1.5}
\]

For the two-term common-factor family in the prior report, \(l\) is an
isomorphism in this bidegree and \(\dim\ker r=1476\).  Hence

\[
 \kappa(F_2;T_1,T_2)=2016-1476=540\le 588.
 \tag{1.6}
\]

So (1.5) passes the exact deletion test which defeated the raw Betti number.

## 2. Glynn notation and the common quadrics

The following calculation is carried out for general \(n\ge3\).  Put
\(W=K^{n\times n}\), with dual differential variables \(y_{aj}\), and let

\[
 T_\epsilon=\prod_{j=1}^n\left(\sum_{a=1}^n
 \epsilon_a x_{aj}\right),
 \qquad \epsilon\in\Omega:=\{\pm1\}^n/\{\pm1\}.
 \tag{2.1}
\]

Let \(I_G=\bigcap_{\epsilon\in\Omega}\operatorname{Ann}(T_\epsilon)\)
and \(R_G=S/I_G\).  For a fixed matrix column, every quadratic differential
operator belongs to \((I_G)_2\).  For two distinct columns, identify the
quadrics with matrices \(M\in E\otimes E\), where \(E=K^n\).  Their value on
\(T_\epsilon\) is \(\epsilon^{\mathsf T}M\epsilon\).  Therefore their common
kernel is

\[
 K_0=\Lambda^2E\oplus
 \left\langle y_a\otimes y_a-y_n\otimes y_n:1\le a<n\right\rangle.
 \tag{2.2}
\]

Consequently

\[
 (I_G)_2=
 \bigoplus_{j=1}^n\operatorname{Sym}^2(E_j)
 \oplus\bigoplus_{1\le j<k\le n}K_{0,jk}.
 \tag{2.3}
\]

The extra permanent quadrics consist of one trace quadric for every unordered
column pair.  Put \(U=((I_G)_2)\).  Modulo \(U\), a cubic uses three distinct
columns.  Skew relations allow row labels to be swapped, while trace-zero
diagonal relations identify all repeated pairs.  A row word is therefore
determined by its parity support, which has cardinality one or three.  The
corresponding Walsh characters are independent on \(\Omega\), so

\[
 \dim(S/U)_3=\binom n3\left(n+\binom n3\right).
 \tag{2.4}
\]

On the other hand \(\dim(A_{\operatorname{perm}_n})_3=\binom n3^2\).
Adding the \(\binom n2\) trace quadrics hence creates exactly

\[
 \begin{aligned}
 \delta_n
 &=n^2\binom n2-n\binom n3\\
 &=\frac{n^2(n^2-1)}3
 \end{aligned}
 \tag{2.5}
\]

new linear syzygies.  Equivalently,

\[
 \dim\operatorname{coker}\left[
 \operatorname{Tor}_{2,3}(R_G)\to
 \operatorname{Tor}_{2,3}(A_{\operatorname{perm}_n})\right]=\delta_n.
 \tag{2.6}
\]

Both ideals have no linear forms, so their \(\operatorname{Tor}_{2,3}\)
spaces are literally kernels of multiplication
\(W\otimes I_2\to S_3\), and the map in (2.6) is injective.

## 3. Exact rank of the right Tor arrow

For a Glynn term, let \(L_\epsilon\) be its inactive linear annihilator
space and \(Q_\epsilon\) the span of its \(n\) active square quadrics.  The
term is a complete intersection after removing the inactive variables, so

\[
 \operatorname{Tor}_{2,3}(A_{T_\epsilon})
   =L_\epsilon\otimes Q_\epsilon.
 \tag{3.1}
\]

Choose a splitting only to compute the natural map.  If
\(z\in\ker(W\otimes(I_G)_2\to S_3)\), its image in (3.1) is obtained by
restricting its quadratic factor to \(Q_\epsilon\) and projecting its linear
coefficient to \(L_\epsilon\).  This follows directly by lifting the minimal
linear and quadratic generators through the tensor-product resolution of
the term.  The resulting rank is independent of the splitting.

Both source and target split by column multidegree.  A target block is
indexed by an ordered pair \((j,k)\): the active square lies in column \(j\)
and its inactive linear coefficient lies in column \(k\).  There are \(n^2\)
such mutually disjoint blocks.

Define the even quadratic Walsh space

\[
 Q=\left\langle 1,\epsilon_a\epsilon_b:1\le a<b\le n\right\rangle
\]

and the odd cubic Walsh space

\[
 B_3=\left\langle \epsilon_a,
 \epsilon_a\epsilon_b\epsilon_c:1\le a<b<c\le n\right\rangle.
\]

Pointwise multiplication gives a surjection

\[
 \mu_B:E\otimes Q\longrightarrow B_3.
 \tag{3.2}
\]

Its kernel has dimension

\[
 \begin{aligned}
 h_n
 &=n\left(1+\binom n2\right)-\left(n+\binom n3\right)\\
 &=n(n-1)+2\binom n3
 =\frac{n(n^2-1)}3.
 \end{aligned}
 \tag{3.3}
\]

The middle expression also gives an explicit basis.  For each singleton
character there are \(n\) preimages and hence \(n-1\) differences; for each
triple character there are three preimages and hence two differences.

We now show that every ordered column block of the right Tor map has image
exactly \(\ker\mu_B\).

* If \(j=k\), the source block is

  \[
  \ker\left(E\otimes\operatorname{Sym}^2E
  \longrightarrow\operatorname{Sym}^3E\right),
  \]

  which has dimension \(h_n\).  Its sign-evaluation map lands in
  \(\ker\mu_B\).  It is injective: if its vector-valued quadratic evaluation
  vanishes on every sign, every coordinate belongs to
  \(D_0=\langle x_a^2-x_n^2:a<n\rangle\).  The multiplication map
  \(E\otimes D_0\to\operatorname{Sym}^3E\) is injective, as is seen from the
  distinct monomials \(x_cx_a^2\) and \(x_cx_n^2\).  The original polynomial
  syzygy therefore forces all coordinates to vanish.  Equal dimensions now
  give image \(\ker\mu_B\).

* If \(j\ne k\), a syzygy combines a coefficient from column \(k\) times a
  same-column quadratic in \(j\), with a coefficient from \(j\) times an
  element of \(K_{0,jk}\).  Its output again lies in \(\ker\mu_B\).  The
  explicit Walsh-kernel generators lift using only skew elements of
  \(K_{0,jk}\):

  \[
  y_c\otimes x_b^2-y_b\otimes x_bx_c
     =x_b(x_by_c-x_cy_b)
  \tag{3.4}
  \]

  gives all singleton-character differences, and

  \[
  y_a\otimes x_bx_c-y_b\otimes x_ax_c
     =x_c(x_by_a-x_ay_b)
  \tag{3.5}
  \]

  gives all triple-character differences.  Hence this block is also onto
  \(\ker\mu_B\) and has rank \(h_n\).

It follows that the complete right-arrow persistent rank is

\[
 \rho_n=n^2h_n=\frac{n^3(n^2-1)}3=n\delta_n.
 \tag{3.6}
\]

## 4. Pushout value on the permanent

The only external numerical statement used here is the following complete
result.  Alper--Rowlands, *Syzygies of the apolar ideals of the determinant
and permanent*, `paper_id=Alper-Rowlands-Syzygies-1709.09286`,
`arXiv id=1709.09286`, Main Theorem (b) and Proposition
`thm:dimensions-perm`, prove: in arbitrary characteristic the first syzygy
module of \(\operatorname{perm}_n^\perp\) is minimally generated by

\[
 4\binom{n+1}{3}\binom{n+2}{3}
\]

linear relations and
\(2\binom n2\binom n4\) quadratic relations, with no generators in other
degrees.  Their proof classifies every linear-relation multidegree, computes
its dimension, and sums the table.  The local source checked here is
`downloads/alper_rowlands_1709.09286_source/apolar-syzygies-v9.tex`, lines
172--180, 707--739, and 1024--1047.  Their polynomial ring, apolar action,
standard degree, and \(\beta_{2,3}\) agree with the present definitions.

Since the left Tor map is injective, (1.5), (2.6), and (3.6) give the exact
general Glynn value

\[
 \kappa(\operatorname{perm}_n;\{T_\epsilon\})
   =\delta_n+\rho_n
   =(n+1)\delta_n
   =\frac{n^2(n-1)(n+1)^2}{3}.
 \tag{4.1}
\]

At \(n=7\),

\[
 \delta_7=784,\qquad
 \rho_7=5488,\qquad
 \kappa=6272.
 \tag{4.2}
\]

Equivalently, \(H_{R_G}\) has dimension \(18032\), the right map has kernel
dimension

\[
 18032-5488=12544,
\]

and (1.4) deletes those \(12544\) classes from the \(18816\)-dimensional
permanent space.  Although the pushout keeps all \(784\) quotient-created
classes, it keeps only \(5488\) of the liftable classes.

Therefore

\[
 6272<18523,
 \tag{4.3}
\]

so the canonical Tor-pushout image, and every functorial subquotient of that
image, is incapable of proving rank \(64\).

There is a second, independent obstruction to a degree-uniform theorem that
would assert \(\kappa\le\sum_i\beta_{2,3}(T_i)\).  For the actual small Glynn
decompositions,

\[
 \begin{array}{c|c|c}
 n&\kappa(\operatorname{perm}_n)&
 \sum_\epsilon\beta_{2,3}(T_\epsilon)\\ \hline
 3&96&72\\
 4&400&384.
 \end{array}
 \tag{4.4}
\]

Thus even the hoped-for cap is false for the same canonical construction in
nearby degrees.  This does not alone refute a septic-only inequality, but the
exact \(n=7\) value (4.2) already refutes the required target retention.

## 5. Surviving interface

A successful relative construction cannot factor the target contribution
through

\[
 \operatorname{im}\left[
 \operatorname{Tor}_{2,3}(A_f)\to
 \operatorname{Tor}_{2,3}(D\sqcup_R A_f)
 \right].
\]

It must recover at least \(18523-6272=12251\) of the classes in
\(l(\ker r)\) on the Glynn diagram, while still discarding at least \(1428\)
classes on \(F_2\).  Consequently, merely passing to further images,
kernels, cokernels, associated-graded pieces, or subquotients of the
ordinary module pushout cannot work.  The unresolved object must use extra
multiplicative/apolar-duality data that distinguishes the two kernels before
forming the pushout, rather than the universal property of the module
diagram alone.

## 6. Diagnostic replay

Run

```text
python results/perm7_theory_first_20260822/exact64_syzygy/relative_tor/glynn_pushout_smalln.py
```

The script constructs the common quadratic space, the cubic multiplication
matrix, and the induced maps to every Glynn term.  It checks \(n=3,\ldots,7\)
over the prime `1000003` and independently matches (2.5), (3.6), and (4.1).
The expected final marker is

```text
GLYNN_PUSHOUT_SMALLN_PASS
```

The prime computation is diagnostic only; Sections 2--4 are the
characteristic-zero proof.
