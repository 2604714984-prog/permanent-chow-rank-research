# The quadratic psi chart for every permanent

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` (G-030).
The theorem and proof are purely mathematical over a characteristic-zero
field.  The accompanying exact coefficient-constraint calculation replays
`n=3,4,5,6`; it is not a premise for the general theorem.

## 1. Statement

Let `n>=3`, let `V` be the `n^2`-dimensional space with coordinates
`x_(ia)`, and put

\[
 P_n=\operatorname{perm}_n,
 \qquad
 E=\mathcal D_{n-2}(P_n)\subset\operatorname{Sym}^2V.
\]

Thus `E` is spanned by the `2 by 2` subpermanents and

\[
 \dim E=\binom n2^2.                                \tag{1.1}
\]

Let

\[
 \delta:\operatorname{Sym}^2V\otimes V
 \longrightarrow V\otimes\bigwedge^2V
\]

be the standard Koszul differential.  For `0!=v in V` define

\[
 \psi_v:\operatorname{Sym}^2V/E
 \longrightarrow\operatorname{coker}\delta(E\otimes V),
 \qquad
 [q]\longmapsto[\delta(q\otimes v)].               \tag{1.2}
\]

### Theorem 1.1 (general psi-chart theorem)

For every `n>=3` and every nonzero `v`,

\[
 \boxed{\ker\psi_v=\operatorname{span}([v^2]).}    \tag{1.3}
\]

Consequently

\[
 \operatorname{rank}\psi_v
 =\binom{n^2+1}{2}-\binom n2^2-1.                  \tag{1.4}
\]

### Corollary 1.2 (one new direction gains `n^2-1`)

For every `q notin E`,

\[
 \boxed{
 \operatorname{rank}\delta((E+\operatorname{span}(q))\otimes V)
 \ge
 \operatorname{rank}\delta(E\otimes V)+n^2-1.
 }                                                   \tag{1.5}
\]

This proves that both the psi-chart certificate and the single-new-direction
gain from the `n=4` proof extend to all `n>=3`.  It does **not** say that the
gains of several new directions add.

## 2. Quadratic rank and the permanent prolongation

The row-column torus acts on `E` with the multiplicity-free basis

\[
 P_{\{i,j\},\{a,b\}}
 =x_{ia}x_{jb}+x_{ib}x_{ja}.
\]

### Lemma 2.1

Every nonzero element of `E` has quadratic matrix rank at least four.

#### Proof

Degenerate a nonzero element by a generic row-column one-parameter subgroup.
Its limit is a nonzero scalar multiple of one basis subpermanent.  Matrix rank
cannot increase under specialization, while a `2 by 2` permanent in four
distinct variables has rank four.  ∎

Define the full cubic prolongation

\[
 E^{(1)}=
 \{g\in\operatorname{Sym}^3V:
 \partial_u g\in E\text{ for every }u\in V^*\}.
\]

### Lemma 2.2

\[
 \boxed{
 E^{(1)}=\mathcal D_{n-3}(P_n),
 \qquad
 \dim E^{(1)}=\binom n3^2.
 }                                                   \tag{2.1}
\]

#### Proof

Fix a cubic monomial occurring in `g`.  Differentiating by each of its
variables shows that every two-variable divisor must use distinct rows and
columns.  Hence the three variables form a matching on three rows and three
columns.

Fix those row and column triples.  The six matching monomials are indexed by
`S_3`.  Two coefficients are equated whenever the matchings share one edge;
the coefficient graph is the bipartite graph `K_(3,3)`, hence is connected.
All six coefficients are equal, so this block is a scalar multiple of the
corresponding `3 by 3` subpermanent.  Different row-column triples have
disjoint monomial supports.  This proves (2.1).  ∎

The kernel-prolongation identity now gives

\[
 \operatorname{rank}\delta(E\otimes V)
 =n^2\binom n2^2-\binom n3^2.                      \tag{2.2}
\]

## 3. Relative prolongation and the psi kernel

For nonzero `v`, define

\[
 R_v(E)=\{g\in\operatorname{Sym}^3V:
 \partial_u g\in E
 \text{ whenever }u(v)=0\}.
\]

### Lemma 3.1 (relative kernel-prolongation correspondence)

There is a natural isomorphism

\[
 \boxed{\ker\psi_v\simeq R_v(E)/E^{(1)}.}          \tag{3.1}
\]

Under this isomorphism `[v^2]` corresponds to the class of `v^3`.

#### Proof

The kernel of `delta` on `Sym^2 V tensor V` is the image of the cubic
polarization map `iota:Sym^3 V -> Sym^2 V tensor V`.  If `[q]` belongs to
`ker psi_v`, then

\[
 q\otimes v-z=\iota(g)
\]

for some `z in E tensor V`.  Contracting the last factor by every `u` with
`u(v)=0` shows that `g in R_v(E)`.

Conversely, let `pi_E` and `pi_v` be the quotient maps by `E` and `kv`.
The condition `g in R_v(E)` is equivalent to

\[
 (\pi_E\otimes\pi_v)\iota(g)=0.
\]

Exactness of tensor products over a field gives

\[
 \ker(\pi_E\otimes\pi_v)
 =E\otimes V+\operatorname{Sym}^2V\otimes kv,
\]

which constructs `[q] in ker psi_v`.  The kernel of this construction is
exactly `E^(1)`.  Substituting `g=v^3` gives the last assertion.  ∎

## 4. The coordinate relative prolongation

Put `e=x_(00)`.

### Lemma 4.1

\[
 \boxed{
 R_e(E)=E^{(1)}\oplus\operatorname{span}(e^3).
 }                                                   \tag{4.1}
\]

#### Proof

The monomial argument of Lemma 2.2 still applies, except that differentiation
by `e` is not imposed.  A monomial not containing `e` must again be a
three-edge matching.

For a monomial containing `e`, the terms `e^2z` vanish immediately after
differentiation by `z`.  A term `ez^2` forces, through its `2 by 2` permanent,
a companion whose derivative in a different direction contains two variables
in one row or one column, so its coefficient is zero.  The same two-step
argument removes `ezw` whenever `z,w` fail to complete a three-edge matching.
Thus the only extra monomial is `e^3`.

Within a fixed three-row, three-column matching block, the coefficient graph
is `K_(3,3)`.  If the block contains `e`, omitting differentiation by `e`
deletes at most the one graph edge labelled by `e`; `K_(3,3)` minus one edge
is still connected.  Hence every matching block remains a subpermanent.
Finally `e^3` is not in `E^(1)`, because its derivative would put the rank-one
quadric `e^2` in `E`, contrary to Lemma 2.1.  ∎

## 5. Torus degeneration from an arbitrary direction

Assume the coefficient of `e` in `v` is nonzero and rescale it to one.  Let
`A(e)=v`, let `A` fix all other coordinate variables, and put

\[
 E_A=A^{-1}E.
\]

Choose positive integers `r_i,c_a` with `r_0=c_0=0` and all other entries
positive.  The one-parameter subgroup

\[
 \lambda(s)x_{ia}=s^{r_i+c_a}x_{ia}
\]

fixes `e` and preserves every `2 by 2` subpermanent.  Conjugating the shear
`A` scales all non-`e` coefficients of `v` to zero as `s` tends to zero.
Therefore `E_A` degenerates to `E`, while all nonzero fibers are isomorphic.

Relative prolongation is a kernel of a matrix whose entries vary
polynomially, so its dimension can only increase at the special fiber.
Lemma 4.1 gives

\[
 \dim R_e(E_A)\le\binom n3^2+1.                   \tag{5.1}
\]

On the other hand, `E_A^(1)` has dimension `binom(n,3)^2` and `e^3` always
belongs to `R_e(E_A)`.  The latter is not in `E_A^(1)`: otherwise `e^2` would
belong to `E_A`, and applying `A` would put the rank-one quadric `v^2` in
`E`, contradicting Lemma 2.1.  Equality holds in (5.1).  Naturality under `A`
therefore gives

\[
 \dim R_v(E)=\binom n3^2+1.                       \tag{5.2}
\]

Every nonzero `v` has a nonzero coordinate.  Row and column permutations move
that coordinate to `e` and preserve `E` and `delta`.  Lemma 3.1 and (5.2)
prove Theorem 1.1.

## 6. Proof of the extension gain

Fix `q notin E` and define

\[
 \theta_q:V\longrightarrow\operatorname{coker}\delta(E\otimes V),
 \qquad v\longmapsto\psi_v([q]).
\]

If two independent vectors `v,w` belonged to its kernel, Theorem 1.1 would
give nonzero scalars `a,b` such that

\[
 [q]=a[v^2]=b[w^2].
\]

Thus `av^2-bw^2` would be a nonzero quadratic form in `E` of rank at most
two, contradicting Lemma 2.1.  Hence `dim ker theta_q<=1` and
`rank theta_q>=n^2-1`.  Its image is precisely the extra Koszul image created
by adjoining `q`, proving Corollary 1.2.

## 7. Exact replay and limitation

Run

```text
python scripts/general_quadratic_psi_chart_audit.py \
  --json data/general_quadratic_psi_chart_audit.json
python -m unittest tests/test_general_quadratic_psi_chart.py
```

The replay constructs every coefficient constraint for the full and
coordinate-relative cubic prolongations for `n=3,4,5,6`.  Weighted connected
components over `Fraction` give respectively

\[
 \dim E^{(1)}=1,16,100,400
\]

and relative dimensions `2,17,101,401`.  For `n=6`, the theorem reads

\[
 \operatorname{rank}\psi_v=440,
 \qquad
 \operatorname{rank}\delta((E+\langle q\rangle)\otimes V)\ge7735.
\]

The result is uniform in `v` and `q`, but it is a one-direction theorem.
For a multidimensional extension, the images of the maps `theta_q` can
overlap.  Neither Theorem 1.1 nor Corollary 1.2 makes those gains additive;
the lower-27 residual still requires a coupled module argument.
