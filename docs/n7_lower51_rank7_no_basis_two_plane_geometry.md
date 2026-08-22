# `perm_7` lower-51: no-basis one-six quotient geometry

## Accepted profile

Assume a hypothetical all-rank-seven 50-term identity has no seven factor
planes forming a direct 49-dimensional sum.  The accepted v7 input says that
every ordering has positive increment multiset

\[
 (1,6,7,7,7,7,7,7).                                 \tag{1}
\]

Choose an ordering realizing six full increments first.  Their planes have
direct sum `A` of dimension 42.  Put `D=V/A`, so `dim D=7`.  Let `X,Y` be the
next two positive labels, ordered so that `X` contributes six and `Y`
contributes one.  Write their quotient images as `Xbar,Ybar` in `D`.

Then

\[
 \dim Xbar=6,\qquad Xbar+Ybar=D.                     \tag{2}
\]

## Reverse-order classification

Keep the same six-plane base `A` and reverse only `X,Y`.  If
`b=dim Ybar`, the two quotient increments become `(b,7-b)`.  By (1), their
positive multiset must again be `(1,6)`.  Hence

\[
 \boxed{\dim Ybar\in\{1,6\}}.                        \tag{3}
\]

There are exactly two quotient geometries.

1. **Intrinsic roles.**  `dim Ybar=1`, and
   `D=Xbar direct_sum Ybar`.  The rank-six and rank-one labels remain
   distinct when their order is reversed.
2. **Swapping roles.**  `dim Ybar=6`.  The two quotient images are distinct
   hyperplanes with five-dimensional intersection.  Whichever label is
   ordered first contributes six and the other contributes one.

No other quotient dimension is compatible with the all-order profile.

## Actual-factor support

For the label contributing increment one, the quotient functional on its
seven Boolean factor directions is supported on at most two actual factors.
In the intrinsic branch this applies to `Y`.  In the swapping branch it
applies to both labels, since each can be placed second.

Thus the exact no-basis frontier is split into three theorem branches:

```text
INTRINSIC-SUPPORT-ONE
INTRINSIC-SUPPORT-TWO
SWAPPING-HYPERPLANES-SUPPORT-AT-MOST-TWO-ON-BOTH-LABELS
```

## Boundary

This quotient classification does not identify the graph maps from `X,Y`
back into `A`, does not construct the common degree-two-through-five
coefficient system, and does not close the no-basis lane.  Those data are the
permanent-specific connecting-map problem, not consequences of (1)--(3).

