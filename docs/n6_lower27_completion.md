# Completion of the ordinary lower bound twenty-seven for `perm_6`

## Status

`PURE_CHARACTERISTIC_ZERO_PROOF + EXACT_INTEGER_REPLAY` (N6-057).

Assuming the previously proved fixed-six reduction and term-profile
interfaces, N6-056 and the low-layer arithmetic below rule out every
hypothetical twenty-six-term Chow decomposition.  Therefore

```text
27 <= ChowRank(perm_6) <= 32.
```

The upper bound is Glynn's decomposition.  This note does not determine the
exact value and makes no border-rank claim.

## 1. Fixed-six reduction

Suppose, for contradiction, that

```text
perm_6 = T_1 + ... + T_26.
```

The proved N6-032/N6-038 selection theorem chooses six terms.  Put

```text
R = T_1+...+T_6,     Q = T_7+...+T_26,
H_3 = D_3(R),        E_3 = D_3(perm_6),
h = dim H_3,         b = dim(E_3 intersection H_3).
```

All previously established reductions leave only

```text
45 <= b <= 64.                                           (1.1)
```

The symmetric middle-catalectic quotient inequality gives

```text
rank C_(3,3)(Q) >= 400+h-2b.
```

Since `Q` is a sum of twenty Chow terms and one term has middle rank at most
twenty, the left side is at most 400.  Hence

```text
h <= 2b.                                                 (1.2)
```

N6-056 proves the exact product-shadow minimum for subspaces of `E_3` and
excludes every layer

```text
53 <= b <= 64.                                           (1.3)
```

It remains to exclude `b=45,...,52`.

## 2. Defect and relation bounds

Write

```text
F_i = D_2(T_i),       epsilon_i = 15-dim F_i.
```

Let `m_b` be the exact product-shadow minimum from N6-056 and put

```text
D_b = 78-m_b.
```

Differentiating `E_3 intersection H_3` and applying the six omitted-factor
projections gives

```text
sum_i epsilon_i - min_i epsilon_i <= D_b.                (2.1)
```

If `kappa_2` is the relation dimension among the six spaces `F_i`, the
refined quotient projection gives the conservative bound

```text
kappa_2 <= D_b-sum_i epsilon_i+min_i epsilon_i.           (2.2)
```

This bound deliberately drops the nonnegative individual intersection
defects.  Thus enumerating every epsilon profile satisfying (2.1) covers a
superset of all geometrically realizable states.

The exact individual term profiles are

```text
dim F_i           15   14   13   12   11   <=10
middle lower      20   20   18   --   14      0,
```

where quadratic dimension twelve is impossible.  Assigning zero to every
dimension at most ten is conservative.

The vector-valued degree-two Macaulay theorem gives

```text
rho_3 <= kappa_2^{<2>},
```

for the relation dimension among the six cubic derivative spaces.  The
block-Sylvester inequality therefore gives

```text
h >= sum_i c_i - 2 kappa_2^{<2>},                         (2.3)
```

where `c_i` is the displayed individual lower bound.

## 3. Exhaustive low-layer calculation

For every nondecreasing six-tuple `epsilon` in `{0,...,15}^6` satisfying
(2.1), the replay:

1. rejects the impossible quadratic dimension twelve;
2. uses the conservative individual middle bounds;
3. substitutes the largest allowed `kappa_2` from (2.2);
4. computes the exact Macaulay successor;
5. compares (2.3) with (1.2).

The complete results are

| `b` | `m_b` | `D_b` | feasible types | rank-12 types | `h` lower | `2b` | margin |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 45 | 72 | 6 | 24 | 7 | 98 | 90 | 8 |
| 46 | 72 | 6 | 24 | 7 | 98 | 92 | 6 |
| 47 | 75 | 3 | 6 | 1 | 112 | 94 | 18 |
| 48 | 75 | 3 | 6 | 1 | 112 | 96 | 16 |
| 49 | 75 | 3 | 6 | 1 | 112 | 98 | 14 |
| 50 | 75 | 3 | 6 | 1 | 112 | 100 | 12 |
| 51 | 78 | 0 | 1 | 0 | 120 | 102 | 18 |
| 52 | 78 | 0 | 1 | 0 | 120 | 104 | 16 |

The full JSON stores every feasible symmetric epsilon profile, not only the
minima.  At `b=45,46` the unique minimizing profile is

```text
(0,0,0,0,0,5),  kappa_2<=1,  rho_3<=1.
```

At `b=47,...,50` it is

```text
(0,0,0,0,0,0),  kappa_2<=3,  rho_3<=4.
```

At `b=51,52`, defect zero forces the sole profile `(0,...,0)` and no
quadratic or cubic relations.  Every margin is strictly positive, so every
low layer contradicts (1.2).

## 4. Conclusion

Equations (1.1), (1.3), and the low-layer table exhaust all possibilities.
Therefore a twenty-six-term decomposition cannot exist.  The already proved
ordinary lower bound twenty-six rules out shorter decompositions, and Glynn
gives thirty-two terms.  Hence

```text
27 <= ChowRank(perm_6) <= 32.
```

This is an ordinary Chow-rank result in characteristic zero.  The argument
does not prove border Chow rank at least twenty-seven and does not establish
that the ordinary rank is thirty-two.

## 5. Replay

```text
python scripts/n6_lower27_completion.py \
  --verify-json data/n6_lower27_completion.json
python -m unittest tests/test_n6_lower27_completion.py -v
```

The replay uses only integer enumeration and exact Macaulay arithmetic.  It
contains no random, floating-point, or finite-field inference.
