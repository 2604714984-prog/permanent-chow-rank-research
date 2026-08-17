# Nonuniform graded matrix images remain centrally bounded

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_INTEGER_REPLAYED`.

This note closes the nonuniform degree-shifted version of the binary
matrix-image route left open by the preceding homogeneous-matrix theorem.
Let

\[
R=k[s,t]
\]

and let

\[
\Phi:
\bigoplus_{a\in A}R(-a)^{q_a}
\longrightarrow
\bigoplus_{b\in B}R(-b)^{p_b}
\tag{0.1}
\]

be a degree-zero graded map. Its `(b,a)` block has entries of degree `a-b`.
For a graded `R`-module `M`, define

\[
\rho_{\Phi,d}(M)
=
\dim\operatorname{im}
\left(
\Phi_{M,d}:
\bigoplus_a M_{d-a}^{q_a}
\longrightarrow
\bigoplus_b M_{d-b}^{p_b}
\right).
\tag{0.2}
\]

The main theorem is

\[
\boxed{
R_{\Phi,n,d}
\le
\binom n{\lfloor n/2\rfloor}
\sum_{(b,a)\in\mathcal B_d}p_bq_a
\le
pq\binom n{\lfloor n/2\rfloor},
}
\tag{0.3}
\]

where

\[
p=\sum_bp_b,
\qquad
q=\sum_aq_a,
\]

and `mathcal B_d` is the set of nonzero shift blocks acting between nonzero
Boolean levels at degree `d`.

Consequently, if `p,q<=K_n`, this route proves at most

\[
K_n^2\binom n{\lfloor n/2\rfloor}.
\tag{0.4}
\]

A route of this exact type that reaches Glynn scale must therefore satisfy

\[
\boxed{
K_n
\ge
(1+o(1))
\left(\frac{\pi n}{8}\right)^{1/4}.
}
\tag{0.5}
\]

This is a ceiling on one matrix-image lower-bound mechanism. It is not an
upper bound on actual Chow rank. It does not cover joint Fitting/minor data,
kernels or Betti numbers without a monotonicity theorem, higher syzygy
modules, representation-valued invariants, valuative arguments, or uniform
Chow-realizability defects.

## 1. The inherited monotone interface

The parent theorem proves that for every homogeneous polynomial matrix,
`rho_(Phi,d)` is

1. additive on direct sums;
2. nonincreasing under submodules; and
3. nonincreasing under quotients.

If

\[
f=T_1+\cdots+T_m,
\]

then the apolar subquotient theorem gives

\[
\rho_{\Phi,d}(A_f;W)
\le
m\,\beta_{\Phi,n,d},
\tag{1.1}
\]

where `beta` is the maximum Boolean image rank over all linear maps from the
selected differential two-plane into `(B_n)_1`.

Thus the matrix-image invariant certifies at most

\[
R_{\Phi,n,d}
=
\left\lceil
\frac{\rho_{\Phi,d}(A_{\operatorname{perm}_n};W)}
{\beta_{\Phi,n,d}}
\right\rceil.
\tag{1.2}
\]

The proof below bounds this ratio. No coupled apolar algebra is identified
with a literal direct sum.

## 2. Shift-block decomposition

Write

\[
\Phi=(\Phi_{b,a})_{b\in B,a\in A}.
\]

Degree zero in (0.1) means

\[
\Phi_{b,a}
\in
\operatorname{Mat}_{p_b\times q_a}(R_{a-b}),
\tag{2.1}
\]

with the convention that the block is zero when `a-b<0`.

At degree `d`, the block is

\[
(\Phi_{b,a})_{M,d}:
M_{d-a}^{q_a}
\longrightarrow
M_{d-b}^{p_b}.
\tag{2.2}
\]

Let `mathcal B_d` consist of the nonzero blocks for which both source and
target levels in (2.2) are nonzero. For a block in `mathcal B_d`, write

\[
r_{b,a}
=
\operatorname{rank}_{k(s,t)}\Phi_{b,a}\ge1.
\tag{2.3}
\]

### Lemma 2.1 -- numerator decomposition

For every graded module `M`,

\[
\boxed{
\rho_{\Phi,d}(M)
\le
\sum_{(b,a)\in\mathcal B_d}
\rho_{\Phi_{b,a},d}(M).
}
\tag{2.4}
\]

### Proof

The full map is the sum of the block maps after the natural inclusions of
their source and target summands. Its image is contained in the sum of the
block images. Taking dimensions gives (2.4). No directness is asserted. ∎

### Lemma 2.2 -- envelope domination

For every active block,

\[
\boxed{
\beta_{\Phi,n,d}
\ge
\beta_{\Phi_{b,a},n,d}.
}
\tag{2.5}
\]

### Proof

Restrict the source to the `a`-shifted columns and project the target to the
`b`-shifted rows. The resulting map is exactly the block map. Therefore the
rank of the full Boolean map is at least the rank of that projected
restriction.

The Boolean term envelope is a maximum over all maps from the differential
two-plane. The maximizing witness may depend on `(b,a)`; no common line
specialization for all blocks is required. ∎

## 3. The exact block denominator and numerator

Put

\[
H_j=\binom nj,
\qquad
H_*=\binom n{\lfloor n/2\rfloor}.
\]

For one active block, define

\[
H_s=H_{d-a},
\qquad
H_t=H_{d-b}.
\]

The entries of `Phi_(b,a)` all have the common degree

\[
\delta=a-b.
\]

The homogeneous-matrix theorem applies to this block. A nonzero normal-rank
minor has a point `[alpha:beta]` where its value has rank `r_(b,a)`. Under the
legal Boolean specialization

\[
s\mapsto\alpha L,
\qquad
t\mapsto\beta L,
\qquad
L=z_1+\cdots+z_n,
\]

the block becomes a constant rank-`r_(b,a)` matrix tensored with
multiplication by `L^delta`. Strong Lefschetz gives

\[
\boxed{
\beta_{\Phi_{b,a},n,d}
\ge
r_{b,a}\min\{H_s,H_t\}.
}
\tag{3.1}
\]

The permanent apolar Hilbert function gives the source/target upper bound

\[
\boxed{
\rho_{\Phi_{b,a},d}(A_{\operatorname{perm}_n})
\le
\min\{q_aH_s^2,p_bH_t^2\}.
}
\tag{3.2}
\]

Consequently the isolated block route is bounded by

\[
R_{b,a}
\le
\left\lceil
\frac{\min\{q_aH_s^2,p_bH_t^2\}}
{r_{b,a}\min\{H_s,H_t\}}
\right\rceil.
\tag{3.3}
\]

As in the common-degree theorem,

\[
\frac{\min\{q_aH_s^2,p_bH_t^2\}}
{r_{b,a}\min\{H_s,H_t\}}
\le
\frac{\max\{p_b,q_a\}}{r_{b,a}}H_*.
\tag{3.4}
\]

## 4. Full nonuniform matrix ceiling

### Theorem 4.1 -- exact block-sum route ceiling

\[
\boxed{
R_{\Phi,n,d}
\le
\sum_{(b,a)\in\mathcal B_d}
\left\lceil
\frac{\min\{q_aH_{d-a}^2,p_bH_{d-b}^2\}}
{r_{b,a}\min\{H_{d-a},H_{d-b}\}}
\right\rceil.
}
\tag{4.1}
\]

### Proof

Let

\[
N=\rho_{\Phi,d}(A_{\operatorname{perm}_n}),
\qquad
\beta=\beta_{\Phi,n,d}.
\]

For each active block write `N_(b,a)` and `beta_(b,a)` for the corresponding
numerator and Boolean envelope. Lemmas 2.1 and 2.2 give

\[
\frac N\beta
\le
\sum_{(b,a)\in\mathcal B_d}
\frac{N_{b,a}}\beta
\le
\sum_{(b,a)\in\mathcal B_d}
\frac{N_{b,a}}{\beta_{b,a}}.
\]

Apply (3.1)--(3.2) and integer rounding. ∎

Define the active support area

\[
\omega_d(\Phi)
=
\sum_{(b,a)\in\mathcal B_d}p_bq_a.
\tag{4.2}
\]

### Corollary 4.2 -- support-area ceiling

\[
\boxed{
R_{\Phi,n,d}
\le
\omega_d(\Phi)H_*
\le
pqH_*.
}
\tag{4.3}
\]

### Proof

For positive integers `p_b,q_a` and `r_(b,a)>=1`,

\[
\frac{\max\{p_b,q_a\}}{r_{b,a}}
\le
p_bq_a.
\]

The right side times `H_*` is an integer, so (3.4) implies that each ceiling
in (4.1) is at most `p_bq_aH_*`. Summing proves the first inequality.

The active blocks form a subset of all shift pairs, hence

\[
\omega_d(\Phi)
\le
\sum_{a,b}p_bq_a
=
\left(\sum_bp_b\right)
\left(\sum_aq_a\right)
=pq.
\]

This proves the second inequality. ∎

The sharper rank-weighted block sum (4.1) should be used for concrete
matrices. Equation (4.3) is the uniform route ceiling.

## 5. Matrix-complexity consequence

If

\[
p,q\le K_n,
\]

then

\[
R_{\Phi,n,d}
\le
K_n^2H_*.
\tag{5.1}
\]

Stirling gives

\[
H_*
=
(1+o(1))
2^n\sqrt{\frac2{\pi n}}.
\]

A proof of Glynn-scale lower bound `2^(n-1)` through this exact mechanism must
therefore satisfy

\[
K_n^2
\ge
(1+o(1))
\sqrt{\frac{\pi n}{8}},
\]

or equivalently (0.5).

Thus every bounded-size nonuniform graded matrix is closed at central scale,
and every family with

\[
K_n=o(n^{1/4})
\]

is too small to reach Glynn scale through one matrix-image rank.

The common-degree theorem gives the stronger requirement `Omega(sqrt(n))`
when all entries lie in one degree block. Arbitrary shifts can distribute the
numerator among as many as `pq` active blocks, so the present general theorem
has the weaker but fully nonuniform `Omega(n^(1/4))` requirement.

## 6. Direct sums and finite matrix families

A finite collection of graded matrix-image invariants combined by adding
their image dimensions is equivalent to one block-diagonal graded matrix.
Therefore the theorem applies after replacing `p,q` by the total source and
target free ranks.

This observation does not cover nonlinear combinations such as joint minor
ideals, Fitting strata, maxima or intersections of determinantal loci.

## 7. Exact finite replay

The primary implementation exhausts all positive source and target shift
multiplicity compositions with total ranks at most four and every nonempty
admissible shift-block subset. It checks all active degrees for `3<=n<=9`.

The independent implementation instead assigns shifts to individual source
and target summands, groups them only afterwards, and checks five different
support patterns with exact `Fraction` arithmetic.

Primary boundary:

```text
shift-block patterns                 6,599
degree instances                   442,386
active block instances           1,013,292
maximum support-area ratio             1
```

Independent boundary:

```text
individual shift assignments         14,400
support-pattern instances             70,672
degree instances                   3,604,272
active block instances             4,956,408
positive direct-ratio instances    2,910,432
```

The replays validate the theorem-facing arithmetic and shift indexing. The
general proof is the block decomposition plus the homogeneous-block theorem,
not a finite extrapolation.

## 8. Research decision

The matrix-image frontier is now

```text
fixed 2 x 2 linear pencils                 CLOSED sharply
bounded common-degree matrices             CLOSED at central scale
bounded nonuniform shifted matrices        CLOSED at central scale
sub-n^(1/4) square matrix size              CLOSED for Glynn scale
large support-area matrix families         OPEN
joint Fitting/minor profiles                OPEN
higher syzygy and representation modules   OPEN
```

Another bounded presentation matrix, even with arbitrary grading shifts, is
not a valid default continuation. The next route must use information not
reducible to the sum of individual block-image dimensions.
