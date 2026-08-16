# Dual-frame control of same-span Chow derivative overlaps

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_RATIONAL_REPLAYED`,
`PAIRWISE_LITERAL_OVERLAP_THEOREM`.

Let

\[
T=x_1\cdots x_n,\qquad U=y_1\cdots y_n
\]

be two Chow terms whose factors are linearly independent and span the same
\(n\)-dimensional space \(L\).  Write

\[
\mathcal S_m(x)=\mathcal D_m(T),\qquad
\mathcal S_m(y)=\mathcal D_m(U).
\]

This note proves a sharp quadratic bound in terms of the **dual** factor
frames and derives a Kruskal--Katona bound in every higher output degree.

It does not control two terms with unequal or degenerate factor spans, the
matched-difference map into a permanent derivative space, or a coupled
catalectic image.  It gives no new unrestricted Chow-rank lower bound.

## 1. Why the dual frame is the correct object

Let

\[
\xi_1,\ldots,\xi_n,\qquad
\eta_1,\ldots,\eta_n
\]

be the bases of \(L^*\) dual to the factor bases \(x\) and \(y\).  Define

\[
s^\vee
=
\#\bigl(
\{\mathbf k\xi_i\}_i\cap\{\mathbf k\eta_j\}_j
\bigr).
\tag{1.1}
\]

Thus \(s^\vee\) counts common projective directions of the two **dual**
bases.  It need not equal the number of common factors of \(T\) and \(U\).

The squarefree quadratic spaces satisfy

\[
\mathcal S_2(x)^\perp
=
\operatorname{span}\{\xi_1^2,\ldots,\xi_n^2\},
\tag{1.2}
\]

and similarly for \(y\).  Therefore the literal quadratic overlap is governed
by the intersection of two diagonal-square spaces in the dual, not merely by
the number of common primal factors.

## 2. Exact quadratic identity

Write

\[
\eta_j=\sum_i a_{ij}\xi_i
\]

and let \(A=(a_{ij})\in\operatorname{GL}_n(\mathbf k)\).  Put

\[
K(A)
=
\left\{
d\in\mathbf k^n:
A\operatorname{diag}(d)A^{\mathsf T}
\text{ is diagonal}
\right\},
\qquad
\kappa(A)=\dim K(A).
\tag{2.1}
\]

### Proposition 2.1

\[
\boxed{
\dim\bigl(\mathcal S_2(x)\cap\mathcal S_2(y)\bigr)
=
\binom n2-n+\kappa(A).
}
\tag{2.2}
\]

### Proof

Under the perfect apolar pairing in degree two,

\[
\mathcal S_2(x)^\perp
=
Q_\xi
:=
\operatorname{span}\{\xi_i^2\},
\]

and

\[
\mathcal S_2(y)^\perp
=
Q_\eta
:=
\operatorname{span}\{\eta_j^2\}.
\]

Both spaces have dimension \(n\).  An element
\(\sum_jd_j\eta_j^2\) belongs to \(Q_\xi\) exactly when the matrix

\[
A\operatorname{diag}(d)A^{\mathsf T}
\]

has zero off-diagonal part.  Hence

\[
\dim(Q_\xi\cap Q_\eta)=\kappa(A).
\]

Since \(\dim\operatorname{Sym}^2L=\binom{n+1}{2}\),

\[
\begin{aligned}
\dim(\mathcal S_2(x)\cap\mathcal S_2(y))
&=
\binom{n+1}{2}
-
\dim(Q_\xi+Q_\eta)\\
&=
\binom{n+1}{2}
-
(2n-\kappa(A))\\
&=
\binom n2-n+\kappa(A).
\end{aligned}
\]

∎

## 3. The active support and its component algebra

Choose a generic \(d^0\in K(A)\) whose support is the union of the supports of
all vectors in \(K(A)\).  Let that support be \(S\), with \(|S|=p\), and put

\[
D_0=\operatorname{diag}(d^0).
\]

The diagonal matrix

\[
M_0=AD_0A^{\mathsf T}
\]

has rank \(p\).  Let \(R\) be the support of its diagonal, so \(|R|=p\).

### Lemma 3.1

After permuting rows and columns,

\[
A=
\begin{pmatrix}
B&C\\
0&E
\end{pmatrix},
\tag{3.1}
\]

where \(B=A_{R,S}\) is an invertible \(p\times p\) matrix, and every vector in
\(K(A)\) is supported on \(S\).

### Proof

The columns \(A_S\) are independent.  If \(i\notin R\), then the entire
\(i\)-th row of \(M_0\) is zero:

\[
(A_{i,S}D_0)A_S^{\mathsf T}=0.
\]

The map \(v\mapsto vA_S^{\mathsf T}\) is injective and \(D_0|_S\) is
invertible, so \(A_{i,S}=0\).  Thus \(A_{R^c,S}=0\), while
\(A_{R,S}\) has rank \(p\), proving (3.1). ∎

On the active block,

\[
B D_0 B^{\mathsf T}
\]

is invertible diagonal.  For \(D=\operatorname{diag}(d)\), multiplication by
the inverse of this matrix gives

\[
BDB^{\mathsf T}
(BD_0B^{\mathsf T})^{-1}
=
B D D_0^{-1}B^{-1}.
\tag{3.2}
\]

Consequently normalization by \(d^0\) identifies \(K(A)\) with

\[
\mathcal A_B
=
\left\{
c\in\mathbf k^p:
B\operatorname{diag}(c)B^{-1}
\text{ is diagonal}
\right\}.
\tag{3.3}
\]

Let \(\Gamma(B)\) be the bipartite support graph of \(B\), with row vertices
and column vertices and an edge at every nonzero entry.

### Lemma 3.2

\[
\boxed{\dim\mathcal A_B=\#\pi_0(\Gamma(B)).}
\tag{3.4}
\]

### Proof

The condition in (3.3) is equivalent to the existence of a diagonal vector
\(e\) such that

\[
B\operatorname{diag}(c)=\operatorname{diag}(e)B.
\]

Entrywise,

\[
B_{ij}(c_j-e_i)=0.
\]

Thus \(c_j=e_i\) along every support edge, and the parameters are constant on
the connected components of \(\Gamma(B)\).  Conversely every such component
constant gives a solution.

Because \(B\) is invertible, each component contains the same number of row
and column vertices: after permuting by components, every diagonal block is
square and invertible. ∎

## 4. Sharp dual-frame bound

A singleton component of \(\Gamma(B)\) gives a column of the full matrix \(A\)
with exactly one nonzero entry, because \(A_{R^c,S}=0\).  It therefore gives a
common projective dual direction.  Let \(t\) be the number of singleton
components.  Then

\[
t\le s^\vee.
\tag{4.1}
\]

Every other component contains at least two columns.  Therefore

\[
\begin{aligned}
\kappa(A)
&\le
t+\left\lfloor\frac{p-t}{2}\right\rfloor\\
&=
\left\lfloor\frac{p+t}{2}\right\rfloor\\
&\le
\left\lfloor\frac{n+s^\vee}{2}\right\rfloor\\
&=
s^\vee+\left\lfloor\frac{n-s^\vee}{2}\right\rfloor.
\end{aligned}
\tag{4.2}
\]

Combining (2.2) and (4.2) proves:

### Theorem 4.1 -- sharp same-span quadratic overlap

\[
\boxed{
\dim\bigl(
\mathcal D_2(T)\cap\mathcal D_2(U)
\bigr)
\le
\binom n2
-
\left\lceil\frac{n-s^\vee}{2}\right\rceil.
}
\tag{4.3}
\]

The bound is sharp for every admissible pair \((n,s^\vee)\).

### Sharp constructions

Use the rational blocks

\[
H_2=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
B_3=
\begin{pmatrix}
1&1&1\\
1&-1&0\\
1&1&-2
\end{pmatrix}.
\tag{4.4}
\]

They satisfy

\[
H_2H_2^{\mathsf T}=2I_2,
\qquad
B_3B_3^{\mathsf T}=\operatorname{diag}(3,2,6),
\]

have connected support graphs, and contain no one-sparse columns.

For \(n-s^\vee\) even, take \(s^\vee\) one-by-one identity blocks and
\((n-s^\vee)/2\) copies of \(H_2\).  For an odd remainder at least three, use
one \(B_3\) and the necessary \(H_2\) blocks.  If the remainder is one, use

\[
A=I_n+E_{1n};
\]

then the first \(n-1\) columns are the common dual directions and
\(\dim K(A)=n-1\).  These constructions attain equality in (4.2) and (4.3).

## 5. Higher output degrees

For \(2\le m\le n\), let

\[
H_m=\mathcal S_m(x)\cap\mathcal S_m(y),
\qquad b=\dim H_m.
\]

Every \((m-2)\)-fold derivative of \(H_m\) belongs to the quadratic overlap:

\[
\partial^{m-2}H_m
\subseteq
\mathcal S_2(x)\cap\mathcal S_2(y).
\tag{5.1}
\]

Let \(\kappa_{n,m\to2}(b)\) be the degree-two lower shadow of the first \(b\)
\(m\)-subsets in colex order.  Torus specialization of a \(b\)-plane in
\(\mathcal S_m(x)\), followed by Kruskal--Katona, gives

\[
\dim\partial^{m-2}H_m
\ge
\kappa_{n,m\to2}(b).
\tag{5.2}
\]

Define

\[
B_{n,m}(s^\vee)
=
\max\left\{
b:
\kappa_{n,m\to2}(b)
\le
\binom n2-
\left\lceil\frac{n-s^\vee}{2}\right\rceil
\right\}.
\tag{5.3}
\]

### Corollary 5.1

\[
\boxed{
\dim\bigl(
\mathcal D_m(T)\cap\mathcal D_m(U)
\bigr)
\le
B_{n,m}(s^\vee).
}
\tag{5.4}
\]

For \(s^\vee=0\), the central examples are:

| \(n\) | \(m=\lfloor n/2\rfloor\) | quadratic cap | higher-degree overlap cap |
|---:|---:|---:|---:|
| 6 | 3 | 12 | 11 |
| 7 | 3 | 17 | 21 |
| 8 | 4 | 24 | 36 |
| 9 | 4 | 31 | 71 |
| 10 | 5 | 40 | 127 |
| 11 | 5 | 49 | 253 |
| 12 | 6 | 60 | 463 |

These are universal same-factor-span bounds.  They need not be sharp in
degrees above two.

## 6. Primal common factors cannot replace dual directions

Consider the dual transition matrix

\[
A=
\begin{pmatrix}
0&1&0&-1\\
0&0&0&1\\
0&0&-1&-1\\
1&0&0&1
\end{pmatrix}.
\tag{6.1}
\]

It has three one-sparse columns, so \(s^\vee=3\).  Its inverse transpose is

\[
A^{-\mathsf T}
=
\begin{pmatrix}
0&1&0&0\\
-1&1&-1&1\\
0&0&-1&0\\
1&0&0&0
\end{pmatrix},
\tag{6.2}
\]

which has only one one-sparse column.  Thus the two primal factor bases have
one common projective factor, while the dual bases have three.

The exact common quadratic dimension is five:

\[
\dim\bigl(
\mathcal S_2(x)\cap\mathcal S_2(y)
\bigr)=5.
\]

A bound obtained by substituting the primal shared-factor count into (4.3)
would incorrectly give four.  The dual-frame distinction is therefore
mathematically necessary.

## 7. Relation to the active general-\(n\) route

The previous pairwise-overlap note established:

- a transverse common-factor formula; and
- a zero-common-factor block-rotation family with large literal overlap.

The present theorem identifies the exact quadratic mechanism behind the
same-span part: intersection of the two dual diagonal-square spaces.  It gives
a sharp frame-sensitive bound and a higher-degree shadow consequence.

It still does not control the other term in the correct exact sequence

\[
0\longrightarrow \rho(F\cap G)
\longrightarrow \rho(F)\cap\rho(G)
\longrightarrow \operatorname{im}\Delta
\longrightarrow0.
\tag{7.1}
\]

A numerical Chow-rank improvement now requires a permanent-relative theorem
that couples:

1. the dual-frame literal-overlap invariant in this note; and
2. the matched-difference image inside the permanent derivative space.

## 8. Deterministic reproduction

Run

```bash
python scripts/general_same_span_chow_overlap.py \
  --json /tmp/general_same_span_chow_overlap.json
python -O scripts/general_same_span_chow_overlap.py
python scripts/general_same_span_chow_overlap_independent.py
python -m unittest tests.test_general_same_span_chow_overlap -v
```

Expected terminal markers:

```text
GENERAL_SAME_SPAN_CHOW_OVERLAP_AUDIT_PASS
GENERAL_SAME_SPAN_CHOW_OVERLAP_INDEPENDENT_PASS
```

The primary implementation uses exact `Fraction` elimination.  The independent
implementation imports none of its functions and computes the sum of the two
dual diagonal-square spaces directly in a symmetric-matrix basis.
