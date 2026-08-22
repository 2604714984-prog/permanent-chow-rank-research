# `perm_7` lower-50 major execution package v3

## Status and claim boundary

`ACTIVE RESEARCH PACKAGE — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Input commit: `589fabffae17c518f9118b2df606d5a13cd6a6ee`  
Active research PR: `#31`  
Active branch: `agent/general-column-sign-rank`

This package is the authoritative successor to
`docs/n7_lower50_next_phase_task_plan.md` and
`docs/n7_lower50_major_execution_package_v2.md`.

The v2 package correctly expanded the research scope, but several tasks used
one word, "relation", for two mathematically different kernels. Version 3
installs a mandatory notation firewall before any further execution.

The current ordinary characteristic-zero interval remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64}.
\]

The promotion target for this package is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50}.
\]

No statement about border Chow rank, exact rank 64, or general `perm_n` is
made here.

---

# 0. Completed handoff

The previous weighted common-graph checkpoint is complete and is treated as
input rather than work to repeat.

For the common 42-point graph model, with homogeneous evaluation maps `E_d`
and nonzero diagonal term weights `D`, the frozen interfaces are

\[
\operatorname{rank}E_3+\operatorname{rank}E_4=72,
\]

\[
\operatorname{rank}(E_4^TDE_3)=30,
\]

and degree-six permanent containment

\[
\operatorname{rank}\begin{bmatrix}E_6\\S_6\end{bmatrix}
=\operatorname{rank}E_6.
\]

The old `(30,42)` and `(31,41)` profiles are incompatible with degree-six
target containment. Reduced-point strict growth removes `(36,36)` and also
`(32,40)`, because the latter would force `H_Z(4)=H_Z(5)=40<42`. Three rank
pairs and six numerical Hilbert triples remain:

```text
(33,39,40)
(34,38,39), (34,38,40)
(35,37,38), (35,37,39), (35,37,40)
```

These triples are numerical candidates, not six asserted geometric or target
controls. The four curve-union constructions remain only `H_3/H_4` profile
controls.

---

# 1. Mandatory notation firewall

For every degree `d`, define four different objects:

\[
C_d=\operatorname{im}E_d\subseteq k^{42},
\]

\[
R_d=C_d^\perp=\ker(E_d^T)\subseteq k^{42},
\]

\[
I_d=\ker(E_d)\subseteq S^d(k^7),
\]

and

\[
W_d=I_d^\perp=\operatorname{rowspan}(E_d)
\subseteq S^d(k^7)^*.
\]

Hence

\[
\dim C_d=\dim W_d=H_Z(d),
\]

\[
\dim R_d=42-H_Z(d),
\]

\[
\dim I_d=\binom{d+6}{6}-H_Z(d).
\]

These roles are fixed:

- weighted coupling uses `R_4` and `C_3`;
- reciprocal-weight/Hadamard coupling uses `R_3` and `R_4`;
- Macaulay growth, multiplication by linear forms, generic initial ideals,
  Betti tables, Hilbert-Burch data, and geometric carriers use `I_d`;
- degree-six permanent target containment is `T_6 subset W_6`;
- no multiplication map `R_3 -> R_4` is assumed or named.

Any result violating this firewall is rejected before mathematical review.

---

# 2. Package-level outcomes

The package must aim at theorem-scale decisions, not another restricted-family
inventory.

## Primary B1 outcome

Return exactly one of:

```text
B1-CLOSED:
No characteristic-zero weighted common-graph Packet-B solution exists.
```

or

```text
B1-SURVIVOR:
An exact characteristic-zero common-graph packet satisfies every encoded
middle equality, nonzero-weight coupling, graph condition, and permanent
target condition.
```

## Arbitrary Packet-B outcome

Return exactly one of:

```text
B2-CLOSED
B2-SURVIVOR
```

B1-CLOSED alone is not enough for lower 50.

## Packet-A outcome

Return exactly one of:

```text
A-CLOSED
A-SURVIVOR
```

Lower 50 may be promoted only after `B2-CLOSED` and `A-CLOSED`.

---

# 3. Initial effort allocation

Until B1 is decided:

```text
50%  common-graph target/integrability theorem
20%  common-graph Hilbert/ideal/weighted-coupling reductions
20%  arbitrary mixed Packet-B structural reduction
10%  Packet-A term-labelled module
```

This is a research priority guide, not a scheduling system.

---

# Workstream B1-C — common-graph theorem core

## B1-C1 — prove basis-independent interface equivalence

Prove, with all rank and invertibility hypotheses stated, the equivalence
between:

1. the full labelled Sylvester-equality condition;
2. `ker(E_4^T) subset D im(E_3)`;
3. `rank(E_4^T D E_3)=30` on an equality stratum;
4. the reciprocal-weight Hadamard formulation below.

No moving-kernel basis may be part of the theorem statement.

**Deliverable:** short proof note plus regression against the existing full
1,645-dimensional labelled calculation.

## B1-C2 — enumerate all Hilbert continuations

For each surviving pair `(H_Z(3),H_Z(4))`, enumerate every possible

\[
H_Z(5),H_Z(6),\ldots,42
\]

compatible with:

- 42 distinct reduced points in `P^6`;
- nondegenerate linear span;
- Macaulay growth using `I_d`;
- the Artinian first-difference condition;
- the proved bound `H_Z(5)<=40`;
- eventual value 42.

The four existing curve-union controls are positive controls only; they do not
prove exhaustiveness.

**Deliverable:** exact finite inventory and a proof or deterministic integer
enumerator.

## B1-C3 — derive the full multi-relation integrability system

Choose an inclusion-minimal subset `S` whose sixth powers span the seven
squarefree sextic targets. If

\[
\rho^{(1)},\ldots,\rho^{(t)}
\]

span the relations among the fifth powers on `S`, derive the complete
characteristic-zero mixed-partial compatibility equations

\[
c_i\wedge a_i
=\sum_{\alpha=1}^t\rho_i^{(\alpha)}\beta_\alpha
\]

without assuming `t=0` or `t=1`.

Record the action of changing the relation basis and identify the invariant
subspace `span(beta_1,...,beta_t)`.

**Deliverable:** symbolic theorem that specializes exactly to the already
proved zero- and one-relation arguments.

## B1-C4 — classify the two-relation frontier

Treat `t=2` as the first new hard case. Classify only the alternating-form
pencils that can actually occur in B1-C3, including:

- common-kernel strata;
- constant-rank pencils;
- decomposable and partially decomposable pencils;
- support restrictions forced by the point columns `a_i`;
- degeneration boundaries.

**Deliverable:** finite type list or a replacement invariant that avoids full
pencil classification.

## B1-C5 — support-replacement theorem

For every B1-C4 type, determine whether the supported compatible gradient can
be replaced by fewer seventh powers than the number of supported summands.
The goal is a Waring contradiction with

\[
\operatorname{WaringRank}(x_0\cdots x_6)=64.
\]

Do not claim that an arbitrary alternating-form pencil is decomposable.

## B1-C6 — extend to `t>=3` only after C4/C5

Use the structure found for `t=2` to stratify larger relation spaces by
common kernel, maximal rank, decomposable locus, and support incidence. Seek a
single inequality on replacement cost rather than an exhaustive canonical
form if possible.

**Stop rule:** if an exact compatible survivor appears, freeze it and analyze
it before adding more relation-space cases.

## B1-C7 — reduce degree-six target containment to low-dimensional blocks

Let

\[
T_6=\operatorname{span}
\{x_0\cdots\widehat{x_j}\cdots x_6:0\le j\le6\}.
\]

Rewrite `T_6 subset W_6` dually as

\[
I_6\subseteq T_6^\perp.
\]

Study the maps

\[
I_4\otimes S^2(k^7)\to S^6(k^7)\to T_6^*,
\]

and

\[
I_5\otimes S^1(k^7)\to S^6(k^7)\to T_6^*.
\]

Split by permanent row/column torus weights. The objective is the smallest
exact target-defect block equivalent to, or forced by, full target
containment.

**Deliverable:** deterministic characteristic-zero target-block evaluator and
proof of what zero defect means.

## B1-C8 — reciprocal-weight Hadamard coupling

Put

\[
w_i=d_i^{-1}.
\]

Prove and use the coordinate-free equivalence

\[
D^{-1}R_4\subseteq C_3
\iff
w\in(R_3\star R_4)^\perp,
\]

where `star` is coordinatewise product in `k^42`.

For every Hilbert sub-stratum compute or bound:

- `dim(R_3 star R_4)`;
- the dimension of the admissible weight space;
- whether it lies in a coordinate hyperplane;
- whether it meets the dense torus `(k^*)^42`;
- jump loci where the Hadamard rank drops.

This replaces unit-weight testing with the correct arbitrary-weight problem.

## B1-C9 — nonzero-weight saturation

Any algebraic elimination involving the weights must exclude `d_i=0` exactly.
Use saturation by `prod d_i`, reciprocal variables, or an equivalent finite
chart proof. A solution with one vanished graph term is not a 42-term graph
packet.

## B1-C10 — common-graph assembly lemma

Combine Hilbert continuation, integrability, target blocks, Hadamard coupling,
point distinctness, and graph nondegeneracy into one theorem-facing interface.
All six numerical Hilbert triples must instantiate the same definitions.

---

# Workstream B1-S — decide all six common-graph Hilbert triples

For clarity set

```text
S1 = (33,39,40)
S2 = (34,38,39)
S3 = (34,38,40)
S4 = (35,37,38)
S5 = (35,37,39)
S6 = (35,37,40)
```

For each `Sxx`, execute the same four decision tasks.

## B1-S1.1 through S6.1 — freeze the full stratum inventory

Freeze:

- all Hilbert continuations from B1-C2;
- dimensions of `R_d` and `I_d`;
- Hadamard coupling ranks;
- admissible nonzero-weight dimension;
- target-block ranks;
- positive characteristic-zero profile controls.

## B1-S1.2 through S6.2 — classify integrability types

Use B1-C3 through C6 to determine every multi-relation type that can occur for
that profile and Hilbert continuation. Do not transfer a type from another
profile without verifying the dimensions.

## B1-S1.3 through S6.3 — impose coupling plus target jointly

Intersect:

```text
reduced distinct points
+ exact Hilbert sub-stratum
+ invertible diagonal weights
+ weighted coupling
+ degree-six permanent target
+ graph nondegeneracy
+ integrability constraints
```

Use exact elimination only after structural reduction. Finite fields are for
component discovery and candidate minors, not nonexistence certificates.

## B1-S1.4 through S6.4 — decisive output

Return one of:

```text
Sxx-CLOSED
Sxx-SURVIVOR
Sxx-FINITE-EXACT-SUBCASES
```

The third state is temporary and accepted only when the finite list is proved
complete and small enough for exact exhaustion in the same phase.

B1 is complete only after all six triples are decided.

---

# Workstream B2-M — arbitrary mixed Packet B

## B2-M1 — write the full arbitrary mixed equality system

Keep the seven direct rank-six terms and all 42 separate rank-seven graph
complements term-labelled. State precisely which graph maps, factor bases,
and weights vary term-by-term.

## B2-M2 — identify what common-graph specialization forgets

List the true residual moduli lost when all graph complements are replaced by
one 42-point evaluation code. Do not assume these moduli are removable by a
change of basis.

## B2-M3 — derive synchronized equality data

From the slope-ten equality and

\[
\ker B\subseteq\operatorname{im}C,
\]

derive all common flags, shared quotients, synchronized relation spaces,
overlap constraints, and weight equations that are genuinely forced.

## B2-M4 — prove or falsify a common-code reduction

The preferred theorem is that every arbitrary mixed packet induces one common
pair of degree-three/four codes, or finitely many code types covered by B1.
If false, construct an exact counterexample and retain the minimal residual
moduli.

## B2-M5 — exhaustive exceptional-stratum inventory

Produce a mathematically exhaustive finite list of residual branches such as

```text
common-code
rank-drop
overlap
support partition
boundary/degeneration
genuine higher-rank perturbation
```

No branch may be introduced solely because it appeared in a random search.

## B2-M6 — map existing exact certificates

Map the already completed high-overlap, Laurent-torus, `(2,3)/(3,2)`,
`(2,4)/(4,2)`, sign, monomial, and shear certificates onto the branches from
B2-M5. This is a short proof table, not a new registry.

## B2-M7 — attack only uncovered forced branches

New computation is authorized only for a branch proved necessary by B2-M5
and not already covered. Start with the smallest structural invariant that can
distinguish it.

## B2-M8 — genuine higher-rank perturbations

If higher-rank graph perturbations survive the reduction, analyze the first
forced rank before increasing support size. Do not open unrestricted `GL_6`
brute force.

## B2-M9 — Packet-B decision

Return `B2-CLOSED` only after arbitrary allowed graph complements and every
boundary stratum are covered. Otherwise freeze one exact `B2-SURVIVOR`.

---

# Workstream A-T — all-rank-seven Packet A

## A-T1 — construct the minimal term-labelled module

For each of the 49 rank-seven Chow terms retain

\[
D_2(T_i),\quad D_5(T_i),\quad D_6(T_i)
\]

and the termwise multiplication/differentiation maps. Build the labelled
direct sums before quotienting by aggregate images.

## A-T2 — compute actual coupled capacity

Measure the permanent-side rank and the one-term contribution after the
`2/5/6` compatibility equations are imposed. Do not infer capacity by adding
uncoupled scalar maps; that route is already known to be insufficient.

## A-T3 — torus-weight block decomposition

Split the term-labelled maps by row/column permanent weights and identify the
smallest blocks capable of carrying a contradiction.

## A-T4 — degree `2/5` relation pairing

Construct the labelled complementary-degree relation pairing and write the
Sylvester equality with all term labels retained. Determine radicals and
transport maps exactly.

## A-T5 — add degree-six permanent containment

Impose

\[
E_6\subseteq H_6
\]

using the same 49 terms and coefficients as A-T4. The target may not be
optimized independently from the relation pairing.

## A-T6 — mandatory adversarial controls

Every proposed structural lemma must be tested against:

1. the exact 49-term Glynn truncation;
2. the existing non-tensor-split Sylvester-equality example;
3. a positive commuting control;
4. a control passing unlabelled Hilbert data but failing target containment.

A lemma contradicted before the permanent-specific hypotheses enter is
rejected.

## A-T7 — close strict subfamilies only with explicit scope

Decide tensor-split, row-sign, and row-uniform subfamilies using the actual
module, not withdrawn literature claims. These are useful controls but are not
Packet-A closure.

## A-T8 — decide the non-tensor simple multilinear packet

Return `A-CLOSED` or freeze an exact `A-SURVIVOR` satisfying every encoded
term-labelled cross-degree condition.

Only a genuine A-T4+A-T5 survivor authorizes escalation to a larger degree
`3/4` middle system.

---

# Workstream R — evidence, audit, and promotion

## R1 — exact arithmetic rule

Finite fields may locate components, pivots, minors, or counterexamples.
Every theorem-facing exclusion or survivor must end in exact integer,
rational, explicitly controlled number-field arithmetic, or a modular
nonzero-minor argument with a valid integer lift.

## R2 — independent replay

Every load-bearing finite computation gets one materially independent replay
or a mathematically independent certificate. The replay may not merely reload
the same frozen payload and call the same top-level routine.

## R3 — focused artifact rule

Default maximum per theorem-facing computational lemma:

```text
1 proof note
1 primary exact script
1 frozen payload
1 focused test file
1 independent replay when load-bearing
```

Additional files require a mathematical reason. No manager, database,
registry, generalized runner, or evidence platform is authorized.

## R4 — adversarial review

At every `CLOSED` or `SURVIVOR` decision check:

- characteristic and ordinary/border scope;
- reducedness and point distinctness;
- nonzero weights;
- saturation and chart boundaries;
- repeated-point and nonreduced degenerations;
- modular-rank direction;
- target equations;
- imported theorem scope;
- mandatory negative controls.

Fatal or major findings block promotion.

## R5 — lower-50 theorem assembly

Promote

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge50
\]

only when:

```text
[ ] B2-CLOSED
[ ] A-CLOSED
[ ] every finite exceptional inventory is proved complete
[ ] every load-bearing computation has characteristic-zero meaning
[ ] one independent proof-chain audit has no fatal/major finding
[ ] focused theorem-facing tests pass at one frozen HEAD
```

---

# 4. Execution waves

## Wave 1 — launch immediately

Run in parallel:

```text
B1-C2   Hilbert continuation inventory
B1-C3   full multi-relation integrability equations
B1-C7   low-dimensional degree-six target blocks
B1-C8   reciprocal-weight Hadamard coupling
B1-S1.1 first surviving profile inventory
B2-M1   complete arbitrary mixed Packet-B equations
A-T1    minimal Packet-A term-labelled module
```

Wave 1 ends when all four core B1 interfaces are frozen and at least one
surviving profile is ready for exact structural classification.

## Wave 2 — decide the hard common-graph frontier

Execute:

```text
B1-C4 through B1-C6
B1-C9 through B1-C10
B1-S1.2 through B1-S2.4
B2-M2 through B2-M4
A-T2 through A-T5
```

Preferred milestone: one complete profile closure plus a general two-relation
theorem. An exact survivor supersedes that milestone.

## Wave 3 — finish B1 and freeze the mixed reduction

Execute:

```text
remaining S1/S2/S3/S4/S5/S6 decisions
B1 assembly gate
B2-M5 through B2-M7
A-T6 through A-T7
```

Required output: `B1-CLOSED` or `B1-SURVIVOR`, plus a complete B2 exceptional
inventory.

## Wave 4 — theorem assembly

Execute:

```text
B2-M8 through B2-M9
A-T8
R1 through R5
```

Preferred outcome: lower 50. A second scientifically valid outcome is an
exact endpoint survivor that identifies the missing invariant.

---

# 5. Milestone gates

```text
P2-M1  CORE-FROZEN
       Hilbert, integrability, target-block, and Hadamard-coupling interfaces
       are exact and independently checked.

P2-M2  FIRST-STRATUM-DECIDED
       One of S1/S2/S3/S4/S5/S6 is CLOSED or has an exact characteristic-zero
       survivor.

P2-M3  B1-DECIDED
       All six triples are decided: B1-CLOSED or B1-SURVIVOR.

P2-M4  B2-REDUCTION-FROZEN
       Arbitrary mixed packets reduce to B1 plus a proved-complete finite
       exceptional inventory.

P2-M5  PACKET-B-DECIDED
       B2-CLOSED or B2-SURVIVOR.

P2-M6  PACKET-A-DECIDED
       A-CLOSED or A-SURVIVOR.

P2-M7  LOWER-50-PROMOTION
       A-CLOSED and B2-CLOSED are assembled and audited at one frozen commit.
```

---

# 6. Stop rules

Suspend unless a new proved reduction specifically reopens them:

- larger scalar derivative/shadow dynamic programs;
- more uncoupled standard Koszul or higher-wedge sweeps;
- enlargement of the old monomial-curve weight box;
- unit-weight-only Packet-B classification;
- blind random finite-field searches;
- unrestricted general-`GL_6` scans;
- indiscriminate larger mixed-Glynn families;
- duplicate recomputation of frozen overlap certificates;
- exact-64 work before the 49-term equality packets are decided;
- generalized orchestration, database, or evidence-management architecture.

A workstream also stops immediately on an exact survivor. Analyze that
survivor against the original endpoint hypotheses before opening new search
families.

---

# 7. What counts as substantive progress

Substantive progress includes:

- a complete multi-relation integrability theorem;
- exact closure of one full common-graph profile;
- an exact characteristic-zero survivor;
- a proved mixed-to-common structural reduction;
- a complete exceptional-stratum inventory;
- a permanent-specific Packet-A term-labelled defect;
- Packet-A or Packet-B closure;
- lower-50 promotion.

The following do not count by themselves:

- more random samples with the same negative result;
- another confirming prime;
- a unit-weight-only exclusion;
- a restricted family not forced by the endpoint equations;
- a prettier implementation of an existing rank test;
- new infrastructure unrelated to a theorem-facing calculation.

---

# 8. End-of-package success criterion

The preferred result is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge50}.
\]

A second theorem-scale success is an exact Packet-A or Packet-B endpoint
survivor satisfying every currently proved cross-degree equation and thereby
exposing the precise missing invariant.

The minimum acceptable end state, short of lower 50, is one equality packet
closed and the other reduced to one explicit structurally meaningful
component. Repeated closure of arbitrary restricted search families is not a
successful completion of this package.
