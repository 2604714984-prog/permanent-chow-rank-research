# Pairwise intersections of Chow derivative spaces

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_RATIONAL_REPLAYED`,
`GENERAL_N_ROUTE_DIAGNOSTIC`.

This note isolates the literal-intersection term in the exact sequence

\[
0\longrightarrow \rho(F\cap G)
\longrightarrow \rho(F)\cap\rho(G)
\longrightarrow \operatorname{im}\Delta
\longrightarrow0
\]

that arises when two Chow derivative spaces are compared modulo a permanent
derivative space.  It proves an exact formula in a transverse common-factor
frame and an exact counterexample to any bound that depends only on the
number of common projective factors.

The statements concern the **literal** spaces
\(\mathcal D_m(T)\) and \(\mathcal D_m(U)\).  They do not identify their sum
with the coupled catalectic image of \(T+U\), and they give no new
unrestricted Chow-rank lower bound.

## 1. Notation

Let \(V\) be a vector space over a characteristic-zero field.  For a
degree-\(n\) form \(f\), write

\[
\mathcal D_m(f)
\]

for the output-degree-\(m\) derivative space, equivalently the image of the
\((n-m,m)\) catalecticant.

If

\[
T=\ell_1\cdots\ell_n
\]

has linearly independent factors, then

\[
\mathcal D_m(T)
=
\operatorname{span}
\left\{
\ell_{i_1}\cdots\ell_{i_m}:
1\le i_1<\cdots<i_m\le n
\right\},
\tag{1.1}
\]

and therefore

\[
\dim\mathcal D_m(T)=\binom nm.
\tag{1.2}
\]

All intersection results below use this output-degree convention.

## 2. The transverse common-factor formula

Assume that

\[
T=
z_1\cdots z_s\,x_1\cdots x_{n-s},
\qquad
U=
z_1\cdots z_s\,y_1\cdots y_{n-s},
\tag{2.1}
\]

and that the union

\[
z_1,\ldots,z_s,
x_1,\ldots,x_{n-s},
y_1,\ldots,y_{n-s}
\]

is linearly independent.

### Theorem 2.1

For every \(0\le m\le n\),

\[
\boxed{
\mathcal D_m(T)\cap\mathcal D_m(U)
=
\operatorname{span}
\left\{
z_{i_1}\cdots z_{i_m}:
1\le i_1<\cdots<i_m\le s
\right\},
}
\tag{2.2}
\]

with the right side interpreted as zero when \(m>s\).  Consequently,

\[
\boxed{
\dim\bigl(\mathcal D_m(T)\cap\mathcal D_m(U)\bigr)
=
\binom sm.
}
\tag{2.3}
\]

### Proof

Use the independent union in (2.1) as coordinates.  Equation (1.1) gives a
squarefree monomial basis for each derivative space.  A basis monomial from
\(\mathcal D_m(T)\) can use only the \(z\)'s and \(x\)'s; a basis monomial
from \(\mathcal D_m(U)\) can use only the \(z\)'s and \(y\)'s.  Since all
coordinate monomials are linearly independent, a monomial belongs to both
spaces exactly when it uses only the shared \(z\)'s.  This proves (2.2) and
(2.3). \(\square\)

### Corollary 2.2 -- the \(n-1\)-factor merge rule

If two nonzero degree-\(n\) Chow terms share \(n-1\) projective factors, then
their sum is one Chow term:

\[
c\,z_1\cdots z_{n-1}x
+
d\,z_1\cdots z_{n-1}y
=
z_1\cdots z_{n-1}(cx+dy).
\tag{2.4}
\]

If the last factor vanishes, the two terms cancel.  Hence a
support-minimal decomposition cannot contain two distinct nonzero terms that
share \(n-1\) projective factors.

This is an ordinary support simplification.  It does not imply a comparable
rule for \(n-2\) common factors.

## 3. A zero-common-factor overlap family

The transverse formula is not a global bound in terms of shared factors.

Let \(n=2r\), let

\[
V=\bigoplus_{i=1}^r
\operatorname{span}\{x_i,y_i\},
\]

and define

\[
T=\prod_{i=1}^r x_i y_i,
\qquad
U=\prod_{i=1}^r (x_i+y_i)(x_i-y_i).
\tag{3.1}
\]

The two terms have no common projective factor.

### Theorem 3.1 -- block-rotation overlap

For \(0\le m\le 2r\),

\[
\boxed{
\dim\bigl(\mathcal D_m(T)\cap\mathcal D_m(U)\bigr)
=
\begin{cases}
2^m\binom rm,&m\le r,\\
0,&m>r.
\end{cases}
}
\tag{3.2}
\]

### Proof

Give the symmetric algebra the multigrading by the \(r\) two-dimensional
blocks.  In one block, the local output-degree spaces for \(T\) are

\[
\mathbf k,\qquad
\operatorname{span}\{x_i,y_i\},\qquad
\operatorname{span}\{x_i y_i\},
\tag{3.3}
\]

in local degrees \(0,1,2\).  The corresponding spaces for \(U\) are

\[
\mathbf k,\qquad
\operatorname{span}\{x_i+y_i,x_i-y_i\}
=
\operatorname{span}\{x_i,y_i\},\qquad
\operatorname{span}\{x_i^2-y_i^2\}.
\tag{3.4}
\]

The local degree-two lines in (3.3) and (3.4) are disjoint.  Therefore a
multidegree component contributes to the global intersection if and only if
every active block has local degree one.  Choose \(m\) of the \(r\) blocks;
on each selected block the common degree-one space has dimension two.  This
gives

\[
\binom rm 2^m
\]

when \(m\le r\).  If \(m>r\), every block multidegree of total degree \(m\)
contains a local degree-two block, so the intersection is zero. \(\square\)

The central examples are

\[
\dim\bigl(\mathcal D_3(T)\cap\mathcal D_3(U)\bigr)=8
\quad(n=6),
\tag{3.5}
\]

\[
\dim\bigl(\mathcal D_4(T)\cap\mathcal D_4(U)\bigr)=16
\quad(n=8),
\tag{3.6}
\]

and

\[
\dim\bigl(\mathcal D_5(T)\cap\mathcal D_5(U)\bigr)=32
\quad(n=10).
\tag{3.7}
\]

Thus even zero shared factors do not force a small literal derivative-space
intersection.

## 4. Consequence for the matched-difference program

Suppose \(E\) is a permanent derivative space and

\[
E\cap F=E\cap G=0,
\qquad
F=\mathcal D_m(T),
\qquad
G=\mathcal D_m(U).
\]

Let \(\rho\) be the quotient map modulo \(E\), put

\[
H=\rho(F)\cap\rho(G),
\]

and match the unique lifts of elements of \(H\).  Their difference defines
\(\Delta:H\to E\).  The correct sequence is

\[
0\longrightarrow \rho(F\cap G)
\longrightarrow H
\overset{\Delta}{\longrightarrow}
\operatorname{im}\Delta
\longrightarrow0.
\tag{4.1}
\]

The exact permanent product-shadow theorem may control
\(\operatorname{im}\Delta\), but it does not control \(F\cap G\).

Theorem 2.1 gives the literal term exactly under a transverse common-factor
hypothesis.  Theorem 3.1 proves that the number of common factors alone is
insufficient: frame geometry can create a substantial literal overlap even
when the common-factor count is zero.

Accordingly, the next valid invariant must retain at least one of:

1. the relative position of the two factor frames;
2. the multigraded apolar intersection;
3. the common-section cocycle coupling literal overlap to
   \(\operatorname{im}\Delta\); or
4. a permanent-relative incidence condition excluding the block-rotation
   family.

A theorem stated only in terms of the number of shared projective factors is
not sufficient.

## 5. Hidden assumptions and strongest objection

### Hidden assumptions

The transverse formula assumes one independent union of shared and unshared
factors.  It is not asserted after arbitrary collisions, linear dependencies,
or changes of basis inside a common factor span.

The rotation theorem uses characteristic different from two.  The repository
works in characteristic zero, so this causes no transfer issue.

### Strongest objection

The block-rotation pair is an abstract pair of Chow terms.  It is not shown to
occur inside the permanent-relative final frontier.  Therefore it is a route
barrier, not a counterexample to a stronger theorem that uses the actual
permanent quotient, coupled sum, or section-difference cocycle.

That objection is correct.  The result narrows the next theorem: it must be
permanent-relative or frame-sensitive rather than factor-count-only.

## 6. Deterministic reproduction

Run

```bash
python scripts/general_pairwise_chow_overlap.py \
  --json /tmp/general_pairwise_chow_overlap.json
python scripts/general_pairwise_chow_overlap_independent.py
python -m unittest tests.test_general_pairwise_chow_overlap -v
```

Expected terminal markers:

```text
GENERAL_PAIRWISE_CHOW_OVERLAP_AUDIT_PASS
GENERAL_PAIRWISE_CHOW_OVERLAP_INDEPENDENT_PASS
```

The primary replay expands the rotated factors and computes the exact
projection rank over `Fraction`.  The independent replay imports none of the
primary implementation and uses the block multidegree proof directly.
