# A general multidimensional-shadow lower bound

## Status

`PROOF_DRAFT_COMPLETE` — the argument is written in full below, and the displayed finite certificates use exact rational arithmetic. External peer review and a complete literature novelty review have not been performed.

## 1. Setup

Work over a characteristic-zero field, after scalar extension to an algebraic closure when a torus degeneration is used.

Let

\[
P_n=\operatorname{perm}_n,
\qquad
N=n^2,
\]

and choose an output derivative degree

\[
2\le m\le n-2.
\]

Put

\[
r=n-m.
\]

For a degree-`n` form `f`, write

\[
\mathcal D_j(f)
=
\operatorname{im}C_{n-j,j}(f).
\]

The permanent derivative dimensions are

\[
\dim\mathcal D_j(P_n)=\binom nj^2.
\]

The first-Koszul flattening at output degree `m` has target rank

\[
A_{n,m}
=
N\binom nm^2-inom n{m+1}^2,
\tag{1.1}
\]

and one Chow term contributes at most

\[
B_{n,m}
=
N\binom nm-inom n{m+1}.
\tag{1.2}
\]

The key point is that the residual-rank loss is controlled by the intersection at the **complementary degree** `r`, even when the catalecticant is not square or self-transpose.

## 2. The asymmetric double-quotient cancellation

Fix a form `R` and define

\[
E_m=\mathcal D_m(P_n),
\qquad
H_m=\mathcal D_m(R),
\]

\[
E_r=\mathcal D_r(P_n),
\qquad
H_r=\mathcal D_r(R).
\]

Let

\[
h=\operatorname{rank}C_{r,m}(R),
\]

so both `H_m` and `H_r` have dimension `h`. Put

\[
a=\dim(E_m\cap H_m),
\qquad
b=\dim(E_r\cap H_r).
\]

Use divided-power bases, or equivalently the natural perfect pairings, so the row space of `C_{r,m}(f)` is identified with `D_r(f)`.

### Lemma 2.1 — residual catalectic rank

\[
\dim\mathcal D_m(P_n-R)
\ge
\binom nm^2+h-a-b.
\tag{2.1}
\]

### Proof

Let

\[
A=C_{r,m}(P_n),
\qquad
B=C_{r,m}(R).
\]

The horizontal concatenation has rank

\[
\operatorname{rank}[A\ B]
=
\dim(E_m+H_m)
=
\binom nm^2+h-a.
\]

The vertical concatenation has rank

\[
\operatorname{rank}
\begin{bmatrix}A\\B\end{bmatrix}
=
\dim(E_r+H_r)
=
\binom nr^2+h-b.
\]

Since

\[
\binom nr=\binom nm,
\]

the double-quotient rank inequality gives

\[
\begin{aligned}
\operatorname{rank}(A-B)
&\ge
\operatorname{rank}[A\ B]
+
\operatorname{rank}
\begin{bmatrix}A\\B\end{bmatrix}
-
\operatorname{rank}A-\operatorname{rank}B\\
&=
\binom nm^2+h-a-b.
\end{aligned}
\]

The image of `A-B` is `D_m(P_n-R)`. ∎

### Lemma 2.2 — output-side quotient prolongation

\[
\dim(E_m+H_m)^{(1)}
\le
\binom n{m+1}^2+N(h-a).
\tag{2.2}
\]

### Proof

Take all first derivatives of an element of `(E_m+H_m)^(1)` and reduce them modulo `E_m`. The kernel is `E_m^(1)`, so there is an injection

\[
(E_m+H_m)^{(1)}/E_m^{(1)}
\hookrightarrow
(E_m+H_m)/E_m\otimes V^*.
\]

The quotient on the right has dimension `h-a`, while

\[
\dim E_m^{(1)}
=
\dim\mathcal D_{m+1}(P_n)
=
\binom n{m+1}^2.
\]

This gives (2.2). ∎

### Proposition 2.3 — complementary-intersection residual bound

\[
\boxed{
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-Nb.
}
\tag{2.3}
\]

### Proof

Let

\[
G=\mathcal D_m(P_n-R).
\]

Then `G subset E_m+H_m`, hence

\[
G^{(1)}\subseteq(E_m+H_m)^{(1)}.
\]

By the Koszul kernel-prolongation formula, Lemma 2.1, and Lemma 2.2,

\[
\begin{aligned}
\operatorname{rank}K_m(P_n-R)
&=N\dim G-\dim G^{(1)}\\
&\ge
N\left(\binom nm^2+h-a-b\right)
-
\left(\binom n{m+1}^2+N(h-a)\right)\\
&=
N\binom nm^2-inom n{m+1}^2-Nb\\
&=A_{n,m}-Nb.
\end{aligned}
\]

The output intersection `a` and the catalectic rank `h` cancel. Only the complementary derivative-space intersection `b` remains. ∎

This cancellation is the main structural advance over the even-only presentation: self-transpose middle catalectics are convenient but not necessary.

## 3. Multidimensional shadows at the complementary degree

The permanent space

\[
E_r=\mathcal D_r(P_n)
\]

has the multiplicity-free row-column torus basis

\[
\{P_{I,J}:I,J\in\tbinom{[n]}r\}.
\]

For a nonzero subspace

\[
S\subseteq E_r,
\qquad
s=\dim S,
\]

write

\[
s=\binom yr^2
\]

with the unique real `y>=r`.

A generic row-column one-parameter subgroup degenerates `S` to a coordinate family

\[
\mathcal F\subseteq
\binom{[n]}r\times\binom{[n]}r
\]

of size `s`. The first derivatives of the coordinate limit are indexed by the simultaneous lower shadow of `F`. Rank cannot increase under specialization, so Bukh's multidimensional Kruskal--Katona theorem gives

\[
\boxed{
\dim\partial S
\ge
\binom y{r-1}^2.
}
\tag{3.1}
\]

Now let

\[
R=T_1+\cdots+T_q
\]

be a sum of `q` Chow terms and set

\[
S=E_r\cap\mathcal D_r(R).
\]

Since

\[
\partial S
\subseteq
\mathcal D_{r-1}(R)
\]

and one Chow term has degree-`(r-1)` derivative-space dimension at most `binom(n,r-1)`, one has

\[
\dim\partial S
\le
q\binom n{r-1}.
\tag{3.2}
\]

Combining (3.1) and (3.2) yields the following cap.

### Proposition 3.1

If `x>=r` satisfies

\[
q\binom n{r-1}
\le
\binom x{r-1}^2,
\tag{3.3}
\]

then

\[
\boxed{
\dim\bigl(E_r\cap\mathcal D_r(R)\bigr)
\le
\binom xr^2.
}
\tag{3.4}
\]

## 4. General theorem

For `x in [r,n]`, define

\[
q_{n,m}(x)
=
\left\lfloor
\frac{\binom{x}{r-1}^2}{\binom n{r-1}}
\right\rfloor,
\qquad
s_{n,m}(x)
=
\left\lfloor\binom xr^2\right\rfloor.
\tag{4.1}
\]

### Theorem 4.1 — general multidimensional-shadow bound

For every `n>=4`, every `2<=m<=n-2`, and every `x in [n-m,n]` with `q_{n,m}(x)>=1`,

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge
\max\left\{
L_K(n),
q_{n,m}(x)
+
\left\lceil
\frac{A_{n,m}-n^2s_{n,m}(x)}{B_{n,m}}
\right\rceil
\right\},
}
\tag{4.2}
\]

provided the residual numerator is positive.

### Proof

The global first-Koszul lower bound `L_K(n)` is at least the central binomial coefficient. Also

\[
q_{n,m}(x)
\le
\binom n{r-1}
\le
\binom n{\lfloor n/2\rfloor}
\le
L_K(n).
\]

Thus every hypothetical decomposition contains at least `q=q_{n,m}(x)` terms. Fix any `q` of them and call their sum `R`.

Proposition 3.1 gives

\[
b
=
\dim\bigl(E_r\cap\mathcal D_r(R)\bigr)
\le
s_{n,m}(x).
\]

Proposition 2.3 therefore gives

\[
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-n^2s_{n,m}(x).
\]

The residual is a sum of the remaining Chow terms, each of Koszul rank at most `B_{n,m}`. Hence the number of residual terms is at least the ceiling in (4.2). Adding the fixed `q` terms proves the result. ∎

## 5. Exact reviewed certificates

The following values are certified by rational witnesses stored in `src/permanent_chow_rank/multishadow.py`.

| `n` | output `m` | complement `r` | global Koszul bound | fixed `q` | intersection cap | residual terms | new lower bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 7 | 2 | 6 | 6 | **8** |
| 5 | 2 | 3 | 11 | 4 | 19 | 9 | **13** |
| 6 | 3 | 3 | 21 | 4 | 40 | 19 | **23** |
| 7 | 3 | 4 | 36 | 13 | 274 | 28 | **41** |
| 8 | 4 | 4 | 71 | 12 | 496 | 64 | **76** |
| 9 | 4 | 5 | 127 | 43 | 3,607 | 98 | **141** |
| 10 | 5 | 5 | 253 | 42 | 7,084 | 225 | **267** |
| 11 | 5 | 6 | 463 | 175 | 60,479 | 331 | **506** |
| 12 | 6 | 6 | 925 | 179 | 125,640 | 789 | **968** |
| 13 | 6 | 7 | 1,718 | 668 | 907,508 | 1,185 | **1,853** |
| 14 | 7 | 7 | 3,434 | 623 | 1,673,882 | 2,945 | **3,568** |
| 15 | 7 | 8 | 6,440 | 2,388 | 12,460,405 | 4,491 | **6,879** |
| 16 | 8 | 8 | 12,875 | 2,422 | 25,470,785 | 10,890 | **13,312** |

For odd `n=2k+1`, the reviewed certificate uses

\[
m=k,
\qquad
r=k+1.
\]

Thus the strongest reviewed odd-degree instances deliberately use the lower output degree and control the larger complementary derivative space. This is why the asymmetric formulation is stronger than simply applying the even argument at `m=ceil(n/2)`.

### Corollary 5.1

\[
\operatorname{ChowRank}(\operatorname{perm}_5)\ge13,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_7)\ge41,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_9)\ge141.
\]

The `n=5` general bound is weaker than the special small-`n` computer-assisted lower bounds under review. It is valuable because it does not use the `n=5` finite-state architecture.

## 6. Relationship to earlier repository results

1. `docs/general_n_koszul_bounds.md` gives the base `L_K(n)`.
2. `docs/shadow_removal_asymptotics.md` proves a zero-intersection removal theorem.
3. `docs/even_n_multidimensional_shadow_bound.md` is the even, self-transpose special case of Theorem 4.1 and contains the current even-degree asymptotic analysis.
4. The present theorem strictly improves the recorded general lower bounds for every reviewed `n>=5`.

The ordinary shadow-removal theorem remains useful because its logic is different and can apply at non-middle derivative degrees without tracking a nonzero intersection. It is not deleted.

## 7. Claim boundary

The theorem does not establish:

- exact Glynn optimality;
- a border Chow-rank improvement beyond the determinantal Koszul bound;
- optimality of the frozen rational witnesses;
- equality cases for the subspace shadow degeneration;
- literature novelty of the combined argument.

For `n=6`, the exact problem remains

\[
23\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 8. References and reproduction

Combinatorial input:

- Boris Bukh, *Multidimensional Kruskal--Katona theorem*, arXiv:1009.2375.

Chow/Koszul context checked:

- Yonghui Guan, *Flattenings and Koszul Young flattenings arising in complexity theory*, arXiv:1510.00886.
- Yonghui Guan, *Equations for secant varieties of Chow varieties*, arXiv:1602.04275.

Reproduce the exact table with:

```bash
python -m unittest tests.test_multishadow -v
python scripts/generate_multishadow_bounds.py
```
