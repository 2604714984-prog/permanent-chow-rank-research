# Forced-gradient reduction of the Packet-A equality locus

## Status

`EXACT RESIDUAL COMPONENT; UNIVERSAL BLOCK DEFECT NOT YET DERIVED.`

Degree-six target containment allows arbitrary coefficients expressing the
49 permanent derivatives in the aggregate `D6` span.  A Chow identity is
strictly stronger.  Differentiation forces those coefficients to be the same
factor coefficients and external term weights that define the original
terms.

For omitted column `b`, let `A6_b(F)` be the projected labelled degree-six
map.  Its forced transport is

\[
 R_b(F,c)_{(i,\widehat r),(s,b)}
 =c_i\,[x_{s,b}]\ell_{i,r}.
\]

Every Packet-A equality point must therefore satisfy

\[
 A6_b(F)R_b(F,c)=T_b,\qquad b=0,\ldots,6.       \tag{1}
\]

The residual component `Z_A_grad` is the intersection of these seven systems
with the open rank-seven/simple-multilinear matroid locus and the labelled
inverse-coefficient `2/5` incidence.

## Exact controls

For the first 49 Glynn terms, one block of (1) has exact rational residual
rank five; every one of its 6,468 entries is nonzero.  The seven disjoint
omitted-column blocks give total residual rank 35.  This recovers the earlier
target quotient obstruction with the coefficient transport now forced rather
than freely chosen.

For all 64 Glynn terms, the residual is exactly zero.  Thus (1) is a genuine
permanent identity constraint, not an inconsistent relaxation.

## Why the present invariants do not yet give a universal defect

The simple-multilinear matroid condition is an open collection of nonvanishing
rank minors.  It does not impose an equation in a fixed permanent torus block.
Moreover, the aggregate maps have dimensionally possible injective shapes

```text
A2: 1225 x 1029
A5: 2869685 x 1029
```

so the current hypotheses do not force either `K2` or `K5` to be nonzero.
On the open stratum `K2=K5=0`, the complementary pairing is vacuous.
Consequently simple-matroid geometry plus the pairing alone cannot currently
prove that one fixed block of (1) has nonzero defect.

The smallest missing invariant is a permanent-specific syzygy showing that
`Z_A_grad` inside the simple-matroid open set necessarily develops a nonzero
`2/5` relation incompatible with inverse-coefficient pairing, or is empty.
Equivalently, one must classify the component of (1) rather than optimize the
three degrees independently.

This package produces neither an exact 49-term survivor nor `A-CLOSED`.
Ordinary lower 50 and border rank remain unresolved.

Replay:

```text
python scripts/n7_packet_a_equality_locus_gradient.py \
  --verify-json data/n7_packet_a_equality_locus_gradient.json
python -m unittest tests.test_n7_packet_a_equality_locus_gradient -v
```
