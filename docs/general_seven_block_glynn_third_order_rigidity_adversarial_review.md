# Adversarial review: third-order local rigidity of the compressed Glynn witness

## Scope reviewed

This review challenges the packet
`general_seven_block_glynn_third_order_rigidity` at the standard compressed
Glynn seven-block point. The claimed result is local, regular, and
order-bounded: after deleting one standard summand, the other six standard
blocks cannot first recover the missing direction at order three.

The review does not treat the packet as a global six-block zero theorem.

## 1. Main proof dependency

The proof uses three inherited facts for every deletion:

1. the full tangent map has rank `574` on `666` parameters, so its exact kernel
   has dimension `92`;
2. the projected tangent image has rank `108`, while adjoining the missing
   summand raises the rank to `109`; and
3. the projected second fundamental form on the full tangent kernel lies in the
   projected tangent image.

The new calculation then splits every full second derivative as

```text
B(e_i,e_j) + L H_ij = Q_ij
```

and reduces the corrected polarized cubic tensor modulo the projected tangent
space.

If any of these inherited ranks or the exact kernel lift were wrong, the
third-order conclusion would fail. The packet therefore reuses their frozen
cores explicitly and independently rebuilds the relevant finite interfaces.

## 2. Full second-order compatibility is not skipped

A tempting but invalid shortcut would be to use only the fact that projected
quadratic curvature lies in the projected tangent image. That would ignore the
full `3,876`-coordinate second-order equation and could include first-order
kernel directions that do not lift to order two.

The packet does not make that shortcut. Its exact full second cokernel ranks are

```text
missing-sign weight 1: 66
missing-sign weight 2: 66
missing-sign weight 3: 70
```

with `104,116,104` nonzero pair representatives. Hence the full second-order
obstruction is visibly nonzero. Only directions satisfying `Q(y,y)=0` enter
the order-three argument.

## 3. Dependence on the chosen tangent splitting

The corrections `H_ij` are not canonical as parameter vectors. Replacing one
splitting by another changes `H_ij` by an element of the tangent kernel.
The corrected cubic tensor changes by a term in `pi B(K,K)`, which the inherited
second-order theorem places inside the projected tangent image. Therefore the
class of the corrected cubic tensor modulo the projected tangent space is
independent of the splitting.

The theorem concerns this quotient class, not the raw `H_ij` coefficients.

## 4. Symmetry coverage

Only three deletion indices are computed exactly. This is sufficient because
permuting the three free sign coordinates preserves the standard witness and
partitions the seven retained signs into Hamming-weight orbits of sizes
`3,3,1`. The representatives have weights `1,2,3`, so all seven deletions are
covered.

A deformation outside the standard chart is not related by this symmetry and
is not addressed.

## 5. Characteristic-zero status

The primary calculation lifts the complete modular tangent kernel to exact
rational coefficients and verifies every relation against the full tangent
map. The independent implementation uses a different prime only as an
independent finite replay. The characteristic-zero theorem rests on the exact
rational verification, not on a finite-field heuristic.

## 6. What the theorem does not prove

The packet does not exclude:

- a remote six-block representation;
- a singular or Puiseux degeneration;
- a six-block path with a different limiting frame;
- first appearance at order four or higher;
- a global six-block zero theorem; or
- any improvement to ordinary or border Chow rank.

In particular, it does not prove `mu(6,4)=7`.

## 7. Route decision

The third-order quotient calculation is exact and nonvacuous, but continuing
mechanically to fourth and higher order would remain local to one known
seven-block point. Two successive corrected fundamental forms have already
returned to the same projected tangent image. The packet's stopping rule is
therefore appropriate: move to genuinely mixed or remote six-block equations
rather than building an unbounded higher-jet framework.

## Verdict

```text
local third-order algebra                     ACCEPT
full second-order integrability               ACCEPT
splitting independence modulo tangent         ACCEPT
seven-deletion symmetry coverage              ACCEPT
characteristic-zero lift                      ACCEPT
global six-block conclusion                   NOT CLAIMED
mu(6,4)=7                                     NOT ESTABLISHED
literature novelty                            NOT ESTABLISHED
```

Frozen theorem core under review:

```text
a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62
```
