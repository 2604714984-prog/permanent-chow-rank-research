# N6-125: the same-row finite (K_{3,2}) germ

**Status.** `EXACT_SAME_ROW_FINITE_GERM_EXCLUSION` in characteristic zero.

N6-124 leaves four same-row equal-coefficient directions as the only
individual first-Schur blocks which can have rank at most three.  This note
re-centers one representative and computes its complete local
rank-at-most-six germ.

## 1. The finite point

Use the (K_{3,2}) support
[
W=langle 00,01,10,11,20,21angle.
]
At the representative (T=I_3otimes E_{00}), take
[
L_0=operatorname{graph}(T),qquad M_0=operatorname{graph}(-T).
]
The exact cross rank is (6), while
[
dim(L_0+M_0)=9.
]
The two graph charts have (72) variables.  The first Schur matrix has
shape (360	imes72), rank (68), and a four-dimensional exact rational
kernel.

## 2. The quadratic initial ideal

After eliminating the (68) linear variables, the quadratic Schur columns
have reduced generators
[
J=(x_0^2-x_2^2, x_0x_3, x_2x_3).
]
Its reduced support is the union of three planes:
[
egin{aligned}
&x_3=0,quad x_0-x_2=0,\\
&x_3=0,quad x_0+x_2=0,\\
&x_0=x_2=0.
end{aligned}
]
The calculation gives (Jsubsetoperatorname{in}_{mathfrak m}(I)), where
(I) is the completed rank-at-most-six incidence ideal.

## 3. Three exact branches and the sandwich

The three planes integrate without higher corrections.  In the displayed
graph coordinates they are:


- (B_+): (x_3=0, x_2=x_0);
- (B_-): (x_3=0, x_2=-x_0);
- (B_{mathrm{prod}}): (x_0=x_2=0).

For all parameters, each branch has cross rank (6).  The first two have
(dim(L+M)=9).  The third is the common-(A_3) product family and has
(dim(L+M)=12) generically.  Their graph coordinates recover the branch
parameters, so the maps are formal closed embeddings.  Their three prime
ideals intersect in exactly (J).  Therefore the branch inclusions give
(operatorname{in}_{mathfrak m}(I)subset J), and the complete filtered
lifting argument gives the scheme-theoretic union of these three branches.

On the product branch the frame determinant is
[
det[Lmid M]=64,x_3^3(x_1-1)^3.
]
Thus only this branch can be complementary.  It is precisely the
(I_3otimesoperatorname{Mat}_2) family; N6-119 proves that its relaxed
cross-free (12)-plane has block projections of rank at most (9), so it
cannot be an actual Chow section difference.

Consequently no actual complementary Chow pair passes through this finite
same-row representative.  Column permutations carry the result to all four
same-row equal-coefficient directions from N6-124.

## 4. Boundary

This is a local theorem for the four same-row finite representatives.  It
does not classify mixed first-Schur weight sums, arbitrary (6	imes6) graph
operators, the full six-term cocycle, ordinary lower (29), exact
(operatorname{ChowRank}(operatorname{perm}_6)), or border rank.

Replay:

~~~text
python scripts/n6_k32_same_row_finite_germ.py \\
  --verify-json data/n6_k32_same_row_finite_germ.json
python -m unittest tests.test_n6_k32_same_row_finite_germ -v
~~~
