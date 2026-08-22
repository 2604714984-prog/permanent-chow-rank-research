# Program A — all-rank-seven Packet A

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

Construct the larger middle-degree system only for an exact component that
passes the complete `2/5/6` interface.

## A-14 — decision

Return exactly `A-CLOSED` or an exact `A-SURVIVOR`.
