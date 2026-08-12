# Central directness does not force quadratic directness

## Status

`PURE_EXPLICIT_COUNTEREXAMPLE + EXACT_QQ_REPLAY` (G-045).

This note closes one proposed shortcut at the `b=34` endpoint of the
ordinary lower-28 program.  Literal directness of sextic Chow derivative
spaces in degrees three and four does not imply literal directness in degree
two.

## 1. Explicit terms and pure support count

In ten independent variables put

\[
 T_A=x_0x_1x_2x_3x_4x_5,
 \qquad
 T_B=x_0x_1x_6x_7x_8x_9.
\tag{1.1}
\]

For a squarefree monomial supported on a six-set `S`, its degree-`m`
derivative space has the squarefree monomial basis indexed by
`binom(S,m)`.  The two supports in (1.1) meet in `{0,1}`.  Hence

\[
 \dim\bigl(\mathcal D_m(T_A)\cap\mathcal D_m(T_B)\bigr)
 =\binom2m.
\tag{1.2}
\]

If `K_m` denotes the ordinary colored relation space of the two literal
degree-`m` derivative spaces, (1.2) gives

\[
 \boxed{\kappa_2=1,\qquad\kappa_3=\kappa_4=0.}
\tag{1.3}
\]

Thus both the central cubic spaces and the literal quartic spaces are direct,
while the quadratic spaces have the common line `span(x0*x1)`.

## 2. Coupled derivative ranks

For completeness, exact sparse rational elimination on the catalectics of
`T_A+T_B` gives

\[
 \boxed{
 \dim\mathcal D_2(T_A+T_B)=29,
 \quad
 \dim\mathcal D_3(T_A+T_B)=40,
 \quad
 \dim\mathcal D_4(T_A+T_B)=29.
 }
\tag{2.1}
\]

These numbers also follow directly from supports.  In degree two the two
literal images share `x0*x1`, giving 29.  In degree three their monomial
bases are disjoint, giving 40.  In degree four the literal image spaces are
disjoint and have total dimension 30, but the single source differential
`partial_0 partial_1` maps to

\[
 x_2x_3x_4x_5+x_6x_7x_8x_9,
\]

so the coupled catalectic has rank 29.  This distinction between the literal
quartic sum and the coupled quartic image is essential.

## 3. Consequence and boundary

The example disproves the implication

```text
kappa_3 = kappa_4 = 0  =>  kappa_2 = 0.
```

Therefore any proposed backward shortcut for the lower-28 `b=34` endpoint
which requires quadratic literal directness from central and quartic literal
directness fails.  Differentiation controls higher-degree relations from
lower-degree ones; this example rules out only the zero-relation converse,
not every possible quantitative relation-shadow inequality.

The example contains only two terms and does not involve `E_m(perm_6)`.  It
does not realize the required 366- or 367-dimensional relative central
intersection, and it neither proves nor refutes ordinary lower 28, exact
rank 32, or any border-rank statement.

## 4. Replay

```text
python scripts/n6_central_neardirect_quadratic_barrier.py \
  --verify-json data/n6_central_neardirect_quadratic_barrier.json
python -m unittest tests/test_n6_central_neardirect_quadratic_barrier.py -v
```

The support proof is pure combinatorics.  The regression uses exact rational
sparse elimination; there is no random, floating-point, or finite-field
inference.
