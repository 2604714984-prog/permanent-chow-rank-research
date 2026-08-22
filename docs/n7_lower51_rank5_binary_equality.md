# `perm_7` lower-51: rank-five binary equality family

Fix five independent factor directions as `x_1,...,x_5`.  If the two
remaining factors are supported on `span(x_1,x_2)`, write their product as

\[
 L M=a x_1^2+c x_1x_2+b x_2^2.
\]

For

\[
 T=x_1x_2x_3x_4x_5LM,
\]

put `g=x_1x_2LM` and `h=x_3x_4x_5`.  The disjoint-variable derivative
decomposition gives

\[
 \dim\mathcal D_3(gh)=1+2\cdot3+
 3\dim\mathcal D_2(g)+2=9+3\dim\mathcal D_2(g).     \tag{1}
\]

The middle binary catalectic of
`g=a*x_1^3*x_2+c*x_1^2*x_2^2+b*x_1*x_2^3` is

\[
 \begin{pmatrix}
 0&6a&2c\\3a&4c&3b\\2c&6b&0
 \end{pmatrix},
 \qquad
 \det=8c(9ab-2c^2).                                \tag{2}
\]

The binary quartic remains concise, so this matrix has rank at least two.
Equations (1)--(2) therefore give the exact classification

\[
 \dim\mathcal D_3(T)=
 \begin{cases}
 15,&c(9ab-2c^2)=0,\\
 18,&c(9ab-2c^2)\ne0.
 \end{cases}                                      \tag{3}
\]

The full `35 by 70` symbolic third-derivative matrix independently replays
both ranks.  Gorenstein symmetry gives the same degree-four middle
dimension.

Over the algebraically closed characteristic-zero base field, every
binary quadratic factors.  Thus (3) supplies two genuine rank-five equality
components: the diagonal family

\[
 x_1x_2x_3x_4x_5(a x_1^2+b x_2^2),
\]

including the triple-parallel boundary when one coefficient vanishes.  In
addition, the conic `9ab=2c^2` is an equality component with generically
nonzero cross coefficient.  The equality locus is therefore strictly larger
than the monomial normal form `x_1^3x_2x_3x_4x_5`; treating that monomial, or
even the diagonal family, as the whole equality locus would be incorrect.

The computation is replayed by
`scripts/n7_lower51_rank5_binary_equality.py`.  This closes the binary-tail
subcase of `R5-EQUALITY-FORMS`, but not the full task: one must still prove
that a middle-dimension-15 pair with support on three or more frame
directions reduces to this family, or classify an additional component.
