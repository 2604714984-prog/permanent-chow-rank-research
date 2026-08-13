# The forty-six-dimensional product-shadow equality locus

**Status.** `PURE_CHARACTERISTIC_ZERO_B46_EQUALITY_LOCUS_CLASSIFICATION`,
`EXACT_INTEGER_FOUR_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION`,
`EXACT_SYMBOLIC_STABILIZER_ORBIT_BRANCH_REPLAY` (N6-101).  The base field is
algebraically closed of characteristic zero.

Let \(E_3\) and \(E_2\) be the permanent cubic and quadratic coordinate
spaces.  N6-056 gives

\[
 S\subset E_3,\quad \dim S=46
 \quad\Longrightarrow\quad \dim\partial S\ge72.
\tag{0.1}
\]

This note classifies the equality locus.  If equality holds and
\(K=\partial S\), then

\[
 \boxed{\dim\partial K=23}.                                  \tag{0.2}
\]

Moreover, \(\partial K\) is a genuine projective member of one of the
following two flag families, or of a row-column transpose:

\[
 R_4\otimes C_5+R_3\otimes C_6,
 \qquad R_3\subset R_4,                                      \tag{0.3}
\]

or

\[
 R_4\otimes C_5+R_5\otimes C_3,
 \qquad R_4\subset R_5,\quad C_3\subset C_5.                 \tag{0.4}
\]

The second family is called the **biflag rectangle hook** below.  It is not
the standard N6-064 flag hook, so the distinction in (0.3)--(0.4) is
essential.

## 1. The four original coordinate supports

Let

\[
 \mathcal A\subset\binom{[6]}3\times\binom{[6]}3,
 \qquad |\mathcal A|=46,
 \qquad |\partial_\times\mathcal A|=72.                      \tag{1.1}
\]

Write \(B_R=\{C:(R,C)\in\mathcal A\}\), and for a row pair \(I\) put

\[
 U_I=\bigcup_{R\supset I}\partial B_R.
\]

Then \( |\partial_\times\mathcal A|=\sum_I|U_I| \).  The two
product-colex compressions preserve the decreasing original row-degree
profile.  The exact Ferrers program has precisely four minimizers:

\[
\begin{aligned}
 &(16,10,10,10),\qquad (10^4,1^6),\\
 &(10,4^9),\qquad (4^{10},1^6),
\end{aligned}                                                \tag{1.2}
\]

with zeros appended.  The last two are the transpose profiles of the first
two.  The proof now works in the original support; it does not reverse a
compression.

### 1.1 The profile \((16,10,10,10)\)

Let \(R_*\) be the distinguished row and let \(\mathcal F\) be the four
active row labels.  A sixteen-triple family has at least fourteen pairs in
its shadow, and a ten-triple family has at least ten.  The three pairs below
\(R_*\) therefore contribute at least \(3\cdot14\).  Every pair in
\(\partial\mathcal F\setminus\partial R_*\) lies below an ordinary fiber and
contributes at least ten.  Since four triples have at least six pairs,

\[
 72\ge42+10\bigl(|\partial\mathcal F|-3\bigr)\ge72.           \tag{1.3}
\]

Equality holds throughout.  Thus

\[
 \mathcal F=\binom{U_4}{3}.                                  \tag{1.4}
\]

The three pairs outside \(R_*\) form a triangle on the three ordinary
fibers.  Equality on every edge makes their ten-pair shadows identical.
The exact one-factor equality theorem gives

\[
 B_R=\binom{V_5}{3}\quad(R\ne R_*),
 \qquad Q=\partial B_R=\binom{V_5}{2}.                       \tag{1.5}
\]

The distinguished fiber has size sixteen and shadow fourteen.  The exact
one-factor replay says that its complement consists of all four triples
containing one fixed pair \(\{x,y\}\).  Equality on the other three edges
requires \(Q\subset\partial B_{R_*}\), so exactly one of \(x,y\) lies outside
\(V_5\).  Writing \(V_4=V_5\setminus\{y\}\),

\[
 B_{R_*}=\{C:|C\cap V_4|\ge2\}.                              \tag{1.6}
\]

Thus this support is determined by the two coordinate flags

\[
 R_3\subset R_4,\qquad C_4\subset C_5.                       \tag{1.7}
\]

There are \(60\cdot30=1800\) labelled supports.

### 1.2 The profile \((10^4,1^6)\)

Let \(\mathcal H\) be the four high rows, \(\mathcal F\) all ten active
rows, and \(D=\partial\mathcal H\).  High fibers contribute at least ten,
while a nonempty singleton contributes three.  Hence

\[
 72\ge10|D|+3\bigl(|\partial\mathcal F|-|D|\bigr)
    =3|\partial\mathcal F|+7|D|\ge72.                        \tag{1.8}
\]

Equality gives

\[
 \mathcal H=\binom{U_4}{3},
 \qquad \mathcal F=\binom{U_5}{3}.                           \tag{1.9}
\]

Connectivity of the four high rows synchronizes their fibers to one
\(\binom{V_5}{3}\).  The six low rows are indexed by the edges of \(U_4\).
At each outer row pair the three incident singleton shadows have union of
size three, so the line graph of \(K_4\) makes all six singleton fibers equal
to one \(\{C_3\}\).  At an inner pair their shadow is contained in
\(\binom{V_5}{2}\), whence \(C_3\subset V_5\).  This support is determined by

\[
 R_4\subset R_5,\qquad C_3\subset C_5,                       \tag{1.10}
\]

and again there are \(30\cdot60=1800\) labelled supports.

Transposition supplies the other two profiles.  Consequently there are

\[
 \boxed{7200}
\]

coordinate fixed points, in four row-column symmetry orbits.  The script
also replays the one-factor counts

\[
 (|B|,|\partial B|)=(4,6),(10,10),(16,14)
 \quad\longmapsto\quad15,6,15
\]

and checks their asserted clique or fixed-pair forms.

## 2. Exact local initial ideals

Work in the closed projective incidence

\[
 X_{46}=\{(S,K):S\in\operatorname{Gr}(46,E_3),
 K\in\operatorname{Gr}(72,E_2),\ \partial S\subset K\}.      \tag{2.1}
\]

At one representative of each of the four coordinate orbits, exact integer
connected-component elimination of the full linearized incidence gives

\[
 \dim T_{(S,K)}X_{46}=20,\qquad\text{no eta-only root}.       \tag{2.2}
\]

The twenty variables are elementary row or column replacement weights.
After all linear equations have been eliminated, every nonzero grounded
quadratic equation is exactly twice one squarefree monomial.  The resulting
radical graph edge ideals have respectively

\[
 31,\ 32,\ 32,\ 31                                          \tag{2.3}
\]

edge generators.  Every maximal independent set has size five.  Their
counts are

\[
 960,\ 900,\ 900,\ 960.                                     \tag{2.4}
\]

Thus the reduced quadratic initial support is pure five-dimensional.

## 3. All exact five-parameter branches

For every maximal independent facet, apply the five corresponding Boolean
row or column replacements in dependency order: if \(a\to b\) and
\(b\to c\) both occur, apply \(a\to b\) first.  The script verifies
symbolically, with integer polynomial coefficients, both containments

\[
 \partial G_3(S)\subset G_2(K),
 \qquad \partial G_2(K)\subset G_1(M),                       \tag{3.1}
\]

where \(M=\partial K\) at the coordinate point.  It also checks an exact
\(5\times5\) identity Jacobian.  The coordinate stabilizer has order 288;
checking its 21, 18, 18 and 21 facet-orbit representatives transports (3.1)
to all 3720 facets.

Let \(J\) be the graph edge ideal in the twenty completed linear variables.
The grounded equations give

\[
 J\subset\operatorname{in}_{\mathfrak m}I.
\]

The actual five-parameter branches give the reverse inclusion into the
intersection of the facet primes, which equals \(J\) because \(J\) is
radical.  The complete filtered lifting used in N6-064, N6-073 and N6-076
therefore identifies the completed local ideal scheme-theoretically with
the intersection of the branch ideals.  No hidden embedded or nilpotent
local component remains.

## 4. The second shadow

The exact product-shadow minimum for a 72-plane in \(E_2\) is 23.  At the
four coordinate points the second shadows are, respectively, the supports
of (0.3), (0.4), the transpose of (0.4), and the transpose of (0.3).

On every branch, (3.1) puts the second shadow inside the corresponding
23-plane \(G_1(M)\).  The degree-one replacements are genuine invertible
linear shears, so \(G_1(M)\) remains a genuine member of the appropriate
projective flag family.  The universal lower bound 23 forces equality.

Let \(Y\subset X_{46}\) be the projective closed incidence where
\(\partial K\) is contained in a member of one of the four families.  Every
irreducible component of the torus-stable projective scheme \(X_{46}\)
contains a coordinate fixed point.  Sections 2--3 put the full formal germ
there inside \(Y\).  Faithful flatness of completion gives a Zariski
neighborhood in \(Y\), and closedness then puts the entire component in
\(Y\).  This proves (0.2)--(0.4).

## 5. Boundary and replay

N6-101 treats only the exact \(46\to72\) equality locus.  In particular,
the biflag family (0.4) must not be silently replaced by the standard
N6-064 hook.  This theorem does not classify first-shadow dimensions
73--75, does not by itself exclude the critical six-term packet, does not
prove ordinary Chow rank at least 29, and makes no border-rank claim.

```text
python scripts/n6_product_shadow_b46_equality_locus.py \
  --verify-json data/n6_product_shadow_b46_equality_locus.json
python -m unittest tests.test_n6_product_shadow_b46_equality_locus -v
```
