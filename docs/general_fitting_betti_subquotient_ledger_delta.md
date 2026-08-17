# Research-ledger delta: Fitting and Betti subquotient barrier

## Status

This delta belongs to the stacked branch
`research/fitting-betti-subquotient-barrier` and supplements the canonical
`RESEARCH_LEDGER.md` until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorem

### Quotient Fitting functoriality

For a surjection of finitely presented `k[s,t]`-modules,

```text
M ->> Q,
```

one has

```text
Fitt_i(M) subset Fitt_i(Q).
```

Direct sums obey the convolution formula

```text
Fitt_k(M direct_sum N)
 = sum_(i+j=k) Fitt_i(M)Fitt_j(N).
```

### Higher-Fitting submodule barrier

The same Fitting index can move in opposite ideal-order directions under
submodules:

```text
k -> k^2:
  Fitt_1(k)=R
  Fitt_1(k^2)=(s,t)

(s,t)/(s,t)^2 -> R/(s,t)^2:
  Fitt_1((s,t)/(s,t)^2)=(s,t)
  Fitt_1(R/(s,t)^2)=R.
```

Therefore the raw higher-Fitting profile is not a
subquotient-monotone invariant.

### Betti barrier

Finite-length examples show raw Betti numbers can increase under both halves
of the apolar subquotient:

```text
R/(s^2,t^2) ->> R/(s,t)^2:
  (1,2,1) -> (1,3,2)

(s,t)/(s,t)^2 ~= k(-1)^2 -> R/(s,t)^2:
  (2,4,2) -> (1,3,2).
```

Raw Betti and syzygy counts are not promoted.

### One-operator Fitting closure

For a finite-length `k[u]`-module

```text
M=direct_sum_i k[u]/(u^(lambda_i)),
```

the valuations of all Fitting ideals recover the complete Jordan partition.
Every additive subquotient-monotone scalar depending only on that partition is
a nonnegative combination of Jordan-tail counts.

The permanent/Boolean ratio of every Jordan tail is one binomial coefficient,
so the complete one-operator Fitting route is capped by

```text
binom(n,floor(n/2)).
```

This is the already closed one-direction Jordan scale, not a new lower bound.

## Claim boundary

```text
new numerical Chow-rank lower bound=false
raw higher Fitting profile=REJECTED
raw graded Betti tables=REJECTED
one-operator Fitting scalarizations=CLOSED AT CENTRAL BINOMIAL
all Fitt_0 valuations closed=false
joint two-dimensional determinantal data=OPEN
derived additive Fitting construction=OPEN
representation-valued syzygy envelope=OPEN
Chow-realizability defect=OPEN
border-rank improvement=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```

## Next authorized interface

The next default route must establish its functoriality before any rank ratio.
Priority is:

1. a genuinely two-dimensional determinant/minor construction with an
   additive subquotient-monotone scalar;
2. a representation-valued syzygy envelope with the same functoriality; or
3. a uniform Chow-realizability defect.

Another raw Betti table or one-line Fitting valuation is not an authorized
continuation.
