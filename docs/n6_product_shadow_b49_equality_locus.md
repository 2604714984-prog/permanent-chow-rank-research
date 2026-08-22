# The forty-nine-dimensional product-shadow equality locus

**Status.** `PURE_CHARACTERISTIC_ZERO_B49_EQUALITY_LOCUS_CLASSIFICATION`,
`EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION`,
`EXACT_RELATIVE_240_BRANCH_REPLAY` (N6-073).  The base field is algebraically
closed of characteristic zero.  This theorem concerns ordinary linear
subspaces of the permanent derivative spaces; it makes no border-rank claim.

Put

\[
 E_3=\langle p_{R,C}:R,C\in\tbinom{[6]}{3}\rangle,
 \qquad
 E_2=\langle p_{I,J}:I,J\in\tbinom{[6]}{2}\rangle .
\]

The product-shadow inequality gives

\[
 \dim\partial S\geq75\qquad(\dim S=49).
\tag{0.1}
\]

N6-073 proves the following extension theorem.

## Theorem

If \(S\subset E_3\) has

\[
 \dim S=49,\qquad \dim\partial S=75,
\tag{0.2}
\]

then there is a fifty-plane \(T\supset S\) with

\[
 \dim\partial T=75,\qquad \partial S=\partial T.
\tag{0.3}
\]

Consequently N6-064 applies to \(T\): if \(K=\partial S\), then

\[
 \dim\partial K=23,
\tag{0.4}
\]

and \(\partial K\) is a genuine projective flag hook, in one orientation or
the other.

## 1. Coordinate fixed points

For a coordinate support

\[
 \mathcal A\subset\binom{[6]}{3}\times\binom{[6]}{3},
 \qquad |\mathcal A|=49,
\]

the two product colex compressions used in N6-056 preserve the decreasing
row-degree profile.  The exact Ferrers dynamic program has minimum 75 and
exactly four minimizing profiles:

\[
 \begin{split}
 &(20,10,10,9,0^{16}),\qquad(19,10,10,10,0^{16}),\\
 &(4^{10},1^9,0),\qquad(4^9,3,1^{10}).
 \end{split}
\tag{1.1}
\]

Equality is traced in the original, uncompressed support; no compression is
reversed without its equality conditions.

For either of the first two profiles, let \(\mathcal F\) be the four active
row labels and let \(R_*\) be the distinguished row of degree 19 or 20.  The
three pairs in \(\binom{R_*}{2}\) each see the column shadow of that fiber,
which has size 15.  Every pair in
\(\partial\mathcal F\setminus\binom{R_*}{2}\) sees a fiber of size 9 or 10,
whose column shadow has size at least 10.  Since four triples have at least
six pairs in their shadow,

\[
 |\partial_\times\mathcal A|
 \geq45+10\left(|\partial\mathcal F|-3\right)\geq75.
\tag{1.2}
\]

Equality forces \(|\partial\mathcal F|=6\), and the one-factor equality
classification gives
\(\mathcal F=\binom{U}{3}\) for a four-set \(U\).  The three new pairs in
\(\partial\mathcal F\setminus\binom{R_*}{2}\) each lie below two of the three
non-distinguished fibers.  Their incidences form a triangle on those fibers.
At each edge the union of the two column shadows has size 10, while either
shadow has size at least 10; hence the two shadows coincide.  The triangle
makes all three non-distinguished column shadows the same
\(\binom{V}{2}\), where \(|V|=5\).  The one-factor equality classifications
used here are

\[
 \begin{array}{c|c|c}
 \text{family size}&\text{shadow size}&\text{families}\cr
 9&10&\binom{V}{3}\text{ with one triple deleted}\cr
 10&10&\binom{V}{3}\cr
 19&15&\binom{[6]}{3}\text{ with one triple deleted}.
 \end{array}
\tag{1.3}
\]

Thus these two profiles are obtained by deleting one cell from a row-oriented
fifty-cell hook.

For either of the last two profiles, let \(\mathcal H\) be the ten rows of
degree at least three, let \(\mathcal L\) be the singleton rows, and put
\(D=\partial\mathcal H\).  The active row labels comprise nineteen or twenty
of the twenty triples, so

\[
 \partial\mathcal H\cup\partial\mathcal L=\binom{[6]}{2}.
\]

Every pair in \(D\) contributes at least six column pairs and every pair
outside \(D\) contributes at least three.  Hence

\[
 |\partial_\times\mathcal A|
 \geq6|D|+3(15-|D|)=45+3|D|\geq75.
\tag{1.4}
\]

Equality forces \(|D|=10\) and
\(\mathcal H=\binom{U}{3}\) for a five-set \(U\).  Connectivity of the Johnson
graph makes all high-row shadows one common six-set \(\binom{V}{2}\), with
\(|V|=4\).  The needed one-factor classifications are that four triples with
shadow six form \(\binom{V}{3}\), while three triples with shadow six are that
four-triple family with one member deleted.  Connectivity of the line graph
of \(K_5\), still connected after one row label is omitted, makes all
singleton fibers one triple contained in \(V\).  These are exactly the
one-cell deletions from transposed hooks.

The finite replay enumerates the small one-factor families in (1.3) and its
transposed analogue and checks their asserted clique or one-deletion forms.
This is the finite part supporting the equality argument above; it is not an
enumeration of all \(\binom{400}{49}\) supports.  It then generates all
labelled parents:

\[
 2\binom{6}{4}\binom{4}{3}\binom{6}{5}=720.
\]

Deleting one of fifty cells produces 36,000 distinct supports, every one
with shadow 75 and every one with a unique coordinate parent.  The counts by
profile are

\[
\begin{array}{c|r}
(20,10,10,9)&10{,}800\\
(19,10,10,10)&7{,}200\\
(4^9,3,1^{10})&14{,}400\\
(4^{10},1^9,0)&3{,}600.
\end{array}
\tag{1.5}
\]

For later use, define the cubic prolongation of the coordinate shadow by

\[
 P_E(K_0)=\{f\in E_3:\partial f\subset K_0\}.
\tag{1.6}
\]

The replay checks all 400 coordinate weights and finds exactly the fifty
weights of \(T_0\).  This also proves the assertion for arbitrary vectors:
\(K_0\) is stable under the row-column torus, hence \(P_E(K_0)\) is torus
stable, and the 400 cubic weight spaces are one-dimensional with mutually
distinct weights.  Therefore \(P_E(K_0)\) is the coordinate span of those
fifty weights and

\[
 \boxed{P_E(K_0)=T_0.}
\tag{1.7}
\]

## 2. The exact linear incidence tangent

Let \(S_0\) be one of the four coordinate representatives, \(T_0\) its
unique coordinate fifty-hook parent, and \(K_0=\partial S_0=\partial T_0\).
Use the incidence of a 75-plane \(K\subset E_2\) with
\(\partial S\subset K\).  Since (0.1) is a universal lower bound, a
rank-at-most-75 point has rank exactly 75 and \(K=\partial S\) is unique.
An invertible 75-minor therefore identifies the incidence and the
rank-at-most-75 locus formally near \(S_0\).

In Grassmann graph coordinates

\[
 t:S_0\longrightarrow E_3/S_0,
 \qquad \eta:K_0\longrightarrow E_2/K_0,
\]

the equations are the same bilinear incidence equations as in N6-064:

\[
 qD(t)-\eta P_0-\eta pD(t)=0.
\tag{2.1}
\]

The linear coefficients are equalities between one \(t\)-variable and one
\(\eta\)-variable, grounded variables, or zero.  Exact integer
connected-component elimination gives, for every representative,

\[
 \dim T_{(S_0,K_0)}=65=16+49.
\tag{2.2}
\]

The sixteen directions are precisely the full N6-064 linear incidence
tangent at \((T_0,K_0)\).  The other 49 are

\[
 \operatorname{Hom}(S_0,T_0/S_0),
\]

the tangent to \(\operatorname{Gr}(49,T_0)\cong\mathbf P^{49}\).  There is no
free \(\eta\)-only component.  The differential from the full parent
incidence tangent plus the relative hyperplane tangent has rank 65.

## 3. Quadratic initial forms

After eliminating every transverse variable by the formal implicit-function
theorem, write the completed local ring as

\[
 k[[h_1,\ldots,h_{49},x_1,\ldots,x_{16}]]/I.
\]

The \(h\)'s are the relative hyperplane variables.  The \(x\)'s split into
the four N6-064 Boolean groups of sizes

\[
 3,\quad4,\quad4,\quad5.
\]

Let

\[
 J=\sum_{G}(x_ax_b:a<b,\ a,b\in G).
\tag{3.1}
\]

There are 25 generators.  In equations whose complete linear part is zero,
the order-two contribution is obtained by substituting the linear solution
into \(-\eta pD(t)\).  The exact integer replay gives:

\[
\begin{array}{c|r|r}
\text{profile}&\text{grounded equations}&\text{nonzero quadratic rows}\cr
(19,10,10,10)&114{,}288&1{,}122\\
(20,10,10,9)&114{,}312&1{,}116\\
(4^9,3,1^{10})&114{,}288&1{,}122\\
(4^{10},1^9,0)&114{,}312&1{,}116.
\end{array}
\tag{3.2}
\]

Every nonzero row is twice one forbidden monomial.  All 25 forbidden
monomials occur, no non-\(J\) monomial occurs, and no monomial contains an
\(h\)-variable.  Division by two over \(\mathbb Q\) gives the exact 25 unit
vectors as reduced row space.  No modular rank inference is used.  Therefore

\[
 J\subset\operatorname{in}_{\mathfrak m}(I).
\tag{3.3}
\]

## 4. Relative Boolean branches and the formal germ

Let \(\mathcal T\) be the tautological rank-fifty bundle on an exact N6-064
Boolean family.  Each of the 240 families carries the projective bundle

\[
 \mathbf P(\mathcal T^*)=\operatorname{Gr}(49,\mathcal T).
\tag{4.1}
\]

Containment in the N6-073 incidence holds to all orders tautologically:
\(S\subset T\) and the exact N6-064 identity
\(\partial T\subset K\) imply \(\partial S\subset K\).  The script does not
claim to recheck this all-order polynomial identity independently; it checks
the relative chart Jacobians.  The projective bundle is a smooth
53-dimensional family at \(S_0\): four Boolean parameters and 49 relative
hyperplane parameters.  The replay checks all 240 selected chart Jacobians.
N6-064 supplies the exact \(4\times4\) identity Jacobian in the Boolean
parameters.  The tautological projective chart supplies the
\(49\times49\) identity in the hyperplane parameters, and the present replay
checks that these free-coordinate sets are disjoint.  Hence the combined
Jacobian is block identity of rank 53.  Its tangent prime chooses one variable
in each of the four \(x\)-groups and leaves every \(h\)-variable free.

The 240 tangent primes are precisely the facets of \(J\).  The exact branches
give one side of the initial sandwich, while (3.3) gives the other:

\[
 \operatorname{in}_{\mathfrak m}(I)=J\,k[h_1,\ldots,h_{49},x_1,\ldots,x_{16}].
\tag{4.2}
\]

Let \(B\) be the union of the 240 relative branches and let \(I_B\) be its
closed formal ideal.  We use only

\[
 \operatorname{in}(I_B)
 \subseteq\bigcap_P\operatorname{in}I(B_P)=J;
\]

we do not commute initial ideals with intersections.  Since \(I\subset I_B\),
(4.2) gives equality of the two initial ideals.  Repeatedly matching and
subtracting lowest homogeneous forms converges in the complete local ring,
so two nested closed ideals with the same filtered initial ideal are equal.
Thus

\[
 \boxed{I=I_B.}
\tag{4.3}
\]

This is the full formal germ statement, not merely equality of reduced
tangent-cone supports.

## 5. Projective globalization and extension

Let \(X_{49}\subset\operatorname{Gr}(49,E_3)\) be the rank-at-most-75 locus.
It is projective and stable under the connected row-column torus.  Every
irreducible component is torus stable and contains a torus fixed point; the
fixed Grassmannian points are coordinate subspaces.  Section 1 supplies the
four fixed-point types.

Let \(X_{50}\) be the N6-064 equality locus and form the relative incidence

\[
 Z=\{(S,T):S\subset T,\ \dim S=49,\ T\in X_{50}\}.
\tag{5.1}
\]

It is projective, so its image \(Y\subset\operatorname{Gr}(49,E_3)\) is
closed.  At every torus fixed point of \(X_{49}\), (4.3) says that every
formal branch lies in \(Y\).  Hence an irreducible component through that
fixed point contains a nonempty local open subset in \(Y\); closedness gives
that the whole component lies in \(Y\).  Applying this to every component
proves

\[
 X_{49}=Y.
\tag{5.2}
\]

This component argument is the required globalization.  It does not infer
extension merely by reversing a one-parameter torus specialization.

For \(S\subset T\) furnished by (5.2), (0.1) and
\(\partial S\subset\partial T\), with the latter of dimension 75, force
\(\partial S=\partial T\).  N6-064 then gives (0.4) and the projective
flag-hook description of the second shadow.

## 6. Replay and boundary

```text
python scripts/n6_product_shadow_b49_equality_locus.py \
  --json data/n6_product_shadow_b49_equality_locus.json
python -m unittest tests.test_n6_product_shadow_b49_equality_locus -v
```

The ordinary lower-29 argument still has to connect this theorem to the
fixed-six equality chain.  In particular, N6-073 does not treat the
all-`alpha=3` \(b=47\) or \(b=48\) layers, and it does not make any statement
about border Chow rank.
