# N6-124: first-Schur weight blocks at the \(K_{3,2}\) collision

**Status.** EXACT_QQ_FIRST_SCHUR_WEIGHT_BLOCK_PROFILES.
This is an exact characteristic-zero block calculation, not a full tangent-cone
classification.

At the coordinate collision \(L=M=A_3\otimes P_2\), the rank-three base cross
matrix has a \(33\times15\) first Schur map \(S_1(T)\), linear in the relative
graph direction \(T\). Keeping target and source row/column characters
separate, the row-column torus separates its 36 entries into 24 singleton
weight blocks and four three-variable same-row blocks.

The exact rational replay gives:

- every singleton row-changing block has \(\operatorname{rank}S_1=3\);
- each same-row block has generic rank 6;
- in each same-row block, rank at most 3 occurs exactly when its three
  coefficients are equal, giving one line \(a_0=a_1=a_2\).

For the last statement, the replay computes all nonzero \(4\times4\) minors
of one representative block and their exact Gröbner basis. The basis contains
\(c^3(a-c)\), \(c^3(b-c)\), and, when \(c=0\), the equations \(a^4=b^4=0\).
Thus its rank-\(\le3\) zero set is precisely \(a=b=c\); the other three
blocks are related by column permutations.

Consequently the only individual weight-block candidates for first-Schur
rank at most 3 are 24 row-changing unit lines and four equal-coefficient
same-row lines, 28 lines in total. This is a candidate list for individual
blocks only. Sums of different torus-weight blocks can interact through the
matrix rank condition and are deliberately left open.

The result does not classify the full first tangent cone, nonlinear lifts,
arbitrary \(6\times6\) graph operators, ordinary lower 29, or exact
unrestricted Chow rank 32.

Replay:

~~~text
python scripts/n6_k32_first_schur_weight_blocks.py \
  --verify-json data/n6_k32_first_schur_weight_blocks.json
python -m unittest tests.test_n6_k32_first_schur_weight_blocks -v
~~~
