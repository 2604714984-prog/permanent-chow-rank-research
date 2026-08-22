# `perm_7` lower-51: rank-five equality forms

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

## Excluding support on three or more frame directions

Let `Q=LM` and suppose first that its support is contained in three frame
directions.  Put `g=x_1x_2x_3Q` and `h=x_4x_5`.  The same disjoint-variable
calculation gives

\[
 \dim\mathcal D_3(gh)=3+3\dim\mathcal D_2(g).
\]

Thus equality 15 requires the `6 by 10` middle catalectic of `g` to have
rank at most four.  Write

\[
 Q=q_{00}x_1^2+q_{11}x_2^2+q_{22}x_3^2+
 q_{01}x_1x_2+q_{02}x_1x_3+q_{12}x_2x_3.
\]

Exact `5 by 5` minors give the following finite case split.

- If all three diagonal coefficients are nonzero, minors proportional to
  `q00^3*q01*q22`, `q00^3*q02*q11`, and `q00^3*q12*q22` force all cross
  coefficients to vanish.  The resulting diagonal quadratic has rank three,
  contradicting `Q=LM`.
- If exactly two diagonal coefficients are nonzero, say `q00,q11`, minors
  force `q02=q12=0`; the remaining condition is precisely
  `q01*(9*q00*q11-2*q01^2)=0`.
- If exactly one diagonal coefficient is nonzero, three power minors force
  all cross coefficients to vanish.  If none is nonzero, fifth-power minors
  force `Q=0`.

For a putative equality form with larger support, specialize the coefficients
of `L,M` outside any chosen three frame directions to zero.  Catalectic rank
cannot increase under specialization, while the five fixed coordinate
factors keep factor rank five, whose universal lower bound is 15.  Hence
every nonzero three-direction specialization is again an equality form and
the preceding case split applies.  If the union of the supports of `L,M`
contained at least three indices, one could choose three retaining both
factors and genuinely using all three, a contradiction.  Consequently, after
a coordinate permutation both extra factors lie in one coordinate two-plane,
and (3) is the complete rank-five middle-equality classification.

Coordinate scalings on `x_1,x_2` show that the equality locus has exactly
three orbit types (up to frame permutation):

1. the triple-parallel boundary, where only one square coefficient is
   nonzero;
2. the two-square diagonal type, with `c^2/(ab)=0`;
3. the conic type, with `c^2/(ab)=9/2`.

If a binary tail lies off the equality divisor, (3) gives middle dimension
18.  If a pair uses at least three directions and were not already an
equality form, choose a three-direction specialization witnessing this.  Its
ternary formula is `3+3*dim D2(g)`, with the middle rank at least five, hence
at least 18; semicontinuity transfers that lower bound back to the original
pair.  Therefore every non-equality rank-five product has

\[
 \dim\mathcal D_3(T)\ge18,
\]

so its full-increment surplus is at least `18-15=3`.

The computation is replayed by
`scripts/n7_lower51_rank5_binary_equality.py`.  This completes
`R5-EQUALITY-FORMS`.  It does not classify intermediate quotient directions
or close every rank-five 50-term packet.
