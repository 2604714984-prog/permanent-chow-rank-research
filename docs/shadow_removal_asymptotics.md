# Asymptotic additive gain from shadow removal

## Status

`PROOF_DRAFT_COMPLETE` — the entropy optimization and Stirling argument below have been checked symbolically and numerically. External peer review and a complete literature novelty review have not been performed.

## 1. Purpose

The generalized first-Koszul lower bound has central-binomial scale. The shadow-removal theorem improves it by an additive quantity. This note proves that one explicit central-degree choice already gives an exponentially growing additive gain.

Let

\[
L_K(n)=
\left\lceil
\frac{A_{n,m_0}}{B_{n,m_0}}
\right\rceil,
\qquad
m_0=\left\lceil\frac n2\right\rceil,
\qquad
k=\left\lfloor\frac n2\right\rfloor.
\]

The equality with the optimized first-Koszul bound follows from `docs/central_koszul_optimality.md`.

For `1<=d<=k`, the central shadow-removal capacity is

\[
q_{n,d}=
\left\lfloor
\frac{\binom kd^2-1}
{\min\{\binom nd,\binom n{k-d}\}}
\right\rfloor.
\]

The shadow-removal theorem gives

\[
L_{SR}(n)\ge L_K(n)+q_{n,d}
\]

whenever the global lower-bound cap is inactive; the proof below verifies that it is inactive for the chosen asymptotic sequence.

## 2. Main theorem

Define

\[
\beta=1-\frac1{\sqrt2},
\qquad
\alpha=\frac\beta2
=
\frac{1-1/\sqrt2}{2},
\qquad
 a=\frac{1+\sqrt2}{2}.
\]

Choose an integer `d_n` nearest to `beta k`.

### Theorem 2.1

There exist constants `c,C>0` and `N` such that for every `n>=N`,

\[
c\frac{a^n}{\sqrt n}
\le
q_{n,d_n}
\le
C\frac{a^n}{\sqrt n}.
\]

Consequently, for some constant `c_0>0`,

\[
\boxed{
L_{SR}(n)
\ge
L_K(n)+c_0\frac{a^n}{\sqrt n}
}
\]

for every sufficiently large `n`.

This is an additive improvement of exponential size. It remains exponentially smaller than the leading central-binomial term because `a<2`.

## 3. Which denominator is active

Because

\[
\frac{d_n}{k}\longrightarrow\beta<\frac12,
\]

we have `d_n<k-d_n` for all sufficiently large `n`. Moreover,

\[
\frac{k-d_n}{n}
\longrightarrow
\frac{1-\beta}{2}
=
\frac1{2\sqrt2}
<\frac12.
\]

Both indices are eventually on the increasing side of the binomial sequence `binom(n,j)`. Therefore

\[
\min\left\{\binom n{d_n},\binom n{k-d_n}\right\}
=
\binom n{d_n}.
\tag{3.1}
\]

Thus it is enough to analyze

\[
Q_n=
\frac{\binom{k}{d_n}^2}{\binom n{d_n}}.
\]

The subtraction of one and the outer floor alter the result by at most a bounded additive amount, which is negligible compared with the exponential growth established below.

## 4. Entropy exponent

Let

\[
H_2(x)=-x\log_2x-(1-x)\log_2(1-x)
\]

be the binary entropy. Standard Stirling estimates, uniformly on compact subintervals of `(0,1)`, give

\[
\binom{k}{d_n}
=
\Theta\left(
\frac{2^{kH_2(\beta)}}{\sqrt k}
\right)
\]

and

\[
\binom n{d_n}
=
\Theta\left(
\frac{2^{nH_2(\alpha)}}{\sqrt n}
\right),
\]

because `k=n/2+O(1)` and `d_n/n -> alpha`. Hence

\[
Q_n
=
\Theta\left(
\frac{2^{n(H_2(\beta)-H_2(\alpha))}}{\sqrt n}
\right).
\tag{4.1}
\]

The entropy difference has the exact value

\[
2^{H_2(\beta)-H_2(\alpha)}
=
\frac{1+\sqrt2}{2}
=a.
\tag{4.2}
\]

To verify (4.2), put `s=1/sqrt(2)`, so `beta=1-s`, `alpha=(1-s)/2`, and

\[
(1-s)(1+s)=s^2=\frac12.
\]

Substituting these identities into the entropy expression reduces its logarithm to

\[
\log\left(\frac{1+s}{2s}\right)
=
\log\left(\frac{1+\sqrt2}{2}\right).
\]

Equations (4.1) and (4.2) prove

\[
Q_n=\Theta\left(\frac{a^n}{\sqrt n}\right).
\]

Because the right side tends to infinity, the floor and the `-1` in the numerator preserve the same asymptotic order. This proves the two-sided estimate for `q_{n,d_n}`.

Finally,

\[
L_K(n)=\Theta\left(\frac{2^n}{\sqrt n}\right),
\]

so `q_{n,d_n}/L_K(n)` tends to zero exponentially. In particular, the cap `q<=L_K(n)` in the shadow-removal theorem is inactive for all sufficiently large `n`.

## 5. Optimal derivative fraction within the central construction

For a general sequence with `d/k -> x` and `0<x<1/2`, the exponential rate per matrix size is

\[
F(x)=H_2(x)-H_2(x/2).
\]

Its second derivative is

\[
F''(x)
=-\frac{1}{(\ln2)x(1-x)(2-x)}<0,
\]

so `F` is strictly concave. Its critical-point equation is

\[
H_2'(x)-\frac12H_2'(x/2)=0,
\]

which is equivalent to

\[
(1-x)^2=x(2-x).
\]

The unique solution in `(0,1/2)` is

\[
x=1-\frac1{\sqrt2}=\beta.
\]

Therefore `beta` uniquely maximizes the exponential base among all central-degree shadow-removal choices with a limiting derivative fraction below one half.

## 6. Quantitative interpretation

Numerically,

\[
a=1.207106781\ldots,
\qquad
\log_2a=0.271553303\ldots.
\]

Thus the explicit additive gain grows like

\[
\frac{1.2071^n}{\sqrt n}.
\]

Relative to the leading first-Koszul term, it is smaller by the exponential factor

\[
\left(\frac{1+\sqrt2}{4}\right)^n
=0.603553\ldots^n.
\]

The result strengthens the finite values in the deterministic bound table, but it does not change the leading central-binomial asymptotic scale.

## 7. Scope boundary

- The theorem is an ordinary Chow-rank statement because it uses named summands from an actual decomposition.
- No border Chow-rank analogue is claimed.
- The theorem gives a lower bound on the optimized additive gain; it does not prove a matching upper bound for `L_SR(n)-L_K(n)`.
- The theorem does not imply the conjectural exact value `2^(n-1)`.
- No novelty claim is made pending a dedicated comparison with existing Chow-secant and Koszul--Young flattening literature.
