# Research-ledger delta: the admissible `Fitt_0` order is linewise Jordan data

## Status

This delta supplements the Fitting/Betti barrier on the stacked branch
`research/fitting-betti-subquotient-barrier`.

No numerical Chow-rank boundary changes.

## New theorem

For a finite-length graded module over

```text
R=k[s,t], m=(s,t),
```

define

```text
nu_0(M)=ord_m Fitt_0(M).
```

For a generic linear form `v`, Fitting base change to a generic line gives

```text
nu_0(M)=dim_k M/vM.
```

The right side is the number of Jordan blocks of the nilpotent operator `v`.
Consequently `nu_0` is additive on direct sums and nonincreasing under
submodules and quotients.

For the permanent apolar algebra and the Boolean one-term envelope, generic
strong Lefschetz gives

```text
nu_0(A_perm_n)=binom(n,floor(n/2))^2
nu_0(B_n)=binom(n,floor(n/2)).
```

Thus the resulting Chow-rank lower bound is exactly

```text
binom(n,floor(n/2)).
```

The maximal-ideal order of `Fitt_0` is therefore admissible but belongs to the
already closed one-direction Jordan cone.

## Claim boundary

```text
new numerical Chow-rank lower bound=false
ord_m Fitt_0=ADMISSIBLE
ord_m Fitt_0=GENERIC JORDAN b_1
ord_m Fitt_0 route ceiling=CENTRAL BINOMIAL
all one-operator Fitting scalars=CLOSED BY JORDAN CONE
all Rees or arc valuations closed=false
joint two-dimensional determinantal data=OPEN
derived additive Fitting construction=OPEN
representation-valued syzygies=OPEN
Chow-realizability defects=OPEN
```

## Next authorized interface

A determinantal continuation must retain genuinely two-dimensional joint data.
Passing to a generic line, a single valuation, or one Jordan partition is no
longer an authorized default route.
