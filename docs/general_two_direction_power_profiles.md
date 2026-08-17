# Two-direction apolar power profiles for the permanent

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_SUBQUOTIENT_THEOREM`,
`FINITE_ROUTE_DIAGNOSTIC`, `EXACT_INTEGER_REPLAYED`.

This note introduces a two-direction invariant that is compatible with the
actual apolar algebra of a sum. It proves the required subquotient theorem,
reduces every single Chow term to a squarefree Boolean envelope, and computes
the complete homogeneous power-profile method for `3<=n<=6`.

The finite conclusion is negative:

```text
n                         3   4   5   6
best two-direction bound  3   6  10  20
existing repository bound 4   8  16  28
```

Thus homogeneous powers of one two-plane do not improve any current small-`n`
bound. This is not a theorem that every two-direction module invariant is
weak, and it introduces no new Chow-rank number.

## 1. Apolar modules and the coupled-safe interface

Let

\[
S=\operatorname{Sym}(V^*)
\]

be the differential-operator ring and put

\[
A_f=S/f^\perp.
\]

The grading on `S` makes `A_f` a finite graded module. Fix a two-dimensional
subspace

\[
W\subseteq S_1.
\]

Restricting scalars makes `A_f` a graded module over

\[
R=\operatorname{Sym}(W)\cong k[s,t].
\]

This construction uses the apolar ideal of the actual polynomial sum. It does
not replace a coupled catalectic image by the literal sum of termwise images.

### Theorem 1.1 -- apolar subquotient for a Chow decomposition

If

\[
f=T_1+\cdots+T_r,
\]

then, for every `W subseteq S_1`, the `R`-module `A_f` is a quotient of an
`R`-submodule of

\[
\bigoplus_{i=1}^r A_{T_i}.
\]

Equivalently, `A_f` is an `R`-subquotient of the direct sum of the termwise
apolar algebras.

### Proof

Let

\[
I=\bigcap_{i=1}^r T_i^\perp.
\]

Every operator in `I` annihilates each `T_i`, hence annihilates their sum, so

\[
I\subseteq f^\perp.
\]

The diagonal map gives an injection

\[
S/I\hookrightarrow\bigoplus_i S/T_i^\perp,
\]

while the ideal inclusion gives a surjection

\[
S/I\twoheadrightarrow S/f^\perp=A_f.
\]

Both maps are graded `S`-linear and therefore graded `R`-linear after
restriction of scalars. ∎

The intermediate module `S/I` is essential. In general one cannot replace it
by either `A_f` or the direct sum of the termwise derivative spaces.

## 2. Homogeneous two-direction power profiles

For integers `p>=0` and `d`, define

\[
\Lambda_{p,d}(M;W)
=
\dim\operatorname{im}\left(
\operatorname{Sym}^pW\otimes M_{d-p}
\longrightarrow M_d
\right).
\tag{2.1}
\]

Equivalently,

\[
\Lambda_{p,d}(M;W)=\dim (W^pM)_{d}.
\]

### Proposition 2.1 -- monotonicity

The function `Lambda_(p,d)` has the following properties.

1. It is additive on direct sums.
2. If `N subseteq M`, then
   \[
   \Lambda_{p,d}(N;W)\le\Lambda_{p,d}(M;W).
   \]
3. If `M -> Q` is surjective, then
   \[
   \Lambda_{p,d}(Q;W)\le\Lambda_{p,d}(M;W).
   \]

### Proof

The image `W^pN` is contained in `W^pM`. Under a quotient map, `W^pQ` is a
quotient of the image of `W^pM`. Direct sums are componentwise. ∎

Combining Proposition 2.1 with Theorem 1.1 gives

\[
\Lambda_{p,d}(A_f;W)
\le
\sum_{i=1}^r\Lambda_{p,d}(A_{T_i};W).
\tag{2.2}
\]

## 3. Every Chow term has a Boolean envelope

Let

\[
T=\ell_1\cdots\ell_n
\]

with no independence assumption on the factors. Define the squarefree
Boolean algebra

\[
B_n=k[z_1,\ldots,z_n]/(z_1^2,\ldots,z_n^2).
\]

For a differential direction `D in V^*`, put

\[
\rho_T(D)=\sum_{i=1}^nD(\ell_i)z_i.
\tag{3.1}
\]

This extends to a graded algebra homomorphism `rho_T:S->B_n`.

### Theorem 3.1 -- Boolean single-term envelope

The apolar algebra `A_T` is a quotient of the graded `S`-submodule

\[
\operatorname{im}\rho_T\subseteq B_n.
\]

Consequently it is a `k[W]`-subquotient of `B_n`, where `W` acts through the
at-most-two-dimensional space `rho_T(W) subseteq (B_n)_1`.

### Proof

For a homogeneous differential operator `P` of degree `q`, write

\[
\rho_T(P)=\sum_{|I|=q}c_Iz_I.
\]

Direct differentiation gives

\[
P(T)
=q!\sum_{|I|=q}c_I\prod_{j\notin I}\ell_j.
\tag{3.2}
\]

Therefore `rho_T(P)=0` implies `P(T)=0`, so

\[
\ker\rho_T\subseteq T^\perp.
\]

Hence

\[
S/\ker\rho_T\cong\operatorname{im}\rho_T
\twoheadrightarrow
S/T^\perp=A_T.
\]

The assertion remains valid when the factors are dependent. In that case
`im rho_T` may be a proper submodule of `B_n`, and further relations among the
actual subproducts are absorbed by the final quotient. ∎

This subquotient formulation is deliberately weaker than saying that every
formal factor-subproduct is itself an actual derivative. That stronger
statement is false for dependent factors and is not used here.

## 4. The general two-direction lower bound

Define the exact Boolean envelope

\[
\beta_{n,p,d}
=
\max_{\dim U\le2}
\dim\operatorname{im}\left(
\operatorname{Sym}^pU\otimes(B_n)_{d-p}
\longrightarrow(B_n)_d
\right).
\tag{4.1}
\]

### Corollary 4.1

For every degree-`n` form `f`, every two-plane `W subseteq S_1`, and every
legal `p,d`,

\[
\boxed{
\operatorname{ChowRank}(f)
\ge
\left\lceil
\frac{\Lambda_{p,d}(A_f;W)}{\beta_{n,p,d}}
\right\rceil.
}
\tag{4.2}
\]

### Proof

Apply Theorem 3.1 to each term in a Chow decomposition, then use (2.2) and the
definition of `beta_(n,p,d)`. ∎

The denominator is a maximum over all induced pairs of Boolean linear forms.
No genericity assumption on the factors of a Chow term is needed.

## 5. Universal rank caps

Let `M` be any finite graded commutative algebra, let

\[
h_j=\dim M_j,
\]

and let `W subseteq M_1` have dimension at most two. The multiplication map in
(2.1) has the immediate upper bound

\[
\Lambda_{p,d}(M;W)
\le
\min\{h_d,(p+1)h_{d-p}\}.
\tag{5.1}
\]

There is one useful uniform sharpening when `d-p=1`.

### Lemma 5.1 -- source-degree-one commutativity syzygies

If `dim W=2`, then

\[
\boxed{
\Lambda_{p,p+1}(M;W)
\le
\min\{h_{p+1},(p+1)h_1-p\}.
}
\tag{5.2}
\]

### Proof

The source contains

\[
\operatorname{Sym}^pW\otimes W.
\]

Multiplication on this subspace factors through

\[
\operatorname{Sym}^{p+1}W.
\]

The first space has dimension `2(p+1)` and the second has dimension at most
`p+2`, so the restricted kernel has dimension at least `p`. These are the
standard commutativity relations

\[
s^{p-j}t^j\otimes t
-
s^{p-j-1}t^{j+1}\otimes s,
\qquad 0\le j<p.
\]

They remain in the kernel of the complete source map. ∎

For `B_n`, one has `h_d=binom(n,d)`. For the permanent apolar algebra,

\[
\dim(A_{\operatorname{perm}_n})_d=\binom nd^2.
\tag{5.3}
\]

A normalized basis is indexed by pairs `(I,J)` of `d`-subsets. Multiplication
by the differential direction with coefficient matrix `C=(c_ij)` is

\[
e_{I,J}
\longmapsto
\sum_{i\notin I,\,j\notin J}
c_{ij}e_{I\cup\{i\},J\cup\{j\}}.
\tag{5.4}
\]

## 6. Exact finite replay for `3<=n<=6`

The primary implementation uses bitmask bases and composes one-step
multiplication maps. The independent implementation instead computes the
coefficient of `L_0^(p-j)L_1^j` directly from the final added row and column
sets, summing over all bijections and all choices of the `j` right-form
edges. The two implementations share no matrix generator.

For every

\[
3\le n\le6,
\qquad
1\le p\le d\le n,
\]

the deterministic Boolean pair

\[
u=\sum_i z_i,
\qquad
v=\sum_i(i+1)z_i
\]

and two fixed integer permanent matrices attain the upper bounds (5.1)--(5.2).
Therefore those bounds are the exact maxima over all two-planes in these
finite cases.

The exact best ratios are

| `n` | best `(p,d)` | permanent profile | Boolean envelope | exact ratio | certified bound | existing bound |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | `(1,2)` | 9 | 3 | `3` | 3 | 4 |
| 4 | `(1,2)` | 31 | 6 | `31/6` | 6 | 8 |
| 5 | `(1,3)` | 100 | 10 | `10` | 10 | 16 |
| 6 | `(1,3)` | 400 | 20 | `20` | 20 | 28 |

The complete replay contains

```text
homogeneous (n,p,d) profile entries      52
Boolean and permanent cap equalities    104
independent decisive profile checks       4
independent higher-power checks            3
```

A modular rank `r` is used only to exhibit an integer `r`-minor that is
nonzero modulo `1,000,003`, hence nonzero in characteristic zero. The matching
upper bound always comes from (5.1) or (5.2). Finite-field equality is not
silently promoted.

## 7. Research interpretation

The two-direction construction is mathematically valid and preserves more
information than one scalar derivative dimension. Nevertheless, the
homogeneous maximal-ideal powers

\[
W, W^2, W^3,\ldots
\]

do not improve even the current small-`n` regression bounds through `n=6`.
The best cells are again the central first-power cells.

This does **not** prove that the complete `k[s,t]`-module route is capped at the
central binomial coefficient. The following information has not been tested
or bounded here:

1. images `IM` for arbitrary homogeneous ideals `I subset k[s,t]` rather than
   only powers `(s,t)^p`;
2. relation-sensitive data that remains monotone under subquotients;
3. multigraded or representation-valued coupling between different
   differential two-planes;
4. Chow-realizability restrictions on the termwise Boolean envelope.

The next fail-closed interface is therefore the image profile

\[
I\longmapsto\dim(IM)_d
\]

for small canonical homogeneous ideals `I subset k[s,t]`. This remains
additive on direct sums and monotone under submodules and quotients. A search
must first beat the exact `n<=6` regression boundary before any asymptotic
promotion.
