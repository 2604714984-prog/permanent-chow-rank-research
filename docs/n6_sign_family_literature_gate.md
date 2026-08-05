# Literature gate for the `n=6` sign-family pilot

## Status

`BLOCKED_PENDING_FULL_TEXT_RECONCILIATION`.

This gate suspends implementation of the finite column-dependent sign pilot described in Section 7 of `docs/n6_research_program.md`. No sign-family search code, orbit enumerator, SAT layer, or decomposition claim is authorized until the comparison below is complete.

The current Chow-rank interval is unchanged:

\[
25\le \operatorname{ChowRank}(\operatorname{perm}_6)\le 32.
\]

## 1. Triggering reference

The arXiv record for

- Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*, arXiv:2311.05890,

states in its abstract that the paper:

1. derives Glynn's formula from Ryser's formula;
2. proves by an orbital argument that Glynn's formula gives an optimal row-homogeneous Chow decomposition of the permanent; and
3. gives a parametric description of rank-revealing row-homogeneous Chow decompositions.

Only the title, authors, date, and abstract have been independently retrieved in the present review. The full theorem definitions, hypotheses, proof, version differences, and precise meaning of `row-homogeneous` have not yet been ingested into this repository.

## 2. Why this blocks N6-17B

The proposed N6-17B pilot enlarges the column-uniform Glynn family to column-oriented sign terms

\[
G_A
=
\prod_{j=0}^{5}
\left(
\sum_{i=0}^{5}a_{ij}x_{ij}
\right),
\qquad a_{ij}\in\{\pm1\}.
\]

The abstract claim about optimal row-homogeneous decompositions may subsume, overlap with, or be logically incomparable to this family. The abstract alone does not determine which. Running a new orbit calculation before resolving that inclusion could duplicate a known theorem or attach an incorrect novelty interpretation to a restricted-family replay.

Therefore the repository fails closed:

```text
N6_17B_IMPLEMENTATION=BLOCKED
NOVELTY_CLAIM=FORBIDDEN
ROW_HOMOGENEOUS_EQUALS_COLUMN_SIGN_FAMILY=UNVERIFIED
COLUMN_SIGN_FAMILY_SUBSET_OF_ROW_HOMOGENEOUS=UNVERIFIED
ROW_HOMOGENEOUS_SUBSET_OF_COLUMN_SIGN_FAMILY=UNVERIFIED
```

## 3. Required family comparison

The full-text review must define and compare the following classes without silently identifying them:

- `F_uniform`: the 32 column-uniform Glynn sign products already treated by G-020;
- `F_one_defect`: terms in which one designated column may use a different normalized sign vector;
- `F_column_sign`: arbitrary normalized column-oriented sign matrices `A`;
- `F_row_sign`: the transposed row-oriented analogue;
- `F_row_homogeneous_XG`: the exact row-homogeneous family defined in arXiv:2311.05890;
- unrestricted Chow terms.

For every claimed inclusion or equality, the review must record the exact definition and theorem location in the paper. Transposition must not be used as a symmetry of `F_column_sign` unless `F_row_sign` is explicitly adjoined.

## 4. Minimum evidence packet

Before implementation resumes, add a source-bound note containing:

1. the exact arXiv version reviewed;
2. a hash or immutable source identity for the PDF or source archive;
3. the paper's definition of row-homogeneous decomposition;
4. the precise optimality theorem and the field assumptions;
5. the parametrization theorem and its scope;
6. an inclusion diagram for the six families listed above;
7. a verdict on whether G-020 is a rediscovery, a strict special case, or an independent reformulation; and
8. a verdict on whether the proposed one-defect or full column-sign pilot asks a genuinely uncovered question.

An abstract-only comparison is insufficient to clear the gate.

## 5. Decision table

| Full-text result | Repository action |
|---|---|
| The paper already proves optimality for `F_one_defect` or `F_column_sign` | close N6-17B as redundant; retain only an independently replayable reproduction if useful |
| The paper's family strictly contains G-020 but not the proposed pilot | reclassify G-020 as a known special case; narrow the pilot to the uncovered difference |
| The paper's family is incomparable with the column-oriented sign family | document the non-inclusion witnesses; only then run a bounded pilot |
| The definitions or theorem remain ambiguous | keep the route blocked |
| A shorter exact decomposition is found in the literature | update the upper bound before any further lower-bound work |

## 6. Hidden assumptions

The blocked pilot implicitly assumed that the column-dependent sign direction was not already resolved by existing row-homogeneous work. That assumption is currently unsupported.

It also assumed that a symmetry-reduced exact span computation would add research value. If the published parametrization already describes the relevant family, another enumerator would add reproducibility at most, not a new route.

## 7. Assume all assumptions are false

If the paper already covers the proposed family, the correct action is to stop sign-family development and classify the repository result as an independent replay or special-case proof. The current lower bound 25 remains the active endpoint; no replacement architecture is needed.

## 8. Strongest objection

The abstract may use `row-homogeneous` in a narrower sense than the proposed column-dependent sign family, so blocking all implementation may delay a genuinely distinct finite experiment.

That objection is valid but not sufficient to bypass the gate. The cost of reading and mapping the full theorem is small relative to implementing an orbit search under an unverified novelty premise.
