# `perm_7` lower-50 next-phase task plan

## Status and claim boundary

`ACTIVE RESEARCH PLAN — NOT A NEW CHOW-RANK RESULT.`

Created: 2026-08-22  
Input research snapshot: `bfb2b0e241fb17f061309fe82bd2502547631264`  
Active research PR: `#31`

The current ordinary characteristic-zero interval is

\[
49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

The next promotion target is exactly

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\geq50.}
\]

This plan does not claim lower 50, exact rank 64, border rank, or a general
formula for `perm_n`. It records the shortest current path to a theorem and
explicitly stops work on routes that have reached a proved capacity ceiling.

## 1. Frozen starting point

The following facts are treated as the input boundary for this phase.

1. The complete scalar derivative tower proves lower 49. Its exact `n=7`
   saturation thresholds through degree six are

   ```text
   7, 22, 39, 46, 48, 49.
   ```

2. More scalar shadow dynamic programming, additional scalar derivative
   degrees, and further scalar block-projection closure are not the primary
   route beyond 49.

3. Standard higher-wedge Koszul maps and their uncoupled nonnegative direct
   sums have an optimistic integer ceiling at most 61. They cannot by
   themselves establish exact 64.

4. At a hypothetical 49-term identity, the slope-ten endpoint argument leaves
   exactly two global equality packets:

   - **Packet A:** all 49 terms have factor rank seven;
   - **Packet B:** seven rank-six equality terms span a direct 42-space and
     the other 42 terms are rank-seven graph complements.

5. Both packets must satisfy term-labelled cross-degree equality, not merely
   scalar dimension bounds. In particular, the relevant Sylvester equality
   contains a condition of the form

   \[
   \ker B\subseteq\operatorname{im}C.
   \]

6. In the common-graph specialization of Packet B, with point-evaluation maps
   `E_3,E_4` and nonzero diagonal term-weight matrix `D`, the correct coupling
   condition is

   \[
   \boxed{\ker(E_4^T)\subseteq D\operatorname{im}(E_3).}
   \]

   The weights cannot be normalized away in a general classification.

7. The existing monomial-curve box is a completed restricted family. All 130
   scalar-equality candidates in that box fail the permanent target equations
   for every choice of nonzero term weights. Enlarging the same blind weight
   box is not the next task.

The principal source files for this boundary are:

```text
docs/general_full_degree_tower_envelope.md
docs/general_scalar_tower_polynomial_ceiling.md
docs/n7_multidegree_capacity_inventory.md
docs/n7_slope10_rectangular_endpoint.md
docs/n7_packet_b_curve_coupling_probe.md
docs/n7_equality_packet_crossdegree_search.md
docs/n7_higher_overlap_resume.md
docs/n7_glynn49_quadratic_interface_counterexample.md
```

## 2. Phase objective

Exclude both 49-term equality packets by permanent-specific, cross-degree
arguments.

The phase is complete only after proving

```text
Packet A impossible
AND
Packet B impossible
```

for an actual identity

\[
\operatorname{perm}_7=\sum_{i=1}^{49}T_i.
\]

Closing a restricted family, a finite sample, one coefficient normalization,
or one affine chart is not sufficient for promotion.

## 3. Priority allocation

Research effort should be allocated approximately as follows:

```text
65%  weighted Packet-B equations and permanent-target incompatibility
25%  Packet-A term-labelled cross-degree structure
10%  independent replay, adversarial checks, and frozen evidence
```

This is a priority guide, not a scheduling framework. No new manager,
registry, database, or generalized experiment platform is required.

---

# Workstream B1 — weighted common-graph Packet B

## Goal

Decide the characteristic-zero solvability of the complete weighted
common-graph equality system.

Let `Z=(z_1,...,z_42)` denote the graph-tail points and let

\[
D=\operatorname{diag}(d_1,\ldots,d_{42}),\qquad d_i\neq0.
\]

The system must retain all three interfaces:

1. scalar middle equality;
2. weighted cross-degree coupling;
3. permanent target containment.

The target system is therefore schematically

\[
\begin{cases}
\operatorname{rank}E_3+\operatorname{rank}E_4=72,\\
\ker(E_4^T)\subseteq D\operatorname{im}(E_3),\\
E_6\subseteq H_6(Z,D),\\
E_7\subseteq H_7(Z,D)\quad\text{if degree six does not already close the case},\\
\text{graph-complement rank and nonvanishing conditions}.
\end{cases}
\]

On a fixed equality-rank stratum, the coupling equation may be represented
without choosing a moving kernel basis by

\[
\boxed{\operatorname{rank}(E_4^TDE_3)=30.}
\]

This rank form is valid only together with the equality ranks and invertibility
of `D`; those hypotheses must remain explicit in every elimination.

## Tasks

### B1.1 — enumerate the actual equality-rank strata

Determine all feasible pairs

\[
(r_3,r_4)=(\operatorname{rank}E_3,\operatorname{rank}E_4)
\]

under the Packet-B equality hypotheses. Do not infer that the two profiles
observed in the monomial-curve box are globally exhaustive without proof.

**Output:** a short characteristic-zero lemma or an explicit finite list of
unresolved rank strata.

### B1.2 — formulate the degree-six target equations

Construct the smallest term-labelled matrix or quotient test that is
equivalent to

\[
E_6\subseteq H_6(Z,D)
\]

on each B1.1 stratum. Preserve the diagonal weights. Prefer row/column or
multidegree blocks to one large undifferentiated matrix.

**Output:** exact symbolic equations and a deterministic evaluator.

### B1.3 — combine coupling and degree-six containment

Analyze the ideal or determinantal system formed by

```text
middle equality
+ weighted coupling
+ degree-six permanent containment
+ graph nondegeneracy
```

Degree seven is added only if degree six leaves a genuine survivor.

Use finite fields only to locate components, choose pivots, or falsify proposed
lemmas. Every promoted exclusion or survivor must be certified in
characteristic zero by exact rational, integer, or explicitly controlled
number-field computation.

### B1.4 — return one of two decisive outcomes

The workstream stops when it produces either:

```text
B1-CLOSED:
No weighted common-graph Packet-B solution exists in characteristic zero.
```

or

```text
B1-SURVIVOR:
An exact characteristic-zero weighted solution to every encoded equality,
coupling, graph, and permanent-target equation.
```

A survivor is not automatically a 49-term decomposition. It must first be
checked against every hypothesis used in the Packet-B reduction. However, an
exact survivor takes priority over further exclusion searches.

## Promotion gate

No common-graph theorem is promoted from:

- unit weights only;
- one or two finite fields;
- a larger monomial-curve weight box;
- generic random graph complements;
- a rank computation that omits the permanent target equations.

---

# Workstream B2 — arbitrary mixed graph-complement Packet B

## Goal

Upgrade the B1 result from a common-graph specialization to every mixed
Packet-B equality configuration.

## Tasks

### B2.1 — derive a structural reduction before further enumeration

Prove that an arbitrary equality packet either:

1. reduces to a common-code/common-graph model covered by B1; or
2. belongs to a finite list of explicit support, overlap, rank-drop, or
   boundary strata.

A failed reduction is also informative: record the precise extra moduli that
survive and construct the smallest exact test for them.

### B2.2 — reuse the existing exclusion library

Apply, rather than duplicate, the completed exact certificates for:

- high-overlap dense strata;
- the repaired Laurent-torus boundary audit;
- overlapping `(2,3)/(3,2)` rank-one updates;
- overlapping `(2,4)/(4,2)` rank-one updates;
- signed, monomial, elementary-shear, and other already closed restricted
  families.

New computation is authorized only for a stratum that is explicitly produced
by B2.1 and is not already covered.

### B2.3 — avoid unrestricted `GL_6` brute force

Do not begin a general `GL_6` scan without a theorem reducing the equality
packet to finitely many tractable strata. Large parameter searches without
such a reduction are diagnostic only and cannot close Packet B.

## Decisive outcomes

```text
B2-CLOSED:
Every mixed graph-complement equality packet is impossible.
```

or

```text
B2-SURVIVOR:
An exact characteristic-zero packet satisfying every currently proved
Packet-B equality and permanent-target condition.
```

Packet B is closed only after B2-CLOSED. B1-CLOSED alone is insufficient.

---

# Workstream A — all-rank-seven Packet A

## Goal

Exclude, or structurally classify, the equality packet of 49 rank-seven Chow
terms whose factor seven-planes form the forced simple multilinear matroid.

## Known barrier

Unlabelled Hilbert data, quadratic containment, factor-plane incidence, and
current scalar erasure bounds do not suffice. The exact 49-term Glynn
truncation counterexample satisfies these weaker interfaces while failing
permanent containment in higher degree.

Therefore this workstream must retain term labels and complementary-degree
compatibility.

## Tasks

### A.1 — construct the minimal term-labelled cross-degree module

Start with the smallest useful combination of

\[
D_2(T_i),\quad D_5(T_i),\quad D_6(T_i)
\]

and the termwise multiplication/differentiation maps between them.

The first candidate interfaces are:

- the degree `2/5` relation pairing;
- degree-six permanent target containment;
- the corresponding Sylvester equality condition.

Degree `3/4` is added only if the smaller interface leaves a genuine survivor.

### A.2 — split by permanent torus weights

Use row/column multidegrees or torus weights to replace a single huge matrix
by small exact blocks. The aim is a theorem, such as:

- one target block must have positive defect;
- equality forces a tensor-split or column-uniform normal form;
- a term-labelled relation cannot be simultaneously realized in complementary
  degrees.

### A.3 — adversarially test every proposed lemma

The 49-term Glynn truncation and existing non-tensor-split Sylvester-equality
examples are mandatory controls. A proposed structural lemma is rejected if
it is contradicted by either control before permanent-specific hypotheses are
used.

## Decisive outcomes

```text
A-CLOSED:
No all-rank-seven 49-term equality packet can satisfy the permanent identity.
```

or

```text
A-SURVIVOR:
An exact characteristic-zero packet satisfying every encoded term-labelled
cross-degree condition.
```

An exact survivor is investigated before expanding the search family.

---

# 4. Execution order

The default order is:

```text
1. B1.1  Freeze all weighted common-graph equality strata.
2. B1.2  Build the degree-six permanent-target interface.
3. B1.3  Solve coupling + target jointly in characteristic zero.
4. B2.1  Derive the arbitrary-Packet-B structural reduction.
5. B2.2  Reuse existing certificates and close only newly exposed strata.
6. A.1   Build the minimal Packet-A term-labelled module.
7. A.2   Prove a permanent-specific block defect or structural normal form.
8. Combine A-CLOSED and B2-CLOSED to promote lower 50.
```

Packet-A work may proceed in parallel at low intensity, but it must not divert
the main effort from the more concrete weighted Packet-B system.

## Immediate next task

The first implementation task is narrowly defined:

> On the weighted common-graph Packet-B model, derive an exact block matrix for
> degree-six permanent containment and combine it with the fixed-stratum rank
> condition `rank(E_4^T D E_3)=30`.

The first checkpoint should answer:

1. Which equality-rank strata are genuinely feasible?
2. What is the smallest symbolic matrix for the degree-six target condition?
3. Does the existing weighted `(31,41)` coupling control survive that target
   condition in characteristic zero?
4. If not, can the failure be certified by an exact minor or elimination
   identity?

No broader computation is started before these four questions are resolved.

# 5. Stop rules

The following work is suspended unless a new theorem explicitly reopens it:

- larger scalar derivative/shadow dynamic programs;
- additional uncoupled standard Koszul sweeps;
- direct transfer of the `perm_6` single-middle-layer proof;
- larger blind random finite-field searches;
- increasing the maximum weight in the same monomial-curve family;
- unit-weight-only Packet-B classification;
- unrestricted general-`GL_6` scans;
- unstructured expansion to larger mixed-Glynn support families;
- an exact-64 program before the two 49-term equality packets are understood.

A workstream also stops immediately when it finds an exact survivor. The
survivor must be analyzed before adding more exclusion cases.

# 6. Evidence and review standard

For every theorem-facing result:

1. state the exact characteristic and ordinary-rank scope;
2. separate proved statements from finite-field diagnostics;
3. record the precise input commit and generated evidence hashes;
4. use exact arithmetic for the final certificate;
5. provide one independent replay when a finite computation is load-bearing;
6. include a negative control that would fail if term weights or target
   equations were accidentally omitted;
7. keep the artifact set minimal: one proof note, one replay, one frozen
   payload, and focused tests when those components are actually needed.

A planning-only change needs no artificial data file or test. The repository
CI and English-language policy remain the only gates for this document.

# 7. Lower-50 promotion gate

The statement

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\geq50
\]

may be promoted only when all of the following hold:

```text
[ ] Packet B is excluded for arbitrary term weights and arbitrary permitted
    graph complements, not only a common graph or restricted transform family.
[ ] Packet A is excluded using permanent-specific term-labelled cross-degree
    equations.
[ ] Every load-bearing finite computation has exact characteristic-zero
    interpretation and deterministic replay.
[ ] An adversarial review finds no fatal or major gap.
[ ] The frozen theorem-facing tests pass at one exact commit.
```

Until then, the repository status remains

\[
\boxed{49\leq\operatorname{ChowRank}(\operatorname{perm}_7)\leq64.}
\]

# 8. Success criterion for this phase

The preferred successful output is a lower-50 theorem. A second valid outcome
is an exact survivor that demonstrates why the present endpoint formulation is
insufficient and identifies the missing invariant.

Repeated exclusion of larger restricted families without either outcome is
not considered substantive progress.