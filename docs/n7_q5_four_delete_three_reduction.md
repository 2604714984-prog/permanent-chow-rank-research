# Deleting three points reduces the `q5=4,q6=3` frontier to one relation

## Status and boundary

`F4-TARGET-INTEGRABILITY-CLOSED.`

This note treats the common-graph `F4` frontier

\[
(H_3,H_4,H_5,H_6)=(35,37,38,39),
\qquad (q_5,q_6)=(4,3).
\]

The argument is over an algebraically closed field of characteristic zero.
It is an ordinary Waring-rank replacement argument.  It does not classify the
four-dimensional bivector web, and it makes no statement about border Waring
rank, border Chow rank, or flat limits.

Let `a_1,...,a_42` be the distinct nonzero vectors representing the graph
points, and let

\[
W_d=\operatorname{span}\{a_1^d,\ldots,a_{42}^d\},
\qquad
R_d=\left\{r\in k^{42}:\sum_i r_i a_i^d=0\right\}.
\]

Thus `dim W6=39`, `dim R6=3`, `dim W5=38`, and `dim R5=4`.  The seven
squarefree sextic targets are contained in `W6`.

## A common projective trivialization

Choose a linear form `ell` which is nonzero at every point `a_i`.  This is
possible because the field is infinite and the union of the 42 hyperplanes

\[
\{\ell:\ell(a_i)=0\}
\]

is a proper finite union.  Put

\[
s_i=\ell(a_i)^{-1},\qquad b_i=s_i a_i.
\]

Then `ell(b_i)=1` for every `i`.  This projective rescaling does not change
the indexed projective points or any Hilbert rank.

The relation coefficients do change with degree.  If

\[
\sum_i r_i a_i^d=0,
\]

then, because `a_i=s_i^(-1)b_i`, the corresponding relation among the
normalized powers is

\[
\sum_i r_i s_i^{-d}b_i^d=0.
\tag{1}
\]

Thus the diagonal map

\[
(r_i)_i\longmapsto(r_i s_i^{-d})_i
\]

identifies the old and normalized `R_d`.  It preserves dimensions, supports,
coordinate minors, and the property that a selected coordinate restriction
is injective.  We use the normalized relation spaces from now on.

Contract a normalized degree-six relation with `ell`.  Since
`ell(b_i)=1`,

\[
0=\ell\mathbin{\lrcorner}\sum_i r_i b_i^6
=6\sum_i r_i b_i^5.
\]

Characteristic zero permits division by six, so the same coefficient vector
is a degree-five relation.  Consequently the chosen trivialization gives a
literal inclusion

\[
R_6\subset R_5.
\tag{2}
\]

The inclusion (2) is the only cross-degree identification used below.  It is
not asserted before the common `ell(b_i)=1` normalization.

## Selecting the three deleted coordinates

Choose a basis of the three-dimensional space `R6` and form its `3 x 42`
coordinate matrix.  It has row rank three, so it contains a nonsingular
`3 x 3` column minor.  Let `D` be the corresponding set of three indices and
let `S` be its 39-index complement.  Equivalently, the coordinate restriction

\[
\operatorname{res}_D:R_6\longrightarrow k^D
\tag{3}
\]

is an isomorphism.

For either degree, a relation on the retained points extends by zero on `D`
to a relation on all 42 points.  Conversely, a full relation which vanishes
on `D` restricts to a relation on the retained points.  Therefore zero
extension gives the exact identification

\[
R_d(S)=R_d\cap\ker(\operatorname{res}_D).
\tag{4}
\]

Applying (4) in degree six and using (3) gives

\[
R_6(S)=0.
\tag{5}
\]

Hence the 39 retained sixth powers are linearly independent.  Their span has
dimension 39, equal to `dim W6`, so they form a basis of the original space
`W6`.  In particular, deleting `D` does not merely preserve the seven target
sextics: the retained powers still span every element of the original
sixth-power space.

Now apply (4) in degree five.  By (2), the restriction of
`res_D:R5 -> k^D` to `R6` is the isomorphism (3).  The restriction from `R5`
therefore has rank at least three, and its codomain has dimension three, so
its rank is exactly three.  Rank-nullity gives

\[
\dim R_5(S)=\dim R_5-3=1.
\tag{6}
\]

Thus the 39-point retained configuration has exactly

\[
(q_5',q_6')=(1,0).
\tag{7}
\]

## The unique retained gradient representation

Let `T6` denote the seven-dimensional span of the first derivatives of the
squarefree septic `m=x_0x_1...x_6`.  Since `T6 subset W6` and the retained
sixth powers form a basis of `W6`, every target derivative has a
representation using only the retained 39 powers.  Equation (5) makes each
coefficient row unique.  Write the resulting vector-valued sextic as

\[
\nabla m=\sum_{i\in S}c_i l_i^6,
\tag{8}
\]

where `l_i` is the linear form represented by `b_i`.

Let `rho` span the one-dimensional space `R5(S)`.  Equality of mixed
partials in (8) gives a bivector `beta` such that

\[
c_i\wedge b_i=\rho_i\beta
\qquad(i\in S).
\tag{9}
\]

There is no `R6(S)` gauge: (8) is the unique retained representation.

## One-relation Waring replacement

If `beta=0`, equation (9) makes every `c_i` proportional to `b_i`.  The
gradient integrates term by term, expressing `m` as a sum of at most 39
seventh powers.

Suppose `beta` is nonzero.  Choose an index with `rho_i!=0`.  Then `beta` is
a nonzero scalar multiple of the decomposable bivector
`c_i wedge b_i`, so `beta` is decomposable.  Let `U` be its two-dimensional
support.  For every index in

\[
A=\operatorname{supp}(\rho),
\]

equation (9) implies

\[
b_i,c_i\in U.
\tag{10}
\]

The supported part of (8) is separately closed: its mixed-partial defect is
`beta` multiplied by the fifth-power relation

\[
\sum_{i\in A}\rho_i l_i^5=0.
\]

It therefore integrates to a binary septic.  Over the algebraic closure a
binary septic has Waring rank at most seven.

The relation `rho` is nonzero and the projective points are distinct.  Any at
most six distinct projective points have independent fifth powers, by
isolating each point with a product of at most five separating hyperplanes.
Consequently

\[
|A|\ge7.
\tag{11}
\]

For `i` outside `A`, equation (9) says `c_i wedge b_i=0`, so those columns
integrate individually.  Replacing the supported binary primitive and
charging every outside column gives

\[
\operatorname{WaringRank}(m)
\le(39-|A|)+7
\le39.
\tag{12}
\]

The characteristic-zero Waring rank of the squarefree monomial
`x_0x_1...x_6` is 64.  Equation (12), as well as the `beta=0` bound, is a
contradiction.

## Decision

The three deleted indices are selected from the relation code itself, not
from a sampled point family.  The retained sixth powers form a basis of the
entire original target-containing space, and the retained coefficient
representation has no gauge.  Therefore the argument applies to every
hypothetical `F4` configuration and to every original `q6=3` coefficient
representative.

The exact target-integrability decision is

```text
Q5-FOUR-TARGET-INTEGRABILITY-CLOSED
F4-CLOSED
```

No classification of `P3` Pfaffian webs, no weighted-coupling computation,
and no finite-field or numerical inference is needed.  The result is an
ordinary characteristic-zero nonexistence theorem only; it does not imply a
border-rank lower bound.
