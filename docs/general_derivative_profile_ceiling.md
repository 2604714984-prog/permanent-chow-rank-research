# A ceiling theorem for scalar derivative profiles

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_BARRIER`.

For every `n>=2`, let

\[
h_m(f)=\dim \mathcal D_m(f)
      =\operatorname{rank} C_{n-m,m}(f),
\qquad
0\le m\le n,
\]

and write

\[
h(f)=(h_0(f),\ldots,h_n(f)).
\]

This note proves that any natural Chow-rank lower bound which factors only
through this scalar dimension vector is bounded, on the permanent, by the
central binomial coefficient.

The result is a barrier theorem. It does not improve a numerical Chow-rank
lower bound. It identifies information that a general-`n` proof must retain.

## 1. The two derivative profiles

Let

\[
c_n(m)=\binom nm,
\qquad
p_n(m)=\binom nm^2.
\]

### Proposition 1.1 — one Chow term

If

\[
T=\ell_1\cdots\ell_n
\]

has linearly independent factors, then

\[
h_m(T)=c_n(m).
\]

For an arbitrary, possibly degenerate, Chow term,

\[
h_m(T)\le c_n(m).
\]

### Proof

After a linear change of variables, an independent-factor term is
`x_1...x_n`. Its degree-`m` derivative space has the squarefree products of
`m` distinct factors as a basis, hence dimension `binom(n,m)`.

An arbitrary factor tuple is a specialization of independent tuples. Every
`h_m` is the rank of a matrix whose entries depend polynomially on the factor
coefficients. Matrix rank cannot increase under specialization. ∎

### Proposition 1.2 — the permanent

For the `n x n` permanent,

\[
h_m(\operatorname{perm}_n)=p_n(m)=\binom nm^2.
\]

### Proof

An order-`n-m` derivative leaves an `m x m` subpermanent. Such a derivative is
indexed by an `m`-element row set and an `m`-element column set. Different
pairs have disjoint row-column support, so the resulting subpermanents are
linearly independent. ∎

## 2. Profile methods

A **scalar derivative-profile method** in degree `n` is a function

\[
\Phi_n:\mathbb R_{\ge0}^{n+1}\longrightarrow\mathbb R_{\ge0}
\]

with the following properties.

1. **Coordinate monotonicity.** If `x<=y` coordinatewise, then
   `Phi_n(x)<=Phi_n(y)`.
2. **Subadditivity.**
   \[
   \Phi_n(x+y)\le\Phi_n(x)+\Phi_n(y).
   \]
3. **Positive homogeneity.**
   \[
   \Phi_n(\lambda x)=\lambda\Phi_n(x)
   \quad(\lambda\ge0).
   \]
4. **One-term normalization.**
   \[
   \Phi_n(c_n)\le1.
   \]

The definition includes every nonnegative weighted ratio of scalar
catalecticant ranks and every block-diagonal direct sum formed by repeating
scalar catalecticants.

### Lemma 2.1 — profile methods give rank lower bounds

For every degree-`n` form `f`,

\[
\operatorname{ChowRank}(f)\ge\Phi_n(h(f)).
\]

### Proof

Suppose

\[
f=T_1+\cdots+T_r.
\]

For every `m`, linearity of the catalectic map gives

\[
\mathcal D_m(f)
\subseteq
\mathcal D_m(T_1)+\cdots+\mathcal D_m(T_r).
\]

Therefore

\[
h(f)\le h(T_1)+\cdots+h(T_r)
\]

coordinatewise. By monotonicity, subadditivity, Proposition 1.1, and the
normalization,

\[
\Phi_n(h(f))
\le
\sum_{i=1}^r\Phi_n(h(T_i))
\le
r.
\]

Taking the minimum over decompositions proves the claim. ∎

## 3. The profile ceiling

Put

\[
M_n=\binom n{\lfloor n/2\rfloor}.
\]

### Theorem 3.1 — general scalar-profile ceiling

For every scalar derivative-profile method,

\[
\boxed{
\Phi_n(h(\operatorname{perm}_n))\le M_n.
}
\]

### Proof

For every `m`,

\[
p_n(m)
=
\binom nm^2
\le
M_n\binom nm
=
M_n c_n(m).
\]

Thus

\[
p_n\le M_n c_n
\]

coordinatewise. Monotonicity, positive homogeneity, and normalization give

\[
\Phi_n(p_n)
\le
\Phi_n(M_n c_n)
=
M_n\Phi_n(c_n)
\le
M_n.
\]

∎

### Consequence

No method satisfying the four axioms and retaining only the numbers

\[
\dim\mathcal D_0(f),\ldots,\dim\mathcal D_n(f)
\]

can prove the conjectural permanent lower bound `2^(n-1)` for any `n>=3`,
because

\[
M_n<2^{n-1}.
\]

The theorem also explains why using every derivative degree without retaining
maps between the degrees does not solve the problem.

## 4. Weighted direct sums of scalar catalecticants

Let `w_0,...,w_n` be nonnegative real numbers, not all zero. The normalized
rank ratio is

\[
R_w(n)
=
\frac{\sum_m w_m p_n(m)}
     {\sum_m w_m c_n(m)}
=
\frac{\sum_m w_m\binom nm^2}
     {\sum_m w_m\binom nm}.
\]

### Corollary 4.1

\[
\boxed{
R_w(n)\le M_n.
}
\]

Equality holds exactly when every positive weight is supported on a central
degree:

\[
\binom nm=M_n.
\]

### Proof

The ratio is a weighted average of the numbers `binom(n,m)`, with
nonnegative weights `w_m binom(n,m)`. ∎

This includes a block-diagonal matrix formed from any number of repeated
scalar catalecticants. Adding more blocks cannot beat the best single central
degree.

### Equal weight on every degree

Vandermonde's identity gives

\[
\sum_{m=0}^n\binom nm^2=\binom{2n}{n},
\qquad
\sum_{m=0}^n\binom nm=2^n.
\]

Hence the equal-weight all-degree direct sum has ratio

\[
\frac{\binom{2n}{n}}{2^n},
\]

which is strictly smaller than `M_n` for `n>=2`.

For `n=6`, for example,

\[
M_6=20,
\qquad
\frac{\binom{12}{6}}{2^6}
=\frac{231}{16},
\]

so the all-degree scalar direct sum certifies only the integer lower bound 15.

## 5. The asymptotic missing factor

Stirling's formula gives

\[
M_n
=
2^n\sqrt{\frac{2}{\pi n}}\,(1+o(1)).
\]

The Glynn upper bound is `2^(n-1)`. Therefore

\[
\frac{2^{n-1}}{M_n}
=
\sqrt{\frac{\pi n}{8}}\,(1+o(1)).
\]

The currently missing scale is only polynomial, not exponential, but scalar
derivative dimensions cannot recover it.

## 6. Relation to the existing results

The theorem does **not** subsume the stronger in-repository methods.

- The first Koszul differential uses the map
  \[
  \mathcal D_m(f)\otimes V
  \longrightarrow
  \mathcal D_{m-1}(f)\otimes\Lambda^2V,
  \]
  not merely the dimensions of its source layers.
- Shadow arguments use incidence between adjacent derivative degrees.
- Quotient gain and the fixed-six lower-25 proof use the geometry and
  prolongation of coupled relation modules.
- Multigraded or representation-valued syzygies retain information absent
  from `h(f)`.

Indeed, at `n=6` the scalar profile ceiling is 20, whereas the repository
already proves the ordinary Chow-rank lower bound 25. The extra five units come
from structure that the profile discards.

## 7. The correct next object

Define the complete derivative tower

\[
\mathcal M(f)
=
\bigoplus_{m=0}^n\mathcal D_m(f)
\]

together with all differentiation maps

\[
\partial_{ij}:
\mathcal D_m(f)\longrightarrow\mathcal D_{m-1}(f).
\]

For a hypothetical decomposition

\[
f=T_1+\cdots+T_r,
\]

the relevant object is not a list of dimensions. It is the coupled module map

\[
\mathcal M(f)
\longrightarrow
\sum_i\mathcal M(T_i)
\]

and the full relation module

\[
0\longrightarrow\mathcal R
\longrightarrow
\bigoplus_i\mathcal M(T_i)
\longrightarrow
\mathcal U
\longrightarrow0.
\]

A general-`n` lower bound must charge compatibility across degrees or relations
among summands. Merely adding scalar degree bounds is now ruled out.

### 7.1 The raw adjacent relation dimension is still profile data

For every form `f` and every `m>=1`, total differentiation gives a surjection

\[
\mu_m(f):
V^*\otimes\mathcal D_m(f)
\longrightarrow
\mathcal D_{m-1}(f).
\]

Surjectivity follows because every derivative of order `n-m+1` is one
additional first derivative of a derivative of order `n-m`. Hence

\[
\dim\ker\mu_m(f)
=
(\dim V)h_m(f)-h_{m-1}(f).
\]

The scalar dimension of this first adjacent relation space therefore contains
no information beyond the derivative profile. Merely tabulating these kernel
dimensions does not evade Theorem 3.1.

The first potentially new object is a higher compatibility quotient, such as
Koszul homology, a Young flattening, or a coupled relation module. Even there,
a scalar total dimension may be too weak.

## 8. Next research gate

The first gate is **coordinate invariance**. The row-column torus stabilizes the
permanent but does not stabilize an arbitrary Chow summand. A functional of
permanent-side torus weights is not automatically bounded termwise after an
arbitrary change of coordinates.

A candidate is authorized only if it is either:

1. the rank of a natural `GL(V)`-equivariant construction with a proved
   uniform cap for every Chow term; or
2. a target-torus functional with a proved orientation-independent cap over
   the full `GL(V)` orbit of one Chow term.

The first experiment should compare a small list of `GL(V)`-natural Koszul or
Young complexes at `n=5,6`. For each candidate:

- derive the generic and degenerate one-term cap;
- replay the permanent rank exactly;
- test the common-factor adversarial family; and
- stop unless it exceeds 25 at `n=6` or suggests a uniform doubling
  recurrence.

Torus-weight decompositions may be used to discover or verify a natural map,
but they are not by themselves a decomposition lower bound.

No manager, registry, generic SAT layer, or large state tree is justified
before such a map and its one-term cap are stated.

## 9. Hidden assumptions and strongest objection

### Hidden assumptions

- Natural profile bounds should be monotone and positively homogeneous.
- A useful general invariant can be made subadditive on coupled sums.
- The missing factor is encoded in cross-degree compatibility rather than in a
  shorter decomposition.

### Assume all assumptions are false

Then an exotic nonmonotone profile invariant might evade Theorem 3.1, or the
conjectural value `2^(n-1)` may be false. In that case the appropriate response
is an exact decomposition search at `n=6`, not a larger scalar-profile
calculation.

### Strongest objection

The four axioms do not logically classify every imaginable function of the
profile. A specially designed integer-valued, nonmonotone rule might not be
covered. The theorem is therefore a barrier for the natural decomposition
methods that remain valid through coordinatewise image inclusion. It is not a
metatheorem about every possible argument that mentions derivative
dimensions.

## 10. Deterministic replay

Run

```bash
python scripts/general_derivative_profile_ceiling_audit.py \
  --max-n 50 \
  --json /tmp/general_derivative_profile_ceiling.json
python -m unittest tests.test_general_derivative_profile_ceiling -v
```

Expected marker:

```text
GENERAL_DERIVATIVE_PROFILE_CEILING_AUDIT_PASS
```

The audit uses only Python's standard library and exact integer/rational
arithmetic. It verifies all degrees through `n=50` and exhausts all nonzero
Boolean weight supports through `n=12`. The frozen compact payload is

```text
data/general_derivative_profile_ceiling.json
```

## Claim boundary

This theorem does not prove a new Chow-rank lower bound. It does not constrain
invariants using cross-degree maps, quotient geometry, multigrading,
representation theory, syzygies, or coupled relation modules. Its role is to
close the scalar derivative-profile route and force the general-`n` program
toward structure rather than larger dimension tables.
