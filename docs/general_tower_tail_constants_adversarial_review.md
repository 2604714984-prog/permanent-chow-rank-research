# Adversarial review: fixed-codimension tower tails

## Verdict

The threshold-monotonicity theorem, one-term Lipschitz bound,
fixed-codimension constants, top-row gap and `C4` interpretation are valid
general-`n` consequences of the exact scalar derivative tower.

They do not improve the numerical Chow-rank bounds of PR #51. The main
research value is a route localization:

```text
fixed-codimension top tail = bounded additive correction
linear-codimension regime = still open
```

## 1. Dependency boundary

The argument depends on the following previously proved statements.

1. `B_(n,d)(q)` is a valid upper bound for the permanent-relative
   intersection with a literal sum of `q` Chow derivative spaces.
2. Exact product shadows for arbitrary subspaces equal the coordinate
   Ferrers minima.
3. The block-projection recurrence has the prefix-envelope form.
4. The shadow-complement deficit recurrence is valid.

If any of these inputs is withdrawn, the present result must be downgraded
rather than reinterpreted from the finite tables.

## 2. Coupled versus literal spaces

For an actual decomposition, only

```text
D_d(sum_i T_i) subset sum_i D_d(T_i)
```

is used. The argument never replaces the coupled catalectic image by the
literal sum.

The thresholds `Q_(n,d)` are saturation thresholds of a certified **upper
capacity**, not dimensions asserted to be attained by arbitrary Chow blocks.

## 3. Threshold monotonicity

The key strict implication is

```text
B_(n,d-1)(q)<A_(n,d-1)
=> Gamma_(n,d)(B_(n,d-1)(q))<A_(n,d).
```

It uses the fact that the full degree-`d` permanent space has complete shadow
`A_(n,d-1)`. A weak inequality here would not exclude premature saturation.

The conclusion is only

```text
Q_(n,d)>=Q_(n,d-1).
```

It does not say that the capacities themselves are ordered across degrees.

## 4. Lipschitz direction

The capacity increment satisfies

```text
0<=B(q+1)-B(q)<=M.
```

The upper bound follows by retaining the first `q` terms and adding one
literal one-term space. The lower bound uses the nondecreasing direct cap and
the prefix envelope.

Reversing to deficits gives

```text
D(t)<= (Q-t)M.
```

It would be invalid to replace this upper bound by equality or to infer
concavity of the capacity row.

## 5. The condition `n>=2k` is essential to the proof

The transition theorem compares

```text
M_0=binom(n,k)
M_1=binom(n,k-1).
```

The proof requires `M_0>=M_1`, hence `n>=2k`. Without this condition,
`Q>=M_0` does not guarantee `Q>=M_1`, and the literal deficit estimate used in
the tail transport can fail.

No statement is made for the lower half of the derivative tower by symmetry.
The tower recurrence itself is directional.

## 6. Large distance from the previous threshold

For `r=Q-t`, a minimal `a` with `binom(a,k)>=r` need not exist when
`r>binom(n,k)`. The proof explicitly separates the range

```text
r>=M_1,
```

where the ambient bound `F<=M_1^2<=rM_1` is enough. The rectangle argument is
used only when `r<M_1<=M_0`, where an `a<=n` is guaranteed.

Omitting this split is a real quantifier error.

## 7. Rectangle construction is an upper bound only

The family

```text
C([a],k) x C([n],k)
```

provides

```text
F_(n,k)(z)<=binom(a,k-1)binom(n,k-1).
```

It does not classify exact-shadow minimizers and need not be optimal. The
constants `c_k` are universal safe increments, not claimed exact for each
transition.

## 8. Finiteness and asymptotics of `c_k`

For `a>=3k`,

```text
binom(a-1,k)>=binom(a,k-1),
```

so the positive part in `c_k` vanishes. The exact maximum is finite.

The asymptotic proof uses a candidate
`a=(phi^2-k^(-1/2))k+O(1)`. The difference factor is only polynomially small,
so it does not change the binomial exponential rate. This establishes the
rate of the **universal constants**, not the actual tower increments.

In particular,

```text
c_k^(1/k) -> 5.703275...
```

does not imply that the scalar tower has that exponential base.

## 9. Top-row `C4` interpretation

An element of the degree-two product layer is one bipartite `K_(2,2)`, and its
shadow is its four-edge set. This proves exact equality between `F_(n,2)(z)`
and the minimum number of edges supporting at least `z` distinct `C4`s.

The criterion concerns only the final transition. It is not a reduction of
the complete Chow-rank problem to graph supersaturation.

## 10. No new numerical rank claim

The finite replay reproduces the PR #51 thresholds:

```text
perm_7  scalar tower = 49
perm_8  scalar tower = 90
perm_9  scalar tower = 164
perm_10 scalar tower = 307.
```

No number in this PR exceeds those values. Any statement that the tail theorem
itself improves an unrestricted Chow-rank lower bound is rejected.

## 11. Strongest objection

The theorem may be evidence that the scalar route is structurally limited:
the top `o(n)` codimension tail contributes only `exp(o(n))` additively, while
all difficult exponential behavior is pushed into the linear-codimension
shadow transform.

This objection is correct and useful. The next step must analyze that transform
or add non-scalar information. Extending the finite threshold table is not a
substitute.

## 12. Independent replay boundary

The primary implementation maximizes Ferrers size under each shadow budget.
The independent implementation minimizes shadow at each exact family size.
The independent file imports none of the primary or historical tower modules.

Required outputs include:

```text
tail constants=1,5,20,83,362,1572,7513
capacity Lipschitz checks=1,151
threshold monotonicity checks=21
tail threshold checks=9
bipartite graphs enumerated=66,048
top thresholds through n=8=4,8,15,27,49,90
```

## 13. Final classification

```text
general threshold monotonicity=PASS
fixed-codimension tail theorem=PASS
top-row gap at most one=PASS
C4 top-row interpretation=PASS
new numerical Chow-rank bound=NO
linear-codimension scalar asymptotic=OPEN
Chow-realizability correction=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
merge readiness=PENDING EXACT-HEAD HOSTED CI
```
