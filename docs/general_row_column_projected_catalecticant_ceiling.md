# Row--column representation projections of permanent catalecticants are centrally capped

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

This note studies a representation-sensitive refinement that remains after the
scalar derivative-profile barrier.  The refinement first projects a
catalecticant to the permanent matching subspace and then to an arbitrary
row--column `S_n x S_n`-stable summand.

The main result is the exact route ceiling

\[
\boxed{
\left\lceil
\frac{\operatorname{rank}\mathcal C_{m,W}(\operatorname{perm}_n)}
{\max_T\operatorname{rank}\mathcal C_{m,W}(T)}
\right\rceil
\le
\binom nm.
}
\tag{0.1}
\]

Here `W` may be an arbitrary sum of row--column isotypes.  An arbitrary finite
block-diagonal direct sum across degrees and stable summands is therefore
capped by

\[
\binom n{\lfloor n/2\rfloor}.
\]

This is a ceiling on a named projected-catalecticant mechanism, not an upper
bound on actual Chow rank.  It does not cover row--column projections inserted
inside higher Koszul or Young complexes, nonlinear joint minors, higher
syzygies, valuative arguments, or Chow-realizability defects.

The note also records a separate boundary: every `GL(V)`-equivariant
pre/post-projection of the standard exterior differential is either zero or a
scalar multiple of that differential.  Thus a nontrivial representation
refinement must break full ambient `GL(V)` symmetry, change the Pieri map, or
retain higher relation data.

## 1. The permanent matching projection

Let

\[
V=\operatorname{span}\{x_{rc}:1\le r,c\le n\}.
\]

For `1<=m<=n`, let

\[
X_m=\binom{[n]}m,
\qquad
M_m=k^{X_m}.
\]

For row and column sets `R,C in X_m`, write

\[
p_{R,C}
=
\sum_{\sigma:R\overset\sim\longrightarrow C}
\prod_{r\in R}x_{r,\sigma(r)}
\]

for the corresponding subpermanent.  Different pairs `(R,C)` have disjoint
monomial supports.  Hence the linear map

\[
Q_m:\operatorname{Sym}^mV\longrightarrow
E_m:=\operatorname{span}\{p_{R,C}\}
\tag{1.1}
\]

is defined canonically by

\[
Q_m(x_\sigma)=\frac1{m!}p_{R,C}
\]

for a matching monomial with row set `R` and column set `C`, and by zero on
all nonmatching monomials.  It satisfies

\[
Q_m|_{E_m}=\operatorname{id}_{E_m}
\]

and is `S_n x S_n`-equivariant.

Under

\[
p_{R,C}\longleftrightarrow e_R\otimes e_C,
\]

one has

\[
E_m\simeq M_m\boxtimes M_m.
\tag{1.2}
\]

## 2. Projected catalecticants

Let

\[
W\subseteq E_m
\]

be any `S_n x S_n`-stable subspace.  Over characteristic zero choose the
orthogonal equivariant projection

\[
P_W:E_m\longrightarrow W
\]

with respect to the basis `p_(R,C)`.

For a degree-`n` form `f`, define

\[
\mathcal C_{m,W}(f)
=
P_W Q_m C_{n-m,m}(f).
\tag{2.1}
\]

The construction is linear in `f`, so rank subadditivity supplies a legitimate
Chow-rank lower-bound ratio.

For the permanent,

\[
\operatorname{im}C_{n-m,m}(\operatorname{perm}_n)=E_m.
\]

Since `Q_m` is the identity on `E_m`,

\[
\boxed{
\operatorname{rank}\mathcal C_{m,W}(\operatorname{perm}_n)
=\dim W.
}
\tag{2.2}
\]

## 3. A transitive diagonal-compression lemma

Let `X` be a finite transitive `G`-set, put `M=k^X`, and identify

\[
M\otimes M=k^{X\times X}.
\]

Define the diagonal embedding

\[
D:M\longrightarrow M\otimes M,
\qquad
D(e_x)=e_x\otimes e_x.
\tag{3.1}
\]

Let `W subset M tensor M` be `G x G`-stable and let `P_W` be the orthogonal
projection.

### Lemma 3.1

\[
\boxed{
\operatorname{rank}(P_WD)
\ge
\frac{\dim W}{|X|}.
}
\tag{3.2}
\]

### Proof

The map `D` is an isometry and `P_W` is a contraction, so

\[
\|P_WD\|_{\mathrm{op}}\le1.
\tag{3.3}
\]

Because `W` is `G x G`-stable, `P_W` commutes with the product action.  That
action is transitive on `X x X`; consequently every diagonal matrix
coefficient of `P_W` in the basis `e_x tensor e_y` is equal.  Its common value
is the normalized trace

\[
\frac{\dim W}{|X|^2}.
\tag{3.4}
\]

Therefore

\[
\begin{aligned}
\|P_WD\|_{\mathrm F}^2
&=
\sum_{x\in X}
\langle P_W(e_x\otimes e_x),e_x\otimes e_x\rangle\\
&=
|X|\frac{\dim W}{|X|^2}
=
\frac{\dim W}{|X|}.
\end{aligned}
\tag{3.5}
\]

If the nonzero singular values are `s_1,...,s_r`, then every `s_i<=1` by
(3.3).  Hence

\[
\frac{\dim W}{|X|}
=
\sum_i s_i^2
\le r.
\]

This is (3.2).  The argument may be made after scalar extension to `C`; ranks
are unchanged, so it applies over every characteristic-zero field. ∎

The proof is valid for an arbitrary stable sum of isotypes.  No
multiplicity-free decomposition or Krein-parameter calculation is required.

## 4. The diagonal Chow term

Take

\[
T_\Delta=\prod_{r=1}^n x_{rr}.
\]

Its degree-`m` derivative space has basis

\[
x_S=\prod_{r\in S}x_{rr},
\qquad S\in X_m.
\]

The matching projection gives

\[
Q_m(x_S)=\frac1{m!}p_{S,S}.
\]

Under (1.2), the restriction of `mathcal C_(m,W)(T_Delta)` is, up to a
nonzero scalar, exactly

\[
P_WD:M_m\longrightarrow W.
\]

Lemma 3.1 therefore gives

\[
\boxed{
\max_T\operatorname{rank}\mathcal C_{m,W}(T)
\ge
\operatorname{rank}\mathcal C_{m,W}(T_\Delta)
\ge
\frac{\dim W}{\binom nm}.
}
\tag{4.1}
\]

Combining (2.2) and (4.1) proves (0.1).

The witness is one fixed coordinate matching term.  No generic-orientation
claim about arbitrary Chow terms is used.

## 5. Arbitrary isotype sums and finite block sums

The permutation module on `m`-subsets decomposes multiplicity-free as

\[
M_m
\simeq
\bigoplus_{i=0}^{\min(m,n-m)}
S^{(n-i,i)}.
\tag{5.1}
\]

Thus every row--column isotype projection, and every arbitrary sum of such
isotypes, is a special case of the theorem.

Now take finitely many pairs `(m_alpha,W_alpha)` and combine the projected
catalecticants block diagonally.  The same diagonal term `T_Delta` is a witness
for every block.  Put

\[
M_\alpha=\binom n{m_\alpha}.
\]

Then

\[
\frac{
\sum_\alpha\dim W_\alpha
}{
\sum_\alpha \dim W_\alpha/M_\alpha
}
\le
\max_\alpha M_\alpha
\le
\binom n{\lfloor n/2\rfloor}.
\tag{5.2}
\]

Hence no finite collection of row--column representation-projected
catalecticants escapes the scalar central-binomial scale.

## 6. Full `GL(V)` projections of the standard exterior differential

The standard exterior differential is

\[
\delta_{m,p}:
\operatorname{Sym}^mV\otimes\Lambda^pV
\longrightarrow
\operatorname{Sym}^{m-1}V\otimes\Lambda^{p+1}V.
\]

Pieri's rule gives, with the nonexistent boundary summands omitted,

\[
\operatorname{Sym}^mV\otimes\Lambda^pV
\simeq
\mathbb S_{(m+1,1^{p-1})}V
\oplus
\mathbb S_{(m,1^p)}V,
\tag{6.1}
\]

\[
\operatorname{Sym}^{m-1}V\otimes\Lambda^{p+1}V
\simeq
\mathbb S_{(m,1^p)}V
\oplus
\mathbb S_{(m-1,1^{p+1})}V.
\tag{6.2}
\]

The only common irreducible is

\[
\mathbb S_{(m,1^p)}V,
\]

and it occurs with multiplicity one.  The map `delta_(m,p)` is nonzero, so by
Schur's lemma it is zero on the noncommon source summand and a scalar
isomorphism on the common hook.

### Proposition 6.1

For arbitrary `GL(V)`-equivariant endomorphisms `P` and `Q` of the two spaces,

\[
\boxed{
Q\,\delta_{m,p}\,P=c\,\delta_{m,p}
}
\tag{6.3}
\]

for some scalar `c`.  In particular, equivariant idempotent pre/post
projections either retain the standard differential up to scalar or kill it.

This closes only projections at the standard exterior-differential stage.  It
does not close source projections before the catalecticant, arbitrary Pieri
maps, row--column projections inside a Koszul complex, or higher syzygy
modules.

## 7. Exact finite replay

The primary implementation constructs the primitive idempotents of the
Johnson scheme modulo a large prime.  For every

```text
3<=n<=8,
1<=m<=floor(n/2),
```

it verifies:

- the two-row Specht dimensions in (5.1);
- orthogonal idempotent decomposition of the subset module;
- the actual diagonal-compression rank on every irreducible pair;
- the inequality `binom(n,m)*rank >= dim(W)`;
- several deterministic nonrectangular sums of row--column isotypes; and
- the route ceiling `<=binom(n,m)`.

A second implementation builds Johnson eigenspaces as nullspaces rather than
projector polynomials.  It constructs a nowhere-zero vector in each nonzero
stable constituent and verifies directly that pointwise multiplication by
that vector is injective on every other constituent.

The finite calculations replay the representation interface.  The general
ceiling is the Frobenius/operator-norm proof of Lemma 3.1, not a finite
extrapolation.

## 8. Research decision

The following routes are now closed at central-binomial scale:

```text
scalar derivative dimensions
complete scalar derivative tower
unprojected standard Koszul--Young maps
GL(V)-equivariant projections of the standard exterior differential
row--column isotype-projected catalecticants
arbitrary stable sums of row--column catalecticant isotypes
finite block sums of those projected catalecticants
```

The remaining representation-sensitive frontier must retain information not
present in a projected catalecticant alone.  The first legitimate candidates
are:

1. row--column projections **inside** higher Koszul/Young complexes;
2. arbitrary Pieri maps whose one-term rank is uniformly controlled;
3. representation-valued relation or syzygy modules;
4. joint determinantal data with a proved subquotient envelope; or
5. Chow-realizability defects.
