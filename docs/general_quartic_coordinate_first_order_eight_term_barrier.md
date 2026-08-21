# Coordinate regular first-order lifts require eight quartic components

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`, `STRICT_ROUTE_THEOREM`.

This note proves:

\[
\boxed{
q\le 7
\quad\Longrightarrow\quad
[\varepsilon]\sum_{i=1}^{q} g_i(\varepsilon)
\notin
\mathbf k^*\operatorname{perm}_4
}
\tag{0.1}
\]

for every regular first-order family in which each \(g_i(\varepsilon)\) is an
output-degree-four derivative of a degree-six Chow term and the limiting six
factors are matrix coordinate variables in one \(4\times4\) block.

Repeated coordinate factors, internal source-kernel cancellation, arbitrary
first-order factor motions, and arbitrary first-order source motion are all
allowed.

Equivalently, the coordinate regular first-order term count is at least eight.

This is not an unrestricted six- or seven-block zero theorem. It does not
exclude noncoordinate initial frames, singular or multigrade valuation trees,
or a first nonzero coefficient of order at least two. Consequently it does not
change

\[
6\le \mu(6,4)\le 8
\]

or the current unrestricted Chow-rank interval for \(\operatorname{perm}_6\).

## 1. Coordinate source model

For one component let \(F\) be the six-dimensional factor-label space with
labels \(1,\dots,6\). At the limiting coordinate frame write

\[
\ell_a(0)=x_{\gamma_a},
\qquad
\gamma_a\in[4]\times[4],
\]

where the cells \(\gamma_a\) may repeat. The squarefree factor-label source is

\[
\operatorname{Sq}^4(F)
=
\operatorname{span}\{s_I: I\subset[6],\ |I|=4\}.
\]

The coordinate specialization map is

\[
\Phi_\gamma(s_I)
=
\prod_{a\in I}x_{\gamma_a}.
\tag{1.1}
\]

Allowing an arbitrary source vector in this 15-dimensional space is an upper
envelope for the actual Chow derivative space. Therefore a zero theorem in
this enlarged source model remains valid for actual degree-six Chow
derivatives.

Put

\[
A_\gamma=\{\gamma_1,\dots,\gamma_6\},
\]

as a set when intersections with perfect matchings are taken, while retaining
the multiplicities of the six labels for source-kernel calculations.

Let \(\mathcal M\) be the 24 perfect matchings of \(K_{4,4}\).

## 2. Three matching sets attached to one frame

### 2.1 Full first-order envelope

A perfect matching created after moving at most one factor must retain three
unchanged coordinate factors. Hence define

\[
E(\gamma)
=
\{M\in\mathcal M: |M\cap A_\gamma|\ge3\}.
\tag{2.1}
\]

Every matching monomial in the first derivative of the component belongs to
\(E(\gamma)\).

### 2.2 Direct source motion

First-order motion of the source vector, with the coordinate frame fixed, can
create only a matching already contained in the frame:

\[
D(\gamma)
=
\{M\in\mathcal M: M\subseteq A_\gamma\}.
\tag{2.2}
\]

### 2.3 Internal source-kernel motion

Repeated coordinate factors make \(\Phi_\gamma\) noninjective. A leading
source vector in \(\ker\Phi_\gamma\) can vanish internally at order zero and
still produce a nonzero matching after a labeled factor moves. This mechanism
must not be replaced by a cross-component sharing assumption.

For a cell \(c\), let \(m_c\) be its multiplicity among the six labels. Define
\(K(\gamma)\) as the set of matchings accessible from
\(\ker\Phi_\gamma\) by one labeled factor motion.

### Lemma 2.1 -- exact internal-kernel criterion

A matching \(M\) belongs to \(K(\gamma)\) exactly when there are

- a three-edge submatching \(P\subset M\cap A_\gamma\), and
- a coordinate cell \(c\) in the frame,

such that

\[
\boxed{
m_c\ge 2+\mathbf 1_{c\in P}.
}
\tag{2.3}
\]

#### Proof

The basis vectors \(s_I\) split into fibers according to the coordinate
monomial \(\Phi_\gamma(s_I)\). The kernel on one fiber is the zero-sum
subspace.

Fix a labeled factor over cell \(c\). Its first-order motion acts
nontrivially on the zero-sum fiber exactly when some source subsets in that
fiber contain the label and some do not. If the three unchanged labels map to
\(P\), one selected \(c\)-label is moved to the missing edge of \(M\). The
fiber is nontrivial precisely when an additional unselected \(c\)-label
exists. If \(c\notin P\), two copies of \(c\) suffice; if \(c\in P\), three
copies are required. This is (2.3).

Conversely, under (2.3), choose the movable \(c\)-label, labels mapping to
the three edges of \(P\), and an unused \(c\)-label. Two source subsets in the
same coordinate-monomial fiber then differ in whether they use the movable
label. Their difference lies in \(\ker\Phi_\gamma\), and moving that label to
the missing edge of \(M\) gives a nonzero coefficient. ∎

The matchings that can be generated without requiring a nonzero order-zero
coordinate monomial to be shared with another component are therefore

\[
S(\gamma)=D(\gamma)\cup K(\gamma).
\tag{2.4}
\]

By construction,

\[
S(\gamma)\subseteq E(\gamma).
\tag{2.5}
\]

## 3. Exact local inequality

### Theorem 3.1 -- coordinate six-frame tradeoff

For every unordered multiset \(\gamma\) of six cells of a \(4\times4\)
matrix,

\[
\boxed{
|E(\gamma)|+|S(\gamma)|\le6.
}
\tag{3.1}
\]

This includes every multiplicity pattern and every placement of repeated
factors.

### Exact finite classification

There are

\[
\binom{16+6-1}{6}=54\,264
\]

unordered coordinate six-frames. The primary implementation uses criterion
(2.3). An independent implementation reconstructs the fibers of the fifteen
four-label source subsets and tests the kernel functional directly. Both give
the following complete profile table:

| \(|E|\) | \(|D|\) | \(|K|\) | \(|S|\) | frame count |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 19,584 |
| 1 | 0 | 0 | 0 | 5,856 |
| 1 | 0 | 1 | 1 | 7,200 |
| 1 | 1 | 1 | 1 | 240 |
| 2 | 0 | 0 | 0 | 4,848 |
| 2 | 0 | 1 | 1 | 4,032 |
| 2 | 0 | 2 | 2 | 2,592 |
| 2 | 1 | 1 | 1 | 864 |
| 2 | 1 | 2 | 2 | 576 |
| 2 | 2 | 0 | 2 | 72 |
| 3 | 0 | 0 | 0 | 1,728 |
| 3 | 0 | 1 | 1 | 1,152 |
| 3 | 0 | 2 | 2 | 1,152 |
| 3 | 1 | 0 | 1 | 864 |
| 4 | 0 | 0 | 0 | 2,064 |
| 4 | 0 | 2 | 2 | 576 |
| 4 | 1 | 0 | 1 | 576 |
| 6 | 0 | 0 | 0 | 288 |

Every row satisfies (3.1).

There are 864 equality frames. They have exactly two profiles:

```text
(|E|,|D|,|K|,|S|) = (6,0,0,0): 288 frames
(|E|,|D|,|K|,|S|) = (4,0,2,2): 576 frames.
```

Under independent row and column permutations, the equality locus has four
orbits:

- two distinct-factor orbits of size 144;
- two repeated-factor orbits of size 288.

The distinct-factor equality frames have row and column degree sequence
\((2,2,1,1)\). The repeated-factor equality frames have five distinct cells,
multiplicity pattern \((2,1,1,1,1)\), and distinct-support row and column
degree sequence \((2,1,1,1)\).

The finite classification is part of the proof: the domain is the complete
finite set of coordinate multisets, the arithmetic is integral, and the
independent replay does not import the primary implementation.

## 4. Global incidence theorem

Suppose

\[
\sum_{i=1}^{q}g_i(0)=0
\tag{4.1}
\]

and the first nonzero coefficient has matching part equal to a polynomial with
all 24 perfect-matching coefficients nonzero, in particular a nonzero
diagonal-torus transform of \(\operatorname{perm}_4\).

For component \(i\), write

\[
E_i=E(\gamma_i),
\qquad
S_i=S(\gamma_i),
\qquad
s_i=|S_i|.
\]

Let

\[
U=\bigcup_{i=1}^{q}S_i.
\]

### Lemma 4.1 -- matchings outside \(U\) need two envelope incidences

Every target matching in \(U\) needs at least one envelope incidence. Every
target matching outside \(U\) needs at least two.

#### Proof

A target matching outside \(U\) is neither produced by direct source motion
nor by an internal source-kernel vector. Thus any contribution to it must come
from moving one factor of a nonzero order-zero coordinate monomial \(Q\).

Equation (4.1) forces the coefficient of \(Q\) to be canceled by at least one
other component. The same monomial \(Q\) is therefore present in another
coordinate frame. Since the target matching retains three cells of \(Q\), it
belongs to the first-order envelope of both frames. ∎

Let

\[
I=\sum_{i=1}^{q}|E_i|
\]

be the total frame-matching incidence count. Lemma 4.1 gives

\[
I
\ge
|U|+2(24-|U|)
=
48-|U|.
\tag{4.2}
\]

Since

\[
|U|\le\sum_i s_i,
\]

we have

\[
I\ge48-\sum_i s_i.
\tag{4.3}
\]

On the other hand, Theorem 3.1 gives

\[
I
=
\sum_i|E_i|
\le
\sum_i(6-s_i)
=
6q-\sum_i s_i.
\tag{4.4}
\]

Combining (4.3) and (4.4),

\[
48-\sum_i s_i
\le
6q-\sum_i s_i,
\]

and hence

\[
\boxed{q\ge8.}
\tag{4.5}
\]

This proves (0.1).

## 5. Sharpness of the incidence arithmetic

The inequality \(q\ge8\) is sharp only at the support-incidence level.

Four distinct-factor equality frames are known whose six-element envelopes
partition all 24 perfect matchings. Duplicating those four frames produces
eight frames for which every target matching has incidence degree exactly two:

```text
frame count                         8
envelope size per frame             6
unshared set per frame              0
target incidence degree             2 on all 24 matchings.
```

This does not construct an eight-component regular first-order Chow witness.
It shows only that the local-plus-incidence argument cannot by itself prove a
lower bound larger than eight.

## 6. Consequences for the active frontier

The earlier transposition-edge reduction is unnecessary. It arose by forcing
all local inequalities to equality while omitting internal source-kernel
directions. The corrected local invariant \(S=D\cup K\) handles repeated
factors directly and yields the global contradiction before any 72-edge
search.

The coordinate first-order boundary is now:

```text
q <= 7 regular coordinate first-order lift: ZERO
q = 8 support incidence obstruction: SHARP
q = 8 actual coordinate first-order lift: OPEN
```

For the active literal-block problem this closes coordinate first-order
degenerations for both six and seven components. The remaining six-block
interfaces are:

1. first nonzero order at least two with zero coordinate leading matching
   projection;
2. noncoordinate initial frames;
3. singular or multigrade valuation trees; and
4. unrestricted ambient cancellation outside the coordinate degeneration
   model.

## 7. Deterministic replay

Run

```bash
python scripts/general_quartic_coordinate_first_order_eight_term_barrier.py \
  --json /tmp/general_quartic_coordinate_first_order_eight_term_barrier.json

python -O scripts/general_quartic_coordinate_first_order_eight_term_barrier.py

python scripts/general_quartic_coordinate_first_order_eight_term_barrier_independent.py \
  --expected-core 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b

python -m unittest \
  tests.test_general_quartic_coordinate_first_order_eight_term_barrier -v
```

Expected markers:

```text
GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_BARRIER_PASS
GENERAL_QUARTIC_COORDINATE_FIRST_ORDER_EIGHT_TERM_INDEPENDENT_PASS
```

Frozen theorem core:

```text
8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

## Strict claim boundary

```text
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
six-block unrestricted literal sum = OPEN
seven-block unrestricted literal sum = OPEN
mu(6,4) = OPEN in [6,8]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
