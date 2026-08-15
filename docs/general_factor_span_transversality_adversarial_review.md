# Adversarial review of factor-span transversality

## Verdict

```text
PURE_TRANVERSALITY_ARGUMENT=PASS_AS_INTERNAL_PROOF_DRAFT
COUPLED_CATALYTIC_BOUNDARY=PASS
FINITE_ARITHMETIC_REPLAY=PASS
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed claims are

\[
E_d\cap\operatorname{Sym}^dL=0
\quad\text{when}\quad\dim L<d^2,
\]

and the resulting ordinary lower bounds

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge43,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge78.
\]

## 1. Torus-fixed incidence

The incidence

\[
\{(L,[f]):f\in E_d\cap\operatorname{Sym}^dL\}
\]

is closed and projective. The row-column torus preserves it. A fixed line in
`E_d` is one subpermanent because the row-column weights are multiplicity
free. A fixed `L` is coordinate. Thus the degeneration does not assume a
generic initial support or replace a noncoordinate intersection by an
unrelated coordinate experiment.

## 2. Why a subpermanent needs all `d^2` cells

Every cell of a `d x d` rectangle occurs in a perfect matching. Therefore the
union of the monomial supports of its permanent is the full rectangle. A
coordinate symmetric power containing that subpermanent must contain all
`d^2` coordinate variables. This remains true for `d=2`; no cancellation
between different subpermanents is possible at a fixed point because their
torus weights are distinct.

## 3. Degenerate Chow terms

For a Chow term `T=l_1...l_n`, all degree-`d` derivatives lie in
`Sym^d span(l_1,...,l_n)`. The factor span has dimension at most `n`, with no
independence assumption. For a block of `s` terms the combined factor span has
dimension at most `sn`. Hence the theorem controls repeated factors,
linearly dependent factors, and zero derivative spaces without a generic-term
reduction.

## 4. Projection lemma and coupled images

The omitted-block projection is applied to the literal ambient sum

\[
U=\sum_i\mathcal D_d(T_i).
\]

The actual coupled image satisfies only

\[
\mathcal D_d(\sum_iT_i)\subseteq U.
\]

The proof never replaces this inclusion by equality. A linear section of the
summation map is used only to inject `E_d intersect U` into the direct sum of
the nonomitted components. The kernel would lie in the permanent intersection
with the omitted block, which the transversality theorem makes zero.

## 5. Exact-shadow arithmetic

For `n=7`, fourteen fixed terms and one omitted term leave the same derivative
capacity `13*C(7,3)=455` used by the prior exact-shadow certificate. The exact
transition `452<456` retains intersection cap 238; the residual count remains
29, so the total rises from 42 to 43.

For `n=8`, fifteen fixed terms and one omitted term retain capacity
`14*C(8,3)=784`. The transition `784<793` retains cap 560; the residual count
remains 63, so the total rises from 77 to 78.

For the reviewed `n=7,...,16` Bukh certificates, the same logic reuses the
identical intersection cap and residual count. The global first-Koszul lower
bound exceeds the enlarged fixed count in every row.

## 6. Strongest objections

### Objection A -- the orbit closure may lose the nonzero intersection

The incidence includes the projective line `[f]`; it cannot specialize to the
zero vector. Its limit remains a nonzero point of `P(E_d)` contained in the
limit symmetric power.

### Objection B -- a linear combination of subpermanents might use fewer cells

At the torus-fixed endpoint the line is a single weight line, not an arbitrary
linear combination. This is exactly where multiplicity freeness is used.

### Objection C -- the saved block could reappear through catalectic coupling

The bound is taken in the larger literal sum. Coupling can only shrink the
actual image and therefore cannot invalidate the upper bound.

### Objection D -- the result solves the conjecture asymptotically

It does not. The universally safe omitted count is about `n/4` in the central
range. This is an additive improvement to the fixed-term side of the existing
multishadow argument, not an exponential improvement.

## 7. Claim boundary

The appropriate status is

```text
PROOF_DRAFT_COMPLETE
EXACT_INTEGER_ARITHMETIC_REPLAYED
GENERAL_N_PROGRESS
```

not an exact-rank theorem for `perm_7`, `perm_8`, or general `perm_n`, and not
a border-rank result.
