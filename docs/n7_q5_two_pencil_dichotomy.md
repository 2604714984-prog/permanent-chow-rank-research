# The gauge-free `q5=2` pencil dichotomy

## Status

`TI-01..TI-03-CORRECTED; TI-08A-COMPLETE.`

This theorem applies to the `F3` subcase with `H6=42`, hence `q5=2` and
`q6=0`.  It reduces the relation tensor to three exhaustive structural
branches.  It does not yet close `F3` or the complete `q5=2` class.

## Correct coefficient torsor

Let `A` be the `42 x 7` point matrix, let `E_d` be the homogeneous evaluation
matrix, and suppose that a `7 x 42` matrix `C` satisfies

`C E6=S6`,

where `S6` is the gradient of the squarefree septic.  The solution set, when
nonempty, is a torsor under `R6 tensor k^7`, with `R6=ker(E6^T)`.  For
`j<k`, put

`Psi_(jk)=c_j star a_k-c_k star a_j`.

Differentiating the target identity and subtracting the two mixed partials
gives `Psi_(jk) in R5`.  Thus the earlier map to the quotient by `R5` is zero
on every solution.  If `C` is changed by `U in R6 tensor k^7`, then `Psi`
changes by

`d_A(U)_(jk)=u_j star a_k-u_k star a_j`.

The canonical datum is `[Psi] in coker(d_A)`.  In the present `q6=0` subcase
there is no gauge, so `Psi` itself is canonical.

## Pencil theorem

Choose a basis `rho1,rho2` of `R5` and write, at each point index `i`,

`c_i wedge a_i = rho1_i beta1 + rho2_i beta2`.

Changing the relation basis acts contragrediently on `(beta1,beta2)`, so the
projective line `P(span(beta1,beta2))` is intrinsic in the gauge-free case.
Every nonzero left side is a decomposable bivector.  Therefore every nonzero
relation ratio

`u_i=[rho1_i:rho2_i]`

lies in the intersection of that projective line with `Gr(2,7)`.

Exactly one of the following occurs:

1. `dim span(beta1,beta2)<=1`;
2. the span has dimension two, its projective line is not contained in the
   Grassmannian, and there are at most two distinct nonzero relation ratios;
3. the whole projective line lies in `Gr(2,7)`.

Indeed, the 35 Plucker quadrics restrict to binary quadratics on the line. If
the line is not contained in the Grassmannian, one nonzero restriction has at
most two projective zeros.  Three distinct ratios force every restriction to
vanish identically.  A line contained in `Gr(2,7)` has flag form

`{ U : L subset U subset H }`, with `dim L=1` and `dim H=3`;

equivalently, after a basis choice, `beta1=p wedge q` and
`beta2=p wedge r`.

Zero relation columns `rho1_i=rho2_i=0` remain a separate support stratum.

## Deterministic replay

`scripts/n7_q5_two_pencil_dichotomy.py` constructs all 35 restricted Plucker
quadratics.  It freezes a flag-line positive control and a transverse line
whose intersection consists exactly of its two coordinate endpoints.

## Claim boundary

The theorem is characteristic independent away from the usual exterior-sign
conventions and is used here in characteristic zero.  It is a complete pencil
dichotomy, not a proof that any branch satisfies point reducedness, permanent
target containment, weighted coupling, or the lower-50 endpoint.
