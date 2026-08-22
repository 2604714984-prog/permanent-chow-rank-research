# Exact rigidity of the `n=6` one-defect Glynn sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_FAMILY_THEOREM`.

This note proves that enlarging the 32 Glynn sign terms by allowing one column
to use a different normalized sign vector still does not shorten the
permanent decomposition:

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

The result is exact over characteristic zero. It is not a lower bound for the
full column-sign family, row-homogeneous tensor rank, or unrestricted Chow
rank. The active unrestricted interval remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

The literature boundary is in
`docs/xu_gnang_v2_reconciliation.md`: the row-homogeneous optimality theorem
in Xu--Gnang arXiv:2311.05890v2 is withdrawn in version 3 and is not used here.

## 1. The normalized one-defect family

Let

\[
G=(\mathbb Z/2\mathbb Z)^5.
\]

For `a in G`, define the normalized sign vector

\[
s_a(0)=1,
\qquad
s_a(r)=(-1)^{a_r}
\quad(1\le r\le5).
\tag{1.1}
\]

For column `j`, put

\[
L_{a,j}
=
\sum_{r=0}^{5}s_a(r)x_{rj}.
\tag{1.2}
\]

A one-defect term is

\[
T_{a,v,j}
=
L_{a+v,j}
\prod_{k\ne j}L_{a,k},
\qquad
a,v\in G,\quad0\le j\le5.
\tag{1.3}
\]

When `v=0`, this is the uniform Glynn term and does not depend on `j`. After
identical terms are collected, the family has

\[
32+6\cdot32\cdot31=5984
\]

distinct members. The indexed family with the six duplicate presentations of
each uniform term has `6*32*32=6144` entries and the same linear span.

Define `OneDefectSignRank(f)` as the minimum number of nonzero scalar multiples
of distinct terms (1.3) whose sum is `f`.

Every column-sign product can be projectively normalized to row-zero
coefficient `+1` in each column; the product of the six normalization scalars
is absorbed into the coefficient of the Chow term. For `v!=0`, the majority
sign vector, exceptional column, and defect vector in (1.3) are unique. Thus
the normalization and the count 5,984 do not hide duplicate nonuniform terms.

## 2. Parity blocks

For an assignment

\[
r=(r_0,\ldots,r_5)\in\{0,1,\ldots,5\}^6,
\]

let `e_0=0` and let `e_1,...,e_5` be the standard basis of `G`. Define

\[
\pi(r)=e_{r_0}+\cdots+e_{r_5}\in G.
\tag{2.1}
\]

The coefficient of the monomial

\[
x_{r_0,0}x_{r_1,1}\cdots x_{r_5,5}
\]

in a one-defect term is

\[
\begin{aligned}
[T_{a,v,j}]_r
&=
\left(\prod_{k\ne j}s_a(r_k)\right)s_{a+v}(r_j)\\
&=
(-1)^{a\cdot\pi(r)}s_v(r_j).
\end{aligned}
\tag{2.2}
\]

The audit verifies the character identity underlying (2.2) in all

\[
32^3\cdot6=196608
\]

cases. The proof itself is the displayed character multiplication, not the
finite check.

For `p in G`, let

\[
X_p=\{r:\pi(r)=p\}.
\tag{2.3}
\]

The diagonal sign-change action of `G` decomposes the coefficient space into
the direct sum of the 32 spaces of functions on `X_p`.

Fourier transforming (2.2) over the base label `a` gives

\[
\sum_{a\in G}(-1)^{p\cdot a}T_{a,v,j}
\quad\longmapsto\quad
32\,1_{X_p}(r)s_v(r_j).
\tag{2.4}
\]

The 32 vectors `s_v` span the full six-dimensional space of functions of one
row variable. An exact `6 x 6` integer minor has determinant `-32`.
Consequently the part of the one-defect span in the `p`-block is exactly the
additive function space

\[
\mathcal A_p
=
\left\{
 r\longmapsto\sum_{j=0}^{5}g_j(r_j):
 g_j:\{0,\ldots,5\}\to k
\right\}
\subseteq k^{X_p}.
\tag{2.5}
\]

## 3. Exact additive-feature ranks

Represent (2.5) by the `|X_p| x 36` zero-one matrix whose row for an assignment
`r` has a one in each coordinate `(j,r_j)`.

For every `p`, the five-dimensional space

\[
(g_0,\ldots,g_5)
=(c_0\mathbf1,\ldots,c_5\mathbf1),
\qquad
\sum_jc_j=0,
\tag{3.1}
\]

lies in the kernel, so the rank is at most 31.

The symmetric group on the five nonzero row labels acts transitively on parity
vectors of each Hamming weight. It therefore suffices to certify one matrix for
each weight. The exact integer minors are:

| `weight(p)` | `|X_p|` | certified rank | determinant of the certified minor |
|---:|---:|---:|---:|
| 0 | 2256 | 31 | `-32` |
| 1 | 1712 | 31 | `32` |
| 2 | 1712 | 31 | `-32` |
| 3 | 1200 | 31 | `-32` |
| 4 | 1200 | 31 | `-32` |
| 5 | 720 | 26 | `1` |

For weights zero through four, the nonzero `31 x 31` minors combine with
(3.1) to prove

\[
\ker\mathcal A_p
=
\left\{
(c_0\mathbf1,\ldots,c_5\mathbf1):\sum_jc_j=0
\right\}
\quad(p\ne(1,1,1,1,1)).
\tag{3.2}
\]

For

\[
p_*= (1,1,1,1,1),
\tag{3.3}
\]

the fiber `X_(p_*)` consists exactly of the 720 permutations of
`0,1,...,5`. In addition to the five position-constant relations (3.1), the
five row-total relations

\[
\sum_{j=0}^{5}e_{j,i}-\sum_{j=0}^{5}e_{j,0},
\qquad 1\le i\le5,
\tag{3.4}
\]

vanish on every permutation assignment. These ten relations are independent
in characteristic zero, so the target feature rank is at most `36-10=26`.
The certified `26 x 26` determinant-one minor gives the equal lower bound.
Thus the target rank is exactly 26 without relying on an unsupported
finite-field equality.

### Corollary 3.1 — exact span dimension

There are 31 non-target parity blocks of rank 31 and one target block of rank
26. Hence

\[
\boxed{
\dim\operatorname{span}\{T_{a,v,j}\}
=31\cdot31+26
=987.
}
\tag{3.5}
\]

## 4. The target support is one parity fiber

The permanent coefficient on an assignment `r` is one exactly when `r` is a
permutation and is zero otherwise. By Section 3, this means

\[
\operatorname{perm}_6|_{X_p}=0
\quad(p\ne p_*),
\qquad
\operatorname{perm}_6|_{X_{p_*}}=\mathbf1.
\tag{4.1}
\]

The standard Glynn identity becomes

\[
\operatorname{perm}_6
=
\frac1{32}
\sum_{a\in G}
(-1)^{p_*\cdot a}
\prod_{j=0}^{5}L_{a,j}.
\tag{4.2}
\]

The audit expands all `6^6=46656` coefficient assignments and obtains 32 in
the numerator on the 720 permutation assignments and zero on all 45,936 other
assignments. Therefore

\[
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)\le32.
\tag{4.3}
\]

## 5. Exact lower bound 32

Assume

\[
\operatorname{perm}_6
=
\sum_{t=1}^{m}c_tT_{a_t,v_t,j_t},
\qquad c_t\ne0.
\tag{5.1}
\]

Repeated identical terms are collected. A uniform term may be assigned any
one defect position; fix one such choice.

For each base label `a` and position `j`, define the row function

\[
W_j(a)
=
\sum_{t:\,a_t=a,\,j_t=j}c_ts_{v_t}
\in k^{\{0,\ldots,5\}}.
\tag{5.2}
\]

Its Fourier transform in the base label is

\[
\widehat W_j(p)
=
\sum_{a\in G}(-1)^{p\cdot a}W_j(a).
\tag{5.3}
\]

By (2.2), the coefficient function of (5.1) on `X_p` is

\[
r\longmapsto
\sum_{j=0}^{5}\widehat W_j(p)(r_j).
\tag{5.4}
\]

### 5.1 Non-target parity constraints

For `p != p_*`, the target in (4.1) is zero. Equation (3.2) applied to (5.4)
therefore gives constants `alpha_j(p)` such that

\[
\widehat W_j(p)=\alpha_j(p)\mathbf1,
\qquad
\sum_j\alpha_j(p)=0.
\tag{5.5}
\]

Let

\[
\overline U
=
k^{\{0,\ldots,5\}}/k\mathbf1.
\]

Reducing (5.5) modulo constants shows that, for each `j`, the Fourier
transform of the function

\[
a\longmapsto\overline{W_j(a)}
\]

vanishes at all 31 characters except `p_*`. Fourier inversion gives a fixed
class `u_j in overline U` such that

\[
\overline{W_j(a)}
=(-1)^{p_*\cdot a}u_j
\quad\text{for every }a\in G,
\tag{5.6}
\]

after absorbing the harmless factor `1/32` into `u_j`.

If some `u_j` is nonzero, then `W_j(a)` is nonzero for every one of the 32 base
labels `a`. Each such base requires at least one summand in (5.1). Hence

\[
m\ge32.
\tag{5.7}
\]

### 5.2 The all-constant alternative

It remains to consider the case in which every `u_j` in (5.6) is zero. Then
there are scalar functions `gamma_j:G->k` such that

\[
W_j(a)=\gamma_j(a)\mathbf1.
\tag{5.8}
\]

The second condition in (5.5) says that, for

\[
\Gamma(a)=\sum_j\gamma_j(a),
\tag{5.9}
\]

all Fourier coefficients except possibly the `p_*` coefficient vanish. Thus

\[
\Gamma(a)=\lambda(-1)^{p_*\cdot a}
\tag{5.10}
\]

for some scalar `lambda`.

On the target fiber `X_(p_*)`, equations (5.4), (5.8), and (4.1) give

\[
1
=
\sum_j\widehat\gamma_j(p_*)
=
\widehat\Gamma(p_*)
=32\lambda.
\tag{5.11}
\]

Therefore `lambda=1/32`, so `Gamma(a)` is nonzero for every base label. For
each of the 32 labels `a`, at least one `W_j(a)` is nonzero, and hence at least
one summand in (5.1) has base `a`. Again

\[
m\ge32.
\tag{5.12}
\]

The two cases are exhaustive. Combining (4.3), (5.7), and (5.12) proves:

### Theorem 5.1 — one-defect rigidity

Over every characteristic-zero field,

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

In particular, this family contains no decomposition with at most 25 or at
most 31 terms.

## 6. What the theorem does and does not decide

The theorem strictly extends G-020:

```text
uniform 32-term Glynn family
    -> one normalized defect in an arbitrary column
```

The larger restricted family has 5,984 distinct terms and a 987-dimensional
span, but the minimum support of the permanent remains 32.

It does not decide:

- the full normalized column-sign family, where all six columns may use
  unrelated sign vectors;
- the row-sign family obtained by transposition;
- arbitrary complex row-homogeneous decompositions;
- tensor rank of the permanent; or
- unrestricted Chow rank.

This theorem does not supply the unrestricted improvement; N6-030 later changes
the proof-draft interval to `26..32` by an average-subset argument.
Novelty relative to all literature has not been established.

## 7. Deterministic reproduction

Run

```bash
python scripts/n6_one_defect_sign_rigidity_audit.py \
  --json /tmp/n6_one_defect_sign_rigidity_audit.json
python scripts/n6_one_defect_sign_independent_audit.py
python -m unittest tests.test_n6_one_defect_sign_rigidity -v
python -m unittest tests.test_n6_one_defect_sign_independent -v
```

Expected final markers:

```text
N6_ONE_DEFECT_SIGN_RIGIDITY_AUDIT_PASS
N6_ONE_DEFECT_SIGN_INDEPENDENT_AUDIT_PASS
```

The frozen payload is

```text
data/n6_one_defect_sign_rigidity_audit.json
```

The primary script uses modular elimination only to choose candidate pivot
rows and columns. Every rank lower bound entering the theorem is then
certified by a nonzero integer determinant computed with Bareiss elimination.
Rank upper bounds come from explicit kernel spaces. No random search, floating
threshold, or finite-field equality carries logical responsibility.

The independent script does not import the primary implementation. It uses a
different prime, reconstructs the six canonical parity fibers, verifies the
explicit five- and ten-dimensional kernel spaces, and obtains the matching
modular lower ranks. Thus the finite rank interface is replayed by two
independent implementations.
