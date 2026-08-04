# Full quotient Koszul gain at every coordinate Chow fixed point for `n=6`

## Status

`COMPUTATION_REPLAYED` and proof input for `docs/n6_universal_single_term_full_gain.md`.

This note proves and replays the coordinate-monomial theorem. The earlier limitation to coordinate terms has now been removed by a separate torus-degeneration argument on the at-most-six-dimensional factor span. The present file remains the finite coordinate certificate used by that general proof.

## 1. Coordinate theorem

Let

\[
P=\operatorname{perm}_6,
\qquad
E_3=\mathcal D_3(P),
\qquad
E_2=\mathcal D_2(P).
\]

For a degree-six coordinate monomial

\[
M=\prod_{i,j}x_{ij}^{a_{ij}},
\qquad
\sum_{i,j}a_{ij}=6,
\]

put

\[
F_3=\mathcal D_3(M),
\qquad
F_2=\mathcal D_2(M).
\]

### Theorem 1.1

For every nonzero coordinate monomial `M`,

\[
\boxed{
\delta_3(E_3\otimes V)
\cap
\delta_3(F_3\otimes V)
=0.
}
\]

Equivalently, the quotient Koszul gain equals the full term rank:

\[
\boxed{
\Gamma_{E_3}(F_3)=\operatorname{rank}K_3(M).
}
\]

## 2. Second-Koszul reduction

The next differential is

\[
\delta_2:
\operatorname{Sym}^2V\otimes\Lambda^2V
\longrightarrow
V\otimes\Lambda^3V.
\]

A common vector in the two first-Koszul images lies in

\[
(E_2\cap F_2)\otimes\Lambda^2V
\]

and is killed by `delta_2`. It is therefore enough to prove that

\[
\delta_2|_{(E_2\cap F_2)\otimes\Lambda^2V}
\]

is injective.

## 3. Rectangle-space classification

Let `G_M` be the simple bipartite support graph of `M`: the edge `(i,j)` occurs when `a_ij>0`. It has at most six distinct edges.

The permanent quadratic derivative space has basis

\[
q_{ii';jj'}
=
x_{ij}x_{i'j'}+x_{ij'}x_{i'j}.
\]

The two monomials attached to different rectangles are disjoint. Hence

\[
E_2\cap F_2
\]

is spanned exactly by the rectangle quadrics whose four edges occur in `G_M`.

A simple bipartite graph with at most six edges has:

1. no rectangle;
2. one rectangle; or
3. exactly three rectangles, with cyclic core `K_2,3` or `K_3,2`.

Indeed, two different four-cycles in a union of at most six edges must share an adjacent two-edge path. Their union is `K_2,3` or its transpose and automatically contains the third rectangle.

Thus the relevant quadratic intersection has dimension `0`, `1`, or `3`.

## 4. Injectivity in the three cases

### 4.1 No rectangle

The intersection is zero.

### 4.2 One rectangle

The unique rectangle quadric has matrix rank four. For a rank-at-least-three quadric `q`, diagonalize it as

\[
q=y_1^2+\cdots+y_r^2,
\qquad r\ge3.
\]

If

\[
\delta_2(q\otimes\omega)=0,
\]

independence of the first tensor factors forces

\[
y_i\wedge\omega=0
\]

for three independent `y_i`, hence `omega=0`. The one-rectangle restriction is injective.

### 4.3 The `K_2,3` core

Transposition reduces to

\[
T=
\operatorname{span}
\{
a_1b_2+a_2b_1,
a_1b_3+a_3b_1,
a_2b_3+a_3b_2
\}
\subseteq
\operatorname{Sym}^2L,
\]

where

\[
L=\operatorname{span}\{a_1,a_2,a_3,b_1,b_2,b_3\}.
\]

Choose `V=L direct_sum W`. The number of `W` factors splits the map into three independent blocks.

- On `T tensor Lambda^2 W`, the map is the polarization embedding of `T` tensored with `Lambda^2 W`, hence injective.
- For each `w in W`, the `T tensor (L wedge w)` block is the map
  \[
  T\otimes L\to L\otimes\Lambda^2L.
  \]
  Its regenerated integer matrix has an `18 x 18` minor of determinant `-1`.
- The `T tensor Lambda^2 L` block is
  \[
  T\otimes\Lambda^2L\to L\otimes\Lambda^3L.
  \]
  Its regenerated integer matrix has a `45 x 45` minor of determinant `-1`.

All blocks are injective over characteristic zero. This proves Theorem 1.1.

## 5. Complete orbit replay

A coordinate monomial is a bipartite multigraph with six unlabeled edges. Modulo row permutations, column permutations, transpose, and factor order, there are exactly

\[
167
\]

orbits.

The rectangle distribution is

```text
no rectangle:     151
one rectangle:     15
three rectangles:   1
```

For a monomial `M`, the cubic derivative space and its first prolongation are monomial. Therefore

\[
\operatorname{rank}K_3(M)
=36\dim\mathcal D_3(M)-\dim\mathcal D_3(M)^{(1)}
\]

is an exact integer formula. The full replay gives:

| factor multiplicities | orbit count | `dim D_3(M)` | prolongation | term rank | quotient gain |
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

For each orbit, the audit reconstructs the exact prolongation dimension and computes both the term rank and the new rank modulo `1,000,003`. The modular combined rank equals

\[
14175+\operatorname{rank}K_3(M).
\]

Characteristic-zero rank is at least modular rank, while subadditivity gives the matching upper bound. Thus the displayed quotient-gain equality is exact over characteristic zero.

## 6. Reproduction and claim boundary

Run

```bash
python scripts/n6_coordinate_monomial_full_gain_audit.py
python -m unittest tests.test_n6_coordinate_monomial_full_gain -v
```

Expected outputs include

```text
coordinate_monomial_orbits=167
rectangle_orbit_distribution=151/15/1
K_2,3 exact minors=-1,-1
N6_COORDINATE_MONOMIAL_FULL_GAIN_AUDIT_PASS
```

The machine-readable result is

```text
data/n6_coordinate_monomial_full_gain.json
```

This coordinate computation is now used as a finite lemma in

```text
docs/n6_universal_single_term_full_gain.md
```

which proves full quotient gain for every individual degree-six Chow term by degenerating its factor span, not the term image itself. Neither result implies additivity for a coupled sum of several Chow terms. The exact-24 bottleneck is the quotient rank of `K_3(T_1+...+T_q)` for `q=4` or `5`.
