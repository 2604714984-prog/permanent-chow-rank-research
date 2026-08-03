# Border Chow-rank lower bounds for the permanent

## Status

`PROOF_DRAFT_COMPLETE` — the argument is a direct closed-rank consequence of the generalized Koszul flattening developed in this repository. It has not yet received external peer review or a complete novelty review.

## 1. Border Chow rank

Let `Chow_n(V)` be the projective variety of degree-`n` forms that are products of `n` linear forms. The border Chow rank of a degree-`n` form `f`, denoted

\[
\underline{\operatorname{ChowRank}}(f),
\]

is the least integer `r` such that `[f]` lies in the `r`th secant variety of `Chow_n(V)`. Equivalently, `f` is a limit of sums of `r` Chow terms.

For `2 <= m <= n-1`, let

\[
K_{n,m}(f)=\delta_m\circ
\bigl(C_{n-m,m}(f)\otimes\operatorname{id}_{V_n}\bigr)
\]

be the generalized first-Koszul flattening from `docs/general_n_koszul_bounds.md`.

Set

\[
A_{n,m}=n^2\binom nm^2-\binom n{m+1}^2,
\qquad
B_{n,m}=n^2\binom nm-\binom n{m+1}.
\]

The derivative-tower proof gives

\[
\operatorname{rank}K_{n,m}(\operatorname{perm}_n)=A_{n,m},
\]

while every Chow term `T`, including a degenerate one, satisfies

\[
\operatorname{rank}K_{n,m}(T)\le B_{n,m}.
\]

## 2. Closed determinantal obstruction

### Theorem 2.1

For every characteristic-zero field and every `n >= 3`,

\[
\boxed{
\underline{\operatorname{ChowRank}}(\operatorname{perm}_n)
\ge
L_K(n):=
\max_{2\le m\le n-1}
\left\lceil\frac{A_{n,m}}{B_{n,m}}\right\rceil.
}
\]

### Proof

Fix `m` and suppose that `f` has border Chow rank at most `r`. Then there is a one-parameter family

\[
f(t)=\sum_{i=1}^r T_i(t)
\]

of sums of `r` Chow terms with `f(t)` tending to `f`. The flattening is linear in the polynomial, so for every non-special parameter value,

\[
\operatorname{rank}K_{n,m}(f(t))
\le
\sum_{i=1}^r\operatorname{rank}K_{n,m}(T_i(t))
\le rB_{n,m}.
\]

The locus of matrices of rank at most `rB_{n,m}` is Zariski closed because it is cut out by minors. Therefore the limiting matrix also has rank at most `rB_{n,m}`:

\[
\operatorname{rank}K_{n,m}(f)\le rB_{n,m}.
\]

For `f=perm_n`, the left side is `A_{n,m}`. Hence

\[
r\ge\left\lceil\frac{A_{n,m}}{B_{n,m}}\right\rceil.
\]

Maximizing over `m` proves the theorem. ∎

## 3. Uniform central-binomial consequence

### Corollary 3.1

For every `n >= 3`,

\[
\boxed{
\underline{\operatorname{ChowRank}}(\operatorname{perm}_n)
\ge
\binom n{\lfloor n/2\rfloor}+1.
}
\]

### Proof

Take `m=ceil(n/2)` and write

\[
c=\binom nm,\qquad d=\binom n{m+1}.
\]

Then `c>d>0`, and

\[
\frac{n^2c^2-d^2}{n^2c-d}-c
=
\frac{d(c-d)}{n^2c-d}>0.
\]

The flattening ratio is strictly larger than the integer `c`, so its ceiling is at least `c+1`. By symmetry `c=binom(n,floor(n/2))`. ∎

Using Stirling's formula,

\[
\binom n{\lfloor n/2\rfloor}
\sim
2^n\sqrt{\frac{2}{\pi n}},
\]

so the border Chow-rank lower bound has central-binomial scale.

## 4. Exact central-degree correction

The central choice also admits a closed rational correction above the central binomial coefficient.

For `n=2s`, let `c=binom(2s,s)`. At `m=s`,

\[
\frac{A_{2s,s}}{B_{2s,s}}
=
 c+
 \frac{c}{(s+1)\bigl(4s(s+1)-1\bigr)}.
\]

For `n=2s+1`, let `c=binom(2s+1,s+1)`. At `m=s+1`,

\[
\frac{A_{2s+1,s+1}}{B_{2s+1,s+1}}
=
 c+
 \frac{cs}{(s+2)(2s^3+6s^2+4s+1)}.
\]

These identities follow from

\[
\frac{n^2c^2-d^2}{n^2c-d}-c
=
\frac{d(c-d)}{n^2c-d}
\]

and the adjacent-binomial ratios. They quantify the amount by which the first-Koszul obstruction exceeds the ordinary central catalecticant.

## 5. Scope boundary

The shadow-removal theorem in `docs/general_n_koszul_bounds.md` is currently proved for an actual decomposition because it selects named summands before applying the zero-intersection criterion. This document does **not** promote that stronger bound to border Chow rank. Such a promotion would require a separate argument controlling summands in a degenerating family or a closed incidence formulation.

## 6. Literature status

Ilten and Teitler proved that the border product rank of `perm_n` is greater than `n` for `n >= 3`. Guan developed Koszul--Young equations for Chow varieties and their secants. A dedicated comparison with those equations is still required before any novelty claim is made for Theorem 2.1 or Corollary 3.1.
