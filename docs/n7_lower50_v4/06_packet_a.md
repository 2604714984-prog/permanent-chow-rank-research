# Program A — all-rank-seven Packet A

## Current execution state

A-01 through A-06 now have exact labelled operator, aggregate-kernel,
inverse-coefficient transport, permanent-target, forced-gradient, and
forced-Hessian interfaces.  The completed same-row witness matrix gives two
branches.  Its zero branch is empty in characteristic zero: the structure
theorem makes every term row-separated, while the resulting 49-term tensor
decomposition contradicts the ordinary tensor-rank lower bound
`R(perm_7) >= 55`.  See
`docs/n7_packet_a_wzero_tensor_rank_closure.md`.

The extreme `K2=0` branch is also empty.  Endpoint dimensions would force the
aggregate degree-five space to equal the 441-dimensional permanent derivative
space; all five-factor subproducts would then be row- and column-multilinear,
forcing every term to be one permutation monomial.  Forty-nine such monomials
cannot equal the 5040-term permanent.  See
`docs/n7_packet_a_k2zero_exclusion.md`.

This is not `A-CLOSED`.  The exact active component now has
`W^all != 0`, `K2 != 0`, and `K5 != 0`.  The Hessian subspace is automatically
orthogonal to `K2`, and target containment plus endpoint dimensions make the
entire `2/5` apolar induction map automatically surjective.  Thus the plain
`2/5` interface is exhausted rather than obstructed; see
`docs/n7_packet_a_25_route_exhaustion.md`.

The transverse obstruction is now canonically the cokernel of the quadratic
apolar induction map

\[
 \Phi=P^{\mathsf T}D A_2^{\mathsf T}:F_2^\perp\longrightarrow K_5.
\]

Here `dim F2^perp=784`, with explicit row-internal, column-internal, and
rectangle-difference summands of dimensions 196, 147, and 441.  Target
containment forces `ker Phi=ker A2^T`, of dimension
`196+dim K2`; at endpoint its rank is exactly `dim K5`.  The previously
proposed opposite array bound is withdrawn.  A-13 must add information beyond
the plain complementary `3/4` Sylvester inclusion, since that unrefined
inclusion is subject to the same rank-factorization tautology.

## Schema/control smoke

`docs/n7_packet_a_labelled_256_operator.md` freezes the `(term,I)` labels,
the complementary `2/5` inverse-coefficient convention, and the three
mandatory controls. It is deliberately not an A-01--A-05 completion: general
factor-plane matrices, transport maps, aggregate kernels, and the general
permanent target operator remain to be constructed.

## Goal

Decide the 49 rank-seven terms whose factor planes form the forced simple
rank-seven multilinear matroid.

## A-01 — minimal labelled module

For every term retain

\[
D_2(T_i),\qquad D_5(T_i),\qquad D_6(T_i)
\]

and every multiplication/differentiation map used by endpoint equality.

## A-02 — exact one-term formulas

Write the labelled matrices in factor or Plucker coordinates. Record
polynomial degree and basis-change actions.

## A-03 — aggregate relation spaces

Construct kernels of labelled direct sums mapping to aggregate degree-2,
degree-5, and degree-6 spaces. Do not erase term labels.

## A-04 — complementary `2/5` equality

Derive the exact relation pairing, radicals, and kernel-image condition.

## A-05 — degree-six target operator

Construct the permanent-specific target quotient and split it by row/column
torus weights.

## A-06 — couple `2/5` and degree six

The same factor planes and coefficients must solve both systems. Build one
incidence scheme rather than optimizing separately.

## A-07 — actual coupled capacity

Compute permanent demand and sharp one-term cap after compatibility equations
are imposed. Uncoupled component ratios are rejected.

## A-08 — matroid equations

Translate pairwise transversality and total span 49 into Plucker/rank
conditions on the labelled module.

## A-09 — smallest obstruction block

Identify the lowest-dimensional torus block in which the permanent demand is
not automatic for a simple 49-plane packet.

## A-10 — mandatory controls

Test every lemma against:

1. the exact 49-term Glynn truncation;
2. the non-tensor Sylvester-equality counterexample;
3. the full 64-term Glynn identity as a positive control.

## A-11 — strict subfamilies

Tensor-split, row-sign, row-uniform, or column-uniform closure counts only as a
lemma unless endpoint equations force every packet into that family.

## A-12 — non-tensor theorem

Use the labelled `2/5/6` module to prove a permanent-specific defect or a
finite classification of non-tensor components.

## A-13 — conditional `3/4` escalation

The plain larger middle-degree system has been audited and is automatic at
endpoint equality: `dim M3=dim M4=1715`, the target rank is 1225,
`k3+k4=490`, and cubic apolar induction has rank exactly `k4`.  See
`docs/n7_packet_a_34_plain_route_exhaustion.md`.  Any continued A-13 work must
therefore add a Koszul/recursive-Koszul wedge, Plucker, cross-weight, or other
representation component not determined by the ordinary catalectic
factorization.  Rechecking the plain `3/4` kernel-image inclusion is stopped.

## A-14 — decision

Return exactly `A-CLOSED` or an exact `A-SURVIVOR`.
