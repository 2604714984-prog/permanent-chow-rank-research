# The coordinate equality locus at the selected `perm_8` `q=17` frontier

## Status and claim boundary

`PURE_COORDINATE_EQUALITY_THEOREM`, `EXACT_FINITE_INCIDENCE_REPLAY`,
`LOWER_78_GEOMETRIC_INTERFACE`.

The selected exact-shadow frontier for a hypothetical `77`-term
decomposition is

\[
m=4,\qquad q=17,\qquad b\le725,\qquad F_{8,4}(725)=950.
\]

This note classifies every coordinate family

\[
\mathcal A\subseteq
\binom{[8]}4\times\binom{[8]}4
\]

with

\[
|\mathcal A|=725,\qquad
|\partial_\times\mathcal A|=950.
\]

Up to independent row and column permutations and transposition, there are
exactly **three** orbit types.  The result replaces four abstract Ferrers
profiles by three explicit nested-flag constructions.

It does not classify noncoordinate equality planes, prove that seventeen Chow
terms cannot realize them, supply the missing `1,377` Koszul dimensions, or
prove ordinary lower 78.

## 1. One-dimensional extremal input

We again use the Füredi--Griggs/Mörs uniqueness theorem, as recalled in
Serra--Vena, arXiv:2304.05145, Theorem 4: when the `4`-binomial decomposition
has length smaller than four, the colex initial segment is the unique
shadow-minimizing four-uniform family up to a ground-set permutation.

The sizes used below have decompositions

\[
5=\binom54,\qquad
15=\binom64,\qquad
25=\binom64+\binom53,
\]

\[
35=\binom74,\qquad
45=\binom74+\binom53,\qquad
55=\binom74+\binom63.
\tag{1.1}
\]

All have decomposition length one or two.  Their exact minimum lower shadows
are respectively

\[
10,20,30,35,45,50.
\tag{1.2}
\]

## 2. The four compressed profiles

The exact dynamic program proves that `F_(8,4)(725)=950` has exactly four
Ferrers minimizers:

\[
(15^{45},5^{10},0^{15})
\longleftrightarrow
(55^5,45^{10},0^{55}),
\tag{2.1}
\]

and

\[
(35^5,25^{10},15^{20},0^{35})
\longleftrightarrow
(35^{15},15^{10},5^{10},0^{35}).
\tag{2.2}
\]

The arrows are partition conjugation, hence transposition of the coordinate
product family.  It is therefore enough to classify the first profile in
(2.1), called **profile A**, and the first profile in (2.2), called
**profile B**.

## 3. Profile A: two row-incidence types

Assume the row fibers have sizes

\[
(15^{45},5^{10},0^{15}).
\]

Let

\[
\mathcal H=\{R:|\mathcal A_R|=15\},
\qquad
\mathcal M=\{R:|\mathcal A_R|\ge5\}.
\]

For a lower row triple `I`, the column-shadow fiber has size at least `20` on
`partial H`, at least `10` on `partial M minus partial H`, and zero elsewhere.
Thus

\[
|\partial_\times\mathcal A|
\ge
10|\partial\mathcal H|+10|\partial\mathcal M|.
\tag{3.1}
\]

Since `|H|=45` and `|M|=55`, (1.2) gives

\[
|\partial\mathcal H|\ge45,\qquad
|\partial\mathcal M|\ge50,
\]

so the right side of (3.1) is at least `950`.  Equality forces both level
families to be one-dimensional extremal families.

For a label `z` and a five-set `W` disjoint from `z`, define

\[
\mathcal E_{45}(z,W)
=
\binom{[8]\setminus\{z\}}4
\cup
\left\{\{z\}\cup T:T\in\binom W3\right\}.
\tag{3.2}
\]

Let

\[
[8]\setminus(\{z\}\cup W)=\{a,b\}.
\]

Every extremal `45`-family is of the form (3.2).  The complete containment
classification of extremal `55`-families above it has two orbit types:

### A1 -- common apex

\[
\mathcal H=\mathcal E_{45}(z,W),
\]

\[
\mathcal M
=
\binom{[8]\setminus\{z\}}4
\cup
\left\{\{z\}\cup T:T\in\binom{W\cup\{a\}}3\right\}.
\tag{3.3}
\]

### A2 -- exchanged apex

\[
\mathcal H=\mathcal E_{45}(z,W),
\]

\[
\mathcal M
=
\binom{[8]\setminus\{a\}}4
\cup
\left\{\{a\}\cup T:T\in\binom{W\cup\{b\}}3\right\}.
\tag{3.4}
\]

Swapping `a` and `b` gives the same orbit in each case.  Exact enumeration
finds `336` nested pairs of each type, `672` in total.

For both A1 and A2:

- the Johnson graph on `H`, using common lower triples, is connected;
- the graph on `M minus H`, using triples in
  `partial M minus partial H`, is connected;
- every row in `M minus H` contains a triple from `partial H`.

Equality in (3.1) then forces all high column fibers to have one common
six-set support `V`, and all medium column fibers to have one common five-set
support `C subset V`.  Consequently

\[
\boxed{
\mathcal A
=
\left(\mathcal H\times\binom V4\right)
\cup
\left((\mathcal M\setminus\mathcal H)	imes\binom C4\right),
}
\tag{3.5}
\]

where `|V|=6` and `|C|=5`.

There are

\[
336\binom86\binom65
=336\cdot168
=56,448
\]

families of type A1 and the same number of type A2.  Thus profile A contains
`112,896` families in two `S_8 times S_8` orbits.

## 4. Profile B: one biflag type

Assume the row fibers have sizes

\[
(35^5,25^{10},15^{20},0^{35}).
\]

Define the nested level families

\[
\mathcal R_5=\{R:|\mathcal A_R|=35\},
\]

\[
\mathcal R_6=\{R:|\mathcal A_R|\ge25\},
\qquad
\mathcal R_7=\{R:|\mathcal A_R|\ge15\}.
\]

The layered shadow inequality is

\[
|\partial_\times\mathcal A|
\ge
5|\partial\mathcal R_5|
+10|\partial\mathcal R_6|
+20|\partial\mathcal R_7|.
\tag{4.1}
\]

The one-dimensional minima at level sizes `5,15,35` are `10,20,35`, so the
right side is at least

\[
5\cdot10+10\cdot20+20\cdot35=950.
\]

Equality and uniqueness force a row flag

\[
X_5\subset X_6\subset X_7\subset[8],
\qquad
|X_i|=i,
\tag{4.2}
\]

with

\[
\mathcal R_i=\binom{X_i}4
\quad(i=5,6,7).
\tag{4.3}
\]

The three row strata have sizes `5,10,20`.  Their relevant Johnson graphs are
connected, and every lower stratum shares a shadow triple with the preceding
one.  Hence equality forces one common column family at each stratum, with
nested column shadows of sizes `35,30,20`.

Choose a column five-set `W` and two labels `a,b` outside it, and put

\[
Y_7=W\cup\{a,b\}.
\]

The unique size-25 extremal family on this support has the symmetric form

\[
\mathcal B_{25}(W;a,b)
=
\binom W4
\cup
\left\{\{a\}\cup T:T\in\binom W3\right\}
\cup
\left\{\{b\}\cup T:T\in\binom W3\right\}.
\tag{4.4}
\]

Its shadow is

\[
\binom W3
\cup
\left\{\{a\}\cup P:P\in\binom W2\right\}
\cup
\left\{\{b\}\cup P:P\in\binom W2\right\},
\tag{4.5}
\]

of size `30`.  The only six-sets whose complete triple families lie in
(4.5) are

\[
W\cup\{a\}
\quad\text{and}\quad
W\cup\{b\}.
\tag{4.6}
\]

Indeed, a six-set containing both `a` and `b` would contain a forbidden
triple `{a,b,w}`.  Since it has six elements in the seven-set `Y_7`, omitting
one of `a,b` forces it to contain all of `W`.

Choose `e in {a,b}`.  The complete profile-B family is

\[
\boxed{
\begin{aligned}
\mathcal A={}&
\left(\binom{X_5}4\times\binom{Y_7}4\right)\\
&\cup
\left(\left(\binom{X_6}4\setminus\binom{X_5}4\right)
\times\mathcal B_{25}(W;a,b)\right)\\
&\cup
\left(\left(\binom{X_7}4\setminus\binom{X_6}4\right)
\times\binom{W\cup\{e\}}4\right).
\end{aligned}
}
\tag{4.7}
\]

There are

\[
8\cdot7\cdot6=336
\]

row flags and

\[
\binom87\binom75\cdot2=336
\]

column biflags.  Hence profile B contains

\[
336^2=112,896
\]

families, all in one `S_8 times S_8` orbit.

## 5. Complete coordinate theorem

### Theorem 5.1

Every coordinate family of size `725` and simultaneous lower shadow `950` is,
up to independent row and column permutations, one of:

1. profile A, common-apex type A1;
2. profile A, exchanged-apex type A2;
3. profile B, biflag type.

Their transposes give the other three oriented profiles.  Therefore:

```text
coordinate families across all four profiles = 451,584
S8 x S8 orbits                              = 6
orbits after adjoining transposition        = 3
```

### Proof

The exact Ferrers minimizer count gives the four profiles in Section 2.
Transposition reduces them to profiles A and B.  The layered inequalities
(3.1) and (4.1) force equality in every one-dimensional shadow bound and in
every local union bound.  The source-bound uniqueness theorem gives the level
families and the individual fiber families.  The explicit Johnson
connectivity statements propagate common fiber shadows across each stratum.
The nested extremal incidence classifications in Sections 3 and 4 then give
exactly A1, A2 and B.  Each displayed construction directly has `725` cells
and product shadow `950`. ∎

## 6. Exact replay

The standard-library replay

```text
scripts/general_product_shadow_n8_q17_coordinate_equality.py
```

independently enumerates:

- all `168` extremal size-45 row families;
- all `56` extremal size-55 row families;
- all `672` nested pairs and their `336/336` A1/A2 split;
- all `336` row flags for profile B;
- all `168` column flags for profile A;
- all `336` column biflags for profile B;
- the connectivity and cross-level incidence conditions for every row
  structure;
- representative full `725`-cell shadows for A1, A2 and B.

It verifies the family counts, the six oriented orbits, and the three orbits
with transposition.  The frozen payload and regression are

```text
data/general_product_shadow_n8_q17_coordinate_equality.json
tests/test_general_product_shadow_n8_q17_coordinate_equality.py
```

## 7. Consequence for lower 78

The selected `q=17` scalar frontier no longer contains arbitrary coordinate
`725`-planes.  It contains three explicit orbit types.  The next theorem must
use actual Chow geometry:

1. classify the noncoordinate closures of A1, A2 and B;
2. test whether the coupled fourth-derivative image of seventeen Chow terms
   can equal one of these planes;
3. derive at least `1,377` additional quotient-Koszul dimensions, or improve
   the realizable intersection cap from `725` to at most `703`.

The coordinate classification alone does not provide that gain.

## 8. Claim boundary

```text
coordinate_size725_shadow950_classification=COMPLETE
coordinate_family_count=451584
coordinate_S8xS8_orbits=6
coordinate_orbits_with_transpose=3
noncoordinate_equality_loci=OPEN
seventeen_Chow_term_realizability=OPEN
additional_gain_1377=NOT_PROVED
ordinary_lower_78=NOT_PROVED
border_rank_claim=false
```
