# N6-126: full first-Schur weight blocks at the (K_{3,2}) collision

**Status.** `EXACT_QQ_FULL_FIRST_SCHUR_WEIGHT_BLOCKS` in characteristic zero.

N6-124 studied only the relative graph slice.  Here both Grassmann factors
are allowed to move independently in the (72)-variable graph chart at
[
L=M=A_3otimes P_2.
]
The base cross matrix has rank (3).  Its first Schur map has shape
(33	imes15), and its flattened coefficient matrix has shape (495	imes72)
and exact rank (72).

## 1. Torus blocks

The row-column torus separates the (72) variables into (28) character
blocks:

- (24) row-changing blocks, each with one (L)- and one (M)-variable;
- (4) same-row blocks, each with three (L)- and three (M)-variables.

The block calculation is exact over (mathbf Q), not a finite-field scan.

## 2. Row-changing blocks

For a row-changing block with coefficients ((a,b)), the nonzero (4	imes4)
minors have common factor (a+b).  After dividing by this factor and setting
(b=1), their univariate gcd is (1); a separate (b=0) witness handles the
point at infinity.  Therefore
[
operatorname{rank}S_1(a,b)le3quadLongleftrightarrowquad a+b=0.
]

Thus the only rank-three line in each row-changing character is the
anti-diagonal relative direction.  These are exactly the 24 directions
covered by the N6-123 all-order single-cross exclusion.

## 3. Same-row blocks

Order the six coefficients as
[
(l_0,l_1,l_2,m_0,m_1,m_2).
]
The block has (15) active output rows and (6) output columns.  Each active
row is supported in exactly one output column.  Hence the matrix rank is the
number of active output columns, and rank at most (3) is equivalent to
vanishing of at least three columns.

Enumerating the (20) triples of zero columns gives exactly five projective
lines:
[
egin{gathered}
(1,1,1,1,1,1),quad
(1,-1,-1,1,-1,-1),quad
(1,-1,1,1,-1,1),\\
(1,1,-1,1,1,-1),quad
(1,1,1,-1,-1,-1).
end{gathered}
]
The last line is the relative all-row direction treated by N6-125; the other
four are average/sign directions and remain to be analyzed nonlinearly.

Consequently the complete full-chart torus-fixed first-Schur list has
[
24+4cdot5=44
]
projective lines.  This corrects the narrower relative count in N6-124.

## 4. Boundary

This is a fixed-weight first-order classification only.  It does not classify
sums of different torus characters, the full first tangent cone, nonlinear
lifts of the four average/sign lines, arbitrary invertible (6	imes6) graph
operators, the six-term cocycle, ordinary lower (29), exact
(operatorname{ChowRank}(operatorname{perm}_6)), or border rank.

Replay:

~~~text
python scripts/n6_k32_full_first_schur_weight_blocks.py \\
  --verify-json data/n6_k32_full_first_schur_weight_blocks.json
python -m unittest tests.test_n6_k32_full_first_schur_weight_blocks -v
~~~
