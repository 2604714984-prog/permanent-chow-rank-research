# Research-ledger delta: Koszul--Young and representation-projected catalecticants

## Status

This delta belongs to the stacked branch
`research/koszul-young-and-projected-catalecticant-ceilings` and supplements
the canonical `RESEARCH_LEDGER.md` until the open stack is consolidated.

No numerical Chow-rank boundary changes in this result.

## New route ceilings

### Complete standard Koszul--Young family

For every standard exterior Koszul--Young flattening `K_(m,p)`, one
independent-factor Chow term has rank at least one quarter of the smaller
term-side source and target dimensions.  The permanent numerator is at most
the central binomial coefficient times the same smaller dimension.  Hence

```text
rank K_(m,p)(perm_n)
-----------------------------------------
max_T rank K_(m,p)(T)

<= 4*binom(n,floor(n/2)).
```

The same ceiling holds for every finite block-diagonal direct sum over output
and wedge degrees.

### Row--column representation-projected catalecticants

Let `W` be an arbitrary `S_n x S_n`-stable subspace of the degree-`m`
subpermanent module.  Compose the catalecticant with the canonical matching
projection and the projection to `W`.

For the permanent the rank is `dim W`.  The diagonal Chow term gives the
transitive diagonal-compression lower bound

```text
one-term rank >= dim(W)/binom(n,m).
```

Therefore every such projected route is capped by

```text
binom(n,m),
```

and every finite block sum is capped by the central binomial coefficient.
This includes arbitrary sums of row--column isotypes, not only one irreducible
component.

### Ambient `GL(V)` projection redundancy

Pieri multiplicity one shows that the standard exterior differential maps
only the common hook `S_(m,1^p)V`.  Equivariant pre/post-projections at this
stage either retain the map up to scalar or kill it.

## Route decision

```text
unprojected standard Koszul--Young maps        CLOSED
all standard wedge degrees                    CLOSED
finite direct sums of standard maps           CLOSED
GL(V)-equivariant delta projections           REDUNDANT
row-column projected catalecticants            CLOSED
arbitrary stable catalecticant isotype sums    CLOSED
finite block sums of projected catalecticants  CLOSED

row-column projections inside Koszul complexes OPEN
arbitrary Pieri maps                           OPEN
representation-valued syzygies                 OPEN
joint determinantal data                       OPEN
Chow-realizability defects                     OPEN
```

## Claim boundary

These are route ceilings, not upper bounds on actual Chow rank.  They add no
finite-`n` lower bound and do not close representation-selective higher
relation complexes.

## Next authorized interface

The next default representation route must retain relations that disappear
under a projected derivative image.  Priority is:

1. row--column isotype projections inside a higher Koszul/Young complex;
2. arbitrary Pieri maps with a uniform all-Chow one-term envelope;
3. representation-valued syzygy modules with proved functoriality; or
4. a uniform Chow-realizability defect.

Another unprojected wedge degree or projected catalecticant is not an
authorized continuation.
