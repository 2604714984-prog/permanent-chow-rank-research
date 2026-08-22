# A common-quotient counterexample in the alpha-three stratum

## Status

`PURE_EXPLICIT_CONSTRUCTION + EXACT_QQ_REPLAY` (G-043).

This note disproves a proposed pair-intersection lemma.  Six actual
epsilon-zero, alpha-three Chow quadratic spaces can be literal direct and
still have one common quotient fifteen-plane.  The construction realizes
all quadratic scalar data of the final `b=60` state, but its cubic permanent
intersection is zero.  It therefore redirects, rather than closes, the
remaining problem.

## 1. The six terms

For `0<=r,c<=5` write `x_(r,c)` for the permanent variables.  Use the six
sign rows

```text
sigma_0 = (+,+,+,+,+,+),
sigma_i = (+,+,...,+,-,+,...,+),  1<=i<=5,
```

where the unique minus sign in `sigma_i` is in coordinate `i`.  Put

```text
ell_(i,c) = sum_r sigma_(i,r) x_(r,c),
T_i       = product_c ell_(i,c).
```

These are actual degree-six Chow terms.  Their quadratic and cubic derivative
spaces are

```text
F_i = span{ell_(i,c) ell_(i,d) : c<d},
C_i = span{ell_(i,c) ell_(i,d) ell_(i,e) : c<d<e}.
```

Thus `dim F_i=15` and `dim C_i=20`.

## 2. One common W15

For a fixed column pair `c<d`, expand

```text
ell_(i,c) ell_(i,d)
 = sum_r x_(r,c)x_(r,d)
   + sum_(r<s) sigma_(i,r)sigma_(i,s)
       (x_(r,c)x_(s,d)+x_(s,c)x_(r,d)).
```

Every parenthesized cross-row expression belongs to `E_2(perm_6)`.  Hence

```text
q(ell_(i,c)ell_(i,d))
 = q(sum_r x_(r,c)x_(r,d)),
```

independently of `i`.  The fifteen column-pair blocks are independent, so
all six quotient images equal the same fifteen-plane `W`.

## 3. Literal directness and the complete quadratic data

In one column-pair block, the six coefficient tensors are the rank-one
squares `sigma_i^2` in `Sym^2(k^6)`.  Project them to the six coordinates

```text
e_0^2, e_0e_1, ..., e_0e_5.
```

The resulting matrix has rows

```text
(1, sigma_(i,1), ..., sigma_(i,5)).
```

Subtracting its all-plus row from the other five rows gives `-2` times the
five coordinate vectors.  Its determinant is `(-2)^5`, so the six squares
are independent in characteristic zero.  Different column-pair blocks have
disjoint monomial support.  Consequently

```text
F_0 direct_sum ... direct_sum F_5,
d2 = 15*6 = 90.
```

The quotient of this 90-plane is `W`, of dimension fifteen.  Since the
kernel of `q` is `E_2`,

```text
a2 = dim(E_2 intersect sum_i F_i) = 90-15 = 75,
t2 = 15.
```

In particular every pair `F_i,F_j` has zero intersection despite having the
same `W`.  This is a strict characteristic-zero counterexample to the
proposed pair-intersection assertion.

## 4. Why it does not realize b=60

The same six-by-six minor proves that the six rank-one cubes `sigma_i^3`
are independent: use the coefficients of

```text
e_0^3, e_0^2e_1, ..., e_0^2e_5.
```

Therefore the twenty column-triple blocks give

```text
h = dim(C_0+...+C_5) = 20*6 = 120.
```

For a linear combination `sum_i a_i sigma_i^3` to be squarefree, the six
displayed repeated-row coefficients must vanish.  Their coefficient matrix
is the same invertible sign matrix, hence all `a_i` vanish.  The permanent
cubic space is squarefree in the row variables on every column-triple block,
so

```text
b = dim(E_3 intersect (C_0+...+C_5)) = 0.
```

The residual state requires `b=60`.  Thus the construction does not realize
that state.  It proves instead that the missing obstruction must use cubic
coupling; quadratic common-quotient geometry alone cannot suffice.

## 5. Replay and boundary

The replay constructs the symmetric-square and symmetric-cube coefficient
matrices over the integers and performs exact rational elimination.

```text
python scripts/n6_alpha3_common_quotient_counterexample.py \
  --verify-json data/n6_alpha3_common_quotient_counterexample.json
python -m unittest tests/test_n6_alpha3_common_quotient_counterexample.py -v
```

This counterexample refutes only the proposed pair-intersection lemma and a
purely quadratic exclusion route.  It neither supplies a permanent
decomposition nor excludes or realizes the `b=60` state, and it changes no
Chow-rank bound.
