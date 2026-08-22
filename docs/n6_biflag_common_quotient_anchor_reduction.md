# The common-quotient biflag anchor reduction

**Status.** PURE_BIFLAG_COMMON_QUOTIENT_ANCHOR_REDUCTION,
EXACT_COORDINATE_MATCHING_REPLAY (N6-104). The base field is algebraically
closed of characteristic zero.

N6-103 reduces the biflag survivor to at least nineteen actual
\((\varepsilon,\alpha)=(0,3)\) Chow frames with one common quotient
\(W_{15}\), all row and column blocks singular. Fix the critical six. Their
factor spans sum to

\[
 M=R_4\otimes C_5+R_5\otimes C_3,\qquad
 R_4\subset R_5,\quad C_3\subset C_5.
\tag{0.1}
\]

This note proves that the survivor must contain both a common-rank row
anchor and a common-rank column anchor. Only four rank combinations remain.

## 1. Coordinate contraction types

For a coordinate row covector \(e_r^*\), contraction of (0.1) is

\[
 \pi_r(M)=
 \begin{cases}
 C_5,&e_r^*|_{R_4}\ne0,\\
 C_3,&e_r^*|_{R_4}=0,\ e_r^*|_{R_5}\ne0,\\
 0,&e_r^*|_{R_5}=0.
 \end{cases}
\tag{1.1}
\]

The coordinate restrictions span \(R_4^*\), so at least four rows have the
first type. Since

\[
 \dim\operatorname{Ann}(R_4)=2,\qquad
 \dim\operatorname{Ann}(R_5)=1,
\]

at most two coordinate rows have the second type and at most one has the
zero type. The possible counts
\((\#C_5,\#C_3,\#0)\) are exactly

\[
 (6,0,0),(5,1,0),(5,0,1),(4,2,0),(4,1,1).
\tag{1.2}
\]

Dually, a coordinate column contraction is \(R_5\), \(R_4\), or zero
according as the coordinate covector is nonzero on \(C_3\), kills \(C_3\)
but not \(C_5\), or kills \(C_5\). The possible counts are

\[
\begin{split}
 &(6,0,0),(5,1,0),(5,0,1),(4,2,0),\\
 &(4,1,1),(3,3,0),(3,2,1).
\end{split}
\tag{1.3}
\]

The entries mean \((\#R_5,\#R_4,\#0)\).

## 2. The common-image dichotomy

Let \(A_{i,r}:k^6\to C\) be the row block of color \(i\), and put

\[
 H_{i,r}=\{A_{i,r}ZA_{i,r}^{\mathsf T}:Z\in S_0(k^6)\}.
\]

The common quotient gives one map \(\theta_r:W\to\operatorname{Sym}^2C\)
whose image is \(H_{i,r}\) for every color. The first-shadow lemma from
N6-072 says

\[
 \operatorname{rank}A_{i,r}\ge2
 \quad\Longrightarrow\quad
 \partial H_{i,r}=\operatorname{im}A_{i,r}.
\tag{2.1}
\]

Hence, at a nonzero contraction \(N=\pi_r(M)\) of dimension \(d\ge2\),
there are only two possibilities.

1. Some block has rank at least two. Then every color has rank \(d\), and
   all six block images equal \(N\).
2. Every block has rank at most one. Their common quadratic image must be
   zero; otherwise all nonzero block images would be the same line and
   could not span \(N\). Thus each nonzero block has a coordinate domain
   covector, and the six image lines span \(N\).

The same argument applies to columns. In the first alternative the possible
row ranks are \(3,5\), and the possible column ranks are \(4,5\).

Literal directness of the six quadratic spaces is not used here.

## 3. Excluding the all-rank-one alternative

Suppose every nonzero row and column contraction uses the second alternative.
For one injective factor matrix \(X_i:k^6\to R\otimes C\), every row block
then has rank at most one and a coordinate domain covector.

The six row-block row spaces must span the six-dimensional factor domain.
There are only six ambient rows, so no row block is zero and their six
domain labels form a permutation. The identical column argument says that
the six column labels form a permutation.

At an ambient cell \((r,c)\), the corresponding coefficient functional lies
simultaneously on the row label and the column label. It can be nonzero only
when those labels agree. It follows that \(X_i\) is supported on a
permutation matching: exactly one nonzero cell in each row and each column,
with one cell for every factor.

There are \(6!=720\) such supports. The exact replay evaluates the
fifteen-axis permanent quotient signature of each and finds 720 distinct
signatures. This is the matching subcase of the pure coordinate quotient
injectivity theorem N6-043. Hence two distinct matching frames cannot have
one common \(W_{15}\). If their supports agree, their factor spans agree,
which is incompatible with the 23-dimensional sum (0.1).

Thus the all-rank-one branch is impossible.

## 4. The four surviving anchor combinations

At least one row contraction must therefore use the first alternative, and
at least one column contraction must use it. The remaining rank frontier is

\[
 (\operatorname{rank}A_{\rm row},
   \operatorname{rank}A_{\rm column})
 \in\{(3,4),(3,5),(5,4),(5,5)\}.
\tag{4.1}
\]

This is a substantial reduction from arbitrary singular \(6\times6\)
blocks. The rank-five cases meet the G-050 Cremona barrier; the rank-three
and rank-four cases require a new cross-anchor compatibility argument.

## 5. Exact boundary

Proved: every N6-103 biflag survivor contains a common-image row anchor of
rank three or five and a common-image column anchor of rank four or five.
The branch in which every coordinate contraction has rank at most one is
impossible.

Not proved: exclusion of any of the four combinations (4.1), exclusion of
the biflag branch, ordinary lower 29, exact rank 32, or a border-rank bound.

Replay:

    python scripts/n6_biflag_common_quotient_anchor_reduction.py \
      --verify-json data/n6_biflag_common_quotient_anchor_reduction.json
    python -m unittest \
      tests.test_n6_biflag_common_quotient_anchor_reduction -v
