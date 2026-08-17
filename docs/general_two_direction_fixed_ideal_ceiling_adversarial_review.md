# Adversarial review: fixed binary ideal profiles

## Verdict

The asymptotic ceiling is valid for every fixed homogeneous `m`-primary ideal
in `k[s,t]`, conditional on the parent apolar-subquotient and Boolean-envelope
theorems.

It does not apply uniformly to an ideal family whose complexity grows with
`n`.

## 1. Fixed ideal is a real hypothesis

The number of generators `r`, all generator degrees `p_i`, and an integer `N`
with

```text
(s,t)^N subset I
```

must be independent of `n`. The constants hidden in `O_I` depend on these
data.

Allowing `N`, `r` or the degrees to grow can destroy the `O_I(2^n/n)` split
quotient estimate relative to central-binomial scale.

## 2. m-primary is essential for the split quotient

The proof uses `s^N,t^N in I`. A height-one ideal with a nontrivial common
factor need not contain either pure power. Such ideals are not covered by the
split-quotient argument, although principal height-one ideals are already
closed by the separate principal theorem.

## 3. Generator presentation gives only an upper cap

The permanent numerator satisfies

```text
dim((I A_perm)_d)
 <= min(target dimension,sum of generator-source dimensions).
```

Relations among the generators, annihilators and additional apolar syzygies
are ignored. This makes the route ceiling weaker but safe. No exact permanent
image rank is claimed.

## 4. Degenerate one-dimensional Boolean witnesses

For each generator `g_i`, the denominator maximum may use a different point
`[alpha:beta]` where `g_i(alpha,beta)!=0` and map both binary variables to
multiples of one strong-Lefschetz element.

This is legal because the Boolean envelope is a maximum over all images of
dimension at most two. It is not a claim that one Boolean plane simultaneously
maximizes all generators.

## 5. Direction of the split comparison

Since `(s^N,t^N) subset I`, one has a surjection

```text
B_n/(s^N,t^N)B_n -> B_n/I B_n.
```

Thus the `I`-quotient is no larger and the `I`-image is no smaller. Reversing
this quotient direction would invalidate the denominator lower bound.

## 6. Strong-Lefschetz quotient formula

The exact formula is

```text
dim(B_m/L^N B_m)_j
 = [C(m,j)-C(m,j-N)]_+.
```

The positive part is required because multiplication by `L^N` is maximal rank:
it is injective on the increasing side and surjective on the decreasing side.
Raw differences become negative past the crossover and are not quotient
dimensions.

## 7. Total-dimension telescoping

The sum of the positive `N`-step differences is bounded by `N` central layers,
not by `(m+1)N` central layers. This telescoping is what yields

```text
O_I(2^n/n)
```

for the split tensor quotient.

## 8. Near-central case split

If some principal generator is surjective, the denominator equals the target
Boolean dimension. If all sources are small, the sum-of-source numerator gives
the central ceiling. The split quotient is used only when a source exceeds
`M_n/r`, which forces the target itself to have central-binomial scale.

The `O_I(n^-1/2)` relative loss is not asserted in arbitrary tail degrees.

## 9. Fixed complete intersections are included

Every fixed `(s^a,t^b)` is `m`-primary and is covered, including unequal
`a,b`. This does not mean a family `(s^(a_n),t^(b_n))` with growing exponents is
covered uniformly.

## 10. Strongest objection

An `n`-dependent staircase could trade a growing Boolean quotient complexity
against a larger permanent source sum. The theorem does not rule out such a
construction.

This objection is correct. Any continuation along ideal images must now expose
an explicit growing-complexity mechanism and prove its termwise Boolean
envelope. Otherwise the default research direction should move to
subquotient-monotone relation or representation data.

## 11. Final classification

```text
fixed m-primary ideal ceiling=PASS
fixed complete intersections=PASS
fixed staircase ideals=PASS
new numerical Chow-rank lower bound=NO
n-dependent ideal families=OPEN
height-one nonprincipal ideals=OPEN OUTSIDE THIS THEOREM
relation-sensitive monotone invariants=OPEN
border-rank claim=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
