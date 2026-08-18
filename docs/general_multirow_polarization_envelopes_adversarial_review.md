# Adversarial review: dyadic multirow polarization envelopes

## Verdict

`PROOF_DRAFT_COMPLETE_WITH_EXACT_INTERFACE_REPLAY`.

The theorem is valid within its stated characteristic-zero and literal
derivative-space scope. The proof does not establish sharpness for
intermediate term counts, a new Chow-rank lower bound, or a border-rank
statement.

## 1. Claim under review

For

\[
1\le t\le m,\qquad n\ge m(m-t+1),
\]

the branch constructs \(2^{t-1}\) degree-\(n\) Chow terms whose
output-degree-\(m\) derivative spaces contain a common linear combination
equal to one \(m\times m\) coordinate subpermanent of
\(\operatorname{perm}_n\).

The construction must pass four separate checks:

1. the Walsh sum selects exactly the row-bijective monomials;
2. the selected local permanents assemble to the full \(m\times m\)
   permanent;
3. every sign component is contained in one actual Chow derivative space; and
4. the witness survives degree extension.

All four checks pass.

## 2. Walsh normalization

The first row sign is fixed to \(+1\), leaving \(2^{t-1}\) sign vectors.
For an assignment with row multiplicities \(c_r\), its unnormalized
coefficient is

\[
\sum_{\varepsilon}
\prod_{r=1}^{t-1}\varepsilon_r^{1+c_r}.
\]

This factorizes into \(t-1\) two-point character sums. It equals
\(2^{t-1}\) exactly when every \(c_r\), \(r\ge1\), is odd, and is zero
otherwise.

Because there are \(t\) slots and \(t-1\) required positive odd counts, no
count can be three or larger. Hence all selected-row counts equal one,
including the first row. The surviving assignments are exactly the
bijections.

The normalization factor \(2^{1-t}\) is therefore correct. There is no
missing \(t!\): each bijection is already one distinct multilinear monomial,
not one occurrence inside a homogeneous power.

Finite replay checks every weak multiplicity vector through \(t=9\) and every
ordered assignment through \(t=6\). It also expands the complete
row-Laplace construction for all 21 pairs \(1\le t\le m\le6\), covering
1,936,741 signed envelope monomials. The independent implementation repeats
the ordered-assignment check with a bit-mask Walsh transform.

## 3. Laplace assembly

For a fixed \(t\)-column set \(C\), the Fourier selector produces the
permanent on the selected \(t\) rows and columns \(C\). Multiplication by the
complementary permanent uses exactly the remaining rows and columns.

Summing over all \(t\)-subsets \(C\) is the ordinary row-Laplace expansion of
the permanent. Every permutation monomial appears once, indexed by the set of
columns occupied by the selected rows. No sign occurs because the permanent,
not the determinant, is being expanded.

The empty complementary permanent at \(t=m\) is correctly set to one.

## 4. Chow-envelope membership

For one sign vector, the proposed factor frame contains

\[
m+m(m-t)=m(m-t+1)
\]

linear factors.

The \(m\) transformed column factors are independent because different
columns use disjoint coordinate-variable blocks. They are also independent
from all coordinate factors in rows \(t,\ldots,m-1\), since those variables
do not occur in the transformed factors.

A monomial of \(G_\varepsilon\) selects:

- \(t\) transformed factors in distinct columns; and
- \(m-t\) coordinate factors, one in each remaining row and column.

Thus it is a squarefree product of exactly \(m\) factors from the frame. For
a product of independent factors, every such \(m\)-factor subproduct occurs
in the output-degree-\(m\) derivative space after differentiating away the
other factors. This proves actual Chow-derivative origin, not merely support
containment in a symmetric power.

## 5. Extension to larger degree

Multiplying an envelope by \(n-m(m-t+1)\) additional independent factors
creates a degree-\(n\) Chow term. Differentiating every added factor once and
every unselected original factor once recovers each original
output-degree-\(m\) subproduct up to a nonzero scalar.

There are enough ambient directions. When \(n=m\), no added factor is needed.
When \(n>m\),

\[
n^2-m^2=(n-m)(n+m)\ge n-m
\]

provides at least as many coordinate directions outside the chosen
\(m\times m\) block as any extension requires.

The chosen \(m\times m\) subpermanent belongs to
\(\mathcal D_m(\operatorname{perm}_n)\) by the standard subpermanent
description of permanent derivatives.

## 6. Endpoint checks

### \(t=1\)

The sign set is a singleton. The envelope is the product of all \(m^2\)
coordinates in the chosen block, and row-Laplace expansion places
\(\operatorname{perm}_m\) in its derivative space.

### \(t=2\)

The formula becomes

\[
\frac12(G_+-G_-),
\]

with the same \(a_j=x_{0j}+x_{1j}\) and
\(b_j=x_{0j}-x_{1j}\) construction as the parent pair-threshold result.

### \(t=m\)

There is no complementary permanent. Each \(G_\varepsilon\) is one product of
\(m\) linear forms, so the identity is the standard
\(2^{m-1}\)-term sign decomposition.

These checks show that the intermediate family genuinely interpolates
between established endpoints.

## 7. Arbitrary \(q\) and fixed-degree inversion

If \(2^s\le q\), a nonzero \(2^s\)-term literal sum remains contained in a
\(q\)-term literal sum after adding arbitrary extra Chow terms. No assertion
about their coefficients or coupled derivative image is needed.

At a fixed degree \(n\), the smallest staircase exponent supplied by this
construction is

\[
s=\min\{m-1,\max\{0,m-\lfloor n/m\rfloor\}\}.
\]

Indeed,

\[
m(m-s)\le n
\]

is equivalent to

\[
s\ge m-n/m,
\]

and the smallest integral solution is \(m-\lfloor n/m\rfloor\), clipped to
the legal interval.

The primary replay checks this inversion on every staircase cell through
\(m=64\); the independent replay extends it through \(m=128\).

## 8. Coupled/literal firewall

The forms \(G_\varepsilon\) are generally not Chow terms. The proof uses only

\[
G_\varepsilon\in\mathcal D_m(T_\varepsilon)
\]

and the literal vector-space sum of these derivative spaces.

It does not claim

\[
\mathcal D_m\!\left(\sum_\varepsilon T_\varepsilon\right)
=
\sum_\varepsilon\mathcal D_m(T_\varepsilon),
\]

nor does it replace any coupled catalectic object by a direct sum.

## 9. Characteristic and field scope

The normalization divides by \(2^{t-1}\). Characteristic zero is sufficient.
The proof also works over fields of characteristic different from two, but
the branch deliberately retains the repository's characteristic-zero scope
and makes no broader claim.

## 10. Rejected overclaims

The following conclusions do not follow and are not stated:

- \(2^{t-1}\) is minimal for \(2<t<m\);
- \(m(m-t+1)\) is the exact first nonzero degree for \(q\ge3\);
- the construction improves a Chow-rank lower bound;
- the intermediate identities are ordinary Chow decompositions of
  \(\operatorname{perm}_n\);
- the result transfers automatically to border Chow rank; or
- literature novelty has been established.

## 11. Evidence reviewed

```text
docs/general_multirow_polarization_envelopes.md
scripts/general_multirow_polarization_envelopes.py
scripts/general_multirow_polarization_envelopes_independent.py
data/general_multirow_polarization_envelopes.json
tests/test_general_multirow_polarization_envelopes.py
```

Validation:

```text
primary normal Python                         PASS
primary python -O                            PASS
independent normal Python                    PASS
independent python -O                        PASS
focused unit tests                           5/5 PASS
compileall                                   PASS
frozen JSON equals regenerated payload       PASS
```
