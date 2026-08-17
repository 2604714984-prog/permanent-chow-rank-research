# Research-ledger delta: two-sided matching-source compression

## Status

This delta belongs to the stacked branch
`research/two-sided-matching-source-ceiling` and supplements the canonical
`RESEARCH_LEDGER.md` until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorems

### Canonical effective source

For the degree-`m` permanent derivative module `E_m`, the equivariant source
section `J_m` satisfies

```text
Q_m C_perm J_m=I_(E_m).
```

For a permutation-matching Chow term,

```text
Q_m C_(T_sigma) J_m
  =(m!(n-m)!)^(-1) P_sigma,
```

where `P_sigma` is the coordinate projector onto the matching graph subspace.

### Symmetric two-sided compression

For every subspace `U subset E_m`, with no invariance assumption,

```text
rank(P_U Q_m C_perm J_m P_U)
----------------------------------------
max_T rank(P_U Q_m C_T J_m P_U)

<= binom(n,m).
```

The proof averages positive graph compressions.

### Distinct equivariant pre/post maps

The row--column module `E_m` is multiplicity-free. Arbitrary
`S_n x S_n`-equivariant endomorphisms before and after the effective
catalecticant act by scalars on irreducible summands. Their common nonzero
support reduces to the same positive-compression theorem, giving the same
ceiling.

A finite block-diagonal family across derivative degrees is capped by

```text
binom(n,floor(n/2)).
```

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
canonical matching-source section=closed
same-subspace non-equivariant two-sided compression=closed
row-column equivariant source projections=closed
row-column equivariant target projections=closed
equivariant pre/post endomorphisms=closed
finite block sums=closed

unrelated non-equivariant source/target spaces=open
source kernel directions outside J_m(E_m)=open
minimal syzygy functors=open
nonlinear determinantal data=open
valuative data=open
Chow-realizability defects=open
exact rank for n>=6=open
```

## Next authorized interface

A source-sensitive continuation must no longer use another row--column
isotype projection through the effective matching source. It must instead use
at least one of:

1. differential-source directions in the kernel of the permanent
   catalecticant;
2. unrelated non-equivariant source and target spaces with a proved uniform
   one-term envelope;
3. a minimal representation-valued syzygy functor;
4. nonlinear joint determinantal information; or
5. a valuative or Chow-realizability obstruction.
