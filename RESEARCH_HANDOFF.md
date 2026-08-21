# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank
research stack. Every synchronized result must update this file.

Last updated: **2026-08-21**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
active PR: #92
PR URL: https://github.com/2604714984-prog/permanent-chow-rank-research/pull/92
parent branch: research/quartic-six-term-frontier
parent PR: #89
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
two-supported theorem head: b6facbc6ad5cfb5ce10589ac4097a30b1184feab
positive-singleton theorem head: THIS HANDOFF UPDATE
publication receipt head: PENDING
stack tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
```

Keep the stack narrow. Do not introduce a manager, registry, dispatcher,
database, broad solver framework, or second control plane.

## 2. Current proved numerical boundary

For arbitrary degree-six Chow terms over a characteristic-zero field,

\[
\mathcal D_4(\operatorname{perm}_6)
\cap
\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
\]

Therefore

\[
\boxed{6\le\mu(6,4)\le8}.
\]

Six and seven arbitrary blocks remain open. Eight blocks are nonzero by the
padded order-four decomposition. The unrestricted ordinary boundary remains

\[
28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

## 3. Inherited PR #89 frontier

PR #89 synchronizes:

- the five-block zero theorem;
- exact coordinate, row-separated, column-separated, and sign-family barriers;
- partition-Laplace essential stratification;
- the 15-dimensional common-source mixed-slice interface; and
- the universal full-support six-element quotient circuit.

The main frozen cores are:

```text
five-block zero:
72a73cc0012e7113f1a483150b61c8e7444310c38542b1d5bca40c9182c15171

partition-Laplace essential stratification:
1bcbe6b3d3594f649171a21d8837b2a811596858f60dd2b41c52268484525e6c

common-source and quotient circuit:
d82e88706313fb20bd8cf0e51d7ab7a7fadac00d9805d72d2fd1b2ccd1d6d85c
```

## 4. Results synchronized in PR #92

### 4.1 Two-supported coordinate regular two-jets

Assume all six nonzero coordinate leading matching projections are supported
on exactly two perfect matchings and form a support-minimal rank-five circuit.
The support multigraph is a six-cycle, theta, tight handcuff, or loose
handcuff. Retaining every continuous gain stratum, the exact matching-support
maxima of the regular first- and second-order common-source lift are

```text
six-cycle          6
theta               5
loose handcuff      6
tight handcuff      8
perm_4             24
```

Frozen theorem core:

```text
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9
```

### 4.2 Positive-singleton support classification

A support-minimal rank-five coordinate six-circuit with nonzero leading
matching projection on every component has at most two singleton components.
The positive-singleton support families are exactly

```text
one singleton:  square lollipop or double-edge tail
two singletons: endpoint-marked P5
three or more:  impossible
```

Their row-column orbit counts are `5`, `29`, and `18`.

For each singleton, the two unused degree-six factors are an unordered
multiset from all sixteen coordinate cells. Repetition and reuse of a leading
matching cell are included. Of the 136 multisets, six create a second perfect
matching and the remaining 130 are true singleton frames.

### 4.3 Universal positive-singleton second-order envelope

For a coordinate frame `E` and leading matching support `S`, every matching
monomial in a regular second-order common-source lift lies in

\[
\mathcal E(E,S)=
\{M:|M\cap E|\ge3\}
\cup
\{M:\exists M_0\in S,\ |M\cap M_0|\ge2\}.
\]

This is a termwise envelope, so first-order cancellation can only reduce its
support. Exhaustion of all embeddings and all repeated-factor singleton
frames gives

```text
square lollipop       650 decorated configurations, maximum 22
double-edge tail     3770 decorated configurations, maximum 22
endpoint-marked P5 304200 decorated configurations, maximum 23
perm_4 matching support                                    24
```

Thus every regular positive-singleton coordinate two-jet is incompatible with
a nonzero diagonal-torus transform of `perm_4`.

Frozen theorem core:

```text
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### 4.4 Combined coordinate boundary

Combining Sections 4.1 and 4.3 closes every regular coordinate six-circuit
two-jet for which all six leading matching projections are nonzero. The next
coordinate boundary is the zero-leading matching-projection case. This does
not change `6<=mu(6,4)<=8`.

## 5. Canonical proof files

```text
docs/general_quartic_five_to_six_term_frontier.md
docs/general_quartic_two_supported_coordinate_two_jet_barrier.md
docs/general_quartic_two_supported_coordinate_two_jet_barrier_adversarial_review.md
docs/general_quartic_singleton_coordinate_circuit_reduction.md
docs/general_quartic_singleton_coordinate_circuit_reduction_adversarial_review.md
docs/general_quartic_singleton_coordinate_circuit_reduction_ledger_delta.md
scripts/general_quartic_singleton_coordinate_circuit_reduction.py
scripts/general_quartic_singleton_coordinate_circuit_reduction_independent.py
data/general_quartic_singleton_coordinate_circuit_reduction.json
tests/test_general_quartic_singleton_coordinate_circuit_reduction.py
RESEARCH_HANDOFF.md
RESEARCH_LEDGER.md
```

## 6. Validation and hosted CI

The current packet reports:

```text
primary normal Python                         PASS
primary python -O                             PASS
independent replay                            PASS
independent replay under python -O            PASS
frozen JSON == regenerated payload            PASS
focused singleton tests                       5/5 PASS
py_compile                                    PASS
diff check                                    PASS
English-only proof-tree scan                  PASS
```

Parent run #762 completed 912 tests with one inherited stale
exact-product-shadow expectation. The first PR #92 commit repairs that
expectation from `3563...` to the checked-in payload hash `18eb...` without
changing the underlying theorem payload.

Hosted CI for the current positive-singleton theorem head is pending. Do not
describe the repository-wide suite as green before the current run finishes.

## 7. Exact next task

Classify coordinate components whose leading matching projection is zero.
Retain the same six-factor common-source data and determine whether such a
component can enter the unique six-element quotient circuit at the first
nonzero valuation grade.

The target is one of:

1. a forced proper subcircuit, contradicting five-block zero;
2. a reduction to a separated or already excluded coordinate family;
3. a finite exact survivor that justifies a third-order calculation; or
4. an exact six-block witness.

Do not open a broad nonlinear solver or general third-order framework before
this zero-leading boundary is resolved.

## 8. Strict claim boundary

```text
five-block literal sum = ZERO
six-block literal sum = OPEN
seven-block literal sum = OPEN
eight-block literal sum = NONZERO
mu(6,4) exact value = OPEN in [6,8]
two-supported coordinate regular two-jets = CLOSED
positive-singleton coordinate regular two-jets = CLOSED
all-positive coordinate regular two-jets = CLOSED
zero-leading matching-projection components = OPEN
noncoordinate and higher-order lifts = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```

## 9. Mandatory synchronization rule

Every subsequent mathematical result must be committed to GitHub and this file
must be updated in the theorem commit or in an immediately following receipt
commit. Record the exact branch, PR, theorem head, receipt head, workflow run,
and any inherited compatibility failure.
