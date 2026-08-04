# Exact first-Koszul additivity after removing one `n=6` Chow term

## Status

`PROOF_DRAFT_COMPLETE` — this is a corollary of `docs/n6_universal_single_term_full_gain.md` and the multiplicity-free permanent derivative basis. External peer review and a complete literature-novelty review have not been performed.

## 1. Central derivative spaces are disjoint

Let

\[
P=\operatorname{perm}_6,
\qquad
E_3=\mathcal D_3(P).
\]

The row-column torus acts on `E_3` with the multiplicity-free basis of all `3 x 3` subpermanents

\[
P_{I,J},
\qquad
I,J\in\binom{[6]}3.
\]

### Lemma 1.1

Every nonzero cubic

\[
g\in E_3
\]

has essential-variable dimension at least nine.

### Proof

Choose a generic row-column one-parameter subgroup. Because the basis weights are distinct, `g` degenerates to a nonzero scalar multiple of one basis vector `P_{I,J}`. The first catalectic rank cannot increase under specialization. A `3 x 3` permanent has nine linearly independent first derivatives, so

\[
\operatorname{rank}C_{1,2}(g)
\ge
\operatorname{rank}C_{1,2}(P_{I,J})
=9.
\]

The rank of `C_{1,2}(g)` is the dimension of the essential-variable space of `g`. ∎

Now let

\[
T=\ell_1\cdots\ell_6
\]

be any degree-six Chow term and put

\[
F_3=\mathcal D_3(T).
\]

Every element of `F_3` belongs to

\[
\operatorname{Sym}^3L,
\qquad
L=\operatorname{span}\{\ell_1,\ldots,\ell_6\},
\qquad
\dim L\le6.
\]

Therefore Lemma 1.1 gives

\[
\boxed{
E_3\cap F_3=0.
}
\tag{1.1}
\]

This holds for independent, dependent, and repeated factors.

## 2. Exact residual additivity

Let

\[
A=K_3(P),
\qquad
B=K_3(T).
\]

The row-space containment for the first-Koszul flattening gives

\[
\operatorname{row}A
\subseteq
E_3\otimes V^*,
\qquad
\operatorname{row}B
\subseteq
F_3\otimes V^*.
\]

Equation (1.1) implies

\[
\operatorname{row}A\cap\operatorname{row}B=0.
\tag{2.1}
\]

The universal single-term theorem gives

\[
\operatorname{im}A\cap\operatorname{im}B=0.
\tag{2.2}
\]

Apply the double-quotient rank inequality to `A-alpha B`, where `alpha` is nonzero. Equations (2.1) and (2.2) imply that both the horizontal and vertical concatenations have rank

\[
\operatorname{rank}A+\operatorname{rank}B.
\]

Hence

\[
\operatorname{rank}(A-\alpha B)
\ge
\operatorname{rank}A+\operatorname{rank}B.
\]

The reverse inequality is ordinary rank subadditivity. Therefore:

### Theorem 2.1

For every nonzero scalar `alpha` and every nonzero degree-six Chow term `T`,

\[
\boxed{
\operatorname{rank}K_3(P-\alpha T)
=
14175+\operatorname{rank}K_3(T).
}
\tag{2.3}
\]

The equality is uniform over all factor degenerations.

## 3. Numerical range and limitation

The rank of one degree-six Chow term ranges from

\[
35
\]

for a sixth power to

\[
705
\]

for six independent factors. Thus (2.3) gives

\[
14210
\le
\operatorname{rank}K_3(P-\alpha T)
\le
14880.
\]

This exact one-term additivity does not raise the current universal Chow-rank lower bound above `23`. A hypothetical 23-term decomposition leaves 22 terms after removing one term, and their crude capacity

\[
22\cdot705=15510
\]

still exceeds the largest residual rank in (2.3).

The next obstruction must therefore be coupled: one needs a lower bound for the quotient rank of the single map

\[
K_3(T_1+\cdots+T_q)
\]

modulo `K_3(P)`, not a sum of separate one-term bounds.
