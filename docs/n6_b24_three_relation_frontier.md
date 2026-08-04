# The historical three-relation diagnostic at `b=24`

## Status

`SUPERSEDED_ROUTE_DIAGNOSTIC`, with exact integer replay.

The defect table and the unique cap-three pattern below remain valid. They
no longer describe an open proof boundary: the componentwise Macaulay
argument in

```text
docs/n6_component_prolongation_exclusion.md
```

bounds the full cubic relation kernel and excludes the entire `b=24` layer.
The current in-repository conclusion is

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

## 1. Historical fixed-four boundary

Before the component-prolongation theorem, the proved fixed-four exclusion
chain had removed

\[
b=27,
\qquad
b=26,
\qquad
b=25,
\]

and left the range

\[
20\le b\le24
\]

under a hypothetical 23-term decomposition.

At the top layer, the quadratic shadow is exactly

\[
\dim\left(
\mathcal D_2(\operatorname{perm}_6)
\cap
\sum_{i=1}^4\mathcal D_2(T_i)
\right)
=45.
\tag{1.1}
\]

If it were at least 46, the already-proved `b=25` analysis would give a
central-rank contradiction.

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
\]

For one labelled pattern, let

\[
r_i=15-\varepsilon_i,
\qquad
q_i=12-\varepsilon_i+\alpha_i.
\]

The dimension-only quadratic relation-kernel cap is

\[
\kappa
\le
\sum_ir_i-45-\max_iq_i.
\tag{2.2}
\]

## 3. Exact exhaustive table

The standard-library generator enumerates every nonnegative labelled
solution of (2.1). It finds

\[
\boxed{1153}
\]

patterns:

```text
relation-kernel cap 0: 940
relation-kernel cap 1: 189
relation-kernel cap 2:  23
relation-kernel cap 3:   1
```

Quadratic derivative dimension 12 is impossible for a degree-six Chow term.
Exactly 16 patterns require that profile. Removing them leaves

\[
\boxed{1137}
\]

profile-feasible patterns:

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

The unique pattern with quadratic relation-kernel cap three is

\[
\boxed{
\varepsilon_1=\cdots=\varepsilon_4=0,
\qquad
\alpha_1=\cdots=\alpha_4=0.
}
\tag{4.1}
\]

Thus all four terms have 15-dimensional quadratic derivative spaces,
three-dimensional permanent intersections, and 12-dimensional quotient
images. The extremal six-plane theorem applies to all four factor spans.

## 5. Why the former firewall stopped here

A zero-dimensional quadratic relation kernel makes the central derivative
spaces direct. Dimension one forces pure-cube relation components, while
dimension two forces binary cubic components. The previously proved term
profiles exclude those possibilities.

Dimension three can support a ternary squarefree cubic, so that component
classification could not be extended mechanically. This was a genuine
failure of the old proof route.

## 6. How the layer is now excluded

The superseding theorem does not classify ternary cubic components. If the
quadratic relation kernel has dimension `kappa`, each scalar component of a
cubic relation lies in the first prolongation of a quadratic space of
dimension at most `kappa`. Macaulay growth gives

\[
\dim P^{(1)}\le\kappa^{\langle2\rangle}.
\]

For four components, the entire cubic relation kernel has dimension at most

\[
3\kappa^{\langle2\rangle}.
\]

At `b=24`, one has `kappa<=3` and

\[
3^{\langle2\rangle}=4.
\]

The resulting cubic relation cap is 12. The block-Sylvester inequality then
gives

\[
\dim\mathcal D_3(R)
\ge
4\cdot20-2\cdot12
=56.
\]

The nineteen-term residual inequality gives instead

\[
\dim\mathcal D_3(R)\le2b-20=28.
\]

Hence `b=24` is impossible.

## 7. Claim boundary

The exact table in this note is still useful as an independent arithmetic
replay, but it is no longer a theorem boundary. The superseding result
proves only

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge24.
\]

It does not prove a lower bound of 25, a border-rank lower bound of 24, or
the conjectural exact value 32.

## 8. Reproduction

Run

```bash
python scripts/n6_b24_three_relation_frontier.py
python -m unittest tests.test_n6_b24_three_relation_frontier -v
python scripts/n6_component_prolongation_exclusion.py
python -m unittest tests.test_n6_component_prolongation_exclusion -v
```
