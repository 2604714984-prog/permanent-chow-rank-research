# The forty-seven-dimensional product-shadow equality locus

**Status.** `PURE_CHARACTERISTIC_ZERO_B47_EQUALITY_LOCUS_CLASSIFICATION`,
`EXACT_INTEGER_224_ORBIT_LINEAR_AND_QUADRATIC_ELIMINATION`,
`EXACT_RELATIVE_240_BRANCH_REPLAY` (N6-078).

Let \(E_3\) and \(E_2\) be the permanent cubic and quadratic coordinate
spaces. Over an algebraically closed field of characteristic zero, N6-078
proves

\[
 S\subset E_3,\quad \dim S=47,\quad \dim\partial S=75
 \quad\Longrightarrow\quad
 S\subset T\subset E_3,
\]

where

\[
 \dim T=50,qquad \partial T=\partial S.
\tag{0.1}
\]

Consequently N6-064 applies to \(T\). If \(K=\partial S\), then

\[
 \boxed{\dim\partial K=23,}
\tag{0.2}
\]

and \(\partial K\) is a genuine projective flag hook.

## 1. Original coordinate supports

Let

\[
 \mathcal A\subset
 \binom{[6]}3\times\binom{[6]}3,
 \qquad |\mathcal A|=47,
 \qquad |\partial_\times\mathcal A|=75.
\]

Write \(B_R=\{C:(R,C)\in\mathcal A\}\), \(d_R=|B_R|\), and

\[
 U_I=\bigcup_{R\supset I}\partial B_R.
\]

Then \(|\partial_\times\mathcal A|=\sum_I|U_I|\). The two product colex
compressions preserve the decreasing original row-degree profile. The exact
Ferrers dynamic program has minimum 75 and 14 minimizing profiles. Seven are

\[
\begin{aligned}
 &(20,10,10,7),\ (20,10,9,8),\ (20,9,9,9),\\
 &(19,10,10,8),\ (19,10,9,9),\\
 &(18,10,10,9),\ (17,10,10,10),
\end{aligned}
\tag{1.1}
\]

with zeros appended; the other seven are their transpose Ferrers profiles.
The proof now works in the original support and does not reverse compression.

### 1.1 Row-oriented profiles

Let \(\mathcal F\) be the four active row labels and \(R_*\) the row of
degree at least 17. A family of at least 17 triples on six vertices has all
15 pairs in its shadow: every pair has four cubic lifts and at most three
triples are missing. Each other active fiber has at least seven triples and
therefore at least nine pairs. If
\(|\partial\mathcal F|\ge7\), then

\[
 |\partial_\times\mathcal A|
 \ge45+9\bigl(|\partial\mathcal F|-3\bigr)
 \ge81,
\]

which is impossible. Thus \(|\partial\mathcal F|=6\) and

\[
 \mathcal F=\binom{U_4}{3}.
\tag{1.2}
\]

The three new row pairs form a triangle on the three ordinary fibers. In
every profile in (1.1), the union of the two column shadows along each edge
has size at least ten: every fiber of size at least eight already has
ten-pair shadow, while the only size-seven fiber is adjacent to two
size-ten fibers. Equality of the total product shadow forces every edge union
to have size exactly ten.

If all ordinary fibers have size at least eight, triangle connectivity and
the exact one-factor equality classification synchronize their shadows to

\[
 Q=\binom{V_5}{2}.
\]

The size-eight, size-nine and size-ten fibers are respectively
\(\binom{V_5}{3}\) with two, one or zero triples deleted. In the sole
size-seven case, the other two fibers first give the same \(Q\); both edges
then force the size-seven shadow into \(Q\), so every one of its triples lies
in \(V_5\). Thus it is a three-cell deletion from
\(\binom{V_5}{3}\). The distinguished fiber is the full 20-family with
zero to three cells deleted. Hence all seven profiles in (1.1) are precisely
three-cell deletions from a row hook.

### 1.2 Transpose-oriented profiles

Six transpose profiles have ten high rows: their degree multisets are

\[
 4^{10},\quad4^9 3,\quad4^9 2,\quad
 4^8 3^2,\quad4^8 3 2,\quad4^7 3^3.
\tag{1.3}
\]

The remaining profile has nine degree-four rows and eleven singleton rows.
All active row-label families have size at least 17, so their row shadow is
all 15 pairs.

If every high degree is at least three, put \(D=\partial\mathcal H\). A
high fiber contributes at least six column pairs and an outside singleton
contributes three. Therefore

\[
 75\ge6|D|+3(15-|D|)=45+3|D|\ge75.
\tag{1.4}
\]

Equality gives \(|D|=10\) and
\(\mathcal H=\binom{V_5}{3}\).

For either profile containing one degree-two high row \(H_*\), remove it and
write \(D_0\) for the shadow of the nine remaining high rows. Those rows have
degree at least three, so \(|D_0|\ge10\). Let
\(u=|\partial H_*\setminus D_0|\). The sharper count is

\[
 75\ge6|D_0|+5u+3(15-|D_0|-u)
 =45+3|D_0|+2u\ge75.
\tag{1.5}
\]

Thus \(|D_0|=10\) and \(u=0\). The nine-row equality classification gives
\(\mathcal H\setminus\{H_*\}=\binom{V_5}{3}\setminus\{H^*\}\); since
all pairs of \(H_*\) lie in \(D_0\), the distinct tenth row must be
\(H_*=H^*\). Again \(\mathcal H=\binom{V_5}{3}\).

In the exceptional profile, the nine degree-four rows obey (1.4) directly and
form \(\binom{V_5}{3}\setminus\{H^*\}\). Since every row label is active,
the missing \(H^*\) is one of the eleven singleton rows.

At every inner pair equality gives \(|U_I|=6\). The Johnson graph on the
high rows remains connected after deleting one vertex, so all degree-at-least
three fiber shadows synchronize to

\[
 Q=\binom{W_4}{2}.
\]

The degree-two or exceptional singleton high fiber has every row pair under
another high row; hence its shadow is contained in \(Q\). All high fibers
therefore lie in \(\binom{W_4}{3}\) and are obtained by the stated zero to
three deletions.

The low singleton rows are indexed by the edges of \(K_5\). At most three
are inactive. The graph \(K_5\) remains connected after deleting at most
three edges, so its line graph remains connected. Equality at every outer
pair makes all active singleton fibers the same \(\{C_*\}\), and equality at
the inner pair forces \(\partial C_*\subset Q\), hence \(C_*\subset W_4\).
This proves that all seven transpose profiles are three-cell deletions from a
transpose hook.

Thus every coordinate fixed point is a three-cell deletion from a unique
50-hook. Since every hook shadow coordinate has at least four cubic lifts,
every such deletion preserves the 75-shadow. The labelled support count is

\[
 720\binom{50}{3}=\boxed{14,112,000}.
\tag{1.6}
\]

## 2. All 224 stabilizer orbits

For a standard parent, the \(\binom{50}{3}=19,600\) deletions split into
112 stabilizer orbits. Row and transpose orientations give 224 orbits. The
exact certificate records every representative and orbit size.

For the parent shadow \(K_0\), all 400 cubic weights are checked and the
coordinate prolongation is exactly the 50-dimensional parent \(T_0\). The
row-column torus has distinct one-dimensional cubic weights, so this also
proves the full linear statement

\[
 P_E(K_0)=\{f\in E_3:\partial f\subset K_0\}=T_0.
\tag{2.1}
\]

## 3. Exact local scheme

At every one of the 224 orbit representatives, connected-component
elimination of the full incidence linearization gives

\[
 \dim T=157=16+141,
 \qquad141=\dim\operatorname{Gr}(47,50),
\tag{3.1}
\]

with no eta-only root. The 16 parent directions and 141 relative
Grassmannian directions use disjoint coordinates.

After eliminating all transverse variables, every nonzero grounded quadratic
row is a nonzero integer multiple of a single monomial. Its exact rational
row span is precisely the 25 within-group products from N6-064. No forbidden
product is missing, no extra monomial occurs, and no monomial contains a
relative \(\operatorname{Gr}(47,50)\) variable.

Let \(J\) be the radical ideal generated by these 25 products. Its 240 prime
facets correspond to the four Boolean groups of sizes \(3,4,4,5\). Each
N6-064 four-dimensional branch has the relative
\(\operatorname{Gr}(47,50)\) bundle over it, producing a smooth branch of
dimension

\[
 4+141=145.
\]

The grounded equations give \(J\subset\operatorname{in}_{\mathfrak m}I\),
while the 240 actual branches give the reverse inclusion. The same complete
filtered lifting used in N6-073 and N6-076 proves scheme-theoretically that
the completed local germ is exactly the union of these 240 relative branches.

## 4. Projective globalization

Let \(X_{47}\) be the projective rank-at-most-75 product-shadow locus, and
let \(Y\subset X_{47}\) be the projective image of

\[
 \{(S,T,K):S\subset T,\ \dim S=47,\ \dim T=50,\
   \dim K=75,\ \partial T\subset K\}.
\]

The image \(Y\) is closed. Every irreducible component of the torus-stable
projective scheme \(X_{47}\) contains a coordinate fixed point. Section 1
classifies all such points, and Section 3 shows that their full formal germs
lie in \(Y\). Faithful flatness of completion gives a Zariski neighborhood
inside \(Y\); closedness then puts the whole component in \(Y\). Therefore
\(X_{47}=Y\), proving (0.1).

## 5. Boundary and replay

N6-078 is an ordinary characteristic-zero theorem. It does not treat the
dimension-46 locus, does not by itself prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\), and makes no
border-rank claim.

```text
python scripts/n6_product_shadow_b47_equality_locus.py \
  --verify-json data/n6_product_shadow_b47_equality_locus.json
python -m unittest tests.test_n6_product_shadow_b47_equality_locus -v
```
