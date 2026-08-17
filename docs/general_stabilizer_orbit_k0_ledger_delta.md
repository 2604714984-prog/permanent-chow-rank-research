# Research-ledger delta: stabilizer-efficient equivariant orbit barrier

## Status

This delta belongs to the stacked branch
`research/stabilizer-efficient-orbit-barrier` and supplements the canonical
`RESEARCH_LEDGER.md` until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorem

For a `G`-invariant decomposition `f=sum_i T_i`, let `H_i` be the projective
apolar stabilizer of `T_i`. The quotient by the intersection of the distinct
orbit ideals embeds in

```text
direct_sum_i Ind_(H_i)^G A_(T_i)
```

and surjects onto `A_f`. Thus `A_f` is an equivariant subquotient of the
smallest distinct-orbit envelope.

For `G=S_n x S_n`, the independent-factor Chow locus contains generic terms
with trivial projective stabilizer. Their efficient orbit envelope is

```text
k[G] tensor B_n.
```

Every nonnegative exact-additive graded isotype scalar is therefore dominated
coefficientwise by one generic term orbit. The resulting permanent/one-term
route ratio is at most one.

## Route classification

```text
full-group exact-additive orbit profiles          CLOSED
stabilizer-efficient distinct-orbit profiles      CLOSED
exact-additive row-column isotype scalarizations  CLOSED WITH CEILING ONE

fixed natural maps linear in f                    OPEN
minimal/persistence syzygy functors               OPEN
nonlinear determinantal data                      OPEN
valuative flat-sum data                           OPEN
Chow-realizability defects                        OPEN
```

## Evidence

```text
docs/general_stabilizer_orbit_k0_barrier.md
docs/general_stabilizer_orbit_k0_barrier_adversarial_review.md
scripts/general_stabilizer_orbit_k0_barrier.py
scripts/general_stabilizer_orbit_k0_barrier_independent.py
data/general_stabilizer_orbit_k0_barrier.json
tests/test_general_stabilizer_orbit_k0_barrier.py
```

Frozen theorem core:

```text
bf3defd92cc779905b2c676bc507fc7b03c7b5c1ad515f64393793ad2227782f
```

## Next authorized interface

A representation-valued continuation must no longer rely on exact-additive
symmetrization of arbitrary summands, even after removing duplicate orbit
copies. It must use a fixed natural map, non-exact relation data with proved
functoriality, nonlinear determinantal information, a valuation, or a
Chow-realizability theorem.
