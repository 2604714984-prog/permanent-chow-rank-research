# A polynomial ceiling for the complete scalar permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

Let

\[
\Theta_n=\max_{1\le d\le n-1}Q_{n,d}
\]

be the complete scalar derivative-tower lower bound defined by the preceding
stacked results. This note proves

\[
\boxed{
\Theta_n
=
O\!\left(
 n^{1/4}\binom n{\lfloor n/2\rfloor}
\right)
=
O\!\left(\frac{2^n}{n^{1/4}}\right).
}
\tag{0.1}
\]

Consequently,

\[
\boxed{
\frac{2^{n-1}}{\Theta_n}=\Omega(n^{1/4}).
}
\tag{0.2}
\]

Thus the **complete exact scalar derivative tower**, including every output
degree, exact Ferrers product shadows, repeated block projection, direct
saturation, and the full-degree tail, cannot by itself prove the conjectural
Glynn-optimal lower bound `2^(n-1)` for all large `n`.

This is a ceiling on a named lower-bound mechanism, not an upper bound on the
actual Chow rank. It does not obstruct a non-scalar, multigraded,
representation-valued, valuative, or Chow-realizability argument.

## 1. Exact inputs

Put

\[
M_{n,d}=\binom nd,
\qquad
A_{n,d}=M_{n,d}^2.
\]

The complete tower has capacities `B_(n,d)(q)` and deficits

\[
D_{n,d}(q)=A_{n,d}-B_{n,d}(q).
\]

Its saturation threshold is

\[
Q_{n,d}=\min\{q:D_{n,d}(q)=0\}.
\tag{1.1}
\]

The shadow-complement form of the exact recurrence is

\[
H_{n,d}(q)
=
\max\left\{
0,
A_{n,d}-qM_{n,d},
F_{n,n-d+1}\bigl(D_{n,d-1}(q)\bigr)
\right\},
\tag{1.2}
\]

\[
D_{n,d}(q)
=
\max_{0\le t\le q}
\left(
H_{n,d}(t)-(q-t)M_{n,d}
\right).
\tag{1.3}
\]

Here `F_(n,k)(b)` is the exact minimum simultaneous lower shadow of a
`b`-plane in `D_k(perm_n)`.

The parent branch also proves the terminal localization estimate. For
`1<=K<=n/2`,

\[
\Theta_n-Q_{n,n-K}
\le
\sum_{j=1}^{K-1}\binom nj.
\tag{1.4}
\]

The slightly weaker replacement by `sum_(j=0)^K binom(n,j)` is sufficient
below and avoids irrelevant endpoint conventions.

## 2. Elementary threshold bounds

### Lemma 2.1 -- one-step saturation

For every `2<=d<=n-1`,

\[
\boxed{Q_{n,d}\le Q_{n,d-1}+M_{n,d}.}
\tag{2.1}
\]

### Proof

Set `q=Q_(n,d-1)+M_(n,d)`.

If `t<Q_(n,d-1)`, then `H_(n,d)(t)<=A_(n,d)` and

\[
(q-t)M_{n,d}\ge M_{n,d}^2=A_{n,d}.
\]

If `t>=Q_(n,d-1)`, the preceding deficit is zero, so

\[
H_{n,d}(t)
=
\max\{0,A_{n,d}-tM_{n,d}\}
\le
(q-t)M_{n,d},
\]

because `q>=M_(n,d)`. Every term in (1.3) is therefore nonpositive, and
`D_(n,d)(q)=0`. ∎

### Corollary 2.2 -- lower-half start

For `d<n/2`,

\[
Q_{n,d}
\le
\sum_{j=1}^{d}\binom nj
\le
\binom nd\frac{n-d+1}{n-2d+1}.
\tag{2.2}
\]

### Proof

Iterate Lemma 2.1 from `Q_(n,1)=n`. For `j<=d`,

\[
\frac{\binom n{j-1}}{\binom nj}
=
\frac{j}{n-j+1}
\le
\frac{d}{n-d+1}<1.
\]

The second inequality is the corresponding geometric-series bound. ∎

### Lemma 2.3 -- deficit Lipschitz bound

For `0<=t<=Q_(n,d)`,

\[
\boxed{
D_{n,d}(t)
\le
\bigl(Q_{n,d}-t\bigr)M_{n,d}.
}
\tag{2.3}
\]

### Proof

Block projection gives

\[
B_{n,d}(q+1)\le B_{n,d}(q)+M_{n,d}.
\]

Equivalently,

\[
D_{n,d}(q)\le D_{n,d}(q+1)+M_{n,d}.
\]

Iterate to `D_(n,d)(Q_(n,d))=0`. ∎

## 3. Central product-shadow smoothing

The key new input is an upper construction for exact product shadows near the
middle levels.

### Lemma 3.1 -- hypergeometric atom bound

There is a universal constant `C_0` such that, whenever

\[
\frac n3\le k\le\frac{2n}3,
\]

and `X` is the size of the intersection of a uniformly random `k`-subset of
`[n]` with a fixed `floor(n/2)`-subset, then

\[
\max_j\Pr(X=j)\le\frac{C_0}{\sqrt n}.
\tag{3.1}
\]

### Proof

Write `p=floor(n/2)` and `theta=k/n`. The hypergeometric law is the
conditional law of

\[
X_1\sim\operatorname{Bin}(p,\theta)
\]

given

\[
X_1+X_2=k,
\qquad
X_2\sim\operatorname{Bin}(n-p,\theta),
\]

with the two binomials independent. Uniform Stirling bounds, valid because
`theta` lies in `[1/3,2/3]`, give

\[
\max_j\Pr(X_i=j)=O(n^{-1/2})
\]

and

\[
\Pr(X_1+X_2=k)=\Theta(n^{-1/2}).
\]

The conditional point probability is therefore `O(n^(-1/2))`, uniformly in
`k`. ∎

### Lemma 3.2 -- one-coordinate density-preserving shadow

Let

\[
N_k=\binom nk.
\]

For every integer `0<=u<=N_k`, with `k` in the range of Lemma 3.1, there is a
family

\[
\mathcal A\subseteq\binom{[n]}k,
\qquad |\mathcal A|=u,
\]

such that

\[
\frac{|\partial\mathcal A|}{N_{k-1}}
\le
\frac{u}{N_k}+\frac{2C_0}{\sqrt n}.
\tag{3.2}
\]

### Proof

Fix a half-set `P` and put

\[
\mathcal H_t^{(k)}
=
\{S:|S\cap P|\le t\}.
\]

Choose `t` with

\[
|\mathcal H_t^{(k)}|
\le u
\le
|\mathcal H_{t+1}^{(k)}|
\]

and fill an arbitrary part of the next layer to obtain `A` of size `u`.
Deleting one element cannot increase `|S cap P|`, so

\[
\partial\mathcal A\subseteq\mathcal H_{t+1}^{(k-1)}.
\tag{3.3}
\]

Couple a uniform `(k-1)`-set `Y` with a uniform `k`-set `Z` by adding a
uniform missing element. If `|Y cap P|<=t+1`, then `|Z cap P|<=t+2`. Hence

\[
\Pr_{k-1}(|Y\cap P|\le t+1)
\le
\Pr_k(|Z\cap P|\le t)
+2\max_j\Pr_k(|Z\cap P|=j).
\]

Use Lemma 3.1 and

\[
\Pr_k(|Z\cap P|\le t)
\le u/N_k.
\]

The empty and full families are immediate endpoint cases. ∎

### Theorem 3.3 -- central product-shadow smoothing

There is a universal constant `C_1` such that for every

\[
\frac n3\le k\le\frac{2n}3
\]

and every `0<=b<=N_k^2`,

\[
\boxed{
\frac{F_{n,k}(b)}{N_{k-1}^2}
\le
\frac{b}{N_k^2}
+
\frac{C_1}{\sqrt n}.
}
\tag{3.4}
\]

### Proof

Set

\[
u=\left\lceil\frac{b}{N_k}\right\rceil.
\]

Choose `A` from Lemma 3.2 and consider the cylinder

\[
\mathcal A\times\binom{[n]}k.
\]

It has at least `b` elements. Select any `b`-element subfamily. Its
simultaneous lower shadow is contained in

\[
\partial\mathcal A\times\binom{[n]}{k-1}.
\]

Thus

\[
\frac{F_{n,k}(b)}{N_{k-1}^2}
\le
\frac{|\partial\mathcal A|}{N_{k-1}}
\le
\frac{b}{N_k^2}
+
\frac1{N_k}
+
\frac{2C_0}{\sqrt n}.
\]

In the central range, `1/N_k` is exponentially small and can be absorbed into
`C_1/sqrt(n)`. Coordinate families are actual permanent-derivative
subspaces, so this is a valid upper bound for the exact subspace minimum. ∎

## 4. Transport across the central window

For brevity write

\[
Q_d=Q_{n,d},\qquad M_d=M_{n,d}.
\]

Assume that degree `d-1` and complementary shadow degree `n-d+1` lie in the
central range of Theorem 3.3.

### Lemma 4.1 -- central threshold transfer

There is a universal `C_2` such that

\[
Q_d
\le
\begin{cases}
\displaystyle
\frac{M_d}{M_{d-1}}Q_{d-1}
+rac{C_2M_d}{\sqrt n}+1,
& M_d\ge M_{d-1},\\[10pt]
\displaystyle
Q_{d-1}
+rac{C_2M_d}{\sqrt n}+1,
& M_d\le M_{d-1}.
\end{cases}
\tag{4.1}
\]

### Proof

For `t<Q_(d-1)`, Lemma 2.3 and Theorem 3.3 give

\[
F_{n,n-d+1}(D_{d-1}(t))
\le
M_d^2
\left(
\frac{Q_{d-1}-t}{M_{d-1}}
+
\frac{C_2}{\sqrt n}
\right).
\tag{4.2}
\]

A sufficient condition for the shadow term in (1.3) to vanish at `q` is

\[
q
\ge
 t+
\frac{M_d}{M_{d-1}}(Q_{d-1}-t)
+
\frac{C_2M_d}{\sqrt n}.
\tag{4.3}
\]

The literal term is simultaneously handled by `q>=M_d`.

If `M_d/M_(d-1)>=1`, the right side of (4.3) is largest at `t=0`; if the ratio
is at most one, it is largest at `t=Q_(d-1)`. The integrality rounding costs
at most one. Finally `Q_(d-1)>=M_(d-1)` makes the displayed bounds at least
`M_d`, so no separate maximum is needed. ∎

### Corollary 4.2

On the increasing side of the central binomial sequence,

\[
\frac{Q_d}{M_d}
\le
\frac{Q_{d-1}}{M_{d-1}}
+O(n^{-1/2})+rac1{M_d}.
\tag{4.4}
\]

On the decreasing side,

\[
Q_d\le Q_{d-1}+O(M_dn^{-1/2})+1.
\tag{4.5}
\]

## 5. Parameterized ceiling

Let

\[
M_*=\binom n{\lfloor n/2\rfloor}.
\]

Choose a window width `w=w_n` satisfying

\[
\sqrt n\ll w\ll n,
\tag{5.1}
\]

and put, with harmless integer rounding,

\[
d_-=n/2-w,\qquad d_+=n/2+w.
\]

For large `n`, the entire window and all complementary shadow degrees lie in
`[n/3,2n/3]`.

### Proposition 5.1 -- central-window bound

\[
\boxed{
\frac{Q_{n,d_+}}{M_*}
=
O\left(
\frac n w+
\frac w{\sqrt n}+1
\right).
}
\tag{5.2}
\]

### Proof

Corollary 2.2 gives

\[
\frac{Q_{n,d_-}}{M_{n,d_-}}=O(n/w).
\tag{5.3}
\]

Iterate (4.4) from `d_-` to a central maximum. There are `O(w)` steps, so

\[
\frac{Q_{n,\lfloor n/2\rfloor}}{M_*}
=
O\left(
\frac n w+
\frac w{\sqrt n}+1
\right).
\tag{5.4}
\]

On the decreasing side, sum (4.5). Since

\[
\sum_dM_{n,d}=2^n
\]

and, by Stirling, `M_*=Theta(2^n/sqrt(n))`, the total smoothing cost is
`O(M_*)`; the `O(w)` integer cost is negligible. This proves (5.2). ∎

### Proposition 5.2 -- terminal tail

\[
\boxed{
\frac{\Theta_n-Q_{n,d_+}}{M_*}
=
O\left(
\sqrt n\exp(-2w^2/n)
\right).
}
\tag{5.5}
\]

### Proof

Apply the terminal localization estimate (1.4) with

\[
K=n-d_+.
\]

The resulting lower binomial tail is at distance `w+O(1)` from the mean.
Hoeffding's inequality gives

\[
\sum_{j\le n/2-w+O(1)}\binom nj
\le
2^n\exp(-2w^2/n+O(w/n)).
\]

Divide by `M_*=Theta(2^n/sqrt(n))`. ∎

Combining the propositions yields

\[
\boxed{
\frac{\Theta_n}{M_*}
=
O\left(
\frac n w+
\frac w{\sqrt n}+1+
\sqrt n\exp(-2w^2/n)
\right).
}
\tag{5.6}
\]

## 6. Optimization

Take

\[
w=\left\lceil n^{3/4}\right\rceil.
\]

Then

\[
\frac n w=\Theta(n^{1/4}),
\qquad
\frac w{\sqrt n}=\Theta(n^{1/4}),
\]

and the exponential tail is negligible. Therefore

\[
\Theta_n=O(n^{1/4}M_*).
\]

Since `M_*=Theta(2^n/sqrt(n))`, equations (0.1)--(0.2) follow.

## 7. Interpretation and next route

### Fact

The complete scalar tower is asymptotically separated from the Glynn scale by
an unbounded polynomial factor.

### What this closes

No larger exact dynamic program, additional derivative degree, or repeated
scalar block projection inside the same tower can establish
`ChowRank(perm_n)=2^(n-1)` for all large `n`.

### What remains open

The actual unrestricted Chow rank may still equal `2^(n-1)`. A successful
proof must use information absent from the scalar tower, for example:

- `S_n x S_n` representation type;
- multigraded relation modules;
- frame-sensitive overlap data;
- syzygies across several derivative degrees;
- valuative or ordinary-rank-specific obstructions; or
- a genuine cross-`n` recurrence.

The strongest objection is that a Chow-realizable intersection may be much
more rigid than an arbitrary Ferrers or cylinder extremizer. That objection is
correct. The theorem closes only the scalar route that deliberately forgets
this geometry.

## 8. Reproduction

Run

```bash
python scripts/general_scalar_tower_polynomial_ceiling.py \
  --json /tmp/general_scalar_tower_polynomial_ceiling.json
python scripts/general_scalar_tower_polynomial_ceiling_independent.py
python -m unittest tests.test_general_scalar_tower_polynomial_ceiling -v
```

Expected terminal markers:

```text
GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_AUDIT_PASS
GENERAL_SCALAR_TOWER_POLYNOMIAL_CEILING_INDEPENDENT_PASS
```
