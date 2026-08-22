# Global quotient-prolongation caps above an extremal term

**Status.** `PURE_PROJECTIVE_FIXED_POINT_REDUCTION`,
`EXACT_MODULAR_UPPER_CERTIFICATE`, `EXTREMAL_STATE_EXCLUSION` (N6-047).
The base field is algebraically closed of characteristic zero.  This note
excludes every remaining `b=61,62,63` fixed-six state which contains at least
one extremal rectangle term.  It does not treat a general `alpha=1` term and
does not exclude the fourteen states having no extremal term.

## 1. The global ambient quadratic space

Write

\[
 E_m=\mathcal D_m(\operatorname{perm}_6),
 \qquad H_m=\mathcal D_m(R),
 \qquad A=E_2+H_2,
\]

where `R` is the sum of the six fixed terms.  Put

\[
 t=\dim(A/E_2).
\]

Suppose one fixed term is extremal and let

\[
 L=\langle\ell_1,\ldots,\ell_6\rangle,
 \qquad F=\mathcal D_2(\ell_1\cdots\ell_6).
\]

Then

\[
 \dim L=6,
 \qquad \dim F=15,
 \qquad Q_L:=E_2\cap\operatorname{Sym}^2L\subseteq F,
 \qquad \dim Q_L=3.
\tag{1.1}
\]

Since `F` is one of the individual derivative spaces entering `H_2` in the
surviving fixed-six states, the already proved coupled inclusions give

\[
 E_2+F\subseteq A.
\tag{1.2}
\]

Thus `q(F)` is a twelve-plane contained in the global `t`-plane `A/E_2`.
Unlike a local calculation inside `Sym^2L`, the remaining `t-12` directions
of `A/E_2` may be arbitrary ambient quotient directions.  The finite
calculation below includes all of them.

Every derivative of `E_3` lies in `E_2`, and every derivative of `H_3` lies
in `H_2`.  For the first prolongation

\[
 A^{(1)}=
 \{g\in\operatorname{Sym}^3V:
       \partial_\lambda g\in A\text{ for all }\lambda\in V^*\},
\]

one therefore has

\[
 E_3+H_3\subseteq A^{(1)}
\]

and hence

\[
 \boxed{\dim A^{(1)}\ge400+h-b,}
 \qquad
 h=\dim H_3,\quad b=\dim(E_3\cap H_3).
\tag{1.3}
\]

For the surviving layers, the right side ranges from `457` through `459`.

## 2. A projective fixed-point reduction which controls every point

For fixed `t in {12,13,14}`, consider the relaxed incidence variety `Y_t` of
triples `(L,F,A)` satisfying:

\[
\begin{aligned}
 &L\in\operatorname{Gr}(6,V),
 &&\dim(E_2\cap\operatorname{Sym}^2L)=3,\\
 &F\in\operatorname{Gr}(15,\operatorname{Sym}^2V),
 &&Q_L\subseteq F\subseteq\operatorname{Sym}^2L,\\
 &A\in\operatorname{Gr}(225+t,\operatorname{Sym}^2V),
 &&E_2+F\subseteq A.
\end{aligned}
\tag{2.1}
\]

The extremal six-plane theorem identifies the first line with the closed
extremal locus and proves that `dim Q_L=3` everywhere on it.  Consequently
`Q_L` is the kernel bundle of a constant-rank vector-bundle map.  The two
remaining containments in (2.1) are closed Grassmann-bundle incidences.
Thus `Y_t` is projective.  It is a relaxation of the actual fixed-term
geometry, so proving an upper bound on all of `Y_t` is sufficient.

The function

\[
 (L,F,A)\longmapsto\dim A^{(1)}
\tag{2.2}
\]

is the kernel dimension of a vector-bundle map whose entries depend
regularly on `A`; it is upper semicontinuous.  The row-column torus preserves
`Y_t`, `E_2`, and (2.2).  Its maximum locus is a nonempty closed torus-stable
projective variety.  The closure of a torus orbit in a projective variety
contains a fixed point.  Therefore the global maximum of (2.2) occurs at a
torus-fixed triple.

This is a maximum-on-a-projective-incidence argument.  It does not infer a
universal bound from a generic specialization.

## 3. Classification of all fixed triples

At a fixed triple, `L` is a coordinate six-plane in the extremal locus and
therefore a coordinate `K_(2,3)` or `K_(3,2)` plane.  Row-column permutation
and transposition symmetry reduce to

\[
 L_0=\langle x_{00},x_{01},x_{02},x_{10},x_{11},x_{12}\rangle.
\]

As in N6-044, the torus-fixed fifteen-planes `F` containing `Q_(L_0)` give
exactly

\[
 {18\choose12}=18564
\tag{3.1}
\]

twelve-axis spaces `W=q(F)` inside the eighteen local quotient axes.

Globally,

\[
 \dim(\operatorname{Sym}^2V/E_2)=441.
\]

All its torus weight spaces are one-dimensional:

\[
 36\text{ squares}
 +90\text{ same-row axes}
 +90\text{ same-column axes}
 +225\text{ rectangle quotient axes}.
\tag{3.2}
\]

Hence a fixed `A/E_2` is a coordinate `t`-plane.  Once its contained
twelve-plane `W` is fixed, its extra directions are an arbitrary choice of
one or two of the remaining

\[
 441-12=429
\tag{3.3}
\]

ambient axes.  In particular, these directions are not restricted to
`q(Sym^2L_0)`.

## 4. Exact cubic-weight calculation

The `8436` cubic monomials split into

\[
 {6+3-1\choose3}^2=56^2=3136
\]

row-column torus weight blocks.  Inside one block, write the coefficients of
a cubic `g` as a column vector.  For every derivative direction, membership
of the derivative in `A` gives one integer linear equation in that block,
labelled by a quadratic quotient axis.  Selecting that axis in `A/E_2`
removes precisely the labelled equation.

The replay builds every block and every labelled derivative equation.  It
computes the ranks modulo the prime

\[
 p=1000003.
\]

For an integer matrix,

\[
 \operatorname{rank}_{\mathbb Q}M
 \ge\operatorname{rank}_{\mathbb F_p}(M\bmod p),
\]

so the modular nullity is a rigorous upper bound for the characteristic-zero
nullity.  Summing the 3136 block bounds therefore gives a rigorous upper
bound for `dim A^(1)`; equality across characteristics is not assumed.

### The `t=12` and `t=13` searches

The stabilizer `S_2 times S_3` of `L_0` has `1683` orbits on the `18564`
possible `W`.  The exact orbit-size histogram is

\[
 \{1:3, 2:6, 3:17, 6:231, 12:1426\}.
\tag{4.1}
\]

For every orbit representative the replay tests all 429 possible ambient
extra axes.  It obtains

\[
 \boxed{
 \dim A^{(1)}\le436\quad(t=12),
 \qquad
 \dim A^{(1)}\le440\quad(t=13).
 }
\tag{4.2}
\]

### Completeness of the `t=14` pair reduction

There are `C(441,2)=97020` unordered pairs of quotient axes.  Two axes affect
disjoint sets of cubic weight blocks for 77040 pairs.  The other pairs share
one block in 16200 cases and six blocks in 3780 cases.

For a fixed `W`, gains of a disjoint pair add.  Sorting the 429 individual
gains and stopping only when the sum of the current gain and the next gain
cannot exceed the incumbent is an exact branch-and-bound search, not a
heuristic.  Every one of the 19980 interacting pairs is evaluated explicitly;
on its one or six shared blocks the replay adds the exact failure-of-
additivity correction.  Thus every pair is covered.

Replacing an arbitrary `W` by its `S_2 times S_3` representative is also
lossless: the same stabilizer permutes all 441 ambient quotient axes, and the
search at the representative ranges over every ambient pair.  Therefore the
1683 representative searches cover all

\[
 18564{429\choose2}
\]

fixed triples.  The result is

\[
 \boxed{\dim A^{(1)}\le448\qquad(t=14).}
\tag{4.3}
\]

## 5. State exclusions

Combining (1.3), (4.2), and (4.3), every `b=61,62,63` state containing an
extremal term is impossible: its required dimension is at least 457, while
the applicable upper cap is at most 448.

Canonical state identifiers below are the zero-based positions in the
frozen N6-041 layer tables.

| `b` | all states | excluded here | remaining | remaining IDs |
|---:|---:|---:|---:|---|
| 61 | 73 | 61 | 12 | `b61_state_061` through `b61_state_072` |
| 62 | 11 | 10 | 1 | `b62_state_010` |
| 63 | 11 | 10 | 1 | `b63_state_010` |

The frozen JSON records every excluded ID and the complete data of every
remaining state.  Of the above exclusions, N6-046 had already removed 13,
4, and 4 states respectively; N6-047 supplies 48, 6, and 6 new exclusions.

The twelve remaining `b=61` states and the two all-`alpha=1` states at
`b=62,63` contain no extremal rectangle term.  They are outside the incidence
treated here.  Accordingly this theorem does not yet prove
`ChowRank(perm_6)>=27`.

## 6. Replay

Run

```text
python scripts/n6_global_quotient_prolongation_caps.py \
  --json data/n6_global_quotient_prolongation_caps.json
python -m unittest tests/test_n6_global_quotient_prolongation_caps.py -v
```

Expected principal outputs are

```text
fixed_W_count=18564
fixed_W_orbit_representative_count=1683
characteristic_zero_prolongation_upper_caps={12:436,13:440,14:448}
state_exclusion_counts={61:61,62:10,63:10}
remaining_state_counts={61:12,62:1,63:1}
N6_GLOBAL_QUOTIENT_PROLONGATION_CAPS_PASS
```
