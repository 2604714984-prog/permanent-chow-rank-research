# Ledger delta: one-term Glynn compression

Add the following general explicit nonzero family:

\[
n\ge m+2\Longrightarrow \mu(n,m)\le2^{m-1}-1.
\]

The construction removes one Glynn term using the unique order-`m-2` Walsh
relation and places each difference of two tails in one degree-`m+2` Chow
derivative block.

At `(n,m)=(6,4)`:

```text
five blocks: ZERO (inherited)
six blocks: OPEN
seven blocks: NONZERO (current construction)
mu(6,4): OPEN IN [6,7]
```

Inside the paired-column family, seven is exact. The unrestricted ordinary
Chow-rank and border-rank boundaries do not change.
