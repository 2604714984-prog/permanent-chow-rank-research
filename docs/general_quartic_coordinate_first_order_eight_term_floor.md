# The eight-term floor for coordinate regular first-order lifts

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`RESTRICTED_COORDINATE_FIRST_ORDER_FLOOR`.

Let `q` regular degree-six coordinate Chow frames specialize in one fixed
`4 x 4` block, repetitions allowed. Let their regular quartic component
families have total order-zero polynomial equal to zero. If the first
derivative has all 24 perfect-matching coefficients nonzero, then

\[
\boxed{q\ge8.}
\tag{0.1}
\]

In particular every coordinate regular first-order block with at most seven
components is zero relative to a nonzero diagonal-torus transform of `perm_4`.

This is a restricted degeneration theorem. It does not prove that eight such
coordinate degenerating components exist, does not exclude arbitrary
noncoordinate six- or seven-block intersections, and does not change

\[
6\le\mu(6,4)\le8.
\]

## Proof

For component `i`, retain the notation from the coordinate first-order closure
theorem:

```text
e_i = size of the matching envelope,
p_i = number of direct perfect matchings,
v_i = non-direct matching support of the internal source-kernel tangent.
```

The exact local theorem gives

\[
e_i+p_i+v_i\le6.
\tag{1.1}
\]

Let `d` be the number of target matchings direct in at least one component and
let `s` be the number of non-direct target matchings occurring in exactly one
envelope. The degree-one incidence lemma puts every such non-direct target into
one of the vertical sets. Hence

\[
\sum_{i=1}^q e_i\ge d+s+2(24-d-s)=48-d-s,
\]

while

\[
d\le\sum_i p_i,
\qquad
s\le\sum_i v_i.
\]

Therefore

\[
48\le\sum_{i=1}^q(e_i+p_i+v_i)\le6q.
\]

Thus `q>=8`. At `q=6` the contradiction margin is twelve; at `q=7` it is six.

## Consequence

The coordinate regular first-order route has the exact lower floor

```text
q <= 7: impossible
q = 8:  not decided by this theorem
```

The next active coordinate interface is a second-order first-nonzero lift, not
a seven-component first-order search.
