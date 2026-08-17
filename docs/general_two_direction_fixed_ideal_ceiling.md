# Fixed binary ideal profiles have a central-binomial asymptotic ceiling

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACE_REPLAYED`.

This note extends the principal and maximal-ideal results to every fixed
homogeneous `m`-primary ideal

\[
I\subset k[s,t],
\qquad
\mathfrak m=(s,t).
\]

Here **fixed** means that the ideal, its generator degrees and its number of
minimal generators do not depend on `n`.

Let `R_n^I` denote the largest Chow-rank lower bound obtainable from the
monotone image profiles

\[
M\longmapsto\dim((IM)_d)
\]

over all output degrees and all differential two-planes. The main theorem is

\[
\boxed{
R_n^I
\le
\left(1+O_I(n^{-1/2})\right)
\binom n{\lfloor n/2\rfloor}.
}
\]

Consequently every fixed staircase ideal and every fixed complete intersection
such as `(s^a,t^b)` remains a factor `Omega_I(sqrt(n))` below the Glynn scale.

This is a route ceiling for fixed `m`-primary ideals. It is not an upper bound
on actual Chow rank and does not cover ideals whose degrees or number of
generators grow with `n`, non-image relation invariants, representation-valued
modules, valuative methods or Chow-realizability defects.

## 1. Monotone ideal-image profile

Fix a differential two-plane

\[
W=\langle s,t\rangle\subseteq S_1.
\]

For a homogeneous ideal `I subset k[s,t]` and a graded `k[W]`-module `M`, put

\[
\lambda_{I,d}(M;W)
=
\dim((IM)_d).
\tag{1.1}
\]

The assignment (1.1) is additive on direct sums. If `N` is a submodule or
quotient of `M`, then `(IN)_d` is a subquotient of `(IM)_d`; hence

\[
\lambda_{I,d}(N;W)\le\lambda_{I,d}(M;W).
\tag{1.2}
\]

The apolar subquotient theorem therefore gives, for every decomposition

\[
\operatorname{perm}_n=T_1+\cdots+T_r,
\]

\[
\lambda_{I,d}(A_{\operatorname{perm}_n};W)
\le
r\,\beta^I_{n,d},
\tag{1.3}
\]

where

\[
\beta^I_{n,d}
=
\max_{\dim U\le2}
\dim((IB_n)_d)
\tag{1.4}
\]

is the Boolean one-term envelope.

## 2. Two lower bounds for the Boolean envelope

Choose homogeneous generators

\[
I=(g_1,\ldots,g_r),
\qquad
\deg g_i=p_i.
\tag{2.1}
\]

The number `r` and the degrees `p_i` are fixed.

### 2.1 Principal witnesses

For every nonzero `g_i`, choose a point

\[
[\alpha:\beta]\in\mathbf P^1
\]

with

\[
g_i(\alpha,\beta)\ne0.
\]

Map

\[
s\mapsto\alpha L,
\qquad
t\mapsto\beta L,
\]

where `L=z_1+...+z_n` is the Boolean strong-Lefschetz element. Then `g_i`
maps to a nonzero scalar multiple of `L^(p_i)`. Consequently

\[
\boxed{
\beta^I_{n,d}
\ge
\max_i
\min\left\{
\binom n{d-p_i},
\binom nd
\right\}.
}
\tag{2.2}
\]

The maximizing one-dimensional Boolean image may depend on `i`; this is legal
because (1.4) is a maximum.

### 2.2 Split quotient witness

Because `I` is `m`-primary, there exists a fixed integer `N` such that

\[
\mathfrak m^N\subseteq I.
\tag{2.3}
\]

In particular

\[
s^N,t^N\in I.
\]

Partition the Boolean variables into blocks of sizes

\[
a=\lfloor n/2\rfloor,
\qquad
b=\lceil n/2\rceil,
\]

and choose `s=L_a`, `t=L_b`, the sums of the variables in the two disjoint
blocks. Then

\[
B_n\cong B_a\otimes B_b
\]

and

\[
B_n/IB_n
\quad\text{is a quotient of}\quad
B_n/(s^N,t^N)B_n.
\tag{2.4}
\]

The latter quotient splits exactly:

\[
B_n/(s^N,t^N)B_n
\cong
(B_a/L_a^NB_a)\otimes(B_b/L_b^NB_b).
\tag{2.5}
\]

Strong Lefschetz gives

\[
\dim(B_m/L_m^NB_m)_j
=
\left[
\binom mj-\binom m{j-N}
\right]_+,
\tag{2.6}
\]

with the second binomial interpreted as zero outside its natural range.

Since the Boolean Hilbert function is symmetric and unimodal, summing the
positive differences in (2.6) leaves at most `N` boundary layers. Therefore

\[
\dim(B_m/L_m^NB_m)
\le
N\binom m{\lfloor m/2\rfloor}.
\tag{2.7}
\]

Combining (2.4)--(2.7), every graded quotient component satisfies

\[
\dim(B_n/IB_n)_d
\le
N^2
\binom a{\lfloor a/2\rfloor}
\binom b{\lfloor b/2\rfloor}
=
O_I\left(\frac{2^n}{n}\right).
\tag{2.8}
\]

Thus the split witness gives

\[
\boxed{
\beta^I_{n,d}
\ge
\binom nd-O_I(2^n/n).
}
\tag{2.9}
\]

whenever the right side is useful.

## 3. Permanent numerator cap

Write

\[
H_j=\binom nj,
\qquad
M_n=\binom n{\lfloor n/2\rfloor}.
\]

Since

\[
\dim(A_{\operatorname{perm}_n})_j=H_j^2,
\]

the generator presentation (2.1) gives the universal cap

\[
\boxed{
\lambda_{I,d}(A_{\operatorname{perm}_n};W)
\le
\min\left\{
H_d^2,
\sum_{i=1}^{r}H_{d-p_i}^2
\right\}.
}
\tag{3.1}
\]

This uses only target dimension and the sum of the generator source
dimensions. Relations among the generators can only lower the numerator.

## 4. Asymptotic ceiling

Let

\[
S_d=\max_iH_{d-p_i}.
\]

We split into three cases.

### 4.1 A principal witness is surjective

If `H_(d-p_i)>=H_d` for some `i`, equation (2.2) gives

\[
\beta^I_{n,d}\ge H_d.
\]

Together with the target cap in (3.1),

\[
R_{n,d}^I\le H_d\le M_n.
\tag{4.1}
\]

### 4.2 All sources are small

Assume every source is smaller than the target and

\[
S_d\le M_n/r.
\]

Equation (2.2) gives `beta>=S_d`, while (3.1) gives

\[
\lambda_{I,d}(A_{\operatorname{perm}_n};W)
\le rS_d^2.
\]

Hence

\[
R_{n,d}^I\le rS_d\le M_n.
\tag{4.2}
\]

### 4.3 Near-central range

The remaining case has

\[
H_d>S_d>M_n/r.
\tag{4.3}
\]

By standard central-binomial estimates,

\[
M_n=\Theta(2^n/\sqrt n).
\]

The split quotient loss in (2.8) is `O_I(2^n/n)`, so (4.3) implies

\[
\frac{\dim(B_n/IB_n)_d}{H_d}
=
O_I(n^{-1/2}).
\tag{4.4}
\]

Using the split denominator (2.9) and the target numerator cap,

\[
R_{n,d}^I
\le
\frac{H_d^2}{H_d-O_I(2^n/n)}+1
\le
\left(1+O_I(n^{-1/2})\right)M_n.
\tag{4.5}
\]

Equations (4.1), (4.2) and (4.5) prove

\[
\boxed{
R_n^I
:=
\max_dR_{n,d}^I
\le
\left(1+O_I(n^{-1/2})\right)M_n.
}
\tag{4.6}
\]

## 5. Consequences

### 5.1 Fixed complete intersections

For every fixed positive pair `(a,b)`,

\[
I=(s^a,t^b)
\]

is `m`-primary and satisfies the theorem. Therefore

\[
R_n^{(s^a,t^b)}
\le
\left(1+O_{a,b}(n^{-1/2})\right)M_n.
\]

Unequal generator degrees do not evade the asymptotic central-binomial
barrier when the degrees remain fixed.

### 5.2 Fixed staircase ideals

Every fixed monomial staircase ideal containing a power of `m` also satisfies
the theorem, regardless of the number or arrangement of its boundary
generators.

### 5.3 Remaining ideal frontier

To escape this theorem, an ideal family `I_n` must have complexity growing with
`n`: generator degrees, generator count, nilpotence threshold, or some
combination must diverge. Even then, an improved profile must retain a Boolean
envelope for all Chow terms and must beat the existing unrestricted small-`n`
regressions before promotion.

## 6. Exact finite replay

The replay verifies the strong-Lefschetz quotient formula

\[
\dim(B_m/L_m^NB_m)_j
=
[\binom mj-\binom m{j-N}]_+
\]

by explicit subset-inclusion matrices for

```text
2<=m<=8,
1<=N<=min(4,m),
0<=j<=m.
```

It also verifies the total-dimension bound

\[
\dim(B_m/L_m^NB_m)
\le
N\binom m{\lfloor m/2\rfloor}
\]

and its split tensor consequence through `n=20`.

These finite computations replay the explicit interfaces. The asymptotic route
ceiling is proved by the analytic inequalities above and is not inferred from
finite data.

## 7. Research decision

The two-direction image-profile frontier is now

```text
principal ideals                         CLOSED generally
fixed m-primary ideals                   CLOSED asymptotically
fixed complete intersections             CLOSED asymptotically
fixed staircase ideals                   CLOSED asymptotically
ideals with complexity growing with n    OPEN
relation-sensitive monotone invariants   OPEN
```

The next default direction is no longer another fixed binary ideal. It is
preferable to seek either:

1. a subquotient-monotone relation or Fitting invariant;
2. a representation-valued `S_n x S_n` module; or
3. an `n`-dependent ideal family with a proved Boolean envelope and a genuine
   unrestricted gain.
