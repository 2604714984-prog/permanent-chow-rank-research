# Coordinate five-term cubic cap for `perm_8`

## Status and claim boundary

`RESTRICTED_FIXED_POINT_THEOREM`, `EXACT_FINITE_ENUMERATION`,
`FLAT_SUM_BARRIER`.

Let

\[
E_3=\mathcal D_3(\operatorname{perm}_8).
\]

For five coordinate degree-eight Chow monomials `T_1,...,T_5`, this note proves

\[
\boxed{
\dim\left(
E_3\cap
\sum_{i=1}^{5}\mathcal D_3(T_i)
\right)
\le40.
}
\tag{0.1}
\]

This is far below the general arbitrary-subspace cap 160 and the target cap
146 identified in PR #42.

The theorem is deliberately restricted to the literal sum at a torus-fixed
coordinate endpoint.  Literal derivative-space sums are not closed under
specialization: a flat limit may retain section-difference directions that are
not in the sum of the limiting termwise spaces.  Consequently (0.1) does not
prove the unrestricted five-term cap 146 or
`ChowRank(perm_8)>=80`.

Its mathematical value is to isolate the remaining obstruction.  Any
compactified degeneration preserving a 147-dimensional permanent-relative
intersection must carry at least 107 permanent directions outside the endpoint
literal sum.

## 1. Coordinate Chow terms as sparse bipartite graphs

A coordinate degree-eight Chow monomial has the form

\[
T=\prod_{e\in[8]\times[8]}x_e^{m_e},
\qquad
\sum_em_e=8.
\]

Let

\[
G(T)=\{e:m_e>0\}
\]

be its support graph.  It is a bipartite graph with at most eight edges.
Repeated factors do not help cover a squarefree perfect-matching monomial.

The cubic derivative space `D_3(T)` is a coordinate monomial space.  A
squarefree three-edge matching monomial belongs to it if and only if all three
edges lie in `G(T)`.

For row and column triples `R,C`, the basis vector

\[
p_{R,C}=\operatorname{perm}(x_{ij})_{i\in R,j\in C}
\]

is the sum of the six perfect-matching monomials of `K_(R,C)`.  Since the
literal sum of coordinate Chow derivative spaces is itself a coordinate
monomial space,

\[
p_{R,C}\in\sum_i\mathcal D_3(T_i)
\]

if and only if every one of its six matching monomials occurs in at least one
support graph `G(T_i)`.

Thus the coordinate intersection dimension is exactly the number of `3 x 3`
rectangles whose six matchings are covered by the five graphs.

## 2. A graph with eight edges supports at most eight repeated rectangles

For a bipartite graph `G`, let `p_(R,C)` be the number of perfect matchings in
its induced `3 x 3` rectangle and define

\[
P(G)=
\sum_{R,C}\binom{p_{R,C}}2.
\tag{2.1}
\]

Every rectangle with at least two matchings contributes at least one to
`P(G)`, so their number is at most `P(G)`.

### Proposition 2.1

If `G` has at most eight edges, then

\[
\boxed{P(G)\le8.}
\tag{2.2}
\]

Consequently `G` has at most eight `3 x 3` rectangles with at least two
perfect matchings.

### Exact exhaustion proof

Adding edges cannot decrease `P(G)`, so it suffices to consider exactly eight
edges.  If `P(G)=0`, there is nothing to prove.  Otherwise choose one pair of
perfect matchings on the same row and column triples.

Two permutations in `S_3` have only two possible union types.

1. **They share one edge.**  Their union is a four-cycle plus a disjoint edge,
   containing five edges.  Up to independent row and column relabelling this
   is one fixed graph `H_5`.  The remaining three edges can be chosen in

   \[
   \binom{64-5}{3}=\binom{59}{3}=32509
   \]

   ways.  Exact enumeration gives the pair-count histogram

   ```text
   P=1:  1,700
   P=2:  8,950
   P=3: 14,420
   P=4:  6,920
   P=5:    200
   P=6:    294
   P=8:     25
   ```

   and maximum eight.

2. **They are disjoint.**  Their union is a six-cycle, containing six edges.
   Up to relabelling this is one fixed graph `H_6`.  The remaining two edges
   have

   \[
   \binom{64-6}{2}=\binom{58}{2}=1653
   \]

   choices.  The exact histogram is

   ```text
   P=1: 1,455
   P=3:    30
   P=4:    90
   P=5:    75
   P=6:     3
   ```

   and maximum six.

The two cases exhaust every graph with `P(G)>0`, proving (2.2).  The maximum
is attained by two disjoint `K_(2,2)` components.  Each four-cycle combines
with each of the four edges of the other component, giving eight distinct
rectangles with exactly two matchings.

The enumeration uses edge subsets only; it is not a random graph search or an
unlabelled-isomorphism heuristic.

## 3. Five coordinate terms cover at most forty permanent basis vectors

Suppose a rectangle is covered by five support graphs.  Its six perfect
matchings are assigned to five graphs, so by the pigeonhole principle one
graph contains at least two of them.  Charge the rectangle to one such graph.

By Proposition 2.1, each graph receives at most eight charges.  Therefore the
number of covered rectangles is at most

\[
5\cdot8=40.
\]

The subpermanents `p_(R,C)` have disjoint row-column weights and are linearly
independent.  This proves (0.1).

## 4. Quantitative flat-sum gap

PR #42 identifies 146 as the five-term cap sufficient for lower 80, while the
arbitrary-subspace recursive shadow cap is 160.  The coordinate endpoint
literal sum is much smaller:

```text
arbitrary-subspace cap=160
required Chow-realizable cap=146
coordinate literal-sum cap=40.
```

Suppose a proper compactification preserves a permanent-relative `h`-plane
while the five Chow terms specialize to coordinate monomials.  At the endpoint,
at most forty dimensions of that `h`-plane can lie in the literal sum of the
limiting derivative spaces.  Hence at least

\[
h-40
\]

dimensions must be carried by nonliteral flat-sum or section-difference data.
For the first excluded target `h=147`, this is

\[
\boxed{107}
\]

dimensions.

This explains why a fixed-point classification of the limiting terms alone
cannot prove the general cap.  The next theorem must control valuation-leading
relation packets, flat sums, or complete-collineation data.

## 5. Evidence

The exact standard-library replay is

```text
scripts/n8_coordinate_five_term_cubic_cap.py
```

with frozen result

```text
data/n8_coordinate_five_term_cubic_cap.json.
```

It enumerates all 32,509 shared-edge extensions and all 1,653 disjoint-pair
extensions, independently counts three-edge matchings by their row/column
vertex sets, and records both matching-pair and multi-rectangle histograms.

The theorem-facing core is bound by

```text
194ad847df5d43e122a6a702c6594648ad9f1194dd6f93ec75d47f86d7da5e89
```

## 6. Unproved items

```text
general five-term cubic cap <=146=OPEN
flat-sum extra-direction cap=OPEN
valuation-tree classification=OPEN
perm_8 lower 80=OPEN
exact perm_8 rank=OPEN
border-rank consequence=NO
```
