# Research-ledger delta: growing two-direction power profiles

## Status

This delta belongs to the stacked branch
`research/growing-two-direction-power-ceiling` and supplements the canonical
`RESEARCH_LEDGER.md` until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route theorem

For every differential subspace `W` of dimension at most two, every power
`p=p(n)` and every output degree `d`, define

```text
Lambda_(p,d)(A_f;W)=dim((W^p A_f)_d).
```

The permanent numerator and a uniform independent-term denominator satisfy

```text
Lambda_(p,d)(A_perm;W)
 <= min((p+1) binom(n,d-p)^2, binom(n,d)^2),

max_T Lambda_(p,d)(A_T;W)
 >= min(binom(n,d-p),binom(n,d)).
```

Consequently

```text
R_(n,p,d)
 <= H_* min(
      sqrt(p+1),
      n exp(-(p-1)^2/(4n))
    ) + 1,

H_*=binom(n,floor(n/2)).
```

Uniformly over `p,d,W`,

```text
R_n
 = O((n log(n+1))^(1/4) H_*)
 = O(2^n (log n)^(1/4) / n^(1/4))
 = o(2^(n-1)).
```

The same ceiling holds for every finite block-diagonal family of such power
profiles, even when the powers and number of blocks depend on `n`.

## Claim boundary

```text
new numerical Chow-rank lower bound=false
actual Chow-rank upper bound=false
all powers (s,t)^p=CLOSED AS A GLYNN ROUTE
powers p=p(n)=CLOSED
finite additive power-profile families=CLOSED

general growing binary ideals=OPEN
minimal/persistence syzygy functors=OPEN
nonlinear determinantal data=OPEN
valuative flat-sum data=OPEN
Chow-realizability defects=OPEN
exact rank for n>=6=OPEN
```

## Next authorized interface

Another maximal-ideal power calculation is not an authorized continuation.
Priority is now:

1. an `n`-dependent binary ideal with genuinely unrelated minimal generators
   and a proved common one-term envelope;
2. a minimal or persistence syzygy functor which survives the apolar
   subquotient gate;
3. nonlinear determinantal or valuative information; or
4. a uniform Chow-realizability defect.
