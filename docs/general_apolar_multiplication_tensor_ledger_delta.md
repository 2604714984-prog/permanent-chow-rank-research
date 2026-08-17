# Research-ledger delta: apolar multiplication tensors

## Status

This delta belongs to the stacked branch
`research/apolar-multiplication-tensor-framework` and supplements
`RESEARCH_LEDGER.md` until the open stack is consolidated.

No existing numerical Chow-rank boundary changes in this result.

## New legal nonlinear interface

### Chow-term Boolean algebra subquotient

For every Chow term

```text
T=product_i ell_i,
```

including dependent or repeated factors, define

```text
B_n=k[z_1,...,z_n]/(z_i^2)
psi(alpha)=sum_i alpha(ell_i) z_i
C_T=im psi.
```

If `lambda` extracts the coefficient of `z_1...z_n`, then

```text
A_T ~= C_T / Ann_(C_T)(lambda).
```

Thus every term apolar algebra is a quotient of a subalgebra of the Boolean
square-zero algebra.

### Decomposition algebra subquotient

For `f=sum_i T_i`,

```text
R/intersection_i T_i^perp
```

embeds as an algebra in the termwise direct product and surjects onto `A_f`.
Tensor rank and border rank of multiplication are monotone under both steps
and subadditive on direct products.

Hence

```text
R(mu_(A_f)) <= r R(mu_(B_n))
borderR(mu_(A_f)) <= r borderR(mu_(B_n)).
```

### Permanent diagonal Segre algebra

The permanent apolar algebra is

```text
A_(perm_n) ~= B_n # B_n
             = direct_sum_d B_n[d] tensor B_n[d]
```

with disjoint-union multiplication and dimension

```text
binom(2n,n).
```

### Baseline bounds

Since `borderR(mu_(B_n))=2^n` and every unital multiplication tensor is
concise,

```text
ChowRank(perm_n)
 >= ceil(binom(2n,n)/2^n).
```

This is exactly the all-degree equal-weight scalar ratio already present in
the repository and is not a new numerical improvement.

Using the Alder--Strassen lower bound and the published `W_3^(tensor n)`
upper decomposition,

```text
ChowRank(perm_n)
 >= ceil(
      (2*binom(2n,n)-1)
      /((n+2)*2^(n-1))
    ).
```

This ordinary baseline is asymptotically weaker than the border baseline.

## Route status

```text
apolar multiplication tensor framework=OPEN
Chow-term algebra Boolean envelope=PROVED
permanent diagonal Segre structure=PROVED
border baseline=REPRODUCES EXISTING SCALE
ordinary baseline=WEAKER THAN EXISTING BOUNDS

smoothability of A_perm=OPEN
border-rank excess of A_perm=OPEN
ordinary bilinear complexity of B_n#B_n=OPEN
homogeneous multiplication slices=OPEN
asymptotic tensor functionals=OPEN
```

## Strict boundary

This result does not claim:

- a new best finite-`n` lower bound;
- smoothability or nonsmoothability of the permanent apolar algebra;
- exact tensor rank or border rank of its multiplication tensor;
- a border-Chow-rank improvement over the current repository;
- exact Chow rank for any `n>=6`; or
- general Glynn optimality.

## Next authorized interface

The next step is not another generic tensor-rank estimate.  It must determine
one of:

1. smoothability or a border-rank excess for `B_n#B_n`;
2. an ordinary bilinear-complexity lower bound for `B_n#B_n` that is large
   relative to the Boolean `W`-tensor denominator;
3. a homogeneous multiplication slice with a uniform dependent-factor
   Boolean envelope; or
4. an asymptotic tensor functional whose ratio exceeds the scalar tower.

If all such algebra-structure ratios remain centrally capped, the project
should return to Chow-realizability defects rather than enlarge the tensor
framework mechanically.
