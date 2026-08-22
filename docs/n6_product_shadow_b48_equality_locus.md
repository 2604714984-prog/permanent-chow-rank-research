# The forty-eight-dimensional product-shadow equality locus

**Status.** PURE_CHARACTERISTIC_ZERO_B48_EQUALITY_LOCUS_CLASSIFICATION,
EXACT_INTEGER_36_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION,
EXACT_RELATIVE_240_BRANCH_REPLAY (N6-076).  The base field is algebraically
closed of characteristic zero.  This is an ordinary linear-subspace theorem,
not a border-rank statement.

Put

\[
 E_3=\langle p_{R,C}:R,C\in\tbinom{[6]}{3}\rangle,
 \qquad
 E_2=\langle p_{I,J}:I,J\in\tbinom{[6]}{2}\rangle.
\]

The product-shadow inequality gives

\[
 \dim\partial S\geq75\qquad(\dim S=48).
\tag{0.1}
\]

## Theorem

If \(S\subset E_3\) satisfies

\[
 \dim S=48,\qquad \dim\partial S=75,
\tag{0.2}
\]

then there is a fifty-plane \(T\supset S\) such that

\[
 \dim\partial T=75,\qquad \partial S=\partial T.
\tag{0.3}
\]

Consequently N6-064 applies to \(T\).  For \(K=\partial S\),

\[
 \boxed{\dim\partial K=23,}
\tag{0.4}
\]

and \(\partial K\) is a genuine projective flag hook, in one orientation or
the other.

## 1. The eight original row-degree profiles

Let

\[
 \mathcal A\subset
 \binom{[6]}{3}\times\binom{[6]}{3},
 \qquad |\mathcal A|=48,
 \qquad |\partial_\times\mathcal A|=75,
\]

be a coordinate equality support.  Write

\[
 B_R=\{C:(R,C)\in\mathcal A\},\qquad d_R=|B_R|,
\]

and, for a row pair \(I\), put

\[
 U_I=\bigcup_{R\supset I}\partial B_R.
\tag{1.1}
\]

Then

\[
 |\partial_\times\mathcal A|=\sum_I|U_I|.
\tag{1.2}
\]

As in N6-062A and N6-073, the two product colex compressions preserve the
decreasing original row-degree profile.  The exact Ferrers dynamic program
has minimum 75 and precisely the following eight minimizers:

\[
\begin{array}{c|c}
\text{row-oriented}&\text{transpose-oriented}\\ \hline
(18,10,10,10,0^{16})&(4^9,2,1^{10})\\
(19,10,10,9,0^{16})&(4^8,3^2,1^{10})\\
(20,10,10,8,0^{16})&(4^9,3,1^9,0)\\
(20,10,9,9,0^{16})&(4^{10},1^8,0^2).
\end{array}
\tag{1.3}
\]

The rest of this section works in the original support.  Thus the argument
does not reverse a compression and does not assume the extension theorem it
is proving.

### 1.1 The four row-oriented profiles

Let \(\mathcal F\) be the four active row labels and let \(R_*\) be the
row of degree at least 18.  A family of 18, 19 or 20 triples on six vertices
has all fifteen pairs in its shadow: each pair has four cubic lifts, while at
most two triples are absent.  Hence the three pairs of \(R_*\) contribute
15 each to (1.2).

Every pair in
\(\partial\mathcal F\setminus\binom{R_*}{2}\) lies below a fiber of size at
least eight, whose pair shadow has size at least ten.  Four triples have at
least six pairs in their shadow, so

\[
 75
 =|\partial_\times\mathcal A|
 \geq45+10\left(|\partial\mathcal F|-3\right)
 \geq75.
\tag{1.4}
\]

Equality holds throughout.  Thus
\(|\partial\mathcal F|=6\), and the four row labels are

\[
 \mathcal F=\binom{U_4}{3}.
\tag{1.5}
\]

The three pairs in
\(\partial\mathcal F\setminus\binom{R_*}{2}\) form a triangle on the three
non-distinguished rows.  Along every edge, the union of the two column
shadows has size ten, while either shadow has size at least ten.  The three
shadows therefore coincide with one ten-set \(Q\).

The exact one-factor equality classification says that every family of
eight, nine or ten triples with ten-pair shadow is respectively

\[
 \binom{V_5}{3}\setminus\{2,1,0\text{ triples}\},
 \qquad Q=\binom{V_5}{2}.
\tag{1.6}
\]

Thus the four profiles in the left column of (1.3) are exactly the following
two-cell deletions from a row hook:

\[
\begin{array}{c|c}
\text{profile}&\text{deleted fiber cells}\\ \hline
(18,10,10,10)&2\text{ in the full row}\\
(19,10,10,9)&1\text{ full-row and }1\text{ ordinary-row cell}\\
(20,10,10,8)&2\text{ in one ordinary row}\\
(20,10,9,9)&1\text{ in each of two ordinary rows}.
\end{array}
\tag{1.7}
\]

### 1.2 The four transpose-oriented profiles

First consider the last three profiles in the right column of (1.3).  Let
\(\mathcal H\) be the ten rows of degree at least three and set
\(D=\partial\mathcal H\).  The active row-label family has size 18, 19 or 20,
so its shadow is all fifteen row pairs.  For \(I\in D\), a high fiber gives
\(|U_I|\geq6\); outside \(D\), a nonempty singleton fiber gives
\(|U_I|\geq3\).  Since ten triples have at least ten pairs,

\[
 75\geq6|D|+3(15-|D|)=45+3|D|\geq75.
\tag{1.8}
\]

Equality forces

\[
 |D|=10,\qquad \mathcal H=\binom{V_5}{3}.
\tag{1.9}
\]

For the exceptional profile \((4^9,2,1^{10})\), let
\(\mathcal H_3\) be the nine degree-four rows.  The same estimate applies to
\(D=\partial\mathcal H_3\); equality and the nine-triple equality
classification give

\[
 \mathcal H_3=\binom{V_5}{3}\setminus\{H_*\}.
\tag{1.10}
\]

If the degree-two row were outside \(\binom{V_5}{3}\), it would contain two
outer pairs.  Its two-element fiber has at least five column pairs in its
shadow.  Hence \(U_I\), even after any further low singleton contributions,
would have size at least five, contradicting its equality value three at
either outer pair.  The row is therefore \(H_*\), so the ten top labels form
\(\binom{V_5}{3}\).

At an inner pair, equality gives \(|U_I|=6\).  In the three
non-exceptional profiles, every high fiber has size at least three and hence
shadow size at least six.  Connectivity of the Johnson graph on
\(\binom{V_5}{3}\) therefore makes all their shadows coincide with

\[
 Q=\binom{W_4}{2}.
\tag{1.11}
\]

In the exceptional profile, the Johnson graph on the nine degree-four rows,
namely the same graph with the vertex \(H_*\) deleted, is connected.  Their
shadows first synchronize to the same \(Q\).  Each pair of \(H_*\) is also
contained in a degree-four row; the equality \(|U_I|=6\) then forces the
degree-two fiber shadow to be contained in \(Q\).

Thus every high fiber of size four, three or two is contained in
\(\binom{W_4}{3}\) and has precisely the indicated one- or two-cell
deletions.  Indeed, every triple in such a fiber has all three pairs in
\(Q=\binom{W_4}{2}\), which forces the triple itself to lie in \(W_4\).

The remaining row labels are
\(\{\infty\}\cup e\), \(e\in\binom{V_5}{2}\), with zero, one or two of these
low rows inactive.  At an outer pair \(\{\infty,v\}\), equality gives a
three-dimensional union of singleton-fiber shadows.  Thus all active
singleton fibers incident to \(v\) are equal.  The line graph of \(K_5\)
remains connected after deleting at most two edges, so every active low
fiber is the same singleton \(\{C_*\}\).  At the inner pair \(e\), (1.11)
forces

\[
 \partial C_*\subset Q,\qquad C_*\subset W_4.
\tag{1.12}
\]

This proves that the four right-column profiles are respectively the
same-high-row, distinct-high-row, high-low and low-low two-cell deletions
from a transpose hook.

The replay exhausts only the finite one-factor equality families used above:

\[
\begin{array}{c|c|c}
\text{family size}&\text{shadow size}&\text{count}\\ \hline
3&6&60\\
4&6&15\\
8&10&270\\
9&10&60\\
10&10&6.
\end{array}
\tag{1.13}
\]

It verifies their claimed clique-deletion forms.  Equations (1.4)--(1.12),
not an enumeration of \(\binom{400}{48}\) supports, prove the
original-support classification.

## 2. Labelled supports, uniqueness and the 36 fixed types

There are

\[
 2\binom{6}{4}\binom{4}{3}\binom{6}{5}=720
\tag{2.1}
\]

labelled fifty-hooks.  Every quadratic shadow coordinate of a hook has at
least four cubic lifts, so deleting any two cells preserves all 75 shadow
coordinates.

For a coordinate hook shadow \(K_0\), define

\[
 P_E(K_0)=\{f\in E_3:\partial f\subset K_0\}.
\tag{2.2}
\]

The replay checks all 400 cubic weights and finds exactly the fifty parent
weights.  Since \(K_0\) is stable under the row-column torus, so is
\(P_E(K_0)\).  The cubic torus weights are one-dimensional and mutually
distinct; hence

\[
 \boxed{P_E(K_0)=T_0.}
\tag{2.3}
\]

The parent is therefore unique.  Consequently the labelled support count is

\[
 720\binom{50}{2}=\boxed{882{,}000}.
\tag{2.4}
\]

For a standard row hook, write \(A\) for the twenty cells in its full row
and \(B\) for the thirty cells in its three ordinary rows.  For a standard
transpose hook, write \(H\) and \(L\) for its high and low rows.  The exact
stabilizer-orbit summary is

\[
\begin{array}{c|c|r|r|r}
\text{orientation}&\text{deletion type}&
\text{pairs/parent}&\text{orbits}&\text{labelled supports}\\ \hline
\text{row}&AA&190&7&68{,}400\\
\text{row}&AB&600&6&216{,}000\\
\text{row}&BB\text{, same ordinary row}&135&2&48{,}600\\
\text{row}&BB\text{, distinct ordinary rows}&300&3&108{,}000\\
\text{transpose}&HH\text{, same high row}&60&2&21{,}600\\
\text{transpose}&HH\text{, distinct high rows}&720&8&259{,}200\\
\text{transpose}&HL&400&6&144{,}000\\
\text{transpose}&LL&45&2&16{,}200.
\end{array}
\tag{2.5}
\]

Thus there are \(18+18=36\) stabilizer orbits.  The JSON certificate records
all 36 representatives, their two deleted cells and their orbit sizes; the
sizes sum to \(1225\) in each orientation.  The eight profile orbit counts,
in the order displayed in (1.3), are

\[
 7,\ 6,\ 2,\ 3;\qquad 2,\ 8,\ 6,\ 2.
\tag{2.6}
\]

## 3. Exact local linear and quadratic elimination

Let \(S_0\) be any of the 36 representatives, let \(T_0\) be its parent and
let \(K_0=\partial S_0=\partial T_0\).  Use the incidence of a 75-plane
\(K\subset E_2\) with \(\partial S\subset K\).  The universal lower bound
(0.1) makes \(K=\partial S\) unique on the rank-at-most-75 locus.

In graph coordinates

\[
 t:S_0\longrightarrow E_3/S_0,\qquad
 \eta:K_0\longrightarrow E_2/K_0,
\]

the equations are

\[
 qD(t)-\eta P_0-\eta pD(t)=0.
\tag{3.1}
\]

The linear part consists of integer variable equalities and grounded
variables.  Exact connected-component elimination gives, for every one of
the 36 orbits,

\[
 \dim T_{(S_0,K_0)}=112=16+96.
\tag{3.2}
\]

The first summand is the complete N6-064 parent linear incidence tangent.
The second is

\[
 \operatorname{Hom}(S_0,T_0/S_0),\qquad 48(50-48)=96,
\tag{3.3}
\]

the tangent to \(\operatorname{Gr}(48,T_0)\).  The two coordinate sets are
disjoint, their combined Jacobian has rank 112, and there is no free
\(\eta\)-only component.

After eliminating the transverse variables, write the completed local ring
as

\[
 k[[h_1,\ldots,h_{96},x_1,\ldots,x_{16}]]/I.
\]

The \(x\)'s split into the four N6-064 Boolean groups of sizes
\(3,4,4,5\).  Let

\[
 J=\sum_G(x_ax_b:a<b,\ a,b\in G),
\tag{3.4}
\]

the ideal of their 25 within-group squarefree products.  Substituting the
linear free-variable solution into the grounded equations gives only twice
one forbidden monomial in each nonzero row.  All 25 occur, no non-\(J\)
monomial occurs, and no monomial contains an \(h\)-variable.  Division by
two over \(\mathbb Q\) gives the exact unit row span.  The 36 orbit
certificates have three redundant-row signatures:

\[
\begin{array}{c|r|r|r}
\text{orbits}&\text{grounded equations}&\text{nonzero rows}&
\text{quadratic rank}\\ \hline
4&111{,}936&1{,}104&25\\
12&111{,}960&1{,}098&25\\
20&111{,}984&1{,}092&25.
\end{array}
\tag{3.5}
\]

Therefore

\[
 J\subset\operatorname{in}_{\mathfrak m}(I).
\tag{3.6}
\]

No finite-field rank is used in this characteristic-zero certificate.

## 4. The relative branches and complete formal germ

Let \(\mathcal T\) be the tautological rank-fifty bundle on one of the 240
exact N6-064 Boolean branches.  The relative Grassmannian

\[
 \operatorname{Gr}(48,\mathcal T)
\tag{4.1}
\]

is smooth of relative dimension 96.  Containment in the N6-076 incidence is
tautological: \(S\subset T\) and the all-order N6-064 identity
\(\partial T\subset K\) imply \(\partial S\subset K\).

N6-064 supplies the exact \(4\times4\) identity Jacobian in the Boolean
parameters.  The Grassmann chart supplies a \(96\times96\) identity, and the
present 36-orbit replay checks that their free coordinate sets are disjoint.
Every relative branch is therefore smooth of dimension

\[
 4+96=100.
\tag{4.2}
\]

Its tangent prime chooses one variable from each Boolean group and leaves
all 96 relative variables free.  The 240 primes are precisely the facets of
\(J\).  The exact branches and (3.6) give the initial sandwich

\[
 \operatorname{in}_{\mathfrak m}(I)
 =J\,k[h_1,\ldots,h_{96},x_1,\ldots,x_{16}].
\tag{4.3}
\]

Let \(I_B\) be the closed ideal of the union of the 240 relative branches.
We use

\[
 \operatorname{in}(I_B)
 \subseteq\bigcap_P\operatorname{in}I(B_P)=J,
\]

not an invalid commutation of initial ideals and intersections.  Since
\(I\subset I_B\), (4.3) gives equal filtered initial ideals.  Repeatedly
matching and subtracting lowest homogeneous forms converges in the complete
local ring, so the nested closed ideals are equal:

\[
 \boxed{I=I_B.}
\tag{4.4}
\]

Thus this is a complete formal-germ classification, not merely a tangent
dimension or reduced tangent-cone calculation.

## 5. Proper torus globalization

Let \(X_{48}\subset\operatorname{Gr}(48,E_3)\) be the rank-at-most-75 locus
and let \(X_{50}\) be the N6-064 equality locus.  Form

\[
 Z=\{(S,T):S\subset T,\ \dim S=48,\ T\in X_{50}\}.
\tag{5.1}
\]

This relative Grassmannian is projective, so its image
\(Y\subset\operatorname{Gr}(48,E_3)\) is closed.

The connected row-column torus preserves every irreducible component of
\(X_{48}\), and every such projective component contains a torus fixed
point.  The fixed Grassmannian points are coordinate subspaces.  Sections 1
and 2 classify all of them, and the 36-orbit calculation plus (4.4) says that
their complete formal germs lie in \(Y\).  Hence each irreducible component
contains a nonempty local open subset in \(Y\); closedness forces the entire
component into \(Y\).  Therefore

\[
 \boxed{X_{48}=Y.}
\tag{5.2}
\]

This is a proper component argument, not reversal of a one-parameter torus
specialization.  For the resulting \(S\subset T\), the universal lower bound
and

\[
 \partial S\subset\partial T,\qquad\dim\partial T=75
\]

force \(\partial S=\partial T\).  N6-064 now gives (0.4) and the projective
flag-hook description of the second shadow.

## 6. Replay and boundary

    python scripts/n6_product_shadow_b48_equality_locus.py \
      --json data/n6_product_shadow_b48_equality_locus.json
    python -m unittest tests.test_n6_product_shadow_b48_equality_locus -v

N6-076 does not treat the dimension-47 equality locus.  It does not by
itself prove ordinary Chow rank at least 29, and it makes no claim about
border Chow rank.
