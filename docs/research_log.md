# Research log

## 2026-08-03 — repository initialization and first general-`n` extension

### Established in the current proof draft

- The permanent derivative spaces satisfy
  \[
  \dim \mathcal D_m(\operatorname{perm}_n)=\binom nm^2.
  \]
- For `2 <= m <= n-1`, the first prolongation satisfies
  \[
  \mathcal D_m(\operatorname{perm}_n)^{(1)}
  =\mathcal D_{m+1}(\operatorname{perm}_n).
  \]
- The generalized first-Koszul flattening gives the exact target rank
  \[
  A_{n,m}=n^2\binom nm^2-\binom n{m+1}^2
  \]
  and one-Chow-term cap
  \[
  B_{n,m}=n^2\binom nm-\binom n{m+1}.
  \]
- The same determinantal obstruction applies to border Chow rank because matrix-rank upper bounds are Zariski closed.
- The first-Koszul rank ratio is globally and uniquely maximized at the central derivative degree
  \[
  m=\left\lceil\frac n2\right\rceil.
  \]
  This removes the maximization over `m` and yields closed even/odd formulas for `L_K(n)`.
- Consequently,
  \[
  \underline{\operatorname{ChowRank}}(\operatorname{perm}_n)
  \ge \binom n{\lfloor n/2\rfloor}+1.
  \]
- The stronger zero-intersection shadow-removal bound remains an ordinary Chow-rank result only; no border-rank promotion is claimed.
- Choosing the central derivative degree and
  \[
  d\sim\left(1-\frac1{\sqrt2}\right)\left\lfloor\frac n2\right\rfloor
  \]
  gives an explicit additive gain
  \[
  L_{SR}(n)
  \ge L_K(n)+
  \Omega\left(
  \frac{((1+\sqrt2)/2)^n}{\sqrt n}
  \right).
  \]

### `n=6` frontier at that stage

The initial in-repository lower bound was

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge22.
\]

This entry is retained as research history; the next entry supersedes it with 23.

## 2026-08-04 — multidimensional shadows and the first `n=6` geometric obstruction

### General complementary-intersection residual lemma

For arbitrary `n>=4` and `2<=m<=n-2`, put `r=n-m`. If `R` is a fixed sum of Chow terms, the asymmetric catalectic double-quotient argument gives

\[
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-n^2b,
\]

where

\[
b=\dim\left(
\mathcal D_r(P_n)
\cap
\mathcal D_r(R)
\right).
\]

The output-side intersection and the catalectic rank cancel. Thus the self-transpose even case is a convenient special case rather than a necessary hypothesis.

### Multidimensional-shadow intersection control

The permanent complementary derivative basis is indexed by

\[
\binom{[n]}r\times\binom{[n]}r.
\]

A row-column torus degeneration turns an arbitrary intersection subspace into a coordinate family. Bukh's multidimensional Kruskal--Katona theorem controls its simultaneous lower shadow and yields exact-rational lower-bound certificates in every reviewed degree from 4 through 16.

The reviewed table includes

\[
\operatorname{ChowRank}(\operatorname{perm}_5)\ge13,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_6)\ge23,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_7)\ge41.
\]

For `n=6`, four fixed terms imply a central intersection cap of 40, so

\[
14175-36\cdot40=12735,
\qquad
\left\lceil\frac{12735}{705}\right\rceil=19,
\]

and the total lower bound is `4+19=23`.

### Even-degree asymptotics

With `n=2k`, `x=2k-c`, and optimized constant

\[
c_*=\frac{1+1/\log2}{2},
\]

the even-degree lower bound satisfies

\[
L_{MS}(2k)
\ge
L_K(2k)
+
\left(
\frac{1}{2e\log2}+o(1)
\right)
\frac{\binom{2k}{k}}{k}.
\]

### `n=6` coordinate secant audit

The exact finite audit of the 400 coordinate `3 x 3` subpermanents checked all

\[
\binom{400}{2}=79,800
\]

coordinate lines. Their first-catalectic ranks are distributed as follows:

```text
rank  9:  3,600
rank 13: 16,200
rank 15:  3,600
rank 16: 32,400
rank 17: 16,200
rank 18:  7,800
```

At every coordinate point, the rank-at-most-nine locus has affine tangent dimension 19 and projective tangent dimension 18. Hence the low-catalectic boundary is positive-dimensional; an isolated-fixed-point strategy is invalid.

## 2026-08-04 — quotient Koszul gain and a proved barrier for the current `n=6` formula

### Exact quotient gain retained

For

\[
E_m=\mathcal D_m(P_n),
\qquad
H_m=\mathcal D_m(R),
\]

let

\[
h=\dim H_m,
\qquad
a=\dim(E_m\cap H_m),
\]

and define

\[
p_E(H_m)
=
\dim\left((E_m+H_m)^{(1)}/E_m^{(1)}\right),
\]

\[
\Gamma_E(H_m)
=
n^2(h-a)-p_E(H_m).
\]

The residual argument can be kept in the sharper form

\[
\boxed{
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-n^2b+\Gamma_E(H_m),
}
\]

where

\[
b=\dim\left(
\mathcal D_{n-m}(P_n)
\cap
\mathcal D_{n-m}(R)
\right).
\]

Moreover,

\[
\Gamma_E(H_m)
=
\operatorname{rank}\delta_m((E_m+H_m)\otimes V)
-
\operatorname{rank}\delta_m(E_m\otimes V).
\]

Thus `Gamma` is the actual new Koszul image contributed by the quotient directions. The previous multishadow theorem used only the inequality `Gamma>=0`.

### Derivative-transversality criterion

If the lower derivative spaces of two homogeneous subspaces are disjoint, their prolongations split and their Koszul ranks add. In particular, if

\[
\partial E_m\cap\partial H_m=0,
\]

then the entire Koszul rank of `H_m` survives as quotient gain.

### Explicit full-gain term at `n=6`

For

\[
T_{\mathrm{diag}}=\prod_{i=0}^{5}x_{ii},
\]

the spaces

\[
\mathcal D_2(P_6)
\quad\text{and}\quad
\mathcal D_2(T_{\mathrm{diag}})
\]

are disjoint. Consequently

\[
\Gamma=705
\]

and

\[
\operatorname{rank}\delta_3
\left(
(\mathcal D_3(P_6)+\mathcal D_3(T_{\mathrm{diag}}))\otimes V
\right)
=14880.
\]

The independent sparse-integer replay obtains rank 14,880 modulo `1,000,003`. Subadditivity gives the matching characteristic-zero upper bound `14,175+705`, so the equality is exact over characteristic zero.

This is an existence certificate, not a uniform theorem for arbitrary Chow terms.

### Quantified next target

At the current four-term frontier,

\[
b\le40
\]

and the intersection-only residual floor is 12,735. To raise the universal lower bound from 23 to 24 by this state, it would suffice to prove

\[
\boxed{\Gamma\ge661.}
\]

The corresponding thresholds for the neighboring one-step states are 790 for three fixed terms and 676 for five fixed terms. The four-term state is therefore the minimal quantified target.

### Exact route barrier

A complete exact optimization of the current one-step Bukh-shadow formula over every output degree

\[
m\in\{2,3,4\}
\]

and every continuous witness value proves that the formula cannot exceed 23 at `n=6`.

The only maximizing states are

```text
m=3, q=4, intersection cap=40, residual terms=19
m=3, q=5, intersection cap=60, residual terms=18
```

The coordinate family

\[
\binom{[5]}3\times\binom{[4]}3
\]

has size 40 and simultaneous shadow size 60, so the universal `q=4` Bukh cap is sharp. A denser witness search, a different admissible output degree, or a tighter universal scalar shadow estimate cannot produce 24.

The next improvement must use at least one of the following:

1. non-realizability of the extremal coordinate families as Chow intersections;
2. a positive quotient gain `Gamma`;
3. coupled information beyond one shadow cardinality;
4. a different flattening or invariant.

### Odd-degree asymptotic constant

For `n=2k+1`, choose output degree `m=k`, complementary degree `r=k+1`, and witness `x=2k+1-c`. The exact ratio identity

\[
R_{k+1}(c)
=
R_k(c)
\left(1-\frac{c}{k+1}\right)
\]

yields

\[
L_{MS}(2k+1)-L_K(2k+1)
\ge
2c4^{-c}
\frac{\binom{2k+1}{k}}{k}
+
O\left(
\frac{\binom{2k+1}{k}}{k^2}
\right).
\]

The unique optimizer is

\[
c=\frac1{\log4},
\]

so

\[
\boxed{
L_{MS}(2k+1)
\ge
L_K(2k+1)
+
\left(
\frac1{e\log2}+o(1)
\right)
\frac{\binom{2k+1}{k}}{k}.
}
\]

In the normalization `binom(n,floor(n/2))/n`, the odd constant is twice the even constant.

### Evidence and claim boundary

- The quotient-gain identity and parity asymptotic are proof drafts, not peer-reviewed theorems.
- The route-barrier and diagonal-term scripts are exact deterministic diagnostics.
- The route barrier is a limitation of the current scalar one-step formula, not an upper bound on Chow rank.
- No uniform `Gamma>=661` theorem has been proved.
- The current interval remains
  \[
  23\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
  \]

## 2026-08-22 — Rethlas `perm_7` theory-first run

### Corrected unrestricted lower bound

The run produced a working proof draft for

\[
50\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

An initial quadratic-restriction surjectivity claim was false because it reversed the apolar degree. The run explicitly retracted that step, retained counterexamples, and rebuilt the two endpoint exclusions using the correct degree-three and degree-four local restriction maps. Independent internal audits accepted the corrected middle-degree proof.

### Exact-64 route boundary

The exact value 64 remains open. The strongest residual-section formulation currently requires

\[
\operatorname{borderCR}(\operatorname{perm}_7|_{x_{77}=0})\geq63,
\]

while a Glynn-factor degeneration supplies the matching upper bound. The run also records why scalar slope surplus, one-step Tor/Koszul functors, purely linear row-normal layers, and local rigidity at the Glynn point do not close the global problem.

### Evidence and authorship boundary

- Argument source: the Rethlas generation run `perm7_theory_first_20260822` and its recursive branches.
- Verification source: independent internal Rethlas audits and deterministic publication replays.
- No named independent human review or proof-assistant formalization has been completed.
- No whole-problem verifier was called and no `blueprint_verified.md` was produced.
- Detailed proof, status, reports, scripts, and frozen outputs are indexed from `docs/rethlas_perm7_20260822/README.md`.
