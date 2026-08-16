# Adversarial review: full-degree tower envelopes and saturation

## Verdict

The prefix-envelope identity and the full-degree saturation lower bound are
valid consequences of the derivative-tower theorem on the parent stack.
Subject to that dependency, the exact finite replay supports

```text
ChowRank(perm_7)  >= 49
ChowRank(perm_8)  >= 90
ChowRank(perm_9)  >= 164
ChowRank(perm_10) >= 307.
```

No exact-rank, border-rank, or asymptotic claim is accepted.

## 1. Dependency boundary

This result does not re-prove the geometric exact product-shadow theorem or the
section/projection lemma. It uses the parent theorem

```text
dim(D_d(perm_n) intersect sum_i D_d(T_i)) <= B_(n,d)(q)
```

for arbitrary Chow terms. If that theorem is withdrawn, every numerical lower
bound in this PR must be withdrawn as well; the finite dynamic program alone
would then be only a coordinate diagnostic.

## 2. Prefix-envelope proof

The block recurrence is

```text
B(q)=min(C(q), min_(1<=s<q)((q-s)M+B(s))).
```

The claimed formula

```text
B(q)=qM+min_(0<=t<=q)(C(t)-tM)
```

includes `t=0` with `C(0)=0`, so the literal line `qM` is not lost. The proof
is an induction and does not assume convexity, monotonic increments, or a
unique minimizing subblock.

Regression tests must compare the closed envelope with the historical
quadratic block scan for all existing `n=7,8` rows. Agreement at only the final
threshold is insufficient.

## 3. Saturation tail

For

```text
R=max(binom(n,d),Q_(n,d-1)),
```

one has `C(q)=binom(n,d)^2` for every `q>=R`: the literal capacity has reached
ambient and the lower derivative row has saturated. The affine-tail formula
therefore uses the prefix strictly before `R`.

An off-by-one error replacing `t<R` by `t<=R` changes the stored prefix but not
always the final threshold, so the proof and test must retain the stated
strict range.

## 4. Full coverage versus coupled/literal equality

For an actual decomposition

```text
perm_n=sum_i T_i,
```

linearity gives only

```text
D_d(perm_n) subset sum_i D_d(T_i).
```

This is enough: intersecting the literal sum with `D_d(perm_n)` returns the
whole permanent space. The proof never states

```text
D_d(sum_i T_i)=sum_i D_d(T_i).
```

Any such replacement would be a regression against the repaired small-`n`
coupled-catalectic firewall.

## 5. Degree range

The parent tower was initially evaluated only through `n-2` because the
first-Koszul residual uses complementary degrees in that range. The tower
itself remains valid at degree `n-1`, and this extra row is decisive:

```text
n=7: Q_(7,6)=49
n=8: Q_(8,7)=90
n=9: Q_(9,8)=164.
```

Degree `n` is not silently omitted. Its only nonzero permanent subspace is
`span(perm_n)`, whose first shadow is the entire degree-`n-1` space; hence it
has the same saturation threshold as degree `n-1`.

## 6. Dual Ferrers dynamic program

The exact Ferrers theorem reduces the inverse shadow to

```text
maximize sum_i lambda_i
subject to lambda_0>=...>=lambda_(M-1)>=0
and sum_i w_i*k(lambda_i)<=C.
```

The C++ state uses exact cost, previous part, and maximum total size. The
transition

```text
new[x,c+w_i*k(x)] = x + max_(u>=x) old[u,c]
```

is exhaustive. Suffix maxima change the running time, not the state space.

When `w_i=0`, choosing `x=u` dominates `x<u`: it increases the objective being
maximized and leaves a weakly larger upper bound for every later part. This
optimization is valid only for the inverse maximization problem. Reusing it in
a fixed-size primal minimization without proof would be invalid.

## 7. Arithmetic and implementation limits

The certified table is restricted to `3<=n<=10`. The implementation uses
bit masks only in that finite range and all dimensions fit signed 32-bit
storage; binomial construction and intermediate arithmetic use signed 64-bit
integers.

The Python driver fails closed when no C++17 compiler is available. A missing
compiler is not converted into a skipped or passing replay.

The pure-Python implementation independently reconstructs `n<=8`. The `n=9`
and `n=10` results currently have one exact implementation plus the generic
mathematical proof and regression against all smaller rows. They are not
mislabelled as two-implementation certificates.

## 8. Small-n regressions

The scalar tower returns

```text
n=3: 4
n=4: 8
n=5: 15
n=6: 27.
```

The exact small-`n` results are `4,8,16`, and the specialized accessible
`n=6` lower bound is 28. These mismatches are expected and important: the new
scalar theorem does not absorb the coupled finite geometry used at `n=5` or
the relation geometry used at `n=6`.

## 9. Strongest objection

The table

```text
Theta_3,...,Theta_10 = 4,8,15,27,49,90,164,307
```

is compatible with a central-binomial-scale method. Finite ratios do not
establish an exponential rate, a limiting constant, or eventual proximity to
Glynn's `2^(n-1)` upper bound.

This objection is decisive. The next result must prove a uniform asymptotic
estimate for `Theta_n` or add a non-scalar invariant. Extending the exact table
one value at a time is not, by itself, an authorized route to general Glynn
optimality.

## 10. Claim matrix

```text
prefix min-plus envelope                         PROVED
non-circular saturation formula                  PROVED
full-degree range through n-1                    PROVED
ordinary lower bounds 49,90,164,307              EXACT FINITE REPLAY
exact rank for n>=6                              NOT PROVED
border-rank improvement                          NOT PROVED
asymptotic formula for Theta_n                   OPEN
general ChowRank(perm_n)=2^(n-1)                OPEN
literature novelty                               NOT ESTABLISHED
```
