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
n=6: 25 <= ChowRank(perm_6) <= 32
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
- exact rigidity in several sign subfamilies; and
- a general count-product atomic-rank theorem for a restricted aggregate.

These results establish the correct exponential scale but do not recover the
factor needed to reach `2^(n-1)`.

## 2. New barrier: scalar derivative profiles are exhausted

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
```

The missing information must lie in maps between the derivative spaces or in
relations among summands.

## 3. Main object: the complete derivative tower

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

## 4. North-star invariant

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

A weaker but still decisive target is the recurrence

\[
\Phi(\mathcal M(\operatorname{perm}_n))
\ge
2\Phi(\mathcal M(\operatorname{perm}_{n-1})).
\]

The invariant must not factor through the scalar Hilbert profile, by the new
ceiling theorem.

## 5. First workstream: multigraded adjacent-degree relations

The smallest useful structure beyond dimensions is the family of kernels and
cokernels of

\[
V^*\otimes\mathcal D_m(f)
\longrightarrow
\mathcal D_{m-1}(f).
\]

Retain the row-column torus grading and, where practical, the
`S_n x S_n` character.

### NGEN-01 — exact low-`n` character tables

For `n=3,...,8`:

1. construct the adjacent-degree incidence maps directly from subset
   combinatorics;
2. compute exact torus-weight multiplicities of kernels and cokernels;
3. aggregate to symmetric-group character data only after the torus table is
   independently replayed;
4. bind every table to the exact definition and code hash.

### NGEN-02 — one-term formula

Derive the same objects for an independent Chow term analytically. Degenerate
terms require a proved specialization bound; generic calculations alone are
insufficient.

### NGEN-03 — functional search

Search for a nonnegative functional on the multigraded relation data that:

- is bounded by one on every Chow term;
- is monotone under submodules;
- is subadditive under coupled sums; and
- exceeds the scalar profile ceiling on the permanent.

The search is diagnostic. Promotion requires a written invariant and proof.

## 6. Promotion gates

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

## 7. Parallel falsification thread

The conjecture itself remains unproved. Maintain one small construction thread
at `n=6`:

- test only symmetry-reduced complex-coefficient ansatzes;
- treat numerical solutions as candidates;
- require exact algebraic reconstruction and symbolic verification before
  recording an upper bound;
- treat search failure as no lower-bound evidence.

Do not enumerate the full unrestricted parameter space and do not build a
generic solver framework without a compact ansatz.

## 8. Border-rank gate

Before making secant-variety equations a mainline strategy, determine whether

\[
\underline{\operatorname{ChowRank}}(\operatorname{perm}_4)
\]

is 7 or 8.

If it is 7, a closed secant obstruction cannot reproduce the ordinary rank-8
theorem and ordinary-rank-specific valuative structure is necessary.

If it is 8, representation-theoretic equations for secant Chow varieties
remain a plausible general route.

This is a distinct gate, not a prerequisite for NGEN-01.

## 9. Hidden assumptions

1. The conjectural exact value is true.
2. Cross-degree relation data retain the missing factor.
3. A useful invariant can be made subadditive under coupled sums.
4. Low-`n` character patterns stabilize sufficiently to suggest a formula.

### Assume all are false

Then the correct outcome is a barrier theorem plus an exact shorter
decomposition, not additional process. The program should pivot to
construction and ordinary-versus-border separation.

## 10. Strongest objection

Syzygy and representation data may still be only a repackaging of partial
derivatives, and subadditivity may fail under cancellation. This objection is
decisive: no character table is a result by itself. The first theorem-bearing
deliverable must prove the one-term cap and the sum inequality.

## 11. Minimal implementation plan

```text
one combinatorial generator
one exact character-table format
one independent verifier
no database
no manager
no dispatcher
no registry
```

The first implementation should cover `n<=8` in memory and write immutable
JSON summaries. Native acceleration is not authorized until a measured
bottleneck exists.

## 12. Immediate next task

Implement NGEN-01 only for the central adjacent-degree map at `n=5,6`:

\[
V^*\otimes\mathcal D_{\lceil n/2\rceil}(f)
\longrightarrow
\mathcal D_{\lceil n/2\rceil-1}(f).
\]

Record the torus-weight kernel multiplicities for:

1. `perm_n`;
2. one independent Chow term; and
3. the common-factor adversarial family already used against scalar homology.

Stop after this comparison. Extend to all degrees only if a permanent-specific
weight class survives both one-term and common-factor falsification.
