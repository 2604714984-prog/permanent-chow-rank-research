# Research handoff

## Purpose

This file is the canonical operational handoff for the active mathematical
research stack. It records the exact research head, the latest proved or
replayed result, its claim boundary, verification state, unresolved frontier,
and the next executable task.

`RESEARCH_LEDGER.md` remains the canonical high-level mathematical results
ledger. This handoff is narrower: it is the current-state document needed for
another researcher or model to resume work without reconstructing the entire
pull-request history.

## Mandatory update rule

Every GitHub synchronization that adds, changes, retracts, supersedes, or
reclassifies a mathematical result must update this file in the same commit as
the proof, scripts, frozen data, tests, and `RESEARCH_LEDGER.md` delta.

Each update must record:

1. repository, branch, pull request, base, and exact head SHA;
2. the new mathematical statement and its dependency chain;
3. proof status and the precise claim boundary;
4. deterministic replay, independent replay, tests, and hosted CI status;
5. files added or changed;
6. unresolved mathematical interfaces and rejected shortcuts;
7. the single next executable research task;
8. a dated changelog entry.

Do not promote a conjecture, numerical diagnostic, modular experiment, or
finite scan beyond its justified characteristic-zero boundary.

## Current handoff snapshot

Last updated: **2026-08-19**

```text
repository = 2604714984-prog/permanent-chow-rank-research
active PR = #83
active branch = research/multirow-polarization-envelopes
base branch = research/sharp-pair-threshold
base SHA = 2f054482b7cca108e890a01595a10f2cb4e387dd
research head before this handoff commit = 6ed4065e20fcc79ca90f1f5d606a58b3cf269d62
PR state = OPEN / DRAFT / MERGEABLE
```

The SHA above identifies the mathematical head reviewed when this handoff was
created. The commit adding or updating this file becomes the new branch head
and must be recorded in the next handoff update.

## Latest research result

PR #83 generalizes the sharp two-term polarization construction from PR #82
to an arbitrary number of selected permanent rows.

For every characteristic-zero field, every `1 <= t <= m`, and every

```text
n >= m*(m-t+1),
```

there are `2^(t-1)` degree-`n` Chow terms `T_epsilon` such that

```text
0 != perm_m
in D_m(perm_n) intersect sum_epsilon D_m(T_epsilon).
```

The construction uses a Walsh selector on `t` rows, row-Laplace expansion, and
one Chow envelope for each sign vector. It gives the explicit dyadic nonzero
staircase

```text
term count       first constructed nonzero degree
1                m^2
2                m*(m-1)
4                m*(m-2)
8                m*(m-3)
...
2^(m-1)          m.
```

This interpolates between the one-envelope coordinate construction, the sharp
pair threshold from PR #82, and the `2^(m-1)`-term Glynn construction.

## Claim boundary

```text
new explicit general-n nonzero family = true
q=1 endpoint = inherited sharp
q=2 endpoint = inherited sharp
intermediate q>=3 term minimality = OPEN
intermediate q>=3 degree sharpness = OPEN
new Chow-rank lower bound = false
new exact rank for n>=6 = false
border-rank improvement = NO
coupled/literal identification = NO
general Glynn optimality = OPEN
literature novelty = NOT ESTABLISHED
```

The theorem is a literal derivative-space intersection statement. For `n>m`,
it is not a Chow decomposition of `perm_n`.

## Verification snapshot

The PR records:

```text
primary exact replay = PASS
primary python -O = PASS
independent bit-mask Walsh replay = PASS
independent python -O = PASS
focused unit tests = 5/5 PASS
compileall = PASS
English-only proof files = PASS
frozen JSON equals regenerated payload = PASS
```

Hosted workflow at the reviewed head:

```text
workflow = exact-bound-tests
run = 32159368742
run number = 748
status at handoff creation = IN PROGRESS
```

Hosted CI completion remains a promotion condition and must be refreshed in the
next synchronization.

## Current PR files

```text
data/general_multirow_polarization_envelopes.json
docs/general_multirow_polarization_envelopes.md
docs/general_multirow_polarization_envelopes_adversarial_review.md
docs/general_multirow_polarization_envelopes_ledger_delta.md
scripts/general_multirow_polarization_envelopes.py
scripts/general_multirow_polarization_envelopes_independent.py
tests/test_general_multirow_polarization_envelopes.py
RESEARCH_HANDOFF.md
```

## Active mathematical frontier

The zero side and nonzero side are now separated as follows:

- universal two-term zero threshold is sharp by PR #82;
- the dyadic family supplies explicit nonzero blocks for powers-of-two term
  counts;
- sharp thresholds for intermediate term counts are not known;
- the first priority is the three- and four-envelope region, where a genuinely
  non-dyadic construction or a stronger universal zero theorem may close part
  of the gap;
- the cubic `(n,m,q)=(4,3,3)` interface remains a small explicit unresolved
  test case and is a useful falsification target.

## Next executable task

Build an exact three- and four-envelope boundary table before attempting a
large general theorem:

1. combine every currently proved universal zero criterion into one exact
   integer lower frontier for `q=3,4`;
2. combine PR #83 and all simple envelope mergers, specializations, and padding
   operations into one explicit nonzero upper frontier;
3. enumerate the remaining gap cells for small `m` exactly;
4. test whether the cubic `(4,3,3)` cell is zero or nonzero;
5. promote only a proved theorem, explicit counterexample, or strict route
   barrier, with independent replay and a ledger/handoff update.

Do not begin with a broad solver framework or another scalar asymptotic route.
The next work should be a narrow mathematical boundary analysis.

## Changelog

### 2026-08-19 — handoff file introduced

- Created the canonical research handoff on PR #83's active branch.
- Recorded the exact pre-handoff mathematical head and PR ancestry.
- Recorded the multirow Walsh-envelope theorem, its verification, and its
  strict claim boundary.
- Made handoff updates mandatory for every future research synchronization.
- Selected the three-/four-envelope boundary as the next executable research
  task.
