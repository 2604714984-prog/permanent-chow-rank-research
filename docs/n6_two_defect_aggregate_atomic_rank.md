# Atomic rank of the explicit `n=6` two-defect aggregate formula

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_AGGREGATE_THEOREM`.

N6-020 gives an exact representation of `perm_6` in 24 nonzero
base-labelled two-defect **aggregate spaces**. It explicitly does not give a
24-term Chow decomposition. This note determines the actual fixed-base sign
term cost of that particular aggregate assignment.

Let `f` be the quadratic separator from N6-020:

\[
f(r)
=
1-\frac14\sum_{j=0}^{5}1_{r_j\in\{2,3\}}
+\frac12\sum_{0\le j<k<6}z_jz_k,
\qquad
z_j=1_{r_j=2}-1_{r_j=3}.
\tag{1.1}
\]

Then, over every characteristic-zero field,

\[
\boxed{
\rho_2(f)=46,
\qquad
\rho_2(1-f)=46,
}
\tag{1.2}
\]

where `rho_2` is the minimum number of normalized two-defect sign atoms in a
single fixed-base aggregate.

Consequently, decompression of the exact N6-020 24-base aggregate assignment
requires

\[
\boxed{8+16\cdot46=744}
\tag{1.3}
\]

actual sign terms. This is not a lower bound for every possible two-defect
decomposition. It closes only the explicit aggregate construction of N6-020.
The unrestricted interval remains

\[
26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Fixed-base atoms

Fix a normalized base sign vector `a`. After the common base character is
factored out, a two-defect term contributes a coefficient function

\[
r\longmapsto s_v(r_j)s_w(r_k),
\qquad 0\le j<k<6,\quad v,w\in(\mathbb Z/2\mathbb Z)^5.
\tag{1.4}
\]

The cases `v=0` or `w=0` include one-defect functions, and `v=w=0`
gives the constant function. A scalar multiple of (1.4) is one actual
normalized sign term with the fixed base `a`.

Define `rho_2(g)` as the minimum number of nonzero scalar multiples of such
atoms whose sum is `g`.

For a term with exactly two exceptional columns, the four-column majority
base is unique. The same is true for one-defect and uniform terms. Therefore,
once a base-labelled aggregate assignment `W_a` is fixed, its actual term cost
is the sum of the separate fixed-base atomic ranks `rho_2(W_a)`.

## 2. Restriction to three row values

For a lower bound, restrict every row variable to the alphabet

\[
\{0,2,3\}.
\tag{2.1}
\]

Restriction cannot increase support: a full six-row expression with `m` terms
would give a restricted expression with at most `m` terms after identical
restricted atoms are collected.

On (2.1), the nonconstant normalized sign patterns are

\[
A=(1,-1,1),
\qquad
B=(1,1,-1),
\qquad
C=(1,-1,-1),
\tag{2.2}
\]

corresponding to defect labels `2`, `4`, and `6`.

Use the baseline value at row zero. For a one-variable sign pattern `P`, put

\[
d_P=(P(2)-P(0),P(3)-P(0)).
\]

Then

\[
d_A=(-2,0),
\qquad
d_B=(0,-2),
\qquad
d_C=(-2,-2).
\tag{2.3}
\]

The pure pair-interaction block of an atom `P(r_j)Q(r_k)` is
`d_Pd_Q^T`. At every one of the 15 column pairs, the pure interaction of `f`
is

\[
M
=
\frac12
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\tag{2.4}
\]

Terms depending on fewer than two nonconstant positions have zero pure block.
The ANOVA pure blocks belonging to different column pairs form a direct sum.

## 3. Exact local three-atom classification

There are only nine local pure atoms

\[
d_Pd_Q^T,
\qquad P,Q\in\{A,B,C\}.
\]

Exact rational elimination over all supports gives:

```text
compatible one-atom supports=0
compatible two-atom supports=0
compatible three-atom supports=2
```

The two three-atom expressions are

\[
M
=
\frac14\,d_Ad_A^T
+
\frac14\,d_Bd_B^T
-
\frac18\,d_Cd_C^T,
\tag{3.1}
\]

and

\[
M
=
-rac14\,d_Ad_B^T
-
\frac14\,d_Bd_A^T
+
\frac18\,d_Cd_C^T.
\tag{3.2}
\]

The finite interface has only

\[
\binom91+inom92+inom93=129
\]

supports, including 84 triples. The audit solves every system over `Q`; no
floating threshold or finite-field equality is involved.

Let

\[
h_j=1_{r_j\in\{2,3\}}.
\]

When the complete sign products, rather than only their pure blocks, are
inserted in (3.1), their constant and unary contribution is

\[
u_{jk}
=
\frac38-rac14(h_j+h_k).
\tag{3.3}
\]

Expression (3.2) contributes `-u_jk`. Thus every minimum three-atom
realization of the pure block (2.4) has exactly one of the two lower-order
signs

\[
\varepsilon_{jk}u_{jk},
\qquad
\varepsilon_{jk}\in\{+1,-1\}.
\tag{3.4}
\]

## 4. Forty-five atoms are impossible

Since all 15 pair blocks of `f` equal the nonzero matrix `M`, Section 3 gives

\[
\rho_2(f)\ge15\cdot3=45.
\tag{4.1}
\]

Suppose equality held. Then every term would be used in one of the 15 pair
blocks, every pair would use exactly three atoms, and no additional unary or
constant atom would remain. Assign the sign `epsilon_jk` from (3.4).

The target unary coefficient of every `h_j` in (1.1) is `-1/4`. Comparing
with (3.3) forces the signed degree equation

\[
\sum_{k\ne j}\varepsilon_{jk}=1
\qquad(0\le j<6).
\tag{4.2}
\]

Summing (4.2) over the six vertices gives

\[
2\sum_{j<k}\varepsilon_{jk}=6,
\qquad
\sum_{j<k}\varepsilon_{jk}=3.
\tag{4.3}
\]

The constant supplied by all 15 three-atom blocks is therefore

\[
\frac38\sum_{j<k}\varepsilon_{jk}
=
\frac98,
\tag{4.4}
\]

whereas the target constant in (1.1) is one. This contradiction proves

\[
\rho_2(f)\ge46.
\tag{4.5}
\]

The audit also enumerates all `2^15=32768` signed edge assignments. Exactly 70
satisfy all six equations (4.2), and every one has signed edge sum three, as
forced by the hand argument.

The same reasoning applies to `1-f`: its pure blocks are `-M`; matching its
six unary coefficients forces signed degree `-1` at every vertex and constant
`-9/8`, whereas its target constant is zero. Hence

\[
\rho_2(1-f)\ge46.
\tag{4.6}
\]

## 5. Exact 46-atom constructions

Take the positive edges to be the nine edges of

\[
K_{3,3}
\quad	ext{on}\quad
\{0,1,2\}\mid\{3,4,5\},
\tag{5.1}
\]

and take the six within-part edges as negative. Every vertex then has three
positive and two negative incident edges, so its signed degree is one.

On each positive edge use the complete sign-product version of (3.1); on each
negative edge use the version of (3.2). This uses 45 atoms, supplies all pure
pair blocks and all target unary coefficients, and has constant `9/8`.
Adding the uniform atom with coefficient `-1/8` gives exactly `f`.
Therefore

\[
\rho_2(f)\le46.
\]

Together with (4.5),

\[
\boxed{\rho_2(f)=46.}
\tag{5.2}
\]

Negating the 45 pair atoms and replacing the uniform coefficient by `9/8`
gives `1-f`, so

\[
\boxed{\rho_2(1-f)=46.}
\tag{5.3}
\]

The audit checks both identities on all

\[
6^6=46656
\]

row assignments using exact rational arithmetic.

## 6. Exact cost of the N6-020 aggregate assignment

The N6-020 formula has

\[
W_a
=
\frac1{32}
\left[
\chi_{31}(a)-\chi_{25}(a)
+
\bigl(\chi_{25}(a)-\chi_7(a)\bigr)f
\right].
\tag{6.1}
\]

Its coefficient-type histogram is

| numerator pair `(constant, f)` | number of bases | aggregate type |
|---:|---:|---|
| `(0,0)` | 8 | zero |
| `(-2,0)`, `(2,0)` | 8 | nonzero constant |
| `(0,-2)`, `(0,2)` | 8 | nonzero scalar multiple of `f` |
| `(-2,2)`, `(2,-2)` | 8 | nonzero scalar multiple of `1-f` |

A nonzero constant has atomic rank one, while nonzero scalar multiplication
does not change atomic support. Therefore the exact actual-term cost of this
fixed aggregate assignment is

\[
8\cdot1+16\cdot46
=
\boxed{744}.
\tag{6.2}
\]

The eight zero bases remain

```text
0, 1, 6, 7, 24, 25, 30, 31.
```

Thus the 24-base aggregate formula is a valid linear-span certificate but a
very poor rank-one construction.

## 7. Research decision

```text
SEPARATOR_ATOMIC_RANK=46
ONE_MINUS_SEPARATOR_ATOMIC_RANK=46
N6_020_EXPLICIT_AGGREGATE_ACTUAL_TERM_COST=744
N6_020_FORMULA_CAN_YIELD_AT_MOST_25_TERMS=false
GLOBAL_TWO_DEFECT_MINIMUM=OPEN
BROAD_SPARSE_OPTIMIZATION_AUTHORIZED=false
```

The correct next target is no longer to decompress (6.1). It is to optimize
the base-aggregate assignment itself under the 32 Fourier-fiber equations.
Any further executable work must first reduce that problem to a compact exact
code or orbit interface. This theorem does not authorize enumeration of the
467,264-term dictionary or a generic sparse solver.

## 8. Claim boundary

The rank-46 statements are exact for the fixed-base functions `f` and `1-f`.
Equation (6.2) is exact only after the N6-020 aggregate assignment `W_a` is
fixed. Another aggregate assignment may have a different atomic cost.

No new unrestricted Chow-rank lower bound or upper bound is claimed.

## 9. Reproduction

Run

```bash
python scripts/n6_two_defect_aggregate_atomic_rank_audit.py \
  --json /tmp/n6_two_defect_aggregate_atomic_rank_audit.json
python -m unittest tests.test_n6_two_defect_aggregate_atomic_rank -v
```

Expected marker:

```text
N6_TWO_DEFECT_AGGREGATE_ATOMIC_RANK_AUDIT_PASS
```

The frozen payload is

```text
data/n6_two_defect_aggregate_atomic_rank_audit.json
```
