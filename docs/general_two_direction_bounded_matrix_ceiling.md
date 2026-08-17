# Bounded-size homogeneous matrix images cannot reach the Glynn scale

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

This note strengthens the `2 x 2` linear-pencil analysis.  Let

\[
R=k[s,t]
\]

and let

\[
\Phi(s,t)
\in
\operatorname{Mat}_{p\times q}(R_\delta)
\]

be a nonzero matrix whose entries are homogeneous binary forms of one common
degree `delta`.  For a graded `R`-module `M`, define

\[
\rho_{\Phi,d}(M)
=
\dim\operatorname{im}
\left(
\Phi_M:M_{d-\delta}^{\oplus q}
\longrightarrow
M_d^{\oplus p}
\right).
\tag{0.1}
\]

Write

\[
r=\operatorname{rank}_{k(s,t)}\Phi
\]

for the normal rank.  The main theorem is the explicit route ceiling

\[
\boxed{
R_{\Phi,n,d}
\le
\left\lceil
\frac{
\min\left\{
q\binom n{d-\delta}^2,
\ p\binom nd^2
\right\}
{
r\min\left\{
\binom n{d-\delta},
\binom nd
\right\}}
\right\rceil.
}
\tag{0.2}
\]

In particular,

\[
\boxed{
R_{\Phi,n,d}
\le
\frac{\max\{p,q\}}r
\binom n{\lfloor n/2\rfloor}+1.
}
\tag{0.3}
\]

For every fixed matrix size, this is central-binomial scale.  More uniformly,
if `p,q<=K_n`, then every such matrix-image lower bound is at most

\[
K_n\binom n{\lfloor n/2\rfloor}+1.
\tag{0.4}
\]

Consequently a linear or uniform-degree homogeneous matrix-image method with

\[
K_n=o(\sqrt n)
\]

cannot prove a lower bound of Glynn scale `2^(n-1)`.  Any successful method of
this exact type must have matrix size at least `Omega(sqrt(n))`.

This is a ceiling on a named image-rank mechanism, not an upper bound on actual
Chow rank.  It does not cover matrices with nonuniform degree shifts,
collections of Fitting minors treated jointly, higher syzygy modules,
representation-valued data, valuative arguments or Chow-realizability defects.

## 1. Subquotient-monotone interface

The parent theorem proves that the image dimension of every homogeneous
polynomial matrix is additive on direct sums and nonincreasing under both
submodules and quotients.  If

\[
\operatorname{perm}_n=T_1+\cdots+T_m,
\]

then the apolar subquotient theorem gives

\[
\rho_{\Phi,d}(A_{\operatorname{perm}_n};W)
\le
m\,\beta_{\Phi,n,d},
\tag{1.1}
\]

where `beta` is the maximum Boolean image rank over all linear maps from the
selected differential two-plane into `(B_n)_1`.

The maximum includes maps of rank one.  This apparently degenerate part of the
term envelope is the decisive universal witness below.

## 2. A normal-rank evaluation

Because the normal rank is `r`, at least one `r x r` minor

\[
\Delta(s,t)
\]

is a nonzero homogeneous binary form.  Over an infinite field there is a point

\[
[\alpha:\beta]\in\mathbf P^1
\]

such that

\[
\Delta(\alpha,\beta)\ne0.
\]

Therefore the constant matrix

\[
C=\Phi(\alpha,\beta)
\]

has rank exactly `r`.

In the Boolean envelope choose

\[
s\mapsto\alpha L,
\qquad
t\mapsto\beta L,
\qquad
L=z_1+\cdots+z_n.
\tag{2.1}
\]

Homogeneity of every entry gives

\[
\Phi(\alpha L,\beta L)
=
L^\delta C.
\tag{2.2}
\]

Thus the induced Boolean matrix is the tensor product of the constant map `C`
and multiplication by `L^delta`.

## 3. Boolean denominator

The squarefree Boolean complete intersection is strong Lefschetz in
characteristic zero.  Hence

\[
\operatorname{rank}
\left(
L^\delta:(B_n)_{d-\delta}\longrightarrow(B_n)_d
\right)
=
\min\left\{
\binom n{d-\delta},
\binom nd
\right\}.
\tag{3.1}
\]

Tensor-product rank in (2.2) gives the universal term-envelope lower bound

\[
\boxed{
\beta_{\Phi,n,d}
\ge
r\min\left\{
\binom n{d-\delta},
\binom nd
\right\}.
}
\tag{3.2}
\]

No assertion is made that every Chow term realizes this line specialization.
Only one Boolean witness is needed to lower-bound the maximum envelope that
must control all terms.

## 4. Permanent numerator

The permanent apolar Hilbert function is

\[
\dim(A_{\operatorname{perm}_n})_j
=
\binom nj^2.
\tag{4.1}
\]

The matrix image is bounded by both its source and target dimensions:

\[
\boxed{
\rho_{\Phi,d}(A_{\operatorname{perm}_n};W)
\le
\min\left\{
q\binom n{d-\delta}^2,
\ p\binom nd^2
\right\}.
}
\tag{4.2}
\]

Combining (1.1), (3.2) and (4.2) proves (0.2).

If

\[
\binom n{d-\delta}
\le
\binom nd,
\]

then the right side of (0.2) is at most

\[
\frac qr\binom n{d-\delta}+1.
\]

In the opposite inequality it is at most

\[
\frac pr\binom nd+1.
\]

Both binomial coefficients are bounded by the central one, proving (0.3).

## 5. Uniform bounded-size theorem

Fix an integer `K`.  For every nonzero homogeneous matrix with

\[
p,q\le K
\]

and every normal rank `r>=1`, equation (0.3) gives

\[
R_{\Phi,n,d}
\le
K\binom n{\lfloor n/2\rfloor}+1.
\tag{5.1}
\]

This holds uniformly even when the matrix coefficients and the common degree
`delta` depend on `n`.

Since

\[
\binom n{\lfloor n/2\rfloor}
=
\left(1+o(1)\right)
2^n\sqrt{\frac2{\pi n}},
\]

a route capable of reaching `2^(n-1)` must satisfy

\[
\frac{\max\{p,q\}}r
\ge
\left(1+o(1)\right)
\sqrt{\frac{\pi n}{8}}.
\tag{5.2}
\]

In particular, regardless of normal rank,

\[
\boxed{
\max\{p,q\}=\Omega(\sqrt n)
}
\tag{5.3}
\]

is a necessary complexity condition for this matrix-image mechanism to reach
Glynn scale.

Equation (5.3) is not a lower bound on the matrix size required by every
possible proof of Glynn optimality.  It applies only to lower bounds obtained
from one homogeneous matrix-image rank through the Boolean term envelope.

## 6. Relation to the `2 x 2` classification

For `p=q=2`, the general bound gives at most twice the central binomial
coefficient.  The finer classification on the companion note improves this:

- regular and principal pencils are capped exactly by an adjacent binomial
  coefficient;
- the two singular minimal-index blocks reduce to the maximal-ideal profile;
- the resulting complete `2 x 2` ceiling is
  `(1+O(n^(-1/2)))` times the central binomial coefficient.

The present theorem is weaker numerically for `2 x 2`, but stronger
structurally: it closes every bounded-size linear pencil and every
bounded-size common-degree homogeneous matrix without Kronecker
classification.

## 7. Exact finite replay

The primary replay checks, for

```text
2<=n<=9,
1<=delta<=min(4,n),
1<=p,q<=4,
1<=r<=min(p,q),
delta<=d<=n,
```

that the explicit source/target ratio in (0.2) never exceeds the bound in
(0.3).

It also constructs constant rank-`r` matrices tensored with the Boolean
subset-inclusion matrix for `L^delta` and verifies the exact denominator rank
modulo `1,000,003`.

A second implementation uses a disjoint range, a second prime and a transpose
orientation for the subset-inclusion matrices.

The finite computations replay the explicit algebraic interface.  The general
theorem is the normal-rank evaluation plus characteristic-zero strong
Lefschetz, not a finite extrapolation.

## 8. Research decision

The matrix-image frontier becomes

```text
fixed 2 x 2 linear pencils               CLOSED sharply
all bounded-size linear pencils           CLOSED at central scale
all bounded-size uniform-degree matrices  CLOSED at central scale
sub-sqrt(n) matrix size                    CLOSED for Glynn scale
sqrt(n)-or-larger matrix families          OPEN
nonuniform degree-shifted matrices         OPEN
joint Fitting/minor profiles               OPEN
higher syzygy and representation modules  OPEN
```

The next relation-sensitive route should not add another fixed-size matrix.
It must either:

1. use a matrix family of dimension at least order `sqrt(n)`;
2. retain nonuniform graded shifts or joint Fitting data; or
3. move directly to representation-valued higher syzygies.
