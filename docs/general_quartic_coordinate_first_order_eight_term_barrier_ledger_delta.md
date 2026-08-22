# Ledger delta: coordinate regular first-order eight-term barrier

Add the following restricted route theorem to the active `perm_6` quartic
frontier.

## Statement

For regular first-order degenerations from degree-six coordinate Chow frames
in one `4 x 4` block, including repeated factors and internal source-kernel
cancellation,

\[
\boxed{\text{at least eight components are necessary to produce }\operatorname{perm}_4.}
\]

Equivalently, every coordinate regular first-order block of size at most seven
has zero `perm_4` matching target.

## Local invariant

For a coordinate six-frame \(\gamma\), let

```text
E(gamma) = full one-factor-motion matching envelope
D(gamma) = matchings contained in the coordinate frame
K(gamma) = matchings accessible from ker(Phi_gamma)
S(gamma) = D(gamma) union K(gamma).
```

The complete 54,264-frame classification proves

\[
|E(\gamma)|+|S(\gamma)|\le6.
\]

The equality locus contains 864 frames in four row-column orbits.

## Global incidence

Every target matching outside `union_i S(gamma_i)` requires two frame-envelope
incidences because its nonzero order-zero source monomial must cancel across
components. Therefore

\[
48-\sum_i|S_i|
\le
\sum_i|E_i|
\le
6q-\sum_i|S_i|,
\]

which forces \(q\ge8\).

## Frozen theorem core

```text
8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

## Boundary

```text
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
six-block unrestricted literal sum = OPEN
seven-block unrestricted literal sum = OPEN
mu(6,4) = OPEN in [6,8]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```

This supersedes the earlier plan to exhaust six disjoint transposition edges:
the corrected local invariant already rules out the equality state, including
repeated-factor internal cancellations.
