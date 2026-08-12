# A block-shadow exclusion for separated alpha-three terms

**Status.** `PURE_SEPARATED_BLOCK_COUPLING_THEOREM`,
`EXACT_INTEGER_SHADOW_REPLAY`,
`B50_COLUMN_ROW_SEPARATED_EXCLUDED` (N6-059).  The base field is
algebraically closed of characteristic zero.  The pure theorem excludes the
remaining `b=50` all-alpha-three state whenever all six terms are separated
by the same columns, or after transposition by the same rows.  It does not
exclude an arbitrary common-quotient configuration.

## 1. The separated target

Write the permanent variables as \(x_{r,c}\), with
\(0\leq r,c<6\).  Suppose six Chow terms have the form

\[
 T_i=\prod_{c=0}^5\ell_{i,c},
 \qquad
 \ell_{i,c}\in\langle x_{0,c},\ldots,x_{5,c}\rangle.
\tag{1.1}
\]

Thus every term has exactly one factor in each fixed column.  Put

\[
 F_i=\mathcal D_2(T_i),\qquad
 C_i=\mathcal D_3(T_i),
\]

\[
 H_2=\sum_{i=1}^6F_i,\qquad H_3=\sum_{i=1}^6C_i.
\tag{1.2}
\]

Assume the exact quadratic and cubic data of the N6-058 `b=50` endpoint:

\[
 F_1\oplus\cdots\oplus F_6,\qquad \dim H_2=90,
\tag{1.3}
\]

\[
 q(F_i)=W,\qquad \dim W=15,\qquad
 C_1\oplus\cdots\oplus C_6,\qquad \dim H_3=120,
\tag{1.4}
\]

where \(q:\operatorname{Sym}^2V\to
\operatorname{Sym}^2V/E_2\), and
\(E_m=\mathcal D_m(\operatorname{perm}_6)\).

The claimed endpoint would additionally require

\[
 b=\dim(E_3\cap H_3)=50.
\tag{1.5}
\]

We prove instead that (1.1)--(1.4) force \(b\leq40\).

## 2. Every quadratic pair block has permanent intersection five

For a column pair \(J=\{c,d\}\), put

\[
 H_{2,J}=
 \operatorname{span}\{\ell_{i,c}\ell_{i,d}:1\leq i\leq6\}.
\tag{2.1}
\]

Products belonging to different column pairs have disjoint multidegrees.
Hence

\[
 H_2=\bigoplus_{J\in\binom{[6]}2}H_{2,J}.
\tag{2.2}
\]

Each block has dimension at most six.  Since (1.3) has total dimension
\(90=15\cdot6\), every block has dimension exactly six.

The quadratic permanent space has the matching decomposition

\[
 E_2=\bigoplus_JE_{2,J},
\tag{2.3}
\]

where \(E_{2,J}\) is spanned by the two-by-two subpermanents on the two
columns in \(J\).  The class \(q(\ell_{i,c}\ell_{i,d})\) lies in the
corresponding \(J\)-graded quotient block.  Since \(F_i\cap E_2=0\), it is
nonzero for every \(i,J\).  Since all \(q(F_i)\) equal the same
fifteen-plane \(W\), the six quotient vectors in a fixed block lie on the
same nonzero line.  Therefore

\[
 \boxed{
 \dim(E_{2,J}\cap H_{2,J})=6-1=5
 }
 \qquad(J\in\tbinom{[6]}2).
\tag{2.4}
\]

This uses both directness and the common quotient.  Equality of quotient
planes alone would not give (2.4).

## 3. The one-factor squarefree shadow lemma

Let \(A\) be a six-dimensional row space with basis
\(e_0,\ldots,e_5\).  Write

\[
 X_3=\langle e_re_se_t:r<s<t\rangle,\qquad
 X_2=\langle e_re_s:r<s\rangle.
\]

For \(S\subset X_3\), let \(\partial S\subset X_2\) be the span of all
first derivatives.

### Lemma 3.1

If \(\dim S=s\), then for \(0\leq s\leq6\),

\[
 \dim\partial S\geq k(s),
 \qquad
 (k(0),\ldots,k(6))=(0,3,5,6,6,8,9).
\tag{3.1}
\]

In particular,

\[
 \dim\partial S\leq5\quad\Longrightarrow\quad\dim S\leq2.
\tag{3.2}
\]

### Proof

The diagonal torus of \(A\) has twenty distinct weights on the squarefree
cubic basis.  The closure of the torus orbit of \([S]\) in
\(\operatorname{Gr}(s,X_3)\) contains a coordinate \(s\)-plane \(S_0\).
The derivative space is the image of the tautological bundle map

\[
 \mathcal S\otimes A^*\longrightarrow X_2.
\]

Matrix rank cannot increase under specialization, so

\[
 \dim\partial S\geq\dim\partial S_0.
\tag{3.3}
\]

For a coordinate family \(\mathcal A\subset\binom{[6]}3\), the derivative
dimension is exactly the number of pairs contained in at least one member of
\(\mathcal A\).  The colex initial segments give the values in (3.1), and
the one-dimensional Kruskal--Katona theorem says that no family of the same
size has a smaller lower shadow.

Only the threshold used later needs no general theorem: one triple has three
pairs; two distinct triples have at least five pairs; and a third distinct
triple adds at least one new pair, so three triples have at least six.  The
small exact replay independently enumerates the values through \(s=6\).
This proves the lemma. \(\square\)

## 4. Cubic triple blocks have intersection at most two

For a column triple \(C=\{c,d,e\}\), put

\[
 H_{3,C}=\operatorname{span}\{\ell_{i,c}\ell_{i,d}\ell_{i,e}:1\leq i\leq6\}.
\tag{4.1}
\]

Again, different column triples have disjoint multidegrees, so

\[
 H_3=\bigoplus_{C\in\binom{[6]}3}H_{3,C}.
\tag{4.2}
\]

The total rank \(120=20\cdot6\) in (1.4) forces every \(H_{3,C}\) to have
dimension six.  The permanent cubic space has the matching decomposition

\[
 E_3=\bigoplus_CE_{3,C},
\tag{4.3}
\]

where \(E_{3,C}\) is naturally the squarefree row cubic space \(X_3\): its
basis is indexed by row triples.

Let

\[
 S_C=E_{3,C}\cap H_{3,C},\qquad s_C=\dim S_C.
\tag{4.4}
\]

Fix a pair \(J\subset C\), and differentiate elements of \(S_C\) only by
the six variables in the unique column \(C\setminus J\).  Under the
identification with \(X_3\), these are precisely the row derivatives in
Lemma 3.1.  Every output belongs simultaneously to \(E_{2,J}\) and
\(H_{2,J}\).  Consequently

\[
 \partial S_C\subseteq E_{2,J}\cap H_{2,J}.
\tag{4.5}
\]

Equation (2.4) and Lemma 3.1 give

\[
 k(s_C)\leq5,\qquad\boxed{s_C\leq2}.
\tag{4.6}
\]

There are twenty column triples.  Equations (4.2)--(4.4) therefore yield

\[
 \boxed{
 b=\dim(E_3\cap H_3)=\sum_Cs_C\leq20\cdot2=40.
 }
\tag{4.7}
\]

This contradicts the target \(b=50\).  Transposing the matrix proves the
same theorem for terms having one factor in each fixed row.

## 5. Boundary and replay

Proved: every column-separated or row-separated six-term all-alpha-three
common-quotient configuration with \(d_2=90\) and \(h=120\) satisfies
\(b\leq40\), hence cannot realize the N6-058 `b=50` endpoint.

Not proved: an arbitrary term need not have one factor in each common row or
column block.  Thus the theorem does not exclude the general `b=50` state,
prove `ChowRank(perm_6)>=28`, determine the exact ordinary rank, or make a
border-rank claim.

```text
python scripts/n6_alpha3_separated_block_exclusion.py --json data/n6_alpha3_separated_block_exclusion.json
python -m unittest tests.test_n6_alpha3_separated_block_exclusion -v
```
