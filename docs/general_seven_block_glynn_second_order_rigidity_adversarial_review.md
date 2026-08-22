# Adversarial review: second-order rigidity of the compressed Glynn witness

## Verdict

```text
full first-order kernel = EXACT
quotient second fundamental form on that kernel = ZERO
missing-summand second-order absorption = IMPOSSIBLE
remote/singular/higher-order six-block witness = NOT EXCLUDED
mu(6,4) = OPEN IN [6,7]
```

## 1. The full first-order equations are imposed

The 92-dimensional kernel is computed for the complete degree-four tangent map
in all 3876 monomial coordinates. It is not the kernel of the 256-dimensional
column-multilinear projection. Therefore repeated-column first-order defects
cannot be silently ignored.

## 2. Exact rational kernel, not finite-field promotion

Finite-field elimination is used only to select a sparse basis. Its
coefficients lift to `{-2,-1,-1/2,1/2,1,2}` and every lifted relation is
verified directly over the rationals against the full tangent map. Modular
independence plus 92 exact relations proves completeness in characteristic
zero.

## 3. Exact curvature reduction

All 4278 polarized pairs of the exact rational kernel basis are evaluated.
Their projected vectors are reduced against an exact rational basis of the
projected tangent image. The quotient remainders are identically zero. The
independent modular implementation is a cross-check, not the sole
characteristic-zero argument.

## 4. Parameter accelerations are included

Second-order source and factor accelerations contribute through the linear
first-order map and therefore lie in `T_kappa`. The proof quotients by that
entire tangent image. Only the polar quadratic term needs the kernel
calculation; it is not assumed to vanish termwise.

## 5. Projection firewall

A full second-order identity would remain valid after projection to column
multidegree `(1,1,1,1)`. The missing standard summand lives entirely in that
summand. Its nonmembership in the projected tangent space therefore gives a
valid obstruction in the full polynomial space.

## 6. Local and order-bounded conclusion

The theorem concerns the six standard blocks obtained by deleting one term
from the known seven-block formula. It does not classify other six-tuples. It
also stops at order two. A third-order path, a Puiseux path, or a remote exact
six-block representation is not excluded.

## 7. No rank promotion

The result changes neither ordinary Chow rank nor border Chow rank. It is a
local route barrier for the derivative-block threshold `mu(6,4)`.
