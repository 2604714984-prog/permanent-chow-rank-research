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
- The stronger shadow-removal bound remains an ordinary Chow-rank result only; no border-rank promotion is claimed.
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
  The derivative fraction is the unique entropy maximizer within this central shadow-removal construction.

### `n=6` frontier at that stage

The initial in-repository lower bound was

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge22.
\]

This entry is retained as research history; the next entry supersedes it with 23.

## 2026-08-04 — multidimensional shadows and the first `n=6` geometric obstruction

### Even-degree central residual lemma

For `n=2k`, the middle catalecticant is self-transpose. If `R` is a fixed sum of Chow terms,

\[
E=\mathcal D_k(P_n),
\qquad
H=\mathcal D_k(R),
\qquad
s=\dim(E\cap H),
\]

then the current proof draft establishes

\[
\operatorname{rank}K_k(P_n-R)
\ge
\operatorname{rank}K_k(P_n)-n^2s.
\]

The proof combines:

1. the double-quotient rank inequality for the two symmetric middle catalectics;
2. an injection
   \[
   (E+H)^{(1)}/E^{(1)}
   \hookrightarrow
   ((E+H)/E)\otimes V^*;
   \]
3. the Koszul kernel-prolongation identity.

The dimensions of `H` cancel; only the central intersection `s` costs rank.

### Multidimensional-shadow intersection control

The permanent central derivative basis is indexed by

\[
\binom{[2k]}k\times\binom{[2k]}k.
\]

A row-column torus degeneration turns an arbitrary intersection subspace into a coordinate family. Bukh's multidimensional Kruskal--Katona theorem then controls its lower shadow. For

\[
q_x=
\left\lfloor
\frac{\binom{x}{k-1}^2}{\binom{2k}{k-1}}
\right\rfloor,
\]

fixing `q_x` Chow terms forces

\[
s\le\left\lfloor\binom{x}{k}^2\right\rfloor.
\]

Substitution into the residual lemma gives a new exact lower-bound family for every even degree.

### Improved exact certificates

The deterministic exact-rational table now includes:

| `n` | previous central bound | new bound |
|---:|---:|---:|
| 4 | 7 | 8 |
| 6 | 21 | 23 |
| 8 | 71 | 76 |
| 10 | 253 | 267 |
| 12 | 925 | 968 |
| 14 | 3,434 | 3,568 |
| 16 | 12,875 | 13,312 |

In particular,

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_6)\ge23.
}
\]

For the frozen witness, four fixed terms imply `s<=40`; hence

\[
14175-36\cdot40=12735,
\qquad
\left\lceil\frac{12735}{705}\right\rceil=19,
\]

and the total lower bound is `4+19=23`.

The same argument independently excludes seven terms for `perm_4`:

\[
560-16\cdot6=464>5\cdot92=460.
\]

This is a shorter alternative lower proof; it does not replace the independently replayed 659-by-659 chart certificate in the small-`n` evidence boundary.

### Even-degree asymptotics

With `x=2k-c` and optimized constant

\[
c_*=
\frac{1+1/\log2}{2},
\]

the new lower bound satisfies

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

Equivalently, the additive gain for even `n` has scale

\[
\Theta\left(\frac{2^n}{n^{3/2}}\right).
\]

The argument is ordinary-rank only and does not close the multiplicative gap to Glynn.

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

For two coordinate points with row overlap `r` and column overlap `c`, the rank is

\[
18-rc-\binom r2\binom c2.
\]

The rank remains nine only for overlap types `(3,2)` and `(2,3)`; the next rank is 13.

At every coordinate point, the rank-at-most-nine determinantal locus has affine tangent dimension 19 and projective tangent dimension 18. The proof uses 19 explicit rational tangent directions and a rank-381 tangent-map certificate modulo `1,000,003`.

### Route decision

The coordinate low-catalectic boundary is not discrete. Each fixed point lies on multiple row- and column-replacement linear families. Therefore an `n=6` proof must not import an isolated-fixed-point assumption from a smaller case.

The next step is to classify these positive-dimensional branches relative to central intersections. No SAT, Hilbert-scheme, or Kuranishi layer is authorized until that classification produces a proved finite frontier.

### Evidence boundary

- The multidimensional-shadow theorem is a proof draft, not a peer-reviewed theorem.
- A preliminary literature search found Bukh's shadow theorem and Guan's Chow/Koszul framework, but did not establish novelty of their combination here.
- The coordinate audit is a route diagnostic and does not prove `ChowRank(perm_6)=32`.
- The current in-repository interval is
  \[
  23\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
  \]
