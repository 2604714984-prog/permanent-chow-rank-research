# Adversarial review: local rigidity of the compressed Glynn witness

## Verdict

```text
direct pair merge obstruction = PROVED
missing-summand tangent obstruction = PROVED
remote six-block representation = NOT EXCLUDED
singular or higher-order coalescence = NOT EXCLUDED
mu(6,4) = OPEN IN [6,7]
```

## 1. The theorem is local

The tangent computation is performed at the six standard block points left
after deleting one summand from the explicit seven-block formula. It does not
classify every six-tuple of degree-six Chow derivative blocks. A disconnected
or remote six-block witness is untouched.

## 2. No inference from optimization failure

No numerical residual or nonlinear optimizer is used in the proof. The claims
come from rational flattening ranks, analytic dimension bounds, and exact
modular nonzero-minor certificates.

## 3. Characteristic-zero transfer

For each deleted summand, the six tangent spaces have analytic dimension at
most `6*18=108`. Rank 108 modulo a prime gives a nonzero 108-minor over the
integers, so the characteristic-zero rank is exactly 108. Augmented rank 109
modulo a prime proves that the missing summand is not in that rational tangent
sum. Two primes are retained as an implementation cross-check; one valid
minor would suffice mathematically.

## 4. Projection is legitimate

The obstruction is taken in the direct column multidegree `(1,1,1,1)`. A full
polynomial identity would remain valid after this projection. Cross-column
factor motions project to zero because they create one missing and one repeated
column. Therefore failure in the projected space excludes absorption in the
full space.

## 5. Direct pair merge boundary

The essential-dimension argument applies to the exact signed standard
summands. It excludes replacing any two of those seven summands by one block.
It does not say that every sum of two arbitrary derivative-block elements has
essential dimension ten.

## 6. Tangent versus higher order

The nonmembership

```text
G_kappa not in sum_(v != kappa) T_v
```

excludes first-order absorption only. A second-order path can have zero first
derivative and nonzero curvature. The next valid interface is therefore the
second fundamental form modulo the tangent sum, not a declaration that the
seven-block witness is globally minimal.

## 7. Claim firewall

This packet does not improve ordinary Chow rank, prove a border-rank bound, or
establish literature novelty. It only removes the nearest local routes from
the known seven-block witness to a six-block witness.
