# Research-ledger delta: multiblock polar descent

## Status

This delta belongs to the stacked branch

```text
research/multiblock-polar-descent
```

above PR #79. It introduces no new best finite-order numerical lower bound and
does not alter the accepted exact values for `perm_3`, `perm_4` or `perm_5`.

## New theorem

If `z` terms have zero permanent-relative intersection in output degree
`d-1`, then

```text
z + floor((d^2-1)/n)
```

terms have zero intersection in output degree `d`.

Starting from the strict factor-span seed gives

```text
Z_(n,m)=sum_(d=2)^m floor((d^2-1)/n).
```

Every arbitrary block of at most `Z_(n,m)` degree-`n` Chow terms is invisible
to `D_m(perm_n)`.

## Mechanism

Discard

```text
a=floor((d^2-1)/n)
```

component essential spaces. Their total dimension is below `d^2`, while a
nonzero permanent degree-`d` derivative has essential dimension at least
`d^2`. A covector annihilating the discarded components but not the permanent
essential space produces a nonzero degree-`d-1` polar supported on the
remaining labels.

## Scale and boundary

For `m=floor(alpha*n)`,

```text
Z_(n,m)=(alpha^3/3)n^2+O(n).
```

The direct top-degree rank consequence is polynomial and is no stronger than
the central-binomial lower bound for `n>=4`. The theorem is valuable as a hard
zero seed for the exact capacity tower, not as a direct route to Glynn
optimality.

## Evidence

```text
docs/general_multiblock_polar_descent.md
docs/general_multiblock_polar_descent_adversarial_review.md
scripts/general_multiblock_polar_descent.py
scripts/general_multiblock_polar_descent_independent.py
data/general_multiblock_polar_descent.json
tests/test_general_multiblock_polar_descent.py
```

## Next authorized interface

Insert the closure

```text
Zhat_(n,d)=max(
  direct_seed_(n,d),
  Zhat_(n,d-1)+floor((d^2-1)/n)
)
```

as hard zero rows in the prefix min-plus derivative tower, then measure exact
finite thresholds and the scalar-tower ceiling. Do not report an improvement
before exact replay.

No manager, registry, dispatcher, database or second control plane is added.
