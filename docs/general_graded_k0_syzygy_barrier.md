# Exact-additive syzygy data collapse to the graded Hilbert profile

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_ROUTE_CEILING`,
`EXACT_FINITE_INTERFACES_REPLAYED`.

Let

\[
R=k[s,t]
\]

with its standard grading, over a characteristic-zero field. This note
classifies every scalar invariant of finite-length graded `R`-modules which is
additive on short exact sequences. Such an invariant is necessarily a weighted
graded Hilbert function. Consequently, when it is inserted into the apolar
subquotient argument for the permanent, its Chow-rank ratio is capped by the
central binomial coefficient.

The result closes exact-additive Grothendieck-group and Euler-characteristic
repairs of raw Betti or syzygy data. It does **not** close non-exact partial
Euler characteristics, raw Betti tables, persistence rank invariants,
minimal-syzygy functors with a separately proved monotone envelope,
representation-valued data, nonlinear determinantal loci, valuative arguments,
or Chow-realizability defects.

No numerical Chow-rank boundary changes in this note.

## 1. The category

Let `C` be the abelian category of finite-length, finitely generated,
`Z`-graded `R`-modules and degree-zero homomorphisms. Its graded simple objects
are exactly

\[
k(-d)=R/(s,t)(-d),
\qquad d\in\mathbf Z.
\tag{1.1}
\]

Every object of `C` has a finite graded composition series. One way to see
this is to choose a nonzero homogeneous element of the socle, split off the
corresponding simple submodule, and continue by induction on total vector-space
length.

## 2. The graded Grothendieck group

### Theorem 2.1

There is a canonical isomorphism

\[
\boxed{
K_0(\mathcal C)
\simeq
\bigoplus_{d\in\mathbf Z}\mathbf Z\,[k(-d)].
}
\tag{2.1}
\]

For every `M` in `C`,

\[
\boxed{
[M]
=
\sum_d \dim_k(M_d)\,[k(-d)].
}
\tag{2.2}
\]

### Proof

The simple classes generate `K_0(C)` by a graded composition series. The
coefficient of `[k(-d)]` in any composition series equals the coefficient of
`t^d` in the Hilbert series, because Hilbert functions are additive on short
exact sequences and `k(-d)` has Hilbert function equal to one in degree `d`
and zero elsewhere. Hence the multiplicity is `dim_k M_d`, independent of the
chosen series.

The homomorphism sending `[k(-d)]` to the Laurent monomial `t^d` identifies
`K_0(C)` with the group of finite Laurent polynomials. The classes of distinct
shifts are therefore independent, proving (2.1) and (2.2). ∎

## 3. Classification of exact-additive scalar invariants

Let

\[
\Phi:\operatorname{Ob}(\mathcal C)\longrightarrow\mathbf R
\]

satisfy

\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0
\quad\Longrightarrow\quad
\Phi(M)=\Phi(M')+\Phi(M'').
\tag{3.1}
\]

### Corollary 3.1

There are unique real coefficients

\[
c_d=\Phi(k(-d))
\]

such that

\[
\boxed{
\Phi(M)
=
\sum_d c_d\dim_k M_d.
}
\tag{3.2}
\]

If `Phi` is nonnegative on every module, or merely nondecreasing under
submodules and quotients, then

\[
\boxed{c_d\ge0\quad\text{for all }d.}
\tag{3.3}
\]

### Proof

Equation (3.2) is the universal property of `K_0(C)` applied to Theorem 2.1.
For (3.3), evaluate `Phi` on the simple module `k(-d)`. ∎

Thus no exact-additive scalar can retain relation data beyond the graded
Hilbert function.

## 4. Free resolutions and Euler characteristics

A finite-length graded `R`-module has projective dimension at most two. Write a
minimal graded resolution

\[
0\longrightarrow
\bigoplus_j R(-j)^{\beta_{2,j}}
\longrightarrow
\bigoplus_j R(-j)^{\beta_{1,j}}
\longrightarrow
\bigoplus_j R(-j)^{\beta_{0,j}}
\longrightarrow M\longrightarrow0.
\tag{4.1}
\]

Its Hilbert-series identity is

\[
\boxed{
(1-z)^2 H_M(z)
=
\sum_{i=0}^{2}(-1)^i
\sum_j\beta_{i,j}(M)z^j.
}
\tag{4.2}
\]

Therefore every scalar extracted from a resolution through an exact-additive
Euler characteristic factors through `H_M`. In particular, alternating
weighted sums of Betti numbers which are genuinely exact-additive do not evade
Theorem 2.1.

This statement does not make raw `beta_(i,j)`, truncated alternating sums, or
partial Euler characteristics exact-additive. The counterexamples in the
parent Fitting/Betti audit remain in force.

## 5. Application to permanent apolar algebras

Let

\[
A_f=S/f^\perp
\]

be the apolar algebra of a degree-`n` form. The established apolar subquotient
theorem states that a Chow decomposition

\[
\operatorname{perm}_n=T_1+\cdots+T_r
\]

produces an intermediate graded module which embeds into

\[
\bigoplus_{i=1}^{r}A_{T_i}
\]

and surjects onto `A_(perm_n)`. Hence a nonnegative exact-additive scalar is a
legal subquotient-monotone rank-ratio invariant.

Put

\[
H_d=\binom nd.
\]

The permanent apolar Hilbert function is

\[
\dim(A_{\operatorname{perm}_n})_d=H_d^2.
\tag{5.1}
\]

For every Chow term, including dependent-factor terms, the Boolean term
envelope gives

\[
\dim(A_T)_d\le H_d.
\tag{5.2}
\]

An independent-factor Chow term attains equality in every degree
simultaneously. Therefore, for nonnegative coefficients `c_d`, the exact
one-term envelope is

\[
\max_T\Phi(A_T)=\sum_dc_dH_d.
\tag{5.3}
\]

The permanent numerator is

\[
\Phi(A_{\operatorname{perm}_n})
=
\sum_dc_dH_d^2.
\tag{5.4}
\]

Whenever the denominator is nonzero,

\[
\begin{aligned}
\frac{\Phi(A_{\operatorname{perm}_n})}
{\max_T\Phi(A_T)}
&=
\frac{\sum_dc_dH_d^2}{\sum_dc_dH_d}\\
&\le
\max_dH_d.
\end{aligned}
\]

Thus:

### Theorem 5.1 -- exact-additive syzygy ceiling

\[
\boxed{
\left\lceil
\frac{\Phi(A_{\operatorname{perm}_n})}
{\max_T\Phi(A_T)}
\right\rceil
\le
\binom n{\lfloor n/2\rfloor}.
}
\tag{5.5}
\]

The theorem applies to every nonnegative scalar which factors through the
graded Grothendieck class, including every short-exact-additive scalar Euler
characteristic of a free resolution.

## 6. Derived-category formulation

The same statement may be expressed in the bounded derived category of
finite-length graded modules. Its Grothendieck group is the same group as in
Theorem 2.1. Therefore any scalar invariant of a bounded complex which:

1. is invariant under quasi-isomorphism;
2. is additive on distinguished triangles; and
3. is nonnegative on modules used in the rank-ratio argument,

reduces to a nonnegative weighted Hilbert profile on degree-zero cohomology.

Hence replacing raw Betti data by a full Euler characteristic repairs
functoriality only by discarding the relation information that could have made
Betti data useful.

## 7. Exact finite replay

The primary audit enumerates every nonempty Ferrers staircase inside a
`6 x 6` box. For each quotient `R/I` it computes:

- the exact graded Hilbert function;
- the minimal monomial generators of `I`;
- the adjacent Hilbert--Burch syzygy degrees; and
- the identity (4.2).

Every removable staircase corner gives a short exact sequence with quotient a
single shifted copy of `k`; these sequences reconstruct the graded composition
multiplicities.

The finite interfaces are:

```text
monomial staircase modules                 923
Hilbert/Betti numerator checks             923
corner short-exact checks                2,772
composition-factor degree cells         16,632
weighted permanent/Boolean ratios        2,183
exhaustive Boolean weight supports       4,079
```

A second implementation uses independently generated lower ideals and direct
cell-removal filtrations. The computations replay the algebraic interface; the
general theorem is the composition-series proof, not finite extrapolation.

## 8. Research decision

The following continuations are now closed at central-binomial scale:

```text
Grothendieck-class scalarizations
full Euler characteristics of Betti tables
exact-additive alternating syzygy counts
exact-functor scalar dimensions
resolution data used only through K_0
```

The remaining relation-sensitive interfaces must be genuinely non-exact while
still satisfying the apolar gate. Candidates include:

1. image ranks or persistence ranks of natural maps not already covered by the
   fixed-matrix ceilings;
2. a representation-valued minimal-syzygy envelope with separately proved
   submodule and quotient monotonicity;
3. nonlinear joint determinantal data;
4. valuative ordinary-rank obstructions; or
5. a uniform Chow-realizability defect.
