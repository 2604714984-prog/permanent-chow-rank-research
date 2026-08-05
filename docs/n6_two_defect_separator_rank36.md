# Exact fixed-base atomic rank of the `n=6` count-product separator

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`RESTRICTED_AGGREGATE_THEOREM`.

N6-022 constructed an exact 16-base aggregate representation of
`perm_6` from the pairwise function

\[
g(r)=n_4(r)n_5(r),
\]

and proved only

\[
31\le \rho_2(g)\le36.
\]

Here `rho_2` is the minimum number of normalized sign atoms with zero, one,
or two exceptional columns after one base sign character has been factored
out. This note closes that interval:

### Theorem 1 — exact fixed-base rank

Over every characteristic-zero field,

\[
\boxed{\rho_2(g)=36.}
\]

Consequently the particular 16-base aggregate assignment from N6-022 has
exact actual term cost

\[
\boxed{16\cdot36=576.}
\]

This is not a theorem about all two-defect decompositions of `perm_6` and does
not change the unrestricted interval

\[
25\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 1. Fixed-base atoms

Let

\[
G=(\mathbb Z/2\mathbb Z)^5,
\]

and write the normalized row sign vector indexed by `v in G` as

\[
s_v(0)=1,
\qquad
s_v(i)=(-1)^{v_i}
\quad(1\le i\le5).
\]

After a common base character has been removed, a fixed-base atom is one of

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
only atoms with nonzero coefficients.

The separator is

\[
g(r)
=
\sum_{j<k}
\left(
1_{r_j=4}1_{r_k=5}
+
1_{r_j=5}1_{r_k=4}
\right).
\tag{1.2}
\]

## 2. Retraction to four sign labels

Define a retraction of the six row values by

\[
q(0)=q(1)=q(2)=q(3)=0,
\qquad
q(4)=4,
\qquad
q(5)=5.
\tag{2.1}
\]

Let `P` act on a one-variable function by precomposition:

\[
(Pf)(r)=f(q(r)).
\]

### Lemma 2.1 — sign-label projection

For every `v in G`,

\[
P(s_v)=s_{v\mathbin{\&}24}.
\tag{2.2}
\]

Thus every sign vector is sent to one of

\[
1,\ s_8,\ s_{16},\ s_{24}.
\]

Moreover,

\[
P^{\otimes6}(g)=g.
\tag{2.3}
\]

### Proof

Rows `1,2,3` are evaluated at row zero, where every normalized sign vector has
value one. Rows four and five are unchanged, so only the two corresponding
bits survive; this is exactly the mask `v & 24`. The function `g` depends only
on the numbers of row values four and five, which the retraction preserves. ∎

Applying `P` in all six positions sends every full fixed-base atom to a
restricted atom and cannot increase support. Conversely the restricted
four-label dictionary is a subdictionary of the full one. Therefore:

### Corollary 2.2

The full fixed-base atomic rank of `g` equals its rank in the restricted label
set

\[
\{0,8,16,24\}.
\tag{2.4}
\]

This reduction is mathematical; the audit separately checks all 192
sign-vector values and all `6^6=46656` values of `g`.

## 3. One-edge ANOVA model

Set

\[
A=s_8,
\qquad
B=s_{16},
\qquad
C=s_{24}.
\]

On row values `{0,4,5}`, use row zero as the ANOVA baseline. The nonconstant
difference vectors are

\[
d_A=(-2,0),
\qquad
d_B=(0,-2),
\qquad
d_C=(-2,-2).
\tag{3.1}
\]

For one ordered column pair, the pure interaction block of `g` is

\[
M=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\tag{3.2}
\]

There are nine nonconstant pair atoms, with pure blocks

\[
d_Xd_Y^{\mathsf T},
\qquad X,Y\in\{A,B,C\}.
\]

The unique two-atom representation is

\[
M
=
\frac14d_Ad_B^{\mathsf T}
+
\frac14d_Bd_A^{\mathsf T}.
\tag{3.3}
\]

Its complete lower-order contribution is

\[
\frac12
-
\frac12(X_j+Y_j+X_k+Y_k),
\tag{3.4}
\]

where `X_j=1_{r_j=4}` and `Y_j=1_{r_j=5}`.

Using (3.3) on all 15 edges gives 30 pair atoms. Their lower-order part is

\[
\frac{15}{2}
-
\frac52
\sum_{j=0}^{5}(X_j+Y_j).
\tag{3.5}
\]

The correction required to recover `g` has scaled ANOVA vector

```text
constant=-30
at every vertex: X coefficient=10, Y coefficient=10
```

where the displayed integers are four times the actual coefficients.

## 4. Exact local normal forms

For every subset of the nine pair atoms, the audit solves over `Q` the linear
system requiring its pure block to equal `M`. A support is retained exactly
when the affine solution space is nonempty and no selected coordinate is
identically zero. This reconstructs 243 support-affine spaces:

| pair support | affine dimension | number of spaces |
|---:|---:|---:|
| 2 | 0 | 1 |
| 3 | 0 | 11 |
| 4 | 0 | 20 |
| 4 | 1 | 10 |
| 5 | 1 | 77 |
| 5 | 2 | 2 |
| 6 | 2 | 76 |
| 7 | 3 | 36 |
| 8 | 4 | 9 |
| 9 | 5 | 1 |

The lower-order image of each support is another affine space in the
five-dimensional space

\[
(\text{constant},X_j,Y_j,X_k,Y_k).
\]

A local compression is valid when this entire affine image is contained in

\[
\text{lower image of a size-two or size-three pair representation}
+
\text{span of no more than the saved number of ordinary atoms}.
\tag{4.1}
\]

Containment in (4.1) is checked by exact rational rank tests, not by sampling.
Of the 231 support spaces of size at least four, 227 compress. The four
exceptions are the supports

```text
(0,5,7,8)
(2,4,6,8)
(0,2,4,6,8)
(0,4,5,7,8)
```

in row-major order on

```text
AA, AB, AC,
BA, BB, BC,
CA, CB, CC.
```

Four of the eleven size-three forms differ from (3.3) by one ordinary atom and
are absorbed without changing cost. Every global representation can therefore
be normalized, without increasing support, to the baseline (3.3) plus the
following modifications.

### Cost-one point bundles

There are seven local lower-order vectors, scaled by four:

```text
(-3, 2, 2, 2, 2)
(-2, 0, 2, 0, 2)
(-2, 2, 0, 2, 0)
( 0,-2, 0, 2, 0)
( 0, 0,-2, 0, 2)
( 0, 0, 2, 0,-2)
( 0, 2, 0,-2, 0)
```

Using one on an edge costs one atom beyond the two-atom baseline.

### Cost-two point bundles

```text
(-4,2,4,2,4)
(-4,4,2,4,2)
```

### Cost-three affine bundles

```text
base=(-2,0,2,0,2), direction=(-4,8,0,8,0)
base=(-2,2,0,2,0), direction=(-4,0,8,0,8)
```

The parameter is arbitrary. Allowing every parameter value is conservative;
special values that reduce support have already been covered by smaller local
supports.

## 5. Ordinary lower-order support

The ordinary restricted atoms are

\[
1,
\qquad
A_j,
\qquad
B_j,
\qquad
C_j
\quad(0\le j<6).
\]

For a lower-order function

\[
c+\sum_j(x_jX_j+y_jY_j),
\]

write its coefficients at vertex `j` as

\[
a_jA_j+b_jB_j+t_jC_j.
\]

Then

\[
a_j=-\frac{x_j}{2}-t_j,
\qquad
b_j=-\frac{y_j}{2}-t_j.
\tag{5.1}
\]

Consequently the minimum local support is

- zero when `(x_j,y_j)=(0,0)`;
- one when `x_j=0`, `y_j=0`, or `x_j=y_j`;
- two otherwise.

In the two-support case, the possible constant contributions at minimum local
support are

\[
-\frac{x_j}{2},
\qquad
-\frac{y_j}{2},
\qquad
-\frac{x_j+y_j}{2}.
\tag{5.2}
\]

The global minimum is the sum of the six local minima, plus zero when the
target constant belongs to the Minkowski sum of the allowed constants and
plus one otherwise. This gives an exact closed formula for the ordinary
correction cost. In particular, the baseline correction (3.5) needs exactly
six atoms, namely one `C_j` atom at every vertex.

## 6. Exhaustion of support at most 35

A hypothetical representation with at most 35 atoms has, after local
normalization,

\[
30+e+q\le35,
\tag{6.1}
\]

where `e` is the total modification cost and `q` is ordinary lower-order
support. Hence only `e+q<=5` must be checked.

There are 105 cost-one point bundles, 30 cost-two point bundles, and 30
cost-three affine bundles after assigning local types to the 15 edges. At most
one modification may be chosen on any edge.

All cases are exact and finite.

### Only cost-one point bundles

| number chosen | configurations covered | required ordinary budget |
|---:|---:|---:|
| 1 | 105 | at most 4 |
| 2 | 5,145 | at most 3 |
| 3 | 156,065 | at most 2 |
| 4 | 3,277,365 | at most 1 |
| 5 | 50,471,421 | zero |

The first three rows use the exact formula in Section 5. The fourth checks all
configurations directly. The fifth uses an exact meet-in-the-middle table of
5,145 two-bundle sums and 156,065 three-bundle sums, with disjoint-edge masks.
No target complement occurs.

### Mixtures with cost-two point bundles

The audit covers

```text
30 * 14 * 7                 = 2,940
30 * C(14,2) * 7^2          = 133,770
30 * C(14,3) * 7^3          = 3,745,560
C(15,2) * 2^2               = 420
C(15,2) * 2^2 * 13 * 7      = 38,220
```

configurations for the possible distributions of one or two cost-two bundles
and the remaining cost-one bundles. Exact ordinary-support tests and hash
complements exclude every case with total extra cost at most five.

### One cost-three affine bundle

Two affine types on each of 15 edges give 30 cases. Since two affine bundles
already cost six, at most one occurs. The exact tests are:

```text
5,730   affine plus at most two ordinary atoms
58,800  affine plus one cost-one bundle and at most one ordinary atom
133,770 affine plus two cost-one bundles and no ordinary atom
840     affine plus one cost-two bundle and no ordinary atom
```

Each test is a rational affine-span or affine-zero calculation. None is
feasible.

The cases above exhaust (6.1). Therefore no representation with at most 35
atoms exists, and

\[
\rho_2(g)\ge36.
\tag{6.2}
\]

## 7. The 36-atom upper bound

For each edge `j<k`, take

\[
\frac14A_jB_k+rac14B_jA_k.
\tag{7.1}
\]

These are 30 pair atoms. At every vertex add

\[
-\frac54C_j.
\tag{7.2}
\]

Equations (3.5) and (7.2) cancel the complete lower-order part, leaving exactly
`g`. The audit checks the identity on all 46,656 assignments. Thus

\[
\rho_2(g)\le36.
\tag{7.3}
\]

Combining (6.2) and (7.3) proves Theorem 1.

## 8. Consequence for the 16-base construction

N6-022 uses 16 distinct majority-base labels, and every nonzero aggregate is a
nonzero scalar multiple of `g`. A normalized term with at most two exceptional
columns has a unique majority base, appearing in at least four columns.
Therefore atoms from different base aggregates cannot be the same normalized
term and cannot be silently merged across bases.

The exact cost is consequently

\[
16\rho_2(g)
=16\cdot36
=\boxed{576}.
\]

This closes the specific N6-022 construction as a route to a short
decomposition. It remains a valid span and Fourier-support certificate.

## 9. Claim boundary and next route

The theorem proves only

```text
FIXED_BASE_SEPARATOR_ATOMIC_RANK=36
N6_022_SPECIFIC_ASSIGNMENT_ACTUAL_TERM_COST=576
```

It does not prove

- that 16 is the minimum aggregate support;
- that every aggregate assignment costs at least 576;
- that the global two-defect sign rank is 32;
- row-homogeneous tensor-rank optimality; or
- unrestricted Chow rank 32.

The direct separator constructions now have exact costs 744 and 576, both far
above Glynn's 32 terms. Further sign-family work requires a joint invariant on
the entire vector-valued aggregate assignment, not another low-base separator
whose fixed-base rank is analyzed only afterward. A broad sparse solver or
enumeration of all 467,264 terms remains unauthorized.

## 10. Reproduction

Run

```bash
python scripts/n6_two_defect_separator_rank36_audit.py \
  --json /tmp/n6_two_defect_separator_rank36_audit.json
python -m unittest tests.test_n6_two_defect_separator_rank36 -v
```

Expected marker:

```text
N6_TWO_DEFECT_SEPARATOR_RANK36_AUDIT_PASS
```

The frozen payload is

```text
data/n6_two_defect_separator_rank36_audit.json
```

The audit uses only the Python standard library and exact `Fraction`
elimination. The largest direct point-bundle layer contains 3,277,365
configurations; the 50,471,421 five-bundle layer is covered by an exact
meet-in-the-middle certificate. No floating-point optimizer, random sample,
or finite-field equality is used.
