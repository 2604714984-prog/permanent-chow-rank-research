# Research-ledger delta: Koszul--Young and symmetry-projection ceilings

## Status

This delta stacks after PR #59.  It adds two general route ceilings and does
not alter any numerical Chow-rank boundary.

## New theorem 1: all standard Koszul--Young maps

For every standard exterior Koszul--Young flattening `K_(m,p)` of a degree-`n`
form in `n^2` variables, one independent-factor Chow term has rank at least one
quarter of the smaller term-side source and target dimensions.  The permanent
numerator is at most the central binomial coefficient times the same smaller
dimension.  Hence

```text
rank K_(m,p)(perm_n)
-----------------------------------------
max_T rank K_(m,p)(T)

<= 4*binom(n,floor(n/2)).
```

The same ceiling holds for every finite block-diagonal direct sum of standard
maps.

## New theorem 2: rectangular row--column symmetry projections

Let

```text
E_m ~= k[C([n],m)] tensor k[C([n],m)]
```

be the permanent derivative module.  For nonzero Johnson-isotype sums `A,B`,
project the catalecticant to `A tensor B`.

The permanent rank is `dim(A)*dim(B)`.  The diagonal Chow term

```text
product_i x_ii
```

induces diagonal comultiplication.  Its projected rank is at least
`max(dim(A),dim(B))`, by the transitive pointwise-multiplication lemma.
Therefore

```text
route ratio <= min(dim(A),dim(B)) <= binom(n,m).
```

The same ceiling holds for finite block-diagonal sums of rectangular
projections.

## Additional representation boundary

Pieri decomposition shows that the standard exterior differential has one
multiplicity-one common `GL(V)` hook between source and target.  An ambient
`GL(V)`-equivariant isotypic projection inserted immediately before or after
that differential either kills the map or leaves a scalar multiple.  It is not
a new flattening.

## Route decision

```text
standard exterior Koszul--Young maps, all wedge degrees=CLOSED
finite direct sums of standard maps=CLOSED
individual row-column isotype catalecticants=CLOSED
rectangular Johnson-isotype sums=CLOSED
finite block sums of rectangular projections=CLOSED
GL(V)-isotype projections around the standard delta stage=REDUNDANT

single nonrectangular row-column isotype unions=OPEN
row-column projected higher Koszul maps=OPEN
projections on the f-dependent catalecticant source=OPEN
arbitrary Pieri maps=OPEN
representation-valued higher syzygies=OPEN
Chow-realizability defects=OPEN
```

## Claim boundary

These are route ceilings, not upper bounds on actual Chow rank.  No finite-`n`
lower bound, border-rank statement, exact rank for `n>=6`, or general Glynn
optimality result is claimed.

## Next authorized interface

The next representation-valued route must use information not reducible to:

1. the unprojected standard exterior differential;
2. one rectangular row--column derivative isotype; or
3. a finite block sum of those rectangles.

The smallest remaining interfaces are a genuinely nonrectangular symmetry
projection sharing one source copy, a row--column projected higher Koszul map,
or a representation-valued higher syzygy with a uniform one-term envelope.
