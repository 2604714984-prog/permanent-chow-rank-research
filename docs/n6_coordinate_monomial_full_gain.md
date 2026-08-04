# Full quotient Koszul gain at every coordinate Chow fixed point for `n=6`

## Status

`PROOF_DRAFT_COMPLETE` — the argument below proves the coordinate-monomial theorem in characteristic zero. A standard-library audit independently enumerates all 167 bipartite-multigraph orbit types and replays every rank. External peer review and a complete literature-novelty review have not been performed.

## 1. Scope

Let

\[
P=\operatorname{perm}_6,
\qquad
V=\operatorname{span}\{x_{ij}:0\le i,j<6\},
\qquad
\dim V=36,
\]

and put

\[
E=\mathcal D_3(P).
\]

The central first-Koszul image has dimension

\[
\operatorname{rank}\delta_3(E\otimes V)=14175.
\]

For a degree-six form `T`, write

\[
F_T=\mathcal D_3(T)
\]

and define its quotient Koszul gain relative to the permanent by

\[
\Gamma_E(F_T)
=
\operatorname{rank}\delta_3((E+F_T)\otimes V)
-
\operatorname{rank}\delta_3(E\otimes V).
\]

The general residual theorem in `docs/quotient_koszul_gain.md` uses only `Gamma_E(F_T)>=0`. This note proves the strongest possible value for every **coordinate monomial**

\[
M=\prod_{i,j}x_{ij}^{a_{ij}},
\qquad
a_{ij}\in\mathbb Z_{\ge0},
\qquad
\sum_{i,j}a_{ij}=6.
\]

### Theorem 1.1

For every nonzero coordinate monomial `M` of degree six,

\[
\boxed{
\Gamma_E(F_M)
=
\operatorname{rank}\delta_3(F_M\otimes V).
}
\]

Equivalently,

\[
\boxed{
\delta_3(E\otimes V)
\cap
\delta_3(F_M\otimes V)
=
0.
}
\]

Thus every reduced coordinate fixed point has full quotient gain, including all factor-multiplicity degenerations.

This is not yet a theorem for arbitrary non-monomial Chow terms. Section 7 explains the non-strict specialization obstruction.

## 2. A second-Koszul reduction

Let

\[
E_2=\mathcal D_2(P),
\qquad
F_{M,2}=\mathcal D_2(M).
\]

The next differential in the Koszul complex is

\[
\delta_2:
\operatorname{Sym}^2V\otimes\Lambda^2V
\longrightarrow
V\otimes\Lambda^3V.
\]

### Lemma 2.1

Set

\[
T_M=E_2\cap F_{M,2}.
\]

Then

\[
\delta_3(E\otimes V)
\cap
\delta_3(F_M\otimes V)
\subseteq
\ker\left(
\delta_2|_{T_M\otimes\Lambda^2V}
\right).
\]

### Proof

The image of `delta_3(E tensor V)` is contained in

\[
E_2\otimes\Lambda^2V,
\]

and the image of `delta_3(F_M tensor V)` is contained in

\[
F_{M,2}\otimes\Lambda^2V.
\]

Hence a common image vector lies in `T_M tensor Lambda^2 V`. It is also a Koszul cycle because consecutive Koszul differentials compose to zero. ∎

It therefore suffices to prove that

\[
\delta_2|_{T_M\otimes\Lambda^2V}
\]

is injective.

## 3. The rectangle space of a coordinate monomial

Let `G_M` be the simple bipartite support graph of `M`. Its left vertices are the six matrix rows, its right vertices are the six matrix columns, and `(i,j)` is an edge exactly when `a_ij>0`. The graph has at most six distinct edges.

The permanent quadratic derivative space has the basis

\[
q_{ii';jj'}
=
x_{ij}x_{i'j'}
+
x_{ij'}x_{i'j},
\qquad
i<i',
\quad
j<j'.
\]

Different rectangles have disjoint pairs of monomial supports.

### Lemma 3.1

The intersection `T_M` is the span of precisely those `q_{ii';jj'}` whose four rectangle edges occur in `G_M`.

### Proof

The monomial space `F_{M,2}` is spanned by the degree-two monomial divisors of `M`. Because every permanent quadratic basis vector has its own two-monomial support pair, a linear combination belongs to this monomial space exactly when both monomials of every used rectangle divide `M`. This is equivalent to the presence of all four rectangle edges in `G_M`. ∎

### Lemma 3.2 — six-edge rectangle classification

A simple bipartite graph with at most six edges has one of the following rectangle sets:

1. no rectangle;
2. exactly one rectangle;
3. exactly three rectangles, in which case its cyclic core is `K_2,3` or `K_3,2`.

### Proof

Two distinct four-cycles whose union has at most six edges must share at least two edges. In a bipartite graph, two distinct four-cycles sharing two edges share an adjacent length-two path. Their union is therefore `K_2,3` or `K_3,2`, and the third four-cycle is automatically present. A `K_2,3` already uses six edges, so no further edge can belong to the support. ∎

Consequently, `T_M` has dimension `0`, `1`, or `3`.

## 4. Injectivity for one rectangle

Suppose

\[
T_M=\operatorname{span}\{q\}.
\]

The quadric `q` has matrix rank four.

### Lemma 4.1

If a quadratic form `q` has rank at least three, then

\[
\delta_2:
\operatorname{span}\{q\}\otimes\Lambda^2V
\longrightarrow
V\otimes\Lambda^3V
\]

is injective.

### Proof

After a linear change of variables, the gradient of `q` contains three linearly independent variables `y_1,y_2,y_3`. If

\[
\delta_2(q\otimes\omega)=0,
\]

independence of the first tensor factors gives

\[
y_i\wedge\omega=0
\qquad
(i=1,2,3).
\]

The first equation gives `omega=y_1 wedge a`. The second forces `a` to lie in `span(y_1,y_2)`, so `omega` is a scalar multiple of `y_1 wedge y_2`. The third equation then forces that scalar to vanish. ∎

Thus the one-rectangle case contributes no common Koszul image.

## 5. Injectivity for the `K_2,3` rectangle space

It is enough to treat `K_2,3`; transposition gives `K_3,2`.

Let

\[
L=\operatorname{span}
\{a_1,a_2,a_3,b_1,b_2,b_3\}
\subseteq V
\]

and let

\[
T=
\operatorname{span}
\{
a_1b_2+a_2b_1,
a_1b_3+a_3b_1,
a_2b_3+a_3b_2
\}.
\]

Choose a complement `V=L direct_sum W`. The decomposition

\[
\Lambda^2V
=
\Lambda^2L
\oplus
(L\wedge W)
\oplus
\Lambda^2W
\]

is preserved by the number of `W`-factors in the output of `delta_2`.

### Proposition 5.1

The restriction

\[
\delta_2|_{T\otimes\Lambda^2V}
\]

is injective.

### Proof

There are three independent blocks.

#### The `Lambda^2 W` block

For a fixed nonzero `w wedge w'`, the map is the gradient map on `T`, tensored with `w wedge w'`. The gradient map is injective because Euler multiplication recovers `2q` from the gradient of `q`. Hence this block is injective.

#### The `L wedge W` block

For every fixed `w in W`, the relevant map is

\[
T\otimes L
\longrightarrow
L\otimes\Lambda^2L.
\]

In the ordered basis

\[
a_1,a_2,a_3,b_1,b_2,b_3,
\]

the exact integer matrix has an `18 x 18` minor of determinant

\[
-1.
\]

Therefore this map is injective over every field.

#### The `Lambda^2 L` block

The remaining map is

\[
T\otimes\Lambda^2L
\longrightarrow
L\otimes\Lambda^3L.
\]

Its exact integer matrix has a `45 x 45` minor of determinant

\[
-1.
\]

Hence this block is also injective over every field.

The two minors are reconstructed from the definitions by `scripts/n6_coordinate_monomial_full_gain_audit.py`; their selected row indices are frozen in that script, while the matrices themselves are regenerated rather than stored. ∎

Combining Sections 3–5 proves that the kernel in Lemma 2.1 is always zero, and therefore proves Theorem 1.1.

## 6. Exact ranks and the 167-orbit replay

A degree-six coordinate monomial is equivalently a bipartite multigraph with six unlabeled edges. Row permutations, column permutations, transpose, and factor order reduce these monomials to exactly

\[
167
\]

orbits.

For a monomial `M`, the space `F_M` is a monomial cubic space. Its first prolongation is also monomial: a degree-four monomial belongs to `F_M^(1)` exactly when deleting any one of its variables leaves a cubic divisor of `M`. Hence

\[
\operatorname{rank}K_3(M)
=
36\dim F_M-\dim F_M^{(1)}
\]

is computed over the integers without numerical rank estimation.

The complete orbit replay gives:

| factor multiplicities | orbit count | `dim D_3(M)` | `dim D_3(M)^(1)` | term rank | quotient gain |
|---|---:|---:|---:|---:|---:|
| `6` | 1 | 1 | 1 | 35 | 35 |
| `5+1` | 2 | 2 | 2 | 70 | 70 |
| `4+2` | 2 | 3 | 3 | 105 | 105 |
| `4+1+1` | 6 | 4 | 4 | 140 | 140 |
| `3+3` | 2 | 4 | 5 | 139 | 139 |
| `3+2+1` | 8 | 6 | 6 | 210 | 210 |
| `3+1+1+1` | 17 | 8 | 8 | 280 | 280 |
| `2+2+2` | 4 | 7 | 6 | 246 | 246 |
| `2+2+1+1` | 25 | 10 | 8 | 352 | 352 |
| `2+1+1+1+1` | 50 | 14 | 11 | 493 | 493 |
| `1+1+1+1+1+1` | 50 | 20 | 15 | 705 | 705 |

The rectangle distribution across the 167 orbits is

```text
no rectangle:    151
one rectangle:    15
three rectangles:  1
```

For every representative, the script rebuilds:

1. the exact monomial prolongation upper bound;
2. the term Koszul rank modulo `1,000,003`;
3. the combined permanent-plus-term rank modulo the same prime.

The modular combined rank equals

\[
14175+\operatorname{rank}K_3(M).
\]

Since matrix rank over characteristic zero is at least the modular rank, while subadditivity gives the matching upper bound, the full-gain equality follows exactly in characteristic zero.

The frozen machine-readable result is

```text
data/n6_coordinate_monomial_full_gain.json
```

and the replay command is

```bash
python scripts/n6_coordinate_monomial_full_gain_audit.py
```

## 7. Why this does not yet prove full gain for every Chow term

The row-column torus preserves `E`, and every Chow term has coordinate-monomial limits. However, the rank of `K_3(T)` can drop in such a limit. The condition

\[
\operatorname{im}K_3(T)\cap\operatorname{im}K_3(P)=0
\]

is not closed across rank-dropping families.

A model linear-algebra example is

\[
B_t=
\begin{pmatrix}
1&0\\
0&t
\end{pmatrix},
\qquad
A=\operatorname{span}(e_2).
\]

For `t != 0`, the image of `B_t` meets `A`; at `t=0`, the image drops to `span(e_1)` and the intersection disappears. Thus a bad generic family need not leave a bad reduced fixed point.

Theorem 1.1 therefore closes the **reduced coordinate boundary**, but a universal full-gain theorem would still have to exclude non-strict rank-loss jets at those fixed points.

## 8. Research consequence

The current evidence supports the conjecture

\[
\Gamma_E(\mathcal D_3(T))
=
\operatorname{rank}K_3(T)
\]

for every degree-six Chow term `T`, including degenerate terms. Random and structured sparse tests have found no counterexample, but those tests are diagnostic only and are not part of Theorem 1.1.

The next proof task is now sharply localized:

> classify first-order and higher-order rank-loss arcs in the Chow-term parameter space whose reduced row-column-torus limit is a coordinate monomial, and prove that no Koszul intersection survives in the associated Rees limit.

No SAT, Hilbert-scheme registry, or large finite-state layer is justified before that local strictness problem is understood.
