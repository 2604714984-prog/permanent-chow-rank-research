# `perm_7` post-v3 grand execution package v4

## Status and scope

`ACTIVE THEOREM-EXECUTION PACKAGE — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Input snapshot: the first parent of the commit adding this document  
Active research PR: `#31`  
Active branch: `agent/general-column-sign-rank`

This package starts after completion of the v3 task package. It does not repeat
v3 implementation work. Its first gate freezes the terminal mathematical
outputs of v3, then it proceeds without another replanning cycle through:

1. any remaining `N=49` theorem closure and lower-50 promotion;
2. complete near-equality analysis for a hypothetical minimal 50-term identity;
3. an ordinary characteristic-zero lower-51 theorem attempt;
4. a stretch lower-52 program if the same invariant supplies enough slack.

The currently promoted numerical interval must be read from the repository
status at the input snapshot. This document does not itself change that
interval. Unless separately proved, every target below concerns ordinary Chow
rank over an algebraically closed field of characteristic zero only.

The preferred next numerical target is

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge 51,
\]

but it is activated only after lower 50 has a frozen proof and audit. The
stretch target is lower 52; exact rank 64 is not an execution target for this
package.

---

# 0. Operating rules

## 0.1 Parent-commit freeze

The first parent of this document is the immutable research input. Every
completed-v3 claim cited below must be tied to a path and exact commit. A moving
branch, PR prose, or latest generated JSON is not a proof boundary.

## 0.2 No repeated work

A v3 task with a terminal theorem, counterexample, correction, or exact
survivor is consumed as input. It is not rerun merely to produce a differently
named artifact.

## 0.3 Corrections dominate plans

If a v3 result corrected an earlier Hilbert-growth, relation-space,
semicontinuity, weight, reducedness, or closure assertion, the corrected
statement is the only admissible input. Historical plans remain history.

## 0.4 Exact-survivor priority

An exact survivor satisfying all currently encoded conditions suspends broad
exclusion searches. The next task is to identify the first condition that
separates the survivor from an actual permanent identity.

## 0.5 Minimal infrastructure

This package authorizes proof notes, focused exact scripts, compact evidence,
and tests. It does not authorize a new scheduler, database, experiment manager,
registry, or generalized computer-algebra platform.

---

# 1. Workstream F — freeze the completed-v3 frontier

## Goal

Convert the completed task package into a one-page executable theorem frontier.
This is consolidation, not a new research phase.

### F.1 — terminal-task ledger

For every v3 task, record exactly one status:

```text
PROVED
EXCLUDED
EXACT-SURVIVOR
COUNTEREXAMPLE-TO-ROUTE
CORRECTED
SUPERSEDED
NO-THEOREM
```

Each row must contain the exact file, commit, scope, and downstream consequence.

### F.2 — notation and object audit

Verify that every result distinguishes

\[
C_d=\operatorname{im}E_d,\qquad
R_d=\ker(E_d^T),\qquad
I_d=\ker E_d,\qquad
W_d=I_d^\perp.
\]

Any statement using multiplication of `R_d`, Macaulay growth of `R_d`, or
weighted coupling on `I_d` is rejected or corrected before use.

### F.3 — correction digest

Collect every post-v3 correction, including strict-growth, reduced-point,
nonzero-weight, target-containment, and boundary corrections. For each one,
state which earlier task or claimed reduction it changes.

### F.4 — survivor inventory

Freeze all exact common-graph, mixed Packet-B, Packet-A, Hilbert-function,
weight, or relation-module survivors. Recompute their load-bearing ranks with
one independent implementation.

### F.5 — theorem dependency graph

Produce the shortest dependency graph from established lower 49 to the current
frontier. Separate:

- pure structural theorems;
- permanent-specific theorems;
- finite exact certificates;
- diagnostics;
- route barriers.

### F.6 — lower-50 gate classification

Return exactly one status:

```text
L50-PROMOTED
L50-PROMOTABLE-PENDING-AUDIT
L50-ONE-EXPLICIT-GAP
L50-EXACT-ENDPOINT-SURVIVOR
L50-MULTIPLE-OPEN-COMPONENTS
```

### F.7 — no-ambiguity handoff

Write one paragraph naming the unique first unresolved theorem statement. If
there is more than one independent unresolved statement, order them by
expected theorem value rather than implementation convenience.

### F.8 — repository status correction

Update any README, status note, task plan, or PR comment that still presents a
superseded frontier as current. Historical documents are not rewritten; they
receive an explicit superseded marker when necessary.

## Gate F

No new search begins until F.1–F.8 are complete. This gate should be short; it
must not grow into a project-management layer.

---

# 2. Workstream P49 — close and promote lower 50 if still necessary

## Entry condition

Run only when Gate F does not return `L50-PROMOTED`.

## Goal

Exclude every actual 49-term identity, or freeze an exact endpoint survivor
showing why the present invariant is insufficient.

### P49.1 — residual common-graph theorem extraction

If common-graph Packet B remains open, replace stratum-by-stratum experiment
prose with the strongest theorem supported by completed v3 outputs. The theorem
must quantify over arbitrary reduced point sets and arbitrary invertible term
weights in its stated scope.

### P49.2 — strict Hilbert-growth correction integration

Incorporate the final corrected Hilbert-function consequences. Distinguish
numerical rank profiles, geometrically realizable profiles, reduced-point
profiles, and profiles compatible with degree-six permanent containment.

### P49.3 — weighted coupling as a torus intersection

Use the exact equivalence

\[
D^{-1}R_4\subseteq C_3
\quad\Longleftrightarrow\quad
w\in(R_3\star R_4)^\perp,
\qquad w_i=d_i^{-1},
\]

only where its hypotheses have been proved. Saturate by
\(\prod_i w_i\) or cover the nonzero torus by exact charts.

### P49.4 — permanent target integration

Enforce degree-six target containment simultaneously with weighted coupling.
Do not optimize or classify these equations independently.

### P49.5 — common-graph decisive outcome

Return exactly one:

```text
COMMON-GRAPH-B-CLOSED
COMMON-GRAPH-B-SURVIVOR
```

### P49.6 — arbitrary mixed Packet-B intrinsic model

Write the 42 graph complements term-by-term, retaining their individual graph
maps, weights, relation transport, and permanent target contributions.

### P49.7 — common-code reduction theorem

Prove that an arbitrary equality packet induces one common code, finitely many
code types, or a finite theorem-defined exceptional list. Do not assume equal
graph maps.

### P49.8 — exceptional Packet-B branch inventory

For each exceptional branch, state the exact invariant that produced it and
map it to an existing certificate or a new focused theorem task.

### P49.9 — reuse completed exclusion certificates

Apply the existing overlap, Laurent-boundary, rank-one update, signed,
monomial, shear, and graph certificates only to branches that satisfy their
formal hypotheses.

### P49.10 — close uncovered Packet-B branches

For each uncovered branch, use the smallest permanent-specific cross-degree
obstruction. New broad family searches are forbidden.

### P49.11 — Packet-B decisive outcome

Return exactly one:

```text
PACKET-B-CLOSED
PACKET-B-SURVIVOR
```

### P49.12 — Packet-A completed module consolidation

Freeze the actual term-labelled degree `2/5/6` module produced by v3. Record
all maps, dimensions, radicals, coefficients, and target blocks.

### P49.13 — Packet-A adversarial controls

Recheck every proposed Packet-A lemma against the 49-term Glynn truncation and
non-tensor-split Sylvester-equality controls.

### P49.14 — Packet-A minimal obstruction

Prove one positive permanent-specific defect in the smallest surviving torus
block, or freeze an exact survivor satisfying the complete `2/5/6` interface.

### P49.15 — conditional `3/4` escalation

Open the larger middle-degree system only for a survivor that passes every
`2/5/6` condition.

### P49.16 — Packet-A decisive outcome

Return exactly one:

```text
PACKET-A-CLOSED
PACKET-A-SURVIVOR
```

### P49.17 — lower-50 theorem assembly

When both packets are closed, write the shortest proof from the slope-ten
endpoint to impossibility of 49 terms. Remove non-load-bearing experiments.

### P49.18 — lower-50 independent audit

Audit arbitrary quotient coverage, all equality cases, term weights,
reducedness, closure directions, characteristic-zero lifts, and the final
ordinary-rank scope.

### P49.19 — lower-50 promotion

Promote only at one exact HEAD with focused tests and repository CI passing.

### P49.20 — endpoint-survivor route change

If either packet has a genuine exact survivor, stop theorem assembly and make
the survivor's first missing identity equation the first task of the next
wave.

---

# 3. Workstream S50 — exact slack ledger for a minimal 50-term identity

## Entry condition

Lower 50 is frozen and audited.

## Goal

Replace the broad question “can 50 terms exist?” by a finite list of
near-equality packets with total slack exactly 35.

For a hypothetical minimal identity

\[
\operatorname{perm}_7=\sum_{i=1}^{50}T_i,
\]

retain the endpoint notation `H_3,H_4,Delta`. The established inequalities
have the form

\[
H_3+H_4+\Delta\ge2940,
\]

\[
H_3+H_4+\Delta\le35N+1225.
\]

At `N=50`, the total available departure from the 49-term equality endpoint is
exactly

\[
35N+1225-2940=35.
\]

### S50.1 — prove an exact slack identity

Decompose the number 35 into nonnegative, geometrically meaningful terms:

- local quotient-symbol excess above `10d_i`;
- filtration loss;
- output-summation/Sylvester loss;
- derivative-space defect;
- target or relation overlap when applicable.

Avoid an inequality-only ledger if exact kernels and cokernels give an
identity.

### S50.2 — define order-independent slack invariants

The factor filtration depends on term order. Define the quantities that are
intrinsic, and state how an arbitrary order redistributes but cannot reduce
total slack.

### S50.3 — local excess table for rank-seven terms

For every quotient rank `d=0,...,7`, freeze the exact or best proved minimum of

\[
\operatorname{rank}\beta_+
+
\operatorname{rank}\beta_-
+
\delta-10d.
\]

Include arbitrary quotients, not only coordinate initials.

### S50.4 — local excess table for rank-six normal forms

For every normal form `s=1,...,6` and every quotient rank, compute the exact
near-equality excess or a proved lower bound sharp enough for the 35-budget
classification.

### S50.5 — rank-five and lower-rank rows

Classify every row that can consume at most 35 slack. Prove that all omitted
factor-rank types have excess greater than 35 or violate the already frozen
structural packet.

### S50.6 — endpoint-attaining row classification

Reconfirm all zero-excess rows and determine their equality geometry, including
actual `R_2`, derivative-space, and quotient conditions.

### S50.7 — small-positive-excess row classification

Classify rows of excess at most 35, especially excess 1–7, 8–14, 15–21, and
22–35. Record equality conditions, not just values.

### S50.8 — integer slack-profile enumeration

Enumerate every multiset of local row types whose total excess is at most 35
and whose factor-span increments sum to 49.

### S50.9 — minimality constraints

Impose that no proper sub-sum represents the permanent and that zero,
proportional, or combinable terms do not artificially consume the fiftieth
slot.

### S50.10 — all-order constraints

A genuine identity must survive every ordering of its terms. Use alternate
orders to rule out profiles that appear feasible in only one filtration.

### S50.11 — polymatroid formulation

Encode factor-span dimensions as a representable polymatroid. Derive the
rank-function inequalities forced by every near-equality profile.

### S50.12 — exact profile payload

Freeze the surviving finite profile list with exact integer arithmetic and a
small independent enumerator.

### S50.13 — profile completeness proof

Prove that the enumerator covers every factor rank, quotient rank, defect, and
slack source allowed by the theorem hypotheses.

### S50.14 — identify dominant profiles

Order surviving profiles by structural generality, not by the ease of a
restricted coordinate computation.

### S50.15 — S50 decisive output

Return a finite list

```text
N50-PROFILE-01
N50-PROFILE-02
...
```

with no residual continuous numerical parameters outside explicitly stated
geometric strata.

---

# 4. Workstream L50 — local geometry below the 35-slack ceiling

## Goal

Turn each numerical N=50 profile into precise local algebraic geometry.

### L50.1 — rank-seven `d=6` geometry

The rank-seven `d=6` row is expected to be a critical low-excess event. Classify
its kernel line, relation subspace, and exact equality/near-equality locus.

### L50.2 — rank-seven `d=5` geometry

Classify the two-dimensional factor-kernel cases that remain within budget,
including boundary degenerations and noncoordinate kernels.

### L50.3 — rank-seven `d=4` geometry

Determine whether every budget-compatible row forces special `R_2`, a
low-essential-variable cubic kernel, or a permanent-relative incidence.

### L50.4 — low-rank quotient exclusion

Prove uniform excess greater than 35 for all quotient ranks that should not
appear. Do not rely on generic quotient assumptions.

### L50.5 — rank-six equality normal forms

Classify the exact geometry of the `s=1,2`, full-rank equality rows, including
factor multiplicity, derivative spaces, and permitted intersections with the
permanent derivative spaces.

### L50.6 — rank-six near-equality normal forms

Classify every `s,d` pair with excess at most 35. Record which bounds are sharp
and produce exact witnesses for sharp rows.

### L50.7 — rank-five equality row

Determine whether the full rank-five, minimal-middle-rank row can coexist with
49 further terms under all-order factor-span arithmetic.

### L50.8 — nonmonomial degeneration audit

For every proof by degeneration, use fixed-source maps or flat families and
check the correct semicontinuity direction. Do not claim derivative dimensions
or intersection spaces are preserved without proof.

### L50.9 — `R_2` compatibility

Classify the actual spaces

\[
R_2=E_2\cap D_2(T)
\]

that occur on budget-compatible rows, including prolongation restrictions.

### L50.10 — complementary-degree compatibility

For each local row, record the induced constraints in degrees `2/5`, `3/4`,
and `1/6` before global assembly.

### L50.11 — local boundary coverage

Cover zero brackets, repeated factors, rank-drop quotient charts, nonreduced
limits, and projective points at infinity.

### L50.12 — local theorem package

Produce one theorem note and one focused replay, not a separate artifact for
every normal form.

---

# 5. Workstream G50 — global geometry of the surviving N=50 packets

## Goal

Classify all global configurations compatible with the finite slack profiles.

### G50.1 — factor-span packet classification

For every profile, determine the representable multilinear matroid or
polymatroid types of the 50 factor spans.

### G50.2 — redundant-increment terms

Classify terms with `d_i=0` or partial increment. Prove what minimality and
cross-degree equality force on such terms.

### G50.3 — one-defect-from-49 packets

Identify configurations obtained from a 49-term equality packet by one extra
term or one local rank defect. Determine which are genuine deformations and
which are only combinatorial shadows.

### G50.4 — all-rank-seven near-uniform packets

Classify 50 rank-seven planes spanning 49 dimensions under the slack budget.
Analyze circuits, pair intersections, and higher intersections.

### G50.5 — mixed rank-six/rank-seven packets

Enumerate the allowed counts of rank-six equality terms, rank-seven terms, and
near-equality terms. Solve the corresponding increment equations.

### G50.6 — graph-complement generalization

For mixed packets, determine whether a 42-space plus graph complements remains
forced, or whether the extra 35 slack permits new ambient decompositions.

### G50.7 — common-code and multi-code branches

Classify when the graph terms induce one common evaluation code, finitely many
codes, or a genuinely coupled multi-code system.

### G50.8 — circuit localization

Use small circuits of factor planes to localize the global slack. Prove that
some bounded-size subpacket carries a fixed positive amount of the total 35.

### G50.9 — deletion/contraction recursion

For a minimal 50-term packet, analyze deleting one term or contracting one new
factor direction. Derive a smaller endpoint problem without assuming Chow rank
additivity.

### G50.10 — permanent row/column symmetry reduction

Use only actual stabilizers of the permanent to normalize packets. Record the
residual stabilizer and avoid arbitrary changes of variables that move the
target.

### G50.11 — profile-to-branch map

Map every numerical profile from S50 to a finite list of global geometric
branches.

### G50.12 — branch completeness theorem

Prove that the list is exhaustive under the minimal 50-term identity
hypothesis.

### G50.13 — existing-certificate reuse map

Identify which N=49 restricted-family certificates still apply to N=50
branches and which do not.

### G50.14 — global exact survivors

Any packet satisfying all current global conditions receives a compact exact
coordinate artifact and independent verification.

### G50.15 — G50 decisive output

Return a finite theorem-defined branch inventory suitable for permanent-
specific cross-degree exclusion.

---

# 6. Workstream X25 — degree `2/5` coupled module

## Goal

Use the smallest complementary-degree system that retains term labels and
sees the permanent identity.

### X25.1 — labelled derivative sums

Construct

\[
\bigoplus_{i=1}^{50}D_2(T_i),
\qquad
\bigoplus_{i=1}^{50}D_5(T_i),
\]

and their maps to the aggregate spaces.

### X25.2 — exact relation spaces

Define the labelled kernels and distinguish them from unlabelled aggregate
Hilbert relations.

### X25.3 — relation transport

Write the termwise multiplication/differentiation map transporting degree-two
relations to degree five and back.

### X25.4 — endpoint slack contribution

Express part of the 35 slack as a kernel, cokernel, or radical dimension in the
`2/5` module.

### X25.5 — torus-weight decomposition

Split the module by the row/column torus of the permanent. Freeze target and
one-term dimensions in each block.

### X25.6 — smallest overloaded block

Identify a block where the permanent demand exceeds the maximum compatible
supply of every surviving N=50 branch.

### X25.7 — coefficient synchronization

The same 50 scalar coefficients must appear in all degrees. Encode this
synchronization explicitly.

### X25.8 — factor-plane synchronization

The same factor planes must realize both derivative layers. Do not optimize
the two layers independently.

### X25.9 — local-to-global defect theorem

Prove a positive defect for at least one entire branch, or produce an exact
survivor of the complete `2/5` system.

### X25.10 — boundary audit

Cover vanishing term coefficients, proportional derivative generators, and
rank-drop charts.

---

# 7. Workstream X34 — conditional degree `3/4` coupled module

## Entry condition

Open only for branches or exact survivors that pass the complete `2/5`
interface.

### X34.1 — labelled middle maps

Build the degree-three and degree-four term-labelled derivative maps.

### X34.2 — exact Sylvester slack

Express the remaining part of the 35 budget through the precise
output-summation and input-image kernels.

### X34.3 — relation inclusion

Enforce the actual condition analogous to

\[
\ker B\subseteq\operatorname{im}C
\]

with all labels and coefficients retained.

### X34.4 — block decomposition

Split by permanent torus weights before elimination.

### X34.5 — one-term caps on surviving local rows

Use the local geometry from L50 rather than the generic 35-dimensional Chow
cap.

### X34.6 — cross-block compatibility

Relations in different torus blocks arise from the same terms. Record the
shared variables instead of proving unrelated block inequalities.

### X34.7 — exact radical classification

Classify the small radicals forced by near-equality branches.

### X34.8 — branch exclusion or survivor

Return a theorem-level contradiction or an exact survivor satisfying `2/5`
and `3/4` simultaneously.

---

# 8. Workstream X16 — degree `1/6` permanent target

## Goal

Use the strongest explicit permanent-specific target after the relation
modules have reduced the branches.

### X16.1 — missing-row and missing-column blocks

Construct the 49 sextic permanent derivative targets in their natural blocks.

### X16.2 — labelled term supply

For each surviving branch, compute the actual degree-six supply with term
labels and coefficients.

### X16.3 — quotient target defect

Compute target images in the quotient by the term span, block by block.

### X16.4 — integrability constraints

Enforce that the seven derivatives in each missing-row or missing-column block
come from one common septic.

### X16.5 — Waring replacement only with proved hypotheses

Use Waring-rank replacement arguments only after proving the independence and
relation-space assumptions needed for integration.

### X16.6 — multi-relation integrability

Classify compatible gradients when the fifth-power relation space has
dimension at least two; do not extrapolate the one-relation proof.

### X16.7 — Chow-structure strengthening

Retain the Chow factorization and term labels where a pure Waring argument is
too weak.

### X16.8 — target-block obstruction

Find one unavoidable positive target defect on each surviving branch.

### X16.9 — degree-seven check

Use the original septic identity only for a branch that passes every degree-six
condition.

### X16.10 — combined `2/5/6` theorem

State one theorem coupling X25 and X16, rather than two independent rank tests.

---

# 9. Workstream Q50 — theorem-defined exact computation

## Goal

Use computation only after S50 and G50 produce finite mathematical strata.

### Q50.1 — profile enumerator

Implement the exact integer slack-profile enumeration with an independent
minimal replay.

### Q50.2 — local-row verifier

Verify every frozen local excess row and equality condition.

### Q50.3 — torus block builder

Generate `2/5`, `3/4`, and `1/6` blocks from one shared term specification.

### Q50.4 — exact rank backend

Use rational or integer arithmetic for theorem-facing ranks. Modular discovery
is allowed only to find pivots or candidate minors.

### Q50.5 — saturation and nonvanishing

Handle nonzero coefficients and chart pivots by exact saturation or complete
chart coverage.

### Q50.6 — reducedness and collision controls

Detect repeated points, proportional terms, zero combined coefficients, and
nonreduced limits.

### Q50.7 — branch-specific elimination

Run elimination only on a theorem-defined branch with a bounded variable set.

### Q50.8 — exact survivor search

Search for rational points first; then controlled number fields with minimal
polynomials and replay.

### Q50.9 — certificate minimization

Retain one load-bearing minor, identity, resultant, or Gröbner certificate per
lemma, not large exploratory dumps.

### Q50.10 — independent replay

Every load-bearing finite exclusion receives a second implementation or a
mathematically independent certificate.

### Q50.11 — resource bounds

Record deterministic runtime and conservative memory bounds for promoted
computations.

### Q50.12 — negative controls

Include examples that fail if labels, coefficients, target equations, or
nonzero-weight conditions are accidentally omitted.

---

# 10. Workstream T51 — lower-51 theorem assembly

## Entry condition

Every N=50 branch is excluded, or one common theorem subsumes the branch list.

### T51.1 — minimal dependency chain

Write the shortest proof from lower 50 and the 35-slack identity to exclusion
of 50 terms.

### T51.2 — branch coverage table

Map every S50 profile and G50 branch to exactly one exclusion theorem.

### T51.3 — no double-counted slack

Audit that local excess, filtration loss, Sylvester loss, and target defect are
not counted twice.

### T51.4 — all-order coverage

Verify that every filtration-order argument is justified for an arbitrary
minimal decomposition.

### T51.5 — coefficient and minimality audit

Check nonzero coefficients, repeated/proportional terms, and possible shorter
sub-decompositions.

### T51.6 — characteristic-zero audit

Confirm every modular certificate has the correct lift direction and no bad
prime dependency.

### T51.7 — ordinary-rank scope

Do not promote to border rank unless closed-family arguments are independently
proved.

### T51.8 — independent proof-chain review

A fresh reviewer reconstructs the proof without following the implementation
order.

### T51.9 — frozen evidence packet

Keep only theorem-facing proof notes, compact payloads, independent replays,
and focused tests.

### T51.10 — promotion gate

Promote

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge51
\]

only at one exact HEAD with no fatal or major audit finding and passing CI.

---

# 11. Workstream S51 — stretch analysis toward lower 52

## Entry condition

Lower 51 is promoted or the lower-51 proof has a complete frozen draft with no
known gap.

## Goal

Determine whether the same near-equality machinery can exclude 51 terms. The
global slack budget relative to the 49-term endpoint becomes 70, so a naive
doubling of the N=50 branch list is not acceptable.

### S51.1 — exact 70-slack identity

Derive the N=51 analogue of S50.1.

### S51.2 — reusable local cost theorem

Seek a theorem that every departure from an equality packet costs one of a
small set of quanta, rather than enumerating arbitrary partitions of 70.

### S51.3 — slack localization

Prove that a bounded-size subpacket carries at least a fixed amount of the 70
slack.

### S51.4 — two-defect packet classification

Classify configurations obtained from equality packets by two local defects,
one larger defect, or an extra circuit.

### S51.5 — deletion to N=50

Determine whether deleting one carefully chosen term leaves a packet governed
by the N=50 classification.

### S51.6 — contraction to lower dimension

Contract a new factor direction or permanent row/column only when the target
identity descends correctly.

### S51.7 — strengthened cross-degree invariant

Measure whether the `2/5/6` theorem used for lower 51 has quantitative slack
that survives one additional term.

### S51.8 — target-block accumulation

Prove that target defects from disjoint torus blocks cannot all be repaired by
two extra one-term contributions.

### S51.9 — coefficient-sharing gain

Exploit that the same 51 coefficients must solve all block systems.

### S51.10 — factor-plane circuit gain

Use the unavoidable circuits among 51 seven-planes in a 49-space to produce a
new labelled relation.

### S51.11 — exact branch inventory

Return a finite branch list only if no reusable theorem closes the endpoint.

### S51.12 — lower-52 decision

Return exactly one:

```text
L52-PROMOTABLE
L52-FINITE-FRONTIER
L52-EXACT-SURVIVOR
L52-NEW-INVARIANT-REQUIRED
```

### S51.13 — stretch theorem assembly

If promotable, assemble and audit ordinary lower 52 under the same standards as
T51.

### S51.14 — stop before exact-64 expansion

A failure at N=51 triggers an invariant report, not a broad exact-64 program.

---

# 12. Workstream U — reusable theorem extraction

## Goal

Extract general statements only after they remove real N=50 or N=51 branches.

### U.1 — near-equality stability theorem

State a general result describing Chow packets within bounded slack of the
slope-ten endpoint.

### U.2 — weighted evaluation-code theorem

Extract a theorem on reduced point sets, Hadamard products of dual codes, and
permanent-gradient containment if it closes more than one branch.

### U.3 — term-labelled complementary-degree theorem

Abstract the `2/5/6` obstruction to degree-seven products only after its
one-term hypotheses are fully classified.

### U.4 — representable-polymatroid theorem

Extract the factor-span circuit statement if it applies beyond one enumerated
profile.

### U.5 — general-`n` diagnostic

Test constants for `n=8,9` only to determine scaling. Do not start a new
proof program without an exponential-scale gain.

### U.6 — publication boundary

Separate internally derived results from verified literature novelty. No
novelty claim without a dedicated source review.

---

# 13. Workstream A — adversarial audit and evidence discipline

### A.1 — hypothesis ledger

For every theorem record characteristic, ordinary/border scope, minimality,
reducedness, coefficient nonvanishing, quotient rank, chart assumptions, and
closure coverage.

### A.2 — semicontinuity audit

Check every degeneration and specialization direction.

### A.3 — relation-space audit

Check every occurrence of `C_d`, `R_d`, `I_d`, and `W_d` against the notation
firewall.

### A.4 — weight audit

Verify whether weights can be normalized, inverted, or absorbed in each map.

### A.5 — target audit

Ensure permanent target containment is imposed in the correct derivative
space and degree.

### A.6 — minimality audit

Rule out shortening by combining proportional terms or deleting a zero
coefficient.

### A.7 — boundary audit

Cover rank drops, vanishing pivots, projective infinity, repeated points, and
nonreduced limits.

### A.8 — adversarial examples

Mandatory controls include Glynn truncations, non-tensor Sylvester equality,
weighted coupling survivors, and every exact v3 survivor.

### A.9 — finite-field audit

A modular nonzero minor may prove characteristic-zero nonvanishing. Modular
failure or absence of a point does not prove characteristic-zero emptiness.

### A.10 — external theorem audit

Record the exact statement and field hypotheses of every Waring, Hilbert,
Macaulay, Cayley–Bacharach, apolar, or syzygy theorem used.

### A.11 — proof-order independence

The final reviewer must be able to reorder lemmas by logical dependency.

### A.12 — artifact minimization

Remove exploratory payloads from the theorem-facing packet unless they are
needed for replay.

---

# 14. Execution waves

## Wave 0 — frontier freeze and route selection

Execute:

```text
F.1–F.8
P49.1–P49.5 if common-graph closure is still open
P49.12–P49.14 if Packet A is still open
S50.1–S50.4 in parallel once lower 50 is promoted
```

Decisions required:

- exact lower-50 status;
- unique unresolved N=49 theorem, if any;
- initial local excess table for N=50.

## Wave 1 — complete 50-term numerical classification

Execute:

```text
S50.5–S50.15
L50.1–L50.7
Q50.1–Q50.3
```

Required output: finite and proved N=50 numerical profile list.

## Wave 2 — convert profiles to global branches

Execute:

```text
L50.8–L50.12
G50.1–G50.15
X25.1–X25.5
Q50.4–Q50.6
```

Required output: exhaustive global branch inventory and first coupled modules.

## Wave 3 — permanent-specific branch closure

Execute:

```text
X25.6–X25.10
X16.1–X16.10
X34 only for genuine survivors
Q50.7–Q50.12
```

Required output: every N=50 branch closed or represented by an exact survivor.

## Wave 4 — lower-51 theorem

Execute:

```text
T51.1–T51.10
A.1–A.12
```

Required output: promoted lower 51 or one explicit unresolved endpoint
component.

## Wave 5 — stretch lower 52

Execute:

```text
S51.1–S51.14
U.1–U.4 where they remove branches
```

Required output: lower 52, a finite N=51 frontier, or an exact explanation that
a new invariant is required.

---

# 15. Parallel lanes

```text
Lane 1  S50 integer/slack classification
Lane 2  L50 local quotient geometry
Lane 3  G50 global packet geometry
Lane 4  X25/X16 permanent-specific modules
Lane 5  exact computation and adversarial controls
```

Dependencies:

- G50 consumes the S50 profile list but may prepare intrinsic equations early.
- X25 may prepare generic blocks early but branch theorems wait for G50.
- X34 waits for an exact `2/5/6` survivor.
- T51 waits for complete N=50 branch coverage.
- S51 waits for a frozen lower-51 proof.

No lane exists merely to keep hardware busy.

---

# 16. Milestones

## M0 — completed-v3 frontier frozen

```text
[ ] terminal-task ledger
[ ] corrections integrated
[ ] survivor inventory verified
[ ] lower-50 gate status fixed
```

## M1 — lower 50 settled

```text
[ ] PACKET-A-CLOSED
[ ] PACKET-B-CLOSED
[ ] lower-50 proof and audit frozen
```

or one exact endpoint survivor is identified.

## M2 — 35-slack identity and local table

```text
[ ] exact slack decomposition
[ ] arbitrary-quotient local excess table
[ ] equality and near-equality loci classified
```

## M3 — finite N=50 profile list

```text
[ ] integer profiles enumerated
[ ] all-order and minimality constraints imposed
[ ] profile completeness proved
```

## M4 — finite global branch list

```text
[ ] factor-span polymatroids classified
[ ] mixed/all-rank-seven branches classified
[ ] branch completeness proved
```

## M5 — smallest cross-degree module decided

```text
[ ] complete `2/5` module
[ ] degree-six target coupled
[ ] every branch excluded or exact survivor frozen
```

## M6 — all N=50 packets decided

```text
[ ] every profile mapped to an exclusion theorem
[ ] no uncovered chart or boundary
```

## M7 — lower 51 promoted

```text
[ ] theorem assembled
[ ] independent audit passes
[ ] exact evidence and CI frozen
```

## M8 — N=51 slack structure decided

```text
[ ] 70-slack identity
[ ] reusable cost/localization theorem or finite branch list
```

## M9 — lower-52 decision

```text
[ ] L52-PROMOTABLE
```

or a precise finite frontier/survivor/new-invariant report.

## M10 — package closeout

Archive only terminal results and the next true mathematical frontier.

---

# 17. Stop rules

Suspend the following unless a theorem-defined branch requires them:

- larger blind random searches;
- more primes as a substitute for characteristic-zero proof;
- unrestricted `GL_7` or `GL_6` scans;
- expansion of completed monomial-curve boxes;
- uncoupled scalar derivative or Koszul sweeps;
- one-number Hilbert bounds without labels or target equations;
- broad mixed-Glynn family enumeration;
- full Gröbner elimination in hundreds of point variables;
- degree `3/4` construction before a `2/5/6` survivor;
- exact-64 architecture before lower 51/52 is decided;
- generalized experiment infrastructure.

Stop a branch immediately when it yields an exact survivor satisfying all
encoded hypotheses. Analyze the survivor before searching adjacent families.

---

# 18. What counts as substantive progress

Substantive progress includes:

- a promoted lower-50 theorem;
- an exact N=49 endpoint survivor;
- the complete 35-slack identity;
- a proved arbitrary-quotient local excess row;
- elimination of one entire numerical N=50 profile;
- a complete global branch classification;
- a term-labelled `2/5/6` defect theorem;
- an exact N=50 survivor exposing the missing invariant;
- promotion of lower 51;
- a reusable theorem reducing the N=51 frontier;
- promotion of lower 52.

The following are not substantive by themselves:

- another random negative sample;
- another test prime;
- a new restricted family not forced by the endpoint;
- a refactor of an existing evaluator;
- a plan, registry, or evidence format with no theorem consequence.

---

# 19. Promotion gates

## Lower 50

```text
[ ] all 49-term equality packets excluded
[ ] arbitrary weights and permitted graph complements covered
[ ] Packet A uses permanent-specific labelled equations
[ ] characteristic-zero evidence complete
[ ] no fatal or major audit finding
```

## Lower 51

```text
[ ] exact 35-slack identity
[ ] complete local excess table for all budget-compatible terms
[ ] finite and exhaustive N=50 profile list
[ ] finite and exhaustive global branch list
[ ] every branch excluded by coupled permanent-specific equations
[ ] all boundaries and orderings covered
[ ] independent proof-chain audit and CI pass
```

## Lower 52

```text
[ ] exact 70-slack identity
[ ] reusable localization/cost theorem or exhaustive N=51 branches
[ ] every N=51 branch excluded
[ ] no unproved transfer from N=50
[ ] independent audit and frozen exact evidence
```

---

# 20. Deliverable budget

For each load-bearing theorem component, the preferred maximum is:

```text
1 proof note
1 compact exact evidence payload if computation is necessary
1 primary replay
1 independent replay or independent mathematical certificate
focused tests
```

Exploratory notebooks, temporary chunks, and search logs are not part of the
promotion packet.

---

# 21. Success criterion

The preferred outcome is an audited ordinary characteristic-zero theorem

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge51.
\]

The stretch outcome is lower 52. A scientifically successful alternative is
an exact 50- or 51-term endpoint survivor satisfying every currently proved
condition and isolating one genuinely missing invariant.

The package is considered unsuccessful if it merely closes more unrestrictedly
chosen finite families without producing a theorem, an exact survivor, or a
strictly smaller exhaustive frontier.
