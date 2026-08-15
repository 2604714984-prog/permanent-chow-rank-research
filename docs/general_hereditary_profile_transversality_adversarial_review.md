# Adversarial review of hereditary profile transversality

## Verdict

```text
HEREDITARY_PROFILE_THEOREM=PASS_AS_INTERNAL_PROOF_DRAFT
BLOCK_TRANSVERSALITY=PASS
COUPLED_IMAGE_BOUNDARY=PASS
CERTIFICATE_ARITHMETIC=PASS
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

## 1. Specialization direction

The row-column torus sends a nonzero `f in D_d(perm_n)` to a single nonzero
subpermanent after selecting a generic one-parameter subgroup and rescaling by
the minimum occurring weight. Catalectic rank is constant on the nonzero orbit
and cannot increase at the limit. Therefore the original derivative rank is
at least the subpermanent rank, not at most it.

## 2. Multiplicity-free endpoint

The row-column weight of `p_(R,C)` records exactly the row set `R` and column
set `C`; distinct pairs have distinct weights. The endpoint is therefore one
basis line rather than an uncontrolled linear combination.

## 3. Derivatives of the endpoint

The degree-`j` derivatives of a `d x d` permanent are the `j x j`
subpermanents. Distinct row-column pairs have disjoint weight labels, so their
number and dimension are exactly `binom(d,j)^2`.

## 4. Further differentiation of a Chow-derived element

An element `f_i in D_d(T_i)` is a linear combination of derivatives of the
original term. Every further derivative of output degree `j` remains in
`D_j(T_i)`. Thus

```text
D_j(sum_i f_i) subset sum_i D_j(T_i)
```

is valid. No equality or independent-factor assumption is used.

## 5. Coupled/literal firewall

For the coupled fixed sum `R=sum_i T_i`, the proof uses only

```text
D_d(R) subset sum_i D_d(T_i).
```

The omitted-block section is constructed in the larger literal direct sum.
A kernel vector would sum to a permanent derivative inside the omitted block,
which the profile inequality excludes. Coupling can only shrink the actual
image and cannot invalidate the upper bound.

## 6. Numerical promotions

For `n=7,8`, the profile-safe block still has size one, so the exact product
shadow caps and residual counts from the parent branch are unchanged. The only
new arithmetic operation is adding one more fixed term, yielding 43 and 78.

For `n=15`, the degree-two profile gives

```text
4*C(15,2)=420 < C(7,2)^2=441,
```

so four terms are safely omitted. The old certificate's residual count 4,491
and intersection cap remain unchanged, giving `2,392+4,491=6,883`.

## 7. Strongest objection

The theorem controls only derivative dimensions of a single intersection
polynomial. Once a block meets every profile capacity, it supplies no
classification of the intersection or of the coupled Chow presentation. Its
asymptotic safe block grows like `((1+sqrt(2))/2)^n/sqrt(n)`, still far below
Glynn's scale. The result is a valid reusable correction, not a complete
strategy for exact rank.

## 8. Claim boundary

The proper status is

```text
PROOF_DRAFT_COMPLETE
EXACT_INTEGER_ARITHMETIC_REPLAYED
GENERAL_N_PROGRESS
```

with no exact-rank, border-rank, or novelty promotion.
