# Universal full quotient Koszul gain for one degree-six Chow term

## Status

`PROOF_DRAFT_COMPLETE` — the argument below is a characteristic-zero proof. Its only finite input is the coordinate rectangle-space certificate already replayed in `scripts/n6_coordinate_monomial_full_gain_audit.py`. External peer review and a complete literature-novelty review have not been performed.

## 1. Statement

Let

\[
P=\operatorname{perm}_6,
\qquad
V=\operatorname{span}\{x_{ij}:0\le i,j<6\},
\qquad
\dim V=36.
\]

Write

\[
E_3=\mathcal D_3(P),
\qquad
E_2=\mathcal D_2(P).
\]

For a degree-six Chow term

\[
T=\ell_1\ell_2\ell_3\ell_4\ell_5\ell_6,
\]

allowing repeated or linearly dependent factors, put

\[
F_3=\mathcal D_3(T),
\qquad
F_2=\mathcal D_2(T).
\]

The central first-Koszul images are

\[
\mathcal K_P
=
\delta_3(E_3\otimes V),
\qquad
\mathcal K_T
=
\delta_3(F_3\otimes V).
\]

### Theorem 1.1 — universal single-term full gain

For every nonzero degree-six Chow term `T`,

\[
\boxed{
\mathcal K_P\cap\mathcal K_T=0.
}
\tag{1.1}
\]

Consequently,

\[
\boxed{
\operatorname{rank}\delta_3((E_3+F_3)\otimes V)
=
14175+\operatorname{rank}K_3(T),
}
\tag{1.2}
\]

and the quotient Koszul gain satisfies

\[
\boxed{
\Gamma_{E_3}(F_3)=\operatorname{rank}K_3(T).
}
\tag{1.3}
\]

Thus every individual Chow term contributes its entire first-Koszul rank modulo the permanent image, including all degenerate factor configurations.

The theorem is about one term. It does not assert that gains add for a sum of several Chow terms; the catalectic and quotient maps remain coupled under summation.

## 2. Reduction to a quadratic Koszul kernel

The next Koszul differential is

\[
\delta_2:
\operatorname{Sym}^2V\otimes\Lambda^2V
\longrightarrow
V\otimes\Lambda^3V.
\]

### Lemma 2.1

Let

\[
Q_T=E_2\cap F_2.
\]

Then

\[
\mathcal K_P\cap\mathcal K_T
\subseteq
\ker\left(
\delta_2|_{Q_T\otimes\Lambda^2V}
\right).
\tag{2.1}
\]

### Proof

Every vector in `K_P` lies in `E_2 tensor Lambda^2 V`, because applying `delta_3` differentiates the cubic factor once. Likewise,

\[
\mathcal K_T
\subseteq
F_2\otimes\Lambda^2V.
\]

A common vector therefore lies in `Q_T tensor Lambda^2 V`. Consecutive Koszul differentials compose to zero, so it is also a `delta_2`-cycle. ∎

Let

\[
L=\operatorname{span}\{\ell_1,\ldots,\ell_6\}.
\]

Then

\[
\dim L\le6,
\qquad
F_2\subseteq\operatorname{Sym}^2L.
\]

Hence

\[
Q_T
\subseteq
Q_L
:=
E_2\cap\operatorname{Sym}^2L.
\tag{2.2}
\]

It is enough to prove the following statement, which no longer refers to the factors of `T`.

### Proposition 2.2

For every linear subspace `L subset V` with `dim L<=6`,

\[
\boxed{
\delta_2|_{Q_L\otimes\Lambda^2V}
\text{ is injective}.
}
\tag{2.3}
\]

Indeed, injectivity on `Q_L` implies injectivity on its subspace `Q_T`; Lemma 2.1 then gives Theorem 1.1.

## 3. Row-column torus degeneration of the six-plane

Let

\[
\mathbb T
=(\mathbb G_m)^6\times(\mathbb G_m)^6
\]

act by

\[
(r_0,\ldots,r_5;c_0,\ldots,c_5)\cdot x_{ij}
=r_ic_jx_{ij}.
\]

The 36 coordinate variables have pairwise distinct characters. The permanent quadratic derivative space `E_2` is `T`-stable, because every basis vector

\[
q_{ii';jj'}
=
x_{ij}x_{i'j'}+x_{ij'}x_{i'j}
\]

is a torus weight vector.

Choose a one-parameter subgroup with pairwise distinct weights on the variables and generic relative to `L`. Its Grassmannian limit is a coordinate subspace

\[
L_0
=
\operatorname{span}\{x_e:e\in S\},
\qquad
|S|=\dim L\le6.
\tag{3.1}
\]

For nonzero `t`, set

\[
L_t=\lambda(t)L,
\qquad
Q_t=E_2\cap\operatorname{Sym}^2L_t.
\]

Since `E_2` is stable,

\[
Q_t=\lambda(t)Q_L.
\]

Let `Q_0` be the Grassmannian limit of the subspaces `Q_t`. Then

\[
\dim Q_0=\dim Q_L,
\qquad
Q_0
\subseteq
E_2\cap\operatorname{Sym}^2L_0.
\tag{3.2}
\]

### Lemma 3.1 — injectivity transfers back from the coordinate limit

If

\[
\delta_2|_{(E_2\cap\operatorname{Sym}^2L_0)\otimes\Lambda^2V}
\]

is injective, then the map in Proposition 2.2 is injective.

### Proof

Suppose that a nonzero

\[
z\in Q_L\otimes\Lambda^2V
\]

satisfies `delta_2 z=0`. The line spanned by `lambda(t)z` has a nonzero projective limit after rescaling. Torus equivariance of the Koszul differential gives a nonzero

\[
z_0
\in
Q_0\otimes\Lambda^2V
\subseteq
(E_2\cap\operatorname{Sym}^2L_0)\otimes\Lambda^2V
\]

with `delta_2 z_0=0`, contradicting coordinate-limit injectivity. ∎

This is a strict Grassmannian argument for the fixed-dimensional kernel candidate `Q_L`. It does not specialize the Chow term or compare a rank-dropping family of first-Koszul images.

## 4. The coordinate rectangle space

Interpret the coordinate set `S` in (3.1) as the edge set of a simple bipartite graph `G_S` on six row vertices and six column vertices. It has at most six edges.

The disjoint monomial supports of the permanent quadrics imply

\[
E_2\cap\operatorname{Sym}^2L_0
=
\operatorname{span}
\left\{
q_{ii';jj'}:
G_S\text{ contains all four edges of the rectangle}
\right\}.
\tag{4.1}
\]

A simple bipartite graph with at most six edges has:

1. no rectangle;
2. one rectangle; or
3. exactly three rectangles, in which case its cyclic core is `K_2,3` or `K_3,2`.

The proof is elementary: two distinct four-cycles in a union of at most six edges must share an adjacent two-edge path, and their union is `K_2,3` or its transpose; the third four-cycle is then forced.

Thus the coordinate rectangle space has dimension `0`, `1`, or `3`.

## 5. Coordinate injectivity

The zero-dimensional case is immediate.

### 5.1 One rectangle

If the rectangle space is `span(q)`, the quadric `q` has rank four. After diagonalizing `q`, a relation

\[
\delta_2(q\otimes\omega)=0
\]

forces three independent variables to wedge to zero with `omega`, hence `omega=0`. Therefore the restriction is injective.

### 5.2 The `K_2,3` core

Transposition reduces the three-rectangle case to

\[
T=
\operatorname{span}
\{
a_1b_2+a_2b_1,
a_1b_3+a_3b_1,
a_2b_3+a_3b_2
\}
\subseteq
\operatorname{Sym}^2L_c,
\]

where

\[
L_c=\operatorname{span}\{a_1,a_2,a_3,b_1,b_2,b_3\}.
\]

Choose `V=L_c direct_sum W`. The number of `W` factors splits the domain and output into three independent blocks:

\[
T\otimes\Lambda^2L_c,
\qquad
T\otimes(L_c\wedge W),
\qquad
T\otimes\Lambda^2W.
\]

The last block is the polarization embedding of `T`, tensored with `Lambda^2 W`, and is injective.

For each fixed `w in W`, the middle block is the map

\[
T\otimes L_c
\longrightarrow
L_c\otimes\Lambda^2L_c.
\]

Its regenerated integer matrix has an `18 x 18` minor of determinant `-1`.

The first block is

\[
T\otimes\Lambda^2L_c
\longrightarrow
L_c\otimes\Lambda^3L_c.
\]

Its regenerated integer matrix has a `45 x 45` minor of determinant `-1`.

Therefore every block is injective over every characteristic-zero field. The matrices and selected minors are rebuilt in

```text
scripts/n6_coordinate_monomial_full_gain_audit.py
```

rather than read from a stored matrix file.

We have now proved coordinate-limit injectivity for every coordinate subspace of dimension at most six. Lemma 3.1 proves Proposition 2.2, and Proposition 2.2 together with Lemma 2.1 proves Theorem 1.1.

## 6. Consequences and numerical boundary

For every nonzero degree-six Chow term,

\[
\operatorname{rank}[K_3(P)\ K_3(T)]
=
14175+\operatorname{rank}K_3(T).
\tag{6.1}
\]

The term rank can range from `35` for a sixth power to `705` for six independent factors. The exact coordinate orbit replay records all intermediate multiplicity values, but Theorem 1.1 is not restricted to coordinate factors.

Combining Theorem 1.1 with the complementary-intersection residual estimate gives, for one term,

\[
\operatorname{rank}K_3(P-T)
\ge
14175
-36\dim(E_3\cap F_3)
+
\operatorname{rank}K_3(T).
\tag{6.2}
\]

This does not improve the current universal lower bound `23` by itself. The exact-24 target requires a lower bound for the **coupled gain of a sum of four or five terms**, not merely full gain for each summand separately.

## 7. What remains open

Theorem 1.1 eliminates the single-term strictness concern. The remaining obstruction is genuinely coupled.

For

\[
R=T_1+\cdots+T_q,
\]

one cannot replace

\[
\mathcal D_3(R)
\]

by the literal sum of the individual derivative spaces, nor can one add the quotient gains term by term. The corrected `n=5` proof demonstrates exactly why such a substitution is invalid: the image of the catalectic of the sum is the relevant object, and coupling can reduce its rank.

The next target is therefore:

> for `q=4` and `q=5`, bound the quotient rank of the coupled map `K_3(T_1+...+T_q)` modulo `K_3(P_6)` using the dimensions of the individual relation kernels and the central intersection.

At the current `q=4`, `b<=40` frontier, a uniform coupled quotient gain

\[
\Gamma\ge661
\]

would raise the Chow-rank lower bound from `23` to `24`.

No large orbit registry, SAT layer, or Hilbert-scheme computation is authorized before a small relation-kernel frontier is proved.

## 8. Reproduction

Run

```bash
python scripts/n6_coordinate_monomial_full_gain_audit.py
python -m unittest tests.test_n6_coordinate_monomial_full_gain -v
```

The expected finite outputs include

```text
coordinate_monomial_orbits=167
rectangle_orbit_distribution=151/15/1
K_2,3 minors=-1,-1
N6_COORDINATE_MONOMIAL_FULL_GAIN_AUDIT_PASS
```

The computation certifies the coordinate cases used in Section 5. The transfer from arbitrary `L` to a coordinate `L_0` is the mathematical torus-degeneration argument in Section 3.
