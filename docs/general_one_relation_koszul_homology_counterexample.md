# One-relation counterexample to the raw Koszul-homology cap

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_ROUTE_COUNTEREXAMPLE`,
`ACTUAL_DERIVATIVE_SPACES`, `EXACT_SPARSE_REPLAYED`.

The independent-factor theorem for the two-step quotient complex is exact, but
it does not extend uniformly to degenerate degree-`n` Chow terms. For every
`n>=5`, let

\[
L=\langle x_1,\ldots,x_{n-1}\rangle
\]

and consider the full-circuit Chow term

\[
T_n=x_1\cdots x_{n-1}(x_1+\cdots+x_{n-1}).
\tag{0.1}
\]

Its actual factor span has dimension `n-1`. Take the identity quotient on
that span and the actual derivative-space complex

\[
\mathcal D_3(T_n)
\longrightarrow
L\otimes\mathcal D_2(T_n)
\longrightarrow
\bigwedge^2L\otimes\mathcal D_1(T_n).
\tag{0.2}
\]

Then the middle homology has dimension

\[
\boxed{\dim H^1(0.2)=\binom n2.}
\tag{0.3}
\]

The independent `n`-factor cap from the parent theorem, evaluated at quotient
rank `d=n-1` and output degree `k=2`, is only

\[
 d\binom{n-d}{k-1}=n-1.
\tag{0.4}
\]

Hence the excess is

\[
\boxed{
\binom n2-(n-1)=\binom{n-1}{2}>0.
}
\tag{0.5}
\]

Thus raw first Koszul relation homology is not a uniform one-Chow-term
invariant. This result does not affect the exact independent-factor theorem;
it rejects only its proposed extension to arbitrary repeated or dependent
factors.

## 1. The actual apolar Hilbert function

Put `r=n-1`, let

\[
R=k[y_1,\ldots,y_r],
\qquad
A_n=R/T_n^\perp.
\]

The algebra `A_n` is Artinian Gorenstein of codimension `r` and socle degree
`n`. Its Hilbert function is

\[
\boxed{
\dim(A_n)_j=
\begin{cases}
1,&j=0,n,\\
n-1,&j=1,n-1,\\
\binom nj,&2\le j\le n-2.
\end{cases}}
\tag{1.1}
\]

This is an actual-space calculation, not an identification with the full
formal squarefree subproduct span.

To prove the interior row, write

\[
X=x_1\cdots x_r,
\qquad
S=x_1+\cdots+x_r,
\qquad
T_n=XS.
\]

For every `j`-subset `I` of `[r]`,

\[
\partial_I T_n
=
\frac{X}{\prod_{i\in I}x_i}
\left(S+\sum_{i\in I}x_i\right).
\tag{1.2}
\]

When `2<=j<=r-1`, the complement of `I` is nonempty. Equation (1.2)
contains a squared monomial which identifies `I`, so these
`binom(r,j)` derivatives are independent.

For every `(j-1)`-subset `K` and any `i in K`,

\[
\partial_i^2\partial_{K\setminus\{i\}}T_n
=2\prod_{a\notin K}x_a.
\tag{1.3}
\]

These give `binom(r,j-1)` independent squarefree outputs. They are
independent from the first family because every nonzero linear combination of
(1.2) retains one of its identifying squared monomials. Therefore

\[
\dim(A_n)_j
\ge
\binom rj+\binom r{j-1}
=\binom nj.
\]

The formal `n`-label squarefree algebra gives the reverse inequality. The
boundary degrees follow from conciseness and Gorenstein symmetry, proving
(1.1).

## 2. Cubic generators

Equation (1.1) gives

\[
\dim(A_n)_2=\binom n2
=\dim\operatorname{Sym}^2(k^{n-1}).
\]

Thus

\[
(T_n^\perp)_2=0.
\tag{2.1}
\]

For `n>=5`, degree three is an interior degree, and

\[
\dim(A_n)_3=\binom n3.
\]

Hence the degree-three apolar ideal has dimension

\[
\begin{aligned}
\dim(T_n^\perp)_3
&=\binom{n+1}{3}-\binom n3\\
&=\binom n2.
\end{aligned}
\tag{2.2}
\]

Because there are no quadratic generators, all elements in (2.2) are minimal.
Therefore

\[
\boxed{\beta_{1,3}^R(A_n)=\binom n2.}
\tag{2.3}
\]

## 3. Gorenstein duality identifies the required homology

The last shift in the minimal `R`-free resolution of `A_n` is

\[
 n+r=2n-1.
\]

Self-duality of an Artinian Gorenstein resolution gives

\[
\beta_{i,j}^R(A_n)
=
\beta_{r-i,\,2n-1-j}^R(A_n).
\tag{3.1}
\]

Applying (3.1) to (2.3) yields

\[
\boxed{
\beta_{n-2,\,2n-4}^R(A_n)=\binom n2.
}
\tag{3.2}
\]

The Koszul chain group in homological degree `n-2` and internal degree
`2n-4` is

\[
\bigwedge^{n-2}L^*\otimes(A_n)_{n-2}.
\]

Using

\[
\bigwedge^{n-2}L^*
\simeq L\otimes\det(L^*)
\]

identifies the three adjacent chain groups, up to the harmless determinant
factor, with

\[
(A_n)_{n-3}
\longrightarrow
L\otimes(A_n)_{n-2}
\longrightarrow
\bigwedge^2L\otimes(A_n)_{n-1}.
\tag{3.3}
\]

Under inverse-system duality `(A_n)_{n-j}=D_j(T_n)`, (3.3) is exactly
(0.2). Equations (3.2)--(3.3) prove (0.3).

The two differential ranks are also forced:

\[
\operatorname{rank}d_0=\binom n3,
\qquad
\operatorname{rank}d_1=2\binom n3.
\tag{3.4}
\]

The first equality follows because an element below the socle killed by all
linear forms is zero; the second follows from the middle dimension,
(0.3), and the complex identity.

## 4. Consequence for the general-`n` program

The parent independent-term theorem remains exact:

\[
\max_{\operatorname{rank}P=d}
\dim H^1_{n,k}(P)
=d\binom{n-d}{k-1}
\]

for `z_1*...*z_n`. The full-circuit term (0.1) shows that this value is not a
uniform cap over the Chow variety. At the first tested degree it misses by a
quadratic amount:

\[
\binom{n-1}{2}.
\]

A corrected candidate cannot merely add a linear factor-rank deficit. It must
either

1. quotient the circuit-generated apolar syzygies before taking homology; or
2. attach a realizability defect which controls the minimal cubic generators
   and is compatible with sums and factor filtration.

No permanent-side calculation is justified until this one-term obstruction is
removed.

## 5. Exact replay

The primary replay reconstructs the Hilbert row, the cubic-generator count,
the Gorenstein-dual Betti position, both differential ranks, and the gap for
`5<=n<=12`.

The independent program embeds the full-circuit algebra in the squarefree
`n`-label algebra, constructs both sparse Koszul matrices, checks their
composition is zero, and row-reduces them modulo `1,000,003` for `5<=n<=9`.
It imports none of the primary implementation.

```bash
python scripts/general_one_relation_koszul_homology_counterexample.py \
  --verify-json data/general_one_relation_koszul_homology_counterexample.json
python scripts/general_one_relation_koszul_homology_counterexample_independent.py
python -m unittest \
  tests.test_general_one_relation_koszul_homology_counterexample -v
```

## 6. Strict boundary

```text
independent squarefree quotient-symbol theorem       RETAINED
independent first-Koszul H1 theorem                  RETAINED
uniform extension to dependent Chow terms            FALSE
raw H1 as a uniform one-term Chow invariant          REJECTED
new ordinary Chow-rank lower bound                   NO
border-rank improvement                              NO
general Glynn optimality                             OPEN
```
