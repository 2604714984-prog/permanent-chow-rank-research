# Factor-span zero blocks and exact permanent quotients

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_REPLAYED`,
`GENERAL_N_MATCHED_DIFFERENCE_THEOREM`.

This note combines the permanent derivative-shadow theorem already proved in
`docs/general_n_koszul_bounds.md` with the actual factor-span dimension of a
block of Chow terms.  It proves that every block whose total factor span has
dimension strictly less than \(m^2\) is invisible to the output-degree-\(m\)
permanent derivative space.  For two terms, the same condition makes the
permanent quotient exact: the quotient intersection is only the image of the
literal intersection and the matched-difference image vanishes.

The theorem is valid for degenerate Chow terms in its zero-block and quotient
forms.  The sharper binomial literal-overlap corollary assumes independent
factor frames.

The strict inequality is essential.  Nothing here controls the boundary
\(\dim L=m^2\), high-span blocks, a coupled image beyond the stated inclusion,
or the exact Chow rank of a new permanent.  No unconditional numerical
Chow-rank lower bound is promoted in this note.

## 1. Existing permanent-side input

Let

\[
E_m=\mathcal D_m(\operatorname{perm}_n).
\]

The repository already proves the following derivative-shadow statement.

### Permanent derivative-shadow theorem

For every nonzero \(f\in E_m\) and every \(1\le a\le m\),

\[
\dim \partial^a f\ge \binom ma^2.
\tag{1.1}
\]

The proof uses the row-column torus to specialize \(f\) to one \(m\times m\)
subpermanent and upper semicontinuity of derivative-matrix rank.

Taking \(a=m-1\) gives the only permanent-side input needed below:

\[
\boxed{
0\ne f\in E_m
\quad\Longrightarrow\quad
\dim\partial^{m-1}f\ge m^2.
}
\tag{1.2}
\]

This note does not reclassify (1.1) as a new theorem.  Its contribution is to
replace the earlier term-count upper bound by the dimension of the **actual
joint factor span**, and to derive the quotient and projection consequences.

## 2. Factor-span upper shadow

Let \(L\subseteq V_n\) be a linear subspace.  If

\[
f\in\operatorname{Sym}^mL,
\]

then every order-\((m-1)\) derivative of \(f\) is a linear form in \(L\).
Therefore

\[
\boxed{
\dim\partial^{m-1}f\le \dim L.
}
\tag{2.1}
\]

For a Chow term

\[
T=\ell_1\cdots\ell_n,
\qquad
L_T=\operatorname{span}\{\ell_1,\ldots,\ell_n\},
\]

one has

\[
\mathcal D_m(T)\subseteq\operatorname{Sym}^mL_T.
\tag{2.2}
\]

This containment remains true when factors repeat or are linearly dependent.

## 3. The factor-span zero-block theorem

Let \(T_1,\ldots,T_q\) be degree-\(n\) Chow terms and put

\[
L_I=\sum_{i\in I}L_{T_i},
\qquad
F_i=\mathcal D_m(T_i)
\]

for a set of labels \(I\subseteq\{1,\ldots,q\}\).

### Theorem 3.1 -- low-span blocks are permanent-invisible

If

\[
\dim L_I<m^2,
\tag{3.1}
\]

then

\[
\boxed{
E_m\cap\sum_{i\in I}F_i=0.
}
\tag{3.2}
\]

### Proof

Every element of the literal sum belongs to

\[
\sum_{i\in I}F_i
\subseteq
\operatorname{Sym}^mL_I.
\]

If a nonzero \(f\) also belonged to \(E_m\), then (1.2) would give

\[
\dim\partial^{m-1}f\ge m^2,
\]

whereas (2.1) would give

\[
\dim\partial^{m-1}f\le\dim L_I<m^2.
\]

This is impossible. ∎

### Coupled-image boundary

For the actual polynomial sum

\[
R_I=\sum_{i\in I}T_i,
\]

the proof uses only

\[
\mathcal D_m(R_I)
\subseteq
\sum_{i\in I}\mathcal D_m(T_i).
\]

It never replaces the coupled catalectic image by the literal sum.  Thus
Theorem 3.1 also implies

\[
E_m\cap\mathcal D_m(R_I)=0,
\]

but no equality of the two right-hand spaces is asserted.

## 4. Removing a low-span block inside a larger literal sum

Let

\[
U=\sum_{i=1}^qF_i,
\qquad
A=E_m\cap U,
\]

and suppose \(I\) satisfies (3.1).  Consider the sum map

\[
\pi:\bigoplus_{i=1}^qF_i\longrightarrow U.
\]

Choose a linear section

\[
s:A\longrightarrow\bigoplus_iF_i
\]

of \(\pi\) over \(A\), and project \(s(A)\) to the components with labels
outside \(I\).

If an element belongs to the kernel of this projection, its selected lift is
supported only on \(I\).  Its sum therefore belongs to

\[
E_m\cap\sum_{i\in I}F_i=0.
\]

Because \(s\) is a section, the original element is zero.  Hence the
projection is injective and:

### Corollary 4.1 -- zero-defect block projection

\[
\boxed{
\dim\left(E_m\cap\sum_{i=1}^qF_i\right)
\le
\sum_{i\notin I}\dim F_i.
}
\tag{4.1}
\]

Since \(\dim F_i\le\binom nm\),

\[
\boxed{
\dim\left(E_m\cap\sum_{i=1}^qF_i\right)
\le
(q-|I|)\binom nm.
}
\tag{4.2}
\]

Unlike a term-count-only zero-intersection criterion, the removed block may
contain arbitrarily many terms provided their **combined** factor span remains
below \(m^2\).

## 5. Exact quotient intersections and vanishing matched differences

Let \(F,G\subseteq\operatorname{Sym}^mV_n\) and let

\[
\rho:\operatorname{Sym}^mV_n\longrightarrow
\operatorname{Sym}^mV_n/E_m
\]

be the quotient map.

### Lemma 5.1

If

\[
E_m\cap(F+G)=0,
\tag{5.1}
\]

then

\[
\boxed{
\rho(F)\cap\rho(G)=\rho(F\cap G).
}
\tag{5.2}
\]

### Proof

Take \(\rho(f)=\rho(g)\) with \(f\in F\), \(g\in G\).  Then

\[
f-g\in E_m\cap(F+G)=0.
\]

Thus \(f=g\in F\cap G\), proving the reverse inclusion in (5.2); the forward
inclusion is automatic. ∎

In the exact sequence used by the matched-difference program,

\[
0\longrightarrow\rho(F\cap G)
\longrightarrow\rho(F)\cap\rho(G)
\overset{\Delta}{\longrightarrow}\operatorname{im}\Delta
\longrightarrow0,
\tag{5.3}
\]

Lemma 5.1 says precisely:

\[
\boxed{\operatorname{im}\Delta=0.}
\tag{5.4}
\]

### Corollary 5.2 -- low-span quotient exactness

For Chow terms \(T,U\), if

\[
\dim(L_T+L_U)<m^2,
\tag{5.5}
\]

then

\[
\boxed{
\rho(\mathcal D_m(T))\cap\rho(\mathcal D_m(U))
=
\rho\bigl(
\mathcal D_m(T)\cap\mathcal D_m(U)
\bigr).
}
\tag{5.6}
\]

This closes the matched-difference part of the pairwise problem on every
low-total-span stratum.

## 6. A literal-overlap cap for unequal independent frames

Assume that the factors of \(T\) are linearly independent, and put

\[
K=L_T\cap L_U,
\qquad
k=\dim K.
\]

First,

\[
\operatorname{Sym}^mL_T\cap\operatorname{Sym}^mL_U
=
\operatorname{Sym}^mK.
\tag{6.1}
\]

Indeed, choose a direct-sum decomposition

\[
V_n=K\oplus A\oplus B\oplus C,
\qquad
L_T=K\oplus A,
\qquad
L_U=K\oplus B,
\]

and compare the resulting multigradings.

The squarefree derivative space

\[
\mathcal D_m(T)
\]

is invariant under the diagonal torus in the factor basis of \(T\).  Specialize
the \(k\)-plane \(K\subseteq L_T\) to a torus-fixed coordinate \(k\)-plane in
the complete Grassmannian.  Intersection dimension with the fixed squarefree
space can only increase under specialization.  At a coordinate \(k\)-plane,
the intersection is spanned by the squarefree \(m\)-fold products supported
there, and has dimension \(\binom km\).  Consequently:

### Proposition 6.1 -- factor-span literal cap

For independent factor frames,

\[
\boxed{
\dim\bigl(
\mathcal D_m(T)\cap\mathcal D_m(U)
\bigr)
\le\binom km.
}
\tag{6.2}
\]

The same conclusion follows if the roles of \(T\) and \(U\) are reversed; only
one independent frame is needed for the displayed argument, while the
applications below use two.

Combining (5.6) and (6.2) gives:

### Corollary 6.2 -- exact low-span pair cap

If both frames are independent and

\[
\dim(L_T+L_U)<m^2,
\]

then

\[
\boxed{
\dim\bigl(
\rho(\mathcal D_m(T))
\cap
\rho(\mathcal D_m(U))
\bigr)
\le
\binom{\dim(L_T\cap L_U)}m.
}
\tag{6.3}
\]

For pairs whose factor spans both have dimension \(n\), write

\[
k=\dim(L_T\cap L_U).
\]

Then the exactness condition is

\[
2n-k<m^2.
\tag{6.4}
\]

## 7. Central-degree consequences

Take

\[
m=\left\lceil\frac n2\right\rceil.
\]

### 7.1 Same-span clusters

If all terms in a block have their factors in one \(n\)-dimensional space,
then Theorem 3.1 applies whenever

\[
n<m^2.
\]

This holds for

\[
n=3
\quad\text{and every}\quad
n\ge5.
\]

Thus, at the central output degree, **an arbitrarily large same-span block**
has zero intersection with the permanent derivative space in every such
degree.

In particular, the sharp same-span literal-overlap theorem of PR #44 becomes
an exact quotient-overlap theorem: the matched-difference image vanishes
identically.

The equality case \(n=4,m=2\) is not covered.

### 7.2 Every pair

Any two Chow factor spans have total dimension at most \(2n\).  Hence every
pair is quotient-exact whenever

\[
2n<m^2.
\]

At the central degree this holds for

\[
n=7
\quad\text{and all}\quad
n\ge9.
\]

This universal pair consequence is numerically consistent with the older
two-term shadow criterion.  The new content is the refinement by the **actual**
union span and its arbitrary-size cluster version.

### 7.3 Boundary tables

For \(n=5,m=3\), pair exactness holds when

\[
\dim(L_T\cap L_U)\ge2.
\]

For \(n=6,m=3\), it holds when

\[
\dim(L_T\cap L_U)\ge4.
\]

For \(n=7,m=4\), every pair is exact.

For \(n=8,m=4\), it holds for every pair with nonzero factor-span
intersection.  If the frames are independent, Corollary 6.2 further gives

\[
\dim\bigl(
\rho(\mathcal D_4(T))
\cap
\rho(\mathcal D_4(U))
\bigr)
\le\binom k4.
\]

Thus the quotient images are disjoint for \(k=1,2,3\).  The transverse case

\[
k=0,\qquad
\dim(L_T+L_U)=16=m^2
\]

is an exact boundary case and remains open.

For \(n=9,m=5\) and every larger central case in the audited table, every pair
is quotient-exact.

## 8. What this closes and what remains

### Closed

- low-total-span blocks have zero permanent-relative intersection;
- such blocks can be removed with zero projection defect;
- the matched-difference image vanishes on every low-total-span pair;
- same-span central pairs and clusters are fully reduced to literal overlap
  for \(n=3\) and \(n\ge5\);
- the PR #44 same-span bounds therefore apply directly in the permanent
  quotient on those strata;
- unequal independent frames receive the cap (6.3) whenever (6.4) holds.

### Open

- the strict boundary \(\dim(L_T+L_U)=m^2\);
- high-total-span pairs and blocks;
- the \(n=8,m=4,k=0\) transverse boundary;
- dependent-factor refinements of the binomial literal cap;
- conversion of these structural results into a new unconditional Chow-rank
  number;
- coupled multi-term collision beyond the safe literal inclusion.

The next compact problem is the equality-span boundary.  For `perm_8` at
output degree four, this is precisely the transverse pair case with two
eight-dimensional factor spans and zero intersection.  A theorem excluding or
classifying that case would complete pairwise matched-difference control at
the central `n=8` layer without building a new state-management framework.

## 9. Deterministic replay

Run

```bash
python scripts/general_factor_span_zero_blocks.py \
  --json /tmp/general_factor_span_zero_blocks.json
python scripts/general_factor_span_zero_blocks_independent.py
python -m unittest tests.test_general_factor_span_zero_blocks -v
```

Expected terminal markers:

```text
GENERAL_FACTOR_SPAN_ZERO_BLOCKS_AUDIT_PASS
GENERAL_FACTOR_SPAN_ZERO_BLOCKS_INDEPENDENT_PASS
```

The primary audit verifies the central thresholds, the pair strata for
\(n=5,\ldots,10\), exact projection-capacity arithmetic and the frozen payload.
The independent implementation rebuilds the \(m^2\) linear-shadow count from
all perfect matchings of `perm_m` for \(m\le7\), imports none of the primary
functions and independently reconstructs the threshold tables.
