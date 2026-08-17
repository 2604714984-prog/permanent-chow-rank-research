# Research-ledger delta: exact higher-Koszul term ranks

## Status

This delta belongs to the stacked branch
`research/general-higher-koszul-term-rank` and supplements the canonical
`RESEARCH_LEDGER.md` until the active stack is consolidated.

No numerical Chow-rank boundary changes.

## New general theorem

For an independent degree-`n` Chow term in an ambient space of dimension
`N=n^2`, the higher-Koszul differential

```text
D_d(T) tensor Lambda^p(V)
  -> D_(d-1)(T) tensor Lambda^(p+1)(V)
```

has the exact rank

```text
sum_q C(N-n,p-q)
  sum_h C(n,h)
        C(n-h,d+q-2h)
        C(d+q-2h-1,d-h-1).
```

The proof decomposes the map by inactive wedge support, active
monomial/wedge intersection, and active union. Every block is an oriented
simplex-boundary map.

The same ranks satisfy the independent complete-intersection recurrence

```text
R_(n,d,p)+R_(n,d+1,p-1)
 =
C(n,d)[C(n^2,p)-C(n^2-n,p-d)]
```

and the Gorenstein duality

```text
R_(n,d,p)=R_(n,n-d+1,n^2-p-1).
```

Degenerate Chow terms have no larger rank by specialization.

## Resolved finite interface

The previous `n=6,p=2` one-term rank window is now exact:

```text
d=2:  8,730
d=3: 12,066
d=4:  9,235.
```

This does not improve the current unrestricted `perm_6` boundary.

## Low-wedge route barrier

Put

```text
r=min(p,n^2-p-1).
```

For `r<=n^2-n`, every single higher-Koszul rank-ratio method is bounded by

```text
C(n,floor(n/2))
*
C(n^2,r)/C(n^2-n,r).
```

Consequently:

```text
r=o(n log n)
  => route ceiling =
     n^(o(1))*C(n,floor(n/2))
  => cannot reach 2^(n-1).
```

If `r=o(n^2)`, reaching Glynn scale through this mechanism requires

```text
r >= (1/2-o(1))*n*log(n).
```

Thus fixed exterior order, `O(n)` exterior order, and the complete
`o(n log n)` exterior-distance range are closed.

## Claim boundary

```text
new numerical Chow-rank lower bound=false
exact independent-term denominator=SOLVED FOR ALL n,d,p
degenerate-term denominator cap=VALID BY SPECIALIZATION
n6 p2 one-term ambiguity=RESOLVED
fixed exterior order reaches Glynn=false
O(n) exterior order reaches Glynn=false
o(n log n) exterior distance reaches Glynn=false
middle-wedge higher Koszul=OPEN
permanent-side middle-wedge rank=OPEN
representation-valued Koszul homology=OPEN
recursive or multimap compatibility=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```

## Next authorized interface

The next higher-Koszul continuation must address the middle-wedge range. It
must either:

1. prove a uniform middle-wedge route ceiling;
2. certify a permanent-side middle-wedge rank in characteristic zero; or
3. retain representation-valued Koszul homology instead of only total image
   dimension.

Another fixed or low exterior degree is not an authorized default route.
