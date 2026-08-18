# Research-ledger delta: closed factor-span endpoints

## Status

This delta is based on PR #67 head

```text
d7e2e5f4c1a767f1429a1b7ab17a4c4f3d9c3315
```

and belongs to the branch

```text
research/closed-factor-span-endpoint-zero-blocks
```

No numerical Chow-rank boundary changes in this result.

## New general theorem

For

```text
E_m=D_m(perm_n),
F_i=D_m(T_i),
L_i=factor span of T_i,
```

if `m>=3`, at least two factor spans form a direct sum, and their total
dimension is at most `m^2`, then

```text
E_m intersect sum_i F_i = 0.
```

Consequently, if

```text
q*n=m^2,
m>=3,
q>=2,
```

then every arbitrary `q`-term Chow block has zero permanent-relative
intersection.

Together with the prior strict theorem, the closed guaranteed zero-block size
is

```text
zeta(n,m)
 = floor((m^2-1)/n)
   + indicator(m>=3 and n divides m^2 and m^2/n>=2).
```

For any larger literal sum of `Q` terms,

```text
dim(E_m intersect sum_(i=1)^Q D_m(T_i))
 <= (Q-zeta(n,m))*binom(n,m).
```

## Sharp exceptions

```text
q=1, n=m^2:
  product of all m^2 block variables has embedded perm_m in its derivatives

m=2, n=2, q=2:
  perm_2 is the sum of its two matching monomials
```

## Route classification

```text
closed equality endpoint                    SOLVED
first uniform indecomposability defect       ESTABLISHED
near-endpoint q*n=m^2+s                      OPEN
new finite numerical lower bound             NO
general Glynn optimality                     OPEN
```

## Next authorized interface

Develop a quantitative small-excess theorem for

```text
q*n=m^2+s
```

that bounds the intersection dimension or forces a center/idempotent defect.
Another arbitrary-subspace scalar shadow estimate is not the default route.
