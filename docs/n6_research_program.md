# `n=6` research program

## Status

`OPEN`. The current in-repository proof-draft interval is

\[
25
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 25 is the fixed-six relation-module argument in
`docs/n6_fixed_six_lower25.md`. The upper bound is Glynn's 32-term
decomposition. No lower-26, border-lower-25, or exact-32 claim is made.

The central first-Koszul fixed-count route, the first higher-wedge ratio route,
the scalar second-shadow route, the scalar second-Koszul homology route, and
two explicit low-base sign-aggregate constructions have now been tested. None
proves lower 26 or produces a sub-32 decomposition.

## 1. Exact numerical baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
\operatorname{rank}K_{6,3}(\operatorname{perm}_6)=14175.
\]

One degree-six Chow term contributes at most 20 to the middle catalectic and
at most 705 to the first Koszul flattening.

The lower-bound history is

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
fixed-four scalar prolongation:         24
fixed-six vector relation module:       25
```

## 2. What closed the 24-term problem

Assume a hypothetical 24-term decomposition and fix six terms. The residual
has eighteen terms. The quadratic projection cap is

\[
5\cdot15+3=78.
\]

Bukh compression and the symmetric middle catalectic give

\[
40\le b\le64,
\]

where

\[
b
=
\dim\left(
\mathcal D_3(\operatorname{perm}_6)
\cap
\mathcal D_3(R)
\right).
\]

The layers `b=40,41` are first-Koszul strict. For the other layers, the
vector-valued Macaulay theorem controls the complete colored relation module:

\[
\dim\mathcal K^{(1)}
\le
(\dim\mathcal K)^{\langle2\rangle}.
\]

A block-Sylvester inequality gives

\[
\operatorname{rank}C_{3,3}(R)
\ge
\sum_i\operatorname{rank}C_{3,3}(T_i)
-
2(\dim\mathcal K)^{\langle2\rangle}.
\]

Exact defect arithmetic excludes every `42<=b<=64`; the smallest strict
margins are two at `b=43,44`.

The proof preserves the coupled-catalectic boundary: `D_3(R)` is always the
image of the catalectic of the sum. Literal sums of individual derivative
spaces are used only as ambient spaces and explicit relation modules.

## 3. Reusable vector-valued Macaulay theorem

For arbitrary finite-dimensional `W,V` and

\[
\mathcal K\subseteq W\otimes\operatorname{Sym}^2V,
\qquad
\dim\mathcal K=k,
\]

the first prolongation satisfies

\[
\boxed{
\dim\mathcal K^{(1)}\le k^{\langle2\rangle}.
}
\]

The proof uses a universal Grassmannian kernel, upper semicontinuity, an
explicit colored-monomial one-parameter subgroup, scalar apolar Macaulay
growth, and superadditivity. The small finite-field replay is diagnostic only.

## 4. Completed lower-26 fixed-count diagnostic

A lower bound of 26 would require excluding a 25-term decomposition. Exact
fixed-count arithmetic evaluated

\[
q\in\{6,7,8\}
\]

fixed terms:

| fixed terms | initial states | central-pruned survivors | structural states | maximum relation cap |
|---:|---:|---:|---:|---:|
| 6 | 1,035 | 327 | 269 | 37 |
| 7 | 1,225 | 355 | 290 | 33 |
| 8 | 1,520 | 635 | 584 | 33 |

Six fixed terms are arithmetically smallest, but the frontier is not compact.
No fixed count is selected and the central first-Koszul state route is
suspended for lower 26.

## 5. Completed alternative-route diagnostics

### 5.1 First higher-wedge Koszul differential

For

\[
\delta_2:
D_m(f)\otimes\Lambda^2V
\to
D_{m-1}(f)\otimes\Lambda^3V,
\]

the exact output-degree ranks give integer ratios

```text
m=2: 15
m=3: 21
m=4: 16
```

identical to the corresponding ordinary first-Koszul integer bounds. The first
higher wedge does not improve the base ratio.

### 5.2 Scalar second shadow

If

\[
b=\binom{x}{3}^2,
\]

then the iterated two-dimensional shadow bound gives

\[
\dim\partial^2S\ge x^2.
\]

For every tested fixed count `q>=6`, however,

\[
\dim D_1(R)\le\min(36,6q)=36,
\]

so the result is only `b<=400`, the full ambient central dimension.

### 5.3 Scalar second-Koszul homology

The output-degree-two complex has exact ranks

\[
\operatorname{rank}\delta_2(\operatorname{perm}_6)=127125,
\qquad
\operatorname{rank}\delta_2(T)=8730
\]

for one independent Chow term. The integer ratio is 15.

A coupled common-factor family satisfies

\[
h_{2,4}\left(\sum_{i=1}^rT_i\right)
=15r+25\binom r2.
\]

At `r=6` this equals 465, already larger than the permanent's 450. Hence a
monotone scalar homology upper bound cannot prove lower 26.

### Diagnostic decision

```text
CENTRAL_FIXED_COUNT_ROUTE=SUSPENDED
HIGHER_WEDGE_BASE_RATIO=NO_IMPROVEMENT
SCALAR_SECOND_SHADOW=VACUOUS
SCALAR_HOMOLOGY_UPPER_BOUND=REJECTED
```

These are route diagnostics, not impossibility theorems for lower 26.

## 6. Xu--Gnang author postmortem

Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
arXiv:2311.05890, is the repository owner's own earlier line. It is withdrawn
and treated as disproved. Its row-homogeneous optimality claim is not a theorem
dependency, an external novelty gate, or a positive input to the current
program.

The postmortem remains useful only for recording the failed projection,
product-tensor dependence, and automorphism-rigidity steps so that they are not
reintroduced.

## 7. Completed sign-family results

Let `G=(Z/2Z)^5` index normalized six-entry sign vectors.

### 7.1 Uniform Glynn family

The 32 fixed column-uniform Glynn products are linearly independent, and the
unique expression of the permanent in their span uses every term. This is a
strict-subfamily result only.

### 7.2 One-defect family

Allow one column to use a second sign vector. The family has 5,984 distinct
terms and span dimension 987. Exact Fourier-parity analysis gives

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

### 7.3 Two-defect parity blocks

Allow two columns to use independent defect vectors. The family has 467,264
distinct terms and exact parity-block ranks

```text
406, 406, 406, 322, 322, 207,
```

with total span dimension 11,533.

A quadratic separator first reduced base-aggregate support to 24. Exact
fixed-base atomic ranks

\[
\rho_2(f)=\rho_2(1-f)=46
\]

show that this fixed assignment costs exactly 744 actual terms.

A count-product separator

\[
g(r)=n_4(r)n_5(r)
\]

then reduced aggregate support to 16. A row retraction

```text
1,2,3 -> 0
0,4,5 fixed
```

reduces the full fixed-base dictionary for `g` to sign labels
`{0,8,16,24}` without increasing support. Exact local normal forms and a
complete extra-budget search prove

\[
\boxed{\rho_2(g)=36.}
\]

Therefore the 16-base assignment costs exactly

\[
16\cdot36=576
\]

actual terms.

### 7.4 Full column-sign and row-sign families

The Boolean monomial slice in `docs/general_column_row_sign_rank.md` removes the
need to optimize two-defect aggregate assignments.  Every normalized
column-sign term, with arbitrary signs in every column, restricts to one Walsh
character on a `32`-point slice.  The permanent restricts to a delta function
whose 32 Fourier coefficients are all nonzero.  Therefore

\[
\boxed{
\operatorname{ColumnSignRank}(\operatorname{perm}_6)
=
\operatorname{RowSignRank}(\operatorname{perm}_6)
=32.}
\]

The full two-defect family is a subfamily of the column-sign family and contains
the 32 Glynn terms, so its exact minimum is also 32.

### Sign-route conclusion

```text
UNIFORM_MINIMUM=32
ONE_DEFECT_MINIMUM=32
FULL_COLUMN_SIGN_MINIMUM=32
FULL_ROW_SIGN_MINIMUM=32
GLOBAL_TWO_DEFECT_MINIMUM=32
FIRST_TWO_DEFECT_FIXED_ASSIGNMENT_COST=744
SECOND_TWO_DEFECT_FIXED_ASSIGNMENT_COST=576
SIGN_ROUTE=CLOSED
```

Low aggregate support is not a reliable proxy for actual term support.  The two
explicit separator constructions remain useful exact examples, but the global
sign minimum is now closed without optimizing their aggregate costs.

## 8. Sign-route closure

The former N6-24 joint aggregate-cost program is cancelled.  Its target was a
lower bound for a proper subfamily that G-022 now settles by a shorter theorem.
No full sign dictionary, sparse optimizer, or additional defect hierarchy is
authorized.

This closure has no unrestricted consequence.  A general Chow term may have a
zero row-zero anchor or arbitrary normalized diagonal coefficients.  In
particular, the diagonal monomial Chow term already restricts to the same delta
function on the Boolean slice, so the slice cannot lower-bound unrestricted
Chow rank.

## 9. Current unrestricted target: a coupled inverse-system invariant

Let

\[
\mathcal M(f)=\bigoplus_{m=0}^{6}\mathcal D_m(f)
\]

with its action by the full algebra of constant-coefficient differential
operators.  Degreewise dimensions, first higher wedges, scalar second shadows,
and scalar homology have reached their documented ceilings.  A new invariant
must use compatibility between degrees and relations, not another scalar sum of
dimensions.

The next theorem candidate must satisfy all of the following before any large
calculation starts:

1. it is functorial under `GL(V)`, so arbitrary Chow factors cannot evade it by
   changing coordinates;
2. it controls the inverse-system module of a coupled sum rather than replacing
   it by a literal direct sum of term modules;
3. it survives the exact six-term common-factor family from N6-017;
4. its single-term contribution is bounded for dependent and repeated factors;
5. its finite interface is small enough for exact rational or integer replay.

A concrete first step is to derive one universal inequality for a quotient of
the relation module of `M(sum_i T_i)` that couples two adjacent derivative
degrees.  If no such inequality beats the common-factor example on paper, the
route stops before implementation.

That first step is now completed in G-023.  Literal relation dimensions satisfy

\[
\kappa_{m+1}\le\kappa_m^{\langle m\rangle},
\]

and the coupled noncentral catalectic obeys

\[
\operatorname{rank}C_{n-m,m}\left(\sum_iT_i\right)
\ge C-\kappa_m-\kappa_{n-m}.
\]

At the center there is an exact extra term

\[
\operatorname{rank}\left(\sum_iA_i\right)
=C-2\rho+\operatorname{rank}(\beta|_{\mathcal R}).
\]

The dimension-only route nevertheless fails.  Two squarefree degree-six Chow
terms sharing four factors form a strict rank-two sum with `rho=4` and zero
pairing correction.  Moreover the two-step cap at `kappa_2=37` is 331 and hence
ambient-vacuous.  G-023 is retained as a structural theorem, not promoted to a
lower-26 program.  Any successor must control the geometry of the radical or a
different quotient module, not only its dimension.

G-024 then falsifies the first naive radical controls.  An explicit six-term
squarefree presentation has `rho=47`, restricted pairing rank 24, and radical
dimension `23>4(6-1)`.  Its raw derivative shadow from fourth-order relations
is all of the 47-dimensional central relation space, not the 23-dimensional
radical.  This does not yet falsify a bound restricted to minimum
decompositions, because the six-term presentation is not proved minimum.  The
next bounded question is therefore whether minimum length itself forces a
radical cap, or whether an example can be certified minimum by an independent
Koszul flattening while violating that cap.

G-025 answers the smallest coordinate test case sharply.  For three distinct
squarefree sextic monomials whose central rank exceeds the two-term cap 40,
minimum length is three and the radical has dimension at most `8=4(3-1)`;
equality occurs for a common-four-factor triple.  Its pure Venn-intersection
proof does not extend to arbitrary Chow factors or to the six fixed terms
needed in the lower-26 program.  It is a positive unit test for a
minimum-length radical principle, not that principle itself.

G-026 isolates the remaining obstruction further.  If the middle
catalecticant itself certifies a sextic decomposition as minimum, the exact
pairing identity forces radical dimension at most nine.  Hence every such
minimum decomposition with at least four terms already satisfies the proposed
`4(q-1)` cap.  A genuine counterexample, or a theorem strong enough for lower
26, must concern minimum length certified by a different coupled invariant;
ordinary middle-rank minimality cannot supply the hard case.

## 10. Falsification and stop rules

Every candidate must first be tested against:

- the six-term common-factor family with scalar homology 465;
- repeated or dependent factors;
- sums whose catalectic images overlap heavily;
- the diagonal-monomial Boolean-slice counterexample; and
- specialization, to ensure every characteristic-zero inequality is used in
  the correct semicontinuity direction.

Suspend a route if it reproduces an existing rank ratio, uses only coordinate
row/column weights, needs a broad state tree before stating a theorem, or
assumes additivity of derivative images or homology.

The active unrestricted interval remains

\[
25\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]
