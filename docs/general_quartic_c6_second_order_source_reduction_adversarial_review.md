# Adversarial review: canonical `C6` second-order source reduction

## Does the nine-dimensional kernel use only frame-level constant weights?

No. The ninety source coordinates are retained separately. The kernel is
computed coefficientwise in the coordinate quartic monomial basis. Twelve
sources per frame are unique and must vanish; the remaining eighteen source
coordinates pair into nine independent differences.

## Could a four-cell monomial occur in three frames?

No. A four-cell source shared by two frames is the complete intersection of
those frames and is labeled by their unique common matching cell. Exactly two
permutations in `S_3` contain a prescribed cell. Triple sharing is impossible.

## Are common first-order tangent monomials missed when sources share only one cell?

No. A quartic one factor motion away from each of two squarefree quartic
monomials must have monomial gcd of degree at least two. Same-row or same-column
cross modes intersect in only one cell, so they cannot share a tangent
monomial. Nonattacking modes intersect in two cells and have exactly four
common tangent channels.

## Does the graph reduction include repeated factors?

The six canonical equality frames have six distinct coordinate factors, so
there are no repeated-factor source fibers in this subcase. Repeated frames are
covered by the preceding general first-order theorem but are not part of this
canonical six-`C6` second-order interface.

## Does the reduction prove the canonical cover impossible?

No. It reduces the coefficient problem to nine order-zero source weights and
eighteen cross-target channels. The edge-weighted first-order kernel and its
quadratic image still have to be computed with all nonmatching equations.

## Strict conclusion

This is an exact reduction, not a zero theorem or construction. It gives no new
unrestricted Chow-rank or border-rank bound and makes no novelty claim.
