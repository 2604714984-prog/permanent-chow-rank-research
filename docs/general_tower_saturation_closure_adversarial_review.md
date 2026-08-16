# Adversarial review: direct derivative-tower saturation

## Verdict

The full-coverage implication is valid and strictly stronger than the
Koszul-only bootstrap at `n=7`:

```text
B_(7,5)(47)=426 < dim D_5(perm_7)=441
B_(7,5)(48)=441
```

Hence a 47-term decomposition is impossible and the stacked ordinary lower
bound is 48.

The resulting fixed point is a boundary only for the named scalar derivative
tower plus first-Koszul inference system. It is not an exact-rank statement.

## 1. Full coverage versus selectable subblocks

The central logical distinction is:

- a partial-term residual proof may select `q` terms only after a prior lower
  bound guarantees `q` available nonzero terms;
- a saturation proof assumes a decomposition with exactly `q` terms and uses
  all of them.

For the second argument no independent selectable-term budget is required.
If

```text
perm_n=sum_(i=1)^q T_i,
```

then linearity gives

```text
D_d(perm_n) subset sum_i D_d(T_i)
```

for every degree. Thus the permanent-relative intersection is the full
permanent derivative space.

Any implementation that imposes the parent bootstrap chronology on this
all-term argument is unnecessarily weak.

## 2. Coupled/literal firewall

The theorem does not assert

```text
D_d(sum_i T_i)=sum_i D_d(T_i).
```

It uses only containment. Full coverage follows because the left side is
`D_d(perm_n)` under the hypothetical equality of polynomials. The literal sum
may be strictly larger.

## 3. Capacity direction

The derivative-tower theorem gives an upper bound on

```text
dim(D_d(perm_n) intersect sum_i D_d(T_i)).
```

Under a decomposition this dimension is exactly `binom(n,d)^2`. Therefore an
upper capacity strictly below ambient is a contradiction. Reversing this
inequality would invalidate the result.

## 4. Exact `n=7` boundary

The independent reconstruction must verify:

```text
B_(7,5)(46)=405
B_(7,5)(47)=426
B_(7,5)(48)=441
ambient degree-five dimension=441
```

It must also compute every derivative-degree saturation threshold and verify
that none exceeds 48.

The conclusion is

```text
Theta_7=max_d Q_(7,d)=48.
```

Merely checking the degree-five row without checking the other rows would
still prove lower 48, but it would not justify the claimed exact scalar-route
closure at 48.

## 5. Relation to the parent fixed point

The parent operator `Phi_7` legitimately stabilizes at 47 because it contains
only partial-term first-Koszul residual promotions. That finite statement is
not retracted.

The phrase "scalar tower closure" must, however, include the tower's direct
full-coverage consequence. The enhanced operator is

```text
max(L,Theta_7,Phi_7(L)),
```

and its exact sequence is

```text
36 -> 48 -> 48.
```

Thus PR #49's `Phi_7` fixed point is retained as a narrower operator result and
superseded as the stopping point of the complete scalar tower inference.

## 6. Assume every hidden assumption is false

If the tower capacity theorem is invalid, if the actual polynomial equality
does not imply derivative-space containment, or if the degree-five capacity
was miscomputed, the lower bound 48 has no proof value. The correct response
would be withdrawal, not reinterpretation of the numerical table.

## 7. What is not proved

```text
ChowRank(perm_7)=48                       false claim
border Chow rank >=48                     not proved
all scalar invariants have ceiling 48      not proved
asymptotic tower fixed point known         not proved
general Glynn optimality                   open
```

## 8. Evidence boundary

The primary implementation reuses the canonical tower and bootstrap code. The
independent implementation must import none of those modules and reconstruct
all finite shadows and tower rows from explicit subsets.

Required status:

```text
new mathematical blocker found=false
new unrestricted lower bound=48
complete named scalar closure=48
exact rank claim=false
merge readiness=pending exact-head hosted CI
literature novelty=not established
```
