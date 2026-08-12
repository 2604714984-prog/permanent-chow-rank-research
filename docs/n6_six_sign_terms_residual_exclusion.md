# Six column-uniform sign terms cannot occur in a 25-term decomposition

## Status and scope

`PROOF_DRAFT_COMPLETE`, `RESTRICTED_FAMILY_THEOREM`.

This is a pure characteristic-zero exclusion for a mixed hypothetical
decomposition: the six fixed terms are column-uniform sign terms, while the
remaining nineteen terms may be arbitrary Chow terms.  It does not assume
that the full decomposition belongs to the sign family and does not prove the
unrestricted lower bound 26.

## 1. Statement

Normalize a column-uniform sign term as

\[
 T_\delta=\prod_{j=0}^5
 \left(\sum_{i=0}^5\delta_i x_{ij}\right),
 \qquad
 \delta=(1,\delta_1,\ldots,\delta_5)\in\{1\}\times\{\pm1\}^5.
\]

### Theorem 1.1

There is no decomposition

\[
 \operatorname{perm}_6
 =\sum_{s=1}^6a_sT_{\delta^{(s)}}+Q,                \tag{1.1}
\]

where the six signatures are distinct, every `a_s` is nonzero, and `Q` has
Chow rank at most nineteen.

Repeated proportional sign terms can be collected, so the distinctness
hypothesis loses nothing for a minimum decomposition.

## 2. Independence of six sign cubes

For a signature `delta`, write

\[
 v_\delta=\delta^{\otimes3}\in(\mathbb Q^6)^{\otimes3}.
\]

### Lemma 2.1

Any six distinct vectors `v_delta` are linearly independent.

### Proof

Suppose a measure `c_delta`, supported on at most six Boolean points, satisfies

\[
 \sum_\delta c_\delta v_\delta=0.                 \tag{2.1}
\]

Because `delta_0=1`, the tensor entries in (2.1) include every Boolean
character of degrees zero, one, two, and three.  Hence all Fourier
coefficients of the measure in degrees at most three vanish.  Fourier
inversion writes the measure on the full five-cube as

\[
 c(x)=\chi_{[5]}(x)
 \left(a_0+\sum_{i=1}^5a_ix_i\right),              \tag{2.2}
\]

because the only remaining characters have degrees four and five.

The measure vanishes away from its support, so the affine linear factor in
(2.2) vanishes at at least 26 cube vertices.  A nonzero affine linear function
on the five-cube vanishes at at most 16 vertices: choose one variable with
nonzero coefficient, and for each assignment of the other four variables at
most one of its two signs solves the equation.  Therefore the affine factor,
and hence the measure, is zero.  This proves the lemma.

## 3. Exact central dimensions

Put

\[
 R=\sum_{s=1}^6a_sT_{\delta^{(s)}},
 \qquad H=D_3(R),
 \qquad E=D_3(\operatorname{perm}_6).
\]

Decompose by the three output columns.  There are twenty identical blocks.
In one block let `S` be the matrix whose six columns are the sign cubes
`v_delta`, and let `A=diag(a_1,...,a_6)`.  The middle catalectic block of `R`
is

\[
 SAS^{\mathsf T}.                                  \tag{3.1}
\]

Lemma 2.1 says that `S` has column rank six.  Since `A` is invertible,
(3.1) also has rank six.  Consequently

\[
 \boxed{h=\dim H=20\cdot6=120.}                   \tag{3.2}
\]

Let `D` be the `6 x 6` matrix with columns `delta^(s)`.  A vector
`sum_s c_s v_delta(s)` lies in the cubic-subpermanent block precisely when
all repeated-row entries vanish.  Those entries are

\[
 \sum_sc_s\delta_j^{(s)},
\]

so the block intersection has dimension `6-rank(D)`.  Thus

\[
 b=\dim(E\cap H)=20(6-\operatorname{rank}D).       \tag{3.3}
\]

The six signatures lie in the affine hyperplane with first coordinate one.
If `rank(D)=r`, they lie in an affine space of dimension at most `r-1`.
Projection onto suitable `r-1` coordinates is injective on that affine space,
which contains at most `2^(r-1)` Boolean vertices.  Six distinct vertices
therefore force `r>=4`.  Equation (3.3) gives

\[
 \boxed{b\leq40.}                                  \tag{3.4}
\]

## 4. Residual contradiction

If (1.1) held, the middle catalectic of `Q` would have rank at most
`19*20=380`.  The symmetric double-quotient inequality gives

\[
 400+h-2b\leq380,
\]

or

\[
 h\leq2b-20.                                      \tag{4.1}
\]

But (3.2) and (3.4) give

\[
 120=h\leq2b-20\leq60,
\]

a contradiction.  This proves Theorem 1.1.

## 5. Boundary

The result excludes six column-uniform sign terms as the fixed part of a
hypothetical 25-term decomposition even when the residual nineteen terms are
arbitrary.  It does not cover general column-sign terms whose signs vary by
column, arbitrary row-homogeneous terms, or unrestricted Chow terms.  The
active high-intersection problem therefore remains genuinely non-coordinate
and non-column-uniform.
