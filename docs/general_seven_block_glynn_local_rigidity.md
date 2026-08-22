# Local six-block rigidity of the compressed Glynn witness

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`, `STRICT_LOCAL_ROUTE_BARRIER`.

The inherited one-term Glynn compression gives a seven-block witness for
`(n,m)=(6,4)`. This note proves that the standard seven summands cannot be
compressed to six by either of the two nearest mechanisms:

1. directly replacing two standard summands by one degree-six Chow derivative
   block; or
2. deleting one summand and absorbing its direction infinitesimally into the
   other six standard blocks.

This is a local theorem at the explicit seven-block witness. It does **not**
exclude a remote six-block representation, a singular or Puiseux degeneration,
a higher-order coalescence, or a different limiting frame. Consequently

\[
\boxed{6\le \mu(6,4)\le 7}
\]

remains the active unrestricted interval.

## 1. The standard seven summands

Let

\[
\Delta=\{v\in\{\pm1\}^4:v_1=1\},
\qquad w=(1,1,1,1),
\qquad \chi(v)=\prod_{r=1}^4v_r.
\]

After sharing the first two columns and removing the reference sign `w`, the
compressed Glynn identity has the seven quartic summands

\[
G_v
=
\chi(v)\,
 v\otimes v\otimes
 \bigl(v\otimes v-w\otimes w\bigr),
\qquad v\in\Delta\setminus\{w\}.
\tag{1.1}
\]

Each `G_v` belongs to the fourth derivative space of the degree-six Chow term
with factors

\[
L_{v,1},L_{v,2},L_{v,3},L_{v,4},L_{w,3},L_{w,4}.
\tag{1.2}
\]

The inherited exact identity is

\[
\operatorname{perm}_4=\frac18\sum_{v\ne w}G_v.
\tag{1.3}
\]

The frozen core of that construction is

```text
045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

## 2. No direct pair merge

Take two distinct retained signs `u` and `v`. Exact flattening ranks of

\[
G_u+G_v
\]

in the four column modes are

\[
\boxed{(2,2,3,3)}.
\tag{2.1}
\]

Because the four column variable spaces are mutually disjoint, the essential
variable dimension is the sum of the four mode ranks:

\[
\boxed{\dim\operatorname{Ess}(G_u+G_v)=10.}
\tag{2.2}
\]

Every quartic in the derivative space of a degree-six Chow term is a polynomial
in the span of its six factors. Its essential dimension is therefore at most
six, including repeated or linearly dependent factors. Hence

\[
\boxed{G_u+G_v\notin\mathcal D_4(T)}
\tag{2.3}
\]

for every degree-six Chow term `T`.

All 21 pairs have the same rank profile. The primary replay computes the ranks
over the rationals; the independent replay confirms the lower ranks modulo an
independent prime.

## 3. Projected tangent space of one standard block

Fix a retained sign `v` and write

\[
C_v=v\otimes v-w\otimes w,
\qquad U_v=\operatorname{span}\{v,w\}\subset V.
\]

Consider the parameterization

\[
(\ell_1,\ldots,\ell_6;s)
\longmapsto
\Phi_{\ell}(s),
\qquad
s\in\operatorname{Sq}^4(\mathbf k^6),
\tag{3.1}
\]

of one degree-six derivative block. Project its tangent image at the standard
point (1.2) to column multidegree `(1,1,1,1)`.

There are 28 nonzero raw projected generators:

- four source directions, choosing `v` or `w` in each tail column;
- eight motions of the two shared-column factors; and
- sixteen motions of the four tail factors.

The shared-column part is

\[
\bigl(V\otimes v+v\otimes V\bigr)\otimes\mathbf k C_v
\]

and has dimension `7`. The tail part is

\[
\mathbf k(v\otimes v)\otimes
\bigl(V\otimes U_v+U_v\otimes V\bigr)
\]

and has dimension

\[
8+8-4=12.
\]

Their intersection is the line spanned by `v tensor v tensor C_v`. Thus the
exact projected tangent dimension is

\[
\boxed{7+12-1=18.}
\tag{3.2}
\]

Cross-column factor motions have a missing column and a repeated column, so
they vanish under this multidegree projection. No tangent direction relevant
to the projected obstruction is omitted.

## 4. No infinitesimal deletion of one summand

For a retained sign `kappa`, let

\[
\mathcal T_v
\]

be the projected tangent space from Section 3 and put

\[
\mathcal T_{-\kappa}
=
\sum_{v\ne w,\kappa}\mathcal T_v.
\]

The analytic dimension bound from (3.2) gives

\[
\dim\mathcal T_{-\kappa}\le6\cdot18=108.
\tag{4.1}
\]

For every one of the seven choices of `kappa`, exact modular elimination at two
primes gives

\[
\operatorname{rank}(\mathcal T_{-\kappa})=108,
\qquad
\operatorname{rank}(\mathcal T_{-\kappa}+\mathbf kG_\kappa)=109.
\tag{4.2}
\]

A nonzero minor modulo a prime is a nonzero integer minor. Hence the first
rank is at least 108 over characteristic zero and is exactly 108 by (4.1). The
augmented rank proves

\[
\boxed{G_\kappa\notin\mathcal T_{-\kappa}}
\tag{4.3}
\]

in characteristic zero.

Equivalently, at the standard six-tuple obtained by deleting `G_kappa`, the
line pointing toward the missing seventh summand is not tangent to the image
of the six-block addition map. Thus the missing summand cannot be absorbed by
a first-order analytic deformation of the other six standard blocks.

The sum of all seven projected tangent spaces has exact rank 123, so the
obstruction is not caused by an accidentally small ambient projection.

## 5. Consequence and next interface

The standard compressed Glynn witness is locally six-irreducible in the
following precise sense:

```text
direct merge of two standard summands: IMPOSSIBLE
first-order absorption of a deleted summand: IMPOSSIBLE
remote six-block witness: OPEN
singular or higher-order coalescence: OPEN
```

Therefore a six-block witness cannot be obtained by the two most direct local
compressions of the known seven-block formula. A successful six-block
construction must leave this standard local chart, use a singular/higher-order
limit, or employ genuinely different mixed frames.

The next narrow calculation is the second fundamental form of the six standard
blocks modulo their 108-dimensional projected tangent sum. This asks whether
the missing direction can first appear at order two. It is strictly smaller
than a generic nonlinear search and directly tests the first surviving local
mechanism.

## 6. Deterministic replay

Run

```bash
python scripts/general_seven_block_glynn_local_rigidity.py \
  --json /tmp/general_seven_block_glynn_local_rigidity.json

python -O scripts/general_seven_block_glynn_local_rigidity.py

python scripts/general_seven_block_glynn_local_rigidity_independent.py \
  --expected-core 7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710

python -m unittest tests.test_general_seven_block_glynn_local_rigidity -v
```

Expected markers:

```text
GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_PASS
GENERAL_SEVEN_BLOCK_GLYNN_LOCAL_RIGIDITY_INDEPENDENT_PASS
```

Frozen theorem core:

```text
7958a27a326b5155bb9e119061f98eabbc81945ca2a931ef9551d73798f2c710
```

## Strict boundary

```text
standard seven-block direct pair merge = ZERO
standard six-tuple missing-summand tangent absorption = ZERO
global six-block literal sum = OPEN
mu(6,4) = OPEN IN [6,7]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
