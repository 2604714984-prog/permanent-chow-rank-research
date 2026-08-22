# N6-127: average/sign finite germs at the (K_{3,2}) collision

**Status.** `EXACT_QQ_AVERAGE_SIGN_GERM_EXCLUSION` in characteristic zero.

N6-126 leaves four same-row average/sign lines in the full first-Schur
weight decomposition.  They are represented by
[
L=M=operatorname{graph}igl(operatorname{diag}(s_0,s_1,s_2)otimes E_{00}igr),
]
with the four sign patterns
[
(1,1,1),quad (1,-1,-1),quad (1,-1,1),quad (1,1,-1).
]
Each finite point has cross rank (6) and sum rank (6).

## 1. Three sign patterns

For the last three patterns, the (360	imes72) first Schur Jacobian has
rank (69).  Its restriction to the (36) difference variables has rank
(36).  The swap (Lleftrightarrow M) fixes the average variables and negates
the difference variables.  Formal uniqueness from the invertible difference
Jacobian therefore forces the completed germ to be diagonal (L=M).  It is
noncomplementary because its sum rank is (6).

## 2. The all-positive pattern

At ((1,1,1)), the average and difference Jacobians have ranks (34) and
(35), respectively, with total rank (69) and a three-dimensional kernel.
After linear elimination the exact quadratic initial ideal is
[
J=(x_1x_2).
]
Both components integrate exactly:

- (x_2=0) is a diagonal branch (L=M), with sum rank (6);
- (x_1=0) is a separating branch, with cross rank (6) but sum rank (9).

The two branch ideals have intersection (J); hence the standard initial
sandwich and complete filtered lifting give the full local germ.  Both
branches are noncomplementary.

Thus all four average/sign fixed lines from N6-126 are excluded from the
complementary rank-six germ.

## 3. Boundary

Together with N6-125, this closes the nonlinear local analysis of the five
same-row fixed lines.  The remaining open layer is still sums of different
torus characters, arbitrary invertible (6	imes6) graph operators, and the
full six-term Chow cocycle.  No claim about ordinary lower (29), exact
(operatorname{ChowRank}(operatorname{perm}_6)), or border rank follows here.

Replay:

~~~text
python scripts/n6_k32_average_sign_germs.py \\
  --verify-json data/n6_k32_average_sign_germs.json
python -m unittest tests.test_n6_k32_average_sign_germs -v
~~~
