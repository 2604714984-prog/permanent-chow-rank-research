# The coordinate equality locus at the `perm_8` exact-shadow threshold

## Status and claim boundary

`PURE_COORDINATE_EQUALITY_THEOREM`, `EXACT_FINITE_REPLAY`,
`CHOW_REALIZABILITY_INTERFACE`.

This note classifies every **coordinate** family

\[
\mathcal A\subseteq
\binom{[8]}4\times\binom{[8]}4
\]

with

\[
|\mathcal A|=560,
\qquad
|\partial_\times\mathcal A|=784.
\]

Equivalently, it classifies the coordinate `560`-planes in
`D_4(perm_8)` attaining the exact minimum first-derivative shadow from
`docs/general_exact_product_shadow.md`.

It does not classify the noncoordinate equality locus, prove that a coupled
sum of fourteen Chow terms cannot attain the equality family, improve the
ordinary lower bound beyond `77`, or make a border-rank claim.

## 1. External one-dimensional equality input

We use the classical uniqueness case of the Kruskal--Katona theorem:

> If a `k`-uniform family has cardinality whose `k`-binomial decomposition
> has length strictly smaller than `k`, then the colex initial segment is the
> unique shadow-minimizing family up to a permutation of the ground set.

This is the Füredi--Griggs/Mörs uniqueness theorem, recalled as Theorem 4 in

- Oriol Serra and Lluís Vena, *Extremal families for the
  Kruskal--Katona theorem*, arXiv:2304.05145.

Only the following two single-binomial instances are used:

\[
|\mathcal H|=\binom74=35,
\quad
|\partial\mathcal H|=\binom73=35
\Longrightarrow
\mathcal H=\binom U4
\quad(|U|=7),
\tag{1.1}
\]

and

\[
|\mathcal B|=\binom64=15,
\quad
|\partial\mathcal B|=\binom63=20
\Longrightarrow
\mathcal B=\binom V4
\quad(|V|=6).
\tag{1.2}
\]

Both binomial decompositions have length one, strictly less than four.
No more general equality classification is imported.

## 2. The flag families

For a row label `z in [8]`, put

\[
U=[8]\setminus\{z\},
\qquad
\mathcal H_z=\binom U4,
\qquad
\mathcal L_z=\{R\in\tbinom{[8]}4:z\in R\}.
\]

Choose a six-set `V subset [8]` in the column ground set and a four-set
`C_0 subset V`.  Define

\[
\boxed{
\mathcal F(z,V,C_0)
=
\left(\mathcal H_z\times\binom V4\right)
\cup
\left(\mathcal L_z\times\{C_0\}\right).
}
\tag{2.1}
\]

Its size is

\[
35\cdot15+35=560.
\tag{2.2}
\]

For a lower row triple `I` not containing `z`, the four high rows above `I`
give the complete column triple family `binom(V,3)`, while the unique low
row contributes `partial{C_0} subset binom(V,3)`.  Hence that shadow fiber
has size `20`.  For a lower row triple containing `z`, all five rows are low
and contribute the same four-set `C_0`, so the fiber has size `4`.  Therefore

\[
|\partial_\times\mathcal F(z,V,C_0)|
=\binom73\cdot20+\binom72\cdot4
=35\cdot20+21\cdot4
=784.
\tag{2.3}
\]

## 3. Row-size profile forced by exact Ferrers minimization

Let `a_R=|\mathcal A_R|` be the column-fiber size of a coordinate family.
Row-fiber colex compression preserves every `a_R`.  After this first
compression, column `j` has height

\[
h_j=|\{R:a_R>j\}|.
\]

Compressing each column to an initial row segment produces a Ferrers diagram
whose row partition is exactly the decreasing rearrangement of the multiset
`{a_R}`.

At size `560`, the exact dynamic program gives exactly two Ferrers minimizers.
The cell-weight conjugation theorem in
`docs/general_product_shadow_cell_weights.md` identifies them as

\[
\lambda=(15^{35},1^{35})
\tag{3.1}
\]

and

\[
\lambda'=(70,35^{14},0^{55}).
\tag{3.2}
\]

They are conjugate.  Transposing the product family exchanges the two
profiles.  Hence, after a possible transpose, every coordinate equality
family has precisely thirty-five row fibers of size `15` and thirty-five row
fibers of size `1`.

## 4. A sharp row-profile inequality

Assume from now on that the row profile is `(15^35,1^35)`.  Let

\[
\mathcal H=\{R:|\mathcal A_R|=15\}
\]

be the family of high rows.  For each lower row triple `I`, let

\[
\mathcal U_I
=
\bigcup_{R\supset I}\partial\mathcal A_R
\]

be its column-shadow fiber.

If `I in partial H`, at least one high row contains `I`; by
Kruskal--Katona, its fifteen-set fiber has shadow at least `20`, so

\[
|\mathcal U_I|\ge20.
\]

If `I notin partial H`, all five rows containing `I` are low singleton
fibers.  The shadow of any one singleton four-set has size four, so

\[
|\mathcal U_I|\ge4.
\]

Therefore

\[
\begin{aligned}
|\partial_\times\mathcal A|
&=\sum_{I\in\binom{[8]}3}|\mathcal U_I|\\
&\ge20|\partial\mathcal H|
+4\left(56-|\partial\mathcal H|\right)\\
&=224+16|\partial\mathcal H|.
\end{aligned}
\tag{4.1}
\]

Since `|H|=35`, ordinary Kruskal--Katona gives

\[
|\partial\mathcal H|\ge35.
\tag{4.2}
\]

Thus (4.1) independently recovers the lower bound `784`.  Equality forces
simultaneous equality in every step:

1. `|partial H|=35`;
2. every high fifteen-set fiber has shadow exactly `20`;
3. `|U_I|=20` for `I in partial H`;
4. `|U_I|=4` for `I notin partial H`.

## 5. Classification of the equality case

### Theorem 5.1 -- coordinate flag classification

If

\[
|\mathcal A|=560,
\qquad
|\partial_\times\mathcal A|=784,
\]

then, up to independent permutations of the row and column ground sets and
up to transposition,

\[
\boxed{
\mathcal A=\mathcal F(z,V,C_0)
}
\]

for a row label `z`, a column six-set `V`, and a column four-set
`C_0 subset V`.

### Proof

After a possible transpose, Section 3 gives the row profile
`(15^35,1^35)`.

By equality in (4.2) and the uniqueness input (1.1), there is a seven-set
`U` such that

\[
\mathcal H=\binom U4.
\tag{5.1}
\]

Let `z` be the unique row label outside `U`.  The low rows are exactly

\[
\mathcal L_z=\{R:z\in R\}.
\]

For a low row `R`, write its singleton column fiber as

\[
\mathcal A_R=\{C_R\}.
\]

Take a lower row triple `I` containing `z`.  All five rows above `I` are low.
Equality gives `|U_I|=4`, while each `partial{C_R}` already has size four.
Hence all five shadows `partial{C_R}` are equal, and therefore all five
four-sets `C_R` are equal.  The Johnson graph on the low rows, identified
with `binom(U,3)` and adjacency by sharing a lower triple containing `z`, is
connected.  Consequently

\[
C_R=C_0
\quad\text{for every low row }R.
\tag{5.2}
\]

Now take a high row `R`.  Equality in its one-dimensional shadow bound and
(1.2) give a six-set `V_R` such that

\[
\mathcal A_R=\binom{V_R}4,
\qquad
\partial\mathcal A_R=\binom{V_R}3.
\tag{5.3}
\]

Fix a lower row triple `I subset U`.  Exactly four high rows and one low row
contain `I`.  The four high shadows in (5.3) each have size twenty, while
equality gives `|U_I|=20`.  Hence all four high shadows are equal.  A six-set
is determined by its three-subsets, so their `V_R` are equal.  The Johnson
graph on `binom(U,4)`, with adjacency by a common three-subset, is connected;
therefore a single six-set `V` satisfies

\[
V_R=V
\quad\text{for every high row }R.
\tag{5.4}
\]

For the same `I`, the low contribution `partial{C_0}` is contained in the
common twenty-element family `binom(V,3)`.  Hence every three-subset of
`C_0` lies in `V`, which forces

\[
C_0\subset V.
\tag{5.5}
\]

Equations (5.1)--(5.5) are exactly the flag form (2.1). ∎

## 6. Orbit and enumeration consequences

The parameters are uniquely recoverable from the family:

- `z` is the common row label of all low rows;
- `V` is the support of any high column fiber;
- `C_0` is the common low singleton.

Thus there are exactly

\[
8\binom86\binom64
=8\cdot28\cdot15
=3360
\tag{6.1}
\]

families in the orientation `(15^35,1^35)`, and another `3360` transposes.
The group `S_8 times S_8` is transitive on each orientation; adjoining
transposition gives one orbit.

The exact standard-library replay in

```text
scripts/general_product_shadow_n8_coordinate_equality.py
```

enumerates all `3360` parameter triples, reconstructs each family and its
simultaneous shadow, checks the values `560/784`, verifies parameter
injectivity, and verifies the single-orbit normalization.

## 7. Consequence for the general-`n` program

The abstract coordinate obstruction at the `perm_8` lower-77 threshold is no
longer an unstructured `560`-set.  It is one flag orbit:

\[
\left(\binom U4\times\binom V4\right)
\cup
\left(\mathcal L_z\times\{C_0\}\right),
\qquad
|U|=7,\ |V|=6,\ C_0\subset V.
\]

The next valid question is geometric rather than another scalar dynamic
program:

1. classify the noncoordinate equality locus specializing to this orbit;
2. determine whether a coupled sum of fourteen Chow terms can realize the
   corresponding permanent-relative `560`-plane;
3. if realization is possible, compute the next derivative shadow or the
   coupled relation-module defect forced by the flag.

A negative answer to step 2, or a positive extra defect in step 3, would
improve the lower bound beyond `77`.

## 8. Claim boundary

```text
coordinate_size560_shadow784_classification=COMPLETE
coordinate_orientations=2
coordinate_orbits_with_transpose=1
coordinate_family_count_per_orientation=3360
noncoordinate_equality_locus=OPEN
fourteen_Chow_term_realizability=OPEN
perm8_lower_78=NOT_PROVED
perm8_exact_rank=OPEN
border_rank_claim=false
```
