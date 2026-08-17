# Adversarial review: two-direction maximal-ideal ceiling

## Verdict

The split-Boolean denominator, finite route ceilings and asymptotic
central-binomial ceiling are valid for the profile

```text
M -> dim((s,t)M_(d-1)).
```

They do not close arbitrary two-generator homogeneous ideals.

## 1. The denominator direction is correct

The one-term envelope is a maximum over all Boolean images of the selected
differential two-plane. The proof constructs one explicit split two-plane and
therefore obtains a lower bound on that maximum.

A lower bound on the denominator gives an upper bound on the rank lower bound,
which is the correct direction for a route ceiling. The argument does not claim
that the split plane is globally maximizing.

## 2. Tensor quotient

The equality

```text
B_n/(s,t)B_n
 = (B_a/sB_a) tensor (B_b/tB_b)
```

uses a disjoint partition of the variables. It would be false for two
arbitrary overlapping linear forms without an additional coordinate change.
Only the explicit witness is needed.

## 3. Primitive Hilbert coefficients

For a Boolean factor, strong Lefschetz gives

```text
dim(B_m/LB_m)_j
 = [binom(m,j)-binom(m,j-1)]_+.
```

The positive part is essential on the decreasing side. Continuing the raw
first difference past the center would introduce negative quotient dimensions
and invalidate the convolution.

## 4. Permanent numerator is deliberately coarse

The numerator is bounded by

```text
min(target dimension, two times source dimension).
```

No commutativity syzygy or permanent-specific relation is subtracted. The
finite numbers are therefore safe upper ceilings and need not be attainable.
A sharper numerator can only reduce the route ceiling.

## 5. The one-dimensional witness remains part of the envelope

The denominator takes the maximum over subspaces of dimension at most two. It
therefore includes the principal strong-Lefschetz image

```text
min(binom(n,d-1),binom(n,d)).
```

This term is necessary on the decreasing side and away from the center.
Discarding it would manufacture false large ceilings.

## 6. Central asymptotic split

When `binom(n,d-1)<=M_n/2`, the source cap alone gives a ceiling at most `M_n`.
When the target side is nonincreasing, the principal denominator equals the
target dimension and again gives at most `M_n`.

Only the increasing near-central range uses the split quotient. In that range
the target binomial coefficient is at least `M_n/2`, while the total split
quotient dimension is `O(2^n/n)`. The relative deficit is therefore
`O(n^(-1/2))`.

The argument does not assert this estimate uniformly for every tail degree.

## 7. Ceilings are not lower bounds

The displayed values

```text
3,7,10,20,35,75,126,252
```

are upper bounds on what the profile could prove for `n=3,...,10`. They are
not certified Chow-rank lower bounds and must not replace the numerical ledger
boundaries.

## 8. Dependent-factor safety

The Boolean module is an envelope for every Chow term through a subquotient,
including dependent-factor terms. The split witness is used to lower-bound the
maximum possible Boolean image; no assertion is made that every term realizes
that witness.

## 9. Strongest objection

An ideal such as `(s^a,t^b)` with unequal degrees combines images from
different source degrees. Its denominator and relative intersection can behave
differently from `(s,t)`. The present theorem gives no ceiling for that
interface.

This objection is correct. Unequal-degree complete intersections and
asymmetric staircase ideals remain open.

## 10. Final classification

```text
split Boolean quotient formula=PASS
finite route ceiling arithmetic=PASS
asymptotic (1+O(n^-1/2))*central ceiling=PASS
new numerical Chow-rank lower bound=NO
arbitrary two-generator ideals=OPEN
relation-sensitive monotone invariants=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
