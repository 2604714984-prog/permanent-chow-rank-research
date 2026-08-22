# Arbitrary nonzero weighted coupling by Schur products

## Status

`W-01-COMPLETE; W-02-COMPLETE; W-03-COMPLETE.`

Let `C3=im(E3)`, `R3=ker(E3^T)`, and `R4=ker(E4^T)`.  If
`D=diag(d_i)` has no zero entry and `w_i=d_i^{-1}`, then

`D^(-1) R4 subset C3`

holds exactly when

`w in (R3 star R4)^perp`.

Indeed, membership in `C3` is orthogonality to `R3`, so the inclusion is
equivalent to

`sum_i r3_i r4_i w_i=0`

for every `r3 in R3` and `r4 in R4`.

## Dense-torus criterion

Over an infinite field, a linear subspace `L` meets the coordinate torus iff
it is not contained in any coordinate hyperplane.  The forward implication is
immediate.  Conversely, if no coordinate vanishes identically on `L`, the
finitely many proper coordinate hyperplane sections cannot cover `L`.

Apply this to `L=(R3 star R4)^perp`.  Nondegeneracy of the coordinate pairing
gives

`L subset {w_i=0}` iff `e_i in R3 star R4`.

Thus arbitrary nonzero weighted coupling exists exactly when none of the 42
coordinate vectors belongs to the Schur span.  For a fixed point code this
replaces saturation by 42 exact membership tests in a matrix with at most 35
columns on the active frontier.

## Controls and boundary

The deterministic replay evaluates the three existing curve-union profile
controls over the two standard primes.  Those rows test matrix orientation and
the membership criterion only.  They do not satisfy the permanent target in
general and cannot close any F frontier from weighted coupling alone.

The theorem is used over characteristic zero (or any infinite field).  A
finite-field control is not itself a characteristic-zero nonexistence or
existence certificate for an arbitrary point component.
