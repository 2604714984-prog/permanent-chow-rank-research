# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank
research stack. Every synchronized result must update this file.

Last updated: **2026-08-20**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-term-frontier
active PR: #89
PR URL: https://github.com/2604714984-prog/permanent-chow-rank-research/pull/89
parent branch: research/quartic-natural-span-barriers
parent PR: #88
parent exact head: 729669c4ab2fd27c1bbf13d6ea519363a1e643f5
publication theorem head: 38e4af25897e29df605333152c7fb6c1e47af87b
publication receipt head: THIS HANDOFF UPDATE; exact SHA recorded by the following pointer commit
stack ancestry: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89
```

Keep the stack narrow. Do not introduce a manager, registry, dispatcher,
database, broad solver framework, or second control plane.

## 2. Current proved boundary

For arbitrary degree-six Chow terms over a characteristic-zero field,

\[
\boxed{
\mathcal D_4(\operatorname{perm}_6)
\cap
\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
}
\]

Therefore

\[
\boxed{6\le\mu(6,4)\le8.}
\]

Six and seven arbitrary blocks remain open. Eight blocks are nonzero by the
padded order-four decomposition.

## 3. Results synchronized in PR #89

### 3.1 Five-block zero theorem

The pair-trigger branch propagates the sharp cubic equality state to all
component pairs and contradicts the twelve-versus-nine second-shadow bound.
The fully coupled branch forces a twelve-dimensional square-zero covector
space, contradicting the order-four star cap four.

Theorem core:

```text
72a73cc0012e7113f1a483150b61c8e7444310c38542b1d5bca40c9182c15171
```

### 3.2 Exact natural-family barriers

```text
coordinate degree-six threshold:            12
one-factor-per-column quartic threshold:      8
one-factor-per-row quartic threshold:         8
normalized sign threshold at (6,4):           8
```

Theorem cores:

```text
coordinate:
4b85646c9b1c96c18b5010206ce7897edba0b330e762f554b7314709ae53b1f9

column-separated:
45a855429fe780db052731a7201713640a0adbe27f656294195399c49fb78623

sign:
af5fbd6fa060649a1a58220f258077d46797013491d89e5623ce2bd7492e0316
```

### 3.3 Partition-Laplace essential stratification

For coefficient support `S`,

\[
\dim\operatorname{Ess}\left(\sum_{\mathbf C\in S}a_{\mathbf C}G_{\mathbf C}\right)
=\sum_a\lambda_a\left|\bigcup_{\mathbf C\in S}C_a\right|.
\]

The natural `(2,2)` six-generator space has minimum essential dimension eight
and zero intersection with every single degree-six Chow derivative block.

Theorem core:

```text
1bcbe6b3d3594f649171a21d8837b2a811596858f60dd2b41c52268484525e6c
```

### 3.4 Common-source slices and six-element circuit

All fixed four-column slices of one component are images of the same source
vector in the 15-dimensional squarefree factor-label space. An isolated slice
is insufficient: one block can already have a fixed slice equal to `perm_4`,
with 232 repeated-column defects elsewhere.

Every hypothetical six-block witness yields six nonzero quotient vectors with
one unique full-support relation; every proper subcollection is independent.

Theorem core:

```text
d82e88706313fb20bd8cf0e51d7ab7a7fadac00d9805d72d2fd1b2ccd1d6d85c
```

## 4. Canonical proof files

```text
docs/general_quartic_five_to_six_term_frontier.md
docs/general_quartic_five_to_six_term_frontier_adversarial_review.md
docs/general_quartic_five_to_six_term_frontier_ledger_delta.md
RESEARCH_HANDOFF.md
```

## 5. Validation and hosted CI

The retained local packets report exact primary and independent replays,
normal and `python -O` equality, frozen JSON comparison, focused unit tests,
`py_compile`, and SHA-256 manifests.

The theorem head triggered:

```text
workflow: exact-bound-tests
run number: 760
run id: 32346595999
status at publication receipt: in_progress
conclusion: pending
URL: https://github.com/2604714984-prog/permanent-chow-rank-research/actions/runs/32346595999
```

Do not describe the repository-wide suite as green before the run finishes.

## 6. Exact next task

Retain the same source vector for each component and impose the unique
six-element quotient circuit simultaneously on the repeated-column layers

```text
(2,1,1), (2,2), (3,1), and (4).
```

The target is one of:

1. a forced proper subcircuit, contradicting five-block zero;
2. a common kernel forcing a component into an excluded separated family; or
3. an exact six-block witness.

Do not replace this with a broad numerical optimizer.

## 7. Strict claim boundary

```text
five-block literal sum = ZERO
six-block literal sum = OPEN
seven-block literal sum = OPEN
eight-block literal sum = NONZERO
mu(6,4) exact value = OPEN in [6,8]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```

## 8. Mandatory synchronization rule

Every subsequent mathematical result must be committed to GitHub and this file
must be updated in the theorem commit or in an immediately following receipt
commit. Record the exact branch, PR, theorem head, receipt head, workflow run,
and any inherited compatibility failure.

## 9. Handoff log

### 2026-08-20 -- PR #89 consolidated five-to-six-term frontier

- synchronized the five-block zero theorem;
- synchronized exact coordinate, separated-frame, and sign-family barriers;
- synchronized the partition-Laplace essential stratification theorem;
- synchronized the common-source mixed-slice interface;
- recorded the universal full-support six-element quotient circuit;
- retained `6<=mu(6,4)<=8` and selected repeated-column circuit compatibility
  as the next task;
- created Draft PR #89 and triggered Actions run #760.
