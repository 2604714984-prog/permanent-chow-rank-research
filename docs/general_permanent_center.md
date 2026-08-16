# Scalar centers of permanent polynomials and the `n=8` equality-span boundary

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_COMBINATORIAL_REPLAYED`,
`GENERAL_N_DIRECT_SUM_BARRIER`.

This note proves that every permanent polynomial of order at least three has
scalar Hessian center and is therefore indecomposable as a nontrivial
Sebastiani--Thom sum.  It then combines this center theorem with the exact
factor-span zero-block theorem of PR #45.

The combination closes the only central two-term factor-span boundary left at
`n=8`: every pair of degree-eight Chow terms has zero literal-sum
intersection with

\[
\mathcal D_4(\operatorname{perm}_8).
\]

Together with the exact product-shadow transition, this gives the stacked
ordinary bounds

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge44,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge79.
}
\]

The result does not determine either exact rank, control five-term flat-sum
directions, or prove a border-rank improvement.

## 1. The concise Hessian center

Let \(f\in\operatorname{Sym}^dW\) be concise, meaning that its order-\((d-1)\)
derivatives span \(W\).  Let \(H_f\) be its Hessian matrix, whose entries are
degree-\((d-2)\) forms.

Define the center

\[
Z_W(f)
=
\left\{
A\in\operatorname{End}(W):
H_fA\text{ is symmetric}
\right\}.
\tag{1.1}
\]

Equivalently,

\[
A^{\mathsf T}H_f=H_fA.
\tag{1.2}
\]

Scalars always belong to \(Z_W(f)\).

If

\[
W=A_0\oplus B_0,
\qquad
f=f_A+f_B,
\qquad
0\ne f_A\in\operatorname{Sym}^dA_0,
\quad
0\ne f_B\in\operatorname{Sym}^dB_0,
\tag{1.3}
\]

then the projection \(e:W\to A_0\) along \(B_0\) is a nontrivial idempotent in
the center.  Indeed, all mixed second derivatives vanish and the Hessian is
block diagonal.

Thus a scalar center excludes every nontrivial direct-sum decomposition.

## 2. Hessian entries of the permanent

Let

\[
P_m=\operatorname{perm}_m
\]

in the \(m^2\)-dimensional variable space

\[
W_m=\operatorname{span}\{x_{ij}:0\le i,j<m\}.
\]

For cells

\[
a=(i,j),\qquad b=(k,\ell),
\]

one has

\[
\partial_a\partial_bP_m=0
\]

when the cells share a row or a column.  Otherwise,

\[
\partial_a\partial_bP_m
=
P_{\widehat{\{i,k\}},\,\widehat{\{j,\ell\}}},
\tag{2.1}
\]

the \((m-2)\times(m-2)\) subpermanent on the remaining rows and columns.

For \(m\ge3\), these nonzero Hessian entries are linearly independent when
indexed by their omitted unordered row pair and omitted unordered column pair:
their row-set and column-set monomial supports are distinct.

The permanent is concise because its order-\((m-1)\) derivatives include all
\(m^2\) variables.

## 3. The permanent center is scalar

Let \(A=(a_{zy})\in Z_{W_m}(P_m)\).  The condition that \(H_{P_m}A\) is
symmetric is

\[
\sum_z H_{xz}a_{zy}
=
\sum_z H_{yz}a_{zx}
\qquad
\text{for all cells }x,y.
\tag{3.1}
\]

### Lemma 3.1 -- every off-diagonal center entry vanishes

For every ordered pair of distinct cells \(z\ne y\), there is a cell \(x\)
such that

1. \(x\) is in a different row and column from \(z\), so \(H_{xz}\ne0\);
2. the omitted-row/omitted-column label of \(H_{xz}\) does not occur among
   the nonzero entries \(H_{yw}\).

### Proof

There are three cases.

- If \(z\) and \(y\) share a row, choose the column of \(x\) outside the two
  columns and choose any row different from their common row.
- If they share a column, use the symmetric row choice.
- If they share neither, choose the row of \(x\) outside their two rows and
  the column outside their two columns.

All choices exist because \(m\ge3\).  In each case \(x\) is compatible with
\(z\), while at least one of the row or column labels required by \(y\) is
absent from the label of \(H_{xz}\). ∎

Taking the coefficient of this unmatched Hessian basis vector in (3.1) gives

\[
a_{zy}=0.
\]

Hence every center element is diagonal.

For a diagonal center element with entries \(\lambda_x\), equation (3.1)
along any compatible pair \(x,y\) gives

\[
H_{xy}\lambda_y=H_{xy}\lambda_x,
\]

so

\[
\lambda_x=\lambda_y.
\]

The graph on matrix cells joining cells in different rows and columns is
connected for \(m\ge3\).  Therefore all diagonal entries are equal.

### Theorem 3.2 -- scalar permanent center

For every \(m\ge3\),

\[
\boxed{
Z_{W_m}(\operatorname{perm}_m)=\mathbf k\operatorname{id}.
}
\tag{3.2}
\]

### Corollary 3.3 -- permanent indecomposability

For \(m\ge3\), \(\operatorname{perm}_m\) admits no nontrivial
Sebastiani--Thom decomposition on its essential variable space.

## 4. Minimal-shadow permanent derivatives are indecomposable

Let

\[
E_m=\mathcal D_m(\operatorname{perm}_n)
\]

and let \(0\ne f\in E_m\).  The permanent derivative-shadow theorem gives

\[
\dim\partial^{m-1}f\ge m^2.
\tag{4.1}
\]

Assume equality and put

\[
W_f=\partial^{m-1}f,
\qquad
\dim W_f=m^2.
\]

Then \(f\in\operatorname{Sym}^mW_f\) is concise.

The row-column diagonal torus has pairwise distinct weights on the
subpermanent basis of \(E_m\).  Choose an integral one-parameter subgroup with
a unique lowest weight among the nonzero subpermanent coefficients of \(f\).
After rescaling,

\[
f_t\longrightarrow cP_{I,J},
\tag{4.2}
\]

where \(P_{I,J}\) is one \(m\times m\) subpermanent.

The spaces

\[
W_t=\partial^{m-1}f_t
\]

have dimension \(m^2\) for \(t\ne0\).  Their Grassmann limit contains the
essential variable space of \(P_{I,J}\), which already has dimension \(m^2\);
therefore the limiting space is exactly that coordinate \(m^2\)-plane.

On the tautological rank-\(m^2\) bundle over the resulting curve in the
Grassmannian, the center is the kernel of a bundle map whose coefficients are
polynomial in the form.  Kernel dimension is upper semicontinuous.  The
special fiber has center dimension one by Theorem 3.2, so the generic center
also has dimension at most one.  Scalars give the reverse inequality.

### Theorem 4.1 -- minimal-shadow indecomposability

If

\[
0\ne f\in\mathcal D_m(\operatorname{perm}_n),
\qquad
m\ge3,
\qquad
\dim\partial^{m-1}f=m^2,
\]

then

\[
\boxed{
Z_{W_f}(f)=\mathbf k\operatorname{id},
}
\tag{4.3}
\]

and \(f\) has no nontrivial direct-sum decomposition on \(W_f\).

The constancy of the essential-space dimension is indispensable here.  The
theorem is not a statement about centers computed in the full ambient
\(n^2\)-variable space, where unused variables would create irrelevant
endomorphisms.

## 5. Closing the `n=8,m=4` transverse equality span

Let

\[
E=\mathcal D_4(\operatorname{perm}_8)
\]

and let \(T,U\) be arbitrary degree-eight Chow terms with factor spans
\(L_T,L_U\).  Put

\[
F=\mathcal D_4(T),
\qquad
G=\mathcal D_4(U).
\]

Each factor span has dimension at most eight, so

\[
\dim(L_T+L_U)\le16.
\]

### Case 1: strict span

If

\[
\dim(L_T+L_U)<16=4^2,
\]

PR #45 gives

\[
E\cap(F+G)=0.
\]

### Case 2: equality span

Suppose

\[
\dim(L_T+L_U)=16.
\]

Then both factor spans have dimension eight and

\[
L_T\cap L_U=0.
\]

Assume that \(0\ne f\in E\cap(F+G)\).  Write

\[
f=g+h,
\qquad
g\in F\subseteq\operatorname{Sym}^4L_T,
\qquad
h\in G\subseteq\operatorname{Sym}^4L_U.
\tag{5.1}
\]

The permanent shadow floor gives

\[
\dim\partial^3f\ge16,
\]

while (5.1) gives

\[
\partial^3f\subseteq L_T\oplus L_U,
\]

so equality holds.

Neither \(g\) nor \(h\) can vanish: if, for example, \(h=0\), then the
essential variable space of \(f\) would have dimension at most eight,
contradicting the lower bound sixteen.

Thus (5.1) is a nontrivial direct-sum decomposition of a minimal-shadow
permanent derivative, contradicting Theorem 4.1.

### Theorem 5.1 -- universal two-term zero block for `perm_8`

For every pair of degree-eight Chow terms,

\[
\boxed{
\mathcal D_4(\operatorname{perm}_8)
\cap
\left(
\mathcal D_4(T)+\mathcal D_4(U)
\right)
=0.
}
\tag{5.2}
\]

Consequently the quotient map modulo
\(\mathcal D_4(\operatorname{perm}_8)\) is injective on the two-term literal
sum.  The quotient intersection is exactly the image of the literal
intersection, and every matched-difference image vanishes.

This includes degenerate Chow terms.  The equality-span case automatically
forces both factor spans to be independent.

## 6. New ordinary lower bounds

### 6.1 `perm_7`

PR #45 already implies that every pair of degree-seven Chow terms is a zero
block in \(\mathcal D_4(\operatorname{perm}_7)\), because their joint factor
span has dimension at most \(14<16\).

Fix fifteen terms.  Project two away, leaving the degree-three shadow capacity

\[
13\binom73=455.
\]

Using

\[
F_{7,4}(238)=452,\qquad F_{7,4}(239)=456
\]

gives intersection cap \(238\), residual count 29, and

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge44.
}
\tag{6.1}
\]

### 6.2 `perm_8`

Fix sixteen terms.  Theorem 5.1 projects an arbitrary two-term block away.
The remaining fourteen terms have degree-three derivative capacity

\[
14\binom83=14\cdot56=784.
\]

The exact product-shadow transition is

\[
F_{8,4}(560)=784,\qquad F_{8,4}(561)=793.
\]

Hence the complementary intersection has dimension at most \(560\).  With

\[
A_{8,4}=310\,464,
\qquad
B_{8,4}=4\,424,
\]

the residual requires

\[
\left\lceil
\frac{310\,464-64\cdot560}{4\,424}
\right\rceil
=63
\]

terms.  Adding the sixteen fixed terms proves

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)\ge79.
}
\tag{6.2}
\]

The current stacked intervals become

\[
44\le\operatorname{ChowRank}(\operatorname{perm}_7)\le64,
\]

\[
79\le\operatorname{ChowRank}(\operatorname{perm}_8)\le128.
\]

## 7. What remains

The pairwise central matched-difference problem is now closed for `n=8`.
The next lower-80 target is not pairwise: PR #42 identifies a five-term cubic
block cap of 146, while PR #43 shows a coordinate cap of 40 and a possible
107-dimensional nonliteral flat-sum defect.

Therefore the next valid interface is the valuation-leading relation packet
of a moving five-term sum.  More pairwise frame enumeration will not by
itself reach lower 80.

This note does not:

- control arbitrary five-term flat sums;
- classify centers of every non-minimal-shadow element of a permanent
  derivative space;
- improve `perm_6`;
- prove an exact rank for `perm_7` or `perm_8`;
- make a border-rank or literature-novelty claim.

## 8. Deterministic replay

Run

```bash
python scripts/general_permanent_center.py \
  --json /tmp/general_permanent_center.json
python scripts/general_permanent_center_independent.py
python -m unittest tests.test_general_permanent_center -v
```

The primary audit supplies an explicit unmatched Hessian-label witness for
every ordered off-diagonal center coefficient for \(3\le m\le10\) and checks
connectivity of the diagonal compatibility graph.

The independent implementation imports none of the primary code.  It builds
the complete integer center equations for \(m=3,4\), verifies that the scalar
identity is in the kernel, and obtains modular rank \(m^4-1\).  The modular
rank is used only as a characteristic-zero lower bound; the explicit scalar
kernel gives the matching upper bound.
