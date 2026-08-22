# Adversarial review: coordinate regular first-order closure

## 1. Does source sharing fail when factors repeat?

Yes, if stated naively. Distinct four-label subsets can specialize to the same
quartic monomial, cancel inside one component, and separate after the repeated
factors move differently. The proof does not discard this phenomenon. It
introduces the vertical set `V_i`, computes the source-fiber kernel exactly,
and charges every non-direct target of envelope degree one to `V_i`.

## 2. Is the envelope sufficient for an actual lift?

No. `E_i` is only a necessary support envelope. Using all of `E_i` can only
make a hypothetical lift easier, so the resulting contradiction is safe. No
coefficient sufficiency or integrability is inferred from support membership.

## 3. Are repeated factors and repeated unused factors included?

Yes. The frame audit ranges over all 54,264 multisets of six cells chosen from
sixteen cells. The primary implementation works with all fifteen four-label
source subsets and their exact monomial fibers. The independent implementation
uses the equivalent equal-label-swap description.

## 4. Why does a degree-one non-direct target have to be vertical?

A nonzero aggregate coefficient of its driving order-zero quartic monomial
must cancel coefficientwise in another component because the total order-zero
polynomial is zero. The three unchanged matching cells then put the target in
that other component's envelope. If no other envelope contains the target, all
driving aggregate coefficients vanish internally, which is precisely the
source-kernel case recorded by `V_i`.

## 5. Does the theorem cover singular degenerations?

No. It assumes regular factor families, regular source vectors, coordinate
specialization, and a first nonzero term at order one. Poles, multigrade
collision trees, noncoordinate initial factors, and second- or higher-order
first nonzero terms remain open.

## 6. Does this prove `mu(6,4)>=7`?

No. It closes one complete degeneration stratum but not every arbitrary
six-block intersection. The exact unrestricted interval remains
`6 <= mu(6,4) <= 8`, and no new ordinary or border Chow-rank bound is claimed.

## Verdict

Within its stated coordinate regular first-order boundary, the proof is
complete and includes the strongest known objection: internal source-fiber
cancellation from repeated factors.
