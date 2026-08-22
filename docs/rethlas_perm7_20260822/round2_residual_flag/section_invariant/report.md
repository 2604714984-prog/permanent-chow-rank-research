# Hyperplane sections of `perm_7`: torus reduction, exact apolar data, and the remaining border-63 gate

## Status

This branch does **not** prove or refute

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

It makes the hyperplane-section route substantially more precise:

1. the uniform ordinary section theorem reduces rigorously to the single
   coordinate **border** theorem
   \[
   \underline{\operatorname{ChowRank}}
   (\operatorname{perm}_7|_{x_{77}=0})\ge 63;
   \]
2. the opposite inequality is proved, so the exact missing statement is
   \[
   \boxed{\underline{\operatorname{ChowRank}}
   (\operatorname{perm}_7|_{x_{77}=0})=63;}
   \]
3. every hyperplane section has the same complete derivative Hilbert vector
   \[
   (1,48,441,1225,1225,441,48,1);
   \]
4. the coordinate section has an explicit apolar ideal: the surviving
   permanent quadrics plus one minimal generator in degree six;
5. every standard Koszul--Young flattening has rank-ratio capacity strictly
   below $60$, so that entire determinantal family cannot prove the missing
   border lower bound $63$; and
6. a concrete seven-factor atom has a 12-dimensional quadratic intersection
   with the coordinate section, refuting a verbatim transfer of the existing
   permanent slope-ten certificate (whose corresponding cap is three).

Throughout, $k$ is algebraically closed of characteristic zero.  Let
$V=\langle x_{ij}:1\le i,j\le7\rangle$, let
$P=\operatorname{perm}_7\in\operatorname{Sym}^7V$, and put

\[
E_m=\mathcal D_m(P)
 =\left\langle P_{I,J}:|I|=|J|=m\right\rangle,
\qquad \dim E_m=\binom7m^2.
\]

No external paper theorem is used in the proofs below.  The literature search
found no theorem about the border product rank or the apolar ideal of a
permanent with one entry specialized to zero.

## 1. Closed torus reduction to one coordinate section

For a nonzero $\ell\in V$, write

\[
q_\ell:V\longrightarrow V/\langle\ell\rangle,
\qquad P_\ell=\operatorname{Sym}^7(q_\ell)(P).
\]

### Proposition 1.1 -- closed section locus

For every $r\ge1$, the set

\[
\mathcal B_r=
\left\{[\ell]\in\mathbf P(V):
\underline{\operatorname{ChowRank}}(P_\ell)\le r\right\}
\tag{1.1}
\]

is Zariski closed.

#### Proof

On $B=\mathbf P(V)$, let

\[
0\longrightarrow\mathcal O_B(-1)
\longrightarrow V\otimes\mathcal O_B
\longrightarrow\mathcal Q\longrightarrow0
\tag{1.2}
\]

be the tautological quotient bundle.  The relative Chow variety

\[
\operatorname{Ch}_7(\mathcal Q)
 \subset \mathbf P(\operatorname{Sym}^7\mathcal Q)
\]

is locally, after trivializing $\mathcal Q$, the product of the base with
the usual projective variety of products of seven linear forms in 48
variables.  Its relative $r$-secant is likewise locally the product with
the fixed closed secant variety
$\sigma_r(\operatorname{Ch}_7(k^{48}))$.  Thus it is a closed relative
subvariety;
in particular its fiber is the actual fiberwise border-rank locus, not an
enlargement caused by varying the base.

The image of $P$ in $\operatorname{Sym}^7\mathcal Q$ is nowhere zero.
Indeed, vanishing at $[\ell]$ would mean
$P\in\ell\operatorname{Sym}^6V$, whereas Lemma 2.1 below (with $m=7$)
says that no nonzero element of $E_7=kP$ has a linear divisor.  Hence $P$
defines a
morphism

\[
s_P:B\longrightarrow\mathbf P(\operatorname{Sym}^7\mathcal Q),
\qquad [\ell]\longmapsto[P_\ell].
\]

The set (1.1) is the inverse image of the relative secant under $s_P$, so
it is closed.  $\square$

### Proposition 1.2 -- torus fixed-point reduction

If $\mathcal B_r\ne\varnothing$, then $[x_{ij}]\in\mathcal B_r$ for some
coordinate $x_{ij}$, and therefore $[x_{77}]\in\mathcal B_r$.

#### Proof

The row/column scaling torus

\[
T=(k^*)^7\times(k^*)^7,
\qquad x_{ij}\longmapsto a_i b_jx_{ij},
\tag{1.3}
\]

makes $P$ a semi-invariant of character
$(\prod_i a_i)(\prod_j b_j)$.  Projectively, $P$ is fixed.  The relative
Chow secants are $T$-stable, so Proposition 1.1 makes $\mathcal B_r$ a
closed $T$-stable subset of $\mathbf P(V)$.

Take $[\ell]\in\mathcal B_r$.  The 49 characters $a_i b_j$ occurring in
$V$ are pairwise distinct.  A generic integral one-parameter subgroup of
$T$ assigns distinct weights to the coordinates occurring in $\ell$.
After projective rescaling, its limit as $t\to0$ is the unique
lowest-weight coordinate line $[x_{ij}]$.  Closedness and $T$-stability
put this coordinate point in $\mathcal B_r$.  Independent row and column
permutations preserve $P$ and act transitively on its variables, giving
$[x_{77}]\in\mathcal B_r$.  $\square$

### Corollary 1.3 -- exact reduction for rank 64

If

\[
\underline{\operatorname{ChowRank}}(P|_{x_{77}=0})\ge63,
\tag{1.4}
\]

then $\operatorname{ChowRank}(P_\ell)\ge63$ for every $\ell\ne0$, and
therefore $\operatorname{ChowRank}(P)=64$.

Indeed, if one section had ordinary rank at most 62, it would have border
rank at most 62, so $\mathcal B_{62}\ne\varnothing$; Proposition 1.2 would
contradict (1.4).  In a minimum Chow decomposition of $P$, restriction to
a hyperplane defined by one factor of one atom kills that atom, giving

\[
\operatorname{ChowRank}(P)
\ge1+\min_{\ell\ne0}\operatorname{ChowRank}(P_\ell)\ge64.
\]

Glynn supplies the opposite inequality.

### Proposition 1.4 -- the sharp coordinate upper bound

\[
\underline{\operatorname{ChowRank}}(P|_{x_{77}=0})\le63.
\tag{1.5}
\]

Choose a factor

\[
\ell_G=\sum_{i=1}^7\delta_i x_{i7}
\]

of one normalized Glynn atom.  Exactly one displayed Glynn atom has that
factor, so $P_{\ell_G}$ has an actual 63-term decomposition.  Consequently
$[\ell_G]\in\mathcal B_{63}$.  Scale rows $1,\ldots,6$ by $t$ and row
7 by one.  Projectively,

\[
\lim_{t\to0}
\left[\delta_7x_{77}+t\sum_{i=1}^6\delta_i x_{i7}\right]
=[x_{77}].
\]

Since $\mathcal B_{63}$ is closed, (1.5) follows.  Combining (1.4) and
(1.5), the exact missing coordinate theorem is

\[
\boxed{
\underline{\operatorname{ChowRank}}(P|_{x_{77}=0})=63.}
\tag{1.6}
\]

## 2. No linear divisors in a subpermanent space

Identify variables with edges of $K_{7,7}$.  A degree-$m$ monomial in
an $m$-subpermanent is a matching of size $m$.  For fixed row and column
sets $I,J$, every matching from $I$ to $J$ has the same coefficient in
an element of $E_m$.

### Lemma 2.1

For every $2\le m\le7$ and every nonzero linear form $\ell\in V$,

\[
\boxed{E_m\cap\ell\operatorname{Sym}^{m-1}V=0.}
\tag{2.1}
\]

#### Proof

Suppose $0\ne g=\ell h\in E_m$, and let $S$ be the edge support of
$\ell$.  Fix $e\in S$.  Since every element of $E_m$ is multiaffine,
comparison of the highest power of the variable $x_e$ in $\ell h$
shows that $h$ is independent of $x_e$.  This holds for every
$e\in S$, so no monomial of $h$ uses an edge of $S$.

If a monomial $M$ of $h$ used an edge sharing a row or column with
$e\in S$, then $x_eM$ would be a nonmatching monomial.  It occurs in
$\ell h$ uniquely through $e$, because $M$ contains no edge of $S$,
so it could not cancel.  This contradicts the matching support of $E_m$.
Thus every monomial of $h$ avoids every row and every column incident to
$S$.  The same unique-term argument says that each monomial of $h$ is
itself a matching.

Choose a nonzero monomial coefficient $c_M$ of $h$, an edge
$e=(i,j)\in S$, and, since $m\ge2$, an edge $f=(k,l)\in M$.  The
matching

\[
N=\{e\}\cup M
\]

has nonzero coefficient ([x_N]g=[x_e]\ell\,c_M).  Swap the columns on
(e,f), replacing them by

\[
e'=(i,l),\qquad f'=(k,j).
\]

The new matching $N'$ has the same row and column sets as $N$, so an
element of $E_m$ must give $N'$ the same nonzero coefficient.  But
$l$ is not incident to $S$'s column set and $k$ is not incident to
its row set.  Hence neither $e'$ nor $f'$ lies in $S$; moreover both
touch a row or column incident to $S$, so neither can occur in $h$.
Every monomial of $\ell h$ contains exactly one edge of $S$, while
$N'$ contains none.  Thus its coefficient is zero, a contradiction.
$\square$

## 3. Every hyperplane section has the same derivative profile

### Theorem 3.1

For every nonzero $\ell\in V$,

\[
\boxed{
\left(\dim\mathcal D_m(P_\ell)\right)_{m=0}^7
=(1,48,441,1225,1225,441,48,1).}
\tag{3.1}
\]

For $2\le m\le5$, more precisely,

\[
\mathcal D_m(P_\ell)=q_\ell(E_m)
\quad\text{and}\quad
E_m\xrightarrow{q_\ell}q_\ell(E_m)
\text{ is an isomorphism}.                         \tag{3.2}
\]

#### Proof

Put $W=V/\langle\ell\rangle$.  The section catalecticant is

\[
C_{7-m,m}(P_\ell)
=\operatorname{Sym}^m(q_\ell)\,
 C_{7-m,m}(P)\,
 \operatorname{Sym}^{7-m}(q_\ell^*).                \tag{3.3}
\]

Under the perfect divided-power pairing, the row space of the middle map is
$E_{7-m}$.  The annihilator of
$\operatorname{Sym}^{7-m}(W^*)\subset\operatorname{Sym}^{7-m}(V^*)$
is

\[
\ell\operatorname{Sym}^{6-m}V.
\]

For $2\le m\le5$, Lemma 2.1 in degree $7-m\ge2$ says that restricting
the domain in (3.3) loses no rank.  Its image is therefore all of $E_m$.
Lemma 2.1 in degree $m$ then says that the output quotient is injective on
this image.  This proves (3.2) and the four middle entries of (3.1).

For $m=1$, the same domain argument uses
$E_6\cap\ell\operatorname{Sym}^5V=0$, so before the output quotient the
image is all of $E_1=V$.  Quotienting gives rank 48.  Transposition of the
catalecticant gives the same rank in degree six.  Finally $P_\ell\ne0$ by
Lemma 2.1 in degree seven, so the endpoint dimensions are one.  $\square$

### Corollary 3.2 -- a surviving cubic intersection theorem

Every nonzero element of $\mathcal D_3(P_\ell)$ has at least eight
essential variables.  Consequently, for every degree-seven Chow atom $T$
in $W$,

\[
\mathcal D_3(T)\cap\mathcal D_3(P_\ell)=0.            \tag{3.4}
\]

Indeed, lift a nonzero section cubic uniquely to $g\in E_3$ by (3.2).
Every nonzero $g\in E_3$ has at least nine essential variables: retain a
nonzero three-row/three-column block to obtain a nonzero multiple of
$\operatorname{perm}_3$, whose nine first derivatives are independent.
Restricting the gradient map from $V^*$ to its hyperplane $W^*$ loses at
most one rank, while the output map is injective on $E_2$ by Lemma 2.1.
Thus the section cubic has at least eight essential variables.  Every cubic
in $\mathcal D_3(T)$ uses at most the seven variables in the factor span.

## 4. Exact apolar ideal of the coordinate section

Put

\[
F=P|_{x_{77}=0},
\qquad
S'=k[y_{ij}:(i,j)\ne(7,7)],
\]

where $y_{ij}$ acts by constant-coefficient differentiation.  Let $K$
be the ideal generated by

1. every square and every product using two entries in a common row or a
   common column; and
2. every rectangle relation
   \[
   y_{ij}y_{kl}-y_{il}y_{kj}
   \]
   whose four variables all belong to $S'$.

Let

\[
M_0=y_{11}y_{22}\cdots y_{66}.
\]

### Theorem 4.1

\[
\boxed{F^\perp=K+(M_0).}                              \tag{4.1}
\]

The class of $M_0$ is nonzero modulo $K$, so it is a minimal generator
of degree six.  In particular, $F^\perp$ is generated by its 735 quadrics
and one degree-six element.

#### Proof

Modulo the unacceptable monomials, monomials are matchings avoiding the
edge $(7,7)$.  Rectangle relations connect any two such matchings with the
same row and column sets.  To see connectivity when both sets contain 7,
identify matchings with permutations avoiding the single assignment
$7\mapsto7$.  Transpositions among the other rows first rearrange their
images arbitrarily while preserving avoidance; swapping row 7 with the row
carrying a desired non-7 image changes its image and still avoids
$7\mapsto7$.  Thus the avoidance graph is connected.  All other blocks
are the usual full permutation graph.

Consequently $S'/K$ has one class for every pair of $d$-element row and
column sets for $2\le d\le6$, one class for each of the 48 available
variables in degree one, and one class in degrees zero and seven.  Acting on
$F$, the matching class indexed by $I,J$ gives the same complementary
subpermanent for every representative.  It is nonzero except in degree six
for

\[
I=J=\{1,\ldots,6\},
\]

where it differentiates toward the deleted variable $x_{77}$.  This is
exactly the class of $M_0$.  All other classes act to polynomials with
distinct complementary row/column supports and are independent.

Finally every available variable multiplied by $M_0$ repeats one of its
six rows or one of its six columns, so $(S'/K)_1M_0=0$.  Killing $M_0$
therefore removes exactly this one degree-six class and creates no further
relations.  The resulting Hilbert vector is (3.1), proving (4.1).  $\square$

### Corollary 4.2 -- exact first linear syzygy count

Since the ideal has no linear generators and its degree-three part is
generated by its quadrics,

\[
\begin{aligned}
\dim(F^\perp)_2
 &=\binom{49}{2}-441=735,\\
\dim(F^\perp)_3
 &=\binom{50}{3}-1225=18375,
\end{aligned}
\]

and therefore

\[
\dim\operatorname{Tor}^{S'}_2(S'/F^\perp,k)_3
=48\cdot735-18375
=16905.                                             \tag{4.2}
\]

For comparison, an independent seven-factor atom in 48 variables has 41
inactive linear annihilators and seven active square quadrics, giving 287
such ambient linear syzygies.  Even if the raw Betti number were subadditive
(it is not), its ratio would be

\[
\frac{16905}{287}=\frac{2415}{41}<59.               \tag{4.3}
\]

Thus the coordinate apolar presentation does not supply a hidden scalar
rank-63 certificate.

### Corollary 4.3 -- exact first prolongations and first-Koszul ranks

For a subspace $A_m\subset\operatorname{Sym}^mW$, write

\[
A_m^{(1)}={G\in\operatorname{Sym}^{m+1}W:
\partial_\lambda G\in A_m\text{ for every }\lambda\in W^*\}.
\]

The apolar orthogonal of $\mathcal D_m(F)^{(1)}$ is
$S'_1(F^\perp)_m$.  Theorem 4.1 therefore gives, for $m=1,\ldots,6$,

\[
\left(\dim\mathcal D_m(F)^{(1)}\right)_{m=1}^6
=(1176,1225,1225,441,49,1).                         \tag{4.4}
\]

Indeed, $(F^\perp)_1=0$ gives the full quadratic space of dimension 1176.
For $m=2,3,4$, there is no new generator in degree $m+1$, so the
prolongation equals $\mathcal D_{m+1}(F)$.  In degree six the one new
generator $M_0$ makes the prolongation of $\mathcal D_5(F)$ one dimension
larger than $\mathcal D_6(F)$, namely 49.  There is no new degree-seven
generator, giving the last entry one.

Consequently the $p=1$ Koszul ranks, exact independent-atom caps, and
resulting integer lower-bound ceilings are

\[
\begin{array}{c|rrrrrr}
m&1&2&3&4&5&6\\ \hline
\operatorname{rank}\delta_{m,1}(F)
 &1128&19943&57575&58359&21119&2303\\
B_{m,1}&308&973&1645&1659&1001&335\\
\left\lceil\operatorname{rank}/B_{m,1}\right\rceil
 &4&21&35&36&22&7
\end{array}                                           \tag{4.5}
\]

Thus no exact first-Koszul flattening gets close to the independently known
ordinary lower bound 50.  For larger exterior degree, Section 5 proves the
stronger capacity ceiling 60, but this branch does not compute all of those
target ranks and establishes no standard flattening lower bound above 50.

## 5. Complete standard Koszul--Young capacity gate

For $1\le m\le7$ and $0\le p\le47$, consider the standard map

\[
\delta_{m,p}(f):
\mathcal D_m(f)\otimes\Lambda^pW
\longrightarrow
\mathcal D_{m-1}(f)\otimes\Lambda^{p+1}W.            \tag{5.1}
\]

Equivalently, precompose with the catalecticant on the fixed domain
$\operatorname{Sym}^{7-m}W^*\otimes\Lambda^pW$.  This precomposed
flattening is linear in $f$, has the same image and hence the same rank as
(5.1), and its determinantal rank bound applies to border Chow rank.

### Proposition 5.1 -- exact one-atom cap

Let $B_{m,p}$ be the maximum rank of (5.1) on a seven-factor Chow atom in
48 variables.  For an independent atom, split $W=L\oplus U$ into its
seven-dimensional factor span and 41 inactive variables.  Then

\[
B_{m,p}=\sum_j\binom{41}{j}r_{m,p-j},                \tag{5.2}
\]

where

\[
r_{m,s}=
\sum_{a=0}^{\min(m-1,s)}
\binom7a
\binom{7-a}{m+s-2a}
\binom{m+s-2a-1}{m-a-1}.                             \tag{5.3}
\]

Terms with invalid binomial indices are zero.

To prove (5.3), index an internal basis vector by a squarefree
$m$-subset $M$ and an exterior $s$-subset $A$.  The Koszul map moves
an element of $M\setminus A$ from $M$ into $A$.  It preserves the
intersection $I=M\cap A$ and union $M\cup A$.  For $a=|I|$, the block
on the remaining $m+s-2a$ elements is a simplex boundary map from
$(m-a)$-subsets to $(m-a-1)$-subsets, of rank

\[
\binom{m+s-2a-1}{m-a-1}.
\]

Choosing $I$ and the remaining union gives (5.3), and choosing inactive
wedge variables gives (5.2).  Independent factor tuples form a dense open
set; every dependent tuple is a specialization, so rank
upper-semicontinuity makes (5.2) the maximum over all Chow atoms.

### Theorem 5.2 -- all standard maps stop below 60

For the coordinate section $F$, every standard map satisfies

\[
\frac{\operatorname{rank}\delta_{m,p}(F)}{B_{m,p}}
\le
\frac{
\min\left\{
h_m\binom{48}{p},
h_{m-1}\binom{48}{p+1}
\right\}}
{B_{m,p}}
\le
\frac{7922320}{134133}
<60,                                                   \tag{5.4}
\]

where $h=(1,48,441,1225,1225,441,48,1)$.  Equality in the numerical
capacity maximum occurs only at $(m,p)=(4,23),(4,24)$.  Thus no standard
Koszul--Young flattening can certify even border Chow rank 61, and in
particular none can prove (1.6).

The first inequality is merely the smaller of source and target dimensions;
the second is exact binomial arithmetic using (5.2)--(5.3).  The replay is

```text
python results/perm7_theory_first_20260822/round2_residual_flag/section_invariant/koszul_young_capacity.py
```

and prints `SECTION_KOSZUL_YOUNG_CAPACITY_PASS`.

As a small-(n) control, the same formulas for
$\operatorname{perm}_4|_{x_{44}=0}$ give the first-Koszul target rank 524
and atom cap 86, hence the integer lower bound seven.  A Glynn-factor
section has seven terms, and its torus degeneration gives the coordinate
upper bound seven.  Thus the coordinate-section strategy succeeds exactly
at $n=4$, while at $n=7$ the complete standard family has a strict
capacity shortfall.

## 6. Why the permanent slope certificate does not transfer verbatim

The coordinate quadratic derivative space contains the 36-dimensional
rank-one grid

\[
G_2=
\left\langle x_{i7}x_{7j}:1\le i,j\le6\right\rangle.
\tag{6.1}
\]

Indeed, the two-by-two subpermanent on rows $\{i,7\}$ and columns
$\{j,7\}$ becomes

\[
x_{ij}x_{77}+x_{i7}x_{7j}
\longmapsto x_{i7}x_{7j}.                             \tag{6.2}
\]

Take the legal independent-factor atom

\[
T=x_{17}x_{27}x_{37}x_{71}x_{72}x_{73}x_{74}.        \tag{6.3}
\]

Then

\[
\boxed{
\dim\bigl(\mathcal D_2(T)\cap\mathcal D_2(F)\bigr)=12.}
\tag{6.4}
\]

The 12 cross products $x_{i7}x_{7j}$, $1\le i\le3$, $1\le j\le4$,
lie in both spaces.  The remaining nine squarefree factor pairs either use
two variables from column 7 or two variables from row 7; such monomials
never occur in $\mathcal D_2(F)$, so (6.4) is exact.

For the full permanent, the corresponding universal intersection cap is
three and is an input to the existing slope-ten local rows.  Equation (6.4)
therefore refutes the direct instruction “replace 49 by 48 and reuse the
same slope certificate.”  Notice that the cubic intersection theorem (3.4)
survives.  A repaired section method must exploit that higher-degree fact,
the special bipartite structure of (6.1), or a genuinely coupled invariant;
it must tolerate quadratic defect at least 12.

## 7. Bounded diagnostic and exact blocker

The symbolic proof of Lemma 2.1 was stress-tested by exact modular
elimination.  The diagnostic exhausts all 511 projective hyperplanes over
$\mathbf F_2$ and all 9,841 over $\mathbf F_3$ for $n=3,m=2$, then
tests structured and deterministic random orientations for $n=4,m=2,3$
and $n=7,m=2$.  All 10,426 intersections vanish.  Run

```text
python results/perm7_theory_first_20260822/round2_residual_flag/section_invariant/section_profile_audit.py
```

to obtain `SECTION_PROFILE_AUDIT_PASS`.  This is diagnostic only; Lemma 2.1
is the characteristic-zero proof.

The branch ends at the following sharp interface:

\[
\boxed{
\text{prove or refute }
\underline{\operatorname{ChowRank}}
(\operatorname{perm}_7|_{x_{77}=0})=63.}
\]

The coordinate form has border rank at most 63, exact full central
catalectic ranks, a quadrics-plus-one-sextic apolar ideal, and no standard
Koszul--Young certificate above 60.  No explicit border decomposition with
at most 62 terms and no invariant proving the lower bound 63 was found.
