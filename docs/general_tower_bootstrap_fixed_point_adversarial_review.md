# Adversarial review: derivative-tower bootstrap fixed point

## Verdict

The promotion theorem is a valid ordinary characteristic-zero implication,
provided its two named dependencies remain valid:

1. the derivative-tower capacity theorem; and
2. the complementary-intersection first-Koszul residual theorem.

The exact `n=7` arithmetic supports the stacked conclusions

```text
ChowRank(perm_7) >= 47
scalar tower/Koszul bootstrap fixed point at n=7 = 47.
```

The second statement is a route boundary only. It is not an upper bound on the
actual Chow rank.

## 1. Selection chronology

The operator may select `q` terms only when a previously proved lower bound
`L>=q` guarantees that every decomposition has at least `q` nonzero terms.
The proof respects this chronology:

```text
36 is independent first-Koszul input
36 -> 46 is proved first
46 -> 47 is used only afterwards
```

The `q=46` endpoint is therefore legal. Using it directly from the initial
bound 36 would be circular.

Regression requirement:

```text
bootstrap sequence must equal [36,46,47,47]
```

and not merely report the final number 47.

## 2. Coupled versus literal derivative spaces

The tower capacity bounds

```text
E_d(perm_n) intersect sum_i D_d(T_i).
```

For the selected polynomial sum `Q=sum_i T_i`, the only allowed transfer is

```text
D_d(Q) subset sum_i D_d(T_i).
```

No equality is used. The proof remains valid if the coupled catalectic rank is
strictly smaller than the dimension of the literal sum.

Any rewrite replacing containment by equality is a mathematical regression.

## 3. Complementary degree

At Koszul output degree `m`, the residual loss is controlled at degree

```text
r=n-m.
```

For the decisive `46 -> 47` certificate:

```text
n=7
m=2
r=5
B_(7,5)(46)=405.
```

Using a degree-two capacity in place of `B_(7,5)` would be invalid.

## 4. The all-term contradiction

At input lower bound 46, assume a 46-term decomposition and select all terms.
The residual is zero. Nevertheless the valid residual theorem and tower cap
would give

```text
A_(7,2)-49*B_(7,5)(46)
=20,384-49*405
=539>0.
```

This contradiction proves that 46 terms are impossible. Writing the same
arithmetic as `46+ceil(539/994)=47` is only a compact counting form; the
logical content is the nonzero lower bound for the zero residual.

## 5. Fixed-point interpretation

The exact scan at input 47 covers

```text
m=2,3,4,5
q=1,...,47.
```

Its largest output is 47. This proves only:

```text
no further promotion follows from the current B capacities plus the current
first-Koszul residual inequality.
```

It does not prove:

- `ChowRank(perm_7)=47`;
- a lower bound ceiling for higher Koszul or Young flattenings;
- a ceiling for representation-valued or valuative invariants;
- a border-rank statement; or
- an asymptotic ceiling for general `n`.

## 6. Assume every hidden assumption is false

If the selection chronology, the coupled/literal containment, or the
complementary-degree residual theorem fails, the number 47 has no proof value.
The finite recurrence and hashes would then be only diagnostics. The result
must be withdrawn rather than repaired by reinterpreting a numerical table.

## 7. Independent replay boundary

The independent implementation must not import either

```text
general_tower_bootstrap_fixed_point.py
general_derivative_tower_capacity.py
general_exact_product_shadow.py
```

It reconstructs:

- colex order;
- first shadows;
- first-container weights;
- the Ferrers integer recurrence;
- all capacity rows through degree five and 47 terms;
- every bootstrap candidate at inputs 36, 46 and 47.

Required outputs include

```text
B_(7,4)(20)=341
B_(7,5)(46)=405
B_(7,5)(47)=426
36 -> 46 -> 47 -> 47
```

The primary and independent scan hashes must agree.

## 8. Severity assessment

```text
new mathematical blocker found=false
new unrestricted lower bound=47
fixed-point boundary=valid for named scalar route
exact rank claim=false
merge readiness=pending exact-head hosted CI
literature novelty=not established
```
