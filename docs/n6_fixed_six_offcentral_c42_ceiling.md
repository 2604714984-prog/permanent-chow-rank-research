# The fixed-six off-central `C_(4,2)` ceiling

**Status.** `PROOF_DRAFT_COMPLETE`, `EXACT_ARITHMETIC_REPLAYED`,
`LOWER_27_ROUTE_CEILING` (N6-038).  The argument is over a
characteristic-zero field.  It proves that the proposed universal criterion
`rank C_(4,2)(Q)>20*15` cannot attack the twenty-term residual.  It does **not** prove
`ChowRank(perm_6)>=27`, construct a decomposition, or make a border-rank
claim.

## 1. Setup

Assume hypothetically that the N6-032 reduction has produced

\[
 P=\operatorname{perm}_6=R+Q,
 \qquad R=T_1+\cdots+T_6,
 \qquad Q=T_7+\cdots+T_{26}.
\tag{1.1}
\]

Put

\[
 E_m=\mathcal D_m(P),\qquad
 H_m=\mathcal D_m(R),\qquad
 G_m=\mathcal D_m(Q),
\tag{1.2}
\]

and write

\[
 h=\dim H_3,\qquad
 b=\dim(E_3\cap H_3).
\tag{1.3}
\]

The surviving range is

\[
 45\le b\le64.
\tag{1.4}
\]

At quadratic and quartic degree define

\[
 d_2=\dim H_2=\dim H_4,
 \quad a_2=\dim(E_2\cap H_2),
 \quad t_2=d_2-a_2,
 \quad j_4=\dim(E_4\cap H_4).
\tag{1.5}
\]

The equality of the two ranks in (1.5) is transposition of the two
complementary catalecticants of `R`.

## 2. The missing upper bound on `t_2`

Let

\[
 S=E_3\cap H_3.
\]

Every first derivative of `S` lies in both `E_2` and `H_2`.  If `m_b` is the
exact integer Bukh-shadow lower bound for a `b`-plane in the multiplicity-free
permanent cubic space, then

\[
 m_b\le\dim\partial S\le a_2.
\tag{2.1}
\]

Each of the six Chow terms has quadratic derivative rank at most fifteen, so

\[
 d_2\le90.
\tag{2.2}
\]

Subtracting (2.1) from (2.2) proves the first key inequality.

### Proposition 2.1

\[
 \boxed{t_2\le90-m_b.}
\tag{2.3}
\]

This direction was absent from N6-037.  In particular, the high middle
intersection forces the fixed-six noncentral quadratic quotient to be
**small**, not large.

## 3. The direct residual rank has a strict ceiling

Let

\[
 A=C_{4,2}(P),\qquad B=C_{4,2}(R).
\]

Since `C_(4,2)(Q)=A-B`, elementary image containment gives

\[
 \operatorname{im}(A-B)
 \subseteq\operatorname{im}A+\operatorname{im}B
 =E_2+H_2.
\tag{3.1}
\]

In fact the two sums are equal:

\[
 E_2+\operatorname{im}(A-B)=E_2+H_2,
\tag{3.2}
\]

because `Bx=Ax-(A-B)x`.  Consequently

\[
 \dim(E_2+G_2)=225+t_2.
\tag{3.3}
\]

Combining (2.3) and (3.1) yields:

### Theorem 3.1 -- direct `C_(4,2)` route ceiling

For every surviving fixed-six state,

\[
 \boxed{
 \operatorname{rank}C_{4,2}(Q)
 \le225+t_2
 \le315-m_b.
 }
\tag{3.4}
\]

For `45<=b<=64`, the exact shadows satisfy `64<=m_b<=78`.  Hence

\[
 \boxed{
 \operatorname{rank}C_{4,2}(Q)\le251<300.
 }
\tag{3.5}
\]

The number 300 is the sum of the twenty individual quadratic-rank caps
`20*15`.  Thus the N6-037 proposal to exclude the endpoint by proving

\[
 \operatorname{rank}C_{4,2}(P-R)>300
\]

is impossible: under the same hypotheses the rank is already forced below
252.  This is a mathematical route obstruction, not merely a failed random
search.

## 4. A lower bound on `t_2` from the existing relation modules

The upper ceiling is the main conclusion.  For completeness, the exact
replay also combines all already proved scalar interfaces to bound `t_2`
from below.

For the six individual quadratic spaces put

\[
 \varepsilon_i=15-\dim\mathcal D_2(T_i).
\]

Let `D_b=78-m_b`.  The omitted-factor inequalities and the refined
projection cap give

\[
 \sum_i\varepsilon_i-\min_i\varepsilon_i\le D_b,
\tag{4.1}
\]

\[
 \kappa_2
 \le D_b-\sum_i\varepsilon_i+\min_i\varepsilon_i,
\tag{4.2}
\]

and

\[
 a_2\le
 78-\left(\sum_i\varepsilon_i-\min_i\varepsilon_i\right).
\tag{4.3}
\]

Here `kappa_2` is the ordinary relation dimension among the six quadratic
spaces.  If `rho_3` is the central relation dimension and `kappa_4` the
quartic relation dimension, vector Macaulay gives

\[
 \rho_3\le\kappa_2^{\langle2\rangle},
 \qquad
 \kappa_4\le\rho_3^{\langle3\rangle}.
\tag{4.4}
\]

The coupled central rank also gives

\[
 \rho_3\le120-h.
\tag{4.5}
\]

Finally the noncentral block-Sylvester inequality gives

\[
 d_2\ge
 90-\sum_i\varepsilon_i-\kappa_2-\kappa_4.
\tag{4.6}
\]

Equations (4.1)--(4.6), the exact N6-032 lower bound on `h`, and the already
proved impossibility of individual quadratic rank twelve form a finite
integer optimization.  No realizability is inferred from an optimizing
integer profile.

The resulting certified inclusive intervals and residual-rank windows are:

| `b` | `m_b` | `h` lower | `t_2` lower | `t_2` upper | `j_4` upper | current `rank C_(4,2)(Q)` window |
|---:|---:|---:|---:|---:|---:|---:|
| 45 | 64 | 90 | 1 | 26 | 15 | 211--251 |
| 46 | 65 | 90 | 1 | 25 | 15 | 211--250 |
| 47 | 66 | 89 | 1 | 24 | 16 | 210--249 |
| 48 | 66 | 88 | 1 | 24 | 16 | 210--249 |
| 49 | 67 | 88 | 1 | 23 | 16 | 210--248 |
| 50 | 68 | 87 | 1 | 22 | 17 | 209--247 |
| 51 | 69 | 86 | 1 | 21 | 17 | 209--246 |
| 52 | 69 | 88 | 1 | 21 | 17 | 209--246 |
| 53 | 70 | 92 | 1 | 20 | 18 | 208--245 |
| 54 | 71 | 96 | 1 | 19 | 18 | 208--244 |
| 55 | 72 | 98 | 1 | 18 | 18 | 208--243 |
| 56 | 72 | 98 | 1 | 18 | 19 | 207--243 |
| 57 | 73 | 100 | 1 | 17 | 19 | 207--242 |
| 58 | 74 | 110 | 2 | 16 | 19 | 208--241 |
| 59 | 75 | 112 | 4 | 15 | 20 | 209--240 |
| 60 | 75 | 112 | 4 | 15 | 20 | 209--240 |
| 61 | 76 | 116 | 8 | 14 | 21 | 212--239 |
| 62 | 77 | 118 | 10 | 13 | 21 | 214--238 |
| 63 | 77 | 118 | 10 | 13 | 21 | 214--238 |
| 64 | 78 | 120 | 12 | 12 | 22 | 215--237 |

The lower endpoint in the last column combines the already proved
`dim G_2>=203` with

\[
 \dim G_2\ge225+t_2-j_4.
\tag{4.7}
\]

The upper endpoint is the new common-sum-space ceiling (3.4).

## 5. Exact closure of the `b=64` endpoint

At `b=64`, `m_b=78` and `D_b=0`.  The omitted-factor inequalities force

\[
 \varepsilon_i=0,
 \qquad
 \dim(E_2\cap\mathcal D_2(T_i))=3
 \quad(1\le i\le6),
\tag{5.1}
\]

and the six individual quadratic spaces have no literal relation.  The
N6-032 high-layer table gives `h=120`.  Therefore all six central spaces
have rank twenty, their literal central relation space is zero, and its
quartic prolongation relation space is also zero.  Applying block-Sylvester
at degrees two and four gives

\[
 d_2=90.
\tag{5.2}
\]

On the other hand, (2.1) gives `a_2>=78`, while the six-term projection cap
gives `a_2<=78`.  Hence

\[
 \boxed{
 (b,h,d_2,a_2,t_2)=(64,120,90,78,12).
 }
\tag{5.3}
\]

The dual shadow theorem gives `j_4<=22`, so (3.4) and (4.7) close the
currently justified endpoint window to

\[
 \boxed{
 215\le\operatorname{rank}C_{4,2}(Q)\le237.
 }
\tag{5.4}
\]

This is an exact geometric consequence, not a finite-field or random
diagnostic.  It does not show that the endpoint is realizable.

## 6. What remains

The direct quadratic rank of `Q` cannot exceed the naive sum of twenty
single-term caps: its universal ceiling is already far below that cap.  A
lower-27 argument must therefore use more than this one rank-versus-naive-cap
comparison, for example:

1. the relative position of `E_2\cap G_2` inside the 225 permanent
   quadrics;
2. the bilinear relation-tableau correction between the degree-two and
   degree-four intersections; or
3. a labelled/Fitting invariant coupling the twenty individual quadratic
   images before summation.

Replacing these maps by only the criterion
`rank C_(4,2)(Q)>20*15` cannot close the proof.  A sharper scalar theorem that
uses additional termwise structure or classifies equality cases is not ruled
out here.

## 7. Replay

Run

```text
python scripts/n6_fixed_six_offcentral_c42_ceiling.py \
  --json data/n6_fixed_six_offcentral_c42_ceiling.json
python -m unittest tests/test_n6_fixed_six_offcentral_c42_ceiling.py
```

The script uses exact integers and `Fraction`.  It reconstructs every Bukh
separator, enumerates the small sorted defect profiles, checks all Macaulay
successors, and freezes the `b=64` endpoint.  No floating-point rank, random
sample, or finite-field inference appears.
