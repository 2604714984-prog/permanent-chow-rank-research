# A central-binomial asymptotic ceiling for the two-direction maximal-ideal profile

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACE_REPLAYED`.

This note treats the first genuinely nonprincipal homogeneous ideal in the
two-direction apolar program:

\[
\mathfrak m=(s,t)\subset k[s,t].
\]

For a graded module `M`, the tested profile is

\[
\lambda_{\mathfrak m,d}(M;W)
=
\dim(WM_{d-1}).
\]

The main conclusion is

\[
\boxed{
R_n^{\mathfrak m}
\le
\left(1+O(n^{-1/2})\right)
\binom n{\lfloor n/2\rfloor},
}
\]

where `R_n^m` is the largest Chow-rank lower bound obtainable from this profile
over all output degrees and all differential two-planes.

Thus the two-linear-generator image profile remains a factor
`Omega(sqrt(n))` below the Glynn scale. This is a ceiling for one named
nonprincipal invariant, not an upper bound on actual Chow rank and not a
ceiling for arbitrary two-generator ideals of unequal or higher degrees.

## 1. Coupled-safe lower-bound interface

The parent theorem proves that if

\[
f=T_1+\cdots+T_r
\]

and `W` is a differential subspace of dimension at most two, then `A_f` is a
`k[W]`-subquotient of an intermediate module inside

\[
\bigoplus_iA_{T_i}.
\]

The image dimension

\[
\lambda_{\mathfrak m,d}(M;W)
=
\dim(WM_{d-1})
\tag{1.1}
\]

is additive on direct sums and nonincreasing under submodules and quotients.
Therefore

\[
\lambda_{\mathfrak m,d}(A_f;W)
\le
r\,\beta^{\mathfrak m}_{n,d},
\tag{1.2}
\]

where

\[
\beta^{\mathfrak m}_{n,d}
=
\max_{\dim U\le2}
\dim(U(B_n)_{d-1})
\tag{1.3}
\]

is the exact one-term Boolean envelope.

The proof below needs only an explicit lower bound for the maximum (1.3). A
larger true envelope only makes the resulting route ceiling stronger.

## 2. A split Boolean witness

Write

\[
B_n=k[z_1,\ldots,z_n]/(z_i^2)
\]

and partition the variables into sets of sizes

\[
a=\lfloor n/2\rfloor,
\qquad
b=\lceil n/2\rceil.
\]

Then

\[
B_n\cong B_a\otimes B_b.
\]

Choose

\[
s=z_1+\cdots+z_a,
\qquad
t=z_{a+1}+\cdots+z_n.
\tag{2.1}
\]

Both factors are Boolean complete intersections with strong Lefschetz
operators. Put

\[
C_m=B_m/L_mB_m,
\qquad
L_m=z_1+\cdots+z_m.
\]

If

\[
h_{m,j}=\binom mj,
\qquad h_{m,-1}=0,
\]

then maximal rank of multiplication by `L_m` gives

\[
\dim(C_m)_j
=
\left[
\binom mj-\binom m{j-1}
\right]_+.
\tag{2.2}
\]

The split choice (2.1) gives an exact tensor quotient

\[
B_n/(s,t)B_n
\cong
C_a\otimes C_b.
\tag{2.3}
\]

Define

\[
q_{n,d}
=
\sum_{i+j=d}
\left[
\binom ai-\binom a{i-1}
\right]_+
\left[
\binom bj-\binom b{j-1}
\right]_+.
\tag{2.4}
\]

Since the degree-`d` quotient has dimension `q_(n,d)`, the explicit two-plane
satisfies

\[
\dim\bigl((s,t)(B_n)_{d-1}\bigr)
=
\binom nd-q_{n,d}.
\tag{2.5}
\]

A one-dimensional strong-Lefschetz choice independently gives the legal lower
bound

\[
\beta^{\mathfrak m}_{n,d}
\ge
\min\left\{
\binom n{d-1},
\binom nd
\right\}.
\tag{2.6}
\]

Combining (2.5) and (2.6), put

\[
\underline\beta_{n,d}
=
\max\left\{
\min\left(\binom n{d-1},\binom nd\right),
\binom nd-q_{n,d}
\right\}.
\tag{2.7}
\]

Then

\[
\beta^{\mathfrak m}_{n,d}
\ge
\underline\beta_{n,d}.
\tag{2.8}
\]

## 3. Permanent numerator cap

The permanent apolar Hilbert function is

\[
\dim(A_{\operatorname{perm}_n})_j
=
\binom nj^2.
\]

For any differential two-plane `W`, the multiplication map

\[
W\otimes(A_{\operatorname{perm}_n})_{d-1}
\longrightarrow
(A_{\operatorname{perm}_n})_d
\]

therefore has rank at most

\[
N_{n,d}
=
\min\left\{
\binom nd^2,
2\binom n{d-1}^2
\right\}.
\tag{3.1}
\]

Equations (1.2), (2.8) and (3.1) imply the exact finite route ceiling

\[
\boxed{
R_{n,d}^{\mathfrak m}
\le
\left\lceil
\frac{N_{n,d}}{\underline\beta_{n,d}}
\right\rceil.
}
\tag{3.2}
\]

No maximal-rank assertion for the permanent is used.

## 4. Asymptotic ceiling

Let

\[
M_n=\binom n{\lfloor n/2\rfloor}.
\]

We consider three cases.

### 4.1 Nonincreasing side

If

\[
\binom n{d-1}\ge\binom nd,
\]

then (2.6) gives `beta>=binom(n,d)`, while the target cap gives

\[
N_{n,d}\le\binom nd^2.
\]

Hence

\[
R_{n,d}^{\mathfrak m}\le\binom nd\le M_n.
\tag{4.1}
\]

### 4.2 Increasing side away from the center

Assume

\[
\binom n{d-1}<\binom nd
\]

and

\[
\binom n{d-1}\le M_n/2.
\]

Using only the one-dimensional denominator in (2.6),

\[
R_{n,d}^{\mathfrak m}
\le
\left\lceil
\frac{2\binom n{d-1}^2}{\binom n{d-1}}
\right\rceil
\le
M_n.
\tag{4.2}
\]

### 4.3 Increasing central range

It remains to consider

\[
\binom n{d-1}>M_n/2.
\tag{4.3}
\]

The total dimension of `C_m` telescopes:

\[
\dim C_m
=
\binom m{\lfloor m/2\rfloor}.
\]

Therefore every coefficient in (2.4) satisfies

\[
q_{n,d}
\le
\binom a{\lfloor a/2\rfloor}
\binom b{\lfloor b/2\rfloor}
=
O\left(\frac{2^n}{n}\right).
\tag{4.4}
\]

Standard central-binomial estimates give

\[
M_n=\Theta\left(\frac{2^n}{\sqrt n}\right).
\tag{4.5}
\]

On the increasing side, (4.3) also gives

\[
\binom nd>M_n/2.
\]

Consequently

\[
\frac{q_{n,d}}{\binom nd}
=
O(n^{-1/2}).
\tag{4.6}
\]

The split denominator in (2.7) and the target numerator cap now give

\[
R_{n,d}^{\mathfrak m}
\le
\frac{\binom nd^2}{\binom nd-q_{n,d}}+1
\le
\left(1+O(n^{-1/2})\right)M_n.
\tag{4.7}
\]

Combining (4.1), (4.2) and (4.7) proves

\[
\boxed{
R_n^{\mathfrak m}
:=
\max_dR_{n,d}^{\mathfrak m}
\le
\left(1+O(n^{-1/2})\right)M_n.
}
\tag{4.8}
\]

Since Glynn has scale `2^(n-1)` and `M_n=Theta(2^n/sqrt(n))`, the maximal-ideal
profile remains a factor `Omega(sqrt(n))` below Glynn.

## 5. Exact finite diagnostic

Applying (3.2) to the frozen permanent Hilbert functions gives

```text
n=3:  route ceiling 3    existing unrestricted boundary 4
n=4:  route ceiling 7    existing unrestricted boundary 8
n=5:  route ceiling 10   existing unrestricted boundary 16
n=6:  route ceiling 20   existing unrestricted boundary 28
n=7:  route ceiling 35   existing unrestricted boundary 49
n=8:  route ceiling 75   existing unrestricted boundary 90
n=9:  route ceiling 126  existing unrestricted boundary 164
n=10: route ceiling 252  existing unrestricted boundary 307.
```

These are upper ceilings on what the profile could prove, not new lower bounds.
The numerator was allowed to attain its full source/target dimension cap, so
no unverified permanent rank computation enters the diagnostic.

An independent replay explicitly constructs the split Boolean multiplication
matrix

\[
(B_n)_{d-1}\oplus(B_n)_{d-1}
\xrightarrow{\ (s,t)\ }
(B_n)_d
\]

and verifies that its rank is exactly `binom(n,d)-q_(n,d)` through `n=8`.

## 6. Research decision

The current two-direction route classification is

```text
principal homogeneous ideals (g)        CLOSED at central binomial
maximal ideal (s,t)                      CLOSED asymptotically near central
powers (s,t)^p                           finite barrier through n=6
unequal-degree two-generator ideals      OPEN
higher staircase ideals                  OPEN
relation-sensitive monotone invariants   OPEN
```

The next ideal profile must use structure not already present in the first
linear image. The natural test objects are unequal-degree complete
intersections such as

\[
(s^a,t^b),
\qquad
(a,b)\ne(1,1),
\]

or genuinely asymmetric staircases. Any denominator must remain an envelope
for all Chow terms under the Boolean subquotient theorem.
