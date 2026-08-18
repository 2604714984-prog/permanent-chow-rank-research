# Research-ledger delta: post-simplex small-excess bands

## Status

This delta belongs to the stacked branch

```text
research/excess-m-plus-four-band
```

above PR #76.  It does not alter the accepted small-order exact values or the
current optimized finite-order numerical table.

## New theorem

```text
m>=4, q>=2, q*n<=m^2+m+3
  => D_m(perm_n) intersect sum_i D_m(T_i)=0

m>=5, q>=2, q*n<=m^2+m+4
  => D_m(perm_n) intersect sum_i D_m(T_i)=0.
```

The proof combines:

1. the component-essential-space private-polar theorem;
2. strict derivative descent on every generic row;
3. exact two-plane iterated shadows on three small rows;
4. divisor arithmetic for the no-private branch; and
5. a new pair-supported polar lemma on the three nonstrict arithmetic rows.

## Exact exceptional rows

```text
private two-plane shadow:
  (m,s,n,q)=(4,6,11,2),(5,7,16,2),(5,9,17,2)

pair-supported polar:
  (m,s,n,q)=(6,9,9,5),(7,11,10,6),(12,16,16,10)
```

## Claim boundary

```text
new exact Chow rank                          NO
new optimized finite-n numerical bound      NO
ordinary characteristic-zero zero theorem   YES
quartic total q*n=24                        OPEN
m>=5 total q*n=m^2+m+5                      OPEN
cubic (4,3,3),(6,3,2)                       OPEN
cubic (3,3,4)                               SHARP NONZERO
border rank                                 NOT CHANGED
literature novelty                          NOT ESTABLISHED
```

## Evidence

```text
docs/general_excess_m_plus_four_band.md
docs/general_excess_m_plus_four_band_adversarial_review.md
scripts/general_excess_m_plus_four_band.py
scripts/general_excess_m_plus_four_band_independent.py
data/general_excess_m_plus_four_band_boundary.json
tests/test_general_excess_m_plus_four_band.py
```

No manager, registry, dispatcher, database or second control plane is added.
