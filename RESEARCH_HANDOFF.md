# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank research stack. Every synchronized mathematical result must update this file.

Last updated: **2026-08-19**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-four-block-zero
active PR: #86
active theorem head: 965c669ed97d542e6316a2eda27964f5b40e12f9
parent branch: research/cubic-block-threshold
parent PR: #85
parent exact head: 34955786ea16bb52fc43313c19c3ce866f030cff
stack ancestry: PR #82 -> #83 -> #84 -> #85 -> #86
```

Keep the stack narrow. Do not introduce a manager, registry, dispatcher, database, broad solver framework, or second control plane.

## 2. Latest result

### Quartic four-block zero theorem

For arbitrary degree-six Chow terms over a characteristic-zero field,

```text
D_4(perm_6) intersect
(D_4(T_1)+D_4(T_2)+D_4(T_3)+D_4(T_4)) = 0.
```

Equivalently, the literal block minimum satisfies

```text
mu(6,4) >= 5.
```

The padded eight-term decomposition of `perm_4` gives `mu(6,4)<=8`; sizes five, six, and seven remain open. This is not an unrestricted Chow-rank or border-rank improvement.

## 3. Proof spine

Let `f=sum_i f_i` be a hypothetical witness. Its essential space has dimension at least 16; each component essential space has dimension at most six.

For every pair of labels, annihilating the complementary pair produces a pair-supported cubic polar space of dimension at least four inside a two-term degree-six Chow block.

A cubic pair-equality lemma uses the exact value

```text
F_(6,2)(4)=8
```

to show that every nonzero two-term cubic witness at order six has component dimensions `6,6`, intersection dimension `3`, and joint dimension `9`.

Applying this lemma to all six pairs forces every pair of quartic component spaces to span exactly nine dimensions. Repeating the pair-supported polar calculation then gives a cubic space of dimension at least seven inside a nine-dimensional span.

Every two-plane in `D_3(perm_6)` has order-two linear shadow at least 12, while a cubic family supported on a nine-plane has linear shadow at most nine. Contradiction.

## 4. Exact interfaces and validation

```text
F_(6,2)(4)                                      8
unique cubic pair-equality state          (6,6,3,9)
coordinate cubic pairs checked              79,800
minimum cubic two-plane linear shadow            12
initial pair-supported polar floor                4
refined pair-supported polar floor                7
focused unit tests                           5/5 PASS
primary normal Python                           PASS
independent normal Python                       PASS
py_compile                                      PASS
frozen JSON == regenerated payload              PASS
```

Frozen theorem-facing core:

```text
cb4ebea747a4ac2ac2b8141bab816395998cdb785d43b0fcd90579e54e949512
```

The characteristic-zero proof uses the repository's exact product-shadow and iterated-shadow theorems. The finite scans replay their small interfaces; they are not used as unsupported field-transfer arguments.

## 5. Current files

```text
docs/general_quartic_four_block_zero.md
docs/general_quartic_four_block_zero_adversarial_review.md
docs/general_quartic_four_block_zero_ledger_delta.md
scripts/general_quartic_four_block_zero.py
scripts/general_quartic_four_block_zero_independent.py
data/general_quartic_four_block_zero.json
tests/test_general_quartic_four_block_zero.py
RESEARCH_HANDOFF.md
```

## 6. Current arithmetic boundary

At total `q*n=24` and quartic output degree:

```text
(n,m,q)=(12,4,2) NONZERO -- sharp pair construction
(n,m,q)=(8,4,3)  OPEN
(n,m,q)=(6,4,4)  ZERO    -- PR #86
(n,m,q)=(4,4,6)  ZERO    -- ChowRank(perm_4)=8
```

The previous handoff line `(4,6,4) OPEN` is superseded.

## 7. Earlier active result

PR #85 proved the partition-Laplace envelope family and the exact cubic literal-block function

```text
mu(n,3)=4 for n=3,4
mu(5,3)=3
mu(n,3)=2 for n=6,7,8
mu(n,3)=1 for n>=9.
```

That cubic classification remains inherited and unchanged.

## 8. Hosted CI state

Parent PR #85 run `#753` remains `IN PROGRESS` at this handoff update. Parent PR #84 run `#751` completed 891 tests with all six PR #84 tests passing, but retained one inherited exact-product-shadow compatibility-hash failure. Do not describe the full repository suite as green until the current hosted run finishes and the inherited hash regression is resolved or explicitly reclassified.

PR #86 hosted CI is triggered from the publication-receipt head and must be refreshed in the next synchronization.

## 9. Strict claim boundary

```text
quartic (6,4,4) = ZERO
mu(6,4) lower bound = 5
mu(6,4) exact value = OPEN
new unrestricted Chow-rank bound = false
new exact Chow rank for perm_6 = false
border-rank improvement = NO
coupled/literal identification = NO
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING
```

## 10. Next executable task

Study the remaining quartic total-24 cell

```text
(n,m,q)=(8,4,3).
```

Begin with pair-supported cubic polar spaces: annihilating one eight-dimensional component forces an at-least-eight-dimensional cubic family inside a two-term degree-eight Chow block. Compute the exact order-two shadow threshold at dimension eight and classify any equality case before attempting coordinate enumeration. A second valid route is to continue `mu(6,4)` at block size five, but do not run both routes as parallel frameworks.

## 11. Mandatory synchronization rule

Every future synchronized result must record the exact branch, PR and head; theorem or route barrier; proof dependencies; scripts, data and tests; focused and hosted validation; superseded statements; and one next executable task. A result is not handed off merely because it appears in chat.

## 12. Handoff log

### 2026-08-19 -- quartic four-block zero

- closed `(6,4,4)` as universal zero;
- proved the cubic two-term equality state `(6,6,3,9)` needed by the argument;
- introduced the pair-supported polar bootstrap;
- obtained `5<=mu(6,4)<=8`;
- moved the total-24 frontier to `(8,4,3)`.

### 2026-08-19 -- exact cubic literal-block threshold

- introduced partition-Laplace envelopes;
- proved the exact function `mu(n,3)`.

### 2026-08-19 -- cubic three-term zero

- closed `(4,3,3)` as universal zero.

### 2026-08-18 -- multirow polarization envelopes

- established the dyadic nonzero staircase and the handoff protocol.
