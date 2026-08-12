# The psi chart in every intermediate derivative degree

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` (G-031).
The theorem is a pure characteristic-zero statement.  The accompanying exact
coefficient replay covers selected cases through `n=6`; it is not a premise
of the proof.

## 1. Statement

Let `n>=3`, let `V` be the `n^2`-dimensional space with coordinates
`x_(ia)`, and put

\[
 P_n=\operatorname{perm}_n,
 \qquad
 E_m=\mathcal D_{n-m}(P_n)\subseteq\operatorname{Sym}^mV
 \quad(2\le m\le n-1).
\]

Thus `E_m` is spanned by the `m by m` subpermanents and

\[
 \dim E_m=\binom nm^2.                              \tag{1.1}
\]

Let

\[
 \delta_m:\operatorname{Sym}^mV\otimes V
 \longrightarrow
 \operatorname{Sym}^{m-1}V\otimes\bigwedge^2V
\]

be the first Koszul differential.  For `0!=v in V` define

\[
 \psi_{m,v}:\operatorname{Sym}^mV/E_m
 \longrightarrow\operatorname{coker}\delta_m(E_m\otimes V),
 \qquad
 [q]\longmapsto[\delta_m(q\otimes v)].             \tag{1.2}
\]

### Theorem 1.1 (full derivative-degree psi chart)

For every `n>=3`, every `2<=m<=n-1`, and every nonzero `v`,

\[
 \boxed{\ker\psi_{m,v}=\operatorname{span}([v^m]).} \tag{1.3}
\]

Consequently

\[
 \operatorname{rank}\psi_{m,v}
 =\binom{n^2+m-1}{m}-\binom nm^2-1.                \tag{1.4}
\]

### Corollary 1.2 (one new direction)

For every `q notin E_m`,

\[
 \boxed{
 \operatorname{rank}\delta_m((E_m+\operatorname{span}(q))\otimes V)
 \ge
 \operatorname{rank}\delta_m(E_m\otimes V)+n^2-1.
 }                                                   \tag{1.5}
\]

The earlier quadratic theorem is the case `m=2`.  At `n=6,m=3`, the theorem
applies directly to the 400-dimensional middle derivative space and gives

\[
 \operatorname{rank}\psi_{3,v}=8035,
 \qquad
 \operatorname{rank}\delta_3((E_3+\langle q\rangle)\otimes V)
 \ge14210.                                          \tag{1.6}
\]

## 2. Essential variables and the full prolongation

### Lemma 2.1

Every nonzero element of `E_m` has essential-variable dimension at least
`m^2`.

#### Proof

The row-column torus gives the subpermanent basis of `E_m` distinct weights,
indexed by a pair of `m`-element row and column sets.  A generic one-parameter
subgroup therefore degenerates any nonzero element of `E_m`, after projective
rescaling, to one nonzero basis subpermanent.

Essential-variable dimension is the rank of the first catalecticant and
cannot increase under specialization.  An `m by m` permanent has `m^2`
linearly independent first derivatives: they have distinct row-column torus
weights.  The original element consequently has at least `m^2` essential
variables.  ∎

Define the full first prolongation

\[
 E_m^{(1)}=
 \{g\in\operatorname{Sym}^{m+1}V:
 \partial_u g\in E_m\text{ for every }u\in V^*\}.
\]

### Lemma 2.2

\[
 \boxed{
 E_m^{(1)}=E_{m+1},
 \qquad
 \dim E_m^{(1)}=\binom n{m+1}^2.
 }                                                   \tag{2.1}
\]

#### Proof

Every degree-`m` monomial in `E_m` is a matching: its variables use distinct
rows and distinct columns.  Hence the derivative constraints force every
degree-`m+1` monomial with nonzero coefficient in a prolongation to be an
`(m+1)`-edge matching.

Fix its row and column sets.  The matching monomials are indexed by
permutations in `S_(m+1)`.  If two permutations share an edge, the derivative
in that edge places their remaining monomials in the same subpermanent block
and equates their coefficients.  The resulting coefficient graph is
connected: transpositions generate `S_(m+1)`, and permutations differing by
one transposition share `m-1>=1` edges.  Thus all `(m+1)!` coefficients in the
block are equal, so the block is a scalar multiple of the corresponding
subpermanent.  Different row-column blocks have disjoint monomial supports.
This proves (2.1).  ∎

The kernel-prolongation identity gives the useful baseline

\[
 \operatorname{rank}\delta_m(E_m\otimes V)
 =n^2\binom nm^2-\binom n{m+1}^2.                 \tag{2.2}
\]

## 3. Relative prolongation

For nonzero `v`, put

\[
 R_{m,v}(E_m)=
 \{g\in\operatorname{Sym}^{m+1}V:
 \partial_u g\in E_m\text{ whenever }u(v)=0\}.
\]

### Lemma 3.1 (relative kernel-prolongation correspondence)

There is a natural isomorphism

\[
 \boxed{
 \ker\psi_{m,v}\simeq R_{m,v}(E_m)/E_m^{(1)}.
 }                                                   \tag{3.1}
\]

Under this isomorphism `[v^m]` corresponds to the class of `v^(m+1)`.

#### Proof

The kernel of `delta_m` on `Sym^m V tensor V` is the image of the
polarization map

\[
 \iota_m:\operatorname{Sym}^{m+1}V
 \longrightarrow\operatorname{Sym}^mV\otimes V.
\]

If `[q]` belongs to `ker psi_(m,v)`, then

\[
 q\otimes v-z=\iota_m(g)
\]

for some `z in E_m tensor V`.  Contracting the last factor by every `u` with
`u(v)=0` gives `g in R_(m,v)(E_m)`.

Conversely, let `pi_E` and `pi_v` denote quotient maps by `E_m` and `kv`.
The relative derivative condition is equivalent to

\[
 (\pi_E\otimes\pi_v)\iota_m(g)=0.
\]

Exactness of tensor products over a field gives

\[
 \ker(\pi_E\otimes\pi_v)
 =E_m\otimes V+\operatorname{Sym}^mV\otimes kv.
\]

This constructs `[q] in ker psi_(m,v)`.  The ambiguity is exactly the full
prolongation `E_m^(1)`.  Substituting `g=v^(m+1)` proves the last assertion. ∎

## 4. A coordinate relative prolongation

Put `e=x_(00)`.

### Lemma 4.1

\[
 \boxed{
 R_{m,e}(E_m)=E_{m+1}\oplus\operatorname{span}(e^{m+1}).
 }                                                   \tag{4.1}
\]

#### Proof

Only differentiation by `e` is omitted.  A monomial not containing `e` is
therefore an `(m+1)`-edge matching by the argument of Lemma 2.2.

Consider a monomial containing `e` and another variable.  Differentiating by
that other variable shows first that the exponent of `e` is one.  If `m>=3`,
differentiating by a suitable third edge detects every repetition or
row-column conflict among the remaining edges.  Differentiating by one of two
remaining edges similarly detects any conflict with `e`.  Hence every
surviving mixed monomial is again an `(m+1)`-edge matching.

For `m=2`, there is one apparent exceptional pattern: `ezw`, where `z,w` are
each disjoint from `e` but conflict with one another; this includes `z=w`.
For example, take `z=x_(ia)` and `w=x_(ib)`.  In the derivative by `z`, the
pair `ew=x_(00)x_(ib)` forces the opposite-corner pair
`x_(0b)x_(i0)`, hence forces the coefficient of
`z x_(0b)x_(i0)`.  Differentiating the latter monomial by `x_(0b)` gives
`z x_(i0)`, a nonmatching pair, so its coefficient and then the original
coefficient vanish.  The common-column case is symmetric, and the same
argument with the harmless derivative multiplicity covers `z=w`.  Thus the
same conclusion holds for `m=2`.  The only genuinely new monomial is
`e^(m+1)`.

It remains to compare coefficients inside a matching block.  When the block
contains `e`, omitting differentiation by `e` removes only the coefficient
connections labelled by that edge.  The graph stays connected.  For
`m+1=3`, it is `K_(3,3)` minus one edge.  For `m+1>=4`, two permutations
differing by a transposition share at least two edges, at most one of which is
`e`; the transposition Cayley graph is therefore still present.  Thus every
matching block remains one subpermanent.

Finally, `e^(m+1)` is not in `E_(m+1)`, since otherwise its derivative would
put the one-variable form `e^m` in `E_m`, contrary to Lemma 2.1.  This proves
(4.1).  ∎

## 5. Degeneration from an arbitrary direction

Suppose the coefficient of `e` in `v` is nonzero and rescale it to one.  Let
`A(e)=v`, let `A` fix every other coordinate, and set

\[
 E_{m,A}=A^{-1}E_m.
\]

Choose positive row and column weights away from row and column zero and zero
weights at row and column zero.  The corresponding one-parameter subgroup
fixes `e`, preserves `E_m`, and conjugates the shear `A` to the identity as
the parameter tends to zero.  Consequently `E_(m,A)` degenerates to `E_m`,
while its nonzero fibers are isomorphic.

The relative prolongation is the kernel of a matrix varying polynomially with
the parameter.  Kernel dimension can only increase at the special fiber, so
Lemma 4.1 gives

\[
 \dim R_{m,e}(E_{m,A})
 \le\binom n{m+1}^2+1.                            \tag{5.1}
\]

The reverse inequality is immediate: `E_(m,A)^(1)` has dimension
`binom(n,m+1)^2`, and `e^(m+1)` lies in the relative prolongation.  These
summands are independent.  Indeed, membership of `e^(m+1)` in the full
prolongation would imply `e^m in E_(m,A)`, hence `v^m in E_m`, contradicting
Lemma 2.1.  Equality holds in (5.1).  Naturality under `A` gives

\[
 \dim R_{m,v}(E_m)=\binom n{m+1}^2+1.             \tag{5.2}
\]

Every nonzero `v` has a nonzero coordinate, and row-column permutations move
that coordinate to `e` while preserving `E_m` and the Koszul differential.
Lemmas 2.2 and 3.1 now prove Theorem 1.1.

## 6. The one-direction gain

Fix `q notin E_m` and define the linear map

\[
 \theta_q:V\longrightarrow\operatorname{coker}\delta_m(E_m\otimes V),
 \qquad
 v\longmapsto\psi_{m,v}([q]).
\]

If two independent vectors `v,w` lay in its kernel, Theorem 1.1 would give
nonzero scalars `a,b` with

\[
 [q]=a[v^m]=b[w^m].
\]

Thus `av^m-bw^m` would be a nonzero element of `E_m` depending on at most two
essential variables.  Lemma 2.1 requires at least `m^2>=4`, a contradiction.
Therefore `dim ker theta_q<=1`, so `rank theta_q>=n^2-1`.  Its image is exactly
the new Koszul image modulo `delta_m(E_m tensor V)`, proving Corollary 1.2.

## 7. Exact replay and boundary

Run

```text
python scripts/general_derivative_psi_chart_audit.py \
  --json data/general_derivative_psi_chart_audit.json
python -m unittest tests/test_general_derivative_psi_chart.py
```

The replay constructs all coefficient constraints for

```text
(n,m)=(3,2),(4,2),(4,3),(5,2),(5,3),(5,4),(6,2),(6,3).
```

Weighted connected components over `Fraction` reproduce

\[
 \dim E_m^{(1)}=\binom n{m+1}^2,
 \qquad
 \dim R_{m,e}(E_m)=\binom n{m+1}^2+1.
\]

No floating-point or finite-field rank participates.  The theorem controls
one quotient direction.  Images belonging to several new directions can
overlap, so neither Theorem 1.1 nor Corollary 1.2 makes their gains additive.
That coupled multi-direction problem remains the relevant lower-27 obstacle.
