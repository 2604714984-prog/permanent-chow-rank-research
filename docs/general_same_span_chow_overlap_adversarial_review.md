# Adversarial review: same-span Chow derivative overlaps

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_PROOF_DRAFT
PRIMARY_EXACT_REPLAY=PASS
INDEPENDENT_REPLAY=PASS
NEW_UNRESTRICTED_CHOW_RANK_BOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY=NOT_ESTABLISHED
```

The reviewed theorem is restricted to two independent-factor Chow terms whose
factor spans are the same \(n\)-plane.

## 1. Hidden assumptions

### Same factor span

The identification of both derivative spaces with squarefree subspaces of one
symmetric algebra requires

\[
\operatorname{span}\{x_i\}
=
\operatorname{span}\{y_j\}.
\]

No claim is made for unequal factor spans.  In the general ambient permanent
problem, two Chow terms may span different \(n\)-planes.

### Independent factors

Each term must have \(n\) independent factors.  Degenerate Chow terms are
specializations, but the literal-overlap dimension is not used here through an
unproved semicontinuity direction.  Degenerate pairs remain outside the
theorem.

### Characteristic zero

The apolar pairing, torus specialization and ordinary Kruskal--Katona argument
are used over an infinite characteristic-zero field.  Every replay is over
integers or `Fraction`; no finite-field equality carries theorem
responsibility.

## 2. The dual/primal distinction

The theorem uses common projective directions of the **dual** bases.  This is
not cosmetic.

The annihilator of the squarefree quadratic space is the diagonal-square
space in the dual basis.  Therefore the relevant transition matrix is the one
between dual frames.  The explicit four-dimensional example has:

```text
dual shared directions=3
primal shared factors=1
common quadratic dimension=5
```

Substituting the primal count into the theorem would give a false bound.

## 3. Active-support reduction

The proof chooses one element of \(K(A)\) with support equal to the union of
all supports.  Such an element exists because the field is infinite: a finite
union of coordinate hyperplanes cannot cover the finite-dimensional space
\(K(A)\).

If the resulting diagonal matrix has support \(R\), then its zero rows force

\[
A_{R^c,S}=0.
\]

This uses injectivity of multiplication by \(A_S^{\mathsf T}\), which follows
from column independence.  It is not inferred merely from vanishing diagonal
entries.

## 4. Component algebra

After normalization, the equations are

\[
B\operatorname{diag}(c)
=
\operatorname{diag}(e)B.
\]

Thus every support edge forces equality of one row and one column parameter.
The solution dimension is exactly the number of connected components.

Invertibility of \(B\) is essential: it ensures that each component has equal
row and column cardinality.  Therefore every nonsingleton component consumes
at least two columns.

## 5. Sharpness

The two-by-two and three-by-three rational blocks have:

- invertible transition matrices;
- connected support graphs;
- diagonal \(BB^{\mathsf T}\);
- no one-sparse columns.

The odd remainder-one case is handled separately by \(I+E_{1n}\).  The proof
does not silently treat a one-dimensional nonshared block as possible.

## 6. Higher-degree shadow direction

For

\[
H_m=\mathcal S_m(x)\cap\mathcal S_m(y),
\]

the derivative shadow satisfies

\[
\partial^{m-2}H_m
\subseteq
\mathcal S_2(x)\cap\mathcal S_2(y).
\]

Torus specialization can only lower the derivative rank.  Hence the colex
shadow gives a lower bound for the original subspace, which is the direction
needed to obtain an upper bound on \(\dim H_m\).

The higher-degree cap is not asserted sharp.

## 7. Strongest objection

The theorem may still be too weak for the permanent problem.  A literal
overlap can satisfy the sharp same-span bound while the matched-difference
image is small, and the two Chow terms in an actual decomposition need not
have the same factor span.

This objection is correct.  The result is retained because it identifies a
precise frame-sensitive obstruction and rejects primal common-factor counting,
not because it closes a numerical Chow-rank bound.

## 8. Claim boundary

```text
same_factor_span=true
independent_factor_frames=true
quadratic_bound=SHARP
higher_degree_bound=VALID_NOT_CLAIMED_SHARP
literal_overlap_only=true
matched_difference=OPEN
unequal_factor_spans=OPEN
degenerate_terms=OPEN
new_perm6_perm7_perm8_bound=false
general_Glynn_optimality=OPEN
```
