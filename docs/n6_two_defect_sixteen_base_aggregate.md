# A 16-base aggregate representation in the `n=6` two-defect sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

N6-020 reduced the permanent to 24 nonzero base-labelled pairwise aggregate
spaces. N6-021 proved that directly decompressing that particular aggregate
assignment costs exactly 744 actual sign terms.

This note changes the aggregate assignment. It gives an exact representation
using only 16 nonzero base aggregates and supplies a fail-closed fixed-base
atomic-rank window for the new separator.

It does not prove that 16 is the minimum aggregate support and does not
determine the minimum number of two-defect terms. The unrestricted interval
remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. A count-product separator

For a row assignment

\[
r=(r_0,\ldots,r_5)\in\{0,\ldots,5\}^6,
\]

let

\[
n_i(r)=|\{j:r_j=i\}|.
\]

Define the pairwise function

\[
g(r)=n_4(r)n_5(r).
\tag{1.1}
\]

Equivalently,

\[
g(r)
=
\sum_{0\le j<k<6}
\left(
1_{r_j=4}1_{r_k=5}
+
1_{r_j=5}1_{r_k=4}
\right).
\tag{1.2}
\]

Thus `g` lies in the fixed-base two-defect aggregate space.

Let

\[
\pi(r)=e_{r_0}+\cdots+e_{r_5}
\in(\mathbb Z/2\mathbb Z)^5,
\qquad e_0=0.
\]

### Lemma 1.1 — target and zero fibers

\[
g|_{X_{31}}=1,
\qquad
g|_{X_7}=0,
\tag{1.3}
\]

where `X_p={r:pi(r)=p}`.

### Proof

On `X_31`, each of the five nonzero row values occurs an odd number of times.
Their total is at most six. The minimum odd total is five, and increasing any
one count by two would give at least seven. Therefore every nonzero value
occurs exactly once and row zero also occurs exactly once. In particular
`n_4=n_5=1`, so `g=1`.

On `X_7`, the counts of row values `1,2,3` are odd while the counts of `4,5`
are even. The first three counts already use at least three positions. If both
`n_4` and `n_5` were positive, their evenness would require at least four more
positions, exceeding six. Hence one of them is zero and `g=0`. ∎

The audit independently checks all 720 assignments in `X_31` and all 1,200
assignments in `X_7`.

## 2. Fourier construction with 16 bases

Write

\[
\chi_p(a)=(-1)^{p\cdot a},
\qquad a,p\in(\mathbb Z/2\mathbb Z)^5.
\]

For every normalized base label `a`, define

\[
W_a
=
\frac{\chi_{31}(a)-\chi_7(a)}{32}\,g.
\tag{2.1}
\]

For an assignment of parity `p`, character orthogonality gives

\[
\begin{aligned}
\sum_a\chi_p(a)W_a(r)
&=
1_{p=31}g(r)-1_{p=7}g(r).
\end{aligned}
\tag{2.2}
\]

By Lemma 1.1, this is one exactly on the permutation assignments and zero on
every other assignment. Hence (2.1) is an exact two-defect aggregate
representation of `perm_6`.

The coefficient is nonzero exactly when

\[
\chi_{31+7}(a)=\chi_{24}(a)=-1.
\]

Therefore the nonzero bases are

```text
8, 9, 10, 11, 12, 13, 14, 15,
16, 17, 18, 19, 20, 21, 22, 23.
```

The other 16 bases vanish. Thus:

### Proposition 2.1 — 16-base aggregate construction

The permanent lies in the sum of 16 base-labelled normalized two-defect
aggregate spaces.

The audit verifies equation (2.2) on all

\[
6^6=46656
\]

assignments using exact rational arithmetic.

No minimum statement is made: this proves aggregate support at most 16, not
that support below 16 is impossible.

## 3. Fixed-base atoms

Fix one base sign vector. After its common character is factored out, a
normalized two-defect atom is

\[
r\longmapsto s_v(r_j)s_w(r_k),
\qquad j<k,\quad v,w\in(\mathbb Z/2\mathbb Z)^5,
\tag{3.1}
\]

including one-defect and uniform cases when a defect is zero.

Let `rho_2(g)` be the minimum number of nonzero scalar multiples of such atoms
whose sum is `g`.

## 4. A strict lower bound of 31

Restrict every row value to

\[
\{0,4,5\}.
\tag{4.1}
\]

The three nonconstant normalized restricted sign patterns correspond to
defect labels

\[
8,16,24.
\]

Using row zero as baseline, their difference vectors are

\[
d_8=(-2,0),
\qquad
d_{16}=(0,-2),
\qquad
d_{24}=(-2,-2).
\tag{4.2}
\]

At every column pair, the pure ANOVA interaction block of `g` is

\[
M
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\tag{4.3}
\]

A restricted atom contributes one of the nine rank-one matrices
`d_v d_w^T`. Exact rational elimination over all one- and two-atom supports
gives

```text
compatible one-atom supports=0
compatible two-atom supports=1.
```

The unique two-atom expression is

\[
M
=
\frac14d_8d_{16}^T
+
\frac14d_{16}d_8^T.
\tag{4.4}
\]

Restoring the complete sign products, the constant and unary contribution of
(4.4) is

\[
\frac12
-
\frac12
\left(
1_{r_j=4}+1_{r_j=5}
+1_{r_k=4}+1_{r_k=5}
\right).
\tag{4.5}
\]

The 15 pure pair blocks form a direct sum. Therefore every representation of
`g` needs at least two pair-contributing atoms per block and hence at least 30
atoms.

If exactly 30 atoms were used, every pair would have to use the unique
expression (4.4), with no remaining unary or constant atom. Summing (4.5) over
all edges of `K_6` gives

\[
\frac{15}{2}
-
\frac52
\sum_{j=0}^{5}
\left(1_{r_j=4}+1_{r_j=5}\right).
\tag{4.6}
\]

But the baseline ANOVA expansion (1.2) of `g` has zero constant and zero unary
part. Hence 30 atoms are impossible, and

\[
\boxed{\rho_2(g)\ge31.}
\tag{4.7}
\]

The local finite interface contains only nine atoms and 45 supports of sizes
one or two. It is fully enumerated over `Q`.

## 5. An explicit 36-atom construction

For every pair `j<k`, use

\[
\frac14s_8(r_j)s_{16}(r_k)
+
\frac14s_{16}(r_j)s_8(r_k).
\tag{5.1}
\]

Across all 15 pairs, these 30 atoms give `g` plus the lower-order term in
(4.6). For each position `j`, add the one-defect atom

\[
-\frac54s_{24}(r_j).
\tag{5.2}
\]

Since

\[
s_{24}(r_j)
=
1-2\left(1_{r_j=4}+1_{r_j=5}\right),
\]

the six terms (5.2) cancel (4.6) exactly. Therefore

\[
\boxed{\rho_2(g)\le36.}
\tag{5.3}
\]

The audit expands the 36 atoms on all 46,656 assignments and obtains `g`
exactly.

Combining (4.7) and (5.3),

\[
\boxed{31\le\rho_2(g)\le36.}
\tag{5.4}
\]

No claim is made about which value in this interval is exact.

## 6. Actual cost of the 16-base assignment

All 16 nonzero aggregates in (2.1) are nonzero scalar multiples of `g`.
Nonzero scalar multiplication does not change atomic support. A normalized
term with zero, one, or two exceptional columns has a unique majority base, so
terms belonging to different base aggregates cannot be silently merged.

Consequently the actual sign-term cost of this fixed aggregate assignment lies
in

\[
16\cdot31
\le
\text{cost}
\le
16\cdot36,
\]

or

\[
\boxed{496\le\text{cost}\le576.}
\tag{6.1}
\]

This improves the explicit N6-020 assignment's exact cost 744 but remains far
above the 32-term Glynn decomposition.

## 7. Research decision

```text
NONZERO_BASE_AGGREGATES=16
SIXTEEN_BASE_REPRESENTATION=EXACT
SIXTEEN_BASE_MINIMALITY=NOT_PROVED
FIXED_BASE_SEPARATOR_ATOMIC_RANK=31..36
SPECIFIC_ASSIGNMENT_ACTUAL_TERM_COST=496..576
DECOMPOSITION_WITH_AT_MOST_25_TERMS_FOUND=false
GLOBAL_TWO_DEFECT_MINIMUM=OPEN
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
```

The construction shows that optimizing aggregate support alone is not enough:
a low-support aggregate can still have high fixed-base atomic rank.

The next useful target is one of:

1. close the small interval `31..36` for `rho_2(g)`; or
2. derive a joint aggregate-cost invariant that trades base support against
   fixed-base atomic complexity.

Neither target requires enumeration of the complete 467,264-term family.

## 8. Reproduction

Run

```bash
python scripts/n6_two_defect_sixteen_base_aggregate_audit.py \
  --json /tmp/n6_two_defect_sixteen_base_aggregate_audit.json
python -m unittest tests.test_n6_two_defect_sixteen_base_aggregate -v
```

Expected marker:

```text
N6_TWO_DEFECT_SIXTEEN_BASE_AGGREGATE_AUDIT_PASS
```

The frozen payload is

```text
data/n6_two_defect_sixteen_base_aggregate_audit.json
```
