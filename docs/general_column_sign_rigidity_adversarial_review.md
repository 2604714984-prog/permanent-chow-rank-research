# Adversarial review of full column-sign rigidity

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_RESTRICTED_FAMILY_PROOF_DRAFT
PRIMARY_EXACT_AUDIT=PASS_PENDING_CI
INDEPENDENT_N6_REPLAY=PASS_PENDING_CI
UNRESTRICTED_CHOW_RANK_CHANGED=false
COUNTEREXAMPLE_FOUND=false
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed claim is

\[
\operatorname{ColumnSignRank}(\operatorname{perm}_n)
=
\operatorname{RowSignRank}(\operatorname{perm}_n)
=2^{n-1}.
\]

It is a theorem only for the sign and anchored diagonal-sign families.

## 1. Normalization is lossless

A column-sign factor has row-zero coefficient `+1` or `-1`. Multiplying each
column factor by its row-zero sign makes every anchor equal to one. The product
of the `n` normalization signs is one nonzero scalar and is absorbed into the
coefficient of the Chow term.

Thus the proof does not discard any column-sign term. Normalization also makes
the coefficient matrix unique because the variable sets of the column factors
are disjoint.

## 2. The Boolean slice is a linear restriction

The proof retains coefficients of the monomials

\[
x_{00}\prod_{j=1}^{n-1}
(x_{jj}\text{ or }x_{0j}).
\]

Taking selected coefficients is a linear map on the ambient polynomial space.
It may identify different full terms, but this cannot invalidate a lower bound:
any full decomposition restricts to a decomposition of the slice with no more
terms.

The permanent is supported at exactly one slice monomial. If any nonzero mask
bit is replaced by row zero, row zero repeats and another row disappears, so
the resulting monomial cannot be a permanent monomial.

## 3. Off-diagonal signs cannot help on the slice

For a normalized term, each selected slice coefficient uses only:

- the row-zero anchor in columns whose mask bit is zero; and
- the diagonal coefficient in columns whose mask bit is one.

Every off-diagonal sign disappears. Terms with the same diagonal signature
therefore have the same slice vector.

This does not assume those terms are equal or linearly dependent in the full
polynomial space.

## 4. Same-signature cancellations are fully allowed

The proof aggregates all scalar coefficients of one signature:

\[
C_d=\sum_{t:d(T_t)=d}c_t.
\]

Walsh inversion determines `C_d`, not each individual term coefficient. Since
every required `C_d` is nonzero, each signature class must contain at least one
term after all cancellations are taken into account.

No linear-independence assumption is made inside a signature class.

## 5. Walsh inversion is valid in the stated field

The Walsh matrix satisfies

\[
HH^T=2^{n-1}I.
\]

It is invertible when the characteristic is not two. All aggregate
coefficients are `+2^(1-n)` or `-2^(1-n)` and are nonzero.

The proof makes no characteristic-two claim.

## 6. The upper bound belongs to the same family

Glynn's identity uses one row sign vector repeated in every column. These are
column-sign terms and lie in every defect family considered in the repository.
The upper and lower bounds therefore concern the same restricted dictionary.

## 7. Row-sign conclusion uses a bijection

Matrix transposition maps every row-sign term to one column-sign term and is
invertible. The permanent is transpose invariant. The row-sign conclusion is
not obtained by pretending transposition is an internal column-family symmetry.

## 8. Anchored enlargement is legitimate

For arbitrary off-diagonal coefficients with nonzero row-zero anchors and
normalized diagonal ratios in `{+1,-1}`, the same coefficient calculation
produces a Walsh character. The proof does not require the other entries to be
signs or nonzero.

This enlargement remains a proper subclass of arbitrary complex
row-homogeneous terms.

## 9. Strongest objections

### Objection A — two terms with different full matrices but one signature may
cancel on the slice

Allowed. Their scalar coefficients are combined into `C_d`. The required
aggregate is nonzero, so complete cancellation is impossible for that
signature in a permanent decomposition.

### Objection B — a shorter full decomposition may restrict to zero terms

A nonzero scalar multiple of a normalized sign term never restricts to zero:
its slice vector is a Walsh character with all entries `+1` or `-1`.

### Objection C — the slice may prove only tensor rank

The restriction is applied to actual polynomial Chow terms. The lower bound is
on the number of those terms in the restricted family. No polarization or
change of rank model occurs.

### Objection D — the theorem restores arbitrary row-homogeneous optimality

False. Arbitrary complex diagonal ratios yield general Segre vectors, not
Walsh characters. The proof supplies no lower bound in that family.

### Objection E — the theorem proves unrestricted rank 32

False. General Chow factors may mix all matrix variables and need not possess
the anchor/diagonal-sign structure. The unrestricted `n=6` interval remains
`26..32` by the separate N6-030 average-subset theorem.

## 10. Evidence boundary

The mathematical proof is a short exact character argument. Computation is a
transcription and regression interface:

- Walsh orthogonality and inversion are checked through `n=10`;
- deterministic full sign matrices with arbitrary off-diagonal patterns are
  checked;
- rational anchored matrices are checked;
- Glynn is expanded on every assignment through `n=6`; and
- an independent `n=6` implementation reconstructs the `32 x 32` system.

No full `2^30` family enumeration is needed or authorized.

## 11. Final classification

```text
PROOF_DRAFT_COMPLETE
COMPUTATION_REPLAYED
RESTRICTED_FAMILY_THEOREM
```

not `VERIFIED_BASELINE` and not an unrestricted Chow-rank theorem.
