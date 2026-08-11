# Relation tableaux and the exact central pairing correction

## Status and boundary

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`.

This note gives two general linear-algebra theorems for coupled sums of
homogeneous forms and one exact obstruction to using them as a dimension-only
route to `ChowRank(perm_6) >= 26`.

No unrestricted Chow-rank improvement is claimed.

## 1. Relation tableaux

Let `T_1,...,T_q` be degree-`n` forms on `V`.  For `0 <= m <= n`, put

\[
F_{i,m}=\mathcal D_m(T_i)\subseteq\operatorname{Sym}^mV
\]

and define the literal-sum relation space

\[
\mathcal K_m=ker\left(
\bigoplus_{i=1}^qF_{i,m}\longrightarrow\sum_{i=1}^qF_{i,m}
\right),
\qquad \kappa_m=\dim\mathcal K_m.
\tag{1.1}
\]

These are relations among the individual derivative spaces.  They are not the
coupled derivative image of `R=sum_i T_i`.

### Theorem 1.1 — arbitrary-degree vector-valued Macaulay bound

For finite-dimensional spaces `W,V`, a subspace

\[
K\subseteq W\otimes\operatorname{Sym}^dV
\]

of dimension `k`, and

\[
K^{(1)}={F\in W\otimes\operatorname{Sym}^{d+1}V:
\partial_\xi F\in K\text{ for all }\xi\in V^*\},
\]

one has, in characteristic zero,

\[
\boxed{\dim K^{(1)}\le k^{\langle d\rangle}.}
\tag{1.2}
\]

Here `k^{<d>}` is the degree-`d` Macaulay successor.

#### Proof

On `Gr(k,W tensor Sym^d V)`, polarization followed by the tautological quotient
gives a vector-bundle map whose fibre kernel is `K^(1)`.  Its dimension is upper
semicontinuous.

Choose a basis `x_0,...,x_(N-1)` of `V`, put `B=d+1`, and assign weight `B^j`
to `x_j`.  Every degree-`d` monomial has a unique weight because its base-`B`
digits lie between zero and `d`.  A color stride larger than the full monomial
weight range separates the basis vectors of `W`.  The resulting one-parameter
subgroup degenerates `K` to a colored monomial space

\[
K_0=\bigoplus_a e_a\otimes P_a.
\]

Differentiation preserves color, so

\[
K_0^{(1)}=\bigoplus_a e_a\otimes P_a^{(1)}.
\]

Scalar Macaulay growth gives

\[
\dim P_a^{(1)}\le(\dim P_a)^{\langle d\rangle}.
\]

The degree-`d` successor is superadditive: put sharp scalar spaces of dimensions
`a` and `b` in disjoint variable sets and apply scalar Macaulay to their direct
sum.  Thus

\[
\sum_a(\dim P_a)^{\langle d\rangle}
\le\left(\sum_a\dim P_a\right)^{\langle d\rangle}.
\]

Upper semicontinuity completes the proof.  The argument over an algebraic
closure descends to every characteristic-zero base field.

### Corollary 1.2 — tableau growth

Differentiating a relation in `K_(m+1)` gives a relation in `K_m`.  Therefore

\[
\mathcal K_{m+1}\subseteq\mathcal K_m^{(1)}
\]

and

\[
\boxed{\kappa_{m+1}\le
\kappa_m^{\langle m\rangle}.}
\tag{1.3}
\]

## 2. A noncentral block-Sylvester bound

Let

\[
c_i=\operatorname{rank}C_{n-m,m}(T_i),
\qquad C=\sum_i c_i,
\qquad R=\sum_iT_i.
\]

### Theorem 2.1

\[
\boxed{
\operatorname{rank}C_{n-m,m}(R)
\ge C-\kappa_m-\kappa_{n-m}.}
\tag{2.1}
\]

#### Proof

Let `D=diag(A_1,...,A_q)` be the block diagonal of the individual catalectic
matrices, let `Sigma` sum the output copies, and let `Delta` diagonally embed the
common source.  Then

\[
C_{n-m,m}(R)=\Sigma D\Delta.
\]

The rank of `Sigma D` is `C-kappa_m`, because its image is the literal sum of
the degree-`m` derivative spaces.  The rank of `D Delta` is `C-kappa_(n-m)`,
because its row spaces are the complementary derivative spaces.  Applying the
Frobenius--Sylvester inequality through the rank-`C` middle block proves (2.1).

The central even-degree case gives `C-2 kappa_(n/2)`.

## 3. Exact correction in the central symmetric case

Let `A_i:X -> X*` be symmetric linear maps and let `U_i=im A_i`.  Each `A_i`
induces a nondegenerate symmetric form on `U_i`:

\[
\beta_i(A_ix,A_iy)=\langle A_ix,y\rangle.
\tag{3.1}
\]

Put `U=direct_sum_i U_i`, `beta=direct_sum_i beta_i`, and

\[
\mathcal R=\ker(\sigma:U\to X^*),
\qquad \rho=\dim\mathcal R,
\]

where `sigma` sums the components.

### Theorem 3.1 — relation-pairing identity

\[
\boxed{
\operatorname{rank}\left(\sum_iA_i\right)
=C-2\rho+\operatorname{rank}(\beta|_{\mathcal R}).}
\tag{3.2}
\]

#### Proof

Define `B:X -> U` by `Bx=(A_1x,...,A_qx)`.  Equation (3.1) gives

\[
\beta(Bx,u)=\langle x,\sigma u\rangle.
\]

Hence `im B=R^(perp_beta)`.  Since `sum_i A_i=sigma B`,

\[
\begin{aligned}
\operatorname{rank}(\sigma B)
&=\dim\operatorname{im}B
-\dim(\operatorname{im}B\cap\mathcal R)\\
&=(C-\rho)-\dim(\mathcal R\cap\mathcal R^{\perp_\beta}).
\end{aligned}
\]

The final intersection is the radical of `beta|_R`, whose dimension is
`rho-rank(beta|_R)`.  This proves (3.2).

The former block-Sylvester estimate is exactly the result of discarding the
last nonnegative term.

## 4. A strict Chow counterexample to positive dimension-only gain

Work with eight independent variables and set

\[
T_1=x_1x_2x_3x_4x_5x_6,
\qquad
T_2=x_1x_2x_3x_4x_7x_8.
\tag{4.1}
\]

Both are degree-six Chow terms.  Their central derivative spaces intersect in
the four monomials indexed by the three-subsets of `{1,2,3,4}`, so `rho=4`.

For a squarefree degree-six monomial, the induced central form pairs a
three-subset only with its complementary three-subset.  The complement in
either support in (4.1) contains both private variables.  It is never in the
four-dimensional intersection.  Consequently

\[
\boxed{\operatorname{rank}(\beta|_{\mathcal R})=0.}
\tag{4.2}
\]

Equation (3.2) gives

\[
\operatorname{rank}C_{3,3}(T_1+T_2)=40-8=32.
\tag{4.3}
\]

This is not an artificial cancellation.  Factoring the common variables gives

\[
T_1+T_2=x_1x_2x_3x_4(x_5x_6+x_7x_8).
\]

The remaining quadratic has matrix rank four, whereas a product of two linear
forms has matrix rank at most two.  Unique factorization therefore shows that
`T_1+T_2` is not one Chow term.  Its Chow rank is exactly two.

Thus no positive lower bound for the correction in (3.2) can depend only on
`rho`, even for a minimal two-term Chow expression.

## 5. Consequence for `n=6`

The relation tableau and pairing correction are valid GL-covariant coupled
invariants.  They survive repeated factors and the N6-017 common-factor family.
However, the exact example (4.1) kills the dimension-only route: a zero pairing
correction does not imply a removable cancellation.

For the current lower-26 fixed-six frontier, iterating (1.3) gives only

\[
\kappa_4\le
(\kappa_2^{\langle2\rangle})^{\langle3\rangle}.
\]

At the allowed maximum `kappa_2=37`, the right side is 331, already larger than
the entire relevant quadratic ambient capacity.  Hence this unrefined
two-step dimension bound supplies no lower-26 exclusion.

The exact correction may still be useful after a geometric classification of
its radical, but the shared-four-factor example shows that such a classification
would contain genuine positive-dimensional Chow strata.  No broad
classification is authorized from this result alone.

## 6. Replay

Run

```bash
python scripts/general_relation_tableau_audit.py \
  --json /tmp/general_relation_tableau_audit.json
python -m unittest tests.test_general_relation_tableau -v
```

The script checks general Macaulay successor arithmetic, exact sparse central
catalectic ranks for all overlap sizes of two squarefree degree-six monomials,
the relation-pairing correction, repeated terms, and the common-factor boundary.
All matrix lower bounds are certified modulo `1,000,003`; the written formulas
give matching characteristic-zero upper bounds.
