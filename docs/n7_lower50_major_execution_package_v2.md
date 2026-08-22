# `perm_7` lower-50 major execution package v2

## Status

`ACTIVE MAJOR RESEARCH PACKAGE — NOT A NEW LOWER-BOUND RESULT.`

Created: 2026-08-22  
Input research snapshot: `170bd086a2c836c53160cf6b353e167b1228586c`  
Active research PR: `#31`  
Current ordinary characteristic-zero interval:

\[
49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

Primary promotion target:

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50.}
\]

This package supersedes the short implementation checkpoint in
`docs/n7_lower50_next_phase_task_plan.md`. The earlier checkpoint has done its
job: it produced the exact weighted common-graph interface, classified the
numerical equality ranks, removed `(36,36)`, exhibited characteristic-zero
realisations of the remaining four Hilbert profiles, and excluded the old
`(30,42)` and weighted `(31,41)` controls from the degree-six permanent target.

The lower-50 theorem itself is not yet proved. The present package is designed
to carry the project from the current four-stratum common-graph frontier all
the way through arbitrary Packet B, Packet A, theorem assembly, adversarial
audit, and promotion if the mathematics supports it.

The package is intentionally large. It is not an architecture expansion. It
contains mathematical work, exact evaluators, theorem-facing replays, and
review tasks only.

---

# 0. Frozen input boundary

The following facts are fixed inputs and are not to be reproved unless a later
argument exposes a contradiction.

## 0.1 Current endpoint reduction

Any hypothetical 49-term decomposition lies in one of two slope-ten equality
packets.

### Packet A

All 49 terms have factor rank seven.

### Packet B

Seven rank-six equality terms span a direct 42-space and the remaining 42
terms are rank-seven graph complements.

Both packets obey term-labelled complementary-degree equality, not just scalar
Hilbert-function inequalities.

## 0.2 Common-graph Packet-B interface

For 42 graph points in `P^6`, write `E_d` for the homogeneous degree-`d`
evaluation matrix and let

\[
D=\operatorname{diag}(d_1,\ldots,d_{42}),\qquad d_i\neq0.
\]

Scalar equality and coupling give

\[
\operatorname{rank}E_3+\operatorname{rank}E_4=72,
\]

\[
\boxed{\operatorname{rank}(E_4^TDE_3)=30}.
\]

Degree-six permanent containment is

\[
\operatorname{rank}\begin{bmatrix}E_6\\S_6\end{bmatrix}
=\operatorname{rank}E_6,
\]

where `S_6` is the `7 x 924` matrix of the seven squarefree sextic permanent
targets for one missing-row block.

## 0.3 Completed rank classification

The seven numerical middle-equality profiles are

```text
(30,42), (31,41), (32,40), (33,39), (34,38), (35,37), (36,36).
```

Degree-six target integrability forces `H_Z(5)<=40`, removing `(30,42)` and
`(31,41)` from any target-compatible solution. The reduced-point Hilbert
function argument removes `(36,36)`.

The surviving geometrically feasible profiles are exactly

```text
(32,40), (33,39), (34,38), (35,37).
```

Each of these four profiles has an explicit characteristic-zero curve-union
realisation. Therefore no future proof may dismiss a profile merely because
it appears nongeneric or was absent from a previous random sample.

## 0.4 Existing controls

The old unit `(30,42)` and weighted `(31,41)` monomial-curve controls satisfy
middle equality and coupling but fail all seven degree-six permanent targets.
Their target failure has characteristic-zero integer certificates.

The 130-point monomial-curve weight box is closed as a restricted family. Do
not enlarge the same box without a new theorem explaining what new component
would be hit.

## 0.5 Claim boundary

Nothing in the frozen input closes the arbitrary weighted common-graph family,
Packet B, or Packet A. No lower 50, exact 64, or border-rank conclusion follows
from the present checkpoint.

---

# 1. Overall execution strategy

The work is divided into five theorem layers.

```text
Layer I    Close the four common-graph strata.
Layer II   Remove the common-graph assumption and close arbitrary Packet B.
Layer III  Close the all-rank-seven Packet A.
Layer IV   Assemble and adversarially audit the lower-50 theorem.
Layer V    Only after promotion, open the lower-51 / exact-rank frontier.
```

Recommended research effort until lower 50 is decided:

```text
45%  Layer I: common-graph four-stratum closure
25%  Layer II: arbitrary Packet-B reduction and closure
20%  Layer III: Packet-A term-labelled equations
10%  exact replay, counterexamples, audit, theorem assembly
```

This allocation is a priority guide, not a scheduling subsystem.

---

# 2. Workstream B1-F — freeze the four surviving common-graph strata

## Goal

Turn the current four numerical profiles into explicit algebraic strata with
all rank hypotheses, nonvanishing conditions, and target equations written in
a form suitable for exact elimination and structural proof.

## B1-F.1 — define stratum-local coordinates

For each profile

```text
S32 = (32,40)
S33 = (33,39)
S34 = (34,38)
S35 = (35,37)
```

choose a representation that keeps the following visible:

- the degree-three kernel `K_3`;
- the degree-four kernel `K_4`;
- the nesting/multiplication compatibility between them;
- the nonzero diagonal weights `D`;
- the seven degree-six target rows;
- point distinctness and graph nondegeneracy.

Do not start with a giant unrestricted coordinate ring in 252 point
coordinates plus 42 weights. First quotient the obvious projective and basis
redundancies that do not change the evaluation codes.

**Output:** one short specification note containing dimensions and variables
for all four strata.

## B1-F.2 — derive kernel-side coupling equations

Rewrite

\[
\ker(E_4^T)\subseteq D\operatorname{im}(E_3)
\]

as equations involving bases for `K_3` and `K_4` whenever this reduces the
variable count.

The derivation must remain equivalent to the rank-30 formulation on the fixed
stratum. Record explicitly which minors or nonvanishing assumptions are used.

**Output:** exact symbolic equations plus equivalence lemma.

## B1-F.3 — derive quotient-side degree-six target equations

Instead of repeatedly forming the full `49 x 924` stack, compute the image of
the seven permanent rows in the quotient

\[
S^6(V^*)/\operatorname{rowspan}(E_6).
\]

Exploit row/column multidegrees and the graph chart to split this quotient into
the smallest exact blocks available.

**Output:** deterministic target-defect evaluator returning block defects and a
proof that zero block defect is equivalent to full degree-six containment.

## B1-F.4 — construct exact positive controls per stratum

For each of the four Hilbert profiles, retain at least one exact integer point
configuration realising the profile. It need not satisfy coupling or target.
The purpose is to prevent accidental algebraic assumptions from deleting the
entire stratum.

**Gate:** every stratum-local parameterization must successfully represent its
control.

## B1-F.5 — construct negative controls

At least two controls must fail for the correct reason:

1. a configuration satisfying the profile and coupling but failing target;
2. a configuration satisfying profile and target-like rank conditions but
   failing the weighted coupling or weight nonvanishing condition, if such a
   control can be constructed exactly.

The evaluator must distinguish these failure modes.

---

# 3. Workstream B1-S32 — close `(32,40)`

## Goal

Prove that no reduced 42-point weighted common-graph configuration with

\[
(\operatorname{rank}E_3,\operatorname{rank}E_4)=(32,40)
\]

can satisfy coupling and all degree-six permanent targets, or produce an exact
characteristic-zero survivor satisfying every encoded condition.

## B1-S32.1 — exploit the ten-dimensional cubic relation space

Here

```text
dim K_3 = 10
dim K_4 = 2
```

for the 42-point code. Determine the multiplication map from the cubic
relations into quartic relations and classify the possible two-dimensional
quartic kernel compatible with a ten-dimensional cubic kernel.

The first target is a structural statement, not brute-force elimination.

## B1-S32.2 — constrain `D` from the two quartic relations

The weighted coupling condition means that the two quartic relations, after
weighting, lie in the degree-three evaluation image in the precise transpose
sense. Eliminate `D` symbolically as far as possible.

Questions to answer:

- Is `D` unique up to scalar on a dense component?
- Does existence of nonzero `D` impose a determinantal condition on the point
  configuration alone?
- Are there forced support partitions or low-degree curves?

## B1-S32.3 — intersect with degree-six target containment

Substitute the coupling consequences into the target-defect blocks. Search for
a load-bearing exact minor, resultant, syzygy, or integrability contradiction.

## B1-S32.4 — classify boundary components

If the dense component is excluded, explicitly enumerate rank-drop and pivot
boundary cases introduced by the local chart. Do not assume they are covered
by continuity unless the equations used are closed on that boundary.

## B1-S32.5 — decisive outcome

Return one of:

```text
S32-CLOSED
S32-SURVIVOR
S32-REDUCED-TO-EXPLICIT-FINITE-SUBCASES
```

The third outcome is accepted only if the subcases are theorem-defined and
small enough to exhaust exactly in the next pass.

---

# 4. Workstream B1-S33 — close `(33,39)`

## Goal

Handle the next Hilbert stratum without copying the S32 calculation blindly.

Here

```text
dim K_3 = 9
dim K_4 = 3.
```

## B1-S33.1 — determine allowed `K_3 -> K_4` growth

Use Macaulay/Gotzmann-type growth only where it is sharp for reduced points.
Record every possible initial ideal or Hilbert-Burch pattern compatible with
`H(3)=33`, `H(4)=39`, and eventual length 42.

## B1-S33.2 — classify low-degree geometric support forced by the Hilbert
function

Test whether the stratum necessarily contains a substantial subset on a
curve, conic bundle, rational normal projection, or another low-degree
subscheme. Separate theorem from diagnostic examples.

## B1-S33.3 — solve the weighted coupling on each structural component

For each component, derive the dimension of admissible diagonal weights. A
component on which no invertible diagonal exists is immediately closed.

## B1-S33.4 — apply permanent-target blocks

Use the seven sextic targets only after the coupling structure has reduced the
problem. Prefer a small multidegree block with positive unavoidable defect to
full elimination.

## B1-S33.5 — exact replay

Any component exclusion relying on a determinant must preserve the actual
integer determinant or a modular nonzero minor with a valid characteristic-
zero interpretation.

---

# 5. Workstream B1-S34 — close `(34,38)`

## Goal

Analyze

```text
dim K_3 = 8
dim K_4 = 4.
```

This more balanced kernel profile may admit more coupling freedom, so the plan
must use complementary-degree structure early.

## B1-S34.1 — compute the multiplication incidence

Construct the exact incidence between cubic relations, their seven linear
multiples, and the four-dimensional quartic relation space.

Measure:

- multiplication rank;
- first syzygy dimension;
- common-factor possibilities;
- support decomposition possibilities.

## B1-S34.2 — derive coupling-induced bilinear form constraints

Interpret `E_4^T D E_3` as a weighted pairing between degree-three and
degree-four evaluation spaces. Determine what rank exactly 30 says about the
radicals on this `(34,38)` stratum.

## B1-S34.3 — permanent-specific incompatibility search

Split the sextic target rows by the row/column torus. For each target block,
write the minimal condition imposed on the pairing radicals. Attempt to prove
that at least one block cannot vanish simultaneously.

## B1-S34.4 — survivor extraction

If symbolic reduction leaves a positive-dimensional component, search it for
an exact rational or number-field point satisfying every condition. A genuine
survivor is higher priority than continuing exclusion by increasingly narrow
families.

---

# 6. Workstream B1-S35 — close `(35,37)`

## Goal

Analyze the most balanced surviving profile

```text
dim K_3 = 7
dim K_4 = 5.
```

This is expected to be the hardest common-graph stratum and should be treated
as such rather than as a final small case.

## B1-S35.1 — classify seven cubic relations with only five quartic relations

Determine the strongest possible common structure of the cubic kernel forced
by this unusually small growth.

Candidate tools include:

- generic initial ideals;
- Green/Macaulay restrictions;
- Hilbert-Burch or minimal free resolution data;
- Cayley-Bacharach consequences;
- reduced-point separator degrees.

Use only statements valid in characteristic zero and record assumptions.

## B1-S35.2 — identify the minimal geometric carrier

Test whether every such 42-point set must lie substantially on a low-degree
curve or reducible union. The existing degree-two curve-union construction is
a positive control for profile realisability, not evidence that all points
have that form.

## B1-S35.3 — solve diagonal coupling dimension

Compute the linear system on the 42 diagonal entries after fixing the point
configuration. Determine generic and special dimensions of admissible weight
space.

## B1-S35.4 — impose nonzero weights exactly

Do not accept a solution supported on fewer than 42 graph terms. Saturate by

\[
\prod_i d_i
\]

or use an equivalent chart-by-chart exact argument.

## B1-S35.5 — combine with sextic target

If target containment and coupling define separate loci, compute their
intersection dimension or exhibit a separating invariant.

## B1-S35.6 — boundary and degeneration audit

Because this stratum is likely to contain degenerations of higher-Hilbert
profiles, explicitly check whether a closure argument accidentally admits
nonreduced points, repeated graph points, or zero weights.

---

# 7. Workstream B1-X — cross-stratum theorem extraction

## Goal

Avoid four unrelated case proofs if one structural theorem explains them all.
This workstream begins after at least two strata have been analyzed deeply
enough to reveal a pattern.

## B1-X.1 — weighted apolar / evaluation-code formulation

Search for a theorem of the following form:

> If a reduced 42-point set in `P^6` has `H(3)+H(4)=72`, admits an invertible
> diagonal pairing of rank 30, and contains the permanent sextic gradient,
> then its degree-three/four Hilbert function violates one of the four allowed
> profiles or its points satisfy an impossible permanent-specific incidence.

A theorem even slightly weaker may remove several strata at once.

## B1-X.2 — relation-support theorem

Determine whether coupling forces the supports of low-degree relations to
align with row/column partitions of the permanent variables. If yes, classify
those partitions exactly.

## B1-X.3 — target integrability upgrade

The existing integrability argument only proves `H_Z(5)<=40`. Seek the next
permanent-specific consequence, for example:

```text
H_Z(5)<=39,
a forbidden shape of the degree-five relation space,
or a forced rank defect in one torus block.
```

Any universal improvement must be checked against the four explicit Hilbert
profile controls.

## B1-X.4 — close B1

B1 is closed only when all four strata are excluded for arbitrary invertible
weights and arbitrary reduced common-graph point configurations.

Required status line:

```text
B1-CLOSED: no weighted common-graph Packet-B solution exists in
characteristic zero.
```

If a survivor remains, record `B1-SURVIVOR` instead and stop broad exclusion
work until the survivor is understood.

---

# 8. Workstream B2-R — remove the common-graph assumption

## Goal

Pass from the common-graph model to the actual arbitrary mixed Packet-B
equality packet.

This is not optional. B1-CLOSED alone does not prove Packet B impossible.

## B2-R.1 — restate arbitrary Packet B in intrinsic coordinates

Write the seven rank-six terms as a direct sum of six-factor spaces and each
of the 42 rank-seven terms as an appropriate graph complement relative to the
fixed 42-space.

Make explicit which graph maps may differ term-by-term.

## B2-R.2 — identify shared equality data

Derive what the slope-ten equality forces globally across the 42 separate
graph complements:

- shared domain/codomain flags;
- common evaluation-code quotients;
- synchronized relation spaces;
- overlap ranks;
- term-weight equations.

## B2-R.3 — prove a common-code reduction if possible

The strongest desired theorem is not necessarily “all graph maps are equal.”
It is enough to show that all terms induce one common pair of degree-three and
degree-four codes, or a finite number of code types covered by B1-like
arguments.

## B2-R.4 — otherwise classify residual moduli

If a common-code theorem is false, construct an exact counterexample and list
the true residual moduli. Then stratify only by invariants that actually enter
the coupling and permanent target equations.

## B2-R.5 — derive finite structural branches

A valid reduction should end in a finite list resembling:

```text
common-code branch
rank-drop branch
overlap branch
boundary/degeneration branch
exceptional support-partition branch
```

The list must be mathematically exhaustive, not empirically observed.

---

# 9. Workstream B2-E — exhaust arbitrary Packet-B branches

## Goal

Close every branch produced by B2-R, reusing the existing exact certificate
library wherever possible.

## B2-E.1 — certificate map

Create a small table mapping each branch to already proved exclusions:

- high-overlap dense strata;
- Laurent-torus boundary audit;
- `(2,3)/(3,2)` rank-one update exclusions;
- `(2,4)/(4,2)` rank-one update exclusions;
- signed families;
- monomial families;
- elementary-shear families;
- common-graph B1 theorem when applicable.

This is documentation, not a new registry or database.

## B2-E.2 — prove uncovered branches

For every branch not covered by an existing theorem, derive the smallest exact
invariant capable of distinguishing it. New computation is justified only for
these explicitly uncovered branches.

## B2-E.3 — mixed-term coupling

Retain term labels. Scalar sums of code dimensions are insufficient. The
arbitrary packet must satisfy the exact relation transport between the
individual graph complements and the seven rank-six terms.

## B2-E.4 — target containment

At least degree six must be enforced. Degree seven is added only if a branch
passes every degree-six test and the original Packet-B reduction really
requires a seventh-degree condition.

## B2-E.5 — Packet-B decisive outcome

Return exactly one of:

```text
PACKET-B-CLOSED
PACKET-B-SURVIVOR
```

`PACKET-B-CLOSED` requires coverage of arbitrary allowed graph complements,
not just common graphs or a finite sampled family.

---

# 10. Workstream A0 — rebuild the Packet-A interface at the current frontier

## Goal

Prepare the all-rank-seven packet for theorem work without reopening already
failed scalar routes.

## A0.1 — freeze exact one-term derivative modules

For a generic rank-seven Chow term `T_i`, record bases and dimensions for

\[
D_2(T_i),\quad D_5(T_i),\quad D_6(T_i),
\]

plus the multiplication/differentiation maps needed below.

## A0.2 — term-labelled direct sum

Construct the labelled spaces

\[
\bigoplus_{i=1}^{49}D_d(T_i)
\]

and the map to the aggregate permanent derivative space. Do not quotient away
term labels before the cross-degree relations are formed.

## A0.3 — mandatory adversarial controls

Every proposed lemma must be tested against:

1. the 49-term Glynn truncation counterexample;
2. existing non-tensor-split Sylvester-equality examples;
3. a generic random rank-seven Chow-term ensemble as a sanity control.

Only the first two are theorem-relevant adversarial examples; the random
ensemble is diagnostic.

---

# 11. Workstream A25 — degree `2/5` relation pairing

## Goal

Exploit complementary degrees before introducing the larger `3/4` interface.

## A25.1 — define the labelled relation spaces

Let `R_2` and `R_5` be the kernels of the maps from the labelled one-term
derivative sums to the corresponding aggregate derivative spaces. Construct
the exact termwise pairing induced by multiplication/differentiation.

## A25.2 — derive Sylvester equality constraints

Translate equality in the endpoint rank bound into a condition of the form

\[
\ker B\subseteq\operatorname{im}C
\]

with all term labels retained. State dimensions and radicals explicitly.

## A25.3 — split by permanent torus weights

Decompose the pairing by row/column multidegrees. Identify the smallest block
in which the permanent target has a rank demand that a 49-term all-rank-seven
packet may fail.

## A25.4 — defect theorem or survivor

Try to prove one permanent-specific positive defect in the `2/5` system. If
no defect exists, construct an exact packet satisfying the full encoded
`2/5` equations and use it to identify what information is missing.

---

# 12. Workstream A6 — degree-six permanent target for Packet A

## Goal

Use degree six as the first explicit permanent-specific target beyond the
relation pairing.

## A6.1 — construct target quotient blocks

For the 49 labelled rank-seven terms, compute the span available in each
missing-row/missing-column sextic block and compare it with the permanent
sextic derivative target.

## A6.2 — couple A6 to A25

The same term coefficients and factor planes must realize both interfaces.
Do not optimize degree-six containment independently from the `2/5` relation
pairing.

## A6.3 — factor-plane matroid constraints

Use the forced simple multilinear matroid only after the term-labelled maps
are written. Existing counterexamples show that unlabelled incidence data is
insufficient by itself.

## A6.4 — search for a blockwise contradiction

Preferred theorem forms include:

- one torus block has unavoidable positive defect;
- equality forces a tensor-split normal form already known to be impossible;
- complementary-degree radicals cannot be simultaneously represented by 49
  rank-seven Chow terms;
- the sextic target forces a forbidden dependence among factor seven-planes.

---

# 13. Workstream A34 — conditional degree `3/4` escalation

## Entry condition

Start only if a genuine exact or symbolically unresolved survivor passes the
complete A25+A6 interface.

## Goal

Add the larger middle complementary-degree system only where it is needed.

## A34.1 — construct term-labelled middle codes

Build the exact degree-three and degree-four labelled derivative maps for the
survivor component.

## A34.2 — relation transport

Track how every term-labelled relation in degree three differentiates or
multiplies into degree four and how the Sylvester equality couples the two.

## A34.3 — permanent torus decomposition

Again split by row/column weights before any large elimination.

## A34.4 — classify surviving components

Return a finite theorem-defined list, an exact survivor, or a contradiction.
Do not replace this step with an unrestricted random search.

---

# 14. Workstream AX — cross-Packet structural lemmas

## Goal

Search for permanent-specific endpoint principles that simultaneously explain
why both equality packets should fail.

This is a secondary stream and must not delay concrete B1/B2 work.

## AX.1 — common complementary-degree obstruction

Compare the exact equality maps in Packets A and B. Determine whether both are
instances of one general statement about minimal 49-term decompositions of
`perm_7`.

## AX.2 — gradient integrability with Chow structure

The current B1 integrability theorem uses Waring rank after passing to powers.
Seek a version retaining Chow factorization and term labels. Even a modest
strengthening may eliminate multiple B1 strata or constrain Packet A.

## AX.3 — apolar resolution interface

Determine whether the permanent's low-degree apolar resolution has a Betti or
syzygy feature incompatible with either endpoint packet while remaining
satisfied by the existing counterexample controls.

A speculative invariant is kept only if it produces a concrete exact test in
one research cycle.

---

# 15. Workstream C — exact computation support

## Goal

Provide only the computation needed by the theorem streams above.

## C.1 — reusable exact evaluation-code primitives

Factor out only genuinely reused routines for:

- homogeneous monomial enumeration;
- evaluation matrices;
- exact/modular rank;
- kernel bases;
- target quotient defect;
- diagonal coupling rank.

Do not build a general computer-algebra framework.

## C.2 — modular discovery protocol

Finite fields may be used to:

- find pivots;
- locate likely components;
- discover candidate minors;
- search for counterexamples;
- estimate dimensions.

They may not by themselves certify characteristic-zero nonexistence.

## C.3 — characteristic-zero promotion

Every theorem-facing finite calculation must end as one of:

- exact rational elimination;
- exact integer determinant/minor;
- modular nonzero minor with a valid integer lift argument;
- exact number-field certificate with minimal polynomial and replay.

## C.4 — survivor serialization

Every exact survivor must be written to one compact machine-readable artifact
containing points/factors, weights, and every claimed rank. Avoid proliferating
intermediate search dumps.

## C.5 — independent replay

A load-bearing computation gets one independent replay implementation or one
mathematically independent certificate. Routine exploratory calculations do
not require duplicated infrastructure.

---

# 16. Workstream D — adversarial theorem audit

## Goal

Prevent a false lower-50 promotion while keeping review proportional.

## D.1 — hypothesis ledger

For each endpoint-exclusion theorem, record:

```text
characteristic
ordinary vs border rank
point reducedness
weight nonvanishing
minimality assumptions
rank-stratum assumptions
closure/boundary coverage
external theorems invoked
```

This is a markdown table, not a new database.

## D.2 — counterexample attack

For every major lemma ask:

- Does Glynn truncation violate it?
- Does the lemma accidentally assume generic points?
- Does setting one weight to zero create a false proof?
- Does a repeated-point degeneration escape the argument?
- Does a nonreduced flat limit invalidate a continuity step?
- Is a modular rank being interpreted in the wrong direction?

## D.3 — boundary audit

Any proof using a chart or invertible minor must explicitly cover its
complement. Boundary coverage may cite another theorem; it need not duplicate
it.

## D.4 — independent mathematical review

Before promotion, perform at least one fresh proof-chain audit from the
slope-ten endpoint reduction to Packet-A and Packet-B exclusion without using
the authors' intended proof order as an assumption.

---

# 17. Workstream P — lower-50 theorem assembly

## Entry condition

Start final assembly only when both statuses exist:

```text
PACKET-A-CLOSED
PACKET-B-CLOSED
```

## P.1 — theorem dependency graph

Write the shortest dependency chain from established lower 49 to exclusion of
all 49-term identities. Remove exploratory lemmas that are not load-bearing.

## P.2 — statement scope

The promoted statement must be exactly scoped. Unless separately proved, it
should read as an ordinary characteristic-zero Chow-rank result:

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge50.
\]

Do not silently promote to border rank or arbitrary characteristic.

## P.3 — exact frozen evidence

Freeze only the artifacts used by the final theorem. Suggested maximum:

```text
1 theorem/proof note
1 dependency/audit note
1 compact exact evidence payload per genuinely computational lemma
1 independent replay per load-bearing computation
focused tests
```

## P.4 — full repository test

Run the theorem-facing exact tests and the existing repository suite at one
frozen commit.

## P.5 — adversarial signoff

No lower-50 promotion while a fatal or major mathematical finding remains.
Minor editorial findings may be repaired in place without creating a new
research architecture.

---

# 18. Workstream N50-S — survivor protocol

## Goal

Treat exact survivors as valuable results rather than failed searches.

Any exact survivor to a major interface immediately changes priorities.

## S.1 — verify every hypothesis

Recompute all required ranks and nonvanishing conditions independently.

## S.2 — determine whether the survivor is a true endpoint packet

Check whether it satisfies only a relaxed interface or all hypotheses of the
Packet-A/Packet-B reduction.

## S.3 — identify the missing invariant

If it is not a true decomposition, isolate the first condition separating it
from an actual 49-term identity. That condition becomes the next theorem
target.

## S.4 — do not bury survivors

A structurally meaningful survivor gets a dedicated note and frozen exact
coordinates. Do not keep expanding a search family merely to find more of the
same type.

---

# 19. Workstream N50-M — milestone sequence

This package is intentionally larger than one checkpoint. Progress should be
recorded against the following milestones.

## Milestone M1 — four-stratum algebra frozen

Required:

```text
[ ] S32/S33/S34/S35 exact coordinates defined
[ ] coupling equations equivalent on each stratum
[ ] degree-six target quotient blocks implemented
[ ] positive and negative controls pass
```

## Milestone M2 — first two common-graph strata decided

Required:

```text
[ ] S32 decisive outcome
[ ] S33 decisive outcome
[ ] exact certificates or exact survivors frozen
```

## Milestone M3 — common-graph family decided

Required:

```text
[ ] S34 decisive outcome
[ ] S35 decisive outcome
[ ] B1-X cross-stratum theorem applied where useful
[ ] B1-CLOSED or B1-SURVIVOR
```

## Milestone M4 — arbitrary Packet B decided

Required:

```text
[ ] exhaustive arbitrary-graph structural reduction
[ ] existing certificate library mapped to branches
[ ] uncovered branches resolved
[ ] PACKET-B-CLOSED or PACKET-B-SURVIVOR
```

## Milestone M5 — Packet A minimal interface decided

Required:

```text
[ ] A25 relation pairing frozen
[ ] A6 target coupled to A25
[ ] adversarial controls checked
[ ] either PACKET-A-CLOSED or an exact survivor entering A34
```

## Milestone M6 — both equality packets decided

Required:

```text
[ ] PACKET-A-CLOSED
[ ] PACKET-B-CLOSED
```

or an exact endpoint survivor demonstrating that lower 50 cannot be promoted
by the present strategy.

## Milestone M7 — theorem promotion

Required:

```text
[ ] complete dependency chain
[ ] exact evidence frozen
[ ] independent replay
[ ] adversarial audit no fatal/major issue
[ ] CI and focused tests pass at one exact HEAD
```

Only at M7 may the lower bound be changed to 50.

---

# 20. Parallel execution map

The following tasks may run in parallel without creating duplicate work.

```text
Lane 1: B1-F -> S32 -> S33
Lane 2: B1-F -> S34 -> S35
Lane 3: B2-R intrinsic reduction, using B1 outputs as they become available
Lane 4: A0 -> A25 -> A6
Lane 5: exact-computation support + adversarial controls
```

Dependencies:

```text
B2-E waits for B2-R structural branches.
A34 waits for a real A25+A6 survivor.
Final theorem assembly waits for PACKET-A-CLOSED and PACKET-B-CLOSED.
```

No lane is created solely to keep hardware busy.

---

# 21. Immediate execution batch

The next concrete batch should be large enough to generate multiple genuine
research decisions before the next replanning cycle.

## Batch 1A — common-graph algebra and two primary strata

Execute all of:

```text
B1-F.1
B1-F.2
B1-F.3
B1-F.4
B1-F.5
B1-S32.1 .. B1-S32.5
B1-S33.1 .. B1-S33.5
```

Expected deliverables:

1. one exact four-stratum interface note;
2. one deterministic evaluator shared only where mathematics is identical;
3. S32 decision note;
4. S33 decision note;
5. compact exact evidence for any load-bearing calculations;
6. focused tests.

## Batch 1B — hard-stratum preparation

In parallel execute:

```text
B1-S34.1
B1-S34.2
B1-S35.1
B1-S35.2
```

The purpose is to expose structural invariants early, not to finish both
strata before S32/S33 feedback is available.

## Batch 1C — arbitrary Packet-B reduction

Execute:

```text
B2-R.1
B2-R.2
B2-R.3
B2-R.4 if the common-code reduction fails
```

Do not wait for B1 closure to discover whether the common-graph assumption is
actually removable.

## Batch 1D — Packet-A minimal system

Execute:

```text
A0.1
A0.2
A0.3
A25.1
A25.2
A25.3
A6.1
```

This is enough to make Packet A a concrete algebraic problem while keeping
A34 deferred.

## Batch 1E — review controls

Execute:

```text
D.1 hypothesis ledger skeleton
C.2 modular-discovery rules in the relevant scripts/tests
mandatory Glynn and Sylvester adversarial controls
```

These are lightweight safeguards attached to actual research outputs.

---

# 22. Explicit stop rules

The following work remains suspended unless a new theorem specifically
reopens it:

- larger scalar derivative/shadow dynamic programs;
- more uncoupled standard Koszul sweeps;
- more one-number Hilbert-function inequalities with no term labels;
- enlargement of the completed 130-case monomial-curve weight box;
- unit-weight-only Packet-B classification;
- unrestricted random point searches advertised as evidence of nonexistence;
- unrestricted `GL_6` scans;
- broad mixed-Glynn support enumeration without a theorem-defined component;
- exact-64 engineering before the 49-term equality packets are understood;
- generalized experiment managers, databases, job schedulers, registries, or
  evidence platforms.

A workstream also stops when it produces an exact survivor that satisfies all
its encoded hypotheses. Analyze the survivor before expanding the search.

---

# 23. What counts as substantive progress

The following count as substantive progress:

- closing one of S32/S33/S34/S35 for arbitrary characteristic-zero points and
  nonzero weights;
- finding an exact survivor to one of those strata;
- proving a cross-stratum theorem that removes at least two strata;
- proving an exhaustive reduction from arbitrary Packet B to finitely many
  branches;
- closing an uncovered arbitrary-Packet-B branch;
- proving a term-labelled Packet-A defect;
- finding a Packet-A survivor that exposes the missing invariant;
- closing Packet A or Packet B;
- promoting lower 50 after full audit.

The following do **not** count as substantive progress by themselves:

- a larger random sample with no survivor;
- another finite-field prime agreeing with the first two;
- a prettier implementation of an already available rank test;
- eliminating a narrowly parameterized family not forced by the endpoint
  equations;
- adding infrastructure unrelated to a theorem-facing calculation.

---

# 24. Promotion gate

The repository may state

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge50}
\]

only when every item below is satisfied.

```text
[ ] Every one of S32, S33, S34, S35 is excluded or subsumed by a valid
    cross-stratum theorem.
[ ] The common-graph assumption is removed by an exhaustive Packet-B
    structural reduction.
[ ] Every arbitrary Packet-B branch is excluded.
[ ] Packet A is excluded by permanent-specific term-labelled complementary-
    degree equations.
[ ] Every boundary introduced by chart choices is covered.
[ ] Nonzero weights and reduced-point hypotheses are handled correctly.
[ ] Every load-bearing computation has a characteristic-zero certificate.
[ ] Mandatory adversarial controls do not contradict any promoted lemma.
[ ] An independent proof-chain review has no fatal or major finding.
[ ] Focused tests and repository CI pass at one frozen exact commit.
```

Until then the status remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

---

# 25. Post-promotion package trigger

Do **not** pre-build the lower-51 program now. Once lower 50 is genuinely
promoted, immediately create a fresh frontier report answering:

1. which inequalities were strict versus endpoint equalities at 50 terms;
2. whether the 50-term endpoint has finitely many packet types or a broad new
   family;
3. whether the lower-50 proof supplies reusable slack toward 51;
4. whether exact 64 remains a realistic medium-term target or a different
   invariant is required.

Only then should the project choose between lower 51, a larger jump, exact 64,
or a general-`n` theorem.

---

# 26. Success criterion for this major package

The preferred success is a fully audited ordinary characteristic-zero lower-50
theorem.

A second scientifically successful outcome is an exact 49-term endpoint
survivor to all currently proved equality conditions that demonstrates a
missing invariant and sharply redirects the research.

A third acceptable intermediate outcome is closure of Packet B or Packet A
with the other packet reduced to one explicit, structurally meaningful
component.

Repeated closure of arbitrary restricted search families without advancing
one of these three outcomes is a signal to stop and re-evaluate the invariant,
not to increase search volume.
