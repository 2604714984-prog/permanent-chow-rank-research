# Audit report: ordinary Chow rank of `perm_6`

**Audit date:** 2026-08-21  
**Repository:** `2604714984-prog/permanent-chow-rank-research`  
**Audit type:** adversarial internal proof review and artifact-consistency review  
**Reviewer:** GPT-5.6 Pro, acting as an AI-assisted internal reviewer rather than a human external referee  
**Claim type:** ordinary Chow rank over characteristic zero; no border-Chow-rank claim is reviewed here

## 1. Frozen review boundary

This report distinguishes three separate proof levels and freezes each one to an immutable repository state.

| Level | Frozen reference | Status reviewed |
|---|---|---|
| Unconditional `main` theorem | commit `111a022c8de36619c32a0c2cf660aa4dd5b5aeab` | lower bound 25 |
| Stacked lower-28 branch | commit `51348d4277c50cf1a7dd45af3dc76aeee26ae7a0` in PR #31 | proposed lower bound 28 |
| Exact-rank-32 candidate | commit `d1860fbef77575938d517be2c4bf8dfd9509d596` in PR #90 | conditional reduction only |

PR #31 currently points at commit `29f8d40452e673961840ebcd22dc0a7af2418171`. That commit has `51348d4277c50cf1a7dd45af3dc76aeee26ae7a0` as its parent and adds `perm_7` work. The `perm_6` assessment in this report remains frozen to the parent commit and does not automatically cover later changes to the `perm_6` proof stack.

Relevant pull requests:

- PR #31: <https://github.com/2604714984-prog/permanent-chow-rank-research/pull/31>
- PR #90: <https://github.com/2604714984-prog/permanent-chow-rank-research/pull/90>

## 2. Executive verdict

The audit verdict is:

| Claim | Verdict | Permitted repository wording |
|---|---|---|
| `ChowRank(perm_6) >= 25` at frozen `main` | **No blocking gap found** | May be treated as the current unconditional internal theorem |
| `ChowRank(perm_6) >= 28` from PR #31 | **Promising but not finally accepted by this audit** | Keep as an unmerged, frozen-candidate claim pending a narrow final audit packet |
| `ChowRank(perm_6) = 32` from PR #90 | **Not proved** | Must remain explicitly conditional on the unrestricted local quotient-symbol proposition |

Accordingly, the unconditional statement supported by the frozen `main` branch is

\[
25 \leq \operatorname{ChowRank}(\operatorname{perm}_6) \leq 32.
\]

This report does not promote the repository to an unconditional exact-rank-32 claim.

## 3. Audit methodology and limitations

The review traced the mathematical dependency chain, inspected the proof documents, checked the direction of the principal dimension and semicontinuity arguments, compared formulas against the exact-arithmetic audit scripts and frozen outputs, and inspected the focused tests and claim-boundary language.

The audit particularly targeted the following failure modes:

1. reversing upper semicontinuity or specialization inequalities;
2. silently replacing an arbitrary decomposition by a general-position one;
3. normalizing several local terms separately when only one common ambient quotient is available;
4. treating a replay table as a derivation of its load-bearing entries;
5. adding local rank contributions without correctly subtracting relation overlap;
6. omitting an extremal defect profile or endpoint layer;
7. confusing ordinary Chow rank with border Chow rank;
8. allowing the prose theorem to exceed what the scripts and certificates actually establish.

This is not a formal proof-assistant verification. It is also not a clean-room rerun of every repository computation from a fresh checkout, and it does not establish literature priority. Computational artifacts are accepted only for the exact finite statements they encode; they do not replace missing universal geometric arguments.

## 4. Audit of the unconditional lower-25 proof

### 4.1 Primary artifacts

The principal lower-25 artifacts are:

- [`n6_fixed_six_lower25.md`](n6_fixed_six_lower25.md)
- [`n6_fixed_six_lower25_adversarial_review.md`](n6_fixed_six_lower25_adversarial_review.md)
- [`vector_valued_macaulay_prolongation.md`](vector_valued_macaulay_prolongation.md)
- [`general_multidimensional_shadow_bound.md`](general_multidimensional_shadow_bound.md)
- [`../scripts/n6_fixed_six_lower25_audit.py`](../scripts/n6_fixed_six_lower25_audit.py)
- [`../scripts/n6_fixed_six_lower25_independent_audit.py`](../scripts/n6_fixed_six_lower25_independent_audit.py)
- [`../tests/test_n6_fixed_six_lower25_audit.py`](../tests/test_n6_fixed_six_lower25_audit.py)
- [`../data/n6_fixed_six_lower25.json`](../data/n6_fixed_six_lower25.json)

### 4.2 Proof architecture

The proof assumes a decomposition with 24 Chow terms, fixes six terms, and denotes the remaining eighteen-term residual by `R`. It then couples:

- the quadratic derivative space;
- the cubic derivative space;
- quadratic relations among the six fixed terms;
- first prolongations of those relations;
- a middle block-Sylvester map;
- exact finite optimization over the remaining defect profiles.

The proof reduces all possible configurations to a finite range of the fixed-six quadratic intersection parameter `b`, excludes the low endpoint by a first Koszul estimate, and excludes the remaining layers by comparing a fixed-six coupled-rank lower bound with the maximal capacity of the eighteen-term residual.

### 4.3 Load-bearing checks

#### A. Quadratic projection and the range of `b`

The proof uses the fixed-six projection cap

\[
\dim\!\left(E_2\cap\sum_{i=1}^{6}D_2(T_i)\right)\leq 78
\]

and the product-shadow estimate to restrict the relevant range of `b`. The audit found no reversal between image, intersection, and quotient dimensions in this reduction. The specialization argument is used in the conservative direction required for a lower-bound proof.

#### B. Vector-valued Macaulay prolongation

The proof requires a bound of the form

\[
\rho\leq \kappa^{\langle 2\rangle}
\]

for the cubic prolongation dimension `rho` of a colored quadratic relation space of dimension `kappa`.

The supporting argument degenerates the relation space to a colored monomial space, applies scalar Macaulay growth color by color, and combines the resulting successors. The audit found the semicontinuity direction and the color decomposition consistent with the claimed upper bound. No hidden assumption that the original relation space is already monomial was detected.

#### C. One-term middle-rank defect classification

For the relevant normal forms, the proof uses the cubic derivative dimensions

\[
14,14,18,20,20
\]

and the corresponding half-defects

\[
3,3,1,0,0.
\]

These values are consistent with the displayed normal forms and with the finite defect enumeration. No omitted worse normal form was identified within the classification used by the theorem.

#### D. Coupled block-Sylvester estimate

The proof subtracts relation overlap from the sum of local contributions using a loss term of the form `2 rho`. The two copies correspond to the two coupled block directions. The audit found no unsupported direct-sum assumption and no obvious double counting in the stated rank inequality.

#### E. Finite endpoint enumeration

The exact-arithmetic script enumerates the admissible defect profiles and evaluates every remaining `b` layer. The formulas in the proof document, script, tests, and frozen JSON are mutually consistent. The critical layers retain a strict positive margin rather than relying on a floating-point or equality-edge decision.

### 4.4 Lower-25 verdict

No fatal or major mathematical gap was found in the frozen lower-25 chain. In particular, the audit did not find:

- a circular invocation of the desired lower bound;
- a reversed semicontinuity argument;
- a hidden general-position replacement;
- an invalid direct addition of local ranks;
- an omitted endpoint in the finite optimization;
- a mismatch between the proof formulas and the exact-arithmetic replay.

The frozen `main` claim

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\geq 25
\]

is therefore acceptable as the repository's current unconditional internal theorem.

One non-blocking editorial repair is recommended: state explicitly how a decomposition with fewer than 24 summands is padded or split to the exact 24-term contradiction format, including the convention on scalar coefficients and zero terms. The intended reduction is standard, but the proof should make it explicit.

## 5. Audit of the proposed lower-28 proof in PR #31

### 5.1 Status of the candidate

The reviewed `perm_6` snapshot is commit

```text
51348d4277c50cf1a7dd45af3dc76aeee26ae7a0
```

within the stacked draft PR #31. The branch contains the claimed N6-071/N6-072 closure of the last lower-28 endpoint, together with a large dependency history and later unrelated `perm_7` work.

### 5.2 New load-bearing content beyond lower 25

The lower-28 promotion depends materially on two structural assertions:

1. **Common-quotient synchronization.** Same-row and same-column compression ranks and images for all six colors must be compared in one actual permanent quotient. Separate favorable coordinates for each color are not sufficient.
2. **All-singular hook exclusion.** After synchronization, the remaining all-singular, nonseparated hook-type locus must be excluded without assuming an invertible row or column block.

Representative artifacts include:

- [`n6_six_color_row_rank_synchronization.md`](n6_six_color_row_rank_synchronization.md)
- [`n6_all_singular_hook_exclusion.md`](n6_all_singular_hook_exclusion.md)
- [`../scripts/n6_six_color_row_rank_synchronization.py`](../scripts/n6_six_color_row_rank_synchronization.py)
- [`../scripts/n6_all_singular_hook_exclusion.py`](../scripts/n6_all_singular_hook_exclusion.py)
- [`../tests/test_n6_six_color_row_rank_synchronization.py`](../tests/test_n6_six_color_row_rank_synchronization.py)
- [`../tests/test_n6_all_singular_hook_exclusion.py`](../tests/test_n6_all_singular_hook_exclusion.py)

### 5.3 Audit concerns that remain before final acceptance

No direct counterexample or immediate arithmetic contradiction was identified. However, the final two structural steps are substantially more delicate than the lower-25 finite-layer optimization. A final acceptance audit must close the following questions in one frozen packet:

- Does every normalization act simultaneously on the six colors and the actual common quotient?
- Are all closure and collision strata included, including rank drops and nonseparated limits?
- Is any statement proved only on a dense chart but then applied to the full projective locus?
- Are the diagonal and wedge coordinates both retained throughout the synchronization argument?
- Does the all-singular exclusion cover every characteristic-zero component, rather than only coordinate or block-invertible representatives?
- Are the exact scripts deriving the relevant classifications, or merely replaying manually supplied representative tables?

The stacked PR spans many historical stages and unrelated later work. This makes it difficult to certify the exact dependency closure of the final lower-28 theorem from the PR surface alone.

### 5.4 Lower-28 verdict

The proposed lower bound

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\geq 28
\]

is **not rejected**, but it is not promoted to final audited status by this report.

The correct repository treatment is:

- keep the claim on a draft or otherwise explicitly provisional branch;
- freeze the exact `perm_6` dependency head;
- extract N6-071/N6-072 and their indispensable prerequisites into a narrow review packet;
- run one final adversarial audit focused only on common-quotient synchronization, closure strata, and all-singular hook exclusion.

No new framework is needed. The issue is proof concentration and dependency freezing, not additional architecture.

## 6. Audit of the exact-rank-32 candidate in PR #90

### 6.1 Primary artifacts

The exact-rank candidate is frozen at

```text
d1860fbef77575938d517be2c4bf8dfd9509d596
```

with the following principal files:

- [`n6_exact_ordinary_chow_rank_32_candidate.tex`](n6_exact_ordinary_chow_rank_32_candidate.tex)
- [`../scripts/n6_exact_ordinary_chow_rank_32_candidate.py`](../scripts/n6_exact_ordinary_chow_rank_32_candidate.py)
- [`../tests/test_n6_exact_ordinary_chow_rank_32_candidate.py`](../tests/test_n6_exact_ordinary_chow_rank_32_candidate.py)

The PR description correctly states that the repository's unconditional interval remains `25 <= ChowRank(perm_6) <= 32`.

### 6.2 What the candidate successfully establishes

The candidate gives a coherent global reduction: if every nonzero degree-six Chow term and every quotient of its actual factor span satisfy the proposed half-defect quotient-symbol inequality, then the filtered global rank comparison yields the lower bound 32. The audit did not find an immediate sign or constant error in the global cancellation mechanism.

In particular, the global argument correctly separates:

- the universal local proposition;
- the aggregation over decomposition terms;
- the defect cancellation;
- the final comparison with the permanent-side rank.

This is useful progress because it isolates one precise local theorem whose proof would close the exact-rank claim.

### 6.3 The decisive missing proposition

The candidate requires a universal local statement of the schematic form

\[
\operatorname{rank}\beta_{P,R}+\frac{20-u}{2}
\geq \frac{10}{3}d
\]

for every allowed Chow term, actual factor span, and quotient map.

That universal proposition is not proved in the candidate. The replay script checks the arithmetic consequences of a supplied table of local minimum ranks; it does not derive those minima from an exhaustive characteristic-zero classification of all quotient spaces and all relative embeddings.

This distinction is decisive:

```text
supplied local minima + arithmetic replay
```

is not equivalent to

```text
proof that those minima hold for every allowed complex quotient configuration.
```

Focused tests can establish that the replay is faithful to the displayed table. They cannot certify the unrestricted local geometry unless the classification or elimination that produces the table is itself included and checked.

### 6.4 Exact-rank-32 verdict

PR #90 is a valid **conditional reduction**, not a proof that

\[
\operatorname{ChowRank}(\operatorname{perm}_6)=32.
\]

The PR must remain draft and must retain explicit `CONDITIONAL` language until the unrestricted half-defect quotient-symbol proposition is established. Restricted coordinate slices, sampled quotients, or favorable orbit representatives are supporting evidence only and cannot close the universal claim.

## 7. Final repository status recommended by this audit

The mathematically accurate status is:

### Unconditional on frozen `main`

\[
\boxed{25\leq \operatorname{ChowRank}(\operatorname{perm}_6)\leq 32.}
\]

### Provisional stacked result

PR #31 proposes

\[
\boxed{28\leq \operatorname{ChowRank}(\operatorname{perm}_6)\leq 32,}
\]

but the lower-28 endpoint should remain provisional until the narrow synchronization and all-singular packet receives final review.

### Conditional exact-rank route

PR #90 reduces exact rank 32 to one unrestricted local quotient-symbol theorem. It does not currently prove that theorem.

## 8. Minimal next actions

Only two focused actions are recommended.

1. **Lower-28 closeout:** extract the exact N6-071/N6-072 dependency closure from PR #31 into a frozen, `perm_6`-only packet and audit the common quotient and all-singular closure strata line by line.
2. **Exact-32 closeout:** stop adding peripheral replay tables and prove the unrestricted local quotient-symbol proposition by a complete orbit stratification, deterministic elimination, or another finite certificate that covers the full complex parameter space.

The repository does not need a new control layer, a new certificate framework, or a broad re-audit of unrelated results. The remaining work is narrow and mathematical.

## 9. Audit disposition

| Severity | Count | Disposition |
|---|---:|---|
| Fatal finding against lower 25 | 0 | none found |
| Major blocking finding against lower 25 | 0 | none found |
| Minor editorial finding against lower 25 | 1 | exact-number-of-summands convention should be stated |
| Final-acceptance hold on lower 28 | 1 | freeze and audit the synchronization/all-singular packet |
| Fatal gap in unconditional exact 32 | 1 | unrestricted local quotient-symbol proposition remains unproved |

This report is scoped to the frozen references listed in Section 1. Any later change to a load-bearing `perm_6` lemma requires a new exact-head review.