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
positive-singleton repair theorem head: a145811984bf0c7f937fde1b7ba9d3eb88e40aa5
publication receipt: PENDING
```

Keep the stack narrow. Do not add a manager, registry, database, generic
solver framework, or second control plane.

## Unrestricted boundary

For arbitrary degree-six Chow terms over a characteristic-zero field,

\[
\mathcal D_4(\operatorname{perm}_6)
\cap
\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
\]

Hence

\[
\boxed{6\le\mu(6,4)\le8},
\qquad
\boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

Six and seven unrestricted literal blocks remain open.

## Current coordinate results

### Two-supported regular two-jets

Every support-minimal rank-five circuit with six nonzero two-supported leading
matching projections is excluded at regular second order.

```text
core:
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

### Corrected positive-singleton regular two-jets

The exact support families and counts are

```text
family                   row-column orbits   fixed-identity embeddings
square lollipop                    5                    216
double-edge tail                  29                    696
endpoint-marked P5                18                    696
```

All 130 repeated-factor singleton frames are included. Exact second-order
matching-support maxima are `22,22,23`, below the 24 matching coordinates of
`perm_4`.

Hosted run #845 exposed two transcription defects in the superseded packet:
the square-lollipop pattern was typed as a triangle with an isolated vertex,
and the double-edge-tail fixed-identity count was typed as 888. Correct
patterns, exact normal forms, and an independent exhaustive replay reproduce
the same histograms and maxima. The route theorem is repaired, not withdrawn.

```text
corrected core:
cf26c24029832ce564bb462d47a94add93f9e706a9c825e1e57fe2ab7a84b223

superseded core:
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### Complete regular coordinate first-order barrier

For every unordered coordinate six-frame multiset `gamma`, exact exhaustion
of all 54,264 frames proves

\[
\boxed{|E(\gamma)|+|S(\gamma)|\le6}.
\]

Global order-zero cancellation then forces

\[
\boxed{q\ge8}.
\]

Thus every regular coordinate first-order degeneration with `q<=7` misses a
nonzero diagonal-torus transform of `perm_4`.

```text
core:
8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

This is a strict coordinate route theorem, not an unrestricted six- or
seven-block zero theorem.

### Second-order equality-state collapse

A safe enlarged second-order local envelope has maximum 20, attained by 288
frames in two row-column orbits with profile `(12,0,8,8)`. On every equality
frame, componentwise order-zero and order-one vanishing force the order-two
matching projection to vanish.

```text
core:
938fa79d2410032ec2d12ff917add00d1affaa7365be39241a1931197f0d4eb9
```

Global six-component cross-cancellation at second order remains open.

## Validation

The corrected positive-singleton packet passes primary and optimized Python,
an independent exhaustive replay in normal and optimized Python, frozen JSON
equality, five focused tests, and `py_compile`. A fresh hosted run must pass
before the repository-wide suite is described as green.

## Exact next task

Study the global six-component second-order compatibility system:

1. shared order-zero quartic source fibers;
2. global first-order cancellation;
3. second fundamental-form terms surviving those cancellations; and
4. equality and near-equality local profiles from the exact 54,264-frame table.

First test whether any useful local-plus-incidence inequality survives full
first-order integrability. If it is already vacuous for six components, stop
the coordinate support route and move to a coordinate-invariant
noncoordinate first-order theorem. Open a third-order expansion only for an
exact survivor.

## Strict boundary

```text
five-block literal sum = ZERO
six-block literal sum = OPEN
seven-block literal sum = OPEN
eight-block literal sum = NONZERO
mu(6,4) = OPEN IN [6,8]
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
all-positive coordinate regular two-jets = CLOSED
single-component internally vanishing equality-frame two-jet = MATCHING ZERO
global first-nonzero-order-two coordinate q=6 = OPEN
noncoordinate / singular / multigrade degenerations = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
