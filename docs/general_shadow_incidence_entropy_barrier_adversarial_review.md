# Adversarial review: incidence and entropy-scale barrier

## Verdict

The incidence sandwich is a valid exact general-`n` theorem. The conclusion

```text
log Theta_n / n -> log 2
```

is also valid, but it is a route-classification statement rather than a new
rank bound.

## 1. Coordinate/subspace boundary

The double-counting proof is stated for coordinate product families. Transfer
to arbitrary subspaces uses the existing exact theorem equating the subspace
minimum with the coordinate Ferrers minimum.

Without that dependency, only the coordinate version is proved.

## 2. Incidence degrees

Each degree-`d` product cell has exactly `d^2` lower neighbors. Each
degree-`d-1` cell has exactly `(n-d+1)^2` upper containers.

Using `n-d` instead of `n-d+1`, or forgetting that both row and column
coordinates contribute, invalidates the bound.

## 3. The upper bound is not an extremal classification

The estimate

```text
F(b)<=d^2*b
```

is the union bound for lower neighbors. It need not be sharp. The theorem
controls exponential rate, not exact minimizers or polynomial prefactors.

## 4. Inverse rounding

The lower inverse bound uses `floor(C/d^2)`. The upper inverse bound uses the
bounded-codegree inequality and must be truncated by the upper ambient
dimension. Neither inequality is an equality claim.

## 5. Linear degree is required for the rate statement

The conclusion that multiplicative factors are subexponential assumes
`d=alpha*n+O(1)` with `0<alpha<1`. Fixed degree and fixed codimension require
separate bookkeeping, though their polynomial factors also do not alter a
positive exponential rate.

## 6. Tower-rate conclusion

The lower bound

```text
Theta_n>=binom(n,floor(n/2))
```

comes from the literal cap in the central derivative row. The upper bound
`Theta_n<=2^(n-1)` uses the existence of Glynn's actual decomposition.

This proves only the first-order exponential rate. It does not prove

```text
Theta_n=Theta(binom(n,floor(n/2)))
```

or any bounded ratio to the central binomial coefficient.

## 7. Strongest objection

The result may appear tautological because both the central binomial
coefficient and Glynn's bound have base two. That objection is correct at the
level of the numerical limit.

The nontrivial research consequence is negative: an entropy-only transform of
the exact shadow recurrence cannot resolve the problem. Any future scalar
asymptotic claim must retain at least logarithmic and polynomial terms.

## 8. Final classification

```text
incidence sandwich=PASS
inverse sandwich=PASS
linear-degree rate preservation=PASS
scalar tower exponential rate log 2=PASS
new numerical lower bound=NO
polynomial normalization=OPEN
central-binomial ceiling=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
