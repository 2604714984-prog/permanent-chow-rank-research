# Two-supported coordinate six-circuit two-jet barrier

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`, `COMPUTATION_REPLAYED`,
`STRICT_ROUTE_BARRIER`.

Let

\[
M_4=\operatorname{span}\{m_\sigma:\sigma\in S_4\}
\]

be the 24-dimensional squarefree matching-monomial space in one fixed
`4 x 4` matrix block.  This note classifies every support-minimal six-element
coordinate circuit whose six leading components each use exactly two matching
coordinates.  It proves that no regular first- or second-order lift of such a
circuit can have matching projection equal to a nonzero multiple of
`perm_4`.

The conclusion is local to this coordinate degeneration stratum.  It does not
prove

\[
\mu(6,4)\ge 7.
\]

The current unrestricted literal-block interval remains

\[
6\le \mu(6,4)\le 8.
\]

## 1. Coordinate matching graph

For `sigma in S_4`, write

\[
m_\sigma=\prod_{r=0}^3 x_{r,\sigma(r)}.
\]

Two distinct perfect matchings can lie in one six-edge coordinate Chow frame
only when they share two matrix cells.  Equivalently, their permutations
differ by a transposition.

Let `Gamma_4` be the graph on `S_4` joining such pairs.  It is the
transposition Cayley graph:

```text
vertices                         24
neighbors per vertex              6
edges                             72
```

A coordinate degree-six Chow-derived quartic has matching projection supported
on at most two vertices of `Gamma_4`.

Assume six nonzero leading matching vectors

\[
g_1^{(0)},\ldots,g_6^{(0)}\in M_4
\]

have support size exactly two, span a five-dimensional space, and have one
unique full-support relation.  Rescale their projective representatives so
that

\[
\sum_{i=1}^6 g_i^{(0)}=0.
\tag{1.1}
\]

The supports form a loopless multigraph `H` inside `Gamma_4`, with one edge for
each component.

## 2. Complete support classification

### Proposition 2.1

The support multigraph `H` has one of four forms:

1. a simple six-cycle on six matching vertices;
2. a theta graph `K_(2,3)` on five matching vertices;
3. a tight handcuff on five matching vertices; or
4. a loose handcuff on five matching vertices.

### Proof

Minimality makes `H` connected.  At every matching coordinate, equation (1.1)
contains at least two incident nonzero coefficients, so every vertex has
degree at least two.

The six columns have rank five.  Therefore the number `v` of matching
coordinates is at least five.  The total incidence degree is twelve, so
`v<=6`.

If `v=6`, every degree is exactly two and connectedness gives a six-cycle.
If `v=5`, one must classify connected loopless multigraphs with five vertices,
six edges, and minimum degree two.  There are seven abstract isomorphism
types.  Requiring every simple support edge to embed in the bipartite graph
`Gamma_4` leaves exactly the theta, tight-handcuff, and loose-handcuff types.
The exact finite enumeration is replayed in the certificate.

The row-column symmetry counts are:

```text
six-cycle orbits                         13
theta embedding orbits                    1
tight-handcuff embedding orbits           5
loose-handcuff embedding orbits          18
```

The numbers of embeddings with the first abstract vertex fixed at the identity
are respectively `48`, `216`, and `696` for theta, tight handcuff, and loose
handcuff.

## 3. Gain normal forms

The support graph does not determine the two endpoint coefficients on each
component line.  These continuous gains must be retained.

Let `e_0,...,e_4` denote the five matching-coordinate basis vectors.  After
using component-line scaling and the diagonal variable torus, the full
character-rank strata have the following normal forms.

### 3.1 Theta

\[
\begin{aligned}
c_{03}&=-e_0+e_3,&
 c_{13}&=-e_1+a e_3,&
 c_{23}&=-e_2-(1+a)e_3,\\
c_{04}&= e_0+e_4,&
 c_{14}&= e_1+b e_4,&
 c_{24}&= e_2-(1+b)e_4.
\end{aligned}
\tag{3.1}
\]

### 3.2 Tight handcuff

\[
\begin{aligned}
c_{04}^{(1)}&= e_0+e_4,&
 c_{04}^{(2)}&=-e_0+x e_4,\\
c_{13}&=e_1-e_3,&
 c_{14}&=-e_1+y e_4,\\
c_{23}&=e_2+e_3,&
 c_{24}&=-e_2-(1+x+y)e_4.
\end{aligned}
\tag{3.2}
\]

### 3.3 Loose handcuff

\[
\begin{aligned}
c_{04}^{(1)}&= e_0+e_4,&
 c_{04}^{(2)}&=-e_0+y e_4,\\
c_{13}&=e_1-e_3,&
 c_{14}&=-e_1-(1+y)e_4,\\
c_{23}^{(1)}&=e_2+x e_3,&
 c_{23}^{(2)}&=-e_2+(1-x)e_3.
\end{aligned}
\tag{3.3}
\]

Every displayed six-column sum is zero.  The open circuit conditions require
all endpoint coefficients to remain nonzero and the five-column minors not to
vanish.

The matching characters of the ambient 16-variable diagonal torus do not
always have full rank on the selected vertex set.  Exact ranks are:

```text
support type       full character rank    deficient character rank
six-cycle          9 orbits of rank 6     4 orbits of rank 5
theta              1 orbit of rank 5      none
tight handcuff     4 orbits of rank 5     1 orbit of rank 4
loose handcuff    17 orbits of rank 5     1 orbit of rank 4
```

In each deficient stratum, one extra nonzero parameter `z` scales one matching
coordinate row.  This supplies the missing torus-quotient gain.  Thus the
symbolic charts use one parameter for deficient cycles, two parameters for
full-rank five-vertex strata, and three parameters for the two deficient
handcuff strata.

## 4. Regular common-source two-jets

For component `i`, label its six coordinate factors by
`e_(i,0),...,e_(i,5)`.  Let

\[
\ell_{i,a}(t)
=x_{e_{i,a}}+t u_{i,a}+t^2v_{i,a}+O(t^3)
\]

and, for every four-subset `I` of the factor labels, let

\[
c_{i,I}(t)
=c_{i,I}^{(0)}+t d_{i,I}+t^2q_{i,I}+O(t^3).
\]

The corresponding Chow-derived quartic is

\[
G_i(t)=
\sum_{|I|=4}c_{i,I}(t)
\prod_{a\in I}\ell_{i,a}(t).
\tag{4.1}
\]

This retains the same fifteen source coefficients across every coefficient
slice of one component.  It is the local common-source interface from the
active six-block frontier.

Each component has

```text
15 source directions + 6*16 factor directions = 111 directions.
```

For six components, the first-order aggregate is

\[
L:\mathbf k^{666}\longrightarrow\operatorname{Sym}^4(\mathbf k^{16}).
\tag{4.2}
\]

Put `K=ker L`.  Polarizing the genuinely quadratic first-order contribution
gives

\[
B:K\times K\longrightarrow M_4.
\tag{4.3}
\]

Free second-order source and factor parameters contribute another copy of
`im L`.

The other twenty variables of the original `6 x 6` matrix can be omitted for
this matching-projection test.  A monomial containing one of those variables
cannot be a perfect matching of the selected `4 x 4` block, and such a
parameter cannot cancel a purely internal first-order monomial.

## 5. Two-jet barrier

### Theorem 5.1

For every support-minimal two-supported coordinate six-circuit, every gain in
the corresponding circuit locus, and every regular common-source two-jet,

\[
\boxed{
\left|
\operatorname{supp}_{M_4}
\left(\operatorname{im}L+B(K,K)\right)
\right|
\le 8.
}
\tag{5.1}
\]

More precisely:

```text
six-cycle maximum support              6
theta maximum support                  5
loose-handcuff maximum support         6
tight-handcuff maximum support         8
```

Consequently:

1. the first-order aggregate cannot be a nonzero multiple of `perm_4`; and
2. if the first-order aggregate vanishes, the second-order aggregate cannot be
   a nonzero multiple of `perm_4`.

### Proof

The matching projection of `im L` is supported on the leading matching
vertices.  A source variation remains in one six-edge frame.  A one-factor
variation changes only one edge of a perfect matching, and no distinct perfect
matching differs in exactly one edge.

At second order, the only new terms are:

1. first-source times first-factor contributions; and
2. two first-factor contributions multiplied by a base source coefficient.

The complete first-order cancellation equations are imposed in the full
quartic monomial space, not only in `M_4`.

For every support orbit and every symbolic gain chart, the exact kernel
certificate supplies a sparse rational-function basis of `K`.  The verifier
checks:

- every listed relation is in `ker L` coefficient by coefficient;
- its free-coordinate submatrix is the identity;
- one exact rational specialization has the complementary rank, proving that
  the relations form the generic kernel; and
- every polarized quadratic matching coefficient outside the stated support
  is the zero polynomial.

The identities hold on a dense open chart.  The condition that the quadratic
map vanish in the forbidden matching coordinates is closed on the
constant-rank circuit locus, so it extends to every gain in that locus.

A diagonal variable-torus transform changes the 24 coefficients of `perm_4`
but leaves every one nonzero.  Since `perm_4` has all 24 matching coordinates
nonzero, an at-most-eight-coordinate output cannot equal a nonzero torus
transform of it.  This proves the theorem.

## 6. Exact replay

The retained replay checks:

```text
abstract five-vertex multigraph types          7
embeddable support types                       3
simple six-cycle symmetry orbits              13
theta embedding orbits                         1
tight-handcuff embedding orbits                5
loose-handcuff embedding orbits               18
symbolic gain charts                           6
symbolic chart orbit rows                     28
first-order parameters per row                666
maximum two-jet matching support                8
```

The frozen symbolic certificate stores exact sparse rational functions with
integer polynomial numerators.  Its compressed and uncompressed SHA-256
digests, schema, and chart inventory are checked before use.  The written
characteristic-zero proof records the polynomial-identity argument.

The independent implementation reconstructs the equation matrices and
quadratic tables modulo `1,000,003`, and replays every named support orbit at
two deterministic generic points.  These modular evaluations are a
transcription check, not the characteristic-zero proof by themselves.

Run:

```bash
python scripts/general_quartic_two_supported_coordinate_two_jet_barrier.py \
  --json /tmp/general_quartic_two_supported_coordinate_two_jet_barrier.json.xz
python scripts/general_quartic_two_supported_coordinate_two_jet_barrier_independent.py
python -m unittest \
  tests.test_general_quartic_two_supported_coordinate_two_jet_barrier -v
```

Expected markers:

```text
GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_PASS
GENERAL_QUARTIC_TWO_SUPPORTED_COORDINATE_TWO_JET_BARRIER_INDEPENDENT_PASS
```

Frozen theorem core:

```text
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

## 7. Research consequence

The entire regular two-jet route from a support-minimal coordinate circuit
with no singleton matching component is closed.

The next coordinate boundary is no longer another two-supported gain graph.
It is the finite family in which one or two leading components have singleton
matching support, together with components whose leading matching projection
vanishes.  Only after those strata are classified is a third-order expansion
justified.

## Strict boundary

```text
two-supported coordinate support types        CLASSIFIED
two-supported gain strata                      COVERED
regular first-order perm4 lift                 IMPOSSIBLE
regular second-order perm4 lift                IMPOSSIBLE
singleton matching components                  OPEN
zero matching-projection components            OPEN
leading-dependent collision trees              OPEN
higher-order lifts                              OPEN
noncoordinate initial circuits                 OPEN
six-block literal sum                           OPEN
seven-block literal sum                         OPEN
mu(6,4)                                         OPEN IN [6,8]
unrestricted Chow-rank improvement              false
border-rank improvement                          false
literature novelty                              NOT ESTABLISHED
```
