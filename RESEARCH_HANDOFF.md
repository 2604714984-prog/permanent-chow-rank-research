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
seven-block local-rigidity packet head: 44021026bb7fb0e2a46c69f927d83cd022b86732
current handoff receipt: THIS COMMIT
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active unrestricted boundary

The inherited five-block theorem and the explicit compressed Glynn witness give

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

For every `m>=3` and `n>=m+2`, the missing full Walsh character at tensor order
`m-2` removes one term from Glynn's formula and gives

\[
\boxed{\mu(n,m)\le2^{m-1}-1.}
\]

At `(m,n)=(4,6)` this is an exact seven-block witness. Frozen core:

```text
045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

Inside the paired-column family `a_i(column 1)b_i(column 2)Q_i(columns 3,4)`,
seven is exact. The six-dimensional symmetric zero-diagonal contraction image
contains no nonzero rank-one matrix, so six paired-column terms are impossible.
A six-block witness must therefore use genuinely mixed frames or ambient
cancellation outside that family.

## Local rigidity of the standard seven-block witness

Write the seven signed standard summands as

\[
G_v=\chi(v)v\otimes v\otimes(v\otimes v-w\otimes w),
\qquad v\ne w=(1,1,1,1).
\]

Two exact local compression mechanisms are now closed.

### Direct pair merge

For every one of the 21 pairs, the four mode-rank profile of `G_u+G_v` is

```text
(2,2,3,3)
```

and its essential dimension is ten. Every quartic in one degree-six Chow
derivative block has essential dimension at most six. Hence no two standard
summands can be replaced directly by one block.

### Infinitesimal deletion and absorption

The complete `(1,1,1,1)` column-multidegree tangent projection of one standard
block has 28 raw generators and exact dimension 18. After deleting any one of
the seven summands, the other six projected tangent spaces have exact rank 108;
adjoining the missing summand raises the rank to 109. This holds at two primes,
and the analytic upper bound `6*18=108` transfers the result to characteristic
zero.

Thus the missing summand is not tangent to the six-block addition image at the
standard six-tuple. It cannot be absorbed by a first-order deformation of the
other six standard blocks.

```text
core: 7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
status: STRICT_LOCAL_ROUTE_BARRIER
```

This is local only. Remote six-block representations, singular/Puiseux paths,
and higher-order coalescence remain open.

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

### Second-order equality-state collapse

The safe enlarged local envelope has maximum 20, attained by 288 frames in two
row-column orbits with profile `(12,0,8,8)`. On every equality frame,
componentwise order-zero and order-one vanishing force the order-two matching
projection to vanish.

```text
core: 938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
```

Global six-component cross-cancellation at second order remains open.

## Validation

The local-rigidity packet passes:

```text
21 rational pair-flattening checks                    PASS
one-block projected tangent rank 18                   PASS
seven deletion ranks 108 -> 109 at two primes         PASS
independent six-factor / 15-source-subset replay       PASS
primary and independent python -O                      PASS
frozen JSON equality                                   PASS
focused unit tests                                  6/6 PASS
py_compile and no-bare-assert checks                    PASS
English / ASCII proof-tree scan                         PASS
```

Hosted run #870 for the preceding branch head was still in progress when this
packet was published. The current receipt must receive its own hosted result
before the repository-wide suite is described as green.

## Exact next task

Only the six-block value remains undecided. Continue in this order:

1. compute the second fundamental form of the six standard retained blocks
   modulo their 108-dimensional projected tangent sum and test whether the
   missing summand can first appear at order two;
2. search mixed-column six-block candidates only through exact linear or
   polynomial interfaces, using the seven-block formula as a controlled base;
3. impose the inherited full-support six-element quotient circuit on the
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
coordinate regular first-order q<=7 = ZERO
global first-nonzero-order-two coordinate q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
