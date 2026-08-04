# Exact shadow and defect budgets in the `n=6` fixed-four proof

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`.

This note records the common integer skeleton of the fixed-four proof that
now gives

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

Exact rational shadow separators and the historical frontier are replayed by

```text
scripts/n6_fixed_four_coupled_frontier.py
```

while the complete `b=22,23,24` defect enumeration and the final
component-prolongation contradictions are replayed by

```text
scripts/n6_component_prolongation_exclusion.py
```

## 1. Fixed-four notation

Under a hypothetical 23-term decomposition, fix four terms with sum `R` and
put

\[
S
=
\mathcal D_3(\operatorname{perm}_6)
\cap
\mathcal D_3(R),
\qquad
b=\dim S.
\]

At quadratic degree write

\[
E_2=\mathcal D_2(\operatorname{perm}_6),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+\cdots+G_4.
\]

The individual term theorem gives

\[
\dim G_i\le15,
\qquad
\dim(E_2\cap G_i)\le3.
\tag{1.1}
\]

A section-and-projection argument therefore gives

\[
\dim(E_2\cap U)\le48.
\tag{1.2}
\]

All first derivatives of `S` lie in `E_2 intersect U`, hence

\[
\dim\partial S\le48.
\tag{1.3}
\]

## 2. Exact shadow lower bounds

Bukh's two-dimensional shadow theorem, together with exact rational
separators, gives:

| `b` | exact separator | integer shadow lower bound |
|---:|---:|---:|
| 20 | `41/10` | 41 |
| 21 | `103/25` | 42 |
| 22 | `207/50` | 43 |
| 23 | `104/25` | 44 |
| 24 | `209/50` | 45 |
| 25 | `21/5` | 46 |
| 26 | `211/50` | 47 |
| 27 | `106/25` | 48 |

Thus

\[
\boxed{
\dim\partial S\ge b+21
\qquad(20\le b\le27).
}
\tag{2.1}
\]

In particular, (1.3) gives `b<=27`.

## 3. Individual-factor defect inequalities

Define

\[
\varepsilon_i
=15-\dim G_i,
\qquad
\alpha_i
=3-\dim(E_2\cap G_i).
\tag{3.1}
\]

Hide the `j`th factor in the projection argument. Combining its upper bound
with (2.1) gives

\[
\boxed{
\sum_{i\ne j}\varepsilon_i+\alpha_j
\le
27-b
\qquad(j=1,2,3,4).
}
\tag{3.2}
\]

Summing the four inequalities gives

\[
3\sum_i\varepsilon_i+
\sum_i\alpha_i
\le
4(27-b).
\tag{3.3}
\]

For one labelled pattern set

\[
r_i=15-\varepsilon_i,
\qquad
q_i=12-\varepsilon_i+\alpha_i.
\]

Let

\[
\kappa
=
\dim\ker\left(
G_1\oplus\cdots\oplus G_4
\longrightarrow U
\right).
\]

Since `E_2 intersect U` has dimension at least `b+21` and the quotient sum
contains every individual `q_i`-dimensional quotient image,

\[
\boxed{
\kappa
\le
\sum_ir_i-(b+21)-\max_iq_i.
}
\tag{3.4}
\]

The right side is at most `27-b`.

## 4. Exact defect tables

The labelled pattern counts and relation-kernel caps are:

| `b` | defect budget | labelled patterns | cap histogram |
|---:|---:|---:|---:|
| 27 | 0 | 1 | `1` pattern at cap 0 |
| 26 | 1 | 24 | `23/1` at caps `0/1` |
| 25 | 2 | 213 | `189/23/1` at caps `0/1/2` |
| 24 | 3 | 1,153 | `940/189/23/1` at caps `0/1/2/3` |
| 23 | 4 | 4,599 | `3446/940/189/23/1` at caps `0/1/2/3/4` |
| 22 | 5 | 14,877 | `10278/3446/940/189/23/1` at caps `0/1/2/3/4/5` |

Quadratic derivative dimension 12 is impossible for a degree-six Chow
term. Removing those patterns gives:

| `b` | impossible dimension-12 patterns | retained patterns | retained cap histogram |
|---:|---:|---:|---:|
| 24 | 16 | 1,137 | `924/189/23/1` |
| 23 | 256 | 4,343 | `3206/924/189/23/1` |
| 22 | 1,716 | 13,161 | `8818/3206/924/189/23/1` |

The unique maximum-cap pattern in every displayed layer is

\[
\varepsilon=(0,0,0,0),
\qquad
\alpha=(0,0,0,0).
\tag{4.1}
\]

## 5. Exclusion chain

### `b=27`

Equality in all four projections forces a common 12-dimensional quadratic
quotient, a direct quadratic sum of dimension 60, and coupled central rank
80. The residual upper bound is 34. See
`docs/n6_b27_common_quotient_exclusion.md`.

### `b=26`

The 24 patterns have relation-kernel cap zero or one. Directness or the
one-relation integrability lemma gives central rank at least 60, while the
residual upper bound is 32. See
`docs/n6_b26_one_relation_exclusion.md`.

### `b=25`

The 213 patterns have relation-kernel cap zero, one, or two. The term-profile
and squarefree-binary arguments give central rank at least 78, while the
residual upper bound is 30. See
`docs/n6_b25_two_relation_exclusion.md`.

### `b=22,23,24`

Let `kappa` be the cap from (3.4). Macaulay growth bounds the first
prolongation of a scalar `kappa`-dimensional quadratic space by

\[
\kappa^{\langle2\rangle}.
\]

For four components, the entire cubic relation kernel has dimension at most

\[
3\kappa^{\langle2\rangle}.
\]

A block-Sylvester inequality then gives:

| `b` | maximum `kappa` | maximum scalar prolongation cap | minimum coupled central rank | residual upper bound |
|---:|---:|---:|---:|---:|
| 22 | 5 | 7 | **38** | 24 |
| 23 | 4 | 5 | **50** | 26 |
| 24 | 3 | 4 | **56** | 28 |

All three layers are impossible. See
`docs/n6_component_prolongation_exclusion.md`.

## 6. Completion of the 23-term exclusion

The only remaining states are

\[
(b,d)=(20,0),(21,0),(21,1).
\]

Their quotient-Koszul lower bounds are respectively

\[
13455,
\qquad
13419,
\qquad
13419,
\]

all strictly above the nineteen-term capacity

\[
19\cdot705=13395.
\]

Therefore every fixed-four state under a hypothetical 23-term
decomposition is contradictory, and

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
}
\]

## 7. Claim boundary

This proof excludes only 23 terms. It does not prove a lower bound of 25,
a border Chow-rank lower bound of 24, or the conjectural exact value 32.

## 8. Reproduction

Run

```bash
python scripts/n6_fixed_four_coupled_frontier.py
python scripts/n6_b24_three_relation_frontier.py
python scripts/n6_component_prolongation_exclusion.py
python -m unittest tests.test_n6_component_prolongation_exclusion -v
```
