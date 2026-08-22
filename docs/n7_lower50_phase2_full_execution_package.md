# `perm_7` lower-50 phase II full execution package

## Status and claim boundary

`ACTIVE LARGE EXECUTION PACKAGE — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Completed predecessor checkpoint: `170bd086a2c836c53160cf6b353e167b1228586c`  
Active branch: `agent/general-column-sign-rank`  
Active research PR: `#31`

The current proved ordinary characteristic-zero interval remains

\[
\boxed{49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.}
\]

The promotion target of this package is exactly

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50.}
\]

This package does not claim lower 50, exact rank 64, border rank, or a general
formula for `perm_n`.  It replaces the small first-checkpoint assignment with
a continuous theorem-facing program covering the complete remaining
lower-50 route.

The package contains **70 executable tasks**.  They are grouped by mathematical
dependency, not by calendar scheduling.  Work should continue across
checkpoints without requesting a new planning round unless one of the
following occurs:

1. an exact characteristic-zero survivor is found;
2. a load-bearing premise is disproved;
3. both equality packets are closed and lower 50 is ready for promotion.

No new manager, task database, registry, generalized solver platform, or
workflow service is authorized.  The package is a research specification,
not an architecture project.

---

# 0. Executive decision

## 0.1 What the predecessor actually completed

The predecessor package's immediate implementation checkpoint is complete.
The repository now has:

- the exact weighted common-graph middle-equality interface;
- the coupling condition
  \[
  \operatorname{rank}(E_4^TDE_3)=30;
  \]
- the degree-six target containment matrix
  \[
  \operatorname{rank}\begin{bmatrix}E_6\\S_6\end{bmatrix}
  =\operatorname{rank}E_6;
  \]
- a mixed-partial integrability argument giving
  \[
  H_Z(5)\leq40;
  \]
- exact controls, frozen data, tests, and a successful CI run.

This is substantial progress, but it is the entrance to B1 rather than the
closure of B1, arbitrary Packet B, or Packet A.

## 0.2 Mandatory boundary correction

The completed checkpoint correctly removed `(36,36)` but retained `(32,40)`
as target-compatible.  The separate correction note

```text
docs/n7_weighted_common_graph_checkpoint_correction.md
```

records why `(32,40)` is also impossible once `H_Z(5)<=40` is imposed:

\[
H_Z(4)=H_Z(5)=40<42
\]

would be a forbidden plateau in the Hilbert function of 42 reduced points.

The corrected surviving middle-rank pairs are therefore

\[
\boxed{(33,39),\ (34,38),\ (35,37).}
\]

They refine to six numerical Hilbert triples:

```text
S1 = (33,39,40)
S2 = (34,38,39)
S3 = (34,38,40)
S4 = (35,37,38)
S5 = (35,37,39)
S6 = (35,37,40)
```

No new computation may use the obsolete four-pair frontier.

## 0.3 Main research allocation

The default allocation of mathematical effort is:

```text
40%  B1: close the six weighted common-graph Hilbert strata
25%  B2: reduce and close arbitrary mixed graph-complement Packet B
25%  A:  build and close the all-rank-seven term-labelled packet
10%  exact certification, independent replay, adversarial review, promotion
```

The percentages are priority guidance only.  They do not introduce a
scheduler or resource manager.

## 0.4 Accepted terminal outcomes

The preferred terminal outcome is:

```text
LOWER50-PROVED:
Packet A is impossible and arbitrary Packet B is impossible.
```

A second scientifically valid terminal outcome is:

```text
EXACT-SURVIVOR:
An exact characteristic-zero packet satisfies every currently proved
endpoint, coupling, graph, and permanent-target equation.
```

An exact survivor is not automatically a 49-term permanent decomposition.
It must be checked against every reduction hypothesis.  Nevertheless, finding
one takes priority over additional exclusion searches because it identifies
the missing invariant or may lead to an actual decomposition.

Repeatedly excluding larger restricted families without a global reduction,
a theorem, or an exact survivor is not a terminal outcome.

---

# 1. Frozen mathematical input

The following facts are treated as the input boundary for this package.

## 1.1 Current lower and upper bounds

The unrestricted ordinary characteristic-zero interval is

\[
49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

The upper bound is supplied by the 64-term Glynn decomposition.  The lower
endpoint is already proved by the recursive shadow tower and complementary
catalectic arguments in the repository.

## 1.2 The two hypothetical 49-term equality packets

At a hypothetical identity

\[
\operatorname{perm}_7=\sum_{i=1}^{49}T_i,
\]

the slope-ten endpoint leaves exactly two global equality configurations.

### Packet A

All 49 terms have factor rank seven.  Their factor seven-planes form the
forced simple rank-seven multilinear matroid.  Unlabelled factor-plane
incidence and scalar derivative dimensions do not exclude this packet.

### Packet B

Seven rank-six equality terms span a direct 42-space.  The remaining 42 terms
are rank-seven graph complements.  Distinct complements need not coincide.
The pair packet only forces their intersections to be sufficiently small.

## 1.3 The load-bearing coupled equality

For the middle rectangular catalectic factorization

\[
B:\bigoplus_iK_i\to H_4,
\qquad
C:H_3^*\to\bigoplus_iK_i,
\]

Sylvester equality is equivalent to

\[
\boxed{\ker B\subseteq\operatorname{im}C.}
\]

No uncoupled dimension count can replace this condition.

## 1.4 Common-graph Packet-B interface

For a common set of 42 graph points and nonzero diagonal term weights `D`, the
small coupling condition is

\[
\boxed{\ker(E_4^T)\subseteq D\operatorname{im}(E_3)}
\]

or, on a middle-equality stratum,

\[
\boxed{\operatorname{rank}(E_4^TDE_3)=30.}
\]

Degree-six permanent containment is

\[
\boxed{
\operatorname{rank}\begin{bmatrix}E_6\\S_6\end{bmatrix}
=\operatorname{rank}E_6.}
\]

The diagonal weights do not change the degree-six point span, but they cannot
be normalized away from the coupling condition.

## 1.5 Corrected common-graph numerical frontier

The target-implied cap `H_Z(5)<=40`, monotonicity, and Hilbert-function
persistence leave the six numerical triples `S1` through `S6` listed above.
Their compatibility with reduced point geometry, nonzero weights, coupling,
and the permanent target is open.

## 1.6 Completed restricted Packet-B work

The repository already contains exact certificates for large proper
subfamilies, including:

- diagonal-sign packets;
- signed-coordinate and arbitrary invertible monomial transforms;
- elementary shears;
- several rank-one coordinate-shear families;
- coincident and overlap-one `(2,2)` closures;
- overlapping `(2,3)/(3,2)` projective support closures;
- overlapping `(2,4)/(4,2)` projective support closures;
- the allowed overlap-four-through-six dense families;
- repaired Laurent-torus boundary rows;
- two-permutation and protected-character exclusions;
- bounded monomial-curve common-graph controls.

These results are reusable lemmas.  They are not a substitute for a structural
reduction from arbitrary Packet B.

## 1.7 Completed route barriers

The following work is not to be repeated without a new theorem reopening it:

- larger scalar derivative or shadow dynamic programs;
- additional uncoupled standard Koszul sweeps;
- nonnegative direct sums of the existing scalar or standard Koszul ranks;
- direct transfer of the `perm_6` single-middle-layer proof;
- larger blind random finite-field searches;
- increasing the same monomial-curve weight box;
- unit-weight-only Packet-B classification;
- unrestricted `GL_6` scanning;
- tangent analysis based at the synchronized mixed-Glynn packet, which has
  exact coupling defect 35 and is not on the equality variety;
- unstructured enlargement of mixed-Glynn support families;
- an exact-64 program before the 49-term equality packets are resolved.

## 1.8 Packet-A negative control

The exact 49-term Glynn truncation satisfies the strongest factor packet,
degree-two containment, and the current scalar erasure inequalities, yet it
fails degree-six permanent containment and complementary-degree equality.
Therefore every Packet-A theorem must retain permanent-specific,
term-labelled cross-degree information.

---

# 2. Execution rules

## 2.1 Exactness hierarchy

Use the following hierarchy consistently.

1. **Exact characteristic-zero proof or certificate** is theorem-facing.
2. **Integer or rational nonzero minor** may certify a rank lower bound.
3. **A modular nonzero minor** may certify that the corresponding integer
   minor is nonzero in characteristic zero when the matrix has an explicit
   integral lift.
4. **Finite-field search** may locate components, pivots, candidate minors,
   or survivors, but cannot establish characteristic-zero emptiness by itself.
5. **Random search** is diagnostic only and is not sufficient for closure.
6. **Multivariate gcd equal to one** is not by itself a certificate that a
   collection of multivariate minors has no common zero.  Use exact ideal,
   saturation, univariate reduction, Bezout, resultant, or another valid
   certificate.

## 2.2 Minimal artifact rule

A theorem-facing computational result normally needs only:

```text
one proof note
one deterministic primary replay
one frozen payload when the computation is load-bearing
one focused test file
one independent replay or logically independent audit
```

Do not create empty manifests, duplicate ledgers, generalized experiment
registries, or planning JSON for their own sake.

## 2.3 Survivor-first rule

Any exact survivor satisfying all encoded equations stops the corresponding
exclusion workstream immediately.  The next action is to:

1. verify every reduction hypothesis;
2. reconstruct the full labelled packet;
3. test the exact polynomial identity;
4. determine whether the survivor is an actual decomposition or a witness
   that the encoded invariant is incomplete.

## 2.4 No checkpoint starvation

Completing one task below does not end the research phase.  The next
prerequisite-satisfied tasks launch automatically.  A new planning document is
not required between individual tasks, strata, or workstreams.

## 2.5 Substantive-progress test

The following count as substantive progress:

- globally removing one of the six B1 Hilbert triples;
- finding an exact B1 survivor;
- proving a common-code or finite-exception reduction for arbitrary Packet B;
- closing an exception class produced by that reduction;
- proving a permanent-specific Packet-A block defect or normal form;
- finding an exact Packet-A survivor;
- closing Packet A or Packet B;
- promoting lower 50.

The following do not count by themselves:

- more random samples with the same target increment;
- one additional finite field;
- a larger instance of an already closed restricted family;
- a new solver wrapper without a new mathematical interface;
- a rank computation omitting either the weights, the coupling equation, or
  the permanent target.

---

# 3. Master dependency map

```text
P0 corrected boundary
  |
  +--> B1F common-graph foundations
  |      |
  |      +--> B1S six refined strata
  |              |
  |              +--> B1-CLOSED or B1-SURVIVOR
  |
  +--> B2 arbitrary Packet-B structural reduction
  |      |
  |      +--> reuse B1 and the existing restricted certificate library
  |              |
  |              +--> B2-CLOSED or B2-SURVIVOR
  |
  +--> A term-labelled all-rank-seven module
         |
         +--> A-CLOSED or A-SURVIVOR

A-CLOSED + B2-CLOSED
  |
  +--> exact-head audit and LOWER50-PROVED
```

The B1, B2-foundation, and Packet-A module lanes should run in parallel where
their prerequisites permit.  B2 must not wait for every B1 calculation before
attempting the structural synchronization theorem.  Conversely, B2 may use a
completed B1 theorem as soon as one is available.

---

# 4. Work package P0 — repair and freeze the correct B1 frontier

## P0-01 — record the finite-point plateau correction

**Status:** completed by
`docs/n7_weighted_common_graph_checkpoint_correction.md`.

**Result to retain:** `(32,40)` and `(36,36)` are both incompatible with the
full target-implied Hilbert conditions.  The surviving rank pairs are
`(33,39)`, `(34,38)`, and `(35,37)`.

## P0-02 — update the executable interface inventory

Update together:

```text
docs/n7_weighted_common_graph_interface.md
scripts/n7_weighted_common_graph_interface.py
data/n7_weighted_common_graph_interface.json
tests/test_n7_weighted_common_graph_interface.py
```

The code must distinguish:

```text
middle-equality numerical pairs
H3/H4 geometric profile controls
target-compatible rank pairs
six target-compatible numerical Hilbert triples
```

**Definition of done:** no repository output describes `(32,40)` as
compatible with `H5<=40`.

## P0-03 — replay degrees five and six for every curve-union control

Extend the existing exact/modular control table from `(H3,H4)` to

```text
(H3,H4,H5,H6).
```

The purpose is classification, not exclusion.  Record exactly which controls
leave the target-implied `H5<=40` locus.

**Output:** a deterministic payload and a short correction in the interface
note.  Do not create a separate broad experiment framework.

## P0-04 — freeze the six refined numerical triples

Add a machine-checked constant inventory:

```text
S1=(33,39,40)
S2=(34,38,39)
S3=(34,38,40)
S4=(35,37,38)
S5=(35,37,39)
S6=(35,37,40)
```

The inventory is numerical only.  Do not label all six geometrically
realizable until that is proved.

## P0-05 — add Hilbert-persistence regressions

Tests must reject:

- `(36,36,...)`;
- `(32,40,40)`;
- `(33,39,39)`;
- any generated sequence with `H(d)=H(d+1)<42` followed by later growth.

Include at least one valid non-plateau control so the test cannot pass by
rejecting every sequence.

## P0-06 — rerun the focused and repository CI gates

Required checks:

```text
weighted common-graph frozen replay
focused unit tests
English-only scan
full configured exact-bound workflow
```

**Definition of done:** all corrected artifacts agree at one exact commit.

## P0-07 — freeze the corrected starting commit

Update the research log with:

- the predecessor checkpoint completion;
- the corrected three rank pairs;
- the six refined triples;
- the exact commit and CI result;
- a statement that lower 50 remains open.

This commit is the base for every B1 theorem-facing calculation below.

---

# 5. Work package B1F — weighted common-graph foundations

The goal of B1F is to replace one large undifferentiated polynomial system by
six exact finite-type geometric problems without losing the diagonal weights
or permanent targets.

## B1F-01 — classify admissible Hilbert first differences

For each `S1` through `S6`, determine every possible first-difference sequence
compatible with:

- 42 reduced points in projective six-space;
- the displayed values in degrees three through five;
- Macaulay growth;
- eventual value 42;
- nondegeneracy required by the graph model.

Use exact integer enumeration of O-sequences only where necessary.

**Output:** `docs/n7_b1_hilbert_triples.md` and, if finite enumeration is
load-bearing, one compact script/payload/test set.

**Gate:** no later stratum solver may silently assume a unique Hilbert
continuation unless B1F-01 proves it.

## B1F-02 — determine the possible saturated Betti tables

For every admissible first-difference sequence, derive or enumerate the
minimal graded Betti-table possibilities of the point ideal through the
degrees needed by `E3`, `E4`, `E5`, and `E6`.

The objective is not a full Hilbert-scheme classification.  Retain only the
syzygies that affect:

- degree-three and degree-four relation spaces;
- the multiplication maps into degree five and six;
- the permanent target quotient.

**Decisive output:** a finite list of algebraic strata or a theorem showing
that one uniform relation-module description covers several triples.

## B1F-03 — separate reduced-point components from formal Hilbert data

Determine which Betti/Hilbert candidates are realizable by 42 distinct
reduced graph points.  Use saturation, Jacobian, or exact incidence arguments
as appropriate.

Do not equate an abstract O-sequence with a realizable graph configuration.

**Outcome labels:**

```text
REALIZABLE-COMPONENT
FORMAL-ONLY-EXCLUDED
UNRESOLVED-COMPONENT
```

A component is promoted as realizable only with an exact characteristic-zero
construction or proof.

## B1F-04 — construct the degree-three/four relation module

For a point configuration `Z`, define the exact relation spaces and
multiplication maps controlling the inclusion

\[
\ker(E_4^T)\subseteq D\operatorname{im}(E_3).
\]

Replace moving kernel bases by basis-free maps whenever possible.  Candidate
forms include:

- Fitting ideals;
- maximal minors of a universal relation matrix;
- exterior-power incidence equations;
- quotient maps on fixed pivot charts.

**Output:** a minimal symbolic interface with a deterministic evaluator.

## B1F-05 — eliminate or parameterize the diagonal weights

Treat

\[
D=\operatorname{diag}(d_1,\ldots,d_{42}),
\qquad d_i\ne0,
\]

as a torus variable, not as unit weights.

For each Hilbert stratum, decide whether the existence of `D` can be expressed
as:

- a linear system after logarithmic or relation-space reduction;
- a torus orbit-incidence condition;
- a finite collection of determinant equations;
- an exact quotient of relation modules.

Saturate by

\[
\prod_i d_i
\]

before drawing conclusions about nonzero weights.

**Decisive outputs:**

```text
WEIGHTS-IMPOSSIBLE
WEIGHTS-PARAMETERIZED
WEIGHTED-INCIDENCE-UNRESOLVED
```

## B1F-06 — compress degree-six permanent containment

The raw target equation uses a `42 x 924` point matrix and seven target rows.
Derive the smallest equivalent block system on each Hilbert stratum by using:

- the point ideal in degrees five and six;
- row/column torus multidegrees;
- the seven missing-row target blocks;
- quotient bases fixed by the Betti data;
- multiplication from degree five to degree six.

The compressed test must be equivalent to

\[
S_6\subseteq\operatorname{rowspan}E_6,
\]

not merely necessary on random evaluations.

**Output:** exact symbolic target equations and a deterministic replay.

## B1F-07 — derive all additional integrability consequences

The existing argument gives `H5<=40`.  Determine whether the same gradient
compatibility imposes stronger restrictions on:

- `H6`;
- the support size of minimal sixth-power representations;
- the degree-five relation module;
- the possible Betti tables;
- the diagonal-weight incidence.

A stronger theorem that eliminates one or more triples takes priority over
full elimination of their universal ideals.

Do not assume a stronger cap without proof.

## B1F-08 — build an exact pivot-chart cover

For each surviving geometric component, choose a finite set of pivot charts
covering the relevant open locus.  Every chart must preserve:

- point distinctness;
- reducedness;
- graph nondegeneracy;
- nonzero weights;
- the prescribed Hilbert ranks.

Use symmetry to reduce duplicate charts, but record why the chosen charts
cover the full locus.

**Forbidden shortcut:** solving one convenient chart and calling the stratum
closed.

## B1F-09 — establish the reconnaissance-to-proof pipeline

Finite fields may be used to:

- identify likely components;
- select pivots and minors;
- detect exact survivors;
- estimate codimension;
- propose elimination identities.

For every candidate theorem, specify in advance how it will be lifted to
characteristic zero:

```text
exact rational elimination
integer nonzero minor
univariate resultant or Bezout identity
saturated ideal over Q
controlled number-field certificate
pure structural proof
```

Add negative controls that fail if `D`, coupling, reducedness, or permanent
target equations are omitted.

---

# 6. Work package B1S — close the six refined common-graph strata

Each stratum has two tasks.  The first task constructs and reduces the exact
geometric/weight incidence.  The second solves it jointly with the permanent
target and returns a theorem-facing outcome.

A stratum is not closed by a finite sample, one component, one pivot chart, or
one choice of weights.

## B1S-01 — `S1=(33,39,40)` structural reduction

Determine all reduced point-ideal components and Betti types realizing the
numerical triple.  Construct the corresponding weight-incidence equations and
compressed degree-six target blocks.

This stratum has the smallest degree-four relation defect among the surviving
triples and saturates the `H5<=40` cap.  Exploit that rigidity before using a
large solver.

**Output:** a finite component/chart list with exact equations.

## B1S-02 — `S1=(33,39,40)` exact decision

For every component from B1S-01, solve

```text
Hilbert stratum
+ reduced distinct graph points
+ nonzero diagonal weights
+ rank(E4^T D E3)=30
+ degree-six permanent containment
```

Return exactly one of:

```text
S1-CLOSED
S1-SURVIVOR
```

A survivor must include exact coordinates and weights over a characteristic-
zero field and a deterministic check of every equation.

## B1S-03 — `S2=(34,38,39)` structural reduction

Classify the components with one-step growth from 38 to 39.  Track the new
degree-five relation explicitly; it may couple the four-dimensional
`ker(E4^T)` to the target quotient more tightly than a generic rank condition.

**Output:** exact universal relation and target matrices per component.

## B1S-04 — `S2=(34,38,39)` exact decision

Solve the complete weighted target system on all components and charts.
Return `S2-CLOSED` or an exact `S2-SURVIVOR`.

If elimination produces a common factor supported only on a coordinate or
weight boundary, saturate and treat that boundary separately rather than
claiming dense-torus closure.

## B1S-05 — `S3=(34,38,40)` structural reduction

Classify the two-step degree-five growth and compare its relation module with
S2.  Determine whether S2 and S3 are adjacent components of one universal
family or genuinely different Betti strata.

Reuse B1F infrastructure; do not duplicate a solver for the same universal
matrix.

## B1S-06 — `S3=(34,38,40)` exact decision

Solve coupling and degree-six containment jointly.  Return `S3-CLOSED` or an
exact `S3-SURVIVOR`.

If a survivor exists only on a specialization where the Hilbert triple drops,
reclassify it into the correct stratum rather than retaining it as an S3
solution.

## B1S-07 — `S4=(35,37,38)` structural reduction

This is the minimal-growth continuation of `(35,37)`.  Analyze whether the
successive one-dimensional growth forces a curve-like, almost-minimal-degree,
or otherwise rigid point configuration.

The task is to prove the relevant structure, not to assume the monomial-curve
controls are universal.

## B1S-08 — `S4=(35,37,38)` exact decision

Solve the full weighted target system on the complete S4 locus.  Return
`S4-CLOSED` or an exact `S4-SURVIVOR`.

An exact dual functional separating one permanent target from every S4 point
span is an acceptable closure certificate if its universality is proved.

## B1S-09 — `S5=(35,37,39)` structural reduction

Classify the degree-five growth-two locus and the possible relation-module
extensions from S4.  Determine whether the additional degree-five direction
creates or destroys solutions to the diagonal-weight incidence.

**Output:** finite exact component inventory and compressed target maps.

## B1S-10 — `S5=(35,37,39)` exact decision

Return `S5-CLOSED` or an exact `S5-SURVIVOR` after solving all components and
boundary strata.

Use degree seven only if degree six leaves a genuine exact survivor.

## B1S-11 — `S6=(35,37,40)` structural reduction

Classify the cap-saturating continuation of `(35,37)`.  Compare it with S5 and
S4 through specialization and semicontinuity.  A theorem showing that every
S6 solution specializes to a previously closed locus is acceptable only if
all equations and nonvanishing conditions survive the specialization.

## B1S-12 — `S6=(35,37,40)` exact decision

Return `S6-CLOSED` or an exact `S6-SURVIVOR`.

Do not infer characteristic-zero emptiness solely from smooth finite-field
fibres.  Supply an exact proof or ideal certificate.

## B1S-13 — degree-seven fallback for exact B1 survivors only

If one or more of S1--S6 has an exact degree-six survivor, add the smallest
term-labelled degree-seven equation needed to test the actual Packet-B
identity.

Do not build a universal degree-seven system before a degree-six survivor
exists.  The fallback must preserve the same weights and graph points.

**Outcome:** survivor killed by an exact degree-seven certificate, or upgraded
to a stronger exact survivor.

## B1S-14 — assemble the weighted common-graph theorem

When all six triples are decided, publish exactly one of:

```text
B1-CLOSED:
No weighted common-graph Packet-B equality packet exists in characteristic
zero.
```

or

```text
B1-SURVIVOR:
An exact characteristic-zero common-graph packet satisfies every proved
middle, coupling, graph, and permanent-target condition.
```

The theorem note must list every stratum, component, boundary, exact
certificate, and survivor check.  B1-CLOSED alone does not close arbitrary
Packet B.

---

# 7. Work package B2 — arbitrary mixed graph-complement Packet B

The goal is to move from a common point code to all 42 independently varying
graph complements allowed by the endpoint theorem.

## B2-01 — write the full mixed Packet-B variables once

Choose exact coordinates for:

- the seven direct rank-six terms;
- the 42 graph-complement seven-planes;
- their factor bases;
- their nonzero term coefficients;
- the 35 degree-three/four row-subset blocks;
- the permanent target blocks.

Quotient only by common changes of basis and scalings whose effect is proved.
Do not normalize away relative term weights or graph moduli.

**Output:** a concise mathematical model, not a general-purpose tensor
framework.

## B2-02 — factor Sylvester equality block by block

Derive the exact small inclusion or rank condition in every one of the 35
complementary row-subset blocks.  Identify which maps are shared and which are
term-specific when the graph complements differ.

The result must specialize exactly to

\[
\ker(E_4^T)\subseteq D\operatorname{im}(E_3)
\]

in the common-graph case.

## B2-03 — prove or disprove block synchronization

Test the central structural proposition:

> Simultaneous equality in all 35 blocks forces the 42 mixed graph terms to
> share a common point code/common graph model, up to a finite list of
> explicit exceptional strata.

A proof may use:

- overlapping row-subset consistency;
- term-labelled relation transport;
- cocycle equations;
- shared kernel/image flags;
- permanent torus weights;
- pairwise graph-plane intersection constraints.

If the proposition is false, produce an exact counterexample and identify the
extra moduli that survive.

## B2-04 — construct the finite-exception alternative

If complete synchronization fails, prove a finite structural reduction of the
form

```text
common-code locus
OR explicit exception class E1
OR ...
OR explicit exception class Ek.
```

Each exception class must have:

- a mathematical definition;
- a finite-dimensional exact parameterization;
- the equations inherited from all 35 blocks;
- a coverage test against the existing certificate library.

Do not replace a failed theorem with unrestricted `GL_6` brute force.

## B2-05 — exploit pairwise graph-plane geometry

Use the endpoint condition on pairwise graph-complement intersections to
control the ranks of relative graph maps.  Determine which rank-drop,
overlap, or shared-kernel patterns are compatible with simultaneous block
equality.

The objective is a theorem reducing relative transforms to a small set of
rank patterns, not a random scan of transform matrices.

## B2-06 — build a nonduplicative certificate coverage map

Map every structurally exposed exception class to the exact certificates
already in the repository:

```text
monomial and signed-coordinate transforms
elementary and coordinate shears
rank-one support closures
coincident and overlap-one families
overlapping (2,3)/(3,2)
overlapping (2,4)/(4,2)
overlap four through six
Laurent boundary rows
permutation-character obstructions
```

Record `COVERED`, `PARTIALLY COVERED`, or `NEW` with exact file references.
This is a short coverage document, not a new tracker application.

## B2-07 — reduce the common-code locus to B1

Prove that every synchronized/common-code mixed packet satisfies precisely the
B1 hypotheses, including the same nonzero weights and permanent target
conditions.  Then import B1-CLOSED or the exact B1 survivor without weakening
its claim boundary.

## B2-08 — close every structurally exposed rank-one exception

Only after B2-04/B2-05 exposes a rank-one class may new rank-one computation
be launched.  Reuse existing support-closure and boundary certificates before
adding cases.

For each genuinely new class, return an exact characteristic-zero closure or
survivor.  Do not enumerate larger supports merely because they exist.

## B2-09 — treat rank-two or higher perturbations only when forced

If the structural reduction exposes rank-two or higher relative transforms,
first derive their canonical support/kernel/image data and the exact block
conditions.  Then classify a finite set of strata.

An unrestricted parameter sweep is forbidden.  The task ends when the
structurally exposed strata are closed or an exact survivor is found.

## B2-10 — combine mixed weights, coupling, and permanent targets

For every remaining exception class, solve the equations jointly:

```text
all 35 Sylvester-equality blocks
+ nonzero term coefficients
+ graph complement and intersection conditions
+ degree-six permanent target containment
+ degree-seven identity only for exact degree-six survivors
```

A calculation omitting any one of these interfaces is diagnostic only.

## B2-11 — reconstruct and test every exact mixed survivor

For any exact survivor:

1. reconstruct all 49 Chow terms;
2. verify factor ranks and graph-complement geometry;
3. verify all middle block equations;
4. verify degree-six and degree-seven target equations;
5. expand the exact polynomial difference from `perm_7`;
6. record whether the result is an actual decomposition or an incomplete-
   invariant witness.

## B2-12 — publish the arbitrary Packet-B decision

Return exactly one of:

```text
B2-CLOSED:
Every Packet-B equality configuration is impossible in characteristic zero.
```

or

```text
B2-SURVIVOR:
An exact mixed Packet-B configuration satisfies every currently proved
condition.
```

A B2-CLOSED theorem must explicitly cover the common-code locus and every
exception class.  It is one of the two theorem gates for lower 50.

---

# 8. Work package A — all-rank-seven Packet A

Packet A cannot be closed by factor incidence, scalar Hilbert functions, or
the quadratic interface alone.  This work package builds the smallest
term-labelled permanent-specific module capable of distinguishing an actual
identity from the 49-term Glynn counterexample.

## A-01 — define the minimal term-labelled data

For each term `T_i`, retain the labelled derivative spaces needed for the
first candidate interface:

\[
D_2(T_i),\qquad D_5(T_i),\qquad D_6(T_i).
\]

Record the termwise multiplication and differentiation maps between them.
Do not begin with every derivative degree.

## A-02 — construct the degree `2/5` relation pairing

Build the exact term-labelled relation spaces in degrees two and five and the
complementary pairing forced by

\[
\sum_iT_i=\operatorname{perm}_7.
\]

The map must distinguish relations belonging to different terms even when
their unlabelled spans coincide.

**Output:** a basis-free module or block matrix with a one-term cap and a
permanent target rank.

## A-03 — add degree-six permanent containment

Construct the smallest exact block test equivalent to

\[
D_6(\operatorname{perm}_7)
\subseteq\sum_iD_6(T_i)
\]

on the Packet-A factor packet.  Split by the seven omitted-row multidegrees so
that failure in one target block is visible.

## A-04 — combine the `2/5` and degree-six interfaces

Form a genuinely coupled module in which the same term labels and coefficient
variables appear in both complementary-degree relations and degree-six target
containment.

The desired gain must come from compatibility, not from adding two rank
inequalities side by side.

## A-05 — decompose by permanent torus weights

Use row and column multidegrees to split the coupled module into small exact
weight blocks.  Determine:

- target rank per block;
- one-term image and relation caps;
- cross-block compatibility imposed by a single factor seven-plane;
- which blocks are already decisive.

The output should permit exact sparse computation without materializing one
huge matrix.

## A-06 — derive a sharp one-term or few-term capacity theorem

For a rank-seven Chow term, prove the maximum contribution to the coupled
module.  Then investigate whether two or more terms sharing incidence data
have a strictly subadditive joint cap.

A successful theorem should force a positive global defect for every
49-term Packet-A configuration.

## A-07 — use the forced multilinear matroid only where load-bearing

Translate the endpoint factor-plane conditions into exact restrictions on the
coupled blocks:

- pairwise transversality;
- seven-dimensional increments;
- total 49-dimensional factor span;
- simplicity of the multilinear matroid.

Do not infer tensor-split or column-uniform normal forms from the abstract
matroid alone; the repository contains an exact Sylvester-equality
counterexample to that implication.

## A-08 — prove a permanent-specific structural lemma or block defect

Target one of the following decisive forms:

```text
one permanent target block must be missing
OR a complementary-degree relation cannot be transported termwise
OR equality forces a normal form incompatible with the permanent
OR the coupled module has rank exceeding the 49-term cap
```

A theorem valid only for a tensor-split or line-packet subfamily is an
intermediate lemma, not A-CLOSED.

## A-09 — maintain mandatory adversarial controls

Every proposed Packet-A lemma must be tested against:

1. the exact 49-term Glynn truncation;
2. the non-tensor-split Sylvester-equality configuration;
3. forced-line finite-field packets from the existing cross-degree search;
4. the full 64-term Glynn decomposition when the statement should permit a
   valid decomposition.

A lemma contradicted by a control is rejected or narrowed before further
computation.

## A-10 — run bounded reconnaissance on the actual coupled locus

Use finite fields only after A-01 through A-05 define the full coupled
conditions.  Search for:

- exact survivors;
- repeated rank defects;
- candidate separating minors;
- small normal forms;
- component dimensions.

Do not repeat the earlier random search that omitted the labelled coupling.

## A-11 — certify the characteristic-zero decision or survivor

Lift any proposed exclusion to exact arithmetic.  Acceptable outputs include:

- a pure block-defect theorem;
- an integer minor valid on every structural chart;
- a saturated ideal certificate over `Q`;
- a finite exact normal-form classification;
- an exact characteristic-zero survivor.

## A-12 — publish the Packet-A decision

Return exactly one of:

```text
A-CLOSED:
No all-rank-seven 49-term equality packet can equal perm_7.
```

or

```text
A-SURVIVOR:
An exact characteristic-zero Packet-A configuration satisfies every encoded
term-labelled cross-degree condition.
```

A-CLOSED is the second theorem gate for lower 50.

---

# 9. Work package X — parallel theorem and survivor lanes

These four tasks run only when they share the same exact interfaces with B1,
B2, or A.  They are not permission to open unrelated research programs.

## X-01 — search for a universal dual separator

Attempt to construct an exact linear or module-valued functional that:

- vanishes on every allowed 49-term equality packet contribution;
- is nonzero on at least one permanent target block.

A successful separator may close several B1 strata or both packets without a
full component classification.

## X-02 — derive a global coupled inequality

Use the same term-labelled relation modules to seek a universal inequality
strictly stronger than the slope-ten equality at `N=49`.

The inequality must exploit compatibility across degrees.  Another scalar
profile inequality or uncoupled direct sum is outside scope.

## X-03 — maintain an exact survivor-first construction lane

Rather than only proving emptiness, actively attempt to solve the exact
coupled equations on the lowest-dimensional components.  A survivor can be
more informative than thousands of exclusions.

The lane is bounded by the same six B1 triples and structurally reduced Packet
A/B loci.  It is not a general numerical optimization over all 49 Chow terms.

## X-04 — perform targeted literature reconciliation

Search the literature only for a concrete theorem needed by an active task,
such as:

- Hilbert functions or Betti tables of reduced points with the six triples;
- torus incidence between evaluation codes;
- simultaneous Waring-gradient integrability;
- multilinear matroid realization;
- term-labelled apolar or syzygy modules.

Record exact theorem statements, hypotheses, field assumptions, and how they
map to repository notation.  Do not start a broad literature survey detached
from an active proof obligation.

---

# 10. Work package Q — exact review, CI, and promotion

## Q-01 — maintain a claim/source map

For every promoted lemma, record:

```text
statement
characteristic
ordinary versus border scope
input commit
proof or computation file
frozen payload if any
independent replay
negative control
claim boundary
```

Use the existing research log and proof notes.  Do not build a new database.

## Q-02 — independent B1 replay

Every load-bearing B1 finite calculation receives a logically independent
replay.  The replay should differ in at least one meaningful way:

- basis construction;
- elimination order;
- direct versus quotient matrix;
- exact rational versus integer/modular minor;
- independent implementation of the Hilbert or relation module.

## Q-03 — independent B2 replay

Replay the structural coverage of every Packet-B exception class.  Verify that
no existing certificate is imported outside its stated support, boundary, or
transform assumptions.

## Q-04 — independent Packet-A replay

Reconstruct the coupled module and decisive rank/ideal certificate without
reusing opaque intermediate matrices from the primary implementation.

## Q-05 — run adversarial mathematical reviews

Perform separate reviews of:

1. the corrected Hilbert frontier and B1 closure;
2. the arbitrary Packet-B reduction and exception coverage;
3. the Packet-A coupled module and controls;
4. the final implication from A-CLOSED and B2-CLOSED to lower 50.

Classify findings as fatal, major, minor, or editorial.  Repair fatal and major
findings before promotion.

## Q-06 — freeze one exact theorem-facing commit

At one exact HEAD, run:

```text
all focused deterministic replays
all focused tests
full repository tests configured by CI
English-only policy
frozen payload comparisons
```

Record the exact commit and workflow result.  Historical success on earlier
heads is not sufficient for the final theorem.

## Q-07 — prepare the minimal promotion packet

The final lower-50 packet should contain:

```text
one theorem note combining the endpoint and packet exclusions
one exact-head review boundary
one independent audit note
links to load-bearing replay artifacts
updated README / STATUS / research log statements
```

Do not package unrelated historical data or large upstream proof bundles.

## Q-08 — promote the correct terminal conclusion

Promote

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\geq50
\]

only if both `A-CLOSED` and `B2-CLOSED` are proved at the frozen head.

If an exact survivor remains, do not promote lower 50.  Instead publish the
survivor, the equations it satisfies, the exact condition still missing, and
the revised route.

---

# 11. Immediate launch batch

The following work is authorized immediately and should proceed without a new
planning round.

## Lane 1 — corrected B1 foundation

```text
P0-02 through P0-07
B1F-01 through B1F-06
```

First deliverables:

```text
corrected executable six-triple inventory
complete H3/H4/H5/H6 control replay
admissible Hilbert first differences
relevant Betti/relation-module inventory
weight-torus incidence equations
compressed degree-six target equations
```

After B1F-06, launch B1S-01, B1S-03, B1S-05, B1S-07, B1S-09, and B1S-11 as
soon as their component descriptions are available.  Do not wait for all six
structural tasks to finish before solving the first ready stratum.

## Lane 2 — arbitrary Packet-B reduction

```text
B2-01 through B2-06
```

This lane should try to prove synchronization or expose a finite exception
list before any new transform enumeration.

## Lane 3 — Packet-A coupled module

```text
A-01 through A-05
A-09
```

This lane can proceed independently of B1.  Its first checkpoint is a working
term-labelled `2/5 + degree-six` block module that rejects the 49-term Glynn
control for the correct permanent-specific reason while remaining compatible
with valid controls.

## Lane 4 — review support

```text
Q-01
X-01
```

The dual-separator lane should reuse the exact blocks from Lane 1 or Lane 3;
it must not create a separate abstraction layer.

---

# 12. Milestones and automatic continuation

## M0 — corrected boundary frozen

Completion requires P0-02 through P0-07.  The active B1 frontier is six
Hilbert triples, not four rank pairs.

**Automatic next action:** continue B1F and launch all ready B1S tasks.

## M1 — common-graph algebra reduced

Completion requires B1F-01 through B1F-09.

**Automatic next action:** solve every S1--S6 component; do not issue another
planning document.

## M2 — B1 decided

Completion requires B1S-01 through B1S-14.

**Automatic next action:** import B1 into B2-07 and close every remaining B2
exception.

## M3 — arbitrary Packet B structurally reduced

Completion requires B2-01 through B2-06.

**Automatic next action:** B2-07 through B2-12.

## M4 — Packet B decided

Completion requires `B2-CLOSED` or an exact B2 survivor.

**Automatic next action:** if closed, focus resources on Packet A; if a
survivor exists, reconstruct it before further exclusions.

## M5 — Packet-A module operational

Completion requires A-01 through A-05 and successful mandatory controls.

**Automatic next action:** A-06 through A-12.

## M6 — both packets decided

Completion requires `A-CLOSED` and `B2-CLOSED`, or an exact survivor that
prevents one of those conclusions.

**Automatic next action:** Q-02 through Q-08.

## M7 — lower 50 promoted or route revised

The phase ends with either a frozen lower-50 theorem or an exact survivor and
a precise revised invariant target.

---

# 13. Stop and pivot rules

## 13.1 Stop immediately on an exact survivor

Do not keep searching for exclusions after an exact survivor is found in the
same locus.  Reconstruct and test it first.

## 13.2 Stop a computational family when it ceases to answer a theorem question

A family is suspended when:

- it repeats an already observed flat target increment;
- it is not produced by the structural reduction;
- its parameters grow without reducing the unresolved locus;
- its output cannot be lifted to a characteristic-zero statement;
- it omits one of the load-bearing equations.

## 13.3 Pivot from elimination to theorem when repeated structure appears

If several strata produce the same minor, relation transport, or target
defect, stop separate enumeration and prove the common structural lemma.

## 13.4 Pivot from degree six to degree seven only for a real survivor

Do not add degree-seven complexity to an already empty degree-six locus.

## 13.5 Do not broaden the target prematurely

Until lower 50 is decided, do not launch:

- an exact-64 classification;
- a general-`n` equality-packet program;
- arbitrary border-rank degeneration searches;
- a new universal algebraic-geometry software layer.

---

# 14. Promotion gate

The statement

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50}
\]

may be promoted only when all boxes are checked:

```text
[ ] The weighted common-graph checkpoint boundary is corrected and frozen.
[ ] Every common-graph Hilbert triple S1--S6 is exactly decided or subsumed by
    a stronger arbitrary-Packet-B theorem.
[ ] Arbitrary Packet B is excluded, including all structurally exposed
    exception classes, arbitrary permitted term weights, and all required
    permanent-target equations.
[ ] Packet A is excluded by a permanent-specific term-labelled cross-degree
    theorem.
[ ] No load-bearing conclusion relies only on finite-field absence, random
    search, one pivot chart, unit weights, or an invalid multivariate-gcd
    inference.
[ ] Every load-bearing finite computation has a deterministic primary replay
    and a logically independent check.
[ ] Adversarial review finds no unrepaired fatal or major defect.
[ ] Full theorem-facing CI passes at one exact frozen commit.
[ ] README, STATUS, and the research log state the same characteristic-zero
    ordinary-rank claim and do not imply a border-rank result.
```

Until then, the repository status remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.}
\]

---

# 15. Conditional continuation after lower 50

These four tasks activate only after Q-08 promotes lower 50.  They prevent the
project from stopping at publication cleanup, but they do not authorize an
immediate exact-64 campaign.

## C51-01 — derive the exact `N=50` slack equations

Recompute the slope-ten and Sylvester budgets at 50 terms.  Identify which
local inequalities can now have slack and which endpoint equalities remain
forced.

## C51-02 — classify the finite near-equality packet types

Use the exact slack budget to derive a finite list of 50-term structural
packets.  Do not assume the two 49-term equality packets persist unchanged.

## C51-03 — run a coupled capacity audit for lower 51

Evaluate the already built B1/B2/A coupled modules on the 50-term packet list.
Determine whether they can in principle prove lower 51 or whether a new
invariant is required.

## C51-04 — freeze one evidence-based lower-51 route

Publish a next target only after C51-01 through C51-03 identify a concrete
packet and a quantified obstruction.  Do not replace the present package with
another broad list detached from the new endpoint geometry.

---

# 16. Definition of phase success

The preferred successful output is an exact ordinary characteristic-zero
lower-50 theorem.  A second successful output is an exact survivor that shows
why the current endpoint equations are insufficient and identifies the
missing permanent-specific invariant.

The package is deliberately larger than the predecessor checkpoint: it covers
the boundary repair, all six common-graph strata, the structural transition to
arbitrary Packet B, the complete Packet-A coupled module, survivor handling,
independent replay, adversarial review, promotion, and the first conditional
post-lower-50 analysis.

It remains intentionally narrow in architecture.  Progress is measured by
mathematical loci closed, exact survivors found, and theorems promoted—not by
the number of scripts, cases, or framework components added.
