# A nonisotropic one-relation Chow pair

## Status

`PURE_EXPLICIT_COUNTEREXAMPLE + EXACT_QQ_REPLAY` (G-044).

This note disproves a proposed shortcut at the `b=34` endpoint of the
ordinary lower-28 program.  A one-dimensional central relation among
full-middle-rank sextic Chow terms need not be isotropic.  Equivalently, the
central rank defect need not be even.

## 1. Explicit terms

Work in six variables `x0,...,x5`.  Put

```text
T1 = x0*x1*x2*x3*x4*x5
```

and let `T2` be the product of the six linear forms whose coefficient rows
are

```text
( 1, 1, 0,-1, 0, 0)
( 0, 0, 0,-1, 1, 0)
( 0, 0, 0,-1, 0,-1)
(-1, 0,-1, 0, 0, 0)
( 0, 0, 1, 0,-1, 0)
(-1, 0, 0,-1, 0, 1).
```

This integer matrix has determinant one.  Hence both terms have six
independent factors and their middle derivative spaces have dimension
twenty.

## 2. The unique relation

Index the twenty squarefree triple products of each factor frame in
lexicographic three-subset order.  Exact elimination on the resulting
`56 by 40` integer coefficient matrix gives rank 39.  Thus

```text
dim(D_3(T1)+D_3(T2)) = 39,
dim(D_3(T1) intersection D_3(T2)) = 1.
```

The replay stores an explicit integral generator of the one-dimensional
relation kernel and verifies its residual coefficient-by-coefficient.

For an independent-factor Chow term, the induced nondegenerate central form
pairs a frame triple with its complementary frame triple.  On the two
components of the displayed relation, the exact self-pairing values are

```text
-24 and 0.
```

Therefore the direct-sum relation form has value `-24`, so its restriction
to the one-dimensional relation space has rank one.  The relation is
nonisotropic.

The relation-pairing identity consequently predicts

```text
rank C_(3,3)(T1+T2) = 40 - 2*1 + 1 = 39.
```

As an independent exact check, the replay expands `T1+T2`, constructs its
full `56 by 56` central catalectic over the integers, and obtains rational
rank 39 directly.

## 3. Consequence and boundary

The construction proves that neither of the implications

```text
one central relation  =>  isotropic relation,
one central relation  =>  central defect at least two
```

is valid for sextic Chow terms.  Hence the near-direct residual at the
lower-28 `b=34` endpoint cannot be excluded by relation parity or the scalar
relation dimension alone.

This example contains only two terms.  It is not a 27-term decomposition of
`perm_6`, does not realize the required 366- or 367-dimensional relative
intersection with `E_3(perm_6)`, and does not prove or refute ordinary lower
28.  It makes no border-rank claim.

## 4. Replay

```text
python scripts/n6_pairing_parity_counterexample.py \
  --verify-json data/n6_pairing_parity_counterexample.json
python -m unittest tests/test_n6_pairing_parity_counterexample.py -v
```

All ranks use exact rational elimination.  There is no random, floating-point,
or finite-field inference.
