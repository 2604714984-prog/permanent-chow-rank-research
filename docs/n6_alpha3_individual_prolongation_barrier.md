# The individual `alpha=3` prolongation barrier

**Status.** `PURE_EXACT_COUNTEREXAMPLE`, `EXACT_COORDINATE_REPLAY`,
`LOWER_27_ROUTE_BARRIER` (G-042).  The base field has characteristic zero.
There is an actual sextic Chow term with `(epsilon,alpha)=(0,3)` for which
the relevant cubic prolongation has dimension `520`.  Hence no universal
individual-term cap below the `b=60` target `460` exists.  This does not
exclude a coupled six-term argument.

## 1. Setup and the attempted cap

Let

\[
 E=\mathcal D_2(\operatorname{perm}_6).
\]

For a sextic Chow term `T`, put `F=\mathcal D_2(T)`.  An `alpha=3`,
`epsilon=0` term satisfies

\[
 \dim F=15,
 \qquad E\cap F=0,
 \qquad \dim(E+F)=240.
\tag{1.1}
\]

At the surviving all-`alpha=3` `b=60` state, the global space
`A=E+H_2` would have quotient dimension fifteen and would have to satisfy

\[
 \dim A^{(1)}\ge400+120-60=460.
\tag{1.2}
\]

One might try to contradict (1.2) by proving
`dim(E+F)^(1)<460` for every individual `alpha=3` term.  The following
actual term disproves that proposed inequality.

## 2. An exact 520-dimensional actual example

Take all six variables in one row:

\[
 T=\prod_{c=0}^5x_{5c},
 \qquad
 F=\langle x_{5c}x_{5d}:0\le c<d\le5\rangle.
\tag{2.1}
\]

The factors are independent, `dim F=15`, and no permanent rectangle lies
inside one row, so `E\cap F=0`.  Thus (2.1) is an actual
`(epsilon,alpha)=(0,3)` Chow term.

The prolongation of `E+F` has a direct coefficient-block description.
Every nonzero cubic uses three distinct columns.  Its row multiset is either

1. three distinct rows;
2. `{5,5,r}` for one of the other five rows `r`; or
3. `{5,5,5}`.

Within each fixed row multiset and column triple, the permanent relations
connect all coefficients and leave one scalar.  Conversely, the corresponding
symmetrized cubic differentiates into `E+F`.  Therefore

\[
\begin{aligned}
 \dim(E+F)^{(1)}
 &=\binom63^2+5\binom63+\binom63\\
 &=400+100+20\\
 &=\boxed{520}.
\end{aligned}
\tag{2.2}
\]

The replay independently reconstructs every weighted coefficient constraint
over `Fraction` and obtains nullity `520`.  A row-column weight-block matrix
modulo `1000003` gives the same nullity.  The modular calculation is not
needed for (2.2); it is an independent exact diagnostic.

Consequently a universal individual `alpha=3` cap below `460` is false.

## 3. Exhaustive coordinate fixed diagnostics

A torus-fixed auxiliary six-plane is a six-edge bipartite graph.  A graph
with six edges has zero, one, or three rectangles.  Up to independent row
and column permutations, without quotienting by transposition, the exact
orbit counts are

\[
\begin{array}{c|ccc}
\text{rectangle count}&0&1&3\\ \hline
\text{labelled supports}&1837392&109800&600\\
\text{row-column orbits}&76&12&2.
\end{array}
\tag{3.1}
\]

For a rectangle-free support, `q(Sym^2L)` has 21 one-dimensional weights;
for a one-rectangle support it has 20.  The replay exhausts respectively all

\[
 \binom{21}{15}=54264,
 \qquad
 \binom{20}{15}=15504
\tag{3.2}
\]

fixed local fifteen-planes per support orbit.  It records the following
histograms of coefficient-component upper caps:

```text
rectangles=0:
{435:7, 436:4, 437:9, 439:4, 440:6, 442:4, 443:13,
 444:6, 450:3, 455:6, 458:6, 460:2, 485:4, 520:2}

rectangles=1:
{436:1, 437:2, 443:2, 445:2, 447:2, 450:1, 458:2}
```

For the three-rectangle `K_(2,3)` and `K_(3,2)` supports, N6-051 gives the
modular characteristic-zero upper cap `458`.  The two `520` rectangle-free
orbits are the same-row and transposed same-column configurations.  The
same-row maximum is exactly the actual example (2.1), not an artifact of
the relaxed fixed incidence.

## 4. Pure uniqueness over the coordinate obstruction

Let `S` be the six cells of one row, `L_S` their span, and `F_S` the
fifteen-plane of their squarefree products.

### Lemma 4.1

If nonzero linear forms `ell,m` satisfy

\[
 \ell m\in E+F_S,
\]

then `\ell,m\in L_S`.

#### Proof

There is no square monomial in `E+F_S`, so the coordinate supports of
`ell` and `m` are disjoint.  A cross pair sharing a row or column can occur
only when both cells lie in `S`.  For a cross pair in distinct rows and
columns, the permanent rectangle relation forces the opposite diagonal to
have nonzero coefficient.  Disjointness leaves one of the two assignments
of those opposite cells to the two factors.  The two resulting cross pairs
which share rows or columns would then force all four rectangle cells into
`S`, impossible because `S` lies in one row.  Hence every cross pair has
both cells in `S`.  Since both forms are nonzero, both supports lie in `S`.
\(\square\)

### Corollary 4.2

If an actual fifteen-dimensional Chow quadratic space `F` satisfies
`q(F)=q(F_S)`, then `F=F_S`.

Indeed, `F\subset E+F_S`, so every pair of its factors lies in `E+F_S`.
Lemma 4.1 puts every factor in `L_S`.  Since

\[
 (E+F_S)\cap\operatorname{Sym}^2L_S=F_S
\]

and both spaces have dimension fifteen, equality follows.  This conclusion
does not require the six factors to be independent.

Thus six literal-direct quadratic spaces cannot all lie over this coordinate
quotient.  However, directness is an open condition and can be lost in a
torus degeneration.  Coordinate-fiber uniqueness therefore does not by
itself exclude the global coupled endpoint.

## 5. Claim boundary and replay

The exact 520 example blocks only a universal **individual-term**
prolongation cap.  It does not refute the possibility of excluding the
all-`alpha=3` `b=60` state by using simultaneously that its six `F_i` are
literal direct and have one common quotient fifteen-plane.  It makes no
ordinary- or border-Chow-rank conclusion.

Run the CPU-parallel replay with

```text
python scripts/n6_alpha3_individual_prolongation_barrier.py \
  --workers 20 \
  --json data/n6_alpha3_individual_prolongation_barrier.json
python -m unittest tests/test_n6_alpha3_individual_prolongation_barrier.py -v
```

Expected principal output is

```text
coordinate_support_orbits={'0': 76, '1': 12, '3': 2}
same_row_exact_prolongation_dimension=520
N6_ALPHA3_INDIVIDUAL_PROLONGATION_BARRIER_PASS
```
