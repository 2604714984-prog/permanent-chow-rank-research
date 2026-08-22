# `perm_7` lower-50 decisive large task package

## Status and claim boundary

`ACTIVE RESEARCH PACKAGE — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Input research snapshot: `170bd086a2c836c53160cf6b353e167b1228586c`  
Active research PR: `#31`  
Active branch: `agent/general-column-sign-rank`

The current ordinary characteristic-zero interval remains

\[
\boxed{49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

The sole theorem-promotion target of this package is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50}.
\]

This package does not claim lower 50, exact rank 64, border rank, or a general
formula for `perm_n`. It replaces the smaller first-checkpoint plan with a
continuous, decisive program covering the complete remaining common-graph
problem, the passage to arbitrary Packet B, Packet A, and final theorem audit.

## 1. Why a larger package is now justified

The previous plan deliberately stopped after its first implementation
checkpoint. That checkpoint has now been completed:

1. the seven numerical middle-equality rank pairs were identified;
2. the weighted coupling condition was compressed to
   `rank(E4^T D E3)=30`;
3. degree-six permanent containment was written as
   `rank(stack(E6,S6))=rank(E6)`;
4. the target condition was shown to imply `H_Z(5)<=40`;
5. deterministic controls and focused tests were frozen;
6. CI passed at the completed checkpoint head.

The checkpoint did not close weighted common-graph Packet B. It exposed the
correct finite relation-defect range and therefore permits a substantially
larger, more concrete task package.

## 2. Mandatory correction to the completed checkpoint

The strict-growth correction in
`docs/n7_weighted_common_graph_strict_growth_correction.md` is part of the
starting boundary of this package.

For 42 distinct reduced projective points, the Hilbert function grows
strictly until it reaches 42. Combining this with `H_Z(5)<=40` removes both

```text
(32,40) and (36,36).
```

Exactly three degree-three/degree-four rank pairs remain:

```text
(33,39), (34,38), (35,37).
```

They refine into six degree-five cases:

| case ID | `H_Z(3)` | `H_Z(4)` | `H_Z(5)` | `dim R_3` | `dim R_4` | `dim R_5` |
|---|---:|---:|---:|---:|---:|---:|
| `B1-33-39-40` | 33 | 39 | 40 | 9 | 3 | 2 |
| `B1-34-38-39` | 34 | 38 | 39 | 8 | 4 | 3 |
| `B1-34-38-40` | 34 | 38 | 40 | 8 | 4 | 2 |
| `B1-35-37-38` | 35 | 37 | 38 | 7 | 5 | 4 |
| `B1-35-37-39` | 35 | 37 | 39 | 7 | 5 | 3 |
| `B1-35-37-40` | 35 | 37 | 40 | 7 | 5 | 2 |

Here

\[
C_d=\operatorname{im}E_d\subset k^{42},
\qquad
R_d=C_d^\perp=\ker(E_d^T).
\]

The relation spaces form the nested flag

\[
R_5\subseteq R_4\subseteq R_3.
\]

This six-case table, not the earlier four-pair label, is the authoritative B1
starting point.

## 3. Definition of package completion

This package is complete only after one of the following decisive outcomes.

### Outcome L50

Both endpoint packets are excluded in characteristic zero:

```text
Packet A: CLOSED
Packet B: CLOSED
```

and the ordinary theorem

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\geq50
\]

passes exact replay and adversarial audit.

### Outcome EXACT-SURVIVOR

An exact characteristic-zero object survives every equation actually encoded
for its workstream. A survivor must include exact coordinates or a controlled
number-field representation, all nonvanishing conditions, and deterministic
verification of every hypothesis. It must then be analyzed before any search
family is enlarged.

A finite-field survivor, a numerical approximate point, a restricted-family
failure, or a larger negative random sample is not package completion.

## 4. Execution rule

This document authorizes continuous execution through the listed dependent
tasks. Do not stop after each small checkpoint to request a new plan. Stop
only for one of these reasons:

1. a load-bearing mathematical contradiction in the package is found;
2. an exact survivor is found;
3. a workstream reaches its stated decisive outcome;
4. the lower-50 promotion gate is satisfied.

Intermediate results should be committed in coherent theorem-facing groups,
not as one commit per tiny calculation.

## 5. Priority allocation

Approximate research allocation:

```text
50%  B1: the six weighted common-graph relation-flag cases
25%  B2: arbitrary mixed graph-complement Packet B
20%  A: all-rank-seven Packet A
 5%  independent replay, adversarial review, and promotion closure
```

Packet-A module construction may proceed in parallel with B1. Heavy B2 case
enumeration must wait for a structural reduction; unrestricted `GL_6` search
is not authorized.

---

# Work Package 0 — repair and freeze the true starting boundary

## WP0 objective

Remove the stale four-stratum label, freeze the six corrected relation-defect
cases, and establish one exact HEAD from which all later work proceeds.

## Task 0.1 — replay the strict-growth correction

Verify independently that a reduced length-42 projective Hilbert function
cannot plateau below 42 and then grow again. Check both eliminated cases:

```text
H3=H4=36<42,
H4=H5=40<42.
```

**Required output:** exact proof note, deterministic payload, and focused test.

## Task 0.2 — reconcile the earlier checkpoint artifacts

Update or explicitly supersede every occurrence of:

```text
target-compatible geometrically feasible strata = four pairs
```

in the checkpoint documentation, payload fields, tests, and research log.
The rational-curve-union examples remain valid only as degree-three/four
profile controls. They are not target-containment witnesses.

**Acceptance condition:** repository search finds no theorem-facing text that
still treats `(32,40)` as compatible with `H_Z(5)<=40`.

## Task 0.3 — freeze the six relation flags

For each of the six cases, record:

- `dim C_3,C_4,C_5`;
- `dim R_3,R_4,R_5`;
- all strictly increasing admissible `H_Z(6)` values;
- all Macaulay-admissible first differences through stabilization;
- whether the points necessarily span `P^6` and, if used, the proof.

**Required output:** one compact machine-readable case table. Do not create six
nearly identical payloads at this stage.

## Task 0.4 — freeze matrix conventions

Use one convention throughout the package:

```text
E_d: 42 x binom(d+6,6) evaluation matrix,
C_d: row/column code in k^42 as explicitly declared,
R_d: dual relation space,
D: nonzero diagonal term-weight matrix,
w_i=d_i^{-1}.
```

Every later script must state whether vectors are rows or columns. Add one
transpose regression test so that `ker(E4^T)` and `im(E3)` cannot silently be
interchanged.

## Task 0.5 — exact baseline gate

Run:

- the strict-growth replay;
- the weighted common-graph interface replay;
- all focused B1 tests;
- the repository English-only gate;
- the full repository test workflow.

**WP0 completion:** one exact commit with successful CI and the six-case table
as the only active B1 boundary.

---

# Work Package 1 — common-graph relation-flag foundation

## WP1 objective

Replace large undifferentiated rank conditions by a small exact system on the
nested relation flag

\[
R_5\subseteq R_4\subseteq R_3\subset k^{42},
\]

the point-coordinate matrix, the seven target coefficient rows, and the
nonzero weights.

## Task 1.1 — derive the evaluation-code multiplication identities

Prove and implement the exact Schur-product relations among the point codes:

\[
C_{d+1}=\operatorname{span}(C_d*C_1)
\]

in the chosen affine/homogeneous convention. Record the dual multiplication
maps

\[
R_{d+1}\longrightarrow R_d\otimes C_1^*
\]

for `d=3,4,5`.

The implementation must work with exact integers or rationals on symbolic
controls and with modular arithmetic only as a replay acceleration.

## Task 1.2 — enumerate admissible Hilbert and Betti data

For each of the six cases, enumerate every Macaulay-admissible continuation
through degree six and stabilization. Determine:

- first-difference sequences;
- possible regularity;
- dimensions of `I_Z(d)` for `d=3,4,5,6`;
- forced numbers of new generators in degrees four, five, and six;
- any Gotzmann-persistent branches;
- any branch forcing a positive-dimensional base locus.

Do not enumerate arbitrary ideals. First use numerical growth to reduce to a
small finite list of Hilbert/Betti types.

**Decisive sub-outcome:** if a listed type is not realizable by 42 distinct
reduced points, remove it with a characteristic-zero proof.

## Task 1.3 — construct a minimal target-support representation

Let `a_i in k^7` be homogeneous point vectors and let `c_i in k^7` be the
column of coefficients representing the seven permanent degree-six targets
as combinations of `l_i^6`.

Choose an inclusion-minimal target-support subset and prove the exact
independence properties needed for that choice. Keep repeated-point exclusion
and nonzero combined coefficients explicit.

**Required output:** a coordinate-free statement and a small evaluator that
checks minimality without enumerating all subsets.

## Task 1.4 — derive the full mixed-partial relation-web equation

From equality of mixed partials derive

\[
c_i\wedge a_i
 =\sum_{\alpha=1}^{q_5}\rho_i^{(\alpha)}\beta_\alpha,
\qquad q_5=\dim R_5\in\{2,3,4\},
\]

where `rho^(alpha)` is a basis of fifth-power relations and
`beta_alpha in wedge^2 k^7`.

Prove basis-change invariance in `R_5`, target-row invariance, and the exact
relation between this equation and degree-six target containment. Separate:

- necessary integrability equations;
- sufficient reconstruction equations;
- open nonvanishing/minimality conditions.

No theorem may be promoted from the necessary equations alone.

## Task 1.5 — classify the `q_5=2` alternating pencil

This lane covers:

```text
B1-33-39-40,
B1-34-38-40,
B1-35-37-40.
```

For the pencil

\[
\beta(s,t)=s\beta_1+t\beta_2,
\]

analyze the rank-at-most-two points forced by the 42 relation-coordinate
columns. Use exact Pfaffian equations. Split into:

1. the entire pencil lies in the decomposable Grassmannian;
2. the relation-coordinate points occupy at most two Pfaffian roots;
3. one or more coefficient columns vanish or leave the minimal support;
4. a boundary with common vector or fixed three-space support.

Classify every branch in characteristic zero. For branches where the entire
pencil is decomposable, apply the classification of linear spaces in
`Gr(2,7)` and derive the resulting restriction on the point vectors `a_i` and
target coefficient vectors `c_i`.

**Preferred theorem:** every full-support target representation in the
`q_5=2` cases integrates to a shorter Waring expression or forces a forbidden
Hilbert plateau.

## Task 1.6 — classify the `q_5=3` alternating net

This lane covers:

```text
B1-34-38-39,
B1-35-37-39.
```

Let the relation coordinates be 42 points in `P^2`. Determine the common zero
scheme of the `4 x 4` Pfaffian quadrics of the alternating net. Split by the
quadratic Hilbert function of those 42 relation-coordinate points:

- not contained in a conic;
- contained in a reduced conic;
- contained in a double line or two lines;
- supported on a line plus residual points;
- finite Pfaffian base locus.

For each branch determine whether the net is contained in the decomposable
Grassmannian, has a common vector, is supported in a fixed four-space, or has
only finitely many rank-two members.

Tie every surviving branch back to the nested relation flag `R_5 subset R_4`
and the actual evaluation-code multiplication maps.

## Task 1.7 — classify the `q_5=4` alternating web

This lane is specific to `B1-35-37-38`.

Let the relation-coordinate points lie in `P^3`. Compute the Pfaffian-quadric
system and split by its base locus:

- all of `P^3`;
- a surface component;
- a curve component;
- a finite scheme;
- coordinate points lying in a proper plane or line.

Use exact primary decomposition only after exploiting the low-dimensional
skew-form classification. Avoid a generic elimination in all point
coordinates.

**Required output:** a finite list of structural web types or a proof that no
full-support web is compatible with the target representation.

## Task 1.8 — compress weighted coupling to a full-support kernel problem

For each point configuration choose:

- a parity-check matrix `P_3` with `ker P_3=C_3`;
- a basis matrix `Q_4` for `R_4`.

With reciprocal weights `w_i=d_i^{-1}`, prove that

\[
R_4\subseteq D C_3
\]

is equivalent to

\[
\boxed{P_3\operatorname{diag}(w)Q_4=0}.
\]

Flatten this to a linear system

\[
A_Zw=0
\]

with respectively 27, 32, and 35 displayed scalar rows for the three rank
pairs. The real condition is not merely `ker A_Z != 0`; it is

\[
\ker A_Z\cap(k^\times)^{42}\ne\varnothing.
\]

Determine exact criteria for the kernel to meet the full-support torus:

- coordinate hyperplanes do not cover the kernel;
- matroid-coloop formulation;
- maximal-minor or dual-support certificate;
- behavior under basis changes of `P_3` and `Q_4`.

## Task 1.9 — derive the coupling degeneracy loci

For each rank pair, determine the locus where `A_Z` has:

- its generic rank;
- rank drop by one;
- larger rank drop;
- a kernel contained in a coordinate hyperplane;
- a full-support kernel.

The output should be a small determinantal or matroid condition on the
relation flag, not all minors of the original `210 x 84` matrix.

## Task 1.10 — compress degree-six target containment through the ideal

Let `I_Z(6)=ker E_6`. Prove that containment of the seven target rows is
equivalent to vanishing of the projection

\[
I_Z(6)\longrightarrow k^7
\]

onto the seven squarefree target coordinates.

Then express this projection using the smallest available data from:

- generators of `I_Z` in degrees at most six;
- multiplication maps from `I_Z(4)` and `I_Z(5)`;
- the relation-web equation;
- the six-case Hilbert/Betti type.

The goal is to avoid repeatedly forming `42 x 924` matrices during symbolic
elimination.

## Task 1.11 — prove target sufficiency or record the missing equations

For every compressed target system, prove one of:

```text
EQUIVALENT:
The small equations plus the declared open conditions are equivalent to
rank(stack(E6,S6))=rank(E6).
```

or

```text
NECESSARY ONLY:
The exact additional equations still missing are listed and implemented in
the final verifier.
```

No case may be closed using a necessary-only compression without checking the
full target matrix at the final exact point or certificate.

## Task 1.12 — choose quotient and gauge coordinates

Remove only genuine symmetries:

- projective scaling of each point;
- basis changes in relation spaces;
- target-row basis changes preserving the fixed target subspace;
- common ambient coordinate changes that preserve the permanent target when
  actually allowed.

Do not quotient by arbitrary `PGL_7` if it changes the seven permanent target
monomials. Record every gauge denominator as an explicit nonvanishing
condition.

## Task 1.13 — build mandatory controls

The foundation must include at least these controls:

1. a reduced 42-point profile control for every displayed `(H3,H4)` pair;
2. the old weighted `(31,41)` coupling-positive, target-negative control;
3. a target-row omission regression that becomes a false positive;
4. a weight omission regression that becomes a false positive;
5. a repeated-point control rejected by minimality;
6. a synthetic system satisfying integrability but failing full target
   reconstruction;
7. a full-support weight vector and a coordinate-hyperplane-only kernel
   control.

## WP1 completion gate

WP1 is complete when all six cases have:

- a finite Hilbert/Betti list;
- an exact relation-web type list;
- the small full-support coupling system;
- an equivalent or explicitly completed target system;
- a deterministic final verifier.

WP1 does not require that the six cases are already excluded.

---

# Work Package 2 — decisive solution of the six B1 cases

## WP2 objective

Return `CLOSED` or an exact survivor for each of the six corrected
common-graph cases. Work by relation-defect dimension, not by another blind
point scan.

## Common lane protocol

Every case lane follows all seven steps below.

### Lane step A — exact chart inventory

Construct a finite chart cover justified by the WP1 structural classification.
State why every reduced full-support configuration in that case enters at
least one chart.

### Lane step B — finite-field reconnaissance

Use at most a few controlled primes to:

- locate components;
- choose pivots;
- estimate dimensions;
- find candidate exact points;
- falsify proposed universal lemmas.

Finite-field emptiness alone is not a characteristic-zero exclusion.

### Lane step C — characteristic-zero closure

Close each chart using one or more of:

- exact rational row reduction;
- integer nonzero minors;
- Groebner or resultant elimination with a stated monomial order;
- saturation by all declared open conditions;
- a controlled algebraic-number certificate;
- a pure structural theorem that makes elimination unnecessary.

### Lane step D — full verifier

Recheck, independently of the elimination representation:

```text
42 distinct reduced points,
correct H3/H4/H5 ranks,
seven degree-six target containments,
nonzero weights,
rank(E4^T D E3)=30,
all graph and minimality hypotheses.
```

### Lane step E — survivor rule

An exact survivor is investigated immediately. Determine whether it:

- gives a genuine common-graph equality packet;
- violates a reduction hypothesis;
- exposes a missing higher-degree target equation;
- extends to the full 49-term permanent identity;
- supplies a counterexample to the planned exclusion lemma.

### Lane step F — independent replay

A second implementation must verify the load-bearing determinant, ideal, or
exact point without importing the first implementation's intermediate
matrices.

### Lane step G — lane verdict

Use exactly one verdict:

```text
CASE-CLOSED
CASE-SURVIVOR
CASE-BLOCKED-BY-EXPLICIT-MISSING-LEMMA
```

`BLOCKED` must name one precise lemma and its smallest falsifiable test; it is
not permission to resume broad search.

## Case 2.1 — `B1-33-39-40`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(9,3,2).
```

Primary route:

1. apply the alternating-pencil classification;
2. classify the one-dimensional growth `H4 -> H5`;
3. determine the unique or finite possible degree-five base-locus geometry;
4. combine the three-dimensional `R4` flag with the 27-row weight system;
5. test whether any full-support reciprocal weight survives the exact target
   equations.

Preferred closure certificate: a pure pencil/base-locus contradiction or one
small saturated ideal.

## Case 2.2 — `B1-34-38-39`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(8,4,3).
```

Primary route:

1. classify the alternating net and the relation-coordinate conic cases;
2. exploit the single growth from 38 to 39;
3. determine whether `R5` forces a common-vector or fixed-four-space web;
4. impose the 32-row full-support weight system;
5. close every conic, line-pair, and finite-Pfaffian branch separately.

## Case 2.3 — `B1-34-38-40`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(8,4,2).
```

Primary route:

1. apply the alternating-pencil classification;
2. exploit two-dimensional growth from degree four to five;
3. compare the extra degree-five code direction with the four-dimensional
   `R4` relation space;
4. determine whether the coupling kernel necessarily loses full support;
5. otherwise solve the remaining exact target incidence.

This lane must not be inferred from Case 2.2; the smaller `R5` changes the
integrability geometry.

## Case 2.4 — `B1-35-37-38`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(7,5,4).
```

Primary route:

1. classify the alternating web in `P^3`;
2. exploit the minimal one-dimensional degree-five growth;
3. classify positive-dimensional Pfaffian base loci before any elimination;
4. combine the five-dimensional `R4` flag with the 35-row weight system;
5. use exact saturation to remove coordinate-weight and repeated-point
   boundary components.

This is expected to be the broadest single common-graph lane. It receives the
largest B1 computational budget, but still may not begin with arbitrary point
coordinates.

## Case 2.5 — `B1-35-37-39`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(7,5,3).
```

Primary route:

1. classify the alternating net;
2. exploit two-dimensional degree-five growth;
3. compare net Pfaffian branches with the five-dimensional `R4` extension;
4. impose full-support reciprocal weights;
5. solve target and coupling jointly, not sequentially.

## Case 2.6 — `B1-35-37-40`

Relation dimensions:

```text
(dim R3, dim R4, dim R5)=(7,5,2).
```

Primary route:

1. classify the alternating pencil;
2. exploit three-dimensional degree-five growth;
3. determine whether the larger growth forces the pencil relation points to
   occupy too few Pfaffian roots;
4. impose the five-dimensional `R4` extension and 35-row weight system;
5. close all full-support branches exactly.

## Task 2.7 — cross-case consolidation

After all six lane verdicts:

- identify shared lemmas and remove duplicated proofs;
- verify every strict-growth and Hilbert branch appears exactly once;
- ensure no lane silently assumes generic points;
- ensure saturation includes all nonzero weights and chart denominators;
- ensure the final full verifier uses the original `E3,E4,E5,E6,S6`
  matrices.

## Task 2.8 — B1 decisive verdict

Return exactly one of:

```text
B1-CLOSED:
No weighted common-graph Packet-B solution exists in characteristic zero.
```

or

```text
B1-SURVIVOR:
An exact characteristic-zero common-graph object satisfies every equality,
coupling, target, reducedness, distinctness, and nonvanishing condition.
```

If some cases are closed and one is blocked, the workstream remains open and
the blocked lemma becomes the sole next B1 target.

## Task 2.9 — B1 adversarial audit

An independent audit must attack:

- the strict-growth use;
- minimal target-support independence;
- relation-web sufficiency;
- basis and transpose conventions;
- saturation by weight coordinates;
- finite-field-to-characteristic-zero inferences;
- omitted boundary charts;
- use of curve controls as anything more than profile controls.

All fatal and major findings must be repaired before B1 is used in B2.

---

# Work Package 3 — arbitrary mixed graph-complement Packet B

## WP3 objective

Upgrade the common-graph result to the full mixed equality packet consisting
of seven direct rank-six equality terms and 42 arbitrary permitted rank-seven
graph complements.

B1 closure alone is not Packet-B closure.

## Task 3.1 — write the coordinate-free full Packet-B variables

Fix the 42-space

\[
A=A_1\oplus\cdots\oplus A_7,
\qquad \dim A_r=6,
\]

from the seven rank-six equality terms. Parameterize each rank-seven
complement by the smallest graph data over the common seven-dimensional
quotient. Keep:

- the 42 individual term labels;
- all 42 term weights;
- the seven factor directions inside each complement;
- pairwise intersection restrictions;
- graph nondegeneracy.

Do not identify different terms merely because their unlabelled spans agree.

## Task 3.2 — derive the exact full Sylvester-equality equations

Construct the labelled maps

\[
B:\bigoplus_i K_i\to H_4,
\qquad
C:H_3^*\to\bigoplus_i K_i
\]

for the full mixed packet and encode

\[
\ker B\subseteq\operatorname{im}C.
\]

Retain the permanent target equations in degrees six and, only when genuinely
needed, seven. Give a block decomposition by row-subset multidegrees.

## Task 3.3 — isolate the coupled rank-drop locus

The synchronized mixed-Glynn packet has coupling defect 35 and is not on the
equality locus. Therefore:

- do not linearize at that packet as though it were a solution;
- do not use its tangent space as a model of the desired component;
- do not continue support-by-support perturbations around it unless a proved
  degeneration connects it to the actual rank-drop locus.

Instead determine the equations forcing the required drop to

```text
rank(BC)=1225,
rank(B)+rank(C)=2870.
```

## Task 3.4 — prove a common-code reduction or expose the exact obstruction

Attempt to prove that every full Packet-B equality object admits, after only
allowed changes of basis, a common evaluation-code model covered by B1.

A valid reduction must preserve:

- term labels;
- term weights;
- the seven target blocks;
- the relation inclusion;
- reducedness and graph nondegeneracy.

If the reduction fails, return an explicit parameter list for the surviving
extra moduli. Examples include:

- block-dependent point codes;
- noncommuting quotient identifications;
- rank drops in graph maps;
- changing factor frames;
- boundary complete-collineation data.

The failure itself is progress only when the extra moduli are finite and
precisely described.

## Task 3.5 — derive a finite structural stratum list

From Task 3.4 produce one of:

```text
COMMON-CODE THEOREM
```

or

```text
FINITE MIXED STRATA S_1,...,S_m.
```

Each mixed stratum must specify dimensions, support/intersection pattern,
open conditions, and which existing exact certificate applies.

No unrestricted `GL_6^42` search is authorized as a substitute.

## Task 3.6 — build the existing-certificate coverage matrix

Map every stratum against the already completed library, including:

- the full monomial-transform classification;
- diagonal, signed-coordinate, and permutation-type closures;
- elementary and multi-direction shear families;
- coincident and overlap-one `(2,2)` closures;
- overlapping `(2,3)/(3,2)` projective support closure;
- overlapping `(2,4)/(4,2)` projective support closure;
- overlap-four-through-six exact minor certificates;
- the repaired Laurent-torus face audit;
- all target-negative common-curve controls.

For every imported certificate record:

- exact hypotheses;
- characteristic;
- covered boundary faces;
- missing nonnilpotent or higher-rank parameters.

Do not rerun or duplicate a closed family.

## Task 3.7 — handle true boundary degenerations

Only for residual strata produced by Task 3.5, construct the correct compact
boundary object. Raw limits of sums of moving subspaces are not sufficient.
Use, as required:

- flat limits;
- Rees modules;
- complete-collineation data;
- Smith/valuation packets;
- initial modules with retained term labels.

Prove that the chosen compactification preserves the equations actually used.

## Task 3.8 — close residual rank-one nonnilpotent strata

If Task 3.5 produces rank-one strata beyond the already completed projective
support closures, classify them by exact support and nilpotence type. Use
projective face closure and saturation. Do not expand support size without a
structural reason from the reduction.

## Task 3.9 — close residual higher-rank perturbation strata

If higher-rank graph perturbations survive, first prove a normal form reducing
them to finitely many ranks and support dimensions. Then encode target and
coupling simultaneously. Random higher-rank matrices are diagnostic only.

## Task 3.10 — mixed-stratum exact verifier

For every residual exact point or exclusion certificate, independently check:

- seven rank-six terms in the correct equality normal form;
- 42 rank-seven graph complements;
- pairwise intersection limits;
- full middle equality;
- `ker B subset im C`;
- all nonzero term weights;
- permanent target containment;
- the actual 49-term coefficient identity when claimed.

## Task 3.11 — Packet-B survivor analysis

An exact mixed survivor takes priority over further exclusion. Determine
whether it is:

- a genuine 49-term decomposition;
- a point satisfying the endpoint equations but not the full identity;
- a counterexample to common-code reduction;
- evidence that degree seven or another labelled module is necessary.

## Task 3.12 — B2 decisive verdict

Return exactly one of:

```text
B2-CLOSED:
Every arbitrary mixed graph-complement equality packet is impossible in
characteristic zero.
```

or

```text
B2-SURVIVOR:
An exact characteristic-zero mixed packet satisfies every proved endpoint,
coupling, graph, and permanent-target condition.
```

Packet B is closed only after `B2-CLOSED`.

## Task 3.13 — independent Packet-B audit

Audit the structural reduction before auditing individual computations. A
perfect residual-stratum computation cannot repair an incomplete reduction.
The audit must explicitly search for:

- unlisted quotient identifications;
- mixed weights lost by normalization;
- non-flat boundary limits;
- term-label permutations that change the equations;
- a hidden reliance on the synchronized mixed-Glynn packet.

---

# Work Package 4 — all-rank-seven Packet A

## WP4 objective

Exclude or exactly classify the 49 rank-seven equality terms whose factor
seven-planes form the forced simple rank-seven multilinear matroid.

Unlabelled Hilbert data, the quadratic interface, factor-plane incidence, and
current scalar erasure bounds are already known to be insufficient.

## Task 4.1 — define the minimal term-labelled module

For every term `T_i`, retain the labelled spaces

\[
D_2(T_i),\quad D_5(T_i),\quad D_6(T_i)
\]

and the termwise multiplication/differentiation maps linking them. Build the
smallest global module that sees:

- the degree `2/5` complementary relation pairing;
- degree-six target containment;
- the Sylvester equality condition;
- the individual term labels.

Do not add degree `3/4` unless the smaller module leaves a genuine survivor.

## Task 4.2 — derive exact dimensions and one-term caps

Compute the target-module rank on `perm_7` and the maximum contribution of one
rank-seven Chow term under the Packet-A transversality constraints. The gain
must come from compatibility, not a nonnegative direct sum of known maps.

Prove all one-term caps in characteristic zero. A modular rank gives only a
lower bound on a denominator and must be paired with a structural upper bound.

## Task 4.3 — split the module by permanent torus weights

Decompose the target and term-labelled maps into row/column multidegrees or
another exact permanent torus grading. Produce small blocks and identify:

- target-only weights;
- term-relation weights;
- complementary `2/5` pairs;
- blocks where the 49-term Glynn truncation is a mandatory negative control.

## Task 4.4 — formulate the degree `2/5` relation pairing

Let the degree-two relation module and degree-five image module retain the
same term labels. Derive the exact pairing or connecting map forced by an
actual identity

\[
\sum_{i=1}^{49}T_i=\operatorname{perm}_7.
\]

State clearly which equations disappear after forgetting labels. The
resulting map should reject the known quadratic-interface counterexample only
when permanent-specific higher-degree data are included.

## Task 4.5 — formulate degree-six target containment

Construct the smallest block matrix equivalent to

\[
E_6\subseteq\sum_iD_6(T_i)
\]

under the Packet-A factor-plane conditions. Keep all 49 target blocks, not
only dimensions or random evaluations.

## Task 4.6 — derive a structural defect theorem

Aim for one theorem of one of these forms:

1. at least one permanent target block has positive defect;
2. equality forces a tensor-split or column-uniform normal form;
3. a term-labelled degree-two relation cannot be realized compatibly in
   degree five;
4. the target module has rank greater than 49 times the one-term cap;
5. every zero-defect configuration lies in an explicit finite list.

The theorem must use permanent-specific hypotheses. Abstract multilinear
matroid plus Sylvester equality is known to be insufficient.

## Task 4.7 — analyze the zero-output-kernel branch

Separate configurations where the relevant output summation map is injective
from those with nonzero labelled relations. The lower-dimensional
non-tensor-split Sylvester-equality example is a mandatory control: any lemma
claiming equality alone forces a tensor split must fail on it.

## Task 4.8 — analyze nonzero relation branches

Classify the smallest possible labelled relation supports. Use factor-plane
transversality and complementary-degree multiplication to determine whether a
relation can propagate across 49 terms without violating a permanent target
block.

Prefer support-minimal relation arguments over enumerating subsets of 49
terms.

## Task 4.9 — mandatory Packet-A controls

Every proposed Packet-A theorem must be tested against:

1. the 49-term Glynn truncation, which passes weaker quadratic/scalar
   interfaces but fails higher-degree permanent containment;
2. the non-tensor-split Sylvester-equality plane configuration;
3. the full 64-term Glynn decomposition as a positive identity control;
4. repeated or proportional terms as a minimality-negative control;
5. a synthetic labelled module with correct dimensions but deliberately
   broken multiplication maps.

## Task 4.10 — finite structural strata only after a theorem

If Task 4.6 reduces Packet A to finitely many normal forms, construct exact
charts for those forms. Do not begin a general search over 49 arbitrary
seven-planes before such a reduction.

## Task 4.11 — exact closure or survivor

For each theorem-produced stratum, return:

```text
A-STRATUM-CLOSED
```

or an exact characteristic-zero survivor with the full labelled module and
target verification.

## Task 4.12 — Packet-A decisive verdict

Return exactly one of:

```text
A-CLOSED:
No all-rank-seven 49-term equality packet can satisfy the permanent identity.
```

or

```text
A-SURVIVOR:
An exact characteristic-zero Packet-A object satisfies every encoded
term-labelled cross-degree and target condition.
```

## Task 4.13 — independent Packet-A audit

The audit must check:

- no accidental replacement of the identity by dimension equalities;
- no loss of term labels;
- no unjustified torus degeneration of arbitrary terms;
- no use of a direct-sum capacity already proved insufficient;
- every control behaves in the expected direction;
- every structural stratum is actually exhaustive.

---

# Work Package 5 — combine, audit, and promote lower 50

## WP5 objective

Convert `A-CLOSED` and `B2-CLOSED` into one frozen ordinary lower-50 theorem
with exact replay and a clean claim boundary.

## Task 5.1 — endpoint-exhaustion reconciliation

Re-read the slope-ten endpoint theorem and verify that the two packets remain
exhaustive after all later corrections. Check:

- the rank-five branch exclusion;
- the integer equation `6a+7b=49`;
- all equality increments;
- characteristic-zero scope;
- ordinary-rank versus border-rank wording.

## Task 5.2 — assemble the proof chain

The theorem draft must expose the chain in this order:

```text
existing lower 49
-> slope-ten equality classification
-> Packet B exclusion
-> Packet A exclusion
-> lower 50.
```

Every imported lemma must cite its exact repository artifact and frozen
commit.

## Task 5.3 — independent exact replay

A clean replay must regenerate all load-bearing finite certificates from one
exact commit. It should not require historical checkpoint chunks that have
already been merged into complete payloads.

## Task 5.4 — adversarial mathematical review

The review must actively attempt to break:

- strict Hilbert growth;
- target-support minimality;
- relation-web classification;
- coupling full-support weights;
- common-code or mixed-stratum exhaustiveness;
- Packet-A module sufficiency;
- characteristic-zero lifting;
- boundary saturation;
- the final endpoint dichotomy.

Classify findings as fatal, major, minor, or editorial. Repair all fatal,
major, and claim-affecting minor findings.

## Task 5.5 — theorem-facing repository update

Update, at minimum:

- `README.md`;
- `STATUS.md`;
- `docs/research_log.md`;
- the relevant `n7` program note;
- the PR body with the exact final HEAD and test result.

Remove or clearly mark historical status lines that still state an earlier
lower bound as current.

## Task 5.6 — promotion gate

The statement

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\geq50
\]

may be promoted only when all boxes are checked:

```text
[ ] The strict-growth correction is integrated and replayed.
[ ] All six B1 cases are closed or subsumed by a stronger exact theorem.
[ ] Arbitrary Packet B is closed, not only the common-graph specialization.
[ ] Packet A is closed using permanent-specific term-labelled equations.
[ ] Every structural reduction is proved exhaustive.
[ ] Every load-bearing computation has an exact characteristic-zero meaning.
[ ] Independent replay succeeds at one exact commit.
[ ] Adversarial review has no unresolved fatal or major finding.
[ ] The theorem-facing CI workflow passes.
```

Until every item is satisfied, the current interval remains

\[
49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

---

# 6. Dependency and parallel-execution map

## Mandatory order

```text
WP0
  -> WP1 relation-flag foundation
      -> WP2 six B1 cases
          -> WP3 Packet-B global closure

WP0
  -> WP4 Packet-A module construction and structural theorem

WP3 B2-CLOSED + WP4 A-CLOSED
  -> WP5 lower-50 promotion
```

## Authorized parallel work

After WP0:

- Tasks 1.1--1.10 may be developed in parallel where interfaces are frozen.
- The three `q5=2` cases may share the pencil theorem but require separate
  final verifiers.
- The two `q5=3` cases may share the net theorem but require separate
  `R4`-extension analysis.
- Packet-A Tasks 4.1--4.5 may proceed while B1 cases are being solved.
- Packet-B Task 3.1--3.4 may begin after the B1 conventions are frozen, but
  heavy residual-stratum computation waits for Task 3.5.

## No artificial serialization

A completed lemma should immediately unlock every dependent case. Do not wait
for all sibling cases when one shared theorem already applies.

---

# 7. Default artifact map

These names are defaults, not a requirement to create empty placeholders.
Consolidate artifacts when one theorem closes several cases.

```text
docs/n7_b1_relation_flag_foundation.md
scripts/n7_b1_relation_flag_foundation.py
data/n7_b1_relation_flag_foundation.json
tests/test_n7_b1_relation_flag_foundation.py

docs/n7_b1_case_33_39_40.md
docs/n7_b1_case_34_38_39.md
docs/n7_b1_case_34_38_40.md
docs/n7_b1_case_35_37_38.md
docs/n7_b1_case_35_37_39.md
docs/n7_b1_case_35_37_40.md

docs/n7_packet_b_global_reduction.md
docs/n7_packet_b_global_closure.md

docs/n7_packet_a_term_labelled_module.md
docs/n7_packet_a_global_closure.md

docs/n7_lower50_proof.md
docs/n7_lower50_adversarial_review.md
```

For each theorem-facing finite result, the minimal preferred artifact set is:

```text
one proof note
one deterministic implementation
one frozen payload when the output is nontrivial
focused tests
one independent replay when the computation is load-bearing
```

Do not create a manager, registry, database, generalized experiment platform,
or one payload per trivial subcase.

---

# 8. Resource and computation discipline

1. Estimate candidate count and peak memory before every large run.
2. Stream candidates; do not materialize large combinatorial families.
3. Use finite fields to discover pivots and components, not as the final
   theorem unless paired with a valid characteristic-zero inference.
4. Prefer small exact blocks over random evaluation matrices.
5. Reuse complete certificates instead of recomputing them.
6. A single exact survivor outranks millions of negative samples.
7. Stop a search when the open dense failure is already understood and the
   equality locus has not been encoded.
8. Do not launch unrestricted `GL_6`, arbitrary 42-point, or arbitrary
   49-plane brute force.

---

# 9. Suspended routes

The following remain suspended unless a new theorem explicitly reopens them:

- additional scalar derivative or shadow dynamic programs;
- more uncoupled standard Koszul sweeps;
- nonnegative direct sums of existing flattenings;
- a direct transfer of the `perm_6` one-middle-layer proof;
- increasing the old monomial-curve weight box;
- unit-weight-only Packet-B classification;
- blind random finite-field point searches;
- tangent expansion around the synchronized mixed-Glynn packet;
- unrestricted general-`GL_6` scans;
- unstructured expansion of mixed-Glynn support families;
- exact-rank-64 work before the two 49-term packets are resolved.

---

# 10. Substantive-progress standard

A result counts as substantive progress if it does at least one of the
following:

1. closes one of the six B1 cases in characteristic zero;
2. proves a shared pencil, net, or web theorem closing multiple cases;
3. produces an exact B1 survivor;
4. proves the common-code reduction or a finite exhaustive mixed-stratum list;
5. closes arbitrary Packet B;
6. builds a sufficient Packet-A term-labelled module;
7. closes Packet A;
8. promotes lower 50 after audit.

The following do not count as substantive completion by themselves:

- another restricted family with no reduction theorem;
- a larger negative random sample;
- a finite-field empty search;
- a new dimension bound already compatible with all six cases;
- a planning-only status update;
- more tests without a new load-bearing claim.

---

# 11. Immediate launch batch

The next execution batch is deliberately larger than the previous one. Begin
without requesting another planning round:

```text
1. Replay and integrate the strict-growth correction.
2. Freeze the six H3/H4/H5 relation-flag cases.
3. Enumerate their admissible Hilbert/Betti continuations.
4. Derive the mixed-partial relation-web equation for q5=2,3,4.
5. Prove the full-support coupling compression P3 diag(w) Q4=0.
6. Build the small ideal-based degree-six target projection.
7. Classify the q5=2 alternating pencil completely.
8. Start the q5=3 net classification and its conic/line branches.
9. Build final exact verifiers for all six cases.
10. In parallel, construct the Packet-A degree-2/5/6 labelled module.
11. Begin the coordinate-free Packet-B reduction, but do not brute-force its
    residual moduli before the reduction theorem is available.
```

The first major checkpoint is not another interface note. It is one of:

```text
- at least three of the six B1 cases closed exactly;
- one shared theorem closing an entire q5 class;
- an exact B1 survivor;
- a proved structural reduction that makes all six cases finite and explicit.
```

# 12. Final success criterion

The preferred output is the ordinary lower-50 theorem. The other scientifically
valid decisive output is an exact survivor showing that the current endpoint
invariants are insufficient and identifying the smallest missing invariant.

Repeatedly enlarging restricted negative families without either output is
not success for this package.
