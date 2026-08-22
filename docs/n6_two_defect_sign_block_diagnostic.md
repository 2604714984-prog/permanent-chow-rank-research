# Exact parity blocks for the `n=6` two-defect sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

This note studies the next finite enlargement after the exact one-defect
theorem. It determines the complete linear span of the normalized two-defect
sign family and proves that the 32-base Fourier-support mechanism from
N6-019 no longer applies.

It does **not** determine the minimum number of two-defect terms. The active
unrestricted interval remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. The family

Let

\[
G=(\mathbb Z/2\mathbb Z)^5
\]

and use the normalized sign vectors and column factors

\[
s_a(0)=1,
\qquad
s_a(r)=(-1)^{a_r},
\qquad
L_{a,j}=\sum_{r=0}^{5}s_a(r)x_{rj}.
\]

For a pair of distinct columns `j<k`, define

\[
T_{a,v,w;j,k}
=
L_{a+v,j}L_{a+w,k}
\prod_{\ell\notin\{j,k\}}L_{a,\ell},
\qquad a,v,w\in G.
\tag{1.1}
\]

The indexed family has

\[
\binom62\cdot32^3=491520
\]

entries. After identical uniform and one-defect presentations are collected,
the number of distinct terms is

\[
\begin{aligned}
&32
+6\cdot32\cdot31
+\binom62\cdot32\cdot31^2\\
&=467264.
\end{aligned}
\tag{1.2}
\]

The first summand counts uniform terms, the second counts terms with exactly
one exceptional column, and the third counts terms with exactly two columns
whose sign vectors differ from the unique four-column majority vector.

## 2. Fourier reduction to pairwise functions

For a row assignment

\[
r=(r_0,\ldots,r_5)\in\{0,\ldots,5\}^6,
\]

write

\[
\pi(r)=e_{r_0}+\cdots+e_{r_5}\in G,
\qquad e_0=0.
\]

The coefficient of the assignment monomial in (1.1) is

\[
[T_{a,v,w;j,k}]_r
=
(-1)^{a\cdot\pi(r)}s_v(r_j)s_w(r_k).
\tag{2.1}
\]

After Fourier transformation in the base label `a`, the block on

\[
X_p=\{r:\pi(r)=p\}
\]

is exactly the restriction of the pairwise-interaction space

\[
\mathcal P
=
\left\{
 r\longmapsto
 c+
 \sum_jg_j(r_j)+
 \sum_{j<k}g_{jk}(r_j,r_k)
\right\}.
\tag{2.2}
\]

Indeed, the 32 sign vectors span every function of one six-valued variable,
so their tensor products span every function of a selected pair of row
variables.

A canonical ANOVA basis for `P` consists of

- one constant;
- `6*5=30` unary indicators for nonzero row values; and
- `15*25=375` pure pair indicators for two nonzero row values.

Thus

\[
\dim\mathcal P=1+30+375=406.
\tag{2.3}
\]

## 3. Exact parity-block ranks

For each Hamming weight of `p`, the audit constructs the restriction matrix of
the basis (2.3) to `X_p` and performs exact sparse Gaussian elimination over
`Q`. A second elimination modulo `1,000,033` is only a cross-check.

The five nonzero row labels can be permuted arbitrarily, so parity vectors of
the same Hamming weight have the same rank. The exact table is:

| `weight(p)` | `|X_p|` | exact rank | kernel dimension in `P` |
|---:|---:|---:|---:|
| 0 | 2256 | 406 | 0 |
| 1 | 1712 | 406 | 0 |
| 2 | 1712 | 406 | 0 |
| 3 | 1200 | 322 | 84 |
| 4 | 1200 | 322 | 84 |
| 5 | 720 | 207 | 199 |

The last fiber is

\[
X_{31}=S_6,
\]

the 720 permutation assignments.

There are 16 parity vectors of weights zero through two, 15 of weights three
or four, and one target vector of weight five. Hence:

### Proposition 3.1 — exact two-defect span dimension

\[
\boxed{
\dim\operatorname{span}\{T_{a,v,w;j,k}\}
=16\cdot406+15\cdot322+207
=11533.
}
\tag{3.1}
\]

This is an exact characteristic-zero dimension, not a finite-field equality.

## 4. An explicit quadratic separator

The rank drop on the weight-three and weight-four fibers is not merely a
numerical defect. It allows an explicit pairwise function to distinguish two
non-target fibers.

For an assignment `r`, put

\[
z_j
=1_{r_j=2}-1_{r_j=3},
\qquad
m=\sum_j1_{r_j\in\{2,3\}},
\]

and define

\[
f(r)
=
1-\frac14m
+\frac12\sum_{j<k}z_jz_k.
\tag{4.1}
\]

Because

\[
\sum_{j<k}z_jz_k
=
\frac{(\sum_jz_j)^2-m}{2},
\]

we may also write

\[
f(r)
=
1+rac14(n_2-n_3)^2-rac12(n_2+n_3),
\tag{4.2}
\]

where `n_i` is the number of occurrences of row value `i`.

### Lemma 4.1 — separator values

\[
f|_{X_7}=0,
\qquad
f|_{X_{25}}=1.
\tag{4.3}
\]

### Proof

On `X_7`, the counts `n_1,n_2,n_3` are odd. Since there are only six
positions, `n_2+n_3` is either two or four. In the first case
`n_2=n_3=1`; in the second case they are one and three in some order. Equation
(4.2) gives zero in both cases.

On `X_25`, the counts `n_1,n_4,n_5` are odd, while `n_2,n_3` are even. The
three required odd counts leave at most three positions, so `n_2+n_3` is zero
or two. In the second case one of `n_2,n_3` is two and the other zero.
Equation (4.2) gives one in both cases. ∎

The audit checks all 1,200 assignments in each fiber using exact rational
arithmetic.

## 5. A 24-base aggregate representation

Let `chi_p(a)=(-1)^(p dot a)`. For every base label `a in G`, define the
pairwise aggregate function

\[
W_a
=
\frac1{32}
\left[
\chi_{31}(a)-\chi_{25}(a)
+
\bigl(\chi_{25}(a)-\chi_7(a)\bigr)f
\right].
\tag{5.1}
\]

The coefficient function obtained by combining the base-labelled aggregate
spaces is

\[
\begin{aligned}
\sum_{a\in G}\chi_{\pi(r)}(a)W_a(r)
&=1_{\pi(r)=31}\\
&\quad+
1_{\pi(r)=25}(f(r)-1)
-
1_{\pi(r)=7}f(r).
\end{aligned}
\tag{5.2}
\]

By Lemma 4.1, the last two terms vanish. Since `X_31` is exactly the
permutation support, (5.2) is the coefficient function of `perm_6`.

The aggregate `W_a` is zero exactly when

\[
\chi_{31}(a)=\chi_{25}(a)=\chi_7(a).
\]

These are two independent linear conditions on `G`, so there are eight zero
bases. Explicitly:

```text
0, 1, 6, 7, 24, 25, 30, 31.
```

Therefore:

### Proposition 5.1 — base-aggregate support drops to 24

The permanent lies in the sum of only 24 of the 32 base-labelled two-defect
aggregate spaces.

The audit verifies (5.2) on all `6^6=46656` assignments.

## 6. Why this is not a 24-term decomposition

Each `W_a` in (5.1) is a pairwise function. Its expression in the sign-product
dictionary can require several rank-one two-defect terms. Proposition 5.1
therefore controls the number of nonzero **base aggregates**, not the number of
Chow terms.

No decomposition with at most 25 terms was found or certified. Conversely, the
result proves that the exact one-defect argument cannot extend by merely
showing that all 32 base labels are forced: at two defects, eight bases can be
cancelled exactly before rank-one compression is considered.

This is a route-falsification result, not an upper bound of 24.

## 7. Route decision

```text
TWO_DEFECT_PARITY_BLOCK_RANKS=EXACT
TWO_DEFECT_SPAN_DIMENSION=11533
ONE_DEFECT_32_BASE_SUPPORT_ARGUMENT_EXTENDS=false
EXACT_BASE_AGGREGATE_SUPPORT_UPPER_BOUND=24
TWO_DEFECT_TERM_SUPPORT=OPEN
DECOMPOSITION_WITH_AT_MOST_25_TERMS_FOUND=false
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
```

The next unresolved problem is a rank-one compression problem inside the 24
nonzero pairwise aggregates. A broad sparse solver is not justified. Before
further implementation, one needs either:

1. a compact lower bound on the number of sign rank-one terms required by the
   aggregate types in (5.1); or
2. an explicit symmetry-reduced construction with at most 25 terms.

If neither reduces to a small exact interface, the sign-family route should be
suspended rather than expanded into an orbit registry or SAT architecture.

## 8. Reproduction

Run

```bash
python scripts/n6_two_defect_sign_block_audit.py \
  --json /tmp/n6_two_defect_sign_block_audit.json
python -m unittest tests.test_n6_two_defect_sign_block_audit -v
```

Expected marker:

```text
N6_TWO_DEFECT_SIGN_BLOCK_AUDIT_PASS
```

The frozen payload is

```text
data/n6_two_defect_sign_block_audit.json
```

All theorem-bearing ranks are computed over `Q` with `Fraction` arithmetic.
The modular ranks are deterministic cross-checks only. No random search,
floating threshold, or finite-field equality is used as a characteristic-zero
claim.
