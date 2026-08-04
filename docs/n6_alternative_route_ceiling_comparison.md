# Exact ceiling comparison for alternative `n=6` lower-26 routes

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

The current in-repository interval remains

\[
25\le \operatorname{ChowRank}(\operatorname{perm}_6)\le 32.
\]

This note compares three genuinely different next-step ideas after the fixed-count central first-Koszul route was suspended:

1. the first higher-wedge Koszul differential;
2. a scalar second derivative shadow; and
3. structured decomposition search inside the column-uniform sign family underlying Glynn's formula.

The comparison is deliberately small. It does not create a new state registry and does not claim lower 26.

## 1. First higher-wedge Koszul flattening

Let

\[
D_m(f)=\operatorname{im}C_{6-m,m}(f)\subseteq \operatorname{Sym}^mV,
\qquad \dim V=36.
\]

For `p=2`, define

\[
\delta_2:
D_m(f)\otimes\Lambda^2V
\longrightarrow
D_{m-1}(f)\otimes\Lambda^3V,
\]

\[
\delta_2(q\otimes\omega)
=
\sum_a \partial_a q\otimes(x_a\wedge\omega).
\]

The script

```text
scripts/n6_second_koszul_rank_audit.py
```

reconstructs every row-column torus block from the definitions and performs sparse Gaussian elimination modulo `1,000,003`.

For the permanent and one independent six-factor Chow term, the certified values are:

| output degree `m` | permanent rank information | one-term rank information | certified rank-ratio lower bound |
|---:|---:|---:|---:|
| 2 | `127125 <= rank <= 127575` | `8730 <= rank <= 8745` | 15 |
| 3 | `rank = 243936` | `rank = 12066` | 21 |
| 4 | `rank = 140455` | `rank = 9235` | 16 |

The upper bounds come from the preceding Koszul image because consecutive differentials compose to zero. At `m=3,4`, the modular lower ranks attain those upper bounds, so the ranks are exact in characteristic zero. At `m=2`, the computation intentionally records a window rather than promoting the modular value to an exact characteristic-zero rank.

The ordinary first-Koszul lower bounds at the same output degrees are respectively

```text
15, 21, 16.
```

Thus the first higher-wedge differential does not improve any of the three integer rank-ratio bounds. In particular, the central output degree still gives only the base lower bound 21 before using intersection geometry.

### Claim boundary

This does not prove that every higher-wedge flattening or every quotient refinement is useless. It proves only that the first higher-wedge rank ratio, for output degrees `2,3,4`, has no better integer ceiling than the already-used first-Koszul ratios.

## 2. The scalar second-shadow dimension is vacuous for `q>=6`

Let

\[
S\subseteq D_3(\operatorname{perm}_6),
\qquad
\dim S=b.
\]

Write

\[
b=\binom{x}{3}^2.
\]

Iterating the two-dimensional Kruskal--Katona/Bukh shadow inequality gives

\[
\dim\partial^2S\ge \binom{x}{1}^2=x^2.
\tag{2.1}
\]

If `S` lies in the central derivative space of a sum of `q` degree-six Chow terms, then

\[
\partial^2S\subseteq D_1(R).
\]

Each term uses at most six essential linear forms, so

\[
\dim D_1(R)\le \min(36,6q).
\tag{2.2}
\]

For every fixed count tested in the lower-26 diagnostic,

\[
q\in\{6,7,8\},
\]

the right side of (2.2) is 36. Equations (2.1)--(2.2) therefore give only

\[
x\le6,
\qquad
b\le\binom63^2=400,
\]

which is the full dimension of `D_3(perm_6)`. Hence a **dimension-only** second shadow adds no restriction to the lower-26 fixed-count frontiers.

This does not rule out a genuinely coupled first/second-shadow theorem that uses incidence or equality structure rather than only the second-shadow dimension.

## 3. Rigidity of the column-uniform Glynn sign family

For arbitrary `n`, fix `epsilon_0=1` and define

\[
G_\epsilon
=
\prod_{j=0}^{n-1}
\left(
\sum_{i=0}^{n-1}\epsilon_i x_{ij}
\right),
\qquad
\epsilon_i\in\{\pm1\}.
\tag{3.1}
\]

There are `2^(n-1)` such Chow terms.

### Theorem 3.1 — restricted-family rigidity

The polynomials `G_epsilon` are linearly independent. Moreover, the unique expansion of `perm_n` in their span uses every one of the `2^(n-1)` terms with a nonzero coefficient. Consequently no proper subfamily of the column-uniform sign terms spans `perm_n`.

### Proof

A monomial in (3.1) chooses one row in each column. Let `c_i` be the number of chosen entries from row `i`. Its coefficient in `G_epsilon` is

\[
\prod_i\epsilon_i^{c_i},
\]

which depends only on

\[
p=(c_1,\ldots,c_{n-1})\pmod2
\in\mathbf F_2^{n-1}.
\]

Every parity vector occurs: choose `c_i=1` on its support and put the remaining count in row zero. The coefficient matrix between sign vectors and parity vectors is the Walsh--Hadamard matrix

\[
H_{p,z}=(-1)^{p\cdot z},
\qquad
HH^{\mathsf T}=2^{n-1}I.
\]

Therefore the `G_epsilon` are linearly independent.

The permanent is supported exactly on row words with every row count equal to one. This is the unique row-count vector with parity

\[
p_*=(1,\ldots,1).
\]

Hence its parity-class coefficient function is the delta function at `p_*`. Walsh inversion gives

\[
\operatorname{perm}_n
=
2^{1-n}
\sum_z
(-1)^{p_*\cdot z}G_z.
\]

Every coefficient is nonzero, so the support of the expansion is uniquely all `2^(n-1)` sign terms. ∎

For `n=6`, the restricted family therefore requires all 32 terms. In particular, no 25-term decomposition exists inside this natural Glynn subfamily.

The script

```text
scripts/glynn_family_rigidity_audit.py
```

checks the exact Walsh identities and the nonzero coefficient support for `2<=n<=10`.

### Claim boundary

This is a restricted-family theorem, not a Chow-rank lower bound. General Chow terms may use arbitrary and column-dependent linear forms.

## 4. Route decision

The exact comparison gives three negative but useful conclusions.

1. The first higher-wedge rank ratio does not improve the existing integer lower bounds.
2. The scalar second-shadow dimension is vacuous for the fixed counts `q=6,7,8`.
3. The most immediate structured decomposition family cannot be shortened below Glynn's 32 terms.

No tested route has a strict global ceiling capable of proving lower 26. Therefore none is promoted to a large proof program.

The next authorized target is narrower:

> find a bulk invariant that uses the **structure** of a coupled second shadow or of the higher-Koszul homology, rather than only its dimension; in parallel, test a strictly larger but still finite structured decomposition family with column-dependent sign patterns.

A route must first produce a global numerical margin or an exact counterexample before any state registry, SAT layer, Hilbert-scheme computation, or workflow abstraction is added.

## 5. Reproduction

Run

```bash
python scripts/n6_second_koszul_rank_audit.py \
  --json /tmp/n6_second_koszul_rank_audit.json
python scripts/glynn_family_rigidity_audit.py \
  --json /tmp/glynn_family_rigidity_audit.json
python -m unittest \
  tests.test_n6_alternative_route_audits -v
```

Expected final markers:

```text
N6_SECOND_KOSZUL_RANK_AUDIT_PASS
GLYNN_FAMILY_RIGIDITY_AUDIT_PASS
```
