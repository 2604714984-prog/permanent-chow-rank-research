# Common-quotient rigidity excludes the fixed-four endpoint `b=27`

## Status

`PROOF_DRAFT_COMPLETE` — this is a characteristic-zero linear-algebra consequence of equality in the fixed-four projection bound. The revised arithmetic frontier is replayed by

```text
scripts/n6_fixed_four_coupled_frontier.py
```

External peer review and an exhaustive literature-novelty review have not been performed.

## 1. Setup

Assume, for contradiction, that

\[
P=\operatorname{perm}_6
=T_1+\cdots+T_{23}.
\]

Fix four terms and write

\[
R=T_1+T_2+T_3+T_4,
\qquad
Q=P-R.
\]

At quadratic output degree put

\[
E=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+G_2+G_3+G_4.
\]

At central output degree put

\[
E_3=\mathcal D_3(P),
\qquad
H_3=\mathcal D_3(R),
\]

\[
b=\dim(E_3\cap H_3),
\qquad
h=\dim H_3.
\]

The raw fixed-four frontier gives

\[
20\le b\le27,
\qquad
h\le2b-20.
\tag{1.1}
\]

Suppose

\[
b=27.
\tag{1.2}
\]

The exact shadow and defect budgets force, for every `i`,

\[
\dim G_i=15,
\qquad
K_i:=E\cap G_i,
\qquad
\dim K_i=3.
\tag{1.3}
\]

They also force

\[
X:=E\cap U,
\qquad
\dim X=48.
\tag{1.4}
\]

Indeed, the 27-dimensional central intersection has quadratic shadow at least 48, while the projection lemma gives `dim X<=48`.

## 2. Equality in every omitted-factor projection

Let

\[
\pi:G_1\oplus G_2\oplus G_3\oplus G_4
\longrightarrow U
\]

be summation, and choose a section

\[
\sigma:X\longrightarrow G_1\oplus G_2\oplus G_3\oplus G_4,
\qquad
\pi\sigma=\operatorname{id}_X.
\]

For each `j`, let `p_hat_j` be projection onto the other three factors.

### Lemma 2.1

For every `j`,

\[
\operatorname{rank}(p_{\widehat j}\sigma)=45,
\qquad
\ker(p_{\widehat j}\sigma)=K_j.
\tag{2.1}
\]

For every `k in K_j`,

\[
\sigma(k)=(0,\ldots,0,k,0,\ldots,0)
\tag{2.2}
\]

with `k` in the `j`th coordinate.

### Proof

The target has dimension `3*15=45`, so the kernel has dimension at least three. If `x` lies in the kernel, `sigma(x)` has only a `G_j` component. Its sum is `x`, hence

\[
x\in E\cap G_j=K_j.
\]

The kernel has dimension at most three, so equality holds throughout. The sole coordinate equals its sum, proving (2.2). ∎

### Corollary 2.2

\[
\boxed{
K_1\oplus K_2\oplus K_3\oplus K_4
\subseteq E.
}
\tag{2.3}
\]

### Proof

If `sum k_i=0` with `k_i in K_i`, linearity and (2.2) give

\[
0
=
\sigma(0)
=
\sum_i\sigma(k_i)
=
(k_1,k_2,k_3,k_4)
\]

in the external direct sum. ∎

## 3. The common twelve-dimensional quotient

Let

\[
M=\operatorname{Sym}^2V/E,
\qquad
\overline G_i=(G_i+E)/E.
\]

Each `overline G_i` has dimension 12. Quotienting `sigma(X)` by the four direct `K_i` gives

\[
Y
=
\sigma(X)/(K_1\oplus K_2\oplus K_3\oplus K_4)
\subseteq
\overline G_1\oplus\cdots\oplus\overline G_4,
\qquad
\dim Y=36.
\tag{3.1}
\]

### Lemma 3.1

Every triple projection is an isomorphism

\[
Y
\xrightarrow{\ \sim\ }
\bigoplus_{i\ne j}\overline G_i.
\tag{3.2}
\]

### Proof

Surjectivity follows from Lemma 2.1. If a class maps to zero, subtract from its representative the three visible coordinate vectors in the corresponding `K_i`; equation (2.2) keeps the result inside `sigma(X)`. The remaining representative has only the `j`th coordinate and therefore comes from `K_j`, so its class is zero. ∎

Every tuple in `Y` sums to zero in `M`.

### Proposition 3.2 — common-quotient rigidity

\[
\boxed{
\overline G_1
=
\overline G_2
=
\overline G_3
=
\overline G_4
=:W,
\qquad
\dim W=12,
}
\tag{3.3}
\]

and

\[
\boxed{
Y
=
\left\{
(w_1,w_2,w_3,w_4)\in W^4:
 w_1+w_2+w_3+w_4=0
\right\}.
}
\tag{3.4}
\]

### Proof

Fix `i ne j` and `w in overline G_i`. Under the isomorphism omitting `j`, prescribe `w` in coordinate `i` and zero in the other two visible coordinates. The hidden coordinate `w_j` satisfies `w+w_j=0` in `M`, so `w in overline G_j`. Symmetry gives equality of all four images. The sum-zero subspace has dimension 36, equal to `dim Y`. ∎

## 4. The quadratic derivative spaces are direct

Since `(U+E)/E=W`,

\[
\dim(U+E)=225+12=237.
\]

Using `dim(E intersect U)=48`,

\[
\dim U=237+48-225=60.
\]

But the sum of the four individual dimensions is also 60. Hence

\[
\boxed{
U=G_1\oplus G_2\oplus G_3\oplus G_4.
}
\tag{4.1}
\]

## 5. Central derivative dimensions and directness

For each `i`, put

\[
C_i=\mathcal D_3(T_i).
\]

The following term-profile fact is proved and exactly replayed in

```text
docs/n6_b26_one_relation_exclusion.md
scripts/n6_fixed_four_coupled_frontier.py
```

> If a degree-six Chow term has quadratic derivative dimension 15, then its cubic derivative dimension is 20 and its cubic derivative space contains no nonzero pure cube.

This statement does **not** assume that the six factors are independent. If the factor span has dimension five, the normal form

\[
x_1x_2x_3x_4x_5(x_1+\cdots+x_s)
\]

has quadratic/cubic dimensions

```text
s=1: 11/14
s=2: 11/14
s=3: 13/18
s=4: 14/20
s=5: 15/20.
```

Thus (1.3) gives

\[
\dim C_i=20
\qquad
\text{for every }i.
\tag{5.1}
\]

### Lemma 5.1

\[
\boxed{
C_1\oplus C_2\oplus C_3\oplus C_4.
}
\tag{5.2}
\]

### Proof

Differentiate a relation `sum c_i=0`, with `c_i in C_i`. Every derivative lies in the direct sum of the `G_i`, so every derivative of every `c_i` is zero. Homogeneity and characteristic zero give `c_i=0`. ∎

Let

\[
A_i=C_{3,3}(T_i),
\qquad
A=C_{3,3}(R)=\sum_iA_i.
\]

The middle catalectics are symmetric, so both the image and row space of `A_i` equal `C_i` under the standard monomial pairing.

### Proposition 5.2

\[
\boxed{
\mathcal D_3(R)
=C_1\oplus C_2\oplus C_3\oplus C_4,
\qquad
h=80.
}
\tag{5.3}
\]

### Proof

If `Ax=0`, directness of the image spaces gives `A_i x=0` for every `i`. Hence

\[
\ker A=\bigcap_i\ker A_i.
\]

The annihilator of this intersection is the direct sum of the row spaces. Therefore

\[
\operatorname{rank}A
=
\sum_i\dim C_i
=80.
\]

Its image is contained in the 80-dimensional direct sum of the `C_i`, so the displayed image equality follows. ∎

## 6. Contradiction and revised frontier

At `b=27`, equation (1.1) gives

\[
h\le34.
\]

Proposition 5.2 gives

\[
h=80.
\]

This contradiction proves:

### Theorem 6.1

Under a hypothetical 23-term Chow decomposition of `perm_6`,

\[
\boxed{b\le26.}
\]

All eight raw states with `b=27` are impossible.

This result has since been strengthened: `docs/n6_b26_one_relation_exclusion.md` also excludes the seven states with `b=26`, leaving the current range

\[
20\le b\le25.
\]

## 7. Claim boundary

The endpoint exclusions do not yet prove

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

The current frontier has 21 states, including ten structural states and eight states conditional on relative-prolongation caps.
