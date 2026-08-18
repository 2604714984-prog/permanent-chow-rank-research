# Permanent Chow-rank research progress — 2026-08-18

## Purpose and evidence boundary

This document consolidates the current accessible state of the dedicated
mathematics repository and records the result developed in the immediately
preceding research session. It is a progress index, not a second theorem
registry. `RESEARCH_LEDGER.md` remains the canonical high-level ledger and
`STATUS.md` remains the detailed theorem inventory.

Open pull requests are reported as stacked or parallel drafts. They are not
canonical on `main` until merged or rebased into a clean main-target pull
request. Route ceilings are limits on named lower-bound mechanisms; they are
not upper bounds on actual Chow rank.

## 1. Canonical small-order baseline

The accepted small-order chain is

```text
ChowRank(perm_3) = 4
ChowRank(perm_4) = 8
ChowRank(perm_5) = 16
```

The `n=3` proof is linear algebra. The `n=4` proof uses the exact first-Koszul
rank, low-rank quadratic classification, the `psi_v` chart and the
double-quotient inequality. The repaired `n=5` proof preserves the coupled
catalectic firewall and binds its deterministic certificates at merged PR #30.

## 2. Current accessible numerical research boundaries

```text
perm_6:   28 <= ChowRank <= 32                 PR #31
perm_7:   49 <= ChowRank <= 64                 PR #51 stack
perm_8:   90 <= ChowRank <= 128                PR #51 stack
perm_9:  164 <= ChowRank <= 256                PR #51 stack
perm_10: 307 <= ChowRank <= 512                PR #51 stack
```

Earlier stacked lower bounds remain recorded for `n=11,...,16`, but the full
degree-tower replay was not extended uniformly to every one of those sizes.
No unrestricted exact value for `perm_6` or any larger order is established in
the currently accessible repository state.

## 3. General-n research map

### 3.1 Exact shadows and derivative towers

The main scalar/shadow stack consists of:

```text
PR #35  exact simultaneous product shadows via Ferrers integer programs
PR #38  zero-intersection block removal inside nonzero-intersection proofs
PR #47  cross-degree block projection
PR #48  recursive derivative-tower capacities
PR #51  full-degree prefix-envelope saturation thresholds
PR #52  shadow-complement duality and max-plus deficit transport
PR #53  tail localization and the central-window theorem
PR #55  polynomial ceiling for the complete scalar tower
```

The complete named scalar tower satisfies the route ceiling

```text
Theta_n = O(n^(1/4) * binom(n,floor(n/2)))
        = O(2^n / n^(1/4)).
```

This closes the current scalar-cardinality mechanism as a route to general
Glynn optimality. It does not close a shadow argument strengthened by a
uniform Chow-realizability defect.

### 3.2 Apolar, matrix-image and presentation-data barriers

The following programs have been made precise and then bounded or rejected:

```text
PR #56  two-direction apolar subquotients and homogeneous power profiles
PR #57  bounded-size binary matrix-image routes
PR #58  nonuniform shifted matrix-image routes
PR #59  raw Fitting/Betti failures and legal one-line Fitting/Jordan data
PR #65  exact-additive graded K0/syzygy scalars collapse to Hilbert data
PR #66  full-orbit equivariant exact-additive profiles pay a regular tax
```

The common lesson is that exact-additive scalarizations lose the relation
information required to beat central-binomial scale, while raw Betti and
higher-Fitting data do not automatically satisfy the subquotient monotonicity
needed by the apolar decomposition argument.

### 3.3 Koszul–Young, matching and representation projections

```text
PR #62  unprojected standard Koszul–Young maps and projected catalecticants
PR #63  arbitrary fixed linear postprocessing after matching derivatives
PR #64  two-sided matching-source compression
```

These results close fixed linear processing of the matching derivative image,
including standard wedge degrees, stable row-column isotype sums and canonical
source/target compressions, at central-binomial scale. They do not close a
minimal syzygy functor, nonlinear determinantal data or a term-dependent
valuative construction.

### 3.4 Current parallel branches after PR #67

PR #67 is the common stabilizer-efficient orbit base for three parallel
experiments:

```text
PR #68  apolar multiplication-tensor framework
PR #69  growing two-direction power ceiling
PR #70  closed factor-span endpoint zero blocks
```

These branches are parallel rather than cumulative. A future consolidation
must not silently treat PRs #68, #69 and #70 as one linear proof stack.

## 4. Result from the immediately preceding research session

PR #70 proves the following general endpoint theorem.

Let

```text
E_m = D_m(perm_n),
F_i = D_m(T_i),
L_i = factor span of T_i.
```

If

```text
m >= 3,
q >= 2,
L_1 + ... + L_q = L_1 direct_sum ... direct_sum L_q,
sum_i dim(L_i) <= m^2,
```

then

```text
E_m intersect (F_1 + ... + F_q) = 0.
```

Consequently the previously open term-count equality endpoint is closed:

```text
q*n = m^2,
m >= 3,
q >= 2
```

implies that every arbitrary `q`-term Chow block has zero
permanent-relative intersection.

The closed guaranteed zero-block size is

```text
zeta(n,m)
  = floor((m^2 - 1)/n)
    + indicator(m>=3 and n divides m^2 and m^2/n>=2).
```

For every larger literal sum of `Q` terms,

```text
dim(E_m intersect sum_(i=1)^Q D_m(T_i))
  <= (Q-zeta(n,m))*binom(n,m).
```

The assumptions are sharp in the stated sense:

```text
q=1, n=m^2  admits an embedded perm_m derivative witness;
m=2, n=2, q=2 is the two-matching decomposition of perm_2.
```

Evidence in PR #70:

```text
docs/general_closed_factor_span_endpoint_zero_blocks.md
docs/general_closed_factor_span_endpoint_zero_blocks_adversarial_review.md
scripts/general_closed_factor_span_endpoint.py
scripts/general_closed_factor_span_endpoint_independent.py
data/general_closed_factor_span_endpoint.json
tests/test_general_closed_factor_span_endpoint.py
```

Frozen theorem core:

```text
7d78c0e595d25130a9bf2f9dd843ef88f3be737004f33b3f85f3be1170eb376a
```

The focused endpoint replay passes. The full inherited repository workflow on
the original PR #70 head failed for unrelated compatibility regressions in the
older scalar-tower stack; the endpoint-specific tests themselves passed.

## 5. CI diagnosis at PR #70 head

Workflow run `32098702656` reached 803 tests. The new endpoint tests passed:

```text
test_endpoint_sizes       PASS
test_frozen_payload       PASS
test_independent_replay   PASS
test_projection_cap       PASS
test_sharp_exceptions     PASS
```

The full job failed for two inherited compatibility issues:

1. four older tower consumers call `ExactProductShadow.transition`, while the
   current shared implementation exposes `minimum` and the binary-search logic
   only through `exact_intersection_cap`;
2. one theorem-boundary test requires the literal word `central` in the
   principal-ideal route-ceiling description.

These are software-interface regressions, not counterexamples to the PR #70
mathematics. They must nevertheless be repaired before the branch can be
called full-CI clean.

## 6. Current primary frontier

The next authorized Chow-realizability interface is the small-excess regime

```text
q*n = m^2 + s,
```

with `s` small. The target is a quantitative theorem of the form

```text
dim(E_m intersect sum_i D_m(T_i)) <= Psi_(n,m)(s),
```

where `Psi_(n,m)(s)` is substantially smaller than the unrestricted
arbitrary-subspace capacity. A center/idempotent defect, a valuative
leading-relation packet or a minimal-syzygy envelope would all be legitimate
mechanisms. Another larger scalar shadow table is not the default route.

## 7. Promotion rules

- Keep all mathematical proof files in English.
- Do not call an open stacked or parallel result canonical on `main`.
- Do not promote finite-field equality without the characteristic-zero
  direction.
- Do not replace a coupled catalectic or apolar object by a literal sum without
  a theorem.
- Record counterexamples and rejected implications.
- Update `RESEARCH_LEDGER.md` or a clearly linked ledger delta in the same PR.
- Do not introduce a manager, registry, dispatcher, database or second control
  plane for the research ledger.
