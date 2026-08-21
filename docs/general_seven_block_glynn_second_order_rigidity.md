# Second-order local rigidity of the compressed Glynn witness

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_RATIONAL_KERNEL_REPLAYED`, `STRICT_LOCAL_SECOND_ORDER_ROUTE_BARRIER`.

The standard compressed Glynn formula gives seven degree-six Chow derivative
blocks whose sum is a nonzero scalar multiple of `perm_4`. The preceding local
rigidity theorem excludes direct pair merging and first-order absorption of a
deleted summand. This note proves the next statement:

> After deleting any one standard summand, the missing summand cannot first be
> generated at order two by a regular deformation of the other six standard
> blocks.

The result is local at the explicit seven-block point. It does not exclude a
remote six-block witness, a singular or Puiseux family, or a third- or
higher-order coalescence. The active interval remains

\[
\boxed{6\le\mu(6,4)\le7}.
\]

## 1. Standard block parameterization

Let

\[
\Delta=\{v\in\{\pm1\}^4:v_1=1\},
\qquad w=(1,1,1,1),
\]

and let the seven retained summands be

\[
G_v
=
\chi(v)v\otimes v\otimes(v\otimes v-w\otimes w),
\qquad v\in\Delta\setminus\{w\}.
\tag{1.1}
\]

For one retained sign, use the six labeled factors

\[
L_{v,1},L_{v,2},L_{v,3},L_{v,4},L_{w,3},L_{w,4}
\tag{1.2}
\]

and an arbitrary source vector in `Sq^4(k^6)`. The local parameter space has

```text
source parameters                         15
factor-motion parameters              6*16
parameters per block                     111
parameters for six retained blocks       666
```

The target polynomial space at full degree four has dimension

\[
\binom{16+4-1}{4}=3876.
\]

Let `F_kappa` be the addition map for the six standard blocks left after
removing `G_kappa`, let

\[
L_\kappa=dF_\kappa,
\qquad K_\kappa=\ker L_\kappa,
\tag{1.3}
\]

and let `pi` denote projection to column multidegree `(1,1,1,1)`, a
256-dimensional direct summand. Put

\[
T_\kappa=\pi(\operatorname{im}L_\kappa).
\tag{1.4}
\]

## 2. Complete first-order kernel

For each of the seven choices of `kappa`, exact elimination gives

\[
\boxed{
\operatorname{rank}L_\kappa=574,
\qquad
\dim K_\kappa=666-574=92.
}
\tag{2.1}
\]

The projected tangent rank is

\[
\boxed{\dim T_\kappa=108.}
\tag{2.2}
\]

The certificate is constructed as follows.

1. Column elimination modulo `1,000,003` produces a 92-vector kernel basis.
2. Every coefficient belongs to
   `{-2,-1,-1/2,1/2,1,2}`.
3. These coefficients are lifted to the rationals.
4. Direct substitution verifies that all 92 lifted vectors annihilate the
   full 3876-coordinate tangent map exactly.
5. Their modular independence and the modular rank 574 prove that this is the
   complete characteristic-zero kernel.

Thus the second-order calculation below is performed on the full
first-order-cancellation kernel, not on a projected or support-only surrogate.

## 3. Polarized second derivative

A first-order parameter direction consists of a source motion `s` and six
factor motions `u_a`. The polar second derivative of one block has only two
types of terms:

\[
B((s,u),(t,z))
=
 d\Phi(u)t+d\Phi(z)s+d^2\Phi(u,z)w_0.
\tag{3.1}
\]

There is no source-source term because the block map is linear in its source.
The last term replaces two distinct factor labels in one of the two active
source subproducts. Formula (3.1) is evaluated exactly and then projected by
`pi`.

For each deletion there are

\[
\binom{92+1}{2}=4278
\]

polarized kernel pairs. Exactly 306 of their projected curvature vectors are
nonzero. Their ordinary span has dimension 24.

The decisive result is stronger:

### Theorem 3.1 -- quotient second fundamental form vanishes

For every retained sign `kappa`,

\[
\boxed{
\pi B_\kappa(K_\kappa,K_\kappa)
\subseteq T_\kappa.
}
\tag{3.2}
\]

Equivalently, the second fundamental form restricted to the full
first-order-cancellation kernel is zero in the quotient

\[
\mathbf k^{256}/T_\kappa.
\tag{3.3}
\]

### Exact verification

The 108-dimensional space `T_kappa` is reconstructed over the rationals from
integer tangent columns. Each of the 4278 curvature vectors is formed from the
exact rational kernel basis and reduced by exact fraction arithmetic against
that tangent basis. Every remainder is zero. The 306 nonzero curvature vectors
span a 24-dimensional subspace already contained in `T_kappa`.

An independent implementation uses monomial tuples rather than the primary
indexed polynomial representation, works modulo the independent prime
`1,000,037`, rebuilds the 666-parameter tangent kernel, and reproduces the
uniform ranks

```text
full tangent rank                         574
kernel dimension                           92
projected tangent rank                    108
nonzero polarized curvature pairs         306
curvature span rank                        24
curvature quotient rank                     0
```

for all seven deletions.

## 4. Missing summand remains transverse through order two

The preceding first-order packet proves

\[
G_\kappa\notin T_\kappa.
\tag{4.1}
\]

The exact augmented projected rank is 109 for every deletion.

Suppose a regular six-block parameter path has expansion

\[
p(t)=p_0+t y+t^2z+O(t^3)
\]

and attempts to follow the missing-summand line at second order:

\[
F_\kappa(p(t))
=
F_\kappa(p_0)+t^2G_\kappa+O(t^3).
\tag{4.2}
\]

The order-one equation gives `y in K_kappa`. The projected order-two
coefficient is

\[
\pi L_\kappa(z)+\frac12\pi B_\kappa(y,y).
\tag{4.3}
\]

Both terms lie in `T_kappa`: the first by definition and the second by
Theorem 3.1. Equation (4.1) contradicts (4.2). Therefore

\[
\boxed{
\text{the deleted standard summand cannot be absorbed at order two.}
}
\tag{4.4}
\]

## 5. Consequence and stopping point

The known seven-block witness is now locally six-irreducible through order two:

```text
direct pair merge                         IMPOSSIBLE
first-order missing-summand absorption    IMPOSSIBLE
second-order missing-summand absorption   IMPOSSIBLE
third- or higher-order absorption         OPEN
remote or singular six-block witness      OPEN
```

This is a substantive stopping point for local regular deformation of the
known construction. Continuing to third order is justified only after the
third fundamental form is written in the quotient by `T_kappa`; a broad
nonlinear search is not a substitute.

The alternative active route is a genuinely different six-block configuration
subject to the inherited full-support six-element quotient circuit and all
common-source repeated-column layers.

## 6. Deterministic replay

Run

```bash
python scripts/general_seven_block_glynn_second_order_rigidity.py \
  --json /tmp/general_seven_block_glynn_second_order_rigidity.json

python -O scripts/general_seven_block_glynn_second_order_rigidity.py

python scripts/general_seven_block_glynn_second_order_rigidity_independent.py \
  --expected-core e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c

python -m unittest tests.test_general_seven_block_glynn_second_order_rigidity -v
```

Expected markers:

```text
GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_PASS
GENERAL_SEVEN_BLOCK_GLYNN_SECOND_ORDER_RIGIDITY_INDEPENDENT_PASS
```

Frozen theorem core:

```text
e80c3b30e9df09144eef28f3424d0b4e44b0f3e6a737e12ef0a8e4a6d5f84a4c
```

## Strict boundary

```text
standard seven-block local compression through order two = ZERO
global six-block literal sum = OPEN
third/higher local coalescence = OPEN
remote/singular six-block witness = OPEN
mu(6,4) = OPEN IN [6,7]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
