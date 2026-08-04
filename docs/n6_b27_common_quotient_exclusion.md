# Common-quotient rigidity excludes the fixed-four endpoint `b=27`

## Status

`PROOF_DRAFT_COMPLETE` — this is a characteristic-zero linear-algebra consequence of the equality case in the fixed-four projection bound. It does not use a new finite computation. The revised 28-state arithmetic frontier is replayed by

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

At quadratic output degree, put

\[
E=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+G_2+G_3+G_4.
\]

At central output degree, put

\[
E_3=\mathcal D_3(P),
\qquad
H_3=\mathcal D_3(R),
\]

and

\[
b=\dim(E_3\cap H_3),
\qquad
h=\dim H_3.
\]

The fixed-four frontier proves

\[
20\le b\le27,
\qquad
h\le2b-20.
\tag{1.1}
\]

Suppose now that

\[
b=27.
\tag{1.2}
\]

The exact shadow and defect budgets force

\[
\dim G_i=15,
\qquad
K_i:=E\cap G_i,
\qquad
\dim K_i=3
\tag{1.3}
\]

for every `i`. They also force

\[
X:=E\cap U
\]

to have dimension 48. Indeed, the 27-dimensional central intersection has quadratic shadow at least 48, while the fixed-four projection lemma gives `dim X<=48`.

The purpose of this note is to exploit equality in that projection lemma rather than merely record it.

## 2. Equality in every omitted-factor projection

Let

\[
\pi:G_1\oplus G_2\oplus G_3\oplus G_4
\longrightarrow
U
\]

be the summation map. Choose a linear section

\[
\sigma:X\longrightarrow
G_1\oplus G_2\oplus G_3\oplus G_4
\]

with

\[
\pi\sigma=\operatorname{id}_X.
\]

For each `j`, let

\[
p_{\widehat j}
\]

be projection onto the three factors other than `G_j`.

### Lemma 2.1 — all four projection bounds are equalities

For every `j`,

\[
\operatorname{rank}(p_{\widehat j}\sigma)=45,
\qquad
\ker(p_{\widehat j}\sigma)=K_j.
\tag{2.1}
\]

Moreover, for every `k in K_j`,

\[
\sigma(k)=(0,\ldots,0,k,0,\ldots,0)
\tag{2.2}
\]

with `k` in the `j`th coordinate.

### Proof

The target of `p_hat_j sigma` has dimension

\[
3\cdot15=45,
\]

so its rank is at most 45. If `x` lies in its kernel, then `sigma(x)` has only a `G_j` component, say `g_j`. Since `pi sigma(x)=x`, one has

\[
x=g_j\in E\cap G_j=K_j.
\]

Thus the kernel has dimension at most three. Rank-nullity and `dim X=48` give

\[
\dim\ker(p_{\widehat j}\sigma)
\ge48-45=3.
\]

Both inequalities are equalities. For a kernel vector, the sole coordinate is its sum, hence (2.2). ∎

### Corollary 2.2 — the four permanent intersections are direct

\[
\boxed{
K_1\oplus K_2\oplus K_3\oplus K_4
\subseteq E.
}
\tag{2.3}
\]

### Proof

Suppose

\[
k_1+k_2+k_3+k_4=0,
\qquad
k_i\in K_i.
\]

By linearity of the section and equation (2.2),

\[
0
=
\sigma(0)
=
\sum_i\sigma(k_i)
=
(k_1,k_2,k_3,k_4)
\]

in the external direct sum. Hence every `k_i` is zero. ∎

## 3. A common twelve-dimensional quotient

Let

\[
M=\operatorname{Sym}^2V/E.
\]

For each `i`, the natural image

\[
\overline G_i=(G_i+E)/E
\subseteq M
\]

has dimension

\[
15-3=12.
\]

By Corollary 2.2, the direct sum of the four `K_i` is contained in `sigma(X)`. Quotienting gives a 36-dimensional space

\[
Y
=
\sigma(X)/(K_1\oplus K_2\oplus K_3\oplus K_4)
\subseteq
\overline G_1\oplus\cdots\oplus\overline G_4.
\tag{3.1}
\]

### Lemma 3.1 — every triple projection is an isomorphism

For each `j`, projection gives

\[
Y
\xrightarrow{\ \sim\ }
\bigoplus_{i\ne j}\overline G_i.
\tag{3.2}
\]

### Proof

Lemma 2.1 says that the corresponding projection before quotienting is surjective onto the 45-dimensional external direct sum of the three `G_i`. Its kernel is exactly `K_j`.

If a class in `Y` maps to zero, choose a representative `sigma(x)`. Its three visible coordinates lie in the corresponding `K_i`. Subtract their coordinate vectors, which belong to `sigma(X)` by (2.2). The resulting representative has only the `j`th coordinate and therefore comes from `K_j`; its class in `Y` is zero. Thus the induced map is injective. It is also surjective, and both spaces have dimension 36. ∎

Every tuple in `Y` sums to zero in `M`, because its unquotiented sum belongs to `X subset E`.

### Proposition 3.2 — common-quotient rigidity

The four quotient images coincide:

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
\dim W=12.
}
\tag{3.3}
\]

Under these identifications,

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

Fix distinct indices `i` and `j` and let `w in overline G_i`. Use the isomorphism (3.2) for the projection omitting `j`. Prescribe coordinate `i` to be `w` and the other two visible coordinates to be zero. There is a unique tuple in `Y`; let its hidden `j`th coordinate be `w_j`. Since the tuple sums to zero in `M`,

\[
w+w_j=0.
\]

Thus `w` belongs to `overline G_j`. Symmetry gives equality. The sum-zero subspace of `W^4` has dimension 36, equal to `dim Y`, proving (3.4). ∎

## 4. The four quadratic derivative spaces are a direct sum

Since all quotient images equal `W`,

\[
(U+E)/E=W
\]

has dimension 12. Therefore

\[
\dim(U+E)=225+12=237.
\]

Using

\[
\dim(E\cap U)=48,
\]

one obtains

\[
\dim U
=
237+48-225
=60.
\]

But

\[
\sum_{i=1}^4\dim G_i=4\cdot15=60.
\]

Hence:

### Corollary 4.1

\[
\boxed{
U=G_1\oplus G_2\oplus G_3\oplus G_4.
}
\tag{4.1}
\]

This is much stronger than pairwise disjointness of the three-dimensional `K_i`.

## 5. Direct quadratic spaces forbid central coupling loss

For each `i`, let

\[
C_i=\mathcal D_3(T_i).
\]

Because `dim G_i=15`, the six factors of `T_i` are independent and

\[
\dim C_i=20.
\]

### Lemma 5.1 — the four central derivative spaces are direct

\[
\boxed{
C_1\oplus C_2\oplus C_3\oplus C_4.
}
\tag{5.1}
\]

### Proof

Suppose

\[
c_1+c_2+c_3+c_4=0,
\qquad
c_i\in C_i.
\]

Differentiate in an arbitrary variable direction. Then

\[
\partial c_i\in G_i.
\]

Corollary 4.1 makes the `G_i` a direct sum, so every first derivative of every `c_i` vanishes. A homogeneous cubic with all first derivatives zero is zero in characteristic zero. Thus all `c_i` vanish. ∎

For each `i`, let

\[
A_i=C_{3,3}(T_i),
\qquad
A=C_{3,3}(R)=A_1+A_2+A_3+A_4.
\]

Under the standard monomial pairing, the middle catalectic is symmetric, so

\[
\operatorname{im}A_i=C_i,
\qquad
\operatorname{row}A_i=C_i.
\tag{5.2}
\]

### Proposition 5.2 — no central coupling loss

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

If `Ax=0`, then

\[
A_1x+A_2x+A_3x+A_4x=0.
\]

Each summand lies in `C_i`, and the `C_i` are direct by Lemma 5.1. Hence

\[
A_ix=0
\qquad
\text{for every }i.
\]

Therefore

\[
\ker A=\bigcap_i\ker A_i.
\]

The annihilator of this intersection is the sum of the row spaces. By (5.2) and Lemma 5.1,

\[
\operatorname{codim}\ker A
=
\dim\left(\sum_i\operatorname{row}A_i\right)
=
\sum_i\dim C_i
=80.
\]

Thus `rank A=80`. Its image is contained in the 80-dimensional direct sum of the `C_i`, so equality of images follows. ∎

This is the degree-six analogue of the direct-sum coupling lemma used in the corrected `n=5` proof. It is applied only after directness has been independently established.

## 6. Contradiction and revised frontier

At `b=27`, the residual central-catalectic inequality (1.1) gives

\[
h\le2\cdot27-20=34.
\]

Proposition 5.2 gives

\[
h=80.
\]

Therefore

\[
80\le34,
\]

a contradiction.

### Theorem 6.1 — endpoint exclusion

Under a hypothetical 23-term Chow decomposition of `perm_6`, the fixed-four central intersection satisfies

\[
\boxed{
20\le b\le26.
}
\tag{6.1}
\]

All eight states with `b=27` are impossible.

The surviving integer frontier is

\[
20\le b\le26,
\qquad
0\le d\le b-20,
\]

and has

\[
1+2+\cdots+7=28
\]

states. Their exact partition is:

```text
3 states:  already strict with Gamma>=0
5 states:  close if p<=23
5 states:  close if p<=59
15 states: structural exclusion or a stronger invariant required
```

The maximum remaining quotient-gain requirement is now

\[
\boxed{157},
\]

attained at `b=26`, rather than 193 at the eliminated endpoint.

## 7. Relation to the extremal six-plane classification

The endpoint also forces each factor span into the equality locus classified in

```text
docs/n6_extremal_six_plane_classification.md
```

but that geometric classification is not needed for Theorem 6.1. The contradiction follows already from equality in all four projection bounds.

The six-plane theorem remains relevant for the new top layer `b=26`, where the per-omitted-factor defect budget is one and almost all individual spaces remain extremal.

## 8. Claim boundary and next target

This theorem does not prove

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

Fifteen structural states remain, and ten states still require relative-prolongation caps `23` or `59`.

The next target is the `b=26` near-equality classification. The defect inequalities permit only one unit of loss in each omitted-factor projection, so the possible distributions of

\[
\varepsilon_i=15-\dim G_i,
\qquad
\alpha_i=3-\dim(E\cap G_i)
\]

are finite and small. That classification should be completed before any broad computational search.

## 9. Reproduction

Run

```bash
python scripts/n6_fixed_four_coupled_frontier.py
python -m unittest tests.test_n6_fixed_four_coupled_frontier -v
```

Expected current outputs include

```text
raw_state_count=36
excluded_b27_states=8
current_state_count=28
current_route_histogram=3/10/15
maximum_remaining_gain_requirement=157
N6_FIXED_FOUR_COUPLED_FRONTIER_PASS
```
