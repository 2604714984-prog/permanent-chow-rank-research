# A central-binomial ceiling for rectangular row--column symmetry projections

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_MODULAR_INTERFACES_REPLAYED`.

Let

\[
X_m=\binom{[n]}m,
\qquad
M_m=k^{X_m}.
\]

The degree-`m` derivative space of the permanent is naturally

\[
E_m=\mathcal D_m(\operatorname{perm}_n)
\simeq M_m\boxtimes M_m
\]

under the row and column permutation group `S_n x S_n`.

This note considers a catalecticant followed by a **rectangular symmetry
projection**

\[
E_m\longrightarrow A\boxtimes B,
\]

where `A,B` are nonzero sums of Johnson isotypes in `M_m`.  The main theorem is

\[
\boxed{
\frac{
\operatorname{rank}F_{A,B}(\operatorname{perm}_n)
}{
\max_T\operatorname{rank}F_{A,B}(T)
}
\le
\min\{\dim A,\dim B\}
\le
\binom nm.
}
\]

The same ceiling holds for every finite block-diagonal sum of rectangular
projections.  Maximizing over `m` gives the central binomial coefficient.

This is a route ceiling, not an upper bound on actual Chow rank.  It does not
cover a single projection onto an arbitrary nonrectangular union of isotype
pairs, row--column projections of higher Koszul maps, arbitrary Pieri maps,
higher syzygies, nonlinear minors, valuative arguments or Chow-realizability
defects.

## 1. Canonical permanent projection

A degree-`m` matching monomial has a unique row set `R` and column set `C`.
Let `p_(R,C)` be the corresponding `m x m` subpermanent.  Distinct pairs
`(R,C)` have disjoint monomial supports.

Define the row--column equivariant linear map

\[
\rho_m:\operatorname{Sym}^m(k^{n\times n})\longrightarrow E_m
\]

by

\[
\rho_m(x_\sigma)=\frac1{m!}p_{R,C}
\]

for a matching monomial on `(R,C)`, and by zero on nonmatching monomials.
Then `rho_m` is the identity on `E_m`.

For nonzero `S_n`-submodules `A,B subset M_m`, let `P_A,P_B` be the canonical
self-adjoint isotypic projections and define

\[
F_{A,B}(f)
=
(P_A\otimes P_B)\rho_m C_{n-m,m}(f).
\]

The map is linear in `f`, so its rank ratio is a valid Chow-rank lower-bound
mechanism.

## 2. Permanent numerator

The catalecticant of the permanent is onto `E_m`.  Since `rho_m` is the
identity there,

\[
\boxed{
\operatorname{rank}F_{A,B}(\operatorname{perm}_n)
=\dim A\,\dim B.
}
\]

## 3. The diagonal Chow-term witness

Take the independent-factor Chow term

\[
T_\Delta=\prod_{i=1}^n x_{ii}.
\]

Its degree-`m` derivative space has basis

\[
x_S=\prod_{i\in S}x_{ii},
\qquad S\in X_m.
\]

Under `rho_m`, this basis maps, up to the common scalar `1/m!`, to

\[
e_S\otimes e_S\in M_m\otimes M_m.
\]

Thus the projected one-term rank is the rank of

\[
D_{A,B}:M_m\longrightarrow A\otimes B,
\qquad
D_{A,B}(e_S)=P_Ae_S\otimes P_Be_S.
\]

## 4. A transitive multiplication lemma

### Lemma

Let a finite group `G` act transitively on a finite set `X`, and let
`M=k^X` over an infinite field.  If `A,B` are nonzero `G`-stable subspaces,
then the pointwise multiplication map

\[
\mu:A\otimes B\longrightarrow M,
\qquad
(a,b)\longmapsto ab
\]

has rank at least

\[
\max\{\dim A,\dim B\}.
\]

### Proof

For every `x in X`, evaluation at `x` is nonzero on `A`.  Otherwise
transitivity would force every coordinate evaluation to vanish on `A`, hence
`A=0`.  The kernels of the finitely many evaluations are proper hyperplanes.
Since the field is infinite, their union does not cover `A`.  Choose
`a in A` with

\[
a(x)\ne0\quad\text{for every }x.
\]

Multiplication by `a` is then injective on all of `M`, hence on `B`.  Therefore
`rank(mu)>=dim B`.  Interchanging `A` and `B` gives the other inequality. ∎

Under the standard invariant pairings, `D_(A,B)` is the transpose of `mu`.
Consequently

\[
\boxed{
\operatorname{rank}D_{A,B}
\ge
\max\{\dim A,\dim B\}.
}
\]

## 5. Route ceiling

The diagonal term is one admissible Chow term, so

\[
\max_T\operatorname{rank}F_{A,B}(T)
\ge
\max\{\dim A,\dim B\}.
\]

Combining with the permanent numerator gives

\[
\frac{\dim A\dim B}{\max_T\operatorname{rank}F_{A,B}(T)}
\le
\min\{\dim A,\dim B\}.
\]

Every Johnson isotype sum lies inside `M_m`, hence

\[
\min\{\dim A,\dim B\}
\le
\dim M_m
=\binom nm.
\]

This proves the theorem.

For a finite block-diagonal family `(A_r,B_r)`, use the same diagonal term in
every block.  The permanent numerator is

\[
\sum_r\dim A_r\dim B_r,
\]

while the one-term denominator is at least

\[
\sum_r\max\{\dim A_r,\dim B_r\}.
\]

Since each product is at most `binom(n,m)` times the corresponding maximum,
the same ceiling follows.

## 6. Individual isotypes

The Johnson permutation module is multiplicity free:

\[
M_m
=\bigoplus_{i=0}^{\min(m,n-m)}
S^{(n-i,i)}.
\]

Its isotype dimensions are

\[
d_i=\binom ni-\binom n{i-1}.
\]

For an individual pair `(i,j)`, the projected permanent rank is `d_i d_j`,
while the diagonal term rank is at least `max(d_i,d_j)`.  Therefore the route
ratio is at most

\[
\min(d_i,d_j)\le\binom nm.
\]

Thus selecting one row--column isotype cannot evade the scalar central
binomial barrier.

## 7. GL(V)-equivariant projections of the standard Koszul differential

There is also no hidden refinement obtained by projecting only the standard
exterior differential through ambient `GL(V)` isotypes.  Pieri's rule gives

\[
\operatorname{Sym}^mV\otimes\Lambda^pV
\simeq
S_{(m+1,1^{p-1})}V
\oplus
S_{(m,1^p)}V,
\]

and

\[
\operatorname{Sym}^{m-1}V\otimes\Lambda^{p+1}V
\simeq
S_{(m,1^p)}V
\oplus
S_{(m-1,1^{p+1})}V,
\]

with the evident boundary conventions.  The exterior differential is
`GL(V)`-equivariant, is nonzero, and its only common irreducible is the
multiplicity-one hook

\[
S_{(m,1^p)}V.
\]

By Schur's lemma it is zero on the unmatched component and an isomorphism,
up to scalar, on the common hook.  Hence any `GL(V)`-equivariant isotypic
projection inserted immediately before or after the standard differential
either kills the map or leaves a scalar multiple of it.  Such a projection is
not a new flattening.

This observation does not close projections involving the f-dependent
catalecticant source, external `S_n x S_n` symmetry, or arbitrary Pieri maps.

## 8. Exact replay

The primary implementation constructs the primitive Johnson idempotents as
polynomials in the Johnson graph adjacency matrix modulo `1,000,003`.
For every `2<=n<=9`, every `m<=n/2`, and every isotype rectangle, it verifies

```text
projected diagonal rank >= max(isotype dimensions)
route ceiling <= binom(n,m).
```

The independent implementation uses a second prime and obtains the same
isotype projectors from nested subset-incidence spaces and exact Gram
inversion.  It imports none of the primary implementation.

The finite computations replay the representation interface.  The general
theorem is the transitive multiplication lemma and does not rely on modular
extrapolation.
