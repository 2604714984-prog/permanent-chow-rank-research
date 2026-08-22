# General-`n` permanent Chow-rank master inventory — 2026-08-22

## Purpose and evidence boundary

This document records the current accessible mathematical state before the
next general-`n` research increment.  It is a source map, not a replacement
for `RESEARCH_LEDGER.md`, `STATUS.md`, or `RESEARCH_HANDOFF.md`.

The repository contains several long-lived parallel branches.  A theorem on a
parallel branch is reported with its branch status and is not silently promoted
to `main` or to the active PR stack.  Route ceilings below are ceilings on the
named proof mechanisms, not upper bounds on actual Chow rank.

Inventory base:

```text
repository: 2604714984-prog/permanent-chow-rank-research
base branch: research/quartic-six-circuit-compatibility
base Draft PR: #92
inventory branch: research/general-n-master-inventory-partition-optimization
```

## 1. Numerical boundaries visible in the active general-`n` stack

```text
ChowRank(perm_3) = 4
ChowRank(perm_4) = 8
ChowRank(perm_5) = 16                proof draft complete, replayed
28 <= ChowRank(perm_6) <= 32         active-stack boundary
49 <= ChowRank(perm_7) <= 64         stacked draft
90 <= ChowRank(perm_8) <= 128        stacked draft
164 <= ChowRank(perm_9) <= 256       stacked draft
307 <= ChowRank(perm_10) <= 512      stacked draft
```

A parallel branch, `agent/general-column-sign-rank`, contains a post-audit
internal proof package claiming the exact ordinary value
`ChowRank(perm_6)=32`.  That result is not integrated into the active
`research/quartic-six-circuit-compatibility` ancestry and must remain labelled
as a parallel proof draft until the branches are reconciled and audited
against one common head.

The universal explicit upper construction remains Glynn's
`2^(n-1)`-term decomposition.

## 2. Exact permanent derivative module

For every `0<=d<=n`,

\[
\dim \mathcal D_d(\operatorname{perm}_n)=\binom nd^2.
\]

The basis is indexed by pairs of `d`-subsets of rows and columns, and
contraction deletes one row and one column.  Thus the complete derivative
module is a double-Boolean incidence module, whereas an independent Chow term
has one Boolean factor-subset module.

The hereditary profile theorem strengthens the dimension formula: for every
nonzero

\[
0\ne f\in\mathcal D_d(\operatorname{perm}_n)
\]

and every `0<=j<=d`,

\[
\dim\mathcal D_j(f)\ge\binom dj^2.
\]

Primary sources:

```text
docs/general_n_research_program.md
docs/general_hereditary_profile_transversality.md
```

The second source currently lives on the parallel branch
`research/general-hereditary-profile-transversality`.

## 3. Scalar derivative-profile and shadow program

### 3.1 Scalar-profile ceiling

Every monotone, positively homogeneous, subadditive lower bound that factors
only through the scalar derivative dimensions is at most

\[
\binom n{\lfloor n/2\rfloor}
\]

on the permanent.  Adding more scalar catalecticant degrees, nonnegative
weights, or raw adjacent-kernel dimensions cannot recover Glynn scale.

### 3.2 Exact product shadows

Simultaneous permanent derivative shadows are solved by exact Ferrers integer
programs.  These feed the cross-degree projection, recursive derivative-tower
capacity, prefix min-plus envelope, and max-plus deficit formulations.

The full named scalar tower gives exact thresholds through `n=10`:

```text
n=3   Theta=4
n=4   Theta=8
n=5   Theta=15
n=6   Theta=27
n=7   Theta=49
n=8   Theta=90
n=9   Theta=164
n=10  Theta=307
```

Its proved asymptotic route ceiling is

\[
\Theta_n
=O\!\left(n^{1/4}\binom n{\lfloor n/2\rfloor}\right)
=O\!\left(\frac{2^n}{n^{1/4}}\right).
\]

This closes the current scalar-cardinality tower as a route to exact Glynn
optimality.  It does not close a shadow method strengthened by a uniform Chow
realizability defect.

Primary sources:

```text
docs/general_exact_product_shadow.md
docs/general_cross_degree_block_projection.md
docs/general_derivative_tower_capacity.md
docs/general_full_degree_tower_envelope.md
docs/general_shadow_complement_deficit_duality.md
docs/general_tower_tail_constants.md
docs/general_scalar_tower_polynomial_ceiling.md
```

## 4. Chow-realizability zero blocks

Let

\[
E_m(n)=\mathcal D_m(\operatorname{perm}_n),
\qquad
F_i=\mathcal D_m(T_i).
\]

The factor-span and private-polar line currently proves the following
universal zero ranges for arbitrary degree-`n` Chow terms.

### 4.1 Strict and closed endpoint

```text
joint factor-span dimension < m^2    => zero intersection
q*n = m^2, m>=3, q>=2               => zero intersection
```

The equality endpoint uses minimal-shadow direct-sum indecomposability of
permanent derivatives.

### 4.2 Hereditary-profile omission

If for some `1<=j<d`,

\[
q\binom nj<\binom dj^2,
\]

then a `q`-term block is invisible to `D_d(perm_n)`.  The corresponding safe
omission count is

\[
\sigma(n,d)
=
\max_{1\le j<d}
\left\lfloor
\frac{\binom dj^2-1}{\binom nj}
\right\rfloor.
\]

In central degrees this grows as

\[
\Omega\!\left(
\frac{((1+\sqrt2)/2)^n}{\sqrt n}
\right),
\]

but remains below the dominant central-binomial scale.

### 4.3 Positive-excess bands

The stacked private-polar and relation-matroid arguments prove:

```text
m>=3: q*n <= m^2+1       => zero
m>=3: q*n <= m^2+m-1     => zero
m>=4: q*n <= m^2+m       => zero
m>=4: q*n <= m^2+m+3     => zero
m>=5: q*n <= m^2+m+4     => zero
```

These are ordinary characteristic-zero statements.  They do not provide an
asymptotically large enough additive correction by themselves.

Primary sources:

```text
docs/general_factor_span_zero_blocks.md
docs/general_closed_factor_span_endpoint_zero_blocks.md
docs/general_first_excess_complete.md
docs/general_small_excess_private_polar_band.md
docs/general_excess_m_simplex_reduction.md
docs/general_excess_m_plus_four_band.md
```

## 5. Literal derivative-block function `mu(n,m)`

Define

\[
\mu(n,m)=\min\left\{
q:E_m(n)\cap\sum_{i=1}^q\mathcal D_m(T_i)\ne0
\right\}.
\]

This is a literal derivative-space threshold, not the Chow rank of
`perm_n` unless `m=n`.

### 5.1 Partition-Laplace envelopes

For a partition

\[
\lambda=(\lambda_1,\ldots,\lambda_b)\vdash m,
\]

the generalized Laplace expansion constructs

\[
q_\lambda=\frac{m!}{\prod_a\lambda_a!}
\]

Chow envelopes at every order

\[
n\ge n_\lambda:=\sum_a\lambda_a^2.
\]

Therefore

\[
\mu(n,m)\le
\min_{\lambda\vdash m:\ \sum_a\lambda_a^2\le n}
\frac{m!}{\prod_a\lambda_a!}.
\]

The repository proves the construction but has not yet solved this partition
optimization in general.

### 5.2 Exact cubic threshold

\[
\mu(n,3)=
\begin{cases}
4,&n=3,4,\\
3,&n=5,\\
2,&n=6,7,8,\\
1,&n\ge9.
\end{cases}
\]

### 5.3 Quartic status

The total-24 cells are classified:

```text
(n,m,q)=(12,4,2)  NONZERO
(n,m,q)=(8,4,3)   ZERO
(n,m,q)=(6,4,4)   ZERO
(n,m,q)=(4,4,6)   ZERO
```

The current active local boundary is

\[
6\le\mu(6,4)\le7.
\]

Five blocks are universally zero, seven blocks are explicitly nonzero, and
six blocks remain open.

Primary sources:

```text
docs/general_partition_laplace_envelopes.md
docs/general_sharp_pair_threshold.md
docs/general_cubic_three_term_zero.md
docs/general_quartic_four_block_zero.md
docs/general_quartic_three_block_zero.md
RESEARCH_HANDOFF.md
```

## 6. Restricted sign and polarization constructions

The repository proves

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=2^{n-1}.
\]

Uniform sign, one-defect, two-defect, full column-sign, and anchored diagonal
sign searches are closed within their stated families.

A separate one-missing-Walsh-character compression gives the general literal
upper construction

\[
\mu(n,m)\le2^{m-1}-1
\qquad(m\ge3,\ n\ge m+2).
\]

For quartics, fixed-axis variable-base and common-base mixed-split sign
families have threshold seven.  The fully variable 336-atom sign dictionary
is only partially closed: four and five atoms are zero, seven are nonzero,
and six remain open.  A prior claim of exact threshold seven was corrected
after the independent C++ projection scan found projected four-direction
states.

Primary sources:

```text
docs/general_column_sign_rigidity.md
docs/general_one_term_glynn_compression.md
docs/general_variable_base_glynn_compression_rigidity.md
docs/general_common_base_mixed_split_glynn_rigidity.md
docs/general_fully_variable_glynn_sign_dictionary_rigidity.md
```

## 7. Nonlinear apolar multiplication-tensor route

Every Chow-term apolar algebra is a quotient of a subalgebra of

\[
B_n=k[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2),
\]

and the apolar algebra of a sum is an algebra subquotient of the termwise
direct product.  Hence multiplication-tensor rank and border rank give valid
nonlinear Chow inequalities.

The permanent apolar algebra is the diagonal Segre product

\[
A_{\operatorname{perm}_n}\simeq B_n\#B_n,
\qquad
\dim A_{\operatorname{perm}_n}=\binom{2n}{n}.
\]

The current border multiplication bound recovers only

\[
\left\lceil\frac{\binom{2n}{n}}{2^n}\right\rceil,
\]

which is the equal-weight scalar-profile ratio.  The algebra-subquotient
framework is valid, but a stronger multiplication-complexity lower bound is
still needed.

Primary source on the parallel branch
`research/apolar-multiplication-tensor-framework`:

```text
docs/general_apolar_multiplication_tensor_framework.md
```

## 8. Named route ceilings and rejected shortcuts

The following mechanisms have been bounded at central-binomial or
sub-Glynn scale, or rejected because the required monotonicity fails:

```text
scalar Hilbert/derivative profiles
complete exact scalar shadow tower
standard unprojected Koszul-Young maps
fixed linear matching-image postprocessing
row-column projected catalecticants
two-sided matching-source compression
finite block-diagonal two-direction power profiles
growing powers W^p with p=p(n)
principal binary ideal profiles
exact-additive graded K0/syzygy scalarizations
full-orbit exact-additive representation profiles
raw Betti and higher-Fitting data without a subquotient theorem
common-factor count as a global overlap parameter
literal/coupled image identification without a theorem
```

The growing two-direction power ceiling is

\[
O\!\left(
(n\log(n+1))^{1/4}
\binom n{\lfloor n/2\rfloor}
\right)
=o(2^{n-1}).
\]

A route ceiling is not an upper bound on actual Chow rank.

## 9. Remaining general-`n` interfaces

The current high-value general interfaces are:

1. optimize the partition-Laplace envelope tradeoff in `(n,m)` and compare it
   with the Walsh and multirow-polarization constructions;
2. prove a uniform Chow-realizability defect beyond scalar exact-shadow
   Ferrers spaces;
3. find a representation-valued or relation-valued invariant that is additive
   and monotone under both submodules and quotients;
4. analyze genuinely two-generator growing binary ideals rather than powers or
   principal ideals;
5. strengthen apolar multiplication complexity beyond algebra dimension;
6. obtain a cross-`n` restriction or valuation theorem, ideally a recurrence
   of the form `R_n>=2R_(n-1)`.

Finite `perm_6` and `perm_8` equality cells remain regression frontiers, not
the primary general-`n` objective of the present branch.

## 10. Selected next task

This branch selects exactly one task:

```text
OPTIMIZE THE PARTITION-LAPLACE ENVELOPE OVER ALL PARTITIONS OF m.
```

The deliverable must provide:

```text
an exact dynamic program for fixed (n,m)
a structural theorem for optimal partition shapes
comparison with the Walsh upper construction
an asymptotic tradeoff in the linear-order regime n=rho*m
an independent replay and frozen JSON
```

No broad solver framework, database, manager, or second control plane is
authorized.
