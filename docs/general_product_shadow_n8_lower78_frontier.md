# The exact product-shadow frontier for an ordinary `perm_8` lower bound of 78

## Status and scope

`EXACT_ROUTE_FRONTIER`, `COMPUTATION_REPLAYED`,
`NO_LOWER_78_CLAIM`.

The exact product-shadow theorem proves

\[
\operatorname{ChowRank}(\operatorname{perm}_8)\ge77.
\]

This note asks whether the same scalar interface, optimized over every
standard first-Koszul output degree and every legal fixed-term count, already
excludes a hypothetical `77`-term decomposition.  The answer is no.  The
complete finite scan selects one strict next frontier:

\[
\boxed{m=4,\quad q=17,\quad b\le725,\quad
\text{missing rank gain}=1377.}
\]

Here `q` is the number of fixed terms and

\[
b=\dim\bigl(\mathcal D_4(\operatorname{perm}_8)
\cap\mathcal D_4(R)\bigr).
\]

The number `1377` is the smallest additional integer rank gain that would
contradict the residual capacity.  This is a route selection, not an ordinary
lower bound of 78 and not a border-rank claim.

## 1. Exact scalar interface

For output degree `m` and complementary degree `r=8-m`, put

\[
A_{8,m}
=64\binom8m^2-\binom8{m+1}^2,
\]

\[
B_{8,m}
=64\binom8m-\binom8{m+1}.
\]

Fix `q` Chow terms and let `R` be their sum.  The exact product-shadow cap is

\[
\beta_{8,r}(q)
=
\max\left\{
 b:F_{8,r}(b)\le q\binom8{r-1}
\right\}.
\]

The existing complementary-intersection theorem then gives

\[
\operatorname{rank}K_m(\operatorname{perm}_8-R)
\ge
A_{8,m}-64\beta_{8,r}(q).
\tag{1.1}
\]

For a hypothetical total of 77 terms, the residual capacity is

\[
(77-q)B_{8,m}.
\tag{1.2}
\]

Define the remaining scalar deficit

\[
\Delta_{m,q}
=(77-q)B_{8,m}
-\left(A_{8,m}-64\beta_{8,r}(q)\right).
\tag{1.3}
\]

A scalar contradiction would require `Delta_(m,q)<0`.  If
`Delta_(m,q)>=0`, an additional quotient, relation or realizability theorem
must supply at least

\[
\Delta_{m,q}+1
\]

integer rank dimensions.

## 2. Complete scan boundary

The replay checks every

\[
2\le m\le6
\]

and every fixed count allowed by the globally optimized first-Koszul lower
bound `71`.  Counts for which the derivative threshold reaches the full
complementary layer or the residual numerator is nonpositive are retained as
vacuous and cannot improve the bound.

The maximum exact-shadow lower bound is 77.  It is attained only at the
central output degree `m=4`, for

\[
q\in\{14,15,16,17,18,19\}.
\]

The complete active table is:

| fixed `q` | derivative threshold | exact cap `b` | `F(b)` | `F(b+1)` | residual rank lower bound | residual term count | deficit to a 77-term contradiction |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 | 784 | 560 | 784 | 793 | 274,624 | 63 | 4,088 |
| 15 | 840 | 605 | 840 | 844 | 271,744 | 62 | 2,544 |
| 16 | 896 | 659 | 894 | 897 | 268,288 | 61 | 1,576 |
| **17** | **952** | **725** | **950** | **956** | **264,064** | **60** | **1,376** |
| 18 | 1,008 | 826 | 1,008 | 1,012 | 257,600 | 59 | 3,416 |
| 19 | 1,064 | 900 | 1,060 | 1,066 | 252,864 | 58 | 3,728 |

At `q=17`,

\[
A_{8,4}=310,464,
\qquad
B_{8,4}=4,424,
\]

and

\[
310,464-64\cdot725=264,064.
\]

Sixty residual terms have capacity

\[
60\cdot4,424=265,440.
\]

Thus the scalar gap is

\[
265,440-264,064=1,376.
\]

Any successful continuation at this frontier must therefore prove one of:

1. an additional quotient-Koszul or coupled rank gain of at least `1,377`;
2. an improved realizable intersection cap
   \[
   b\le703,
   \]
   since reducing `b` by twenty-two adds `22*64=1,408` dimensions;
3. a structural theorem excluding every equality/near-equality family before
   the scalar rank comparison.

## 3. Exact Ferrers minimizers at the selected cap

The exact dynamic program gives

\[
F_{8,4}(725)=950
\]

with exactly four Ferrers minimizers.  They form two conjugate pairs:

\[
(15^{45},5^{10},0^{15})
\longleftrightarrow
(55^5,45^{10},0^{55}),
\tag{3.1}
\]

and

\[
(35^5,25^{10},15^{20},0^{35})
\longleftrightarrow
(35^{15},15^{10},5^{10},0^{35}).
\tag{3.2}
\]

At the first excluded size,

\[
F_{8,4}(726)=956,
\]

there are again exactly four minimizers, obtained from the displayed cap
profiles by the corresponding one-cell increments:

\[
(15^{45},6,5^9,0^{15}),
\]

\[
(35^5,26,25^9,15^{20},0^{35}),
\]

and their conjugates.

The count-four certificate plus the four distinct displayed partitions makes
these lists complete inside the Ferrers class.

## 4. Why this frontier is preferable to `q=14`

The `q=14` endpoint has now been classified at the coordinate level by the
single flag orbit in

```text
docs/general_product_shadow_n8_coordinate_equality.md
```

but its residual rank deficit is `4,088`.  The selected `q=17` frontier needs
only `1,377` additional dimensions.  It has four compressed profiles rather
than two, but the numerical gain requirement is smaller by a factor of almost
three.

The research decision is therefore:

```text
primary lower-78 frontier = q17 / b725 / gain1377
q14 flag orbit            = retained structural laboratory
other q and output degrees = scalar-dominated
```

The `q=14` classification remains useful for developing noncoordinate
methods, but it is not the numerically shortest path to lower 78.

## 5. Exact replay

The standard-library script

```text
scripts/general_product_shadow_n8_lower78_frontier.py
```

reconstructs the exact product-shadow dynamic program at every complementary
degree, scans every allowed fixed count, verifies that no scalar choice yields
78, reproduces the six-row active table, and verifies the four selected
Ferrers minimizers and their conjugates.

The frozen payload is

```text
data/general_product_shadow_n8_lower78_frontier.json
```

and the focused regression is

```text
tests/test_general_product_shadow_n8_lower78_frontier.py
```

## 6. Claim boundary

```text
exact_scalar_maximum=77
selected_output_degree=4
selected_fixed_count=17
selected_intersection_cap=725
selected_scalar_deficit=1376
required_additional_integer_gain=1377
Ferrers_cap_minimizers=4
ordinary_lower_78=NOT_PROVED
border_lower_78=NOT_PROVED
noncoordinate_equality_classification=OPEN
Chow_realizability=OPEN
```
