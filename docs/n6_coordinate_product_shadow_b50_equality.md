# Coordinate equality at the fifty-dimensional product-shadow endpoint

**Status.** `PURE_COORDINATE_PRODUCT_SHADOW_EQUALITY_THEOREM`,
`EXACT_SMALL_KRUSKAL_KATONA_REPLAY` (N6-062A).  The argument is valid over
every field because it is a statement about finite supports.  It classifies
only coordinate subspaces of the permanent cubic derivative space.  It does
not classify arbitrary noncoordinate subspaces or prove a new Chow-rank lower
bound.

Let

\[
 {\cal T}=\binom{[6]}3,
 \qquad {\cal P}=\binom{[6]}2,
\]

and let \({\cal A}\subset {\cal T}\times {\cal T}\).  Its product lower
shadow is

\[
 \partial_\times{\cal A}
 =\{(I,J)\in{\cal P}\times{\cal P}:I\subset R,\ J\subset C
       \text{ for some }(R,C)\in{\cal A}\}.
\tag{1.1}
\]

We prove the following equality classification.

## Theorem 1 -- coordinate equality classification

If

\[
 |{\cal A}|=50,
 \qquad |\partial_\times{\cal A}|=75,
\tag{1.2}
\]

then, after independent permutations of the row and column vertices,
\({\cal A}\) is one of the following two transposed hooks:

\[
 \boxed{
 {\cal A}=
 \left(\binom U3\times\binom V3\right)
 \cup
 \left(\binom{U_0}3\times{\cal T}\right),
 }
\tag{1.3}
\]

where \(|U|=4\), \(U_0\subset U\), \(|U_0|=3\), and \(|V|=5\), or the
transpose of (1.3).

### 1. The only possible row-degree profiles

Write

\[
 B_R=\{C:(R,C)\in{\cal A}\},\qquad d_R=|B_R|.
\]

The two colex compressions of N6-056 do not increase the product shadow.
The first replaces each \(B_R\) by a left-justified colex segment and
preserves the row degrees.  Its column heights are

\[
 h_j=|\{R:d_R>j\}|.
\]

The second compression makes column \(j\) occupy the first \(h_j\) rows.
Consequently the final row-length partition is the conjugate of \(h\), hence

\[
 h=(d^\downarrow)^{\mathsf T},
 \qquad \lambda=h^{\mathsf T}=d^\downarrow.
\tag{1.4}
\]

Thus the two successive compressions preserve the decreasing row-degree
profile, although the intermediate column-height partition is its conjugate.

The exact N6-056 dynamic program has precisely two Ferrers minimizers of size
50 and shadow 75:

\[
 (20,10,10,10,0^{16}),
 \qquad (4^{10},1^{10}).
\tag{1.5}
\]

Therefore the original row-degree profile is one of these two partitions.
We now work directly with the original, uncompressed
support; no equality is inferred merely by reversing a compression.

### 2. Profile \((20,10,10,10)\)

Let \({\cal F}=\{R:d_R>0\}\), so \(|{\cal F}|=4\), and let \(R_*\) be the
unique row with \(d_{R_*}=20\).  For a row pair \(I\), set

\[
 U_I=\bigcup_{R\supset I}\partial B_R.
\]

Then

\[
 |\partial_\times{\cal A}|=\sum_{I\in{\cal P}}|U_I|.
\tag{2.1}
\]

For the three pairs in \(\binom{R_*}2\), the full fiber gives
\(|U_I|=15\).  Every pair in
\(\partial{\cal F}\setminus\binom{R_*}2\) lies below a ten-element fiber,
whose shadow has size at least ten.  The one-factor Kruskal--Katona bound
gives \(|\partial{\cal F}|\geq6\).  Hence

\[
 |\partial_\times{\cal A}|
 \geq45+10\left(|\partial{\cal F}|-3\right)\geq75.
\tag{2.2}
\]

Equality in (1.2) forces equality everywhere.  Four triples with a six-pair
shadow are exactly \(\binom U3\) for a four-set \(U\).  Thus
\({\cal F}=\binom U3\), and \(R_*=U\setminus\{u\}\) for some \(u\in U\).

The three pairs in \(\partial{\cal F}\setminus\partial R_*\) each lie below
two of the three ten-element fibers.  At each such pair their two column
shadows have union of size ten.  Since either shadow has size at least ten,
the two are equal.  These three incidences form a triangle on the three
fibers, so all three column shadows are one common ten-set \(Q\).

A ten-element family of triples with a ten-pair shadow is exactly
\(\binom V3\) for a five-set \(V\).  Moreover its shadow \(\binom V2\)
determines \(V\).  The three fibers are therefore the same
\(\binom V3\).  This is (1.3), with \(U_0=R_*\).

### 3. Profile \((4^{10},1^{10})\)

Let \({\cal F}=\{R:d_R=4\}\) and put \(D=\partial{\cal F}\).  If
\(I\in D\), then \(U_I\) contains the shadow of a four-element triple
family, so \(|U_I|\geq6\).  If \(I\notin D\), all four triples containing
\(I\) are low rows, and their singleton fibers have nonempty three-pair
shadows; hence \(|U_I|\geq3\).  Since ten triples have shadow at least ten,

\[
 |\partial_\times{\cal A}|
 \geq6|D|+3(15-|D|)=45+3|D|\geq75.
\tag{3.1}
\]

Equality forces \(|D|=10\), so
\({\cal F}=\binom U3\) for a five-set \(U\).  For each pair in
\(\binom U2\), the three high rows containing it have column-shadow union
of size six.  Thus their individual six-element shadows coincide.  The
Johnson graph on \(\binom U3\), adjacent when two triples share a pair, is
connected, so every high fiber has the same shadow \(Q\).  A four-element
triple family with six-pair shadow is \(\binom V3\) for a four-set \(V\);
therefore all high fibers equal \(\binom V3\).

Write the sixth row vertex as \(\infty\).  The low rows are
\(\{\infty\}\cup e\), with \(e\in\binom U2\).  For a pair
\(\{\infty,u\}\), equality in (3.1) forces the four singleton fibers below
it to have one common triple.  Connectivity of the line graph of the complete
graph on \(U\) makes all ten low fibers the same singleton \(\{C_*\}\).
For an inner pair \(I\in\binom U2\), its three high fibers already contribute
\(Q=\binom V2\), while its low fiber contributes \(\partial C_*\).  Equality
forces \(\partial C_*\subset Q\), hence \(C_*\subset V\).  This is precisely
the transpose of (1.3).

The two small equality facts used above are finite: among six vertices there
are exactly fifteen four-triple families with six-pair shadow, one for each
four-set, and exactly six ten-triple families with ten-pair shadow, one for
each five-set.  The replay enumerates respectively \(\binom{20}{4}\) and
\(\binom{20}{10}\) families.

## 4. The second shadow is exactly 23

For (1.3), the first product shadow is

\[
 K=
 \left(\binom U2\times\binom V2\right)
 \cup
 \left(\binom{U_0}2\times{\cal P}\right),
\tag{4.1}
\]

of size \(6\cdot10+3\cdot15-3\cdot10=75\).  Its next product shadow is

\[
 M=
 (U\times V)\cup(U_0\times[6]),
\tag{4.2}
\]

and therefore

\[
 \boxed{|M|=4\cdot5+3\cdot6-3\cdot5=23.}
\tag{4.3}
\]

The transpose hook has the same value.  In polynomial language, every
coordinate equality plane has a 75-dimensional first derivative space and a
23-dimensional second derivative space.

## 5. Exact replay and boundary

```text
python scripts/n6_coordinate_product_shadow_b50_equality.py \
  --json data/n6_coordinate_product_shadow_b50_equality.json
python -m unittest tests.test_n6_coordinate_product_shadow_b50_equality -v
```

This theorem is an exact classification of torus-fixed, equivalently
coordinate, equality supports.  A torus degeneration can send a noncoordinate
equality plane to one of these supports, but reversing that degeneration is a
separate geometric problem.  N6-062A makes no such reversal and does not
exclude the unresolved all-`alpha=3`, `b=50` Chow configuration.
