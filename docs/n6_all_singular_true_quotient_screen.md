# A bounded true-quotient screen in the all-block-singular layer

**Status.** `FINITE_FIELD_BOUNDED_DIAGNOSTIC`, G-051.  All arithmetic is
over \(\mathbb F_3\).  This is a finite diagnostic, not a characteristic-zero
exclusion theorem.

## 1. Frozen family

Let \(V=A\otimes C\), with both factors six-dimensional.  Fix the identity
matching

\[
 \{e_c\otimes f_c:0\le c<6\}
\]

and a disjoint permutation matching

\[
 \{e_{\sigma(c)}\otimes f_c:0\le c<6\},
 \qquad \sigma(c)\ne c.
\]

Their coordinate span \(U_\sigma\) has dimension twelve.  In each two-plane
over column \(c\), choose an ordered pair of distinct lines in
\(\mathbb P^1(\mathbb F_3)\), one for the factor of \(L\) and one for the
factor of \(M\).  There are \(4\cdot3=12\) choices per column.  The resulting
six-factor frames are complementary because their two lines are distinct in
each direct column fibre.

This family lies in the required closed layer: every complete row and every
complete column contains only two coordinate directions of \(U_\sigma\).
Consequently each projection to two complete rows or two complete columns
has dimension at most four, hence is singular as a map from the
twelve-plane.

Up to conjugacy, a derangement of six letters has cycle type

\[
 6,\qquad 4+2,\qquad 3+3,\qquad 2+2+2.
\]

The replay fixes one representative of each type.

## 2. The actual quotient test

The computation reuses the 441-axis basis of
\(\operatorname{Sym}^2(V)/E_2\) from N6-038.  In a column-pair block, its
`row` axes are the six diagonal coordinates and its signed `rectangle` axes
are the fifteen wedge coordinates.  Thus this is exactly the

\[
 k^6\oplus\bigwedge^2 A
\]

test, not its diagonal projection.

Each of the fifteen products of a frame belongs to its own column-pair
block and has a nonzero quotient image.  Equality of the two quotient
fifteen-planes is therefore equivalent to fifteen projective vector
equalities, one in each block.  A constraint search exhausts the conceptual
space of \(12^6=2{,}985{,}984\) ordered states for each cycle type.  It finds
no common true-quotient pair in any of the four types.

The same support also has 462 unordered coordinate \(6+6\) splits.  All
four types, hence 1848 splits in total, are checked directly.  The numbers
for which both individual quotient images have dimension fifteen are,
respectively,

\[
 462,\quad434,\quad462,\quad396,
\]

and none of them has a common quotient image.

## 3. Why the wedge coordinates cannot be dropped

For the \(2+2+2\) representative, the frozen payload records an explicit
six-column state.  Its two diagonal projections agree in all fifteen
column-pair blocks; one of these equal projections is nonzero.  Nevertheless
the full diagonal-plus-wedge quotient lines agree in only two blocks.  The
other thirteen blocks are rejected by the true quotient test.  This is a
regression guard against a diagonal-only false positive.

## 4. Exact boundary

The screen exhausts only the displayed two-matching family over
\(\mathbb F_3\), together with its coordinate splits.  It does not classify
arbitrary twelve-planes, lift a finite-field result to characteristic zero,
exclude the general all-row/all-column-block-singular layer, exclude the
\(b=50\) endpoint, prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\), or make a border-rank
claim.

Replay with

~~~text
python scripts/n6_all_singular_true_quotient_screen.py \
  --verify-json data/n6_all_singular_true_quotient_screen.json
python -m unittest tests.test_n6_all_singular_true_quotient_screen -v
~~~
