# The central derivative degree globally optimizes the first-Koszul ratio

## Status

`PROOF_DRAFT_COMPLETE` — the algebraic proof below has been checked symbolically and against exact arithmetic for `3 <= n <= 1000`. External peer review and a complete literature novelty review have not been performed.

## 1. Statement

For `2 <= m <= n-1`, define

\[
R_{n,m}
=
\frac{
 n^2\binom nm^2-\binom n{m+1}^2
}{
 n^2\binom nm-\binom n{m+1}
}.
\]

This is the exact rank ratio of the generalized first-Koszul flattening for `perm_n` against the maximum contribution of one Chow term.

### Theorem 1.1

For every `n >= 3`, the unique maximizer of `R_{n,m}` on `2 <= m <= n-1` is

\[
m_0=\left\lceil\frac n2\right\rceil.
\]

Consequently,

\[
L_K(n)=\left\lceil R_{n,m_0}\right\rceil,
\]

so the maximization over all derivative degrees can be removed from the general Koszul lower bound.

## 2. A one-variable form of the ratio

Write

\[
c_m=\binom nm,
\qquad
d_m=\binom n{m+1},
\qquad
r_m=\frac{d_m}{c_m}=\frac{n-m}{m+1}.
\]

Because `n^2 c_m-d_m>0`, direct subtraction gives

\[
R_{n,m}
=
 c_m+
 \frac{d_m(c_m-d_m)}{n^2c_m-d_m}.
\tag{2.1}
\]

Equivalently,

\[
\frac{R_{n,m}}{c_m}
=
1+\frac{r_m(1-r_m)}{n^2-r_m}.
\tag{2.2}
\]

Let

\[
M_n=\binom n{\lfloor n/2\rfloor}.
\]

## 3. Degrees below the center

If `m < floor(n/2)`, then `d_m>c_m`. Equation (2.1) gives

\[
R_{n,m}<c_m\le M_n.
\]

If `n=2s+1` and `m=s=floor(n/2)`, then `d_m=c_m=M_n`, so

\[
R_{n,s}=M_n.
\]

At the proposed maximizing degree `m_0=ceil(n/2)`, one has `c_{m_0}=M_n` and `d_{m_0}<c_{m_0}`. Hence

\[
R_{n,m_0}>M_n.
\tag{3.1}
\]

Thus every degree at or below `floor(n/2)` is strictly inferior to `m_0`.

## 4. Degrees above the center

Assume `m>m_0`. Then `0<r_m<1`. From (2.2),

\[
\frac{R_{n,m}}{c_m}
=
1+\frac{r_m(1-r_m)}{n^2-r_m}
\le
1+\frac{1}{4(n^2-1)}.
\tag{4.1}
\]

### Even case

Let `n=2s`, so `m_0=s`. For every `m>=s+1`, unimodality of the binomial coefficients gives

\[
\frac{c_m}{M_n}
\le
\frac{\binom{2s}{s+1}}{\binom{2s}{s}}
=
\frac{s}{s+1}.
\]

Since

\[
\frac{1}{4(4s^2-1)}<\frac1s,
\]

we obtain from (4.1)

\[
\frac{R_{2s,m}}{M_{2s}}
\le
\frac{s}{s+1}
\left(1+\frac{1}{4(4s^2-1)}\right)
<1.
\]

Therefore `R_{2s,m}<M_{2s}<R_{2s,s}` for all `m>s`.

### Odd case

Let `n=2s+1`, so `m_0=s+1`. For every `m>=s+2`,

\[
\frac{c_m}{M_n}
\le
\frac{\binom{2s+1}{s+2}}{\binom{2s+1}{s+1}}
=
\frac{s}{s+2}.
\]

For `s>=1`,

\[
\frac{1}{4((2s+1)^2-1)}<\frac2s.
\]

Hence

\[
\frac{R_{2s+1,m}}{M_{2s+1}}
\le
\frac{s}{s+2}
\left(1+\frac{1}{4((2s+1)^2-1)}\right)
<1.
\]

The case `n=3` has no admissible degree above `m_0`. Thus every degree above the center is also strictly inferior.

Combining Sections 3 and 4 proves Theorem 1.1.

## 5. Closed forms at the optimizer

The theorem turns the general Koszul bound into a closed single-degree formula.

For `n=2s`, set `C_s=binom(2s,s)`. Then

\[
R_{2s,s}
=
C_s+
\frac{C_s}{(s+1)(4s(s+1)-1)}.
\]

For `n=2s+1`, set `C_s=binom(2s+1,s+1)`. Then

\[
R_{2s+1,s+1}
=
C_s+
\frac{C_s s}{(s+2)(2s^3+6s^2+4s+1)}.
\]

Therefore

\[
\boxed{
L_K(n)=
\left\lceil R_{n,\lceil n/2\rceil}\right\rceil.
}
\]

The correction above the central binomial coefficient is of order

\[
\Theta\!\left(\frac{2^n}{n^{7/2}}\right),
\]

whereas the central binomial coefficient itself is of order `2^n/sqrt(n)`.

## 6. Consequences and limitations

1. The ordinary and border first-Koszul bounds have an explicit optimizer; exhaustive search over `m` is unnecessary.
2. The theorem does not show that first-Koszul flattenings are optimal among all flattenings.
3. The theorem does not improve the asymptotic scale beyond the central-binomial scale.
4. The shadow-removal optimizer may occur at a different pair `(m,d)` and is not covered by this theorem.
5. No literature novelty claim is made until this exact optimization statement is compared with existing Chow-secant flattening results.
