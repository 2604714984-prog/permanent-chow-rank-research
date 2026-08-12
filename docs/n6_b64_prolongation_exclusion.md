# Prolongation excludes the `b=64` endpoint

**Status.** `PURE_GLOBAL_FIXED_POINT_REDUCTION`,
`EXACT_FINITE_UPPER_BOUND`, `B64_EXCLUDED` (N6-044).  The base field is
algebraically closed of characteristic zero.  This note excludes the single
`b=64` endpoint of the hypothetical twenty-six-term decomposition.  It does
not exclude the other endpoints and does not prove
`ChowRank(perm_6)>=27`.

## 1. The endpoint and the required cubic dimension

Put

\[
 E_m=\mathcal D_m(\operatorname{perm}_6).
\]

At the fixed-six `b=64` endpoint of N6-038, let

\[
 R=T_1+\cdots+T_6,
 \qquad H_m=\mathcal D_m(R),
 \qquad F_i=\mathcal D_2(T_i).
\]

The already proved endpoint equalities are

\[
 \dim H_3=120,
 \qquad \dim(E_3\cap H_3)=64,
 \qquad \dim H_2=90,
 \qquad \dim(E_2\cap H_2)=78.
\tag{1.1}
\]

Moreover, the six fifteen-dimensional spaces `F_i` have literal direct sum.
Since derivatives of a sum lie in the sum of the individual derivative
spaces,

\[
 H_2\subseteq F_1+\cdots+F_6.
\]

Both sides have dimension ninety, so equality holds and every `F_i` is
contained in `H_2`.  N6-040 also gives

\[
 q(F_i)=q(H_2)=W,
 \qquad \dim W=12,
\tag{1.2}
\]

where `q:Sym^2 V -> Sym^2 V/E_2`.  Hence, for every `i`,

\[
 \boxed{E_2+F_i=E_2+H_2=:A,\qquad \dim A=237.}
\tag{1.3}
\]

For a quadratic space `B`, define its first cubic prolongation by

\[
 B^{(1)}=
 \{g\in\operatorname{Sym}^3V:
       \partial_\lambda g\in B\text{ for all }\lambda\in V^*\}.
\tag{1.4}
\]

Every first derivative of `E_3` lies in `E_2`, and every first derivative of
`H_3` lies in `H_2`.  Equation (1.3) therefore implies

\[
 E_3+H_3\subseteq A^{(1)}.
\]

But `dim E_3=400`, so (1.1) requires

\[
 \boxed{\dim A^{(1)}\ge400+120-64=456.}
\tag{1.5}
\]

We prove that every actual extremal frame instead satisfies the universal
upper bound `436`.

## 2. Why a generic specialization argument is insufficient

Every extremal frame branch contains a coordinate frame, and the coordinate
prolongation has dimension `428`.  This alone does **not** give a universal
upper bound: kernel dimension is upper semicontinuous and can jump upward on
an exceptional closed locus.  The following projective maximum argument is
what makes the reduction global.

Let `Y` be the closure, inside

\[
 \operatorname{Gr}(6,V)\times
 \operatorname{Gr}(15,\operatorname{Sym}^2V),
\]

of all pairs `(L,F)` arising from actual independent extremal Chow frames.
Thus

\[
 F\subseteq\operatorname{Sym}^2L,
 \qquad Q_L:=E_2\cap\operatorname{Sym}^2L\subseteq F.
\tag{2.1}
\]

The extremal six-plane classification shows that `dim Q_L=3` everywhere on
the closed extremal locus.  Consequently (2.1) is a closed vector-bundle
incidence and remains true on `Y`.  In particular,

\[
 \dim(E_2+F)=225+15-3=237
\tag{2.2}
\]

everywhere on `Y`.  Thus `(L,F) -> E_2+F` is a morphism from `Y` to
`Gr(237,Sym^2 V)`.

The function

\[
 h(L,F)=\dim(E_2+F)^{(1)}
\tag{2.3}
\]

is the kernel dimension of a vector-bundle map and is therefore upper
semicontinuous.  The actual extremal-frame locus is row-column-torus stable,
so its closure `Y`, as well as `E_2` and `h`, is preserved by that torus.  The
locus where `h` assumes its maximum is consequently a nonempty closed
torus-stable projective subvariety.  An orbit closure for a torus action on a
projective variety contains a torus fixed point.  Therefore the global
maximum of `h` on `Y` occurs at a torus-fixed pair `(L,F)`.

This argument controls exceptional points as well as generic ones; it does
not infer a universal statement from semicontinuity at one specialization.

## 3. Complete classification of the fixed pairs needed for the bound

The variable weights `x_(rc)` of the row-column torus are distinct.  A fixed
six-plane `L` is therefore coordinate.  Since it lies in the extremal locus,
the extremal six-plane theorem makes it a coordinate `K_(2,3)` or `K_(3,2)`
plane.  Transposition reduces the calculation to

\[
 L_0=\langle x_{00},x_{01},x_{02},x_{10},x_{11},x_{12}\rangle.
\]

The torus weight decomposition of `Sym^2 L_0` consists of:

1. fifteen one-dimensional weight spaces: six squares, six same-row
   products, and three same-column products;
2. three two-dimensional rectangle weight spaces, one for each pair of
   columns.

In every rectangle block, `Q_(L_0)` contains its permanent line.  A
torus-stable fifteen-plane `F` containing `Q_(L_0)` therefore contains either
only that line or the entire two-dimensional block.  If it contains `d`
entire rectangle blocks, it must contain `12-d` of the fifteen singleton
axes.  The complete number of fixed candidates is thus

\[
 \sum_{d=0}^3 {3\choose d}{15\choose 12-d}
 =455+4095+9009+5005
 =\boxed{18564}.
\tag{3.1}
\]

This deliberately enumerates every torus-stable `F` satisfying the closed
incidences, including candidates which might not themselves be limits of
actual frames.  Enlarging the set is harmless for an upper bound.

## 4. Exact coefficient-component upper bound

Fix one of the 18564 candidates and put `A=E_2+F`.  Write a general cubic as

\[
 g=\sum_{|\alpha|=3}c_\alpha x^\alpha.
\]

The conditions `partial_lambda g in A` have only two forms in the monomial
basis:

- a coefficient is forced to zero when its derived quadratic monomial is
  absent from `A`;
- the two coefficients above opposite rectangle diagonals satisfy a
  nonzero weighted equality when only the permanent line is present.

Make a graph whose vertices are the cubic coefficients, join two vertices
whenever such an equality occurs, and mark a component zero whenever it
contains a forced-zero vertex.  Every unmarked connected component carries
at most one free scalar.  Ignoring the nonzero derivative multiplicities and
signs can remove inconsistent-cycle equations, but it cannot lower this
count.  Hence

\[
 \dim A^{(1)}
 \le \#\{\text{unmarked coefficient components}\}.
\tag{4.1}
\]

The exact integer replay constructs all cubic monomials, all zero/equality
constraints, and all 18564 fixed candidates.  Its maximum in (4.1) is

\[
 \boxed{436}.
\tag{4.2}
\]

There are three candidates attaining this component upper bound.  No
finite-field or floating-point inference is used.  Since transposition
preserves the calculation, (4.2) holds at every torus-fixed pair.  Section 2
then gives the universal result

\[
 \boxed{\dim(E_2+F)^{(1)}\le436}
\tag{4.3}
\]

for every actual extremal frame.

## 5. Exclusion and claim boundary

At `b=64`, choose any one of the six fixed terms.  Equations (1.3) and (1.5)
give

\[
 456\le\dim(E_2+F_i)^{(1)},
\]

whereas (4.3) gives

\[
 \dim(E_2+F_i)^{(1)}\le436.
\]

This contradiction proves:

### Theorem 5.1

The `b=64` endpoint of the hypothetical twenty-six-term decomposition of
`perm_6` is impossible.

The theorem removes one endpoint only.  It does not exclude the remaining
`b` values, does not prove `ChowRank(perm_6)>=27`, and makes no border-Chow-
rank assertion.  The number `436` is a certified upper bound; the replay does
not claim it is the exact prolongation dimension of the three maximizing
fixed candidates.

## 6. Replay

Run

```text
python scripts/n6_b64_prolongation_exclusion.py \
  --json data/n6_b64_prolongation_exclusion.json
python -m unittest tests/test_n6_b64_prolongation_exclusion.py -v
```

Expected principal outputs are

```text
fixed_F_count=18564
fixed_F_count_by_full_rectangle_blocks={0:455,1:4095,2:9009,3:5005}
maximum_prolongation_dimension_upper_bound=436
b64_required_dimension=456
strict_gap=20
N6_B64_PROLONGATION_EXCLUSION_PASS
```
