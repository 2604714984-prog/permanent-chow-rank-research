# Adversarial review: full-quotient Koszul-cubic duality

## Verdict

`PASS AS AN EXACT ROUTE IDENTITY`.

## Checks

1. The derivative degree `j` is paired with apolar degree `n-j`; the complex
   therefore occupies apolar degrees `n-3,n-2,n-1`.
2. In total internal degree `n+r-3`, Koszul homological degrees
   `r,r-1,r-2` contain exactly those three apolar degrees.
3. Exterior duality changes only a determinant line and converts the high
   Koszul chain segment to the displayed derivative complex.
4. The Artinian-Gorenstein last shift is `n+r`, so
   `(r-1,n+r-3)` is dual to `(1,3)`.
5. `Tor_1` in degree three is the quotient of cubic apolar equations by
   linear multiples of quadratic equations, hence the minimal cubic generator
   space.
6. Tensoring a circuit factor with independent squarefree factors adds only
   quadratic generators; the one-relation cubic count is unchanged.

## Claim firewall

The identity concerns the full actual factor quotient. It does not imply that
partial-quotient homology is determined by a scalar Betti number, nor does it
supply a subadditive invariant of sums. It proves that the uncorrected full
quotient is redundant and identifies the exact relation module that a partial
quotient must remove.

## Research consequence

A scalar subtraction of `beta_(1,3)` is not a new invariant: at full quotient
it annihilates the entire group tautologically. The only viable continuation
is a functorial quotient-visible generator map followed by a cap on its
cokernel.
