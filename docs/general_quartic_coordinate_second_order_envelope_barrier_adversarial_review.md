# Adversarial review: corrected coordinate second-order envelopes

## What failed in the superseded packet?

The scan included all supports, but the expected maximum was hard-coded as 14.
The actual unrestricted scan returns 18. The omitted equality family consists
of punctured row-column crosses with degree sequences `(3,1,1,1)` on both
sides. This is a mathematical scope error, not a floating-point or CI issue.

## Is 14 still useful?

Yes, but only with the explicit additional hypothesis that every row and every
column has degree at most two. Under that cap the 96 C6 supports are exactly the
equality locus. The canonical fixed-`3 x 3` C6 cover lies entirely in this
restricted family.

## Does the corrected maximum produce a witness?

No. `E_2(A)` is only a necessary support envelope. It ignores coefficients,
nonmatching monomials, order-zero and order-one cancellation, repeated-label
source kernels, and integrability.

## Are repeated factors covered?

Yes. Repetition can only reduce the distinct support. The scan includes every
support of size at most six.

## Strict conclusion

The corrected theorem is a support diagnostic. It preserves the conclusion
that support counting alone is insufficient, but it retracts the false global
number 14. It gives no six-block construction, no new ordinary Chow-rank or
border-rank bound, and no novelty claim.
