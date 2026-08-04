# Adversarial review of the fixed-six lower-25 proof draft

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_PROOF_DRAFT
FINITE_ARITHMETIC=INDEPENDENT_REPLAY_PASS
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
EXTERNAL_PEER_REVIEW=NOT_PERFORMED
LITERATURE_NOVELTY_REVIEW=PRELIMINARY_ONLY
```

The reviewed claim is

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge25
\]

over characteristic zero. The proof assumes a 24-term decomposition, fixes six terms, and excludes every resulting central-intersection state.

## 1. Coupling semantics

The proof consistently defines

\[
H_3=\mathcal D_3(T_1+\cdots+T_6)
\]

as the coupled middle-catalectic image. The literal sums

\[
\sum_i\mathcal D_2(T_i),
\qquad
\sum_i\mathcal D_3(T_i)
\]

are used only as ambient spaces and inside explicit relation-kernel arguments. No step asserts that the coupled image equals a literal derivative-space sum.

## 2. Vector-valued Macaulay lemma

The former highest-risk step has been rewritten with:

1. a universal vector-bundle map on the Grassmannian whose fiber kernel is the first prolongation;
2. upper semicontinuity of fiber nullity;
3. an explicit integer one-parameter subgroup separating all colored quadratic monomials;
4. splitting of the coordinate limit by color;
5. the scalar apolar Macaulay bound; and
6. superadditivity of the degree-two Macaulay successor.

The finite audit verifies the explicit weights for 36 variables and six colors, all six-part partition inequalities through relation dimension 16, and an exhaustive 2,825-subspace divided-power counterexample search in the smallest nontrivial model. The finite-field search is diagnostic only.

## 3. Relation and coupled-rank inequalities

For the quadratic relation module `K` and cubic relation module `R`, differentiation gives

\[
\mathcal R\subseteq\mathcal K^{(1)}.
\]

Thus

\[
\rho\le\kappa^{\langle2\rangle}.
\]

For the six symmetric middle catalectics, the factorization

\[
A=\Sigma\operatorname{diag}(A_i)\Delta
\]

and Frobenius--Sylvester give

\[
\operatorname{rank}A
\ge
\sum_i\operatorname{rank}A_i-2\rho.
\]

The equality of the horizontal and vertical intermediate ranks uses symmetry only to identify the sum of row spaces with the sum of image spaces. It does not assume rank additivity of the coupled sum.

## 4. Individual term profiles

If the six factors span at most four variables, the quadratic derivative space has dimension at most ten. If they span five variables, the term is equivalent to

\[
x_1x_2x_3x_4x_5(x_1+\cdots+x_s),
\]

and exact catalectic ranks give the profiles

```text
11/14, 11/14, 13/18, 14/20, 15/20.
```

Six independent factors give `15/20`. Therefore quadratic dimension 12 is impossible. The finite audit deliberately assigns central-rank lower bound zero below dimension 11, so no missing low-profile classification enters the contradiction.

## 5. Independent arithmetic

The primary generator checks rational Bukh separators, term profiles, Macaulay values, symmetric defect types, and every strict margin. A second implementation scans all

\[
16^6=16,777,216
\]

labelled quadratic-defect tuples without importing the primary generator. Both reproduce the minimum central-rank bounds. The smallest margins are two at `b=43` and `b=44`.

## 6. Remaining boundaries

The proof does not establish:

- `ChowRank(perm_6)>=26`;
- a border Chow-rank lower bound of 25;
- `ChowRank(perm_6)=32`;
- literature novelty; or
- external peer-reviewed validity.

The appropriate repository status is `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, not `VERIFIED_BASELINE`.
