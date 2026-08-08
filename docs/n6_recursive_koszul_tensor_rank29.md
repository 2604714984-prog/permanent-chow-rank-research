# Independent recursive-Koszul replay for the order-six permanent tensor

## Status

`LITERATURE_REPLAYED`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

This note independently reconstructs the `n=6` recursive Koszul flattening
from Han--Ju--Kim, *Recursive Koszul flattenings of determinant and permanent
tensors*, arXiv:2503.12032v1, and proves over every characteristic-zero field

\[
\boxed{
\underline{\mathbf R}(\operatorname{perm}^{\mathrm{tensor}}_6)
\ge29.
}
\tag{0.1}
\]

Here the underline denotes border tensor rank. Consequently the ordinary
tensor rank is also at least 29.

A row-homogeneous decomposition of the matrix permanent is exactly a tensor
rank decomposition of the permanent tensor, after choosing the six row spaces
or, equivalently, the six column spaces. Hence

\[
\boxed{
\operatorname{RowHomogeneousRank}(\operatorname{perm}_6)\ge29.
}
\tag{0.2}
\]

Every normalized row-sign, column-sign, one-defect, or two-defect sign family
is a subfamily of the row-homogeneous tensor model. Therefore none of those
families contains a decomposition with at most 28 terms.

This does **not** improve unrestricted Chow rank. A general Chow factor may
mix variables from several tensor factors. The active unrestricted interval
remains

\[
25\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Literature identity and independent role

The reviewed source is

```text
Jong In Han, Jeong-Hoon Ju, Yeongrak Kim
Recursive Koszul flattenings of determinant and permanent tensors
arXiv:2503.12032v1, 15 March 2025
Theorem 5.6
```

Theorem 5.6 reports

```text
matrix size=162000 x 162000
matrix rank=70692
rank-one normalization=2500
border tensor-rank lower bound=29
```

The authors' implementation repository is

```text
jihan099/RKF
reviewed main commit=2ebfbf70d7d1474c045bfbc0f7449c7b083667d9
RKF_Per6.m SHA-1=395c0a05148e34507d1ba0cbdb347ae84eea1491
getRankSymm.m SHA-1=afe1a349e17d2a1b2f11d223aba3a4bbe0988a16
```

The present repository does not call Matlab, read `orbitmat6.dat`, or import
the upstream helpers. The standard-library Python replay reconstructs the
integer matrix directly from the definition, finds every connected component
of its bipartite support graph, and computes component ranks over two exact
prime fields.

Thus the literature theorem is not merely cited: its `n=6` matrix rank is
independently replayed by a structurally different implementation.

## 2. The permanent tensor

Let `V` be six-dimensional with basis `e_0,...,e_5`. The order-six permanent
tensor is

\[
\operatorname{perm}^{\mathrm{tensor}}_6
=
\sum_{\sigma\in S_6}
 e_{\sigma(0)}\otimes\cdots\otimes e_{\sigma(5)}
\in V^{\otimes6}.
\tag{2.1}
\]

Its tensor rank is the least number of decomposable tensors required to
express it. Border tensor rank is the least `r` such that it lies in the
Zariski closure of tensors of rank at most `r`.

## 3. Recursive Koszul flattening

Use exterior degrees

\[
(1,2,3,4).
\]

The recursive Koszul flattening is

\[
\Phi_6:
\Lambda^1V\otimes\Lambda^2V\otimes\Lambda^3V
\otimes\Lambda^4V\otimes V^*
\longrightarrow
\Lambda^2V\otimes\Lambda^3V\otimes\Lambda^4V
\otimes\Lambda^5V\otimes V.
\tag{3.1}
\]

Both sides have dimension

\[
6\binom62\binom63\binom64 6
=6\cdot15\cdot20\cdot15\cdot6
=162000.
\tag{3.2}
\]

On a domain basis vector

\[
I_1\otimes I_2\otimes I_3\otimes I_4\otimes e_j^*,
\]

where `|I_k|=k`, the summand associated with a permutation
`(s_1,...,s_6)` is zero unless `s_5=j` and `s_k notin I_k` for
`1<=k<=4`. Otherwise it is

\[
(e_{s_1}\wedge I_1)\otimes\cdots\otimes
(e_{s_4}\wedge I_4)\otimes e_{s_6},
\tag{3.3}
\]

with the product of the four exterior signs.

For one decomposable tensor, the flattening rank is

\[
\prod_{k=1}^{4}\binom{5}{k}
=5\cdot10\cdot10\cdot5
=2500.
\tag{3.4}
\]

Matrix-rank subadditivity, and the closedness of determinantal rank loci, give

\[
\underline{\mathbf R}(T)
\ge
\left\lceil
\frac{\operatorname{rank}\Phi_6(T)}{2500}
\right\rceil.
\tag{3.5}
\]

## 4. Direct integer-matrix reconstruction

For each of the `720` permutations, the four wedge maps have respectively

\[
\binom51,
\binom52,
\binom53,
\binom54
=
5,10,10,5
\]

nonzero input basis vectors. Thus the replay generates exactly

\[
720\cdot2500=1800000
\tag{4.1}
\]

nonzero signed entries. Every entry is `+1` or `-1`; no two generated entries
occupy the same matrix position.

The deterministic edge stream, encoded as little-endian
`(uint32 row, uint32 column, int8 sign)`, has SHA-256

```text
b06ddee0d9573b2b20e82fb75aa738a5d505190412c15a78959ea63f0aa500f1
```

This hash binds the generated matrix independently of sparse-library formats.

## 5. Connected components and exact modular ranks

The bipartite support graph has

\[
2932
\]

connected components. Every component is square. The exact component
histogram is:

| rows = columns | rank mod `p` | component count | rank contribution |
|---:|---:|---:|---:|
| 1 | 1 | 720 | 720 |
| 3 | 2 | 480 | 960 |
| 8 | 5 | 540 | 2700 |
| 9 | 4 | 20 | 80 |
| 21 | 12 | 360 | 4320 |
| 49 | 24 | 240 | 5760 |
| 55 | 29 | 180 | 5220 |
| 110 | 46 | 12 | 552 |
| 125 | 58 | 120 | 6960 |
| 276 | 118 | 180 | 21240 |
| 590 | 225 | 60 | 13500 |
| 1236 | 434 | 20 | 8680 |

The weighted sum is

\[
\boxed{70692.}
\tag{5.1}
\]

The complete calculation is repeated over the two primes

```text
1000003
1000033
```

and gives the same component histogram and total rank.

The matrix has integer entries. Therefore a rank of 70692 modulo either prime
implies

\[
\operatorname{rank}_{\mathbb Q}\Phi_6
\ge70692.
\tag{5.2}
\]

No finite-field equality is promoted to characteristic zero. Only the valid
lower-bound direction is used.

Combining (3.5) and (5.2),

\[
\underline{\mathbf R}(\operatorname{perm}^{\mathrm{tensor}}_6)
\ge
\left\lceil\frac{70692}{2500}\right\rceil
=29.
\tag{5.3}
\]

## 6. Translation to row-homogeneous decompositions

Write the matrix variables by columns as six copies

\[
V_0,\ldots,V_5\cong V.
\]

A row-homogeneous or column-oriented term has the form

\[
\ell_0(x_{*,0})\cdots\ell_5(x_{*,5}),
\tag{6.1}
\]

and its coefficient tensor is decomposable in

\[
V_0\otimes\cdots\otimes V_5.
\]

Conversely every decomposable tensor gives such a term. Hence the minimum
number of arbitrary complex row-homogeneous terms equals the tensor rank of
(2.1), and the corresponding border notions also agree.

Matrix transposition exchanges row- and column-oriented models and preserves
the permanent. Therefore (5.3) applies equally to either orientation.

The inclusion chain is

```text
uniform signs
  subset one-defect signs
  subset two-defect signs
  subset full column-sign family
  subset arbitrary column-oriented tensor terms
  --transpose--> arbitrary row-homogeneous tensor terms.
```

Thus every family in the chain has ordinary and border support at least 29.
Glynn supplies 32 terms, so their current common numerical interval is

\[
29\le\text{restricted rank}\le32,
\]

except where the repository has a stronger subclass theorem, such as the
one-defect exact value 32.

## 7. Research consequence

The sign-family construction program was initially retained as a possible
search for a decomposition with at most 25 terms. Equation (5.3) rules this
out before any sign restriction is imposed:

```text
ROW_HOMOGENEOUS_DECOMPOSITION_WITH_AT_MOST_28_TERMS=IMPOSSIBLE
FULL_COLUMN_SIGN_DECOMPOSITION_WITH_AT_MOST_28_TERMS=IMPOSSIBLE
TWO_DEFECT_DECOMPOSITION_WITH_AT_MOST_28_TERMS=IMPOSSIBLE
```

Consequently the sign-family route cannot produce a 25-term counterexample to
an unrestricted lower-26 conjecture. Broad sparse sign optimization, orbit
registries, and SAT encodings remain unauthorized.

A legitimate continuation would have to target the narrow unresolved tensor
interval `29..32`, for example by a one-term-removal recursive-Koszul theorem
or a new symmetry-compatible flattening. Such a result would still concern
row-homogeneous tensor rank and would not automatically improve unrestricted
Chow rank.

## 8. Reproduction and claim boundary

Run

```bash
python scripts/n6_recursive_koszul_tensor_rank_audit.py \
  --json /tmp/n6_recursive_koszul_tensor_rank_audit.json
python -m unittest tests.test_n6_recursive_koszul_tensor_rank -v
```

Expected marker:

```text
N6_RECURSIVE_KOSZUL_TENSOR_RANK_AUDIT_PASS
```

The implementation uses only the Python standard library. It does not read the
upstream orbit matrix or precomputed component ranks.

The theorem does not prove:

- unrestricted `ChowRank(perm_6)>=29`;
- row-homogeneous tensor rank 32;
- a border Chow-rank lower bound of 29;
- `ChowRank(perm_6)>=26`; or
- literature novelty.

It independently replays a published tensor-border-rank obstruction and
records its exact consequence for the project's restricted sign families.
