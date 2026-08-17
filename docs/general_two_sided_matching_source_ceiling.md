# Two-sided matching-source compressions are centrally capped

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

This note closes the row--column representation projections that act on the
differential-operator source **before** the permanent catalecticant, provided
they factor through the canonical matching-source section. It also proves a
stronger symmetric-compression statement that does not require representation
stability.

Let

\[
q_{n,m}=\binom nm.
\]

For every fixed subspace of the effective matching module, the same
orthogonal compression on the source and target gives a rank-ratio route
bounded by `q_(n,m)`. More generally, arbitrary row--column equivariant
pre- and post-endomorphisms of that multiplicity-free module obey the same
ceiling. Finite block-diagonal families across derivative degrees are capped
by the central binomial coefficient.

This is a ceiling on a named fixed linear mechanism, not an upper bound on
actual Chow rank. It does not cover unrelated source and target subspaces,
source maps that do not factor through the matching section, minimal syzygy
functors depending on the input form, nonlinear minors, valuative data, or
Chow-realizability defects.

## 1. The effective matching module

Let

\[
V=\operatorname{span}\{x_{rc}:1\le r,c\le n\}
\]

and let

\[
X_m=\binom{[n]}m,
\qquad
M_m=k^{X_m}.
\]

The degree-`m` permanent derivative space is

\[
E_m
=\operatorname{span}\{p_{R,C}:R,C\in X_m\}
\simeq M_m\boxtimes M_m,
\tag{1.1}
\]

where `p_(R,C)` is the corresponding subpermanent. The canonical matching
projection

\[
Q_m:\operatorname{Sym}^mV\longrightarrow E_m
\tag{1.2}
\]

is the identity on `E_m`, sends a matching monomial with row--column support
`(R,C)` to `p_(R,C)/m!`, and kills nonmatching monomials.

### The canonical source section

Define

\[
J_m:E_m\longrightarrow\operatorname{Sym}^{n-m}V^*
\tag{1.3}
\]

on the subpermanent basis by

\[
J_m(p_{R,C})
=
\frac1{(n-m)!}
\sum_{\tau:R^c\overset\sim\longrightarrow C^c}
\prod_{r\in R^c}\partial_{r,\tau(r)}.
\tag{1.4}
\]

Every summand in (1.4) differentiates the permanent to the same
subpermanent. Therefore

\[
\boxed{
Q_m C_{n-m,m}(\operatorname{perm}_n)J_m
=\operatorname{id}_{E_m}.
}
\tag{1.5}
\]

Both `Q_m` and `J_m` are `S_n x S_n`-equivariant.

## 2. Matching terms become graph projectors

For a permutation `sigma in S_n`, put

\[
T_\sigma
=\prod_{r=1}^{n}x_{r,\sigma(r)}.
\tag{2.1}
\]

Let

\[
L_\sigma
=\operatorname{span}
\{e_R\otimes e_{\sigma(R)}:R\in X_m\}
\subseteq M_m\otimes M_m
\tag{2.2}
\]

and let `P_sigma` be its orthogonal coordinate projector.

For fixed `R,C`, exactly one partial matching in (1.4) survives on
`T_sigma` if `C=sigma(R)`, and none survives otherwise. The surviving output
is the complementary matching monomial. Applying `Q_m` gives

\[
\boxed{
Q_m C_{n-m,m}(T_\sigma)J_m
=
\frac1{m!(n-m)!}P_\sigma.
}
\tag{2.3}
\]

The nonzero scalar in (2.3) has no effect on rank.

## 3. Average of the graph projectors

The action of `S_n` on `X_m` is transitive. For every coordinate pair
`(R,C) in X_m x X_m`, the number of permutations satisfying

\[
\sigma(R)=C
\]

is exactly

\[
m!(n-m)!=\frac{n!}{q_{n,m}}.
\]

Hence

\[
\boxed{
\frac1{n!}
\sum_{\sigma\in S_n}P_\sigma
=
\frac1{q_{n,m}}I_{E_m}.
}
\tag{3.1}
\]

This is the source--target analogue of the graph-projector identity used for
fixed postprocessing, but now the graph projector is the complete effective
term catalecticant between the matching source and target copies.

## 4. Arbitrary symmetric compression

Let

\[
U\subseteq E_m
\]

be an arbitrary subspace and let `P_U` be its orthogonal projector. Define

\[
\Psi_U(f)
=
P_U Q_m C_{n-m,m}(f)J_m P_U.
\tag{4.1}
\]

For the permanent, equation (1.5) gives

\[
\operatorname{rank}\Psi_U(\operatorname{perm}_n)
=
\dim U.
\tag{4.2}
\]

For a matching term, equation (2.3) reduces the rank to that of

\[
P_U P_\sigma P_U.
\]

This operator is positive semidefinite on `U`, every eigenvalue lies in
`[0,1]`, and therefore

\[
\operatorname{rank}(P_U P_\sigma P_U)
\ge
\operatorname{tr}(P_U P_\sigma P_U).
\tag{4.3}
\]

Averaging (4.3) and using (3.1) gives

\[
\frac1{n!}
\sum_\sigma
\operatorname{tr}(P_U P_\sigma P_U)
=
\frac{\dim U}{q_{n,m}}.
\]

Consequently some matching term satisfies

\[
\operatorname{rank}\Psi_U(T_\sigma)
\ge
\left\lceil\frac{\dim U}{q_{n,m}}\right\rceil.
\]

### Theorem 4.1 -- symmetric two-sided ceiling

\[
\boxed{
\frac{
\operatorname{rank}\Psi_U(\operatorname{perm}_n)
}{
\max_T\operatorname{rank}\Psi_U(T)
}
\le
\binom nm.
}
\tag{4.4}
\]

No invariance of `U` is required.

## 5. Distinct row--column equivariant pre- and post-maps

The permutation module on `m`-subsets is multiplicity-free:

\[
M_m
\simeq
\bigoplus_{i=0}^{\min(m,n-m)}
S^{(n-i,i)}.
\tag{5.1}
\]

Therefore

\[
E_m
\simeq
\bigoplus_{i,j}
S^{(n-i,i)}\boxtimes S^{(n-j,j)}
\tag{5.2}
\]

is multiplicity-free as an `S_n x S_n`-module.

Let

\[
A,B\in\operatorname{End}_{S_n\times S_n}(E_m)
\]

be arbitrary equivariant endomorphisms, used after and before the effective
catalecticant. Define

\[
\Psi_{A,B}(f)
=
A Q_m C_{n-m,m}(f)J_m B.
\tag{5.3}
\]

By (5.2), both maps act by scalars on every irreducible summand. Let `Z` be the
sum of the summands on which both scalars are nonzero. Then

\[
\operatorname{rank}\Psi_{A,B}(\operatorname{perm}_n)
=
\dim Z.
\tag{5.4}
\]

On `Z`, the restrictions of `A` and `B` are invertible. Compressing a term map
to `Z` gives

\[
A|_Z\,P_ZP_\sigma P_Z\,B|_Z.
\]

Its rank is the rank of `P_ZP_sigmaP_Z`, and the full term map has at least
that rank. The argument of Section 4 now gives:

### Theorem 5.1 -- equivariant two-sided ceiling

\[
\boxed{
\frac{
\operatorname{rank}\Psi_{A,B}(\operatorname{perm}_n)
}{
\max_T\operatorname{rank}\Psi_{A,B}(T)
}
\le
\binom nm.
}
\tag{5.5}
\]

This covers different source and target row--column isotype projections, as
well as arbitrary equivariant linear combinations of those projections.

## 6. Finite block-diagonal families

Take finitely many derivative degrees and either symmetric compressions `U_a`
or equivariant pairs `(A_a,B_a)`. Let `z_a` be the permanent rank of block
`a`, and put

\[
q_a=\binom n{m_a}.
\]

Use the same matching permutation `sigma` in every block. Averaging the sum of
the compression traces gives a term with total rank at least

\[
\sum_a\frac{z_a}{q_a}.
\]

Hence the block-diagonal route satisfies

\[
\frac{\sum_a z_a}{\max_T\sum_a\operatorname{rank}\Psi_a(T)}
\le
\frac{\sum_a z_a}{\sum_a z_a/q_a}
\le
\max_a q_a
\le
\binom n{\lfloor n/2\rfloor}.
\tag{6.1}
\]

## 7. Routes closed and strict boundary

The theorem closes:

```text
same-subspace source/target compression through J_m and Q_m
arbitrary row-column isotype projection on the effective source
arbitrary row-column isotype projection on the target
arbitrary equivariant pre/post endomorphisms of E_m
finite block sums across derivative degrees
```

It does not cover:

```text
unrelated non-equivariant source and target subspaces
source maps not factoring through the canonical section J_m
minimal syzygy functors depending on f
arbitrary Pieri maps not factoring through the effective E_m core
nonlinear joint minors or determinantal intersections
valuative flat-sum data
Chow-realizability defects
```

## 8. Exact replay

The primary audit verifies the source-section graph formula and the exact
coordinate coverage for every `2<=n<=6` and every `1<=m<n`. It also checks
arbitrary dense rational subspaces for `3<=n<=5`, all row--column isotype
support arithmetic through `n=30`, and finite block-sum ceilings.

A second implementation imports none of the primary code. It explicitly
enumerates partial matchings for `n<=5`, uses different dense rational
subspaces, and reconstructs the common-permutation block-sum inequality.

The finite computations replay the interfaces. The general theorem is the
source-section identity plus the averaged positive-compression proof, not a
finite extrapolation.

## 9. Research consequence

Pre-catalecticant row--column representation projections do not escape the
central-binomial barrier when they act through the canonical effective
matching source. A successful source-sensitive representation method must now
use at least one of:

1. a source construction that does not factor through `J_m`;
2. unrelated non-equivariant source and target structures with a uniform
   one-term envelope;
3. a minimal or higher syzygy functor that depends on `f`;
4. nonlinear joint determinantal information; or
5. a Chow-realizability or valuative obstruction.
