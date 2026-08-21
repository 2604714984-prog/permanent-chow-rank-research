# Research handoff

Canonical handoff for the active permanent Chow-rank research stack.

Last updated: **2026-08-22**

## GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
active Draft PR: #92
parent branch: research/quartic-six-term-frontier
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
seven-block first-order local-rigidity packet head: 44021026bb7fb0e2a46c69f927d83cd022b86732
seven-block second-order local-rigidity packet head: b1273af7ca1926e2e3a42be6b17a50e0db4fb4a2
current handoff receipt: THIS COMMIT
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active unrestricted boundary

The five-block theorem and the compressed Glynn witness give

\[
\boxed{6\le\mu(6,4)\le7},
\qquad
\boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

```text
five blocks       ZERO
six blocks        OPEN
seven blocks      NONZERO
eight blocks      NONZERO
```

The ordinary Chow-rank interval is unchanged: a derivative-space intersection
is not a Chow decomposition of `perm_6`.

## Explicit seven-block witness

For every `m>=3` and `n>=m+2`, one missing Walsh character removes a term from
Glynn's formula and gives

\[
\boxed{\mu(n,m)\le2^{m-1}-1.}
\]

At `(m,n)=(4,6)` this is an exact seven-block witness.

```text
core: 045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

Inside the paired-column family `a_i(column 1)b_i(column 2)Q_i(columns 3,4)`,
seven is exact. The six-dimensional symmetric zero-diagonal contraction image
contains no nonzero rank-one matrix, so six paired-column terms are impossible.
A six-block witness must use genuinely mixed frames or cancellation outside
that family.

## Local rigidity of the standard seven-block witness

Write the seven signed summands as

\[
G_v=\chi(v)v\otimes v\otimes(v\otimes v-w\otimes w),
\qquad v\ne w=(1,1,1,1).
\]

### Direct pair merge and first-order absorption

For all 21 pairs, `G_u+G_v` has mode ranks `(2,2,3,3)` and essential dimension
ten, exceeding the one-block cap six.

The `(1,1,1,1)` tangent projection of one standard block has 28 raw generators
and dimension 18. After deleting any one summand, the other six projected
tangent spaces have rank 108; adjoining the missing summand raises the rank to
109. Thus the missing direction is not tangent to the six-block addition image.

```text
core: 7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
status: STRICT_LOCAL_ROUTE_BARRIER
```

### Second-order absorption

For each deletion, the six full degree-four tangent maps use 666 parameters and
have exact rank 574. Their complete characteristic-zero first-order kernel has
dimension 92.

The complete polarized kernel calculation gives

```text
kernel pairs checked                         4,278
nonzero projected curvature vectors            306
curvature span rank                              24
projected tangent rank                          108
curvature quotient rank                           0
missing-summand augmented rank                  109
```

All 92 kernel vectors are lifted from a modular sparse basis to rational
coefficients in `{-2,-1,-1/2,1/2,1,2}` and verified directly against the full
3876-coordinate tangent map. Every one of the 4,278 projected curvature vectors
is then reduced by exact fraction arithmetic against the 108-dimensional
projected tangent basis, with zero remainder.

Consequently the second fundamental form restricted to the full first-order
cancellation kernel is zero in the projected quotient, while the missing
summand remains outside that tangent space. A deleted standard summand cannot
first be absorbed at order two.

```text
core: e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
status: STRICT_LOCAL_SECOND_ORDER_ROUTE_BARRIER
```

This is local and order-bounded. Remote six-block representations,
singular/Puiseux paths, and third- or higher-order coalescence remain open.

## Coordinate degeneration results retained

### Two-supported regular two-jets

Every support-minimal rank-five circuit with six nonzero two-supported leading
matching projections is excluded at regular second order.

```text
core: 0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

### Corrected positive-singleton regular two-jets

```text
family                   row-column orbits   fixed-identity embeddings
square lollipop                    5                    216
double-edge tail                  29                    696
endpoint-marked P5                18                    696
```

All 130 repeated-factor singleton frames are included. Exact second-order
matching-support maxima are `22,22,23`, below the 24 matching coordinates of
`perm_4`.

```text
corrected core: cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223
superseded core: a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### Complete regular coordinate first-order barrier

A complete scan of all 54,264 coordinate six-frame multisets proves

\[
|E(\gamma)|+|S(\gamma)|\le6,
\]

and global cancellation gives `q>=8`. Thus every regular coordinate
first-order degeneration with `q<=7` misses a full-support `perm_4` target.

```text
core: 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

### Coordinate second-order equality-state collapse

The safe enlarged local envelope has maximum 20, attained by 288 frames in two
row-column orbits with profile `(12,0,8,8)`. On every equality frame,
componentwise order-zero and order-one vanishing force the order-two matching
projection to vanish.

```text
core: 938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
```

Global six-component coordinate cross-cancellation at second order remains
open and is distinct from the standard seven-block local chart.

## Validation

The two local-rigidity packets pass:

```text
21 rational pair-flattening checks                       PASS
seven first-order deletion ranks 108 -> 109             PASS
full tangent rank 574 and exact kernel dimension 92     PASS
92 rational kernel relations against 3,876 rows         PASS
4,278 exact polarized curvature reductions              PASS
independent monomial-tuple replay at prime 1,000,037     PASS
primary and independent python -O                        PASS
frozen JSON equality                                     PASS
focused tests: first order 6/6, second order 6/6         PASS
py_compile, no-bare-assert, English/ASCII scans           PASS
```

The current receipt must receive its own hosted Actions result before the
repository-wide suite is described as green.

## Exact next task

Only the six-block value remains undecided. Continue in this order:

1. decide whether the standard seven-block chart has a nonzero third
   fundamental form in the missing-summand quotient; stop the local route if
   it remains tangent or if the calculation ceases to constrain remote points;
2. search genuinely mixed six-block configurations through exact equations,
   using the seven-block formula only as a controlled boundary condition;
3. impose the inherited full-support six-element quotient circuit on all
   common-source layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`; and
4. seek either an exact six-block witness or a six-block zero theorem.

Do not return to broad scalar towers, simple sign-term deletion, or support-only
coordinate enumeration.

## Strict boundary

```text
five-block literal sum at (6,4) = ZERO
six-block literal sum at (6,4) = OPEN
seven-block literal sum at (6,4) = NONZERO
mu(6,4) = OPEN IN [6,7]
paired-column quartic threshold = 7
standard seven-block direct pair merge = ZERO
standard deleted-summand first-order absorption = ZERO
standard deleted-summand second-order absorption = ZERO
standard local third/higher absorption = OPEN
coordinate regular first-order q<=7 = ZERO
global coordinate second-order q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
