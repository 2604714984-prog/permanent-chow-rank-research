# General-`n` handoff: post-`perm_6` middle-symbol capacity

## Base

```text
base branch: main
base head: 107912a550cc4688b160e69008e7f7bb33650447
research branch: research/general-n-middle-symbol-capacity
```

## Established result

The repaired exact `perm_6` proof belongs to a precisely defined
single-middle-layer route. For every even `n`, that route can certify at most

\[
\binom{n}{n/2}+2n.
\]

It matches Glynn at `n=6` and is strictly below Glynn for every even `n>=8`.

## Current trusted numerical context

```text
ChowRank(perm_3)=4
ChowRank(perm_4)=8
ChowRank(perm_5)=16             repaired internal proof draft
ChowRank(perm_6)=32             repaired post-audit internal proof
50<=ChowRank(perm_7)<=64        current main proof draft
general exact value             OPEN
```

The `perm_6` theorem is a dependency frozen on its repaired proof/audit heads;
this branch does not duplicate its publication package.

## Next single task

Construct the smallest coupled two-degree quotient-symbol candidate that uses:

```text
one common factor quotient P:L(T)->D
the adjacent middle derivative spaces
the commutation relation between their differentiation maps
one joint, not additive, degenerate-term cap
```

Promotion requires all of:

```text
GL(V)-natural or orientation-independent
uniform cap for repeated/dependent factors
sum/subquotient inequality
strict gain over the single-middle ceiling
exact n=6 regression
nontrivial n=8 capacity
```

Do not return to finite `perm_6` block classification or build a generic solver
framework.
