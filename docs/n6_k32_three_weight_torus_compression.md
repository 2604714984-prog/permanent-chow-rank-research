# N6-135: three-weight torus compression at the (K_{3,2}) collision

**Status.** `EXACT_QQ_THREE_WEIGHT_TORUS_COMPRESSION` in characteristic zero.

This certificate is a small extension of N6-126 and N6-128.  It does not
claim a full tangent-cone theorem.

## Exact input

The 44 matrices are the fixed rank-three first-Schur rays from N6-126.  A
graph variable from source ((i,p)) to target ((j,q)) is assigned the
row-column torus character

\[
  (e_j-e_i,\,f_q-f_p),
\]

where (p\in\{0,1\}) and (q\in\{2,3\}).  The four finite values
(t=1,2,3,5) classify an identically rank-three pencil exactly: every
4-by-4 minor of (tA+B) has degree at most three, since both endpoint
matrices have rank three.

The exact QQ scan gives:

- 946 unordered ray pairs;
- 102 pairs whose pencil is identically rank at most three;
- 52 compatible triangles;
- every compatible triangle has affine character rank 2;
- all 52 triangles lie in 13 four-cliques;
- no four-clique extends to a five-clique;
- every one of the 13 four-ray spans has symbolic rank exactly 3 for arbitrary
  coefficients.

The frozen JSON stores the complete pair and four-clique index lists, so the
small graph calculation is reproducible rather than a random sample.

## Torus consequence

Let (R_1,R_2,R_3) be three distinct candidate rays with nonzero coefficients
and affinely independent characters.  If

\[
  x=c_1R_1+c_2R_2+c_3R_3
\]

has rank at most 3, the diagonal torus orbit of ([x]) is dense in the whole
projective plane (mathbb P\langle R_1,R_2,R_3\rangle).  The rank-at-most-three
determinantal locus is closed, so the entire three-ray span has rank at most
three.  Consequently all three pair pencils are compatible.  The exact graph
then places the triangle inside one of the 13 listed four-ray rank-three
spaces.

This is a genuine characteristic-zero conditional compression: it reduces a
three-distinct-weight, full-support rank-three point to 13 explicit linear
spaces.  It is not an exclusion of those spaces; their points remain possible
normal-cone directions until another argument applies.

## Boundary

The certificate does not classify affine-degenerate triples, repeated rays in
one same-row character block, supports with four or more weights whose torus
character span is not the full projective span, nonlinear lifts, arbitrary
invertible graph operators, ordinary lower 29, exact
(operatorname{ChowRank}(operatorname{perm}_6)), or border rank.

Replay:

```text
python scripts/n6_k32_three_weight_torus_compression.py --verify-json data/n6_k32_three_weight_torus_compression.json
python -m unittest tests.test_n6_k32_three_weight_torus_compression -v
```
