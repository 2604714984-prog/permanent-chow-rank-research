# Quantitative private-polar shadow amplification

## Status and boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_CHOW_REALIZABILITY_THEOREM`,
`EXACT_INTEGER_INTERFACE_REPLAYED`.

The private-polar theorem gives more than the existence of one descending
direction. In the shifted range

\[
\delta:=m^2-(q-1)n>0
\]

the total dimension of the private polar spaces is forced to be large. When
this dimension is fed into the already proved exact iterated product-shadow
theorem, the support restriction used in the parent PR can be substantially
relaxed.

The cleanest new consequence is:

\[
\boxed{
m\ge4,\quad m\le n\le m^2-m-1
\Longrightarrow
\mathcal D_m(\operatorname{perm}_n)
\cap
\bigl(\mathcal D_m(T)+\mathcal D_m(U)\bigr)=0
}
\]

for arbitrary degree-`n` Chow terms `T,U`.

Thus the two-term zero range moves from `n<(m-1)^2` to

\[
n\le m^2-m-1.
\]

The next pair boundary is the sharp exact-shadow equality

\[
n=m^2-m.
\]

No exact Chow rank or border-rank statement is made.

## 1. Quantitative private-polar dimension

Keep the notation of the private-polar theorem. For a selected element

\[
0\ne f=f_1+\cdots+f_q
\in
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i),
\]

let

\[
M_i=\partial^{m-1}f_i,\qquad r_i=\dim M_i,
\]

\[
M=\sum_iM_i,\qquad D=\sum_i r_i,\qquad k=D-\dim M.
\]

Put

\[
W_i=\sum_{j\ne i}M_j,\qquad t_i=\dim(M_i\cap W_i).
\]

The inherited private-polar lemma gives spaces

\[
S_i\subseteq
\mathcal D_{m-1}(\operatorname{perm}_n)
\cap
\operatorname{Sym}^{m-1}M_i
\]

with

\[
\dim S_i=r_i-t_i
\]

and

\[
t_i\le k.
\]

Assume `qn>m^2` and set

\[
s=qn-m^2.
\]

Then `k<=s`.

### Proposition 1.1 -- quantitative private mass

Define

\[
\delta=m^2-(q-1)n.
\]

If `delta>0`, then

\[
\boxed{
\sum_{i=1}^q\dim S_i\ge q\delta.
}
\tag{1.1}
\]

Consequently some label satisfies

\[
\boxed{\dim S_i\ge\delta.}
\tag{1.2}
\]

### Proof

Using `t_i<=k`,

\[
\begin{aligned}
\sum_i\dim S_i
&=\sum_i(r_i-t_i)\\
&\ge D-qk\\
&=\dim M-(q-1)k\\
&\ge m^2-(q-1)s.
\end{aligned}
\]

Since `s=qn-m^2`,

\[
m^2-(q-1)s
=q\bigl(m^2-(q-1)n\bigr)
=q\delta.
\]

This proves (1.1), and averaging proves (1.2). QED.

The parent PR used only the consequence `delta>=1 => some S_i!=0`. The
present note keeps the full dimension.

## 2. Exact private-shadow criterion

Let `r=m-1`. For a `b`-plane

\[
S\subseteq\mathcal D_r(\operatorname{perm}_n),
\]

write

\[
F^{(r-1)}_{n,r}(b)
\]

for the exact minimum dimension of the order-`r-1` derivative space of `S`.
This is the linear-output instance of the established exact iterated
product-shadow theorem.

### Theorem 2.1 -- quantitative private-shadow exclusion

Assume

\[
m\ge4,\quad q\ge2,\quad n\ge m,\quad qn>m^2,
\]

and

\[
\delta=m^2-(q-1)n>0.
\]

If

\[
\boxed{F^{(m-2)}_{n,m-1}(\delta)>n,}
\tag{2.1}
\]

then

\[
\boxed{
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i)=0.
}
\tag{2.2}
\]

### Proof

Assume a nonzero intersection element exists. Proposition 1.1 gives a label
with `dim S_i>=delta`. Choose a `delta`-plane `S` inside `S_i`. Since

\[
S\subseteq\operatorname{Sym}^{m-1}M_i,
\]

all order-`m-2` derivatives of `S` are linear forms in `M_i`. Hence

\[
\dim\partial^{m-2}S\le\dim M_i\le n.
\]

The exact iterated product-shadow theorem gives

\[
\dim\partial^{m-2}S
\ge
F^{(m-2)}_{n,m-1}(\delta),
\]

contradicting (2.1). QED.

## 3. The first exact linear-shadow tiers

Put `r=m-1`. The exact Ferrers formula for the order-`r-1` product shadow
uses the colex `r`-subset profile `k(t)` and first-container weights `w_i`.
For the first colex rows one has

```text
w_0=r,
w_1=1,
w_2=...=w_r=0,
w_(r+1)=1,
```

while

```text
k(1)=r,
k(t)>=r+1 for t>=2,
k(r+2)=r+2.
```

### Proposition 3.1 -- exact initial tiers

\[
\boxed{F^{(r-1)}_{n,r}(1)=r^2.}
\tag{3.1}
\]

For `2<=b<=r+1`,

\[
\boxed{F^{(r-1)}_{n,r}(b)=r(r+1).}
\tag{3.2}
\]

At the next size,

\[
\boxed{F^{(r-1)}_{n,r}(r+2)=r(r+2).}
\tag{3.3}
\]

Hence by monotonicity,

\[
b\ge r+2
\Longrightarrow
F^{(r-1)}_{n,r}(b)\ge r(r+2).
\tag{3.4}
\]

### Proof

For `b=1`, the only Ferrers partition is `(1)` and the objective is
`w_0 k(1)=r^2`.

For `2<=b<=r+1`, the all-ones partition has objective

\[
(w_0+w_1)k(1)=(r+1)r.
\]

Any partition with first part at least two contributes at least

\[
w_0 k(2)\ge r(r+1)
\]

before the remaining nonnegative terms are added.

For `b=r+2`, the all-ones partition sees `w_(r+1)=1` and has objective
`r(r+2)`. For any other partition, either the second part is positive, giving
at least `r(r+1)+r`, or the first part is `r+2`, giving
`r k(r+2)=r(r+2)`. QED.

## 4. Consequences for arbitrary q

### Corollary 4.1 -- the q>=3 shifted strict region

Assume

\[
m\ge4,\qquad q\ge3,\qquad (q-1)n<m^2.
\]

Then

\[
\boxed{
\mathcal D_m(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_m(T_i)=0.
}
\tag{4.1}
\]

If `qn<=m^2`, use the parent endpoint theorem. Otherwise
`delta=m^2-(q-1)n>=1`.

- If `delta=1`, then `n<=(m^2-1)/2<(m-1)^2`, so `F(1)>n`.
- If `2<=delta<=m`, then `F(delta)=m(m-1)` and
  `n<=(m^2-2)/2<m(m-1)`.
- If `delta>=m+1`, then `F(delta)>=m^2-1>n`.

Theorem 2.1 applies in every case.

## 5. The improved pair theorem

For `q=2`,

\[
\delta=m^2-n.
\]

### Theorem 5.1 -- pair zero range

For

\[
\boxed{m\ge4,\qquad m\le n\le m^2-m-1,}
\tag{5.1}
\]

and arbitrary degree-`n` Chow terms `T,U`,

\[
\boxed{
\mathcal D_m(\operatorname{perm}_n)
\cap
\bigl(\mathcal D_m(T)+\mathcal D_m(U)\bigr)=0.
}
\tag{5.2}
\]

Indeed, `delta=m^2-n>=m+1=r+2`, so

\[
F^{(m-2)}_{n,m-1}(\delta)\ge r(r+2)=m^2-1>n.
\]

Examples are

```text
m=4:  4 <= n <= 11
m=5:  5 <= n <= 19
m=6:  6 <= n <= 29
m=8:  8 <= n <= 55
m=10: 10 <= n <= 89.
```

## 6. Exact stopping point

At

\[
n=m^2-m,
\]

one has `delta=m=r+1`, and Proposition 3.1 gives the exact equality

\[
F^{(m-2)}_{n,m-1}(m)=m(m-1)=n.
\]

Thus the dimension contradiction becomes non-strict for a genuine structural
reason. Any continuation at this pair boundary must classify equality in the
`m`-dimensional private-polar shadow problem rather than merely improve an
integer estimate.

The remaining main interfaces are

```text
q=2, n=m^2-m and above,
shifted equality (q-1)n=m^2 not covered by the simplex theorem,
(q-1)n>m^2,
cubic exceptional rows.
```

The next preferred target is `q=2, n=m^2-m` because all current inequalities
are exact and the product-shadow minimizers have rigid first-tier structure.
