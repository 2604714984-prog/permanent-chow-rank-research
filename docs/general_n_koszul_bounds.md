# General-`n` Koszul and shadow-removal bounds

## Status

`PROOF_DRAFT_COMPLETE` — internally checked and backed by exact arithmetic tests. External peer review and literature novelty review are not complete.

## 1. Setup

Let

\[
P_n=\operatorname{perm}_n\in \operatorname{Sym}^n(V_n),
\qquad
V_n=\operatorname{span}\{x_{ij}:1\le i,j\le n\},
\qquad
\dim V_n=n^2.
\]

For a degree-`n` form `f`, define its degree-`m` derivative space

\[
\mathcal D_m(f)=\operatorname{im} C_{n-m,m}(f)
\subseteq \operatorname{Sym}^m V_n.
\]

For `H subset Sym^m V_n`, define the first prolongation

\[
H^{(1)}=\{g\in\operatorname{Sym}^{m+1}V_n:
\partial_\xi g\in H\text{ for every }\xi\in V_n^*\}.
\]

## 2. Derivative spaces of the permanent

For row and column sets `I,J subset [n]` of size `m`, write `P_{I,J}` for the corresponding `m x m` subpermanent.

### Proposition 2.1

\[
\mathcal D_m(P_n)
=
\operatorname{span}\{P_{I,J}:|I|=|J|=m\},
\qquad
\dim\mathcal D_m(P_n)=\binom nm^2.
\]

### Proof

Applying an `(n-m)`th-order differential operator deletes `n-m` rows and columns and leaves an `m x m` subpermanent. Conversely every such subpermanent is obtained in this way. Distinct pairs `(I,J)` have disjoint row-set/column-set monomial support, so they are linearly independent. ∎

## 3. The prolongation tower

### Proposition 3.1

For `2 <= m <= n-1`,

\[
\boxed{\mathcal D_m(P_n)^{(1)}=\mathcal D_{m+1}(P_n).}
\]

### Proof

The reverse inclusion is immediate: every first derivative of an `(m+1) x (m+1)` subpermanent is an `m x m` subpermanent.

For the forward inclusion, let `g in D_m(P_n)^(1)`. A monomial of `g` cannot contain a repeated variable, repeated matrix row, or repeated matrix column. Otherwise differentiating with respect to a variable occurring in that monomial produces, in a fixed partial derivative, a monomial outside the support of `D_m(P_n)`; no other monomial can cancel it in that same partial derivative.

Hence `g` decomposes by `(m+1)`-row and `(m+1)`-column supports. Fix one block `(I,J)` and write

\[
g_{I,J}=\sum_{\sigma:I\to J}c_\sigma
\prod_{i\in I}x_{i,\sigma(i)}.
\]

For fixed `(i,j)`, the derivative `partial_{ij} g_{I,J}` must be a scalar multiple of the corresponding `m x m` permanent. Therefore all `c_sigma` with `sigma(i)=j` are equal. Two permutations differing by a transposition share at least one fixed assignment because `m+1>=3`; transpositions generate the symmetric group. Thus all coefficients in the block are equal, and the block is a scalar multiple of `P_{I,J}`. Summing over blocks proves the claim. ∎

Consequently,

\[
\dim \mathcal D_m(P_n)^{(1)}=\binom n{m+1}^2.
\]

## 4. Generalized first-Koszul flattening

Define

\[
\delta_m:\operatorname{Sym}^mV_n\otimes V_n
\longrightarrow
\operatorname{Sym}^{m-1}V_n\otimes\Lambda^2V_n,
\]

\[
\delta_m(q\otimes v)=
\sum_a \frac{\partial q}{\partial x_a}\otimes(x_a\wedge v).
\]

The standard Koszul complex is exact at `Sym^m V tensor V`; therefore

\[
\ker(\delta_m|_{H\otimes V_n})\cong H^{(1)}.
\]

Define

\[
K_{n,m}(f)=\delta_m\circ(C_{n-m,m}(f)\otimes\operatorname{id}_{V_n}).
\]

### Theorem 4.1 — exact target and one-term ranks

For the permanent,

\[
A_{n,m}:=\operatorname{rank}K_{n,m}(P_n)
=n^2\binom nm^2-\binom n{m+1}^2.
\]

For one Chow term `T=l_1...l_n`,

\[
\operatorname{rank}K_{n,m}(T)
\le
B_{n,m}:=n^2\binom nm-\binom n{m+1},
\]

with equality when the factors are linearly independent.

### Proof

The permanent formula follows from Propositions 2.1 and 3.1 plus rank-nullity. For an independent Chow term, a linear change of coordinates reduces to `x_1...x_n`; its degree-`m` derivative space is the span of the squarefree `m`-fold products, and its prolongation is the span of the squarefree `(m+1)`-fold products. Degenerate factor tuples are specializations of independent tuples, and matrix rank cannot increase under specialization. ∎

### Corollary 4.2 — computable lower bound

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge
L_K(n):=
\max_{2\le m\le n-1}
\left\lceil
\frac{n^2\binom nm^2-\binom n{m+1}^2}
{n^2\binom nm-\binom n{m+1}}
\right\rceil.
}
\]

This follows from linearity of the flattening and subadditivity of matrix rank. Because the condition `rank K_{n,m}(f) <= r B_{n,m}` is determinantal and therefore Zariski closed, the same bound holds for border Chow rank. The border-rank statement and its scope are written separately in `docs/border_chow_rank_bounds.md`.

The ratio is uniquely maximized at

\[
m=\left\lceil\frac n2\right\rceil.
\]

A proof is given in `docs/central_koszul_optimality.md`. Thus the maximization over `m` can be replaced by a single central-degree evaluation.

### Corollary 4.3 — central catalecticant plus one

For every `n>=3`,

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge \binom n{\lfloor n/2\rfloor}+1.
}
\]

Take `m=ceil(n/2)`, set `c=binom(n,m)` and `d=binom(n,m+1)`. Then `c>d>0`, and

\[
\frac{n^2c^2-d^2}{n^2c-d}-c
=
\frac{d(c-d)}{n^2c-d}>0.
\]

The ratio is strictly greater than the central binomial coefficient, so its ceiling is at least one larger.

## 5. Derivative-shadow rigidity

Let `k=n-m`. For a degree-`k` polynomial `g`, let `partial^d g` denote the span of all order-`d` derivatives.

### Lemma 5.1 — permanent-side lower shadow

For every nonzero `g in D_k(P_n)` and `1<=d<=k`,

\[
\dim \partial^d g\ge\binom kd^2.
\]

### Proof

The row-column torus gives the basis subpermanents `P_{I,J}` pairwise distinct weights. Choose an integral one-parameter subgroup with a unique lowest weight on the support of `g`; after rescaling, the limit is a nonzero scalar multiple of one `P_{I,J}`. Derivative-matrix rank cannot increase at the special fiber, so

\[
\dim\partial^d g\ge\dim\partial^dP_{I,J}=\binom kd^2.
\]

The last equality follows because the derivatives are exactly the `(k-d) x (k-d)` subpermanents obtained by deleting `d` rows and `d` columns. ∎

### Lemma 5.2 — one-Chow-term upper shadow

For every Chow term `T` and every `g in D_k(T)`,

\[
\dim\partial^d g
\le
M_{n,k,d}:=
\min\left\{\binom nd,\binom n{k-d}\right\}.
\]

### Proof

Write the Chow factors as the image of formal variables `y_1,...,y_n` under a linear substitution. Every element of `D_k(T)` is the image of a squarefree degree-`k` polynomial in the `y_i`. Its order-`d` derivatives are generated by at most `binom(n,d)` squarefree differential operators and land in a space spanned by at most `binom(n,k-d)` squarefree monomials. Linear substitution cannot increase the rank. ∎

### Corollary 5.3 — zero-intersection criterion

For Chow terms `T_1,...,T_q`, if

\[
qM_{n,k,d}<\binom kd^2,
\]

then

\[
\mathcal D_k(P_n)\cap
\sum_{i=1}^q\mathcal D_k(T_i)=0.
\]

Indeed, a nonzero element in the intersection would simultaneously have derivative-shadow dimension at least `binom(k,d)^2` and at most `q M_{n,k,d}`.

## 6. Removing certified terms

The transpose of the catalecticant gives

\[
\operatorname{row}K_{n,m}(f)
\subseteq \mathcal D_{n-m}(f)\otimes V_n^*.
\]

Therefore the zero-intersection criterion makes the row spaces of `K_{n,m}(P_n)` and `K_{n,m}(R)` disjoint when `R` is the sum of the selected terms.

For same-shaped matrices `A,B`, the double-quotient inequality is

\[
\operatorname{rank}(A-B)
\ge
\operatorname{rank}[A\ B]
+
\operatorname{rank}\begin{bmatrix}A\\B\end{bmatrix}
-
\operatorname{rank}A-
\operatorname{rank}B.
\]

Disjoint row spaces make the vertical concatenation rank equal to the sum of the two ranks; the horizontal concatenation has rank at least `rank A`. Hence

\[
\operatorname{rank}K_{n,m}(P_n-R)\ge A_{n,m}.
\]

Define

\[
q_{n,m,d}
=
\min\left
\{
L_K(n),
\left\lfloor
\frac{\binom{n-m}{d}^2-1}
{\min\{\binom nd,\binom n{n-m-d}\}}
\right\rfloor
\right\}.
\]

The cap by `L_K(n)` guarantees that any hypothetical decomposition contains at least `q_{n,m,d}` selectable terms.

### Theorem 6.1 — shadow-removal lower bound

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge
L_{SR}(n):=
\max_{m,d}
\left(
q_{n,m,d}
+
\left\lceil\frac{A_{n,m}}{B_{n,m}}\right\rceil
\right).
}
\]

### Proof

Select `q=q_{n,m,d}` terms from a hypothetical decomposition and call their sum `R`. Corollary 5.3 makes the relevant degree-`n-m` derivative spaces disjoint, so the residual flattening has rank at least `A_{n,m}`. The remaining terms contribute at most `B_{n,m}` each. Thus at least `ceil(A/B)` terms remain in addition to the selected `q`. ∎

## 7. Exact arithmetic values

| `n` | `L_K(n)` | `L_SR(n)` | Glynn upper bound |
|---:|---:|---:|---:|
| 3 | 4 | 4 | 4 |
| 4 | 7 | 7 | 8 |
| 5 | 11 | 11 | 16 |
| 6 | 21 | **22** | 32 |
| 7 | 36 | **37** | 64 |
| 8 | 71 | **72** | 128 |
| 9 | 127 | **128** | 256 |
| 10 | 253 | **255** | 512 |
| 11 | 463 | **466** | 1024 |
| 12 | 925 | **928** | 2048 |
| 16 | 12875 | **12881** | 32768 |

The complete table through `n=50` is generated under `data/`.

## 8. What is not proved

These bounds remain on the central-binomial scale. They do not prove the conjectural exact value `2^(n-1)`. No claim of literature novelty is made until a dedicated prior-art review is completed.
