# Incidence bounds and the entropy-scale barrier for permanent product shadows

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note proves a uniform incidence sandwich for the exact product-shadow
function and its inverse. It then identifies a strict research boundary:

> at linear derivative degree, the exact product shadow preserves exponential
> rate, so first-order entropy cannot distinguish central-binomial scale from
> Glynn scale.

The result introduces no new numerical Chow-rank lower bound. It does not
determine the polynomial normalization of the scalar tower.

## 1. Exact product shadows

Let

\[
\mathcal U_d
=
\binom{[n]}d\times\binom{[n]}d,
\qquad
A_{n,d}=|\mathcal U_d|=\binom nd^2.
\]

The exact product-shadow theorem defines

\[
F_{n,d}(b)
=
\min_{\substack{S\subseteq\mathcal D_d(\operatorname{perm}_n)\\
\dim S=b}}
\dim\partial S.
\]

Torus specialization and compression identify this subspace minimum with the
minimum lower-shadow size of a `b`-element coordinate family in
`\mathcal U_d`.

The inverse capacity is

\[
\Gamma_{n,d}(C)
=
\max\{b:F_{n,d}(b)\le C\}.
\]

## 2. Incidence sandwich

### Theorem 2.1

For every `1<=d<=n` and every `0<=b<=A_(n,d)`,

\[
\boxed{
\frac{d^2}{(n-d+1)^2}\,b
\le
F_{n,d}(b)
\le
\min\{A_{n,d-1},d^2b\}.
}
\tag{2.1}
\]

### Proof

Consider the bipartite incidence graph between `\mathcal U_d` and
`\mathcal U_(d-1)`.

A degree-`d` cell `(R,C)` has exactly

\[
d^2
\]

lower neighbors, obtained by deleting one row and one column.

A degree-`d-1` cell `(I,J)` has exactly

\[
(n-d+1)^2
\]

upper containers, obtained by adding one row and one column.

Let `\mathcal A subseteq \mathcal U_d` have size `b`. Counting incidences
between `\mathcal A` and its lower shadow gives

\[
b d^2
\le
|\partial\mathcal A|(n-d+1)^2.
\]

This proves the lower bound.

For the upper bound, each member of `\mathcal A` contributes at most `d^2`
lower cells, so

\[
|\partial\mathcal A|\le d^2b.
\]

The shadow is also contained in the complete lower layer of size
`A_(n,d-1)`. Taking the minimum over coordinate families and using the exact
subspace-coordinate equality proves (2.1). ∎

The lower bound is a bounded-codegree estimate. It does not classify
minimizers or use Kruskal--Katona compression.

## 3. Inverse-shadow sandwich

### Corollary 3.1

For every legal shadow capacity `C`,

\[
\boxed{
\min\left\{
A_{n,d},
\left\lfloor\frac C{d^2}\right\rfloor
\right\}
\le
\Gamma_{n,d}(C)
\le
\min\left\{
A_{n,d},
\left\lfloor
\frac{C(n-d+1)^2}{d^2}
\right\rfloor
\right\}.
}
\tag{3.1}
\]

### Proof

For the lower bound, set

\[
b=\min\left\{A_{n,d},\left\lfloor C/d^2\right\rfloor\right\}.
\]

The upper inequality in (2.1) gives `F_(n,d)(b)<=C`, hence
`\Gamma_(n,d)(C)>=b`.

For the upper bound, `F_(n,d)(b)<=C` and the lower inequality in (2.1)
imply

\[
b\le\frac{C(n-d+1)^2}{d^2}.
\]

Apply the ambient cap and integer rounding. ∎

## 4. Linear-degree exponential-rate identity

Fix `0<alpha<1` and let

\[
d_n=\alpha n+O(1).
\]

Suppose `b_n>=1` satisfies

\[
b_n=\exp(\zeta n+o(n)).
\]

### Corollary 4.1

\[
\boxed{
F_{n,d_n}(b_n)
=
\exp(\zeta n+o(n)).
}
\tag{4.1}
\]

### Proof

In (2.1), the lower multiplicative factor

\[
\frac{d_n^2}{(n-d_n+1)^2}
\]

is bounded away from zero and infinity. The upper factor `d_n^2` is
polynomial in `n`. Multiplying by either factor changes the logarithm by only
`O(log n)=o(n)`. ∎

The same conclusion holds for the inverse capacity: away from ambient
truncation, `Gamma` preserves exponential rate.

Thus the exact Ferrers shadow may contain decisive polynomial information, but
its first-order exponential transform is the identity.

## 5. Exponential rate of the scalar tower

Let

\[
\Theta_n=Q_{n,n-1}
\]

be the complete scalar derivative-tower lower bound, using threshold
monotonicity from the fixed-codimension tail theorem.

The literal one-term cap forces

\[
Q_{n,d}\ge\binom nd.
\]

At the central degree,

\[
\Theta_n
\ge
\binom n{\lfloor n/2\rfloor}.
\tag{5.1}
\]

On the other hand, Glynn's decomposition contains `2^(n-1)` Chow terms. Since
the tower capacity is valid for every actual decomposition,

\[
\Theta_n\le2^{n-1}.
\tag{5.2}
\]

Stirling's formula gives

\[
\binom n{\lfloor n/2\rfloor}
=
\frac{2^n}{\sqrt{\pi n/2}}\,(1+o(1)).
\]

### Theorem 5.1 -- entropy-scale barrier

\[
\boxed{
\lim_{n\to\infty}
\frac1n\log\Theta_n
=
\log2.
}
\tag{5.3}
\]

### Proof

Combine (5.1), (5.2), and Stirling's formula. ∎

This theorem is elementary after the full tower is defined, but it has a
strict methodological consequence:

```text
central-binomial scale: 2^n/sqrt(n)
Glynn scale:            2^(n-1)
```

have the same exponential rate. Therefore an analysis retaining only
`n^(-1) log` quantities cannot decide whether the scalar tower closes the
remaining `sqrt(n)` gap.

## 6. Required next scale

The scalar asymptotic must be studied at second order. Natural normalizations
include

\[
\frac{\Theta_n}{\binom n{\lfloor n/2\rfloor}}
\]

and

\[
\log\Theta_n-n\log2+\frac12\log n.
\]

Likewise, the product-shadow input requires polynomial-prefactor estimates for

\[
F_{n,\alpha n}(b)
\]

rather than only its exponential rate.

The exact finite values

```text
n=3,...,10:
Theta_n = 4,8,15,27,49,90,164,307
```

give ratios to the central binomial coefficient between approximately `1.2`
and `1.5`, but this finite observation is not promoted to a uniform bound.

## 7. Exact replay

For every

\[
3\le n\le8,
\qquad
2\le d\le n-1,
\]

the exact Ferrers tables verify (2.1) at every family size and (3.1) at every
shadow capacity.

```text
shadow-sandwich checks = 17,378
inverse-sandwich checks = 17,378
```

The audit also binds the current PR #51 saturation table through `n=10` and
records its central-binomial normalization. No regression value is used as an
asymptotic proof.

## 8. Research decision

The planned first-order entropy transform is now closed as insufficient. The
next scalar task is:

\[
\boxed{
\text{second-order polynomial-scale asymptotics of }
F_{n,\alpha n}
\text{ and the deficit recurrence}.
}
\]

If that analysis proves

\[
\Theta_n=O\left(\binom n{\lfloor n/2\rfloor}\right),
\]

the exact scalar route remains a factor `Theta(sqrt(n))` below Glynn and should
be treated as formally closed. If it produces an unbounded prefactor, the
degree interval and mechanism must be identified before any further finite
table is extended.
