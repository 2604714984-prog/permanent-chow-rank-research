# Coordinate second-order matching-envelope barrier

## Status and claim boundary

`ROUTE_BARRIER`, `EXACT_FINITE_INTERFACES_REPLAYED`,
`COORDINATE_SECOND_ORDER_SUPPORT_ONLY`.

For a set `A` of at most six coordinate cells in a `4 x 4` block, define the
raw second-order matching envelope

\[
E_2(A)=\{M:\ M\text{ is a perfect matching and }|M\cap A|\ge2\}.
\tag{0.1}
\]

A quartic matching produced by two regular factor motions leaves at least two
unchanged coordinate factors, so it belongs to this envelope. The exact
maximum is

\[
\boxed{|E_2(A)|\le14}.
\tag{0.2}
\]

Equality holds for exactly 96 labeled supports. They form one orbit under
independent row and column permutations, and every equality support is a
six-cycle `C6` on a selected `3 x 3` subblock: equivalently, it is `K_(3,3)`
minus one perfect matching.

However, six equality envelopes already cover all 24 perfect matchings.
Therefore raw second-order matching-support counting cannot exclude a
coordinate six-block lift. Coefficients, lower-order cancellation, and the
common-source equations are indispensable.

This note does not construct a second-order six-block witness and does not
change

\[
6\le\mu(6,4)\le8.
\]

## 1. Exact moment formula

Let `r_j(A)` be the number of `j`-edge matchings contained in `A`. For a target
perfect matching `M`, put `k_M=|M cap A|`. On `k=0,1,2,3,4`,

\[
\mathbf 1_{k\ge2}
=\binom{k}{2}-2\binom{k}{3}+3\binom{k}{4}.
\tag{1.1}
\]

Every two-edge matching extends to two perfect matchings, every three-edge
matching extends uniquely, and every four-edge matching already is perfect.
Summing (1.1) gives

\[
\boxed{|E_2(A)|=2r_2(A)-2r_3(A)+3r_4(A).}
\tag{1.2}
\]

This identity provides an implementation independent of direct enumeration of
the 24 target matchings.

## 2. Equality classification

The exact scan checks

\[
\sum_{a=0}^{6}\binom{16}{a}=14893
\]

cell supports. The maximum is fourteen and is attained by 96 supports. Every
one has row and column degree sequences

```text
(2,2,2,0) and (2,2,2,0),
```

is connected after deleting the isolated row and column, and hence is a `C6`.
For every equality support,

```text
r_2=9,
r_3=2,
r_4=0,
|E_2|=2*9-2*2=14.
```

There are `4*4*6=96` such supports: choose the omitted row, omitted column, and
the perfect matching removed from the remaining `K_(3,3)`.

## 3. Explicit six-envelope cover

Fix rows and columns `0,1,2`. For every permutation `mu in S_3`, define

\[
A_\mu
=\{(r,c):0\le r,c<3,\ c\ne\mu(r)\}.
\tag{3.1}
\]

Each `A_mu` is an equality `C6` support and has a fourteen-element envelope.
The six envelopes satisfy

\[
\boxed{\bigcup_{\mu\in S_3}E_2(A_\mu)=S_4.}
\tag{3.2}
\]

If a target matching fixes the omitted fourth row and column, choose `mu` with
at most one agreement with its `3 x 3` restriction. Otherwise the target uses
exactly two edges inside the selected `3 x 3` block, and one can choose `mu`
that avoids both. In either case at least two target edges belong to `A_mu`.

Equation (3.2) is only a support cover. It does not solve the order-zero and
order-one cancellation equations and does not provide integrable component
coefficients.

## 4. Consequence for the active search

The coordinate regular first-order boundary is closed by the preceding local
budget theorem. At second order, the analogous raw envelope is already broad
enough for six extremal frames to cover the target. Therefore the next valid
object is not a larger support enumeration. It is the coefficient-valued
second-order common-source system, including:

- two-factor motions from order-zero source coefficients;
- factor-source mixed terms;
- second-order source motion;
- repeated-factor source-kernel directions; and
- simultaneous cancellation of the complete order-zero and order-one
  quartics, including nonmatching monomials.

## 5. Verification

Run

```bash
python scripts/general_quartic_coordinate_second_order_envelope.py \
  --json /tmp/general_quartic_coordinate_second_order_envelope.json
python scripts/general_quartic_coordinate_second_order_envelope_independent.py
python -m unittest tests.test_general_quartic_coordinate_second_order_envelope -v
```

The primary replay enumerates supports and row-column orbits. The independent
replay uses the matching-moment identity (1.2).
