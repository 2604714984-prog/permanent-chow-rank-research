# Fitting and Betti data across apolar subquotients

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_ROUTE_BARRIER`,
`EXACT_FINITE_LENGTH_REPLAYED`.

This note audits the next relation-sensitive candidates after the bounded
matrix-image ceilings:

1. Fitting ideals of the two-direction apolar module;
2. graded Betti tables and raw syzygy counts; and
3. Fitting valuations after collapsing the two-plane to one operator.

The conclusions are deliberately asymmetric.

- Raw **higher Fitting profiles** and raw **Betti tables** do not have the
  functoriality required by the apolar subquotient theorem.
- Standard colength, Hilbert-function and radical scalarizations of
  `Fitt_0` are not additive on direct sums.
- The complete Fitting valuation profile of one differential operator is
  exactly equivalent to its Jordan partition. Every additive
  subquotient-monotone scalar of that partition is a nonnegative combination
  of Jordan tails, so the entire one-operator Fitting route is already covered
  by the one-direction Jordan barrier.

The note does **not** close every possible use of `Fitt_0`, a genuinely
two-dimensional joint determinantal construction, derived Fitting ideals,
representation-valued syzygies, or Chow-realizability defects. It introduces
no new numerical Chow-rank lower bound.

## 1. The apolar functoriality gate

Let

\[
R=k[s,t]
\]

and let `A_f` be the apolar algebra of a form `f`, viewed as a finite-length
graded `R`-module through a chosen differential two-plane.

For a Chow decomposition

\[
f=T_1+\cdots+T_r,
\]

the existing apolar theorem supplies an intermediate `R`-module `C` with

\[
C\hookrightarrow\bigoplus_{i=1}^r A_{T_i},
\qquad
C\twoheadrightarrow A_f.
\tag{1.1}
\]

Therefore a numerical invariant used in a rank ratio must be:

1. additive on direct sums;
2. nonincreasing under submodules; and
3. nonincreasing under quotients.

Failure of either monotonicity cannot be repaired by testing only generic
independent-factor Chow terms. The Boolean envelope is a subquotient statement
and includes dependent-factor terms.

## 2. Fitting ideals: the valid facts

For a finite presentation

\[
R^a\xrightarrow{P}R^b\longrightarrow M\longrightarrow0,
\]

write

\[
\operatorname{Fitt}_i(M)=I_{b-i}(P).
\]

The usual conventions are `I_0(P)=R` and `I_j(P)=0` when the requested minors
are too large.

### Proposition 2.1 -- quotient functoriality

If

\[
M\twoheadrightarrow Q,
\]

then

\[
\boxed{
\operatorname{Fitt}_i(M)
\subseteq
\operatorname{Fitt}_i(Q)
}
\tag{2.1}
\]

for every `i`.

### Proof

Choose generators of `M` and use their images as a possibly nonminimal
generating set of `Q`. A presentation matrix for `Q` is obtained by adjoining
relation columns to a presentation matrix for `M`. Every minor generating
`Fitt_i(M)` remains a minor of the enlarged matrix. Fitting ideals are
independent of the chosen presentation. ∎

### Proposition 2.2 -- direct-sum convolution

\[
\boxed{
\operatorname{Fitt}_k(M\oplus N)
=
\sum_{i+j=k}
\operatorname{Fitt}_i(M)
\operatorname{Fitt}_j(N).
}
\tag{2.2}
\]

### Proof

Use the block-diagonal direct sum of presentation matrices and expand its
minors according to how many rows and columns are selected from each block.
∎

Equation (2.2) is multiplicative/convolutional ideal data. It is not additive
numerical data of the kind required by (1.1).

## 3. Higher Fitting ideals have no submodule order

Put

\[
\mathfrak m=(s,t).
\]

All examples below are finite-length graded `R`-modules.

### Example 3.1 -- one direction

The diagonal map gives an injection

\[
k=R/\mathfrak m
\hookrightarrow
k^2.
\]

Explicit presentations give

\[
\operatorname{Fitt}_1(k)=R,
\qquad
\operatorname{Fitt}_1(k^2)=\mathfrak m.
\tag{3.1}
\]

Thus the ambient module's first Fitting ideal is properly contained in that of
the submodule.

### Example 3.2 -- the opposite direction

Inside

\[
R/\mathfrak m^2
\]

the degree-one ideal is

\[
\mathfrak m/\mathfrak m^2
\cong
k(-1)^2.
\]

Hence

\[
\mathfrak m/\mathfrak m^2
\hookrightarrow
R/\mathfrak m^2.
\]

But

\[
\operatorname{Fitt}_1(\mathfrak m/\mathfrak m^2)
=
\mathfrak m,
\qquad
\operatorname{Fitt}_1(R/\mathfrak m^2)
=
R.
\tag{3.2}
\]

Now the submodule's first Fitting ideal is properly contained in that of the
ambient module.

Equations (3.1) and (3.2) prove that neither ideal-inclusion direction is
valid for `Fitt_1` under submodules. Consequently the full ideal-valued
higher-Fitting profile cannot be inserted automatically into the apolar
subquotient inequality.

This does not assert that every specially chosen scalar of `Fitt_0` fails.
Such a scalar must be proved separately.

## 4. Standard `Fitt_0` scalarizations are not additive

For a cyclic quotient,

\[
\operatorname{Fitt}_0(R/I)=I.
\]

For `k` and `k^2`, equation (2.2) gives

\[
\operatorname{Fitt}_0(k)=\mathfrak m,
\qquad
\operatorname{Fitt}_0(k^2)=\mathfrak m^2.
\]

Therefore

\[
\ell(R/\operatorname{Fitt}_0(k))=1,
\qquad
\ell(R/\operatorname{Fitt}_0(k^2))=3,
\]

not `2`. Degreewise Hilbert functions fail additivity for the same reason.
Taking radicals is worse:

\[
\sqrt{\operatorname{Fitt}_0(k^r)}
=
\mathfrak m
\]

for every positive `r`, so support data forgets the number of summands.

A divisorial or order valuation can turn products into sums, but it still
requires a separate submodule theorem. The present note does not assume that
theorem.

## 5. Raw Betti tables fail both monotonicities

Write total Betti numbers as

\[
(\beta_0,\beta_1,\beta_2)
\]

over `R=k[s,t]`.

### Proposition 5.1 -- quotient counterexample

There is a graded surjection

\[
R/(s^2,t^2)
\twoheadrightarrow
R/\mathfrak m^2
\tag{5.1}
\]

because

\[
(s^2,t^2)\subset\mathfrak m^2.
\]

The minimal resolutions are

\[
0\to R(-4)
\to R(-2)^2
\to R
\to R/(s^2,t^2)
\to0,
\]

and

\[
0\to R(-3)^2
\to R(-2)^3
\to R
\to R/\mathfrak m^2
\to0.
\]

Thus

\[
(1,2,1)
\longmapsto
(1,3,2).
\tag{5.2}
\]

Both `beta_1` and `beta_2` increase under the quotient.

### Proposition 5.2 -- submodule counterexample

The inclusion

\[
\mathfrak m/\mathfrak m^2
\cong k(-1)^2
\hookrightarrow
R/\mathfrak m^2
\tag{5.3}
\]

has Betti totals

\[
(2,4,2)
\hookrightarrow
(1,3,2).
\tag{5.4}
\]

Hence `beta_0` and `beta_1` are larger for the submodule than for the ambient
module.

The examples are graded and finite length. They rule out raw total Betti
numbers, individual graded Betti entries, and unproved raw syzygy counts as
automatic invariants in (1.1).

## 6. One-operator Fitting data is exactly Jordan data

Let a single differential operator `L` act on a finite-dimensional apolar
module. Regard the module as a finite-length `k[u]`-module with `u` acting by
`L`.

By the structure theorem,

\[
M
\cong
\bigoplus_{i=1}^r k[u]/(u^{\lambda_i}),
\qquad
1\le\lambda_1\le\cdots\le\lambda_r.
\tag{6.1}
\]

A diagonal presentation gives, for `0<=j<r`,

\[
\boxed{
\operatorname{Fitt}_j^{k[u]}(M)
=
\left(
u^{\lambda_1+\cdots+\lambda_{r-j}}
\right),
}
\tag{6.2}
\]

where the symbol in the displayed principal ideal is the polynomial variable
`u`.

Indeed, the minimum exponent among all `(r-j)`-minors is the sum of the
`r-j` smallest invariant factors, and that monomial divides every other
minor.

If

\[
\nu_j
=
\operatorname{ord}_u\operatorname{Fitt}_j(M),
\]

then

\[
\lambda_{r-j}
=
\nu_j-\nu_{j+1}.
\tag{6.3}
\]

Thus the complete Fitting valuation profile and the complete Jordan partition
determine one another.

## 7. Every admissible one-operator scalar lies in the Jordan-tail cone

For a partition `lambda`, define the Jordan tails

\[
b_s(M)
=
\#\{i:\lambda_i\ge s\}.
\tag{7.1}
\]

### Theorem 7.1

Let `Phi` be a real-valued invariant of finite-length `k[u]`-modules which:

1. depends only on the isomorphism class;
2. is additive on direct sums; and
3. is nonincreasing under submodules and quotients.

Then there are nonnegative numbers `w_s` such that

\[
\boxed{
\Phi(M)
=
\sum_{s\ge1}w_s b_s(M).
}
\tag{7.2}
\]

### Proof

Additivity gives

\[
\Phi(M)=\sum_i g(\lambda_i),
\qquad
g(a)=\Phi(k[u]/(u^a)).
\]

The natural quotient

\[
k[u]/(u^a)\twoheadrightarrow k[u]/(u^{a-1})
\]

and the zero submodule imply

\[
0=g(0)\le g(1)\le g(2)\le\cdots.
\]

Set

\[
w_s=g(s)-g(s-1)\ge0.
\]

Then

\[
g(a)=\sum_{s=1}^a w_s,
\]

and summing over the blocks gives (7.2). ∎

For the Boolean single-term envelope and the permanent apolar algebra, the
strong-Lefschetz Jordan-tail ratios are

\[
\frac{
b_{n-2j+1}(A_{\operatorname{perm}_n})
}{
b_{n-2j+1}(B_n)
}
=
\frac{\binom nj^2}{\binom nj}
=
\binom nj.
\tag{7.3}
\]

Every nonnegative weighted ratio in (7.2) is bounded by the largest component
ratio. Therefore the complete class of admissible one-operator Fitting/Jordan
scalars proves at most

\[
\boxed{
\binom n{\lfloor n/2\rfloor}.
}
\tag{7.4}
\]

The result closes all scalarizations of Fitting data that first collapse the
two-plane to one operator. It does not close genuinely joint variation over
the whole differential plane.

## 8. Exact replay

The primary implementation reconstructs named presentation minors over
`Z[s,t]`, verifies the direct-sum convolution examples, checks the minimal
graded resolutions by Hilbert series, and exhausts every integer partition of
total size at most twelve.

The independent implementation uses the two-variable monomial
Hilbert--Burch rule instead of the primary presentation-minor machinery.

Required exact outputs are:

```text
Fitting submodule direction counterexamples    2
Betti quotient counterexamples                 1
Betti submodule counterexamples                1
integer partitions checked                   271
one-operator tail-ratio cells                n=2..20
```

Finite-field ranks are not used. Every example and resolution is over
`Z[s,t]` and therefore valid in characteristic zero.

## 9. Research decision

The route frontier becomes:

```text
raw higher Fitting ideals                 NOT SUBMODULE-MONOTONE
colength/Hilbert/radical of Fitt_0         NOT ADDITIVE OR TOO COARSE
raw graded Betti tables                    NOT SUBQUOTIENT-MONOTONE
one-operator Fitting valuations            EQUIVALENT TO CLOSED JORDAN ROUTE

special Fitt_0 valuation with a proof      OPEN
joint two-dimensional determinantal data   OPEN
derived/additive Fitting construction       OPEN
representation-valued syzygy envelope       OPEN
Chow-realizability defect                   OPEN
```

The next default continuation should not use raw Betti counts or another
one-line Fitting valuation. A candidate must first prove the exact
submodule/quotient and direct-sum laws needed by (1.1).
