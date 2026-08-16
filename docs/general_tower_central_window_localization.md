# Central-window localization of the permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note sharpens the fixed-codimension tail theorem by retaining the ambient
parameter `n`. It proves that all derivative degrees a linear distance above
the center contribute only an exponentially smaller additive correction to
the complete scalar-tower threshold. At central-binomial precision, only a
moderate-deviation window of width `O(sqrt(n log n))` above the center can
matter.

The result introduces no new numerical Chow-rank lower bound. It does not
analyze the recurrence inside the central window.

## 1. Setup

Let

\[
Q_{n,d}
=
\min\{q:B_{n,d}(q)=\binom nd^2\}
\]

be the saturation threshold of the exact scalar derivative-tower capacity.
Threshold monotonicity gives

\[
\Theta_n
=
Q_{n,n-1}.
\tag{1.1}
\]

The one-term Lipschitz theorem gives, for `t<=Q_(n,d)`,

\[
D_{n,d}(t)
\le
(Q_{n,d}-t)\binom nd.
\tag{1.2}
\]

## 2. Ambient-dependent transition constants

For

\[
2\le k\le\frac n2,
\]

define

\[
\boxed{
c_{n,k}
=
\max_{k\le a\le n}
\left[
\binom a{k-1}
-
\binom{a-1}k
-
1
\right]_+.
}
\tag{2.1}
\]

This is the ambient-truncated version of the universal constant `c_k`.

### Theorem 2.1

For every `2<=k<=n/2`,

\[
\boxed{
0
\le
Q_{n,n-k+1}-Q_{n,n-k}
\le
c_{n,k}.
}
\tag{2.2}
\]

### Proof

Put

\[
Q=Q_{n,n-k},
\qquad
M_0=\binom nk,
\qquad
M_1=\binom n{k-1}.
\]

Since `n>=2k`, one has `M_0>=M_1` and `Q>=M_0>=M_1`.

The proof of the universal tail theorem uses, for each

\[
r=Q-t,
\]

the least integer `a` satisfying

\[
\binom ak\ge r.
\]

Whenever `r<M_1`, such an `a` exists and necessarily satisfies `a<=n` because
`r<M_1<=M_0=binom(n,k)`. Therefore the proof only needs the maximum in (2.1),
not the unrestricted maximum over all `a`.

Explicitly, minimality gives

\[
r\ge\binom{a-1}k+1,
\]

while the rectangular product family gives

\[
F_{n,k}(D_{n,n-k}(t))
\le
\binom a{k-1}M_1
\le
(r+c_{n,k})M_1.
\]

The range `r>=M_1` is handled by the ambient bound

\[
F_{n,k}\le M_1^2\le rM_1.
\]

Substitution into the exact deficit transport at

\[
q=Q+c_{n,k}
\]

shows that every transported deficit is nonpositive. Hence the next row has
saturated. The lower inequality is threshold monotonicity. ∎

## 3. Binomial tail localization

The ambient-dependent constant has the immediate bound

\[
0\le c_{n,k}\le\binom n{k-1}.
\tag{3.1}
\]

### Theorem 3.1

For every integer

\[
2\le K\le\frac n2,
\]

\[
\boxed{
0
\le
\Theta_n-Q_{n,n-K}
\le
\sum_{j=1}^{K-1}\binom nj.
}
\tag{3.2}
\]

### Proof

Sum Theorem 2.1 for

\[
k=K,K-1,\ldots,2
\]

and apply (3.1). ∎

This theorem is stronger than the fixed-`K` statement: `K` may grow with
`n` all the way to the center.

## 4. Linear-distance localization

Let

\[
0<\alpha<\frac12,
\qquad
K_n=\lfloor\alpha n\rfloor.
\]

For the binary entropy

\[
H(\alpha)
=-\alpha\log\alpha
-(1-\alpha)\log(1-\alpha),
\]

the standard binomial-tail estimate gives

\[
\sum_{j=0}^{K_n-1}\binom nj
=
\exp\bigl(nH(\alpha)+O(\log n)\bigr).
\tag{4.1}
\]

### Corollary 4.1

\[
\boxed{
0
\le
\Theta_n-Q_{n,n-K_n}
\le
\exp\bigl(nH(\alpha)+O(\log n)\bigr).
}
\tag{4.2}
\]

Since

\[
H(\alpha)<\log2
\qquad
(\alpha<1/2),
\]

the top `alpha n` derivative degrees contribute an exponentially smaller
correction than the central-binomial scale.

Equivalently, for every fixed `epsilon>0`, the polynomial-scale behavior of
`Theta_n` is already determined by the row at degree

\[
d_n
=
\left(\frac12+\epsilon\right)n+O(1).
\]

No derivative degree above this row can change any base-two polynomial
normalization.

## 5. Moderate-deviation localization

Let

\[
X_n\sim\operatorname{Bin}(n,1/2).
\]

If

\[
K-1\le\frac n2-w,
\]

then Hoeffding's inequality gives

\[
\sum_{j=0}^{K-1}\binom nj
=
2^n\Pr(X_n\le K-1)
\le
2^n\exp\left(-\frac{2w^2}{n}\right).
\tag{5.1}
\]

### Theorem 5.1 -- central-window reduction

If `K_n` and `w_n` satisfy

\[
K_n-1\le\frac n2-w_n
\]

and

\[
\frac{2w_n^2}{n}-\log(n+1)
\longrightarrow+\infty,
\tag{5.2}
\]

then

\[
\boxed{
\Theta_n-Q_{n,n-K_n}
=
o\left(
\binom n{\lfloor n/2\rfloor}
\right).
}
\tag{5.3}
\]

### Proof

Theorem 3.1 and (5.1) give

\[
\Theta_n-Q_{n,n-K_n}
\le
2^n\exp(-2w_n^2/n).
\]

The largest binomial coefficient is at least the average coefficient:

\[
\binom n{\lfloor n/2\rfloor}
\ge
\frac{2^n}{n+1}.
\]

The ratio is therefore at most

\[
(n+1)\exp(-2w_n^2/n),
\]

which tends to zero under (5.2). ∎

More generally, for any fixed `A>=0`, if

\[
\frac{2w_n^2}{n}-(A+1)\log n
\longrightarrow+\infty,
\tag{5.4}
\]

then

\[
\Theta_n-Q_{n,n-K_n}
=
o\left(
\frac1{n^A}
\binom n{\lfloor n/2\rfloor}
\right).
\tag{5.5}
\]

Thus precision at every fixed inverse-polynomial multiple of the central
binomial coefficient requires studying only derivative degrees in a window

\[
\boxed{
d=\frac n2+O(\left(\sqrt{n\log n}\right)).}
\tag{5.6}
\]

The constant in the `O` depends on the desired polynomial precision.

## 6. Exact finite replay

The audit reads the immutable PR #51 threshold rows for `3<=n<=10` and checks
every legal pair `(n,k)` with `2<=k<=n/2`.

```text
ambient-dependent transition checks   16
c_(n,k)<=binom(n,k-1) checks           16
summed binomial-tail checks            16
```

For example:

```text
n=8:
  k=2  c_(8,2)=1   observed gap=1
  k=3  c_(8,3)=5   observed gap=2
  k=4  c_(8,4)=20  observed gap=7

Theta_8-Q_(8,4)=10
sum_(j=1)^3 binom(8,j)=92.
```

The finite inequalities validate the interface but do not prove the
asymptotic estimates; those follow from the analytic arguments above.

## 7. Research consequence

The scalar tower's unresolved polynomial behavior is now localized to a
central moderate-deviation window. Neither the fixed-codimension tail nor any
linearly separated high-degree row can determine the remaining gap to Glynn.

The next valid scalar problem is the second-order product-shadow transform for

\[
d=\frac n2+O(\left(\sqrt{n\log n}\right))
\]

and deficits on the corresponding central-binomial scale.

If this central-window recurrence has a bounded normalization by
`binom(n,floor(n/2))`, the scalar route is formally separated from Glynn by a
factor of order `sqrt(n)`. If it does not, the precise prefactor-amplification
mechanism must be exhibited before extending any finite table.
