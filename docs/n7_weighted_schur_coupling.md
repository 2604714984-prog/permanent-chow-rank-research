# Arbitrary nonzero weighted coupling by Schur products

## Status

`W-01-COMPLETE; W-02-COMPLETE; W-03-COMPLETE; W-04 FIXED-CODE OPERATOR COMPLETE.`

The W-04 structural classification of special point subsets remains open.
The W-05 stabilizer operator is complete for a fixed code; a
characteristic-zero Kneser proof and equality-case classification remain
open.

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

## Puncturing, shortening, and separators

Let `L=R3 star R4`, and let `pi_i` delete coordinate `i`. Then

\[
e_i\in L\quad\Longleftrightarrow\quad
\dim L-\dim\pi_i(L)=1.
\]

This is the W-04 puncture test. The shortening of `R_d` at coordinate `i`
has dimension `q_d-1` when the coordinate functional is nonzero, and `q_d`
when it vanishes identically. In the common-graph affine normalization (or
after trivializing by a nowhere-zero linear form), `C3 subset C4`, hence
`R4 subset R3`.
If coordinate `i` vanishes on `R4`, then it vanishes on every Schur product,
so `e_i` cannot belong to `L`. Equivalently, `e_i in C4`: the point has a
degree-four separator. The evaluator freezes these separator coordinates at
each stated control prime and
checks that they never appear among the puncture rank drops.

## Coordinate stabilizer operator

For a column basis `B=[b_1,...,b_l]` of `L` and a row basis `A` of
`L^perp`, the coordinate stabilizer is the kernel of

\[
K=\begin{bmatrix}
A\operatorname{diag}(b_1)\\
\vdots\\
A\operatorname{diag}(b_l)
\end{bmatrix}.
\]

Indeed, `Kx=0` says exactly that `x star b_j` lies in `L` for every basis
vector. This gives the W-05 fixed-code operator with only 42 unknowns and at
most 341 rows on the active controls.

Over the two control primes, the three curve-union Schur spans have ambient
stabilizer dimensions 15, 22, and 29. These equal the number of zero
coordinates plus one. After puncturing the zero coordinates, every control
has stabilizer dimension one and attains the modular Kneser value 11. Thus
they are effective-support equality controls, not 42-coordinate equality
models and not permanent-target controls. The general characteristic-zero
bound and its equality cases are not promoted here.

## Controls and boundary

The deterministic replay evaluates the three existing curve-union profile
controls over the two standard primes.  Those rows test matrix orientation and
the membership/puncture criteria only.  They do not satisfy the permanent target in
general and cannot close any F frontier from weighted coupling alone.

The theorem is used over characteristic zero (or any infinite field).  A
finite-field control is not itself a characteristic-zero nonexistence or
existence certificate for an arbitrary point component.
