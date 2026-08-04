# The unique three-relation frontier at `b=24`

## Status

`ROUTE_DIAGNOSTIC` with exact integer replay. This note does not exclude `b=24` and does not prove `ChowRank(perm_6)>=24`.

## 1. Current fixed-four boundary

The proved fixed-four exclusion chain removes the layers

\[
b=27,
\qquad
b=26,
\qquad
b=25.
\]

Under a hypothetical 23-term decomposition, the current range is

\[
20\le b\le24.
\]

At the top remaining layer, the quadratic shadow is exactly

\[
\dim\left(
\mathcal D_2(\operatorname{perm}_6)
\cap
\sum_{i=1}^4\mathcal D_2(T_i)
\right)
=45.
\tag{1.1}
\]

If it were at least 46, the already-proved `b=25` direct/one-/two-relation analysis would give a central-rank contradiction.

## 2. Defect inequalities

Put

\[
\varepsilon_i
=15-\dim\mathcal D_2(T_i),
\]

\[
\alpha_i
=3-\dim\left(
\mathcal D_2(\operatorname{perm}_6)
\cap
\mathcal D_2(T_i)
\right).
\]

The four omitted-factor projections give

\[
\boxed{
\sum_{i\ne j}\varepsilon_i+\alpha_j\le3
\qquad(j=1,2,3,4).
}
\tag{2.1}

For one labelled pattern, let

\[
r_i=15-\varepsilon_i,
\qquad
q_i=12-\varepsilon_i+\alpha_i.
\]

Since the total quadratic shadow is 45, the quadratic relation-kernel dimension satisfies

\[
\kappa
\le
\sum_ir_i-45-\max_iq_i.
\tag{2.2}

## 3. Exact exhaustive table

The standard-library generator enumerates every nonnegative labelled solution of (2.1). It finds

\[
\boxed{1153}
\]

patterns, partitioned by the cap (2.2) as

```text
relation-kernel cap 0: 940
relation-kernel cap 1: 189
relation-kernel cap 2:  23
relation-kernel cap 3:   1
```

The degree-six Chow-term profile proved in the preceding layers shows that quadratic derivative dimension 12 is impossible. Exactly 16 patterns require such a dimension. Removing them leaves

\[
\boxed{1137}
\]

profile-realizable patterns:

```text
relation-kernel cap 0: 924
relation-kernel cap 1: 189
relation-kernel cap 2:  23
relation-kernel cap 3:   1
```

The 23 cap-two patterns have only two epsilon types:

```text
(0,0,0,0): 15 patterns
(0,0,0,1):  8 patterns
```

## 4. The unique cap-three pattern

The unique pattern with relation-kernel cap three is

\[
\boxed{
\varepsilon_1=\cdots=\varepsilon_4=0,
\qquad
\alpha_1=\cdots=\alpha_4=0.
}
\tag{4.1}

Thus all four fixed terms satisfy

\[
\dim\mathcal D_2(T_i)=15,
\]

\[
\dim\left(
\mathcal D_2(\operatorname{perm}_6)
\cap
\mathcal D_2(T_i)
\right)=3,
\]

and each quotient image has dimension 12.

The extremal six-plane theorem therefore applies to every factor span: up to transpose, each is a disjoint-support `2 x 3` tensor-product plane.

## 5. Why the existing coupling firewall stops here

A quadratic relation kernel of dimension zero makes the central derivative spaces direct. Dimension one forces every cubic relation component to be a pure cube; dimension two forces every component to be a binary cubic. Those cases are excluded by the degree-six term profiles and the squarefree-binary obstruction.

For dimension three, a relation component may be a ternary squarefree cubic. For example, a product of three independent factor variables is already such a cubic. Therefore the one-/two-relation argument cannot be extended by replacing “binary” with “ternary.”

This is the precise remaining obstruction, not merely a larger version of the previous integer table.

## 6. Next proof target

The next minimal target is to analyze the unique pattern (4.1) using the explicit extremal geometry:

1. put the four factor spans into the classified `2 x 3` / `3 x 2` support components;
2. classify three-dimensional quadratic relation kernels among their 15-dimensional derivative spaces;
3. impose integrability on the induced ternary cubic relation components;
4. bound the coupled middle-catalectic rank or the relative prolongation on the surviving relation types.

No broad SAT, Hilbert-scheme, or workflow layer is justified before this single equality pattern is reduced algebraically.

## 7. Reproduction

Run

```bash
python scripts/n6_b24_three_relation_frontier.py
python -m unittest tests.test_n6_b24_three_relation_frontier -v
```

Expected output includes

```text
all_labelled_pattern_count=1153
profile_realizable_pattern_count=1137
relation_kernel_caps=924/189/23/1
unique_three_relation_pattern=all_zero_defects
N6_B24_THREE_RELATION_FRONTIER_PASS
```
