# Adversarial review: nonuniform shifted matrix ceiling

## Verdict

The block decomposition and support-area ceiling are valid general-`n`
consequences of the apolar subquotient interface and the common-degree
homogeneous block theorem.

The result introduces no numerical Chow-rank lower bound. It closes a named
matrix-image mechanism, not all graded presentations or syzygy methods.

## 1. Shift convention

The graded map is

```text
direct_sum_a R(-a)^(q_a) -> direct_sum_b R(-b)^(p_b).
```

At degree `d`, the source and target pieces are `M_(d-a)` and `M_(d-b)`, so a
nonzero entry has degree

```text
a-b >= 0.
```

Reversing this sign invalidates the line-specialization and level indices.

## 2. Only active blocks enter

A formal nonzero block may act trivially at a selected degree because one
Boolean level lies outside `0,...,n`. Such a block contributes neither a
numerator nor a denominator at that degree and is excluded from `B_d`.

## 3. Different blocks may use different Boolean witnesses

The full term envelope is a maximum over all maps from the differential
plane. For each block separately, one may select a line where a normal-rank
minor is nonzero. The proof requires only

```text
beta_full >= beta_block
```

for every block. It does not assert that one line simultaneously realizes all
block lower bounds.

## 4. The full image is not a direct sum

The proof uses only

```text
image(Phi) subset sum image(Phi_(b,a)).
```

Overlaps and cancellations can make the full image much smaller. No equality
or rank additivity is assumed.

## 5. Block normal rank

Each block has one common entry degree and its own normal rank
`r_(b,a)`. The sharp block bound retains this rank. The coarse support-area
bound discards it using only `r>=1`.

A rank statement for the complete nonuniform matrix over `k(s,t)` cannot be
substituted for the individual block ranks: constant row or column operations
between differently shifted summands need not be graded.

## 6. Rounding

The proof first derives

```text
N/beta <= sum N_block/beta_block.
```

It then takes one ceiling after the sum and bounds it by the sum of block
ceilings. The support-area bound is integral because `p_b*q_a*H_*` is an
integer. No untracked additive constant is needed.

## 7. Why the coarse coefficient is pq

For each active pair,

```text
max(p_b,q_a) <= p_b*q_a
```

because both multiplicities are positive integers. Summing over a subset of
all shift pairs gives

```text
sum p_b*q_a <= (sum p_b)(sum q_a)=p*q.
```

This is a route-complexity bound, not a claim that all blocks are populated.

## 8. Complexity interpretation

The conclusion

```text
K_n = Omega(n^(1/4))
```

is necessary only for this one matrix-image mechanism with both total free
ranks at most `K_n`. It is not a lower bound on the size of every proof,
Fitting presentation or resolution of the permanent.

The common-degree parent theorem has a stronger `Omega(sqrt(n))` condition.
The weakening is real: arbitrary shifts may create up to `p*q` independently
bounded blocks.

## 9. Dependencies

The theorem depends on:

1. apolar subquotient monotonicity for matrix-image ranks;
2. the Boolean envelope for Chow terms, including dependent-factor terms;
3. characteristic-zero strong Lefschetz for the squarefree Boolean algebra;
4. the common-degree homogeneous block theorem.

If one of these is withdrawn, the present theorem must be downgraded rather
than retained from the finite arithmetic.

## 10. Uncovered routes

The theorem does not cover:

- joint Fitting ideals or determinantal schemes;
- kernel dimensions, Betti numbers or Tor groups without a separate
  subquotient-monotonicity theorem;
- intersections or nonlinear combinations of several matrix images;
- representation-valued isotypes;
- higher syzygy modules;
- valuative ordinary-rank obstructions;
- Chow-realizability defects.

## 11. Final classification

```text
nonuniform shift-block decomposition=PASS
exact block-sum ceiling=PASS
support-area pq ceiling=PASS
bounded-size nonuniform matrices=CLOSED AT CENTRAL SCALE
sub-n^(1/4) square size reaches Glynn=NO FOR THIS MECHANISM
new numerical Chow-rank bound=NO
joint Fitting/minor route=OPEN
higher syzygy route=OPEN
representation-valued route=OPEN
exact rank for n>=6=OPEN
border-rank claim=NO
literature novelty=NOT ESTABLISHED
```
