# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank
research stack. It is updated in every GitHub synchronization that changes a
theorem, counterexample, route barrier, numerical boundary, equality
classification, or next mathematical frontier.

Last updated: **2026-08-19**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/cubic-three-term-zero
active PR: TO_BE_CREATED
parent branch: research/multirow-polarization-envelopes
parent PR: #83
parent exact head: ac8801ef067f3d0f6d5bff3b7f01fcbaa68af4e3
stack base: research/sharp-pair-threshold
```

The active branch must remain a narrow mathematical stack. Do not introduce a
manager, registry, dispatcher, database, solver framework, or second control
plane.

## 2. Latest research result

### Cubic three-term zero theorem

For arbitrary degree-four Chow terms over a characteristic-zero field,

```text
D_3(perm_4) intersect
(D_3(T_1)+D_3(T_2)+D_3(T_3)) = 0.
```

This closes the former cubic exception `(n,m,q)=(4,3,3)`.

The excess-`m` cubic arithmetic rows are now fully classified:

```text
(3,3,4) NONZERO -- accepted Glynn endpoint
(4,3,3) ZERO    -- current theorem
(6,3,2) NONZERO -- sharp pair theorem, PR #82
```

No Chow-rank lower bound, exact rank, border-rank improvement, or literature
novelty claim is introduced.

## 3. Proof spine

A hypothetical three-term witness forces the following exact state:

```text
component essential dimensions = 4,4,4
joint essential dimension       = 9
relation defect                 = 3
component overlap dimensions    = 3,3,3
private quadratic dimensions    = 1,1,1.
```

The proof chain is:

1. the permanent derivative-shadow floor forces at least nine essential
   variables;
2. `F_(4,2)(2)=6` caps every private quadratic space at dimension one;
3. private-mass equality forces the unique state above;
4. the three component four-planes are pairwise transverse;
5. each private quadratic has Hessian rank four;
6. every rank-four quadratic in `D_2(perm_4)` has essential space `U tensor V`
   for two two-planes with disjoint-support bases after scalar extension;
7. three pairwise-disjoint `2 x 2` tensor four-planes can span only dimension
   `8`, `10`, or `12`, never the forced dimension nine.

The exact tensor-plane statement is a parity restriction. The stronger-looking
claim that three such pairwise-disjoint planes must span at least ten dimensions
is false and must not be used.

## 4. Direct small-block frontier after this result

For three available terms at cubic output degree:

```text
n<=4 ZERO
n=5 OPEN
n>=6 NONZERO.
```

For general `m>=3`, the current direct three-term boundaries are

```text
zero through floor((m^2-1)/2)
explicitly nonzero from m(m-1).
```

For four available terms, the current direct nonzero construction begins at
`m(m-2)`. The shifted equality theorem also closes `n=m^2/3` when `3|m`,
`m>=6`.

These are direct boundaries from the current PR ancestry. Do not silently fold
in parallel recursive-zero branches.

## 5. Evidence and files

```text
docs/general_cubic_three_term_zero.md
docs/general_cubic_three_term_zero_adversarial_review.md
docs/general_cubic_three_term_zero_ledger_delta.md
docs/general_excess_m_cubic_boundary_clarification.md
scripts/general_cubic_three_term_zero.py
scripts/general_cubic_three_term_zero_independent.py
data/general_cubic_three_term_zero.json
tests/test_general_cubic_three_term_zero.py
RESEARCH_HANDOFF.md
```

Frozen theorem-facing core:

```text
e39a77e46607d1ad7c69e50c04ddedadc9d256dc98b80d86790d03aa9475b5d6
```

## 6. Validation receipt

Completed before publication:

```text
focused unit tests                         6/6 PASS
primary normal Python                         PASS
primary python -O                             PASS
independent normal Python                     PASS
independent python -O                         PASS
py_compile                                    PASS
frozen JSON == regenerated payload            PASS
non-ASCII scan of new proof files             PASS
```

Primary finite interfaces:

```text
private-polar surviving states                  1
rank-two zero-diagonal support models          25
tensor total dimensions                    8,10,12
direct q=3,4 rows through m=32                 60
```

Independent regression:

```text
support two-planes                             25
tensor-product four-planes                    625
pairwise-disjoint pairs                   132,300
pairwise-disjoint triples              12,510,100
observed total dimensions                  8,10,12
```

The independent `F_2` enumeration is a regression only. The characteristic-zero
claim is proved by the pure projection and rank-four block arguments.

## 7. Hosted CI state inherited from the parent

Parent PR #83 workflow run `#749` completed with failure after 885 tests. The
new PR #83 tests passed; the two reported failures were inherited repository
issues:

```text
1. exact-product-shadow payload compatibility hash mismatch
   observed: 18eb66f1b9460d2d793c69131cc4ebc0f1087c86b18f14e5638e71e6d629f567
   expected: 3563dd0205177cd0471210287dc8b2377e1547e2410a419b611b2560b123f06a

2. n6_global_t15_prolongation_cap full replay exceeded the 180-second
   subprocess timeout on the hosted runner.
```

Do not describe the inherited full suite as green. The current theorem has a
clean focused local receipt; hosted full CI must be reported separately.

## 8. Strict claim boundary

```text
cubic (4,3,3) = ZERO
cubic excess-m arithmetic rows = CLASSIFIED
cubic three-term (5,3,3) = OPEN
new numerical Chow-rank bound = false
new exact Chow rank = false
border-rank improvement = NO
coupled/literal identification = NO
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING / INHERITED FAILURES PRESENT
```

## 9. Next authorized mathematical task

Study the single remaining cubic three-term gap

```text
(n,m,q)=(5,3,3).
```

Start with an exact relation-defect ledger. The private quadratic cap remains
small because `F_(5,2)(2)=6>5`, but unlike `(4,3,3)` the private-mass inequality
no longer forces all three private spaces to be nonzero. The first target is
therefore a classification of the no-private and one-private branches, using
actual component essential spaces and the compressed-center interface only if
needed.

Do not begin with a broad SAT search, large orbit database, or another general
workflow layer.

## 10. Mandatory synchronization rule

Every future research synchronization must update this file in the same pushed
commit or in an immediately following publication-receipt commit. Each update
must record:

```text
exact branch and PR
exact head commit
new theorem or diagnostic
claim boundary
proof and data files
focused validation
hosted CI state
superseded statements
next executable mathematical task.
```

A result is not considered handed off merely because it appears in chat.

## 11. Handoff log

### 2026-08-19 -- cubic three-term zero theorem

- closed `(4,3,3)` as a universal zero row;
- completed the excess-`m` cubic arithmetic classification;
- replaced a false dimension-lower-bound shortcut with the exact `8/10/12`
  tensor-plane parity lemma;
- added primary and independent deterministic replays;
- moved the next frontier to `(5,3,3)`;
- recorded the inherited PR #83 CI failures without conflating them with the
  focused theorem receipt.

### 2026-08-18 -- multirow polarization envelopes

- established the dyadic nonzero staircase from one envelope through Glynn;
- inherited the sharp pair endpoint from PR #82;
- created this canonical handoff protocol.
