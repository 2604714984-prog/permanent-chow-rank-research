# Adversarial review: private-polar one-term gain

## Verdict

`FATAL=0`, `MAJOR=0`, `MINOR=0` after the checks below.

The theorem is a zero-intersection statement for literal sums of Chow
derivative spaces.  It does not identify a coupled catalectic image with that
literal sum and does not promote a new exact Chow rank.

## 1. Does the argument assume `qn>=m^2` without saying so?

No.  The strict shifted theorem first disposes of `qn<=m^2` by the already
proved strict/equality endpoint.  Only in the remaining case is

```text
s=qn-m^2>0
```

introduced, and only there is `k<=s` used.

## 2. Is the component essential space really enough?

Yes.  The inherited private-polar theorem uses

```text
M_i=partial^(m-1) f_i
```

rather than the full factor span of `T_i`.  A nonzero `f_i` belongs to
`Sym^m(M_i)` and is concise on that space by definition.  Unused factor
directions are deliberately discarded.  Every `r_i<=n` because `f_i` was
obtained from a degree-`n` Chow term.

## 3. Why does no private polar imply `r_i<=k`?

The private-polar identity is

```text
dim S_i=r_i-t_i
t_i=dim(M_i intersect sum_(j!=i)M_j)
```

and the kernel projection lemma gives `t_i<=k`.  Thus `S_i=0` implies

```text
r_i=t_i<=k.
```

Summing gives `D<=qk`, while `D=dim M+k>=m^2+k`.  Hence
`(q-1)k>=m^2`.

## 4. Check the shifted-count algebra

With `s=qn-m^2`,

```text
(q-1)s < m^2
```

is exactly equivalent to

```text
(q-1)n < m^2.
```

Indeed, after expanding and dividing by the positive integer `q`, both sides
reduce to the second inequality.  No asymptotic approximation is used.

## 5. Is the descended private polar a permanent derivative?

Yes.  The private polar is constructed by an ambient covector which kills all
other selected component essential spaces.  It is literally a first derivative
of the chosen

```text
f in D_m(perm_n),
```

so it belongs to `D_(m-1)(perm_n)`.  It is also supported on `M_i`.  The proof
does not claim that `f_i` itself is a permanent derivative.

## 6. Why is strict support required in Theorem 3.1?

The descended object is one nonzero form supported on at most `n` variables.
The strict factor-span theorem excludes it when

```text
n < (m-1)^2.
```

At equality a one-component embedded-subpermanent phenomenon can occur in
principle; the proof does not silently invoke direct-sum indecomposability for
a single component.  The strict sign is therefore intentional.

## 7. Equality-simplex arithmetic

At

```text
(q-1)n=m^2
```

one has `s=n`.  If all private spaces vanish, then

```text
m^2 <= (q-1)k
k <= n,
```

so `k=n`.  The remaining bounds force

```text
sum_i r_i=qn
r_i=n for every i
dim M=m^2.
```

This is exact arithmetic, not a genericity claim.

## 8. Why is every proper subcollection direct?

Let `K` be the kernel of the sum map.  Under no-private, the projection
`K -> M_i` is onto for every `i`.  Both spaces have dimension `n`, hence that
projection is an isomorphism.  A relation supported on a proper subcollection
omits some label `i`, so its `i`-th component is zero.  Injectivity of the
projection then forces the relation itself to be zero.

## 9. Does the two-block covector always exist?

Yes.  Choose `M_1,...,M_(q-1)` as the direct coordinate decomposition of `M`.
The last block `M_q` projects isomorphically to every coordinate block.  If its
parametrization has invertible coordinate maps `phi_j`, choose any nonzero
`alpha_1` and set

```text
alpha_2=-alpha_1 phi_1 phi_2^(-1)
```

with the evident convention on composition.  The covector supported on blocks
1 and 2 then vanishes identically on the graph `M_q`; both restrictions are
nonzero.

## 10. Could the two surviving polars cancel?

No.  They lie in symmetric powers of the direct spaces `M_1` and `M_2`.
Their intersection in positive degree is zero.  Conciseness makes both first
polars nonzero, so their sum is nonzero.

## 11. Why is `2n<=(m-1)^2` enough at equality?

The descended form `g` is supported on `M_1 direct_sum M_2`.

- If its essential dimension is strictly below `(m-1)^2`, the permanent
  shadow floor is contradicted.
- If equality holds, both direct components are necessary on complementary
  essential subspaces, giving a nontrivial direct-sum decomposition of a
  minimal-shadow degree-`m-1` permanent derivative.

The previously proved scalar-center theorem excludes the second alternative
because `m-1>=3`.

Thus a non-strict two-block support inequality is sufficient.

## 12. Coupled/literal firewall

The theorem starts with one selected element

```text
f in D_m(perm_n) intersect sum_i D_m(T_i)
```

and chooses representatives `f_i`.  It never asserts

```text
D_m(sum_i T_i)=sum_i D_m(T_i).
```

The existing coupled/literal firewall remains intact.

## 13. Finite replay boundary

The scans through `m=128` and `m=96` verify integer conditions, examples and
the simplex model.  They are not the proof.  The general proof is the private
polar dimension argument, exact no-private squeezing and the two-block
descent.

## 14. What remains open

This result does not address

```text
n=(m-1)^2 with strict shifted count,
(q-1)n>m^2,
cubic rows (4,3,3) and (6,3,2).
```

The next continuation must use higher-cardinality private polar spaces,
relation-matroid structure, or the compressed-center interface rather than
repeating the same one-private-direction argument.
