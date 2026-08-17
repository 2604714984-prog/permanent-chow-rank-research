# Research-ledger delta: Koszul--Young and symmetry-projection ceilings

## Status

This delta stacks after PR #59. It adds two general route ceilings and does not
alter any numerical Chow-rank boundary.

## New theorem 1: all standard Koszul--Young maps

For every standard exterior Koszul--Young flattening `K_(m,p)` of a degree-`n`
form in `n^2` variables, one independent-factor Chow term has rank at least one
quarter of the smaller term-side source and target dimensions. The permanent
numerator is at most the central binomial coefficient times the same smaller
dimension. Hence

```text
rank K_(m,p)(perm_n)
-----------------------------------------
max_T rank K_(m,p)(T)

<= 4*binom(n,floor(n/2)).
```

The same ceiling holds for every finite block-diagonal direct sum of standard
maps.

## New theorem 2: all row--column isotype-projected catalecticants

Let

```text
E_m ~= k[C([n],m)] tensor k[C([n],m)]
```

be the permanent derivative module, decomposed multiplicity-freely into
Johnson isotype pairs. For any arbitrary pair set `S`, project the
catalecticant onto the corresponding isotype union.

The permanent numerator is the total selected isotype dimension. For the
diagonal Chow term, the projected Gram operator is the sum of Johnson Schur
products. Krein positivity and the identities

```text
sum_k q_(i,j)^k d_k = d_i*d_j
sum_(i,j) q_(i,j)^k = binom(n,m)
```

show that the permanent numerator is at most `binom(n,m)` times the diagonal
term rank. Therefore every arbitrary, including nonrectangular, isotype-union
projection has route ratio at most

```text
binom(n,m).
```

The same ceiling holds for independent fixed source and target isotype filters
and for finite block-diagonal families.

## Additional representation boundary

Pieri decomposition shows that the standard exterior differential has one
multiplicity-one common `GL(V)` hook between source and target. An ambient
`GL(V)`-equivariant isotypic projection inserted immediately before or after
that differential either kills the map or leaves a scalar multiple. It is not
a new flattening.

## Route decision

```text
standard exterior Koszul--Young maps, all wedge degrees=CLOSED
finite direct sums of standard maps=CLOSED
individual row-column derivative isotypes=CLOSED
rectangular Johnson-isotype sums=CLOSED
arbitrary nonrectangular isotype unions=CLOSED
independent source/target row-column filters=CLOSED
finite block sums of catalecticant isotype filters=CLOSED
GL(V)-isotype projections around the standard delta stage=REDUNDANT

row-column projected higher Koszul maps=OPEN
arbitrary Pieri maps=OPEN
representation-valued higher syzygies=OPEN
Chow-realizability defects=OPEN
```

## Claim boundary

These are route ceilings, not upper bounds on actual Chow rank. No finite-`n`
lower bound, border-rank statement, exact rank for `n>=6`, or general Glynn
optimality result is claimed.

## Next authorized interface

The next representation-valued route must use information not reducible to:

1. the unprojected standard exterior differential;
2. any fixed row--column isotype filter of an ordinary catalecticant; or
3. a finite block sum of those maps.

The smallest remaining interfaces are a row--column projected higher Koszul
map, an arbitrary Pieri map, or a representation-valued higher syzygy with a
uniform one-term envelope.
