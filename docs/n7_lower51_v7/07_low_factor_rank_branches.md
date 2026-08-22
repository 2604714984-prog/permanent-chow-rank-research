# v7 Module 07 — low-factor-rank exceptional branches

Do not assume the lower-49 factor-span floors persist at 50 terms; decide the rank-one through rank-five possibilities explicitly.

## LR-01 — enumerate surviving low-rank atoms

List all rank-one through rank-five states that fit the 35-unit budget when placed first and last.

**Decisive output:** `LOW-RANK-ATOMS`.

## LR-02 — classify rank-five equality forms

Determine the actual Chow normal forms with middle dimension 15 and full-quotient equality.

**Decisive output:** `R5-EQUALITY-FORMS`.

## LR-03 — classify rank-five near-equality forms

Bound all other rank-five middle profiles and their ordering costs.

**Decisive output:** `R5-NEAR-EQUALITY`.

## LR-04 — combine low rank with subset floors

Use two-, three-, and larger-subset floors to constrain every low-rank term's neighbors.

**Decisive output:** `LOW-RANK-NEIGHBORS`.

## LR-05 — exclude multiple low-rank terms

Determine the maximum number of rank-at-most-five terms permitted by all-order budgets and span floors.

**Decisive output:** `LOW-RANK-COUNT-BOUND`.

## LR-06 — analyze rank-four extremals

Classify the minimal-middle rank-four forms that consume only a small full-quotient surplus.

**Decisive output:** `R4-EXTREMALS`.

## LR-07 — analyze ranks one through three

Use conciseness, derivative intersections, and surplus to close or isolate them.

**Decisive output:** `R1-R3-RESULT`.

## LR-08 — derive direct-basis alternatives

Enumerate direct dimension compositions containing low-rank blocks.

**Decisive output:** `LOW-RANK-BASES`.

## LR-09 — derive residual projections

Build the correct degree-three/four restriction theorem for each surviving mixed basis.

**Decisive output:** `LOW-RANK-PROJECTION`.

## LR-10 — use grouped-degree structure

Test whether target containment forces coordinate or row/column-separated factors, as in the lower-50 `K2=0` branch.

**Decisive output:** `LOW-RANK-GROUPED-DEGREE`.

## LR-11 — use centroid and conciseness

Exclude actual decompositions that split the permanent into proper variable blocks.

**Decisive output:** `LOW-RANK-ST-OBSTRUCTION`.

## LR-12 — cover dependent-factor degenerations

Ensure all normal forms and closure arguments include repeated factors.

**Decisive output:** `LOW-RANK-BOUNDARIES`.

## LR-13 — freeze exact survivors

Require a full identity residual and independent verification.

**Decisive output:** `LOW-RANK-SURVIVOR`.

## LR-14 — issue the lane verdict

Return `LOW-RANK-BRANCHES-CLOSED` or a full 50-term identity.

**Decisive output:** `LOW-RANK-VERDICT`.
