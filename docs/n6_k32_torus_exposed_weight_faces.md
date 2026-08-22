# N6-139: exposed torus weight faces at the (K_{3,2}) collision

This is an exact integer character-polytope certificate for the full graph
chart at (L=M=A_3otimes P_2).  A graph variable has character

\[
  (\text{target row}-\text{source row})
  + (\text{target column}-\text{source column}).
\]

There are 28 distinct first-Schur characters: 24 row-changing characters and
4 same-row characters.  Every row-changing character has an explicit integral
one-parameter-subgroup witness with target row and target complementary column
at (+1), source row and source support column at (-1), and all other weights
zero.  Its score is 4, while every other character has score at most 3.

No same-row character is exposed.  If the row potentials are not all equal,
some ordered row difference is positive and the row-changing character with
the same column difference is larger.  If the row potentials are all equal,
that row-changing character ties the same-row character.  This is an exact
argument over the integer character lattice, not a numerical LP result.

The consequence is deliberately narrow: an exposed-face torus reduction can
isolate only the 24 row-changing directions, which are already covered by the
single-cross certificates.  It cannot isolate the four average/sign same-row
directions.  Those four individual finite germs are already excluded by
N6-125 and N6-127.  Character exposure also does not imply that a tangent
direction integrates to a finite actual Chow pair, so mixed-character sums and
the finite-point realization gap in N6-131 remain open.

Replay:

```text
python scripts/n6_k32_torus_exposed_weight_faces.py \
  --json data/n6_k32_torus_exposed_weight_faces.json
python scripts/n6_k32_torus_exposed_weight_faces.py \
  --verify-json data/n6_k32_torus_exposed_weight_faces.json
python -m unittest tests.test_n6_k32_torus_exposed_weight_faces -v
```
