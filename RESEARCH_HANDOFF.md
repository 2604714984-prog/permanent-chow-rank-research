# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank
research stack.  It is updated whenever a synchronized GitHub result changes a
theorem, counterexample, route barrier, numerical boundary, equality
classification, or next executable mathematical task.

Last updated: **2026-08-19**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/cubic-block-threshold
active PR: #85
active theorem head: 6d45984ca9d907f32af7dfa0521a3b0ca5797e92
parent branch: research/cubic-three-term-zero
parent PR: #84
parent exact head: 29a8e37c3cf62c65a03d13ff4d692e1a42209a1f
stack ancestry: PR #82 -> PR #83 -> PR #84 -> current branch
```

Keep the stack narrow.  Do not introduce a manager, registry, dispatcher,
database, solver framework, or second control plane.

## 2. Latest research result

### Partition-Laplace Chow envelopes

For every partition

```text
lambda=(lambda_1,...,lambda_b), sum lambda_a=m,
```

partition the rows into blocks of those sizes and expand `perm_m` over all
ordered column blocks of matching sizes.  This gives

```text
q_lambda = m!/prod_a(lambda_a!)
```

summands.  Each summand lies in the output-degree-`m` derivative space of one
coordinate Chow term with

```text
n_lambda = sum_a lambda_a^2
```

factors.  Hence `q_lambda` terms give a nonzero permanent-relative literal
intersection from order `n_lambda` onward, with extension to larger order by
padding.

### Exact cubic literal block threshold

The partition `lambda=(2,1)` gives three terms at order five:

```text
perm_3=G_0+G_1+G_2,
G_j=x_(0j)*(x_(1a)*x_(2b)+x_(1b)*x_(2a)).
```

Each `G_j` is contained in the cubic derivative space of the product of its
five support variables.  Combining this construction with PRs #82 and #84 and
the one-term factor-span theorem gives the exact characteristic-zero function

```text
mu(n,3)=4 for n=3,4
mu(5,3)=3
mu(n,3)=2 for n=6,7,8
mu(n,3)=1 for n>=9.
```

Here `mu(n,3)` is the least number of degree-`n` Chow terms whose literal cubic
derivative-space sum meets `D_3(perm_n)` nontrivially.  This does not assert a
short Chow decomposition of `perm_n` for `n>3`.

## 3. Dependency chain

```text
n=3:    accepted ChowRank(perm_3)=4
n=4:    PR #84 universal three-term zero theorem
n=5:    PR #82 pair zero + current three-term construction
n=6..8: PR #82 pair construction + strict one-term zero theorem
n>=9:   one coordinate Chow envelope.
```

The general partition-Laplace construction is integral.  The exact minimum
classification is stated in characteristic zero because the lower theorems in
this chain are characteristic-zero results.

## 4. Files in the current result

```text
docs/general_partition_laplace_envelopes.md
docs/general_partition_laplace_envelopes_adversarial_review.md
docs/general_partition_laplace_envelopes_ledger_delta.md
docs/general_excess_m_cubic_boundary_clarification.md
scripts/general_partition_laplace_envelopes.py
scripts/general_partition_laplace_envelopes_independent.py
data/general_partition_laplace_envelopes.json
tests/test_general_partition_laplace_envelopes.py
RESEARCH_HANDOFF.md
```

Frozen theorem-facing core:

```text
20ec2b53ae598adbd78c36387fb8c00e1d8add9a1977d0f323eefdb4084b1c19
```

## 5. Focused validation receipt

```text
focused unit tests                         6/6 PASS
primary normal Python                         PASS
primary python -O                             PASS
independent normal Python                     PASS
independent python -O                         PASS
py_compile                                    PASS
frozen JSON == regenerated payload            PASS
English/non-ASCII proof scan                   PASS
```

Primary exact replay through `m=8`:

```text
partition shapes checked                         66
ordered column partitions checked           108,893
global permutation monomials checked         971,543
support-membership checks                    108,893
cubic threshold rows checked through n=64         62.
```

Independent implementation, importing none of the primary code:

```text
partition shapes checked                         66
permutation visits                           971,543
fibers checked                               108,893
cubic supports                                   3
support size per cubic envelope                   5.
```

The finite replays verify the combinatorial interfaces.  The theorem is proved
by the exact permutation-to-column-partition bijection and squarefree
derivative-space membership, not by extrapolation from the scan.

## 6. Hosted CI boundary inherited from PR #84

PR #84 workflow run `#751` completed after 891 tests.  All six PR #84 focused
tests passed, and the previously observed `n6_global_t15` timeout did not recur.
The full job still failed on one inherited compatibility regression:

```text
exact-product-shadow payload hash
observed: 18eb66f1b9460d2d793c69131cc4ebc0f1087c86b18f14e5638e71e6d629f567
expected: 3563dd0205177cd0471210287dc8b2377e1547e2410a419b611b2560b123f06a.
```

Do not describe the inherited full repository suite as green.  The current
focused result has a separate clean receipt; its own hosted run must be
recorded after publication.

## 7. Strict claim boundary

```text
partition-Laplace explicit family = PROVED
exact cubic literal block threshold = PROVED IN CHARACTERISTIC ZERO
new unrestricted Chow-rank lower bound = false
new exact Chow rank for n>=6 = false
border-rank improvement = NO
coupled/literal identification = NO
partition-family optimality for general m = OPEN
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING / INHERITED FAILURE PRESENT.
```

## 8. Superseded frontier

The previous handoff line

```text
q=3, m=3: n<=4 ZERO; n=5 OPEN; n>=6 NONZERO
```

is replaced by

```text
q=3, m=3: n<=4 ZERO; n>=5 NONZERO.
```

The cubic literal-block program is complete.

## 9. Next executable mathematical task

Move to the first unresolved quartic total-24 cell:

```text
(m,n,q)=(4,6,4).
```

The surrounding arithmetic boundary is

```text
(4,12,2) NONZERO by the sharp pair theorem
(4,8,3)  OPEN
(4,6,4)  OPEN
(4,4,6)  ZERO because ChowRank(perm_4)=8.
```

Begin with the exact component-essential-space relation ledger at `(4,6,4)`.
Use the existing private-polar and pair-supported-polar interfaces before any
coordinate enumeration.  Promote only a theorem, explicit counterexample, or
strict route barrier with an independent replay.

## 10. Mandatory synchronization rule

Every future synchronized result must update this file in the same pushed
commit or an immediately following publication-receipt commit.  Record:

```text
exact branch, PR, and head
mathematical statement and dependencies
strict claim boundary
proof, scripts, data, and tests
focused validation and hosted CI state
superseded statements
single next executable task.
```

A result is not handed off merely because it appears in chat.

## 11. Handoff log

### 2026-08-19 -- exact cubic literal block threshold

- introduced the general partition-Laplace Chow-envelope construction;
- constructed a three-term nonzero cubic block at order five;
- proved the exact function `mu(n,3)` for every `n>=3`;
- superseded the final open cubic three-term cell;
- selected quartic `(4,6,4)` as the next narrow frontier;
- preserved the inherited CI hash failure as a separate promotion condition.

### 2026-08-19 -- cubic three-term zero theorem

- closed `(4,3,3)` as universal zero;
- completed the excess-`m` cubic arithmetic classification;
- moved the remaining three-term gap to order five.

### 2026-08-18 -- multirow polarization envelopes

- established the dyadic nonzero staircase from one envelope through Glynn;
- inherited the sharp pair endpoint from PR #82;
- created the canonical handoff protocol.
