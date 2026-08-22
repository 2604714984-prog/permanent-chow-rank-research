# Program TI — target-integrability complex

## Executable correction to TI-02 and TI-03

The seven target sextics are already the gradient of the squarefree septic.
Consequently, once `C E6=S6` holds, equality of mixed partials automatically
puts the wedge-coordinate vectors in `R5`.  The map to
`(k^42/R5) tensor Lambda^2(k^7)` proposed in the first version of this file is
therefore identically zero on the complete coefficient-solution space; it is
not an additional rank obstruction.

The useful gauge-invariant datum is instead the class

`[Psi_A(C)] in coker(d_A: R6 tensor k^7 -> R5 tensor Lambda^2(k^7))`,

where `d_A(U)_(jk)=u_j star a_k-u_k star a_j`.  A fixed span of coefficient
bivectors is not gauge invariant when `R6` is nonzero.  All tasks below are
to be read with this correction.  In particular, arbitrary target-basis
changes are allowed only together with the corresponding variable/gradient
change.

## Goal

Replace the coarse consequence `H_Z(5)<=40` by the full linear compatibility
system for the permanent sextic gradient. The first priority is to decide
whole relation-defect classes `q5=2`, `q5=3`, and `q5=4`, not individual
sampled point families.

## TI-01 — coefficient solution space

Let `A` be the `42 x 7` point matrix and `S_6` the seven permanent sextic
target rows. Define

\[
\mathcal S_6(A)=\{C:\;CE_6=S_6\}.
\]

Prove, with orientations fixed once and for all:

- `T_6 subset W_6` iff `mathcal S_6(A)` is nonempty;
- two coefficient representations differ by seven rows from `R_6`;
- point rescaling, target-basis changes, and permutation of the 42 points act
  equivariantly.

**Output:** a basis-independent exact sequence and deterministic constructor.

## TI-02 — automatic mixed-partial relation tensor

For the `i`-th columns `c_i` of `C` and `a_i` of `A`, define

\[
\Phi_A(C)_i=c_i\wedge a_i\in\Lambda^2 k^7.
\]

Differentiate `C E6=S6` and prove that every coordinate coefficient vector of
`Phi_A(C)` belongs to `R_5`. Equivalently, the map

\[
\overline\Phi_A:\mathcal S_6(A)\to
(k^{42}/R_5)\otimes\Lambda^2 k^7.
\]

vanishes identically on `mathcal S_6(A)`.  This is a structural relation
tensor, not an independent target-containment obstruction.

**Output:** exact automatic-compatibility theorem and regressions to the
already established zero- and one-relation arguments.

## TI-03 — quotient the `R6` gauge correctly

Do not choose a preferred coefficient representation.  Under translation by
`U in R6 tensor k^7`, the relation tensor changes by `d_A(U)`.  Freeze the
class of `Psi_A(C)` in `coker(d_A)` and prove that it is independent of the
chosen solution `C`.

For every possible `(q5,q6)` in `F1` through `F5`, record source, gauge,
target, and cokernel dimensions.  Do not claim a new existence condition from
the identically zero quotient in TI-02.

## TI-04 — permanent torus blocks

Decompose `overline Phi_A` by row/column weights of the permanent target.
Determine the smallest set of independent blocks whose simultaneous vanishing
is equivalent to the complete mixed-partial system.

A large matrix is not retained when symmetry supplies exact smaller blocks.

## TI-05 — minimal-support compatibility

For an inclusion-minimal subset of sixth powers spanning all seven targets,
prove the exact relation among:

- support cardinality;
- independence of sixth powers;
- `q5` and `q6`;
- repeated points or zero coefficient rows;
- removable summands;
- the lower-49 minimality hypothesis.

## TI-06 — relation-coordinate map

Choose a basis `rho^(1),...,rho^(q5)` of `R_5` and associate

\[
u_i=[\rho_i^{(1)}:\cdots:\rho_i^{(q5)}]\in P^{q5-1}
\]

to every nonzero relation column. Prove basis-change invariance and track zero
columns as a separate support stratum.

## TI-07 — Grassmannian incidence

Write

\[
c_i\wedge a_i=
\sum_{\alpha=1}^{q5}\rho_i^{(\alpha)}\beta_\alpha
\]

and set `B=span(beta_1,...,beta_q5)`. Reformulate integrability as an
incidence between the relation-coordinate points and

\[
P(B)\cap\operatorname{Gr}(2,7)\subset P(\Lambda^2k^7).
\]

Separate zero, decomposable, and higher alternating-rank values.

## TI-08 — the `q5=2` pencil theorem

For `F1` and `F3`, classify only the pencil types actually compatible with
TI-07:

- a line not contained in the Grassmannian;
- a line contained in the Grassmannian;
- one- or two-point intersection;
- common-kernel and degeneration boundaries.

Use the number of distinct relation-coordinate ratios to derive one of:

1. a support partition of the 42 points;
2. a common-factor description;
3. an exact target-integrability contradiction;
4. a finite exact survivor family.

**Gate:** this task must decide the entire `q5=2` class or reduce it to a
proved finite list.

## TI-09 — sparse-ratio partitions

When the `q5=2` relation-coordinate map takes at most two nonzero projective
values, derive the induced partition of fifth-power relations and evaluation
codes. Compute consequences for strict Hilbert growth, degree-six target span,
point distinctness, and weighted coupling.

## TI-10 — Grassmannian-line replacement

Classify a line of decomposable bivectors by its flag data. Prove the sharp
replacement cost for the supported compatible gradient and compare it with
the support cardinality. The desired contradiction is with

\[
\operatorname{WaringRank}(x_0\cdots x_6)=64.
\]

## TI-11 — the `q5=3` net theorem

For `F2` and `F5`, analyze the plane `P(B)`:

- planes contained in `Gr(2,7)`;
- line or conic components;
- finite intersection;
- common-kernel and common-three-space types;
- zero relation columns;
- flat degeneration boundaries.

Use the 42 indexed relation columns. Return a finite type list or a stronger
invariant that avoids full plane classification.

## TI-12 — `q5=3` replacement/target theorem

For every surviving net type, derive a replacement bound or direct permanent
target contradiction. Reuse the same proof for `F2` and `F5` where only the
`R_6` gauge changes, and state exactly where that change matters.

## TI-13 — the `q5=4` web theorem

For `F4`, restrict the Plucker quadrics to `P(B)=P^3`. Prioritize:

- common-kernel strata;
- low-rank Pfaffian loci;
- positive-dimensional Grassmannian intersections;
- relation-coordinate images on curves or surfaces;
- exact support partitions.

Do not classify all four-dimensional subspaces of `Lambda^2 k^7` unless the
endpoint equations force it.

## TI-14 — universal replacement inequality

Seek one inequality

\[
\text{replacement cost}\le
|\operatorname{supp}(R_5)|-\varepsilon
\]

valid for every nontrivial `q5=2,3,4` compatibility type. Test it against
exact compatible gradients in fewer variables.

## TI-15 — target-only decision

Return exactly one:

```text
TARGET-INTEGRABILITY-CLOSED
```

or

```text
TARGET-INTEGRABILITY-SURVIVORS:
a finite theorem-defined list of exact compatibility components.
```

A class closed here requires no weighted-coupling computation.
