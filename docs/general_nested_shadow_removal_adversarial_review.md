# Adversarial review of nested shadow removal

## Verdict

```text
PRE_EXISTING_ZERO_INTERSECTION_THEOREM=CORRECTLY_ATTRIBUTED
NEW_PROJECTION_LEMMA=PASS
COUPLED_LITERAL_FIREWALL=PASS
CERTIFICATE_ARITHMETIC=PASS
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

## 1. Prior-result boundary

The permanent derivative-shadow lower bound and the zero-intersection
criterion already occur in `docs/general_n_koszul_bounds.md`. This work must
not describe them as newly proved. The new content is only the use of a
zero-intersection label block inside a larger nonzero-intersection fixed sum.

## 2. Section-and-projection lemma

A section of the literal summation map exists over any vector subspace. If its
projection away from the omitted labels vanishes, the represented vector lies
in the permanent intersection with the omitted block. The existing
zero-intersection theorem forces that vector to vanish. Hence the projection
is injective and the dimension bound is valid even when the individual
literal spaces have relations.

## 3. Coupling semantics

For the fixed polynomial `R=sum_i T_i`, the proof uses only

```text
D_k(R) subset sum_i D_k(T_i).
```

It does not replace the coupled catalectic image by the literal sum. Enlarging
the target space can only weaken the upper bound, so the direction is safe.

## 4. Selection budget

The enlarged number of fixed terms is checked against the global
first-Koszul lower bound in every finite row. Thus the proof never selects
more named summands than a hypothetical decomposition is already known to
contain.

## 5. Exact product-shadow arithmetic

At `n=7`, fourteen fixed terms minus one omitted term retain the old capacity
455, cap 238 and residual count 29, producing 43. At `n=8`, fifteen minus one
retain capacity 784, cap 560 and residual count 63, producing 78.

## 6. General certificate reuse

The old Bukh witness and intersection cap are not recomputed under a changed
threshold. The threshold is exactly unchanged. Hence the former residual
count remains valid and the total increases by the certified omitted-block
size. The `n=15` four-term block uses the pre-existing degree-two output
witness `420<441`.

## 7. Strongest objection

The construction is all-or-nothing: it removes a block only while its
permanent intersection is zero. It provides no bound once one additional term
makes a nonzero intersection possible. Consequently it improves existing
bounds but does not alter their leading asymptotic scale.

## 8. Claim boundary

The appropriate status is

```text
PROOF_DRAFT_COMPLETE
EXACT_INTEGER_ARITHMETIC_REPLAYED
GENERAL_N_PROGRESS
```

with no exact-rank, border-rank, unrestricted `perm_6`, or novelty promotion.
