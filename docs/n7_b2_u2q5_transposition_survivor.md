# Exact `U2 Q5` transposition-slice survivor

## Status

`EXACT SLICE SURVIVOR; NO COMPLETE PACKET-B SURVIVOR.`

The first two `U`-degree gates do not force quotient-frame synchronization.
There is an exact two-term characteristic-zero identity which matches the
identity permutation and one transposition, and whose full nine-variable
minimal Sylvester complex has zero coupling defect.

Use coordinates

\[
 q_0,\ldots,q_6,u_{01},u_{10}.
\]

Then

\[
\begin{aligned}
 &(1/2)(q_0-q_1-u_{01}-u_{10})(q_1-u_{10})q_2\cdots q_6\\
 &+(1/2)(q_0+q_1+u_{01}-u_{10})(q_1+u_{10})q_2\cdots q_6\\
 &=(q_0q_1+u_{01}u_{10})q_2\cdots q_6.             \tag{1.1}
\end{aligned}
\]

Both summands are products of seven independent linear forms.  Their quotient
frames contain `q_0-q_1` and `q_0+q_1`, so neither frame is monomial.  The
right side is exactly the restriction of `perm_7` to the identity permutation
and the transposition `(0 1)`.

## Residual bilinear form

For the two-term shear pencil, the `U1 Q6` kernel has two coordinates.  After
substitution, the `U2 Q5` coefficient for two `U` directions is

\[
 b(x,y)=x_0y_1+x_1y_0+2x_1y_1,
 \qquad [b]=\begin{bmatrix}0&1\\1&2\end{bmatrix}. \tag{2.1}
\]

It is nondegenerate.  Its isotropic cone is the union of the two lines

\[
 x_1=0,\qquad x_0+x_1=0.
\]

Taking `x=(1,0)` and `y=(-1,1)` gives

\[
 b(x,x)=b(y,y)=0,\qquad b(x,y)=1.                  \tag{2.2}
\]

Thus square `U` targets vanish while the reciprocal pair
`u_01 u_10` has coefficient one.  Formula (1.1) is the integrated form of this
bilinear survivor; it has no terms of `U`-degree above two.

## Exact Sylvester check

The script constructs the labelled 35-dimensional middle of each rank-seven
term directly.  Over the rationals, the two-term complex has

```text
middle dimension = 70
rank B            = 65
rank C            = 60
rank BC           = 55
```

Consequently

\[
 70-65-60+55=0,
\]

so `ker(B) subset image(C)` holds for the unprojected nine-variable slice.
This is stronger than the earlier quotient-only shear diagnostic and proves
that the identity, zero `U1 Q6` layer, one `U2 Q5` transposition target, and
local Sylvester equality together still do not force monomial frames.

## Exact boundary and global join

This survivor has only two terms and only one transposition pair.  It is not a
42-complement packet.  In particular, its ranks `65,60,55` are local slice
ranks, not contributions that may be added independently to the full target
ranks

\[
 \operatorname{rank}B+\operatorname{rank}C=2870,
 \qquad\operatorname{rank}(BC)=1225.               \tag{4.1}
\]

Cross-term intersections change all three ranks.  A valid completion must
assemble the original 49-variable maps before testing (4.1).

The next smallest gate is gluing two transposition slices.  There are two
inequivalent cases: transpositions sharing one row and disjoint
transpositions.  The shared-row case tests compatibility of two bilinear
survivors inside one factor; the disjoint case tests whether their middle
relations remain coupled.  Either computation must retain the unprojected
`B/C` maps.

Replay:

```text
python scripts/n7_b2_u2q5_transposition_survivor.py \
  --verify-json data/n7_b2_u2q5_transposition_survivor.json
python -m unittest tests.test_n7_b2_u2q5_transposition_survivor -v
```
