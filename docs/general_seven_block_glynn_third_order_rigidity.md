# Third-order local rigidity of the compressed Glynn witness

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_RATIONAL_THIRD_JET_REPLAYED`,
`STRICT_LOCAL_THIRD_ORDER_ROUTE_BARRIER`.

The standard compressed Glynn formula gives seven degree-six Chow derivative
blocks whose sum is a nonzero scalar multiple of `perm_4`. Earlier packets
exclude direct pair merging, first-order absorption of a deleted summand, and
second-order absorption. This note proves the next statement:

> After deleting any one standard summand, the missing summand cannot first be
> generated at order three by a regular deformation of the other six standard
> blocks.

The theorem is local at the explicit seven-block point and order-bounded. It
does not exclude a remote six-block representation, a singular or Puiseux
family, or first appearance at order four or higher. Consequently the active
unrestricted interval remains

\[
\boxed{6\le\mu(6,4)\le7}.
\]

## 1. Parameter map and inherited first two orders

Let

\[
\Delta=\{v\in\{\pm1\}^4:v_1=1\},
\qquad w=(1,1,1,1),
\]

and write the seven compressed summands as

\[
G_v=\chi(v)v\otimes v\otimes(v\otimes v-w\otimes w),
\qquad v\in\Delta\setminus\{w\}.
\]

Delete one summand `G_kappa`. Let `F_kappa` be the addition map for the six
remaining degree-six derivative blocks in the same 111-parameter-per-block
model used by the second-order packet. At the standard six-tuple put

\[
L=dF_\kappa,
\qquad B=d^2F_\kappa,
\qquad C=d^3F_\kappa,
\qquad K=\ker L.
\]

Let `pi` denote projection to column multidegree `(1,1,1,1)` and set

\[
T=\pi(\operatorname{im}L)\subseteq\mathbf k^{256}.
\]

The inherited exact data are

\[
\operatorname{rank}L=574,
\qquad \dim K=92,
\qquad \dim T=108,
\]

and

\[
G_\kappa\notin T,
\qquad
\pi B(K,K)\subseteq T.
\tag{1.1}
\]

Thus the missing direction is transverse to the projected tangent image and
the quotient second fundamental form vanishes. A third-order calculation must
still impose the **full** second-order equation; projected curvature alone is
not enough.

## 2. Full second-order splitting

Fix an exact rational basis

\[
e_1,\ldots,e_{92}
\]

of `K`. An exact column-echelon splitting of the full 3,876-coordinate tangent
map assigns, for every unordered pair `i<=j`, a parameter correction `H_ij`
and a fixed cokernel representative `Q_ij` such that

\[
\boxed{
B(e_i,e_j)+L H_{ij}=Q_{ij}.
}
\tag{2.1}
\]

There are

\[
\binom{92+1}{2}=4,278
\]

such equations. For

\[
y=\sum_i a_i e_i
\]

write `H(y,y)` and `Q(y,y)` for the associated quadratic forms. Equation
(2.1) gives

\[
B(y,y)+L H(y,y)=Q(y,y).
\tag{2.2}
\]

A regular path

\[
p(t)=p_0+t y+t^2z+O(t^3)
\]

whose first two output coefficients vanish must satisfy

\[
y\in K,
\qquad
Lz+\frac12 B(y,y)=0.
\tag{2.3}
\]

Hence `Q(y,y)=0`, and one may write

\[
z=\frac12H(y,y)+k,
\qquad k\in K.
\tag{2.4}
\]

The full second-order obstruction is not zero. On the three deletion orbits
under permutation of the three free sign coordinates, its exact finite data
are

| missing-sign weight | orbit size | nonzero pair representatives | full quotient rank |
|---:|---:|---:|---:|
| 1 | 3 | 104 | 66 |
| 2 | 3 | 116 | 66 |
| 3 | 1 | 104 | 70 |

Thus the third-order result below is not obtained by silently assuming that
every first-order kernel direction lifts through order two.

## 3. Corrected polarized third tensor

For basis indices `i<=j<=k`, define

\[
\begin{aligned}
\Theta_{ijk}=\pi\big(&C(e_i,e_j,e_k)
+B(e_i,H_{jk})\\
&+B(e_j,H_{ik})
+B(e_k,H_{ij})\big).
\end{aligned}
\tag{3.1}
\]

This is the polarized third-order tensor after the canonical full second-order
correction.

The definition is intrinsic modulo `T`. If a different splitting of (2.1) is
used with the same cokernel representatives, the corrections differ by
vectors in `K`. By (1.1), their contribution under `pi B(K,K)` lies in `T`.
Therefore the class of `Theta` in `k^256/T` is independent of the tangent
splitting.

### Theorem 3.1 -- corrected third fundamental form vanishes

For every deleted standard summand,

\[
\boxed{
\Theta_{ijk}\in T
\quad\text{for all}\quad
1\le i\le j\le k\le92.
}
\tag{3.2}
\]

Equivalently, the corrected third fundamental form has quotient rank zero in

\[
\mathbf k^{256}/T.
\]

### Exact verification

There are

\[
\binom{92+2}{3}=134,044
\]

polarized triples. For every deletion orbit representative, exactly 1,320
corrected tensors are nonzero before tangent reduction. They span a
24-dimensional subspace, but every one reduces exactly to zero modulo the
108-dimensional space `T`:

```text
full tangent rank                              574
first-order kernel dimension                    92
projected tangent rank                         108
full pair splittings                         4,278
polarized corrected third triples          134,044
raw nonzero corrected triples                1,320
corrected third span rank                        24
corrected third quotient rank                     0
missing-summand augmented projected rank        109
```

The primary implementation uses exact fractions throughout the kernel lift,
full second-order splitting, and all third-order reductions. Permutations of
the three free sign coordinates have deletion orbits of sizes `3,3,1`, so
exact representatives of Hamming weights `1,2,3` cover all seven deletions.

A separate implementation uses indexed monomials, modular arithmetic at the
independent prime `1,000,037`, and no import from the primary verifier. It
reproduces all three orbit rows, all 134,044 triples, the 1,320 nonzero count,
the 24-dimensional raw span, and quotient rank zero.

## 4. Third-order exclusion

Suppose a regular path attempts to absorb the missing summand first at order
three:

\[
F_\kappa(p(t))
=F_\kappa(p_0)+t^3G_\kappa+O(t^4).
\tag{4.1}
\]

Write

\[
p(t)=p_0+t y+t^2z+t^3u+O(t^4).
\]

The first two equations give (2.4). Multiplying the projected third-order
coefficient by six gives

\[
6\pi L(u)
+\pi C(y,y,y)
+3\pi B(y,H(y,y))
+6\pi B(y,k).
\tag{4.2}
\]

The first term lies in `T` by definition. The middle two terms are
`Theta(y,y,y)` and lie in `T` by Theorem 3.1. The final term lies in `T` by
`pi B(K,K) subset T`. Therefore every projected third-order coefficient lies
in `T`, contradicting `G_kappa notin T`.

Hence

\[
\boxed{
\text{a deleted standard summand cannot first be absorbed at order three.}
}
\tag{4.3}
\]

## 5. Consequence and stopping rule

The standard compressed Glynn witness is now locally six-irreducible through
order three:

```text
direct pair merge                         IMPOSSIBLE
first-order missing-summand absorption    IMPOSSIBLE
second-order missing-summand absorption   IMPOSSIBLE
third-order missing-summand absorption    IMPOSSIBLE
fourth or higher local absorption         OPEN
remote or singular six-block witness      OPEN
```

This completes the planned third-fundamental-form test. It does not justify an
unbounded sequence of higher-order local calculations. The local route stops
here: two successive corrected fundamental forms vanish in the selected
quotient, while the result remains unable to constrain remote six-block
points. The next research effort should move to genuinely mixed six-block
configurations or the inherited full-support six-element quotient circuit.

## 6. Deterministic replay

Run

```bash
python scripts/general_seven_block_glynn_third_order_rigidity.py \
  --workers 3 \
  --json /tmp/general_seven_block_glynn_third_order_rigidity.json

python -O scripts/general_seven_block_glynn_third_order_rigidity.py \
  --workers 3 --print-core-only

python scripts/general_seven_block_glynn_third_order_rigidity_independent.py \
  --expected-core a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62

python -m unittest \
  tests.test_general_seven_block_glynn_third_order_rigidity -v
```

Expected markers:

```text
GENERAL_SEVEN_BLOCK_GLYNN_THIRD_ORDER_RIGIDITY_PASS
GENERAL_SEVEN_BLOCK_GLYNN_THIRD_ORDER_RIGIDITY_INDEPENDENT_PASS
```

Frozen theorem core:

```text
a719b2d7f2f021737024931d2c11502e59affaf4012dc1f38792bb7699fe3f62
```

## Strict claim boundary

```text
standard seven-block local compression through order three = ZERO
standard local fourth/higher absorption = OPEN
global six-block literal sum = OPEN
remote/singular six-block witness = OPEN
mu(6,4) = OPEN IN [6,7]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
