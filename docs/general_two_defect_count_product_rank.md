# Exact atomic rank of count-product separators in the two-defect sign family

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_AGGREGATE_THEOREM`.

Let `n>=4`. Normalize the row-sign vectors by fixing the coefficient of row
zero to `+1`. Choose two distinct nonzero row labels `a,b`, and for an
`n`-column row assignment `r` put

\[
g_{a,b}(r)=n_a(r)n_b(r),
\]

where `n_i(r)` is the number of occurrences of row value `i`.

The main result is

\[
\boxed{\rho_2(g_{a,b})=n^2,}
\tag{0.1}
\]

where `rho_2` is fixed-base atomic rank in the normalized two-defect sign
dictionary.

The same count product gives a Fourier aggregate representation of
`perm_n` in exactly `2^(n-2)` nonzero base-labelled aggregate spaces. Its
canonical base-labelled decompression cost is

\[
\boxed{2^{n-2}n^2.}
\tag{0.2}
\]

For `n>=5`, every normalized term with at most two defects has a unique
majority base, so (0.2) is also the exact actual cost of that fixed aggregate
assignment after identical terms are collected. For `n=4`, the fixed-base
theorem and the base-labelled cost remain exact, but cross-base collection is
not classified here.

For `n=6`, this supplies a second, shorter proof of the N6-023 value

\[
\rho_2(n_4n_5)=36
\]

and of the exact cost `16*36=576`. The existing N6-023 exhaustive
normal-form and meet-in-the-middle certificate remains an independent replay.

This is not a theorem about the global two-defect family, row-homogeneous
tensor rank, or unrestricted Chow rank. The active unrestricted `n=6`
interval remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Fixed-base atoms and the valid restriction

Let

\[
G=(\mathbb Z/2\mathbb Z)^{n-1}
\]

index the normalized sign vectors. After one majority base label has been
factored out, a fixed-base atom is a constant, a one-position sign function,
or a two-position product

\[
1,
\qquad
s_v(r_j),
\qquad
s_v(r_j)s_w(r_k),
\quad j<k.
\tag{1.1}
\]

The coefficient multiplying an atom is arbitrary. The support count records
only distinct atoms with nonzero collected coefficients.

Restrict every row value to

\[
\{0,a,b\}.
\tag{1.2}
\]

The full sign family collapses to four local patterns, each with multiplicity
`2^(n-3)` before equal terms are collected:

\[
1,
\qquad
A=1-2h,
\qquad
B=1-2k,
\qquad
C=1-2h-2k,
\tag{1.3}
\]

where

\[
h=1_{r=a},
\qquad
k=1_{r=b}.
\]

The three nonconstant difference vectors are

\[
d_A=(-2,0),
\qquad
d_B=(0,-2),
\qquad
d_C=(-2,-2).
\tag{1.4}
\]

Equal restricted atoms may combine, so restriction cannot increase support.
Conversely the four-pattern dictionary is a literal subdictionary of the full
normalized sign dictionary. Hence the full and restricted fixed-base atomic
ranks of `g_ab` are equal.

Ordinary atoms are the constant and the one-position patterns. A pair atom
means an atom whose two restricted factors are both nonconstant. Its pure ANOVA
block belongs to a unique unordered column pair. Atoms with one constant
factor have zero pure block and are counted with the ordinary one-position
atoms.

## 2. Pair blocks of the target

On the restricted domain,

\[
g_{a,b}
=
\sum_{0\le j<k<n}
\left(h_jk_k+k_jh_k\right).
\tag{2.1}
\]

It has zero constant and unary ANOVA parts. Every column pair has the pure
interaction block

\[
M=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\tag{2.2}
\]

A pair atom `P_jQ_k`, with `P,Q in {A,B,C}`, contributes

\[
d_Pd_Q^{\mathsf T}.
\tag{2.3}
\]

Since `rank M=2`, every pair needs at least two pair atoms. There are
`binom(n,2)` pairs, so the baseline pair support is

\[
2\binom n2=n(n-1).
\tag{2.4}
\]

## 3. Exact local support data

There are only nine local pure atoms. Exact rational elimination gives

```text
support size 1:  0 compatible supports
support size 2:  1 compatible support
support size 3: 18 compatible supports
```

Eleven of the compatible three-supports have all coefficients nonzero. The
unique two-atom expression is

\[
M
=
\frac14d_Ad_B^{\mathsf T}
+
\frac14d_Bd_A^{\mathsf T},
\tag{3.1}
\]

and its unary contribution at either endpoint is

\[
u_2=
\left(-\frac12,-\frac12\right).
\tag{3.2}
\]

The complete histogram of first-endpoint unary vectors from compatible
three-supports is

```text
(-1/2,-1/2): 9
(0,-1/2):     3
(-1/2,0):     3
(0,0):        1
(-1,-1/2):    1
(-1/2,-1):    1
```

Every coordinate is nonpositive. Transposing a local expression exchanges the
two endpoints and preserves the dictionary and the symmetric target block
`M`. Therefore the same coordinatewise nonpositivity holds at the second
endpoint of every compatible three-support.

A second exact classification treats an unknown equal unary target `(t,t)`.
For every support of size at most four, solve

\[
\sum \lambda_{P,Q}d_Pd_Q^{\mathsf T}=M,
\qquad
\sum \lambda_{P,Q}d_P=(t,t).
\tag{3.3}
\]

Among all compatible supports, the only possible values are

```text
t=0:    10 supports
t=-1/2: 42 supports.
```

Thus no support of size at most four can produce a positive equal unary vector
at either endpoint; the second-endpoint statement again follows by
transposition.

The complete theorem-bearing finite interface consists of the nine atoms and
at most

\[
\sum_{i=1}^{4}\binom9i=255
\]

supports. No global support enumeration enters the proof.

## 4. A general star lemma

### Lemma 4.1 — zero-unary star cost

Let `d>=3` copies of the pure block `M` meet at one vertex. If their total
pair-generated unary vector at that vertex is zero, their total incident pair
support is at least

\[
2d+3.
\tag{4.1}
\]

The bound is sharp.

### Proof

Every edge needs at least two atoms.

- With support `2d`, every edge uses (3.1), so the center unary is
  `(-d/2,-d/2)`, not zero.
- With support `2d+1`, one edge uses three atoms and the other `d-1` edges use
  (3.1). The modified edge is coordinatewise nonpositive at the center,
  while the baseline contribution is strictly negative.
- With support `2d+2`, either two edges use three atoms or one edge uses four.
  In the first case, the `d-2>=1` baseline edges are strictly negative and
  both modified contributions are nonpositive. In the second case, the
  four-atom edge would have to supply
  \[
  \left(\frac{d-1}{2},\frac{d-1}{2}\right),
  \]
  a positive equal unary vector, excluded by (3.3).

The argument is independent of whether the center is the first or second
endpoint because Section 3 is transpose symmetric.

For sharpness, use the five atoms

\[
(A,B),
(B,A),
(C,A),
(C,B),
(C,C)
\]

with coefficients

\[
\frac14,
\frac14,
-\frac d4,
-\frac d4,
\frac d4.
\tag{4.2}
\]

They produce the pure block `M` and center unary

\[
\left(\frac{d-1}{2},\frac{d-1}{2}\right).
\]

Together with `d-1` baseline edges, this gives zero center unary with support

\[
5+2(d-1)=2d+3.
\]

∎

## 5. Global lower bound

Consider an arbitrary restricted expression of `g_ab`. For each edge `e`, let
`m_e` be the number of collected pair atoms whose pure block belongs to `e`,
and put

\[
E=\sum_e(m_e-2)\ge0.
\tag{5.1}
\]

The total pair support is `n(n-1)+E`.

Let `u_j` be the unary vector generated at vertex `j` by incident pair atoms,
and let

\[
Z=|\{j:u_j=0\}|.
\tag{5.2}
\]

Every vertex has star degree `n-1>=3`. By Lemma 4.1, each zero-unary vertex
has incident pair excess at least three. Summing over zero vertices counts an
edge excess at most at its two endpoints, hence

\[
3Z\le2E.
\tag{5.3}
\]

Every nonzero `u_j` requires at least one ordinary atom at position `j`.
A constant atom cannot cancel a unary coefficient, and ordinary atoms at
different positions are distinct. Therefore ordinary unary support is at
least `n-Z`.

Ignoring any extra constant atom only weakens the bound. If `R` is total
support, then

\[
\begin{aligned}
R
&\ge n(n-1)+E+n-Z\\
&=n^2+E-Z.
\end{aligned}
\tag{5.4}
\]

Since (5.3) implies `Z<=floor(2E/3)<=E`,

\[
\boxed{R\ge n^2.}
\tag{5.5}
\]

## 6. Matching construction

For every pair `j<k`, use

\[
\frac14A(r_j)B(r_k)
+
\frac14B(r_j)A(r_k).
\tag{6.1}
\]

These `n(n-1)` pair atoms produce all pure blocks. Their lower-order part is

\[
\frac{n(n-1)}4
-
\frac{n-1}{2}
\sum_{j=0}^{n-1}(h_j+k_j).
\tag{6.2}
\]

At each position add

\[
-\frac{n-1}{4}C(r_j).
\tag{6.3}
\]

Since `C=1-2h-2k`, the `n` ordinary atoms cancel (6.2) exactly. The
construction uses

\[
n(n-1)+n=n^2
\]

atoms. Together with (5.5):

### Theorem 6.1 — general count-product rank

For every `n>=4`, every characteristic-zero field, and every two distinct
nonzero row labels `a,b`,

\[
\boxed{\rho_2(n_an_b)=n^2.}
\]

## 7. The corresponding permanent aggregate assignment

Let

\[
p_*=2^{n-1}-1
\]

be the parity vector with every nonzero row bit set. Let `q` be obtained by
clearing the bits of rows `a,b`.

On the target fiber `X_{p_*}`, all `n-1` nonzero row counts are odd. With only
`n` columns, every nonzero row and row zero occurs exactly once. Hence

\[
g_{a,b}|_{X_{p_*}}=1.
\tag{7.1}
\]

On `X_q`, the other `n-3` nonzero row counts are odd while the counts of `a,b`
are even. The odd rows use at least `n-3` positions. If both `n_a,n_b` were
positive, their evenness would require four additional positions, for a total
of at least `n+1`. Therefore

\[
g_{a,b}|_{X_q}=0.
\tag{7.2}
\]

Define

\[
W_x
=
\frac{\chi_{p_*}(x)-\chi_q(x)}{2^{n-1}}g_{a,b}.
\tag{7.3}
\]

Character orthogonality shows that the sum of the base-labelled aggregates is
exactly the permanent coefficient function. The coefficient in (7.3) is
nonzero on exactly

\[
2^{n-2}
\]

base labels. Each nonzero aggregate is a scalar multiple of `g_ab` and has
atomic rank `n^2`. Therefore the canonical base-labelled decompression cost is

\[
\boxed{2^{n-2}n^2.}
\tag{7.4}
\]

When `n>=5`, at most two exceptional columns leave at least three copies of
the majority base. Two different labels cannot both occur at least `n-2`
times. Hence a normalized term has a unique majority base, terms from
different base aggregates cannot become identical after collection, and
(7.4) is the exact actual cost of this fixed assignment.

For `n=4`, a two-defect term can split as two columns versus two columns; the
fixed-base cost 16 and base-labelled cost 64 are exact, but this note does not
determine the post-collection cost.

## 8. Deterministic evidence and claim boundary

The primary audit independently reconstructs the nine local pure atoms,
classifies every support of size at most four over `Q`, verifies the sharp
star examples for degrees 3 through 9, checks the integer lower-bound formula
through `n=20`, and expands both the atomic construction and aggregate identity
on every assignment for `n=4,5,6`.

A second implementation does not import the primary generator. It rebuilds the
local atoms from their three-value truth tables, reruns the support and
equal-unary classifications, checks the sharp star examples, and replays all
`6^6` values in the `n=6` corollary.

The existing N6-023 exhaustive certificate is a third, structurally different
check of the `n=6` value 36.

The theorem does not prove:

- that `2^(n-2)` is minimum aggregate support;
- that every two-defect aggregate has rank at least `n^2`;
- a lower bound for every two-defect decomposition;
- row-homogeneous tensor-rank optimality; or
- an unrestricted Chow-rank improvement.

The appropriate status is `RESTRICTED_AGGREGATE_THEOREM`.

## 9. Reproduction

Run

```bash
python scripts/general_two_defect_count_product_rank_audit.py \
  --json /tmp/general_two_defect_count_product_rank_audit.json
python scripts/general_two_defect_count_product_rank_independent.py
python -m unittest tests.test_general_two_defect_count_product_rank -v
```

Expected final markers:

```text
GENERAL_TWO_DEFECT_COUNT_PRODUCT_RANK_AUDIT_PASS
GENERAL_TWO_DEFECT_COUNT_PRODUCT_INDEPENDENT_AUDIT_PASS
```

No random search, floating threshold, or finite-field equality carries theorem
responsibility.
