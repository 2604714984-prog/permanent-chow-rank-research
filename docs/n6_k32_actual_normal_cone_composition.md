# N6-131: conditional composition at the (K_{3,2}) collision

**Status.** `CONDITIONAL_K32_ACTUAL_NORMAL_CONE_COMPOSITION` in characteristic
zero.  This is a logical composition certificate, not a new elimination.

## What is already closed

N6-126 classifies the torus-fixed individual first-Schur directions in the
full 72-variable graph chart:

\[
24\ \text{row-changing} + 4\cdot 5\ \text{same-row lines}=44.
\]

The 44 lines split into three families relevant to actual Chow pairs:

| family | count | local certificate |
|---|---:|---|
| row-changing anti-diagonal | 24 | N6-123 |
| same-row relative line | 4 | N6-125, with N6-119 removing its relaxed product branch |
| same-row average/sign lines | 16 | N6-127 |

N6-123 makes the complement determinant vanish in the completed local
incidence at every row-changing representative.  N6-125 has two
noncomplementary branches and one relaxed common-(A_3) product branch; the
last branch cannot be a 12-dimensional Chow section difference by N6-119.
N6-127 makes every branch at the four average/sign representatives
noncomplementary.

N6-135 gives a further mixed-weight compression: a rank-at-most-three point
supported on three distinct first-Schur rays with nonzero coefficients and
affinely independent torus characters lies in one of 13 explicit four-ray
rank-three spaces.  N6-136 excludes the straight graph arcs in the 12
row-changing four-ray spaces; the remaining same-row four-ray space is the
N6-125 branch already covered at its finite representative.

## The conditional implication

Assume an actual Chow-pair component through the coordinate (K_{3,2})
collision satisfies the following finite-point realization property:

> an extremal torus degeneration of the component lands at one of the 44
> finite representatives above, and the local branch through that finite point
> is the specialization of the original component.

Then the component cannot be generically complementary.  Its extremal fixed
direction is one of the 24+4+16 lines, while the corresponding completed local
certificate excludes complementarity.  This is the only inference made by
N6-131.

The usual projective-torus observation explains why this is the right missing
interface: a torus-stable irreducible projective normal-cone component has a
torus-fixed point, and N6-126 classifies the fixed first-Schur directions.
What is *not* automatic is that this normal-cone fixed point gives the stated
finite equality representative with a compatible local branch.  N6-116
explicitly leaves precisely this all-order passage open.

## Boundary

N6-131 does not prove the finite-point realization property.  Therefore it does
not yet exclude the full (K_{3,2}) normal cone, nonlinear lifts of the
13 four-ray spaces, affine-degenerate or repeated-weight sums, non-graph
charts, the (K_{2,3}) transpose endpoint, ordinary lower 29, exact
\(\operatorname{ChowRank}(\operatorname{perm}_6)\), or border rank.

Replay:

```text
python scripts/n6_k32_actual_normal_cone_composition.py \\
  --verify-json data/n6_k32_actual_normal_cone_composition.json
python -m unittest tests.test_n6_k32_actual_normal_cone_composition -v
```
