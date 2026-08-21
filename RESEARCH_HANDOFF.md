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
one-term Glynn compression theorem head: THIS COMMIT
publication receipt: PENDING
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Active unrestricted boundary

The inherited five-block theorem gives

\[
\mathcal D_4(\operatorname{perm}_6)
\cap
\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
\]

The current branch now supplies an explicit seven-block witness. Therefore

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

The ordinary Chow-rank interval is unchanged: a seven-block derivative-space
intersection is not a seven-term decomposition of `perm_6`.

## New explicit nonzero family

For every `m>=3` and `n>=m+2`,

\[
\boxed{\mu(n,m)\le2^{m-1}-1.}
\]

With `delta_1=1`, `chi(delta)=prod_r delta_r`, and
`L_(delta,j)=sum_r delta_r x_(rj)`, share `m-2` columns and call the remaining
two-column product `B_delta`. The missing-character Walsh relation is

\[
\sum_\delta \chi(\delta)A_\delta=0,
\qquad
A_\delta=\prod_{j=1}^{m-2}L_{\delta,j}.
\]

For any fixed `delta^0`, subtract this relation times `B_(delta^0)` from
Glynn's formula:

\[
\operatorname{perm}_m
=
2^{1-m}
\sum_{\delta\ne\delta^0}
\chi(\delta)A_\delta(B_\delta-B_{\delta^0}).
\]

Each summand lies in one degree-`m+2` Chow derivative block because its two
products share `m-2` independent factors and use four alternative tail
factors. Padding gives every larger `n`.

At `(m,n)=(4,6)` this is an exact seven-block witness. Frozen core:

```text
045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

Inside the broader paired-column family

```text
a_i(column 1) * b_i(column 2) * Q_i(columns 3,4),
```

seven is exact. The grouped contraction image of `perm_4` is the
six-dimensional symmetric zero-diagonal matrix space, which contains no
nonzero rank-one matrix; six separated terms are therefore impossible. Seven
retained sign outer products attain the bound.

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

and global cancellation gives

\[
\boxed{q\ge8}.
\]

Thus every regular coordinate first-order degeneration with `q<=7` misses a
full-support `perm_4` target.

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

The one-term compression packet passes:

```text
exact compressed identities for m=3,4,5,6        PASS
Walsh parity-mask relation for m=3,...,10         PASS
complete quartic 256-coefficient reconstruction   PASS
paired-column ranks 6 and 7 over Q                 PASS
independent bit-mask / modular replay              PASS
focused unit tests                                 5/5 PASS
primary and independent python -O                  PASS
py_compile                                         PASS
```

The parent corrected-singleton head triggered hosted run #860, which was still
in progress when this theorem packet was published. The current theorem commit
must receive its own hosted result before the full repository is called green.

## Exact next task

Only the six-block value remains undecided. The new paired-column lower bound
closes the most direct attempt to compress the seven-block witness again.
A six-block witness, if it exists, must use genuinely mixed four-column
frames or nontrivial ambient cancellation.

Proceed in this order:

1. test whether the seven-block formula has any six-term deformation outside
   the paired-column family while preserving all repeated-column cancellations;
2. impose the inherited full-support six-element quotient circuit on the
   common-source layers `(2,1,1)`, `(2,2)`, `(3,1)`, and `(4)`;
3. continue the global coordinate second-order compatibility system only when
   it supplies coefficient-level information beyond the now-sharp support
   envelopes; and
4. seek either an exact six-block witness or a six-block zero theorem.

Do not return to broad scalar towers, sign-term deletion, or support-only
coordinate enumeration. The order-`m-2` sign relation has codimension one, so
the current Glynn compression removes exactly one term and no more.

## Strict boundary

```text
five-block literal sum at (6,4) = ZERO
six-block literal sum at (6,4) = OPEN
seven-block literal sum at (6,4) = NONZERO
mu(6,4) = OPEN IN [6,7]
paired-column quartic threshold = 7
coordinate regular first-order q<=7 = ZERO
all-positive coordinate regular two-jets = CLOSED
global first-nonzero-order-two coordinate q=6 = OPEN
noncoordinate / singular / multigrade q=6 = OPEN
unrestricted Chow_rank_improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
