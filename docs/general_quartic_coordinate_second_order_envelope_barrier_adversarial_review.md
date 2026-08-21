# Adversarial review: coordinate second-order matching-envelope barrier

## Is `E_2(A)` the exact second-order image?

No. It is a necessary support envelope. A matching produced by two factor
motions retains at least two base cells, but membership in the envelope does
not guarantee compatible source coefficients or cancellation of lower-order
terms.

## Does the six-envelope cover construct a witness?

No. The cover ignores coefficients, nonmatching monomials, order-zero
cancellation, order-one cancellation, and integrability across source and
factor jets. It proves only that support counting cannot rule out the case.

## Could repeated factors enlarge the support maximum?

No. Repetition reduces the set of distinct cells. The scan includes every
support of size at most six, so all repeated-factor supports are covered by the
same upper bound.

## Is the equality classification dependent on numerical optimization?

No. All 14,893 supports are enumerated exactly. The independent replay checks
`|E_2|=2r_2-2r_3+3r_4` using integer matching counts. Equality supports are
exactly the 96 labeled `C6` graphs.

## Does this weaken the first-order closure theorem?

No. The first-order theorem uses the sharper three-unchanged-cell envelope and
source-kernel incidence budget. This note begins only at the first nonzero
second-order layer.

## Strict conclusion

The result is a route barrier for raw second-order matching support. It gives
no six-block construction, no improvement of `mu(6,4)`, no unrestricted Chow
rank or border-rank bound, and no literature-novelty claim.
