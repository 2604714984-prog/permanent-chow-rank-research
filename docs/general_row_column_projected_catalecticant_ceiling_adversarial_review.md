# Adversarial review: all row--column isotype-projected catalecticants

## Verdict

The central-binomial ceiling is valid for every fixed `S_n x S_n`-equivariant
projection of the permanent catalecticant onto an arbitrary union of
row--column Johnson isotype pairs, for independent source and target filters,
and for finite block-diagonal sums.

It introduces no new numerical Chow-rank lower bound.

## 1. The projection must be fixed and equivariant

The pair set is chosen independently of the Chow decomposition. Term-dependent
filters would destroy rank subadditivity. Because the Johnson module is
multiplicity free, every fixed equivariant idempotent is exactly a union of
isotype pairs; arbitrary nonequivariant projections are not covered.

## 2. The diagonal term is only a denominator witness

The proof uses

```text
T_Delta=product_i x_ii.
```

No claim is made that arbitrary Chow terms preserve row--column symmetry. A
single witness is sufficient to lower-bound the maximum one-term rank and
therefore to upper-bound the proof power of the route.

## 3. Krein positivity is characteristic-zero input

The proof extends scalars to the complex numbers and uses the nonnegative
Krein parameters of the symmetric Johnson association scheme. Ranks of the
rationally defined maps are unchanged by characteristic-zero scalar
extension. The theorem is not promoted to arbitrary positive characteristic.

## 4. Two Krein identities have different origins

The identity

```text
sum_k q_(i,j)^k d_k=d_i*d_j
```

comes from traces and the constant diagonal entries of primitive idempotents.
The identity

```text
sum_(i,j) q_(i,j)^k=binom(n,m)
```

comes from `(sum_i P_i) circ (sum_j P_j)=I`. Confusing either identity with an
unweighted sum over `k` invalidates the numerator budget.

## 5. Why arbitrary nonrectangular unions are now covered

For a selected pair set `S`, the diagonal-term Gram is

```text
G_S=(1/M)*sum_k q_S^k P_k.
```

Krein positivity makes its rank the sum of dimensions of the supported
primitive idempotents. The total permanent dimension is the weighted sum
`sum_k q_S^k d_k`, and every coefficient is at most `M`. No rectangular
factorization is needed.

## 6. Source and target filters

For different source and target pair sets, the permanent rank is the dimension
of their intersection. The diagonal-term filtered map contains the
compression corresponding to that intersection. Rank of a compression cannot
exceed rank of the full map. Applying the output-only theorem to the
intersection gives the same ceiling.

This argument relies on the complement identification under which the
permanent catalecticant is a scalar multiple of the identity.

## 7. Modular replay boundary

The modular scripts verify primitive idempotents, Schur-product supports and
all finite support masks. A nonzero modular coefficient is only a diagnostic
for the rational Johnson data. The general theorem is the characteristic-zero
Krein argument, not finite-field extrapolation.

## 8. Higher Koszul projections remain open

The theorem concerns ordinary catalecticants. The exterior factor in a higher
Koszul map carries additional row--column representation structure, and its
projected diagonal-term rank is not described by the present Johnson
Schur-product calculation.

## 9. Ambient `GL(V)` hook observation

Pieri multiplicity one closes only isotype projections inserted immediately
around the standard exterior differential. It does not classify arbitrary
Pieri maps or projections involving the f-dependent catalecticant source.

## 10. Final classification

```text
individual row-column isotype projections=CLOSED
rectangular Johnson-isotype sums=CLOSED
arbitrary nonrectangular isotype unions=CLOSED
independent source and target isotype filters=CLOSED
finite block-diagonal isotype-filter families=CLOSED
GL(V) projections around standard delta=REDUNDANT
row-column projected higher Koszul maps=OPEN
arbitrary Pieri maps=OPEN
representation-valued higher syzygies=OPEN
new numerical Chow-rank bound=NO
```
