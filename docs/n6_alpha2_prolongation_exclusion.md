# Prolongation excludes the all-`alpha=2` state

**Status.** `PURE_PROJECTIVE_FIXED_POINT_REDUCTION`,
`EXACT_INTEGER_UPPER_CERTIFICATE`, `SCALAR_STATE_EXCLUDED` (N6-049).
The base field is algebraically closed of characteristic zero.  This note
excludes only the N6-041 state `b61_state_072`; it does not by itself exclude
the other `b=61` states or prove `ChowRank(perm_6)>=27`.

## 1. The state and its required prolongation

In `b61_state_072` all six pairs are

\[
 (\varepsilon_i,\alpha_i)=(0,2).
\tag{1.1}
\]

Thus each quadratic derivative space `F_i` has dimension fifteen and

\[
 \dim(E_2\cap F_i)=1,
 \qquad \dim q(F_i)=14.
\tag{1.2}
\]

The global quotient dimension is also `t_2=14`.  Since `F_i\subseteq H_2`,
(1.2) gives

\[
 q(F_i)=q(H_2),
 \qquad E_2+F_i=E_2+H_2=:A.
\tag{1.3}
\]

As before, `E_3+H_3\subseteq A^{(1)}`.  Here `h=120` and `b=61`, so

\[
 \boxed{\dim A^{(1)}\ge400+120-61=459.}
\tag{1.4}
\]

## 2. Projective fixed-point reduction

Take any actual term satisfying (1.2).  Its factor span has dimension at
least five because `dim F=15`.  Choose an auxiliary six-plane `L` containing
that factor span, so that `F subset Sym^2 L`, and put `A=E_2+F`, a
239-plane.  Take the closure of all resulting triples `(L,F,A)` in the
corresponding product of Grassmannians.  This construction includes both the
five-span and the six-span terms.  The containments and rank condition

\[
 F\subseteq\operatorname{Sym}^2L,
 \qquad E_2+F\subseteq A,
 \qquad \dim(E_2\cap F)\ge1
\tag{2.1}
\]

are closed Grassmannian incidences.  This closure is projective and stable
under the row-column torus.  The kernel dimension `dim A^(1)` is upper
semicontinuous.  Its maximum therefore occurs at a torus-fixed triple.

At such a triple the auxiliary `L` is a coordinate six-edge bipartite graph.
The specialized nonzero line `E_2\cap F` lies in
`E_2\cap\operatorname{Sym}^2L`, so the graph contains a rectangle.

### Lemma 2.1

A six-edge bipartite graph having a rectangle has exactly one or exactly
three rectangles.  In the latter case it is `K_(2,3)` or `K_(3,2)`.

#### Proof

If there are two distinct rectangles, they cannot be edge-disjoint, since
their union would have eight edges.  If they share exactly one edge their
union has seven edges.  They cannot share two opposite edges, and sharing
three edges would make them equal.  Hence they share two adjacent edges.
Their six-edge union is `K_(2,3)` or `K_(3,2)`, which contains the third
rectangle.  A six-edge graph cannot contain anything else.  \(\square\)

If the fixed graph has three rectangles, put

\[
 r=\dim(E_2\cap F).
\]

The universal six-plane bound gives `1<=r<=3`.  Hence `q(F)` has dimension
`15-r`, namely fourteen, thirteen, or twelve.  The fixed fourteen-plane
`A/E_2` contains it and adds respectively zero, one, or two arbitrary
ambient quotient axes.  Thus all three possibilities are exactly the
`t=14` fixed incidences enumerated in N6-047.  Its uniform cap gives

\[
 \dim A^{(1)}\le448.
\tag{2.2}
\]

It remains to bound the one-rectangle case.

## 3. Classification of the one-rectangle supports

Mark the unique rectangle and move it to

\[
 \{(0,0),(0,1),(1,0),(1,1)\}.
\]

The remaining two edges are outside this rectangle.  The stabilizer

\[
 S_2\times S_4\times S_2\times S_4
\]

acts on their choices.  Exact orbit enumeration gives twelve support
shapes.  The 488 marked choices represent all 109800 labelled six-edge
graphs with exactly one rectangle: every such graph has a unique marking.

For any of these supports, `dim(E_2 cap Sym^2 L)=1`.  Consequently the fixed
limit still has

\[
 E_2\cap F=E_2\cap\operatorname{Sym}^2L,
 \qquad A=E_2+F.
\]

The quotient `q(Sym^2L)` has twenty one-dimensional torus weight axes:
twenty-one quadratic monomials minus the one rectangle relation.  Hence a
fixed `A/E_2` is an arbitrary fourteen-axis subset.  There are

\[
 {20\choose14}=38760
\tag{3.1}
\]

possibilities for each of the twelve support shapes.

## 4. Exact coefficient-component cap

For every fixed `A`, the replay constructs all cubic coefficient constraints
defining `A^(1)`.  A missing square, same-row, or same-column quotient axis
forces the corresponding derived coefficients to zero.  A missing rectangle
axis equates the two opposite-diagonal coefficients, with their nonzero
derivative multiplicities.  Forgetting those multiplicities can only remove
cycle-consistency equations; thus the number of surviving connected
components is a rigorous characteristic-zero upper bound.

The twelve support-shape maxima are

\[
 453,443,445,442,442,442,453,443,442,435,435,435.
\tag{4.1}
\]

Therefore every fixed point in the one-rectangle branch satisfies

\[
 \dim A^{(1)}\le453.
\tag{4.2}
\]

Combining (2.2), (4.2), and the projective maximum argument gives:

### Theorem 4.1 -- universal `alpha=2` cap

For every actual degree-six Chow term with
`(epsilon,alpha)=(0,2)`, putting `F=D_2(T)` gives

\[
 \boxed{\dim(E_2+F)^{(1)}\le453.}
\tag{4.3}
\]

This includes both five- and six-dimensional factor spans.

In `b61_state_072`, the quotient of every `F_i` already has the full global
dimension fourteen, so `E_2+F_i=E_2+H_2`.  Thus (4.3) contradicts (1.4) and
proves:

### Corollary 4.2

The scalar state `b61_state_072`, in which all six fixed terms have
`(epsilon_i,alpha_i)=(0,2)`, is impossible.

This conclusion does not by itself remove any other `b=61` state, exclude a
hypothetical 26-term decomposition, prove `ChowRank(perm_6)>=27`, or assert a
border-rank lower bound.

## 5. Replay

Run

```text
python scripts/n6_alpha2_prolongation_exclusion.py \
  --json data/n6_alpha2_prolongation_exclusion.json
python -m unittest tests/test_n6_alpha2_prolongation_exclusion.py -v
```

Expected output includes

```text
one_rectangle_support_orbits=12
one_rectangle_cap=453
all_alpha2_required=459
N6_ALPHA2_PROLONGATION_EXCLUSION_PASS
```
