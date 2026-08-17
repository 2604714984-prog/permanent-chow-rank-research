# Research-ledger delta: graded K0 and exact-additive syzygy scalars

## Status

This delta belongs to the stacked branch
`research/graded-k0-syzygy-barrier` and supplements `RESEARCH_LEDGER.md` until
the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorem

### Graded Grothendieck group

For the category of finite-length graded `k[s,t]`-modules,

```text
K_0 ~= direct_sum_d Z [k(-d)]
[M] = sum_d dim(M_d) [k(-d)].
```

Every scalar invariant additive on all short exact sequences is therefore a
weighted graded Hilbert function:

```text
Phi(M)=sum_d c_d dim(M_d).
```

If the invariant is nonnegative or subquotient-monotone, all `c_d` are
nonnegative.

### Resolution Euler barrier

The full alternating numerator of a finite graded free resolution satisfies

```text
(1-z)^2 H_M(z)
  = sum_i (-1)^i sum_j beta_(i,j)(M) z^j.
```

Hence every syzygy scalar repaired to be genuinely exact-additive through a
full Euler characteristic factors through the Hilbert function. It no longer
retains the relation data discarded by the scalar derivative profile.

This does not include raw Betti numbers, one homological degree, truncated
alternating sums, or partial Euler characteristics.

### Permanent/Boolean ceiling

For `H_d=binom(n,d)`,

```text
dim(A_perm_n)_d = H_d^2
dim(A_T)_d <= H_d
```

for every Chow term, and one independent-factor term attains equality in every
degree. Thus every legal nonnegative exact-additive scalar satisfies

```text
Phi(A_perm_n) / max_T Phi(A_T)
  <= binom(n,floor(n/2)).
```

## Exact replay

Primary implementation:

```text
monomial staircase modules                 923
Hilbert/Betti numerator checks             923
corner short-exact checks                2,772
composition-factor degree cells         16,632
weighted permanent/Boolean ratios        2,183
exhaustive Boolean weight supports       4,079
```

Independent implementation:

```text
lattice-path staircase modules             791
independent numerator checks                791
cell-removal filtration checks           13,860
composition-factor cells                 13,860
disjoint large-n weighted ratios          3,420
independent Boolean supports             12,286
```

Frozen theorem core:

```text
8cabf216e75c6a3b83b56827f57d3689524cd94ef92120feecdd451743b6d23e
```

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
graded K0 scalarizations=CLOSED
full exact-additive resolution Euler data=CLOSED
exact functor dimensions factoring through K0=CLOSED

raw Betti tables=REJECTED BY PARENT AUDIT
partial Euler characteristics=OPEN
persistence and image-rank invariants=OPEN
minimal syzygy functors=OPEN
representation-valued envelopes=OPEN
nonlinear determinantal data=OPEN
valuative data=OPEN
Chow-realizability defects=OPEN
border-rank improvement=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```

## Next authorized interface

A relation-sensitive continuation must not repair raw Betti functoriality by
taking a full Euler characteristic: that collapses to the Hilbert profile.

The next candidate must retain non-exact information while still proving the
apolar gate. Priority is:

1. a persistence/image rank of a natural syzygy map not already covered by the
   fixed-matrix ceilings;
2. a representation-valued minimal-syzygy envelope with proved submodule and
   quotient monotonicity;
3. nonlinear joint determinantal data;
4. a valuative ordinary-rank obstruction; or
5. a uniform Chow-realizability defect.
