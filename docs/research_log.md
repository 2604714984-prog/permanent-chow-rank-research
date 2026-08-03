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
- Consequently,
  \[
  \underline{\operatorname{ChowRank}}(\operatorname{perm}_n)
  \ge \binom n{\lfloor n/2\rfloor}+1.
  \]
- The stronger shadow-removal bound remains an ordinary Chow-rank result only; no border-rank promotion is claimed.

### `n=6` frontier

The verified in-repository lower bound is

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge22,
\]

while Glynn gives 32. The central flattening uses `m=3`, with target rank 14,175 and one-term cap 705. Proving exact value 32 by this route requires a refined fixed-term argument that controls a rank margin of 75 after fixing 11 terms.

### Immediate research priorities

1. Compare the border-Koszul theorem with Guan's Chow-secant flattenings and subsequent literature.
2. Test whether the `n=6` central derivative-space intersection can be classified before introducing large finite-state machinery.
3. Search for structured low-rank residuals as route-falsification diagnostics; finite-field observations remain non-decisive.
