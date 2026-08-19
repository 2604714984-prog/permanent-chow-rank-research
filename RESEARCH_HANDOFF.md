# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank research stack. Every synchronized result must update this file.

Last updated: **2026-08-19**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-three-block-zero
active PR: #87
active theorem head: 0094aaaf97bd85d8803822f28bfdfa07ee0f3f39
parent branch: research/quartic-four-block-zero
parent PR: #86
parent exact head: 46bc5f34b2a026cbf9dda62d88e6b5322792fda4
stack ancestry: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87
```

Keep the stack narrow. Do not introduce a manager, registry, dispatcher, database, broad solver framework, or second control plane.

## 2. Latest result

### Quartic three-block zero theorem

For arbitrary degree-eight Chow terms over a characteristic-zero field,

```text
D_4(perm_8) intersect
(D_4(T_1)+D_4(T_2)+D_4(T_3)) = 0.
```

The inherited four-envelope construction is nonzero at order eight, so

```text
mu(8,4)=4.
```

This is an exact literal block minimum, not an exact unrestricted Chow rank.

## 3. Proof spine

A hypothetical three-term quartic witness has essential dimension at least 16 and component essential dimensions at most eight.

Single-component private cubic polars vanish because every nonzero cubic permanent derivative needs at least nine essential variables. Conciseness therefore forces every pair of component spaces to equal the sixteen-dimensional total essential space. Thus all three components are eight-dimensional and pairwise disjoint.

Annihilating the remaining component produces an eight-dimensional cubic polar space inside a two-term degree-eight Chow block supported on a disjoint pair.

For a disjoint two-term cubic witness, private quadratic spaces have the same dimensions `b` as their component essential spaces. The exact shadow table is

```text
b:          1 2 3 4 5 6 7 8
F_(8,2)(b): 4 6 6 8 8 8 9 9.
```

Every value exceeds `b`, while the quadratic shadow is contained in the `b`-dimensional component space. Contradiction.

## 4. Parent result retained

PR #86 proved

```text
D_4(perm_6) intersect sum_(i=1)^4 D_4(T_i) = 0,
```

hence

```text
5 <= mu(6,4) <= 8.
```

Its key cubic pair-equality state is `(6,6,intersection 3,joint 9)`.

## 5. Quartic total-24 boundary

The arithmetic boundary `q*n=24` is now completely classified:

```text
(n,m,q)=(12,4,2) NONZERO -- sharp pair construction
(n,m,q)=(8,4,3)  ZERO    -- PR #87
(n,m,q)=(6,4,4)  ZERO    -- PR #86
(n,m,q)=(4,4,6)  ZERO    -- ChowRank(perm_4)=8
```

The previous handoff label `(8,4,3) OPEN` is superseded.

## 6. Current files and validation

```text
docs/general_quartic_three_block_zero.md
docs/general_quartic_three_block_zero_adversarial_review.md
docs/general_quartic_three_block_zero_ledger_delta.md
scripts/general_quartic_three_block_zero.py
scripts/general_quartic_three_block_zero_independent.py
data/general_quartic_three_block_zero.json
tests/test_general_quartic_three_block_zero.py
RESEARCH_HANDOFF.md
```

```text
focused unit tests                         5/5 PASS
primary normal Python                         PASS
independent normal Python                     PASS
py_compile                                    PASS
frozen JSON == regenerated payload            PASS
exact shadow DP states                         112
```

Frozen theorem-facing core:

```text
f42f161b773843d253dff703c455191891dcf38a0adc4ac396b6ffcec46a1655
```

The finite programs replay exact integer interfaces. The characteristic-zero proof relies on the repository's proved torus-specialization and product-shadow theorems, not on unsupported finite-field transfer.

## 7. Earlier inherited result

PR #85 proved the partition-Laplace envelope family and

```text
mu(n,3)=4 for n=3,4
mu(5,3)=3
mu(n,3)=2 for n=6,7,8
mu(n,3)=1 for n>=9.
```

## 8. Hosted CI state

The new PR #86 and PR #87 hosted workflows are pending at this handoff update. PR #85 run `#753` was still in progress when last checked. PR #84 run `#751` completed 891 tests with all focused PR #84 tests passing but retained one inherited exact-product-shadow compatibility-hash failure. Do not describe the full repository suite as green until current runs complete and the inherited regression is resolved or reclassified.

## 9. Strict claim boundary

```text
quartic (8,4,3) = ZERO
mu(8,4) = 4
quartic total-24 arithmetic boundary = CLASSIFIED
mu(6,4) exact value = OPEN in [5,8]
new unrestricted Chow-rank bound = false
new exact Chow rank for perm_8 = false
border-rank improvement = NO
coupled/literal identification = NO
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING
```

## 10. Next executable task

Determine the exact value of

```text
mu(6,4) in {5,6,7,8}.
```

Start with five-term component essential spaces. Single private cubics still vanish. The first useful descendants are triple-supported cubic polars obtained by annihilating a complementary pair. Combine the exact cubic literal minimum `mu(6,3)=2`, the PR #86 pair-equality state, and exact quadratic shadow tables before any coordinate search. Promote only an explicit five-, six-, or seven-term construction, a universal zero theorem, or a strict route barrier.

## 11. Mandatory synchronization rule

Every future synchronized result must record exact branch, PR and head; theorem or route barrier; dependencies; scripts, data and tests; focused and hosted validation; superseded statements; and one next executable task. A result is not handed off merely because it appears in chat.

## 12. Handoff log

### 2026-08-19 -- quartic three-block zero

- closed `(8,4,3)` as universal zero;
- proved `mu(8,4)=4`;
- completed the quartic `q*n=24` arithmetic classification;
- moved the active frontier to exact `mu(6,4)`.

### 2026-08-19 -- quartic four-block zero

- closed `(6,4,4)`;
- obtained `5<=mu(6,4)<=8`.

### 2026-08-19 -- exact cubic literal threshold

- proved the exact function `mu(n,3)`.

### 2026-08-18 -- multirow polarization envelopes

- established the dyadic staircase and canonical handoff protocol.
