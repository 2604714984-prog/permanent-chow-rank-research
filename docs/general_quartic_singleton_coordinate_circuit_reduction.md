# Positive-singleton coordinate six-circuits and the universal two-jet envelope

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`, `COMPUTATION_REPLAYED`,
`STRICT_ROUTE_BARRIER`.

This note continues the coordinate degeneration program for the active
six-block frontier

\[
6\le \mu(6,4)\le 8.
\]

The prior two-supported theorem treats support-minimal rank-five six-circuits
whose six leading matching projections are all supported on exactly two
perfect matchings. Here one or two components are allowed to have singleton
matching support. The two unused degree-six coordinate factors in a singleton
component are retained, including repeated factors and reuse of a matching
cell.

The result is:

1. every positive-singleton support-minimal coordinate six-circuit belongs to
   one of three exact support families;
2. all 130 repeated-factor singleton frames are included;
3. every regular second-order common-source lift has matching support at most
   23; and therefore
4. no such lift can equal a nonzero diagonal-torus transform of `perm_4`, whose
   matching support is 24.

Combined with the previous two-supported theorem, this closes every regular
coordinate six-circuit two-jet for which all six leading matching projections
are nonzero.

It does **not** cover a component whose leading matching projection is zero,
prove `mu(6,4)>=7`, or improve unrestricted Chow rank or border rank.

## 1. Matching graph and support columns

Let

\[
M_4=\operatorname{span}\{m_\sigma:\sigma\in S_4\}
\]

be the 24-dimensional perfect-matching monomial space in one fixed `4 x 4`
block. Two matching coordinates can occur in the same six-cell coordinate
frame exactly when the corresponding permutations differ by a transposition.
Thus two-supported component lines are edges of the transposition Cayley graph
`Gamma_4` on `S_4`.

Consider six nonzero leading matching vectors

\[
c_1,\ldots,c_6\in M_4
\]

such that:

- every `c_i` has support size one or two;
- their span has dimension five; and
- their unique relation has full support.

Rescale the six columns so that

\[
c_1+\cdots+c_6=0.
\tag{1.1}
\]

A support coordinate appearing in only one column could not cancel in (1.1).
Therefore every used matching coordinate occurs in at least two columns.

## 2. Incidence reduction

Let `s` be the number of singleton columns and let `v` be the number of used
matching coordinates. The total support incidence is

\[
12-s.
\]

Every used coordinate occurs at least twice, while rank five forces at least
five used coordinates. Hence

\[
10\le 2v\le 12-s.
\tag{2.1}
\]

Consequently:

\[
\boxed{s\le2}.
\tag{2.2}
\]

If `s` is one or two, equation (2.1) also forces

\[
\boxed{v=5}.
\tag{2.3}
\]

Thus the positive-singleton problem is a finite five-vertex support problem.

## 3. Complete support classification

### 3.1 Two singleton columns

The four two-supported columns form a simple graph on the five matching
vertices. Every non-singleton vertex must still have total incidence at least
two, and the two singleton vertices must each be incident to a pair edge.
Connectedness and the exact degree sum force a four-edge path, with singleton
columns at its endpoints.

The unique abstract type is therefore:

```text
endpoint-marked P5
```

### 3.2 One singleton column

The five pair supports form a connected multigraph on five vertices with one
marked vertex carrying the singleton. The degree constraints leave four
abstract types:

```text
marked C5
triangle tail
square lollipop
double-edge tail
```

The transposition Cayley graph is bipartite by permutation parity. The marked
five-cycle and triangle-tail types contain odd cycles and cannot embed.
Exactly two types survive:

```text
square lollipop
double-edge tail
```

### 3.3 Symmetry counts

Exact row-column orbit counts are:

```text
square lollipop       5
double-edge tail     29
endpoint-marked P5   18
```

With the first abstract matching vertex fixed to the identity, the embedding
counts are respectively `216`, `888`, and `696`.

The classification can be summarized as

\[
\boxed{
\begin{array}{c|c}
\text{singleton count}&\text{support type}\\ \hline
1&\text{square lollipop or double-edge tail}\\
2&\text{endpoint-marked }P_5\\
\ge3&\text{impossible}
\end{array}}
\tag{3.1}
\]

## 4. Exact circuit normal forms

Let `e_0,...,e_4` be the five matching-coordinate basis vectors. Component-line
rescaling reduces the three support families to the following forms.

### 4.1 Endpoint-marked path

\[
\begin{aligned}
c_1&=e_0,&
 c_2&=-e_0+e_1,&
 c_3&=-e_1+e_2,\\
c_4&=-e_2+e_3,&
 c_5&=-e_3+e_4,&
 c_6&=-e_4.
\end{aligned}
\tag{4.1}
\]

There is no continuous gain parameter.

### 4.2 Square lollipop

\[
\begin{aligned}
c_1&=-e_3,&
 c_2&=e_2+e_3,&
 c_3&=e_0-e_2,\\
c_4&=e_0+a e_1,&
 c_5&=-e_0-(1+a)e_1,&
 c_6&=e_1+e_2.
\end{aligned}
\tag{4.2}
\]

### 4.3 Double-edge tail

\[
\begin{aligned}
c_1&=e_4,&
 c_2&=-e_3+e_4,&
 c_3&=e_0+e_3,\\
c_4&=-e_0+e_1,&
 c_5&=-e_1+a e_2,&
 c_6&=e_1-(1+a)e_2.
\end{aligned}
\tag{4.3}
\]

For the one-parameter families, support-minimality is equivalent to

\[
a\ne0,-1.
\tag{4.4}
\]

All five-column minors are units up to sign and the factors `a`, `1+a`.

## 5. Singleton coordinate frames with repetition

Fix one leading matching `M_0`. A coordinate degree-six frame producing a
singleton matching component contains the four cells of `M_0` and two further
coordinate factors.

The two unused factors form an unordered multiset of size two from all sixteen
matrix cells. Therefore there are

\[
\binom{16+2-1}{2}=136
\tag{5.1}
\]

possibilities. This count includes:

- two equal unused factors;
- one or two unused factors equal to cells of `M_0`; and
- two distinct off-matching cells.

Exactly six multisets are the two missing cells of another perfect matching
which shares two cells with `M_0`; those frames are two-supported rather than
singleton. Hence the exact singleton-frame count is

\[
\boxed{136-6=130}.
\tag{5.2}
\]

Their distinct-cell support sizes are distributed as

```text
four cells      10
five cells      60
six cells       60
```

Under the diagonal stabilizer of `M_0`, the 130 frames form ten orbits of sizes

```text
4, 6, 12, 12, 12, 12, 12, 12, 24, 24.
```

After additionally rooting one adjacent transposition edge, the 780 rooted
configurations form 41 orbits. The full theorem enumeration uses all 130
frames directly; the orbit counts are an independent compression check.

## 6. First-order barrier

Let a coordinate frame have leading matching support `S`, of size one or two.
At first order:

1. varying the common-source coefficients can produce only matching monomials
   already contained in the frame; and
2. varying one coordinate factor in a leading matching retains three of its
   four cells.

Two distinct permutations cannot agree on exactly three rows: agreement on
three rows forces agreement on the fourth. Thus one factor variation cannot
turn a perfect matching into a different perfect matching.

Every positive-singleton circuit above uses exactly five matching coordinates.
Therefore the first-order matching projection has support at most five and
cannot equal `perm_4`.

## 7. Universal second-order matching envelope

The full first-order kernel does not need to be eliminated explicitly. There
is a stronger termwise support bound.

Let `E` be the distinct coordinate-cell support of one degree-six frame, and
let `S` be its leading matching support. Define

\[
\mathcal E(E,S)=
\{M:|M\cap E|\ge3\}
\cup
\{M:\exists M_0\in S,\ |M\cap M_0|\ge2\}.
\tag{7.1}
\]

### Lemma 7.1

Every matching monomial appearing in a regular second-order common-source lift
of the component lies in `E(E,S)`.

### Proof

The second-order terms have four sources:

1. **free second-source directions:** four frame factors remain, so the
   matching lies in the frame;
2. **first-source times first-factor directions:** three unchanged frame
   factors remain, giving `|M cap E|>=3`;
3. **one second-factor direction:** three cells of a leading matching remain;
4. **two first-factor directions:** two cells of a leading matching remain.

These are exactly the two sets in (7.1). The statement is termwise. Imposing
first-order cancellation can delete coefficients but cannot create a matching
outside the envelope. QED.

## 8. Exhaustive exact maxima

For every row-column support orbit and every valid repeated-factor singleton
frame, compute the union of the six component envelopes.

The complete distributions are:

```text
square lollipop
  decorated configurations    5 * 130 = 650
  support histogram            19:124, 20:254, 21:260, 22:12
  maximum                      22

double-edge tail
  decorated configurations   29 * 130 = 3770
  support histogram            19:744, 20:2020, 21:970, 22:36
  maximum                      22

endpoint-marked P5
  decorated configurations   18 * 130^2 = 304200
  support histogram            19:61504, 20:128996, 21:105120,
                               22:8472, 23:108
  maximum                      23
```

Therefore

\[
\boxed{
\max\left|
\bigcup_{i=1}^6\mathcal E(E_i,S_i)
\right|=23<24.
}
\tag{8.1}
\]

Every coefficient of `perm_4`, and of every nonzero diagonal row-column torus
transform of `perm_4`, is nonzero on all 24 matching coordinates. Hence no
regular positive-singleton coordinate two-jet can produce the target.

## 9. Combined coordinate consequence

The prior theorem closes support size pattern

```text
2,2,2,2,2,2.
```

This theorem closes every positive-singleton pattern

```text
1,2,2,2,2,2
1,1,2,2,2,2.
```

Three or more singleton components are impossible. Thus:

\[
\boxed{
\text{every regular coordinate six-circuit two-jet with six nonzero}
\atop
\text{leading matching projections is incompatible with }\operatorname{perm}_4.
}
\tag{9.1}
\]

The exact next coordinate boundary is a component whose leading matching
projection is zero.

## 10. Deterministic replay

The primary implementation verifies the incidence classification, exact normal
forms, full row-column orbit enumeration, all 130 repeated-factor singleton
frames, the stabilizer orbit counts, and every decorated second-order envelope.

The independent implementation imports none of the primary helpers. It
reconstructs the transposition graph, support embeddings, repeated frames, and
all envelope histograms.

Run:

```bash
python scripts/general_quartic_singleton_coordinate_circuit_reduction.py \
  --json /tmp/general_quartic_singleton_coordinate_circuit_reduction.json
python scripts/general_quartic_singleton_coordinate_circuit_reduction_independent.py
python -m unittest \
  tests.test_general_quartic_singleton_coordinate_circuit_reduction -v
```

Expected markers:

```text
GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_PASS
GENERAL_QUARTIC_SINGLETON_COORDINATE_CIRCUIT_REDUCTION_INDEPENDENT_PASS
```

Frozen theorem core:

```text
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

## Strict boundary

```text
positive-singleton support families             CLASSIFIED
repeated-factor singleton frames                 INCLUDED
positive-singleton regular first-order lifts     CLOSED
positive-singleton regular second-order lifts    CLOSED
all-positive coordinate regular two-jets         CLOSED
zero leading matching projection                 OPEN
noncoordinate initial circuits                   OPEN
leading-dependent collision trees                OPEN
higher-order lifts                               OPEN
six-block literal sum                            OPEN
seven-block literal sum                          OPEN
mu(6,4)                                          OPEN IN [6,8]
unrestricted Chow-rank improvement               false
border-rank improvement                           false
literature novelty                               NOT ESTABLISHED
```
