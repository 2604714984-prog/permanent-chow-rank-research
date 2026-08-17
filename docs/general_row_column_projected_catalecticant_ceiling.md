# A central-binomial ceiling for all row--column isotype projections

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_MODULAR_INTERFACES_REPLAYED`.

Let

\[
X_m=\binom{[n]}m,
\qquad
M_m=k^{X_m},
\qquad
M=|X_m|=\binom nm.
\]

The degree-`m` derivative space of the permanent is naturally

\[
E_m=\mathcal D_m(\operatorname{perm}_n)
\simeq M_m\boxtimes M_m
\]

under the row and column permutation group `S_n x S_n`.

The Johnson permutation module is multiplicity free:

\[
M_m=\bigoplus_{i=0}^{s}U_i,
\qquad
s=\min(m,n-m),
\qquad
U_i\simeq S^{(n-i,i)}.
\]

For an arbitrary set of row--column isotype pairs

\[
\mathcal S\subseteq\{0,\ldots,s\}^2,
\]

put

\[
W_{\mathcal S}
=
\bigoplus_{(i,j)\in\mathcal S}U_i\boxtimes U_j
\subseteq E_m.
\]

The main theorem is

\[
\boxed{
\frac{
\operatorname{rank}F_{\mathcal S}(\operatorname{perm}_n)
}{
\max_T\operatorname{rank}F_{\mathcal S}(T)
}
\le
\binom nm,
}
\tag{0.1}
\]

where `T` ranges over degree-`n` Chow terms and `F_S` is the permanent
catalecticant followed by the fixed `S_n x S_n`-equivariant projection onto
`W_S`.

The theorem also allows independent fixed isotype-union filters on the source
and target of the permanent catalecticant, and finite block-diagonal sums of
such maps. Maximizing over `m` gives the central binomial coefficient.

This is a route ceiling, not an upper bound on actual Chow rank. It does not
cover row--column projections of higher Koszul maps, arbitrary Pieri maps,
higher representation-valued syzygies, nonlinear minors, valuative arguments
or Chow-realizability defects.

## 1. Canonical permanent projection

A degree-`m` matching monomial has a unique row set `R` and column set `C`.
Let `p_(R,C)` be the corresponding `m x m` subpermanent. Distinct pairs
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

Let `P_i` be the canonical self-adjoint projection from `M_m` onto `U_i`, and
put

\[
P_{\mathcal S}
=
\sum_{(i,j)\in\mathcal S}P_i\otimes P_j.
\]

Define

\[
F_{\mathcal S}(f)
=
P_{\mathcal S}\rho_m C_{n-m,m}(f).
\tag{1.1}
\]

The map is linear in `f`, so its matrix rank is subadditive on Chow sums.

## 2. Permanent numerator

The permanent catalecticant is onto `E_m`, and `rho_m` is the identity on
`E_m`. Therefore

\[
\boxed{
\operatorname{rank}F_{\mathcal S}(\operatorname{perm}_n)
=
\dim W_{\mathcal S}
=
\sum_{(i,j)\in\mathcal S}d_i d_j,
}
\tag{2.1}
\]

where

\[
d_i=\dim U_i=\binom ni-\binom n{i-1}.
\]

## 3. The diagonal Chow-term witness

Take

\[
T_\Delta=\prod_{r=1}^n x_{rr}.
\]

Its degree-`m` derivative space has basis

\[
x_S=\prod_{r\in S}x_{rr},
\qquad S\in X_m.
\]

Under `rho_m`, this basis maps, up to the common scalar `1/m!`, to

\[
e_S\otimes e_S\in M_m\otimes M_m.
\]

Let

\[
\Delta:M_m\longrightarrow M_m\otimes M_m,
\qquad
\Delta(e_S)=e_S\otimes e_S.
\]

The one-term rank after projection is

\[
\operatorname{rank}(P_{\mathcal S}\Delta).
\tag{3.1}
\]

Its Gram operator is

\[
G_{\mathcal S}
=
\Delta^*P_{\mathcal S}\Delta
=
\sum_{(i,j)\in\mathcal S}P_i\circ P_j,
\tag{3.2}
\]

where `circ` denotes entrywise product in the subset basis.

## 4. Krein expansion in the Johnson scheme

After scalar extension to the complex numbers, the Johnson scheme is a
symmetric association scheme. Its primitive idempotents satisfy

\[
P_i\circ P_j
=
\frac1M\sum_{k=0}^{s}q_{ij}^kP_k,
\qquad
q_{ij}^k\ge0.
\tag{4.1}
\]

The `q_(i,j)^k` are the Krein parameters. Two standard identities are all
that are needed.

### Lemma 4.1 -- dimension identity

\[
\boxed{
\sum_k q_{ij}^k d_k=d_i d_j.
}
\tag{4.2}
\]

### Proof

Every diagonal entry of `P_i` equals `d_i/M` by transitivity. Hence

\[
\operatorname{tr}(P_i\circ P_j)
=M\frac{d_i}{M}\frac{d_j}{M}
=
\frac{d_i d_j}{M}.
\]

Taking traces in (4.1) gives (4.2). ∎

### Lemma 4.2 -- total Krein budget

For every `k`,

\[
\boxed{
\sum_{i,j}q_{ij}^k=M.
}
\tag{4.3}
\]

### Proof

Since `sum_i P_i=I`,

\[
I
=I\circ I
=\sum_{i,j}P_i\circ P_j
=\frac1M\sum_k\left(\sum_{i,j}q_{ij}^k\right)P_k.
\]

Compare the coefficients of the linearly independent primitive idempotents. ∎

For the selected pair set, define

\[
q_{\mathcal S}^k
=
\sum_{(i,j)\in\mathcal S}q_{ij}^k.
\]

Equations (3.2) and (4.1) give

\[
G_{\mathcal S}
=
\frac1M\sum_k q_{\mathcal S}^kP_k.
\tag{4.4}
\]

Since the Krein parameters are nonnegative,

\[
0\le q_{\mathcal S}^k\le M.
\tag{4.5}
\]

Therefore

\[
\boxed{
\operatorname{rank}(P_{\mathcal S}\Delta)
=
\sum_{k:q_{\mathcal S}^k>0}d_k.
}
\tag{4.6}
\]

## 5. Arbitrary isotype-union ceiling

Using Lemma 4.1,

\[
\begin{aligned}
\dim W_{\mathcal S}
&=
\sum_{(i,j)\in\mathcal S}d_i d_j\\
&=
\sum_k q_{\mathcal S}^k d_k\\
&\le
M\sum_{k:q_{\mathcal S}^k>0}d_k\\
&=
M\operatorname{rank}(P_{\mathcal S}\Delta).
\end{aligned}
\tag{5.1}
\]

The diagonal term is one admissible Chow term, so

\[
\max_T\operatorname{rank}F_{\mathcal S}(T)
\ge
\operatorname{rank}(P_{\mathcal S}\Delta).
\]

Combining with (2.1) and (5.1) proves (0.1).

This argument includes rectangular targets `A tensor B`, individual isotype
pairs, and genuinely nonrectangular unions of pairs.

## 6. Independent source and target filters

Identify the permanent catalecticant source quotient with `E_m` by taking row
and column complements. Under this identification the permanent catalecticant
is a scalar multiple of the identity.

Let `S` and `T` be arbitrary isotype-pair unions used as fixed source and
target filters. Put

\[
\mathcal U=\mathcal S\cap\mathcal T.
\]

The permanent rank is

\[
\dim W_{\mathcal U}.
\]

For the diagonal term the filtered map is, up to a scalar,

\[
P_{\mathcal T}\Delta\Delta^*P_{\mathcal S}.
\]

Compressing this map to `W_U` gives

\[
P_{\mathcal U}\Delta\Delta^*P_{\mathcal U}.
\]

A compression cannot have rank larger than the full map, while

\[
\operatorname{rank}
(P_{\mathcal U}\Delta\Delta^*P_{\mathcal U})
=
\operatorname{rank}(P_{\mathcal U}\Delta).
\]

Applying (5.1) to `U` proves that arbitrary fixed row--column isotype filters
on both source and target still have ratio at most `M`.

## 7. Finite block-diagonal families

For finitely many source--target filtered maps, use the same diagonal Chow term
in every block. Each block numerator is at most `M` times its compressed
diagonal-term rank. Summing the inequalities proves the same ceiling for the
block-diagonal direct sum.

Maximizing over `m` gives

\[
\boxed{
\binom n{\lfloor n/2\rfloor}.
}
\]

Thus the complete fixed row--column isotype-projection route for ordinary
catalecticants remains at central-binomial scale.

## 8. Ambient `GL(V)` projections of the standard Koszul differential

There is also no hidden refinement obtained by projecting only the standard
exterior differential through ambient `GL(V)` isotypes. Pieri's rule gives

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
S_{(m-1,1^{p+1})}V.
\]

The only common irreducible is the multiplicity-one hook

\[
S_{(m,1^p)}V.
\]

The exterior differential is nonzero and `GL(V)`-equivariant. By Schur's
lemma it vanishes on the unmatched component and is an isomorphism, up to
scalar, on the common hook. A `GL(V)`-isotype projection inserted immediately
before or after this standard differential therefore either kills the map or
leaves a scalar multiple. It is not a new flattening.

This does not close row--column projections of the full higher Koszul map,
projections on other f-dependent source modules, or arbitrary Pieri maps.

## 9. Exact replay

The primary implementation constructs the primitive Johnson idempotents as
polynomials in the Johnson graph adjacency matrix modulo `1,000,003`. It
reconstructs every Schur-product support, checks all isotype rectangles, and
then exhausts every possible output support mask for `2<=n<=9`.

The independent implementation uses the second prime `1,000,033`; it obtains
primitive idempotents from nested subset-incidence spaces and exact Gram
inversion, then independently exhausts every support mask through `n<=8`.

The modular computations are exact finite diagnostics. The general
characteristic-zero theorem is (4.1)--(5.1), together with scalar extension;
it is not inferred from the finite tables.
