# Adversarial review of the `n=6` one-defect sign theorem

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_RESTRICTED_FAMILY_PROOF_DRAFT
PRIMARY_FINITE_AUDIT=PASS
INDEPENDENT_FEATURE_RANK_REPLAY=PASS
UNRESTRICTED_CHOW_RANK_CHANGED=false
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed claim is only

\[
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
\]

The active unrestricted interval remains `25..32`.

## 1. Normalization and duplicate terms

Each column factor is projectively normalized by fixing its row-zero
coefficient to `+1`; the absorbed product of normalization signs is part of the
scalar coefficient of the Chow term. Thus every normalized column-sign vector
is one of 32 vectors.

A nonuniform one-defect term has five copies of one vector and one copy of a
different vector. Its majority vector, exceptional column, and defect vector
are unique. Uniform terms have six indexed presentations; the proof explicitly
collects them as one term and assigns one arbitrary exceptional-column label
only for bookkeeping. Hence the support lower bound does not count duplicate
presentations as distinct summands.

The resulting distinct family size is

\[
32+6\cdot32\cdot31=5984.
\]

## 2. Character and parity decomposition

For a base sign label `a`, defect `v`, exceptional column `j`, and row
assignment `r`, the coefficient identity

\[
[T_{a,v,j}]_r=(-1)^{a\cdot\pi(r)}s_v(r_j)
\]

was checked in all `32^3*6=196608` cases. More importantly, it follows
algebraically from the character law and is not inferred from the finite
check.

Fourier transformation in `a` is invertible over every characteristic-zero
field because 32 is invertible. Distinct parity fibers have disjoint monomial
support, so their span dimensions add without a coupled-image assumption.

## 3. Exact non-target feature kernels

On every parity fiber, five explicit position-constant relations vanish:

\[
\sum_r e_{j,r}-\sum_r e_{0,r},
\qquad 1\le j\le5.
\]

They are independent, so every additive-feature matrix has rank at most 31.
For the five non-target Hamming-weight representatives, the primary audit gives
nonzero `31 x 31` integer minors with determinants

```text
-32, 32, -32, -32, -32.
```

The non-target kernels therefore have dimension exactly five and consist only
of position constants whose total is zero. Permuting the five nonzero row
labels carries each parity vector to the canonical vector of the same Hamming
weight, so the six representative calculations cover all 32 parity blocks.

## 4. Exact target feature kernel

The target parity fiber is exactly the 720 permutations of `0,...,5`. Besides
the five position relations, five independent row-total relations vanish:

\[
\sum_j e_{j,i}-\sum_j e_{j,0},
\qquad 1\le i\le5.
\]

The ten displayed relations are independent in characteristic zero. Thus the
target feature rank is at most `36-10=26`. A `26 x 26` integer minor of
determinant one gives the equal lower bound. This supplies an explicit proof of
the target rank rather than relying on an informal reference to the affine
span of permutation matrices.

## 5. Independent replay

The primary audit uses modular elimination only to select minors and then
computes their determinants over the integers by Bareiss elimination.

The independent script

```text
scripts/n6_one_defect_sign_independent_audit.py
```

does not import the primary implementation. It uses a different prime,
`1,000,033`, reconstructs the parity fibers, verifies the explicit five- and
ten-dimensional kernel spaces, and obtains the matching modular lower ranks

```text
31, 31, 31, 31, 31, 26.
```

Because these are ranks of integer matrices, the modular ranks are valid
characteristic-zero lower bounds; the explicit kernels are characteristic-zero
upper bounds. Their equality proves the exact ranks independently.

## 6. Lower-support argument

After collecting repeated terms, let `W_j(a)` be the row function contributed
by terms with base label `a` and exceptional position `j`. On every non-target
parity block, the exact kernel classification forces each Fourier transform
`W_hat_j(p)` to be constant, with constants summing to zero.

Modulo constants, Fourier inversion leaves only the target character. There
are two exhaustive cases.

1. Some nonconstant quotient class survives. It is a nonzero multiple of the
   target character at all 32 base labels, so at least one summand occurs at
   every base label.
2. Every quotient class vanishes. The sum of the constant parts has Fourier
   support only at the target character. The target coefficient equation fixes
   it to `(1/32)*chi_target`, which is nonzero at all 32 base labels. Again at
   least one summand occurs at every base label.

Both cases give support at least 32. Glynn gives 32, so the restricted minimum
is exact.

## 7. Strongest objections

### Objection A — a different sign normalization could evade the proof

It cannot. Independent projective rescaling of each column factor changes only
the scalar coefficient of the product and yields the normalized family used in
the theorem.

### Objection B — transposition enlarges the family

Transposition maps the column-oriented one-defect family bijectively to a
separately defined row-oriented one-defect family. It is not treated as an
internal column-family symmetry. Permanent invariance transfers the restricted
minimum between the two families but does not reach arbitrary row-homogeneous
terms.

### Objection C — a 31-term decomposition could use cancellations among many
terms sharing one base label

The proof allows arbitrary cancellations inside every `W_j(a)`. It uses only
whether the aggregate row function is zero. Fourier support forces a nonzero
aggregate at each of 32 base labels in both exhaustive cases.

### Objection D — the theorem implies unrestricted rank 32

It does not. The full normalized column-sign family allows six unrelated sign
vectors, and unrestricted Chow factors may mix rows and columns arbitrarily.
Neither class is controlled here.

## 8. Claim boundary

The appropriate repository status is

```text
PROOF_DRAFT_COMPLETE
COMPUTATION_REPLAYED
RESTRICTED_FAMILY_THEOREM
```

not `VERIFIED_BASELINE` and not an unrestricted rank theorem.
