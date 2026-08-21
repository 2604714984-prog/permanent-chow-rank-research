# Research handoff

Canonical operational handoff for the active permanent Chow-rank research
stack. Update this file with every synchronized mathematical result.

Last updated: **2026-08-21**

## GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
parent branch: research/quartic-six-term-frontier
parent PR: #89
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
active PR: pending creation after theorem commit
```

Keep this branch narrow. Do not add a manager, registry, database, general
solver framework, or second control plane.

## Current numerical boundary

For arbitrary degree-six Chow terms over a characteristic-zero field,

\[
\mathcal D_4(\operatorname{perm}_6)
\cap\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
\]

Consequently

\[
\boxed{6\leq\mu(6,4)\leq8},
\qquad
\boxed{28\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32}.
\]

Six and seven arbitrary quartic blocks remain open. Eight are nonzero by the
padded order-four decomposition.

## Current branch result

Assume the six leading matching projections in one `4 x 4` coordinate block
are nonzero, each is supported on exactly two perfect matchings, and the six
projective lines form a support-minimal rank-five circuit.

The support multigraph is one of

```text
simple six-cycle     row-column orbits 13
theta K_(2,3)        row-column orbits  1
tight handcuff       row-column orbits  5
loose handcuff       row-column orbits 18
```

All continuous circuit-gain strata are retained. Let `L` be the regular
common-source first-order map, `K=ker L`, and `B(K,K)` its polarized quadratic
matching contribution. Exact support maxima are

```text
six-cycle             6
theta                  5
loose handcuff         6
tight handcuff         8
perm_4                24
```

Hence no regular first- or second-order lift in this stratum has matching
projection equal to a nonzero diagonal-torus transform of `perm_4`.

Frozen theorem core:

```text
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

This is a strict route barrier, not a six-block zero theorem.

## Evidence

```text
docs/general_quartic_two_supported_coordinate_two_jet_barrier.md
docs/general_quartic_two_supported_coordinate_two_jet_barrier_adversarial_review.md
docs/general_quartic_two_supported_coordinate_two_jet_barrier_ledger_delta.md
scripts/general_quartic_two_supported_coordinate_two_jet_barrier.py
scripts/general_quartic_two_supported_coordinate_two_jet_barrier_independent.py
data/general_quartic_two_supported_coordinate_two_jet_barrier.json.xz
data/general_quartic_two_supported_coordinate_two_jet_symbolic_kernel_v2/manifest.json
data/general_quartic_two_supported_coordinate_two_jet_symbolic_kernel_v2/part-000.bin ... part-005.bin
tests/test_general_quartic_two_supported_coordinate_two_jet_barrier.py
```

Validation completed locally:

```text
certificate shard and digest checks           PASS
independent modular reconstruction            PASS
normal and python -O entry points             PASS
canonical frozen theorem core                 PASS
focused tests                                 PASS
py_compile                                    PASS
```

The branch also carries the one-line inherited CI correction replacing the
stale exact-product-shadow expectation `3563...` with the checked-in payload
hash `18eb...`. It does not change that theorem's payload.

## Next task

Close the remaining coordinate leading strata before any third-order or broad
nonlinear search:

1. support-minimal rank-five circuits with one singleton matching component;
2. those with two singleton components;
3. components with zero leading matching projection.

For each singleton retain the two unused coordinate factors in its degree-six
frame. Seek a complete coordinate two-jet exclusion, an exact survivor, or a
reduction to an already excluded separated family.

## Claim boundary

```text
five-block literal sum = ZERO
six-block literal sum = OPEN
seven-block literal sum = OPEN
eight-block literal sum = NONZERO
mu(6,4) = OPEN in [6,8]
two-supported coordinate regular two-jets = CLOSED
singleton coordinate components = OPEN
zero matching-projection components = OPEN
higher-order and noncoordinate lifts = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
