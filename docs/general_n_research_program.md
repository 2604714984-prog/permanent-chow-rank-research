# General-`n` research program

## Status

`ACTIVE`.

The working conjecture is

\[
\operatorname{ChowRank}(\operatorname{perm}_n)=2^{n-1}.
\]

The trusted small-`n` boundary is now:

```text
n=3: exact 4
n=4: exact 8
n=5: repaired internal computer-assisted proof draft for exact 16
n=6: exact ordinary rank 32; two independent scope audits pass
```

The `n=5` v14 proof is canonical on `main`; its role in this program is a
small-`n` structural baseline, not a template for an ever larger state
classification.

## 1. What is already known internally

The repository contains:

- exact derivative dimensions
  \[
  \dim\mathcal D_m(\operatorname{perm}_n)=\binom nm^2;
  \]
- general first-Koszul and border-Koszul lower bounds;
- zero-intersection and multidimensional-shadow refinements;
- parity-sensitive asymptotics;
- a quotient-Koszul gain formula;
- a vector-valued Macaulay prolongation theorem;
- the specialized `n=6` lower bound 25;
- exact full column-sign and row-sign rank `2^(n-1)`;
- exact unrestricted ordinary rank 32 at `n=6`, using symmetric image-span
  and half-defect quotient-symbol inequalities;
- a larger anchored diagonal-sign rigidity theorem; and
- a general count-product atomic-rank theorem for a restricted aggregate.

These results establish the correct exponential scale but do not recover the
factor needed to prove unrestricted rank `2^(n-1)`.

## 2. Scalar derivative profiles are exhausted

Let

\[
h(f)=
\bigl(
\dim\mathcal D_0(f),\ldots,\dim\mathcal D_n(f)
\bigr).
\]

The scalar derivative-profile ceiling theorem proves that every monotone,
positively homogeneous, subadditive rank lower bound which factors only
through `h(f)` is at most

\[
\binom n{\lfloor n/2\rfloor}
\]

on the permanent.

Consequences:

```text
MORE_SCALAR_CATALECTICANT_DEGREES=NO
BLOCK_DIAGONAL_SCALAR_CATALECTICANTS=NO
NONNEGATIVE_WEIGHTED_PROFILE_OPTIMIZATION=NO
RAW_ADJACENT_KERNEL_DIMENSIONS=NO
```

The raw map

\[
V^*\otimes\mathcal D_m(f)
\longrightarrow
\mathcal D_{m-1}(f)
\]

is surjective, so its kernel dimension is itself determined by the scalar
profile. The missing information must lie in higher compatibility, quotient
geometry, or relations among summands.

## 3. The sign construction route is closed

The Boolean diagonal-slice theorem gives

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=
2^{n-1}.
\]

The same lower bound holds when all off-diagonal coefficients are arbitrary,
provided every row-zero anchor is nonzero and each normalized diagonal ratio
is a sign.

Consequences:

```text
UNIFORM_SIGN_SEARCH=CLOSED
ONE_DEFECT_SIGN_SEARCH=CLOSED
TWO_DEFECT_SIGN_SEARCH=CLOSED
FULL_COLUMN_SIGN_SEARCH=CLOSED
ANCHORED_DIAGONAL_SIGN_SEARCH=CLOSED
```

A shorter decomposition, if it exists, must use genuinely complex diagonal
ratios, vanishing anchors, or factors that mix the row-column structure. No
further sign defect hierarchy or full sign dictionary optimizer is authorized.

## 4. Main object: the complete derivative tower

For a degree-`n` form `f`, define

\[
\mathcal M(f)
=
\bigoplus_{m=0}^n\mathcal D_m(f)
\]

with the action of the differential operator ring.

For the permanent, the degree-`m` basis is indexed by pairs of `m`-subsets of
rows and columns. Differentiation deletes a row and a column. Thus
`\mathcal M(perm_n)` is a double-Boolean incidence module.

For an independent Chow term, the basis is indexed by one Boolean lattice of
factor subsets.

A decomposition

\[
\operatorname{perm}_n=T_1+\cdots+T_r
\]

must therefore generate the double-Boolean module from `r` single-Boolean
modules, subject to coupled cancellations.

## 5. North-star invariant

Seek an invariant `Phi` of differential modules satisfying:

\[
\Phi(\mathcal N)\le\Phi(\mathcal M)
\quad\text{for }\mathcal N\subseteq\mathcal M,
\]

\[
\Phi(\mathcal M_1+\mathcal M_2)
\le
\Phi(\mathcal M_1)+\Phi(\mathcal M_2),
\]

and

\[
\Phi(\mathcal M(T))\le1
\]

for every Chow term, including degenerate terms.

The target is

\[
\Phi(\mathcal M(\operatorname{perm}_n))=2^{n-1}.
\]

A weaker but decisive target is the recurrence

\[
\Phi(\mathcal M(\operatorname{perm}_n))
\ge
2\Phi(\mathcal M(\operatorname{perm}_{n-1})).
\]

The invariant must not factor through the scalar Hilbert profile.

### Post-`n=6` middle-layer decision

The exact `n=6` proof yields a reusable image-span and factor-filtration
framework, but its one-middle-layer capacity has now been determined. The
linear route is capacity-feasible only through odd `n=5` and even `n=6`.
At `n=7`, a full-factor quotient has combined symbol capacity 70 while the
slope needed for rank 64 demands 145. The immediate target is therefore a
multi-degree coupled derivative module for `perm_7`, not a rectangular copy
of the `n=6` half-defect inequality.

The complete N7-002 capacity scan sharpens this requirement.  Even allowing
every standard higher-wedge Koszul map and taking the permanent-side rank at
its optimistic dimension maximum gives integer ceiling 61.  Nonnegative
direct sums cannot improve the best component ratio.  The next candidate must
therefore impose compatibility across degrees that strictly lowers the
one-term cap; merely stacking standard flattenings is excluded.

N7-004 through N7-009 show that permanent-specific compatibility can already
improve the ordinary lower bound without a new flattening.  N7-007 recursively
applies the same two-dimensional shadow theorem at degrees two, three, and
four.  The unique optimal nested packet has two terms inside five terms inside
twenty selected terms.  Continuing the same tower through degrees five and
six gives \(C_5(46)=405\) and \(C_6(46)=33\).  The raw complementary
\(C_{6,1}\) catalectic then has residual rank at least \(49-33=16\), forcing
three more terms and proving
\(\operatorname{ChowRank}(\operatorname{perm}_7)\ge49\).  Exact selected-size
scans show that this recursive-shadow plus raw-catalectic route itself stops
at 49.  Further progress therefore needs a genuinely stronger compatibility
constraint or a coupled multi-degree module, rather than another packet-size
optimization in the same tower.

## 6. Main workstream: natural cross-degree maps

The first exact inventory of the existing theorem-bearing candidates is
frozen in `data/general_natural_map_inventory.json` and reproduced by
`scripts/general_natural_map_inventory.py`.  It records permanent rank,
one-term rank or cap, common-factor behavior, and explicit `UNKNOWN` fields
without treating a route ceiling as a Chow-rank theorem.  The inventory does
not promote a candidate; the missing ingredient remains a coordinate-invariant
cross-degree invariant with a uniform degenerate one-term cap and a
subadditivity proof.

The first useful candidates must retain higher compatibility, for example:

- Koszul homology after quotienting universal commutation relations;
- Young or Schur flattenings;
- Fitting ranks of coupled relation modules; or
- natural maps between several derivative degrees.

### NGEN-01 — coordinate-invariance gate

The permanent has a row-column torus, but arbitrary Chow summands do not
respect that torus. A permanent-side weight multiplicity is not automatically
a valid termwise charge.

Before computing a large character table, prove that the candidate is either:

1. a natural `GL(V)`-equivariant map whose rank is coordinate invariant and
   has a uniform one-term cap; or
2. a target-torus functional with an orientation-independent cap over every
   `GL(V)` translate of a Chow term.

### NGEN-02 — exact low-`n` natural-map table

For `n=5,6`, inventory a small list of natural Koszul or Young complexes. For
each candidate, compute:

- exact permanent rank;
- exact generic one-term rank;
- a proved degenerate one-term upper bound; and
- the common-factor adversarial value.

### NGEN-03 — promotion

Promote only a candidate whose rank ratio exceeds the scalar profile ceiling
and survives the adversarial family. Torus weights may diagnose the matrix, but
the theorem-bearing quantity must be coordinate invariant.

The search is diagnostic. Promotion requires a written map, a one-term cap,
and a sum inequality.

## 7. Promotion gates

A candidate route is promoted only if one of the following occurs:

```text
perm_6 certified lower bound >= 26
or
uniform doubling recurrence obtained
or
asymptotic lower bound improves the central-binomial scale by an unbounded factor
```

A candidate is rejected if:

- it reduces to a nonnegative weighted scalar profile;
- it is defeated by a common-factor family;
- it assumes a coupled image equals a literal sum;
- its degenerate one-term cap is unproved;
- a finite-field equality carries a characteristic-zero claim;
- test data participate in selecting and certifying the same formula without a
  fresh split; or
- the finite interface requires a large workflow before the mathematical
  invariant is stated.

## 8. Parallel falsification thread

The conjecture remains unproved. Maintain one small construction thread at
`n=6`, but exclude the sign and anchored diagonal-sign families already closed
by the exact theorem.

Authorized ansatzes must be genuinely different, for example:

- symmetry-reduced complex diagonal ratios outside `{+1,-1}`;
- a small number of row-column orbit types with exact complex parameters;
- block-recursive factors that mix several rows or columns; or
- candidates suggested by numerical homotopy and then reconstructed exactly.

Evidence boundary:

```text
numerical solution=candidate only
finite-field solution=diagnostic only
exact algebraic reconstruction=required
symbolic coefficient verification=required
search failure=no lower-bound evidence
```

Do not enumerate the full unrestricted parameter space and do not build a
generic solver framework without a compact ansatz.

## 9. Border-rank gate

Before making secant-variety equations a mainline strategy, determine whether

\[
\underline{\operatorname{ChowRank}}(\operatorname{perm}_4)
\]

is 7 or 8.

If it is 7, a closed secant obstruction cannot reproduce the ordinary rank-8
theorem and ordinary-rank-specific valuative structure is necessary.

If it is 8, representation-theoretic equations for secant Chow varieties
remain plausible.

This is a distinct gate, not a prerequisite for NGEN-01.

## 10. Hidden assumptions

1. The conjectural exact value is true.
2. Cross-degree relation data retain the missing factor.
3. A useful invariant can be made subadditive under coupled sums.
4. Low-`n` natural-map patterns stabilize sufficiently to suggest a formula.

### Assume all are false

Then the correct outcome is a barrier theorem plus an exact shorter
decomposition, not additional process. The program should pivot to
construction and ordinary-versus-border separation.

## 11. Strongest objection

Syzygy and representation data may still be only a repackaging of partial
derivatives, and subadditivity may fail under cancellation. This objection is
decisive: no character table is a result by itself. The first theorem-bearing
deliverable must prove the one-term cap and the sum inequality.

## 12. Minimal implementation plan

```text
one combinatorial generator
one exact comparison format
one independent verifier
no database
no manager
no dispatcher
no registry
```

The first implementation should cover `n=5,6` in memory and write immutable
JSON summaries. Native acceleration is not authorized until a measured
bottleneck exists.

## 13. Immediate next task

Create a compact inventory of the `GL(V)`-natural maps already implicit in the
repository:

1. first Koszul flattening;
2. first higher-wedge Koszul flattening;
3. second-Koszul homology;
4. vector-valued first prolongation; and
5. one small Young flattening candidate from the literature interface.

For `n=5,6`, record for each map:

```text
permanent rank
generic one-term rank
proved degenerate one-term cap
integer rank-ratio lower bound
common-factor adversarial result
profile-determined or genuinely cross-degree
```

This is a ceiling comparison, not a new framework. Select at most one map for
further development, and only if its `n=6` ceiling can exceed 25 or its
structure suggests a uniform recurrence.
