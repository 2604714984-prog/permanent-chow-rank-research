# `n=6` coordinate secant geometry inside the central derivative space

## Status

`COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` — the finite pair and tangent calculations are exact and reproducible, but they do not prove an exact Chow-rank statement for `perm_6`.

## 1. Setup

Let

\[
E=\mathcal D_3(\operatorname{perm}_6).
\]

It has the coordinate basis

\[
\{P_{I,J}:I,J\in\tbinom{[6]}3\},
\qquad
\dim E=20^2=400,
\]

where `P_{I,J}` is the `3 x 3` subpermanent on row set `I` and column set `J`.

Consider the first catalecticant

\[
C_{1,2}(g):V^*\longrightarrow\operatorname{Sym}^2V
\]

for a cubic `g in E`. For one basis point `P_{I,J}`, the nine nonzero derivatives form a matching:

\[
x_{ij}
\longmapsto
P_{I\setminus\{i\},J\setminus\{j\}}
\qquad
(i\in I,\ j\in J).
\]

Hence

\[
\operatorname{rank}C_{1,2}(P_{I,J})=9.
\]

## 2. Exact rank on every coordinate line

Take two distinct coordinate basis points `P_{I,J}` and `P_{I',J'}`, and put

\[
r=|I\cap I'|,
\qquad
c=|J\cap J'|.
\]

### Proposition 2.1

For every pair of nonzero scalars `alpha,beta`,

\[
\boxed{
\operatorname{rank}C_{1,2}
\bigl(\alpha P_{I,J}+\beta P_{I',J'}\bigr)
=
18-rc-\binom r2\binom c2.
}
\tag{2.1}
\]

### Proof

The two catalectic matrices are matchings with nine edges each. Their union has 18 labelled edges before identifications.

A variable vertex is shared precisely when

\[
(i,j)\in(I\cap I')\times(J\cap J'),
\]

so there are `rc` shared variable vertices. At each such vertex, two edges form a rank-one two-edge star instead of two independent rank-one blocks; this lowers the rank by one.

An output vertex is a pair of two-subsets. The two matchings share an output precisely when the row two-subset lies in both `binom(I,2)` and `binom(I',2)`, and similarly for columns. Therefore the number of shared output vertices is

\[
\binom r2\binom c2.
\]

Each again merges two edges into one rank-one star.

For distinct coordinate points, no connected component contains both a shared variable and a shared output. Thus every component is either an isolated edge or a two-edge star, and the two rank losses add. This gives (2.1). ∎

## 3. Complete pair distribution

There are

\[
\binom{400}{2}=79,800
\]

unordered coordinate pairs. Exact enumeration gives:

| line rank | number of pairs | overlap types `(r,c)` |
|---:|---:|---|
| 9 | 3,600 | `(3,2)`, `(2,3)` |
| 13 | 16,200 | `(2,2)` |
| 15 | 3,600 | `(3,1)`, `(1,3)` |
| 16 | 32,400 | `(2,1)`, `(1,2)` |
| 17 | 16,200 | `(1,1)` |
| 18 | 7,800 | at least one overlap is zero |

In particular:

\[
\boxed{
\text{the next coordinate-line rank after }9\text{ is }13.
}
\]

A line remains in the rank-at-most-nine locus exactly when the two basis points have the same row triple and column overlap two, or the same column triple and row overlap two.

## 4. The tangent space at a coordinate point

Let

\[
p=P_{\{0,1,2\},\{0,1,2\}}.
\]

For the determinantal locus

\[
\mathcal R_9
=
\{[g]\in\mathbb P(E):
\operatorname{rank}C_{1,2}(g)\le9\},
\]

the standard tangent condition at `p` is

\[
C_{1,2}(h)(\ker C_{1,2}(p))
\subseteq
\operatorname{im}C_{1,2}(p).
\tag{4.1}
\]

For a coordinate direction `P_{I',J'}`, condition (4.1) holds exactly in the following cases:

1. `(I',J')=(I,J)`;
2. `I'=I` and `|J' intersection J|=2`;
3. `J'=J` and `|I' intersection I|=2`.

There are

\[
1+9+9=19
\]

such affine coordinate directions.

The exact tangent-map matrix has 400 columns. Its rank modulo `1,000,003` is 381. Therefore its rank over `Q` is at least 381. The 19 explicit tangent directions give characteristic-zero nullity at least 19, hence rank at most 381. Both bounds meet.

### Proposition 4.1

At every coordinate point,

\[
\boxed{
\dim T_p^{\mathrm{aff}}\mathcal R_9=19,
\qquad
\dim T_{[p]}\mathcal R_9=18.
}
\tag{4.2}
\]

Row-column permutations are transitive on the 400 coordinate points, so one exact representative proves the result for all of them.

## 5. Visible positive-dimensional branches

The tangent dimension is not an isolated-point artifact. Fix a row triple `I` and a two-column set `A`. The vector space

\[
\operatorname{span}
\{P_{I,A\cup\{b\}}:b\notin A\}
\]

has dimension four, and every nonzero element is obtained by replacing the third column of a `3 x 3` permanent by a linear combination of four ambient columns. Its first catalecticant has rank nine. There are three such column branches through a coordinate point, and three symmetric row branches.

Thus a coordinate rank-nine point lies on several positive-dimensional linear families. Any `n=6` argument that treats torus-fixed low-catalectic points as isolated is incorrect.

## 6. An elementary factorization lemma

The following observation helps interpret the row and column factors.

### Lemma 6.1

Let `f` be a nonzero homogeneous multi-affine polynomial of degree `d`. Its essential-variable dimension is at least `d`. Equality holds if and only if

\[
f=\lambda\ell_1\cdots\ell_d
\]

where the linear forms `ell_i` have pairwise disjoint supports in the original coordinate variables.

### Proof

The span of the first derivatives has dimension equal to the essential-variable dimension, so it is at least `d` for a nonzero degree-`d` form.

Assume equality. Choose `d` coordinate derivative directions whose restrictions form a basis of the essential dual space. In the dual variables `y_1,...,y_d`, multi-affineness gives

\[
\partial_{y_i}^2f=0
\]

for every `i`. A degree-`d` polynomial in `d` variables with this property is a scalar multiple of

\[
y_1\cdots y_d.
\]

For any other original coordinate derivative direction

\[
v=a_1\partial_{y_1}+\cdots+a_d\partial_{y_d},
\]

multi-affineness gives `D_v^2 f=0`. But

\[
D_v^2(y_1\cdots y_d)
=
2\sum_{i<j}a_i a_j
\prod_{h\ne i,j}y_h,
\]

and the displayed monomials are distinct. Hence `a_i a_j=0` for all `i!=j`; every original coordinate occurs in at most one `y_i`. The supports are therefore pairwise disjoint. The converse is immediate. ∎

For a rank-one coefficient tensor `u tensor v` in the row-column indexing of `E`, the first catalecticant factors as a Kronecker product of the row and column derivative matrices. Its rank is nine exactly when both multi-affine cubics have essential-variable dimension three, hence both are disjoint-support products as in Lemma 6.1.

## 7. Consequence for the exact-32 program

These computations do **not** disprove the conjectural value

\[
\operatorname{ChowRank}(\operatorname{perm}_6)=32.
\]

They do rule out a naive strategy:

> Degenerate a dangerous central intersection to coordinate rank-nine points and classify only isolated fixed points.

The coordinate boundary already has multiple positive-dimensional branches and an 18-dimensional projective tangent space at every fixed point. A viable exact-32 proof must either:

1. control these row/column replacement families uniformly;
2. use a stronger invariant than the first catalecticant rank-nine locus; or
3. prove that the dangerous central intersections cannot enter these branches.

No SAT, Hilbert-scheme, or Kuranishi layer should be introduced before one of these structural reductions produces a genuinely finite frontier.

## 8. Reproduction

```bash
python scripts/n6_coordinate_secant_audit.py
```

The required terminal marker is

```text
N6_COORDINATE_SECANT_AUDIT_PASS
```

The frozen output is `data/n6_coordinate_secant_audit.json`.
