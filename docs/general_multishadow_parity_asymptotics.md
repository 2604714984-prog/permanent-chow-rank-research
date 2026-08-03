# Parity-sensitive asymptotics for the general multishadow bound

## Status

`PROOF_DRAFT_COMPLETE` — the asymptotic expansions and one-variable optimizations below have been checked symbolically. External peer review and a complete literature novelty review have not been performed.

## 1. Purpose

The even-degree multidimensional-shadow note proves an additive improvement of order

\[
\frac{1}{2e\log2}
\frac{\binom{2k}{k}}{k}
\]

over the optimized first-Koszul bound. The asymmetric theorem applies to odd degree as well. This note computes the odd constant and shows that it is twice the even constant when expressed on the natural central-binomial scale.

Let

\[
L_K(n)
\]

denote the optimized first-Koszul lower bound and let

\[
L_{\mathrm{MS}}(n)
\]

denote the best lower bound supplied by the general one-step multidimensional-shadow theorem.

## 2. Even degree

For

\[
n=2k,
\qquad
m=r=k,
\qquad
x=2k-c,
\]

with fixed `c>1/2`, the existing calculation gives

\[
L_{\mathrm{MS}}(2k)-L_K(2k)
\ge
4^{-c}(2c-1)
\frac{\binom{2k}{k}}{k}
+
O\left(
\frac{\binom{2k}{k}}{k^2}
\right).
\tag{2.1}
\]

The coefficient

\[
f_{\mathrm{even}}(c)=(2c-1)4^{-c}
\]

has a unique maximum at

\[
c_{\mathrm{even}}
=
\frac{1+1/\log2}{2},
\]

where

\[
f_{\mathrm{even}}(c_{\mathrm{even}})
=
\frac{1}{2e\log2}.
\]

Therefore

\[
L_{\mathrm{MS}}(2k)
\ge
L_K(2k)
+
\left(
\frac{1}{2e\log2}+o(1)
\right)
\frac{\binom{2k}{k}}{k}.
\tag{2.2}
\]

The proof is recorded in `docs/even_n_multidimensional_shadow_bound.md`.

## 3. Odd degree

Now let

\[
n=2k+1,
\qquad
m=k,
\qquad
r=k+1,
\]

and take

\[
x=2k+1-c
\]

for a fixed real `c>0`.

Write

\[
C_k=\binom{2k+1}{k}
=
\binom{2k+1}{k+1}.
\]

At output degree `m=k`, the local first-Koszul data simplify exactly:

\[
A_{2k+1,k}
=
\left((2k+1)^2-1\right)C_k^2,
\]

\[
B_{2k+1,k}
=
\left((2k+1)^2-1\right)C_k.
\tag{3.1}
\]

Hence the local rank ratio is exactly `C_k`.

Define

\[
R_k(c)
=
\frac{\binom{2k+1-c}{k}}{\binom{2k+1}{k}},
\qquad
R_{k+1}(c)
=
\frac{\binom{2k+1-c}{k+1}}{\binom{2k+1}{k+1}}.
\]

The two ratios satisfy the exact identity

\[
R_{k+1}(c)
=
R_k(c)
\left(1-\frac{c}{k+1}\right).
\tag{3.2}
\]

The multishadow theorem fixes

\[
q_k
=
\left\lfloor C_kR_k(c)^2\right\rfloor
\]

terms and uses the intersection cap

\[
s_k
=
\left\lfloor C_k^2R_{k+1}(c)^2\right\rfloor.
\]

Using (3.1), the resulting lower bound is

\[
q_k
+
\left\lceil
C_k
-
\frac{(2k+1)^2}{(2k+1)^2-1}
\frac{s_k}{C_k}
\right\rceil.
\tag{3.3}
\]

Floors and ceilings contribute `O(1)`. Standard gamma-ratio asymptotics give

\[
R_k(c)=2^{-c}\left(1+O(k^{-1})\right).
\tag{3.4}
\]

Moreover,

\[
\frac{(2k+1)^2}{(2k+1)^2-1}
=1+O(k^{-2}).
\]

Substituting (3.2)--(3.4) into (3.3) yields

\[
\begin{aligned}
L_{\mathrm{MS}}(2k+1)
&\ge
C_k
+
C_kR_k(c)^2
\left[
1-
\left(1+O(k^{-2})\right)
\left(1-\frac{c}{k+1}\right)^2
\right]
+O(1)\\
&=
C_k
+
2c4^{-c}
\frac{C_k}{k}
+
O\left(\frac{C_k}{k^2}\right).
\end{aligned}
\tag{3.5}
\]

The optimized first-Koszul bound satisfies

\[
L_K(2k+1)
=
C_k+O\left(\frac{C_k}{k^3}ight)+O(1),
\]

by the closed central-ratio formula. Therefore (3.5) remains unchanged at its leading additive order when measured relative to `L_K(2k+1)`:

\[
L_{\mathrm{MS}}(2k+1)-L_K(2k+1)
\ge
2c4^{-c}
\frac{C_k}{k}
+
O\left(\frac{C_k}{k^2}ight).
\tag{3.6}
\]

## 4. Optimization in odd degree

Set

\[
f_{\mathrm{odd}}(c)=2c4^{-c}.
\]

Then

\[
f_{\mathrm{odd}}'(c)
=
2\,4^{-c}\left(1-c\log4\right).
\]

Thus the unique maximum occurs at

\[
c_{\mathrm{odd}}
=
\frac{1}{\log4}
=
\frac{1}{2\log2}.
\]

At this point,

\[
4^{-c_{\mathrm{odd}}}=e^{-1},
\]

so

\[
f_{\mathrm{odd}}(c_{\mathrm{odd}})
=
\frac{1}{e\log2}.
\]

### Theorem 4.1 — odd-degree asymptotic gain

As `k` tends to infinity,

\[
\boxed{
L_{\mathrm{MS}}(2k+1)
\ge
L_K(2k+1)
+
\left(
\frac{1}{e\log2}+o(1)
\right)
\frac{\binom{2k+1}{k}}{k}.
}
\tag{4.1}
\]

Equivalently, with `n=2k+1`,

\[
\boxed{
L_{\mathrm{MS}}(n)
\ge
L_K(n)
+
\left(
\frac{2}{e\log2}+o(1)
\right)
\frac{\binom{n}{\lfloor n/2\rfloor}}{n}.
}
\tag{4.2}
\]

## 5. Unified parity statement

Combining (2.2) and (4.1) gives:

### Theorem 5.1

For the one-step multidimensional-shadow lower bound,

\[
L_{\mathrm{MS}}(n)-L_K(n)
=
\Omega\left(
\frac{2^n}{n^{3/2}}
\right).
\]

More precisely,

\[
L_{\mathrm{MS}}(n)
\ge
L_K(n)
+
\left(
\frac{1}{e\log2}+o(1)
\right)
\frac{\binom n{n/2}}{n}
\]

along even `n`, while

\[
L_{\mathrm{MS}}(n)
\ge
L_K(n)
+
\left(
\frac{2}{e\log2}+o(1)
\right)
\frac{\binom n{\lfloor n/2\rfloor}}{n}
\]

along odd `n`.

Thus the odd-degree additive constant is twice the even-degree constant in the natural `binom(n,floor(n/2))/n` normalization.

## 6. Interpretation and limitation

The parity effect comes from the asymmetric choice

\[
m=k,
\qquad
r=k+1
\]

in odd degree. The fixed-term count is governed by the `k`th derivative layer, while the residual loss is governed by the `(k+1)`st layer. Their exact ratio differs by

\[
1-\frac{c}{k+1},
\]

producing the factor `2c` in (3.6).

The improvement remains lower order than the central-binomial main term and does not close the multiplicative gap to Glynn's upper bound. It is an ordinary Chow-rank result; no border-rank promotion is claimed.