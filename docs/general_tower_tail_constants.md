# Fixed-codimension tail constants for the permanent derivative tower

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAYED`.

This note analyzes the exact scalar derivative tower after the
shadow-complement reformulation. It proves:

1. saturation thresholds are nondecreasing in derivative degree;
2. the complete scalar-tower lower bound is always the top-degree threshold;
3. every fixed-codimension tail transition has a universal additive constant;
4. the final transition adds at most one term and is governed exactly by
   bipartite `K_(2,2)` supersaturation.

The result does **not** improve the numerical lower bounds already frozen in
PR #51. It identifies which part of the tower can and cannot affect the
general-`n` exponential rate.

No exact Chow rank for `n>=6`, border-rank result, linear-codimension
asymptotic, Chow-realizability defect, or general Glynn optimality is claimed.
Literature novelty has not been established.

## 1. Setup

Write

\[
E_d(n)=\mathcal D_d(\operatorname{perm}_n),
\qquad
M_{n,d}=\binom nd,
\qquad
A_{n,d}=M_{n,d}^2.
\]

For `q` degree-`n` Chow terms, the scalar derivative tower supplies capacities

\[
B_{n,d}(q)
\]

such that

\[
\dim\left(
E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i)
\right)
\le B_{n,d}(q).
\tag{1.1}
\]

Let

\[
F_{n,d}(b)
=
\min_{\substack{S\subseteq E_d(n)\\ \dim S=b}}
\dim\partial S
\tag{1.2}
\]

be the exact first product shadow and let

\[
\Gamma_{n,d}(C)
=
\max\{b:F_{n,d}(b)\le C\}.
\tag{1.3}
\]

The direct cap is

\[
C_{n,d}(q)
=
\min\left\{
A_{n,d},
qM_{n,d},
\Gamma_{n,d}(B_{n,d-1}(q))
\right\}.
\tag{1.4}
\]

The exact projection closure is the prefix envelope

\[
B_{n,d}(q)
=
qM_{n,d}
+
\min_{0\le t\le q}
\left(
C_{n,d}(t)-tM_{n,d}
\right).
\tag{1.5}
\]

Define

\[
D_{n,d}(q)=A_{n,d}-B_{n,d}(q)
\tag{1.6}
\]

and the saturation threshold

\[
Q_{n,d}
=
\min\{q:B_{n,d}(q)=A_{n,d}\}.
\tag{1.7}
\]

The shadow-complement theorem gives

\[
\Gamma_{n,d}(A_{n,d-1}-z)
=
A_{n,d}-F_{n,n-d+1}(z)
\tag{1.8}
\]

and therefore the exact deficit recurrence

\[
H_{n,d}(q)
=
\max\left\{
0,\,
A_{n,d}-qM_{n,d},\,
F_{n,n-d+1}(D_{n,d-1}(q))
\right\},
\tag{1.9}
\]

\[
D_{n,d}(q)
=
\max_{0\le t\le q}
\left(
H_{n,d}(t)-(q-t)M_{n,d}
\right).
\tag{1.10}
\]

## 2. Threshold monotonicity

### Proposition 2.1

For every `n` and `2<=d<=n-1`,

\[
\boxed{
Q_{n,d}\ge Q_{n,d-1}.
}
\tag{2.1}
\]

Consequently, if

\[
\Theta_n=\max_{1\le d\le n-1}Q_{n,d},
\]

then

\[
\boxed{
\Theta_n=Q_{n,n-1}.
}
\tag{2.2}
\]

### Proof

Fix `q<Q_(n,d-1)`. Then

\[
B_{n,d-1}(q)<A_{n,d-1}.
\]

The complete degree-`d` family has shadow exactly `A_(n,d-1)`, so

\[
\Gamma_{n,d}(C)<A_{n,d}
\qquad
(C<A_{n,d-1}).
\]

By the direct cap and the projection recurrence,

\[
B_{n,d}(q)
\le
\Gamma_{n,d}(B_{n,d-1}(q))
<
A_{n,d}.
\]

Thus degree `d` cannot saturate before degree `d-1`. Iterating proves (2.2).
∎

This removes the formal maximum over derivative degrees from the scalar-tower
rank bound: only the degree-`n-1` threshold is maximal.

## 3. One-term Lipschitz continuity

### Proposition 3.1

For every legal `n,d,q`,

\[
\boxed{
0
\le
B_{n,d}(q+1)-B_{n,d}(q)
\le
M_{n,d}.
}
\tag{3.1}
\]

Equivalently, if `q<=Q_(n,d)`,

\[
\boxed{
D_{n,d}(q)
\le
(Q_{n,d}-q)M_{n,d}.
}
\tag{3.2}
\]

### Proof

The direct cap `C_(n,d)(q)` is nondecreasing: the literal cap is
nondecreasing, the preceding tower row is nondecreasing, and `Gamma` is
nondecreasing.

Let

\[
P(q)
=
\min_{0\le t\le q}
\left(
C_{n,d}(t)-tM_{n,d}
\right).
\]

If `P(q+1)=P(q)`, equation (1.5) increases by exactly `M_(n,d)`. Otherwise

\[
B_{n,d}(q+1)=C_{n,d}(q+1)
\ge C_{n,d}(q)
\ge B_{n,d}(q).
\]

The projection recurrence with the retained block `q` also gives

\[
B_{n,d}(q+1)\le B_{n,d}(q)+M_{n,d}.
\]

This proves (3.1). Summing the one-step increases from `q` to the first
saturation point gives (3.2). ∎

## 4. A rectangular upper bound for product shadows

### Lemma 4.1

Let `2<=k<=n`, `k<=a<=n`, and

\[
0\le z\le \binom ak\binom nk.
\]

Then

\[
\boxed{
F_{n,k}(z)
\le
\binom a{k-1}\binom n{k-1}.
}
\tag{4.1}
\]

### Proof

Restrict the row-set coordinate to `k`-subsets of a fixed `a`-set and leave
the column-set coordinate unrestricted:

\[
\mathcal R
=
\binom{[a]}k\times\binom{[n]}k.
\]

It has size

\[
|\mathcal R|=\binom ak\binom nk
\]

and its simultaneous lower shadow is

\[
\binom{[a]}{k-1}\times\binom{[n]}{k-1},
\]

of size displayed in (4.1). Any `z`-subfamily of `mathcal R` has no larger
shadow. Since the exact subspace minimum equals the coordinate-family
minimum, (4.1) follows. ∎

The rectangle is only a universal construction. It is not claimed to classify
the minimizers of `F_(n,k)`.

## 5. Universal fixed-codimension tail constants

For `k>=2`, define

\[
\boxed{
c_k
=
\max_{a\ge k}
\left[
\binom a{k-1}
-
\binom{a-1}k
-
1
\right]_+.
}
\tag{5.1}
\]

The maximum is finite. Indeed, for `a>=3k`,

\[
\frac{\binom{a-1}k}{\binom a{k-1}}
=
\frac{(a-k)(a-k+1)}{ak}
\ge1.
\tag{5.2}
\]

Hence it is enough to check `k<=a<3k`.

### Theorem 5.1 -- fixed-codimension increment bound

For every `k>=2` and `n>=2k`,

\[
\boxed{
0
\le
Q_{n,n-k+1}-Q_{n,n-k}
\le
c_k.
}
\tag{5.3}
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

Because saturation cannot occur before the literal cap saturates,

\[
Q\ge M_0.
\]

The condition `n>=2k` gives `M_0>=M_1`, hence `Q>=M_1`.

We prove that the next row has saturated by

\[
q=Q+c_k.
\]

Use the deficit recurrence (1.10). For `t>=Q`, the preceding row has zero
deficit, and all three entries in (1.9) vanish because `t>=Q>=M_1`.

Now let `t<Q` and write

\[
r=Q-t\ge1.
\]

The literal deficit is at most

\[
A_{n,n-k+1}-tM_1
=
(M_1-t)M_1
\le rM_1.
\tag{5.4}
\]

By Proposition 3.1,

\[
D_{n,n-k}(t)\le rM_0.
\tag{5.5}
\]

If `r>=M_1`, the ambient bound gives

\[
F_{n,k}(D_{n,n-k}(t))
\le M_1^2
\le rM_1.
\tag{5.6}
\]

Assume instead `1<=r<M_1`. Choose the least `a>=k` with

\[
\binom ak\ge r.
\]

Such an `a<=n` exists because `M_0>=M_1>r`. Minimality gives

\[
r\ge\binom{a-1}k+1.
\tag{5.7}
\]

Equations (5.5), Lemma 4.1 and (5.7) yield

\[
\begin{aligned}
F_{n,k}(D_{n,n-k}(t))
&\le
\binom a{k-1}M_1\\
&\le
(r+c_k)M_1.
\end{aligned}
\tag{5.8}
\]

Combining (5.4), (5.6) and (5.8),

\[
H_{n,n-k+1}(t)
\le
(r+c_k)M_1
=
(q-t)M_1.
\]

Every term in the maximum (1.10) is therefore nonpositive, so

\[
D_{n,n-k+1}(Q+c_k)=0.
\]

The lower inequality in (5.3) is Proposition 2.1. ∎

The first constants are

\[
\boxed{
c_2=1,\;
c_3=5,\;
c_4=20,\;
c_5=83,\;
c_6=362,\;
c_7=1572,\;
c_8=7513.
}
\tag{5.9}
\]

### Corollary 5.2 -- fixed tail

For every `K>=2` and `n>=2K`,

\[
\boxed{
0
\le
\Theta_n-Q_{n,n-K}
\le
\sum_{k=2}^{K}c_k.
}
\tag{5.10}
\]

### Proof

Use Proposition 2.1, equation (2.2), and sum Theorem 5.1 for
`k=K,K-1,...,2`. ∎

Thus a fixed number of top derivative degrees changes the scalar lower bound
by only a fixed additive constant, independent of `n`.

## 6. Growth of the tail constants

Let

\[
\varphi=\frac{1+\sqrt5}{2},
\qquad
\beta=\varphi^{\varphi+2}=5.7032759559\ldots.
\]

### Proposition 6.1

\[
\boxed{
\lim_{k\to\infty}c_k^{1/k}
=
\beta.
}
\tag{6.1}
\]

### Proof

If the summand in (5.1) is positive, then

\[
\binom a{k-1}>\binom{a-1}k,
\]

equivalently,

\[
(a-k)(a-k+1)<ak.
\tag{6.2}
\]

Writing `a=lambda k`, equation (6.2) implies

\[
\lambda\le\varphi^2+O(k^{-1}).
\]

Stirling's formula gives, uniformly on compact positive `lambda`-intervals,

\[
\frac1k\log\binom{\lambda k}{k-1}
=
h(\lambda)+o(1),
\]

where

\[
h(\lambda)
=
\lambda\log\lambda
-
(\lambda-1)\log(\lambda-1).
\]

The function `h` is increasing for `lambda>1`, so the positive range gives

\[
\limsup_{k\to\infty}\frac1k\log c_k
\le
h(\varphi^2).
\tag{6.3}
\]

For the reverse inequality, choose

\[
a_k
=
\left\lfloor
(\varphi^2-k^{-1/2})k
\right\rfloor.
\]

The factor

\[
1-
\frac{(a_k-k)(a_k-k+1)}{a_kk}
\]

is positive and of polynomial order `k^(-1/2)`. Therefore the binomial
difference in (5.1) has the same exponential rate as
`binom(a_k,k-1)`, giving

\[
\liminf_{k\to\infty}\frac1k\log c_k
\ge
h(\varphi^2).
\tag{6.4}
\]

Finally,

\[
h(\varphi^2)
=
(\varphi+2)\log\varphi,
\]

which is equivalent to (6.1). ∎

Consequently,

\[
\sum_{k=2}^{K}c_k
=
\exp\left((\log\beta+o(1))K\right).
\tag{6.5}
\]

If `K=o(n)`, the top `K` derivative degrees contribute only
`exp(o(n))` additively. They cannot create a new positive exponential rate
that was absent at degree `n-K`.

This does not analyze the linear-codimension regime `K=Theta(n)`, where the
main scalar-tower asymptotic remains open.

## 7. The final row and bipartite four-cycles

Taking `k=2` in Theorem 5.1 gives `c_2=1`.

### Corollary 7.1 -- top-row gap

For every `n>=4`,

\[
\boxed{
Q_{n,n-2}
\le
Q_{n,n-1}
\le
Q_{n,n-2}+1.
}
\tag{7.1}
\]

The statement also holds directly for `n=3`.

The final scalar-tower row can therefore add only zero or one term.

### Proposition 7.2 -- exact `C4` interpretation

For every `0<=z<=binom(n,2)^2`,

\[
\boxed{
F_{n,2}(z)
=
\min\left\{
|E(G)|:
G\subseteq K_{n,n}
\text{ contains at least }z\text{ copies of }K_{2,2}
\right\}.
}
\tag{7.2}
\]

### Proof

An element of

\[
\binom{[n]}2\times\binom{[n]}2
\]

is a bipartite `K_(2,2)`. Its lower shadow consists of its four edges.

Given a family of `z` such rectangles, the union of its lower shadow is a
bipartite graph containing those `z` distinct four-cycles. Conversely, from a
graph containing at least `z` four-cycles, choose any `z` of them; their lower
shadow is contained in the graph. Taking minima in both directions proves
(7.2). ∎

Let

\[
Q=Q_{n,n-2}.
\]

The exact top threshold is

\[
\boxed{
Q_{n,n-1}
=
\max_{0\le t\le Q}
\left[
t+
\left\lceil
\frac{F_{n,2}(D_{n,n-2}(t))}{n}
\right\rceil
\right].
}
\tag{7.3}
\]

Indeed, the literal deficit contributes only the already dominated threshold
`n<=Q`, and equation (1.10) gives (7.3).

Combining (7.1)--(7.3), the top gap equals one exactly when there is some
`t<Q` such that

\[
F_{n,2}(D_{n,n-2}(t))
>
(Q-t)n.
\tag{7.4}
\]

Thus the last scalar-tower decision is an exact finite bipartite
four-cycle-supersaturation problem.

## 8. Exact replay

The primary implementation reuses only the exact budget-maximizing shadow DP
from PR #52. It verifies:

```text
capacity one-term Lipschitz checks       1,151
threshold monotonicity checks               21
rectangular-shadow checks                32,373
tail-transport checks                       430
tail-threshold checks                          9
```

A second implementation imports none of the primary or historical tower code.
It computes every exact `F_(n,d)(b)` by a family-size-indexed Ferrers DP,
inverts it, and rebuilds the tower through `n=8`.

For the `C4` interpretation, both implementations enumerate all

```text
2^9 + 2^16 = 66,048
```

bipartite graphs of sizes `3 x 3` and `4 x 4`. The resulting minimum-edge
profiles agree exactly with `F_(3,2)` and `F_(4,2)`.

The replay reproduces the existing PR #51 rows through `n=10`, including:

```text
n=7:  7,22,39,46,48,49
n=8:  8,29,59,80,87,89,90
n=9:  9,37,87,136,155,161,163,164
n=10: 10,46,123,219,280,299,305,307,307.
```

The top gaps are one for `3<=n<=9` and zero for `n=10`. These finite values are
checks of the theorem, not evidence of an eventual pattern.

## 9. Research consequence

The full scalar tower maximum is no longer an unknown maximum over degrees:

\[
\Theta_n=Q_{n,n-1}.
\]

However, the top fixed-codimension tail is asymptotically unable to create a
new exponential rate. The unresolved part of the scalar method is therefore
the linear-codimension regime

\[
d=(1-\alpha)n,
\qquad
0<\alpha<\frac12,
\]

not the last finitely many derivative degrees.

The next primary problem is to derive the entropy-rate transform of
`F_(n,alpha n)` and insert it into the deficit recurrence. If that transform
has a central-binomial ceiling, the scalar route should be closed explicitly
and research should move to a representation-valued or Chow-realizability
defect. If it has a strict gain, the degree interval producing the gain is now
localized away from the fixed-codimension tail.
