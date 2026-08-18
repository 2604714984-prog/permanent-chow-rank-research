# Research-ledger delta: quantitative private-polar shadow amplification

## New theorem

For a surviving `q`-term block with

```text
delta=m^2-(q-1)n>0,
```

some private polar space in `D_(m-1)(perm_n)` has dimension at least `delta`.
Therefore the block is impossible whenever

```text
F^(m-2)_(n,m-1)(delta)>n.
```

The exact first linear-shadow tiers are

```text
F(1)=(m-1)^2
F(b)=m(m-1)                 for 2<=b<=m
F(m+1)=m^2-1
F(b)>=m^2-1                 for b>=m+1.
```

## Consequences

```text
m>=4, q>=3, (q-1)n<m^2
    => zero block

m>=4, q=2, n<=m^2-m-1
    => zero pair.
```

The pair result extends the parent support-only range `n<(m-1)^2` by roughly another `m` orders.

## Exact next boundary

At

```text
q=2
n=m^2-m
delta=m
```

the exact product shadow is `F(delta)=n`, so the current argument stops at equality rather than from loss of constants.

## Claim boundary

No new exact Chow rank, no border-rank claim, and no literature-novelty claim is introduced. The next default target is classification of the pair equality boundary `n=m^2-m`.
