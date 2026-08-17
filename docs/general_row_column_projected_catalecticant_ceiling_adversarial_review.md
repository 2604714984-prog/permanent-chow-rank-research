# Adversarial review: rectangular row--column projected catalecticants

## Verdict

The route ceiling is valid for the named rectangular symmetry projections and
finite block-diagonal sums.  It introduces no new numerical Chow-rank lower
bound.

## 1. The projection must be fixed and linear

The map `rho_m` is defined once in the ambient monomial basis.  It is linear in
`f` and row--column equivariant.  Choosing a projection after seeing the Chow
term would invalidate rank subadditivity and is not permitted.

## 2. The diagonal term is a denominator witness, not a restriction

The maximum one-term rank is bounded below using

```text
T_Delta=product_i x_ii.
```

No claim is made that every Chow term is diagonal or row homogeneous.  One
witness is sufficient for an upper ceiling on a rank-ratio method.

## 3. Why the multiplication lemma applies

The Johnson isotype sums are self-dual nondegenerate submodules under the
standard invariant pairing.  The transpose of the projected diagonal map is
pointwise multiplication.  The nowhere-zero vector argument requires an
infinite field; characteristic zero supplies this.

## 4. Rectangular versus arbitrary isotype unions

The theorem covers one target `A tensor B` and block-diagonal sums of such
targets.  A single projection onto an arbitrary nonrectangular collection of
pairs `(i,j)` shares one source copy across all selected components.  Its
one-term rank is not the sum of the component ranks.  That case is explicitly
open.

## 5. Permanent numerator

The statement

```text
rank on perm_n = dim(A)*dim(B)
```

uses two facts: the permanent catalecticant is onto the full subpermanent
space, and `rho_m` is the identity on that space.  It is not a generic-rank
assumption.

## 6. GL(V) hook projection boundary

The multiplicity-one Pieri argument concerns projections inserted around the
standard exterior differential.  It does not classify arbitrary Young/Pieri
flattenings or projections on the f-dependent catalecticant source.

## 7. Finite-field boundary

Modular projector ranks are used only as exact finite diagnostics and
characteristic-zero lower bounds.  The theorem itself is proved over an
infinite characteristic-zero field by the multiplication lemma.

## 8. Final classification

```text
individual row-column isotype projections=CLOSED
rectangular sums of Johnson isotypes=CLOSED
finite block-diagonal rectangular families=CLOSED
GL(V)-isotype projections of the standard delta stage=REDUNDANT
arbitrary nonrectangular isotype union=OPEN
row-column projected higher Koszul maps=OPEN
arbitrary Pieri maps=OPEN
representation-valued higher syzygies=OPEN
new numerical Chow-rank bound=NO
```
