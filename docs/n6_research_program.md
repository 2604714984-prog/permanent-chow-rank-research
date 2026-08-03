# `n=6` research program

## Status

`OPEN`. The currently proved in-repository lower bound is

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge22,
\]

while Glynn gives the upper bound 32.

## Repository-independent numerical baseline

Use the central derivative degree `m=3`:

\[
\dim \mathcal D_3(P_6)=\binom63^2=400,
\qquad
\dim \mathcal D_4(P_6)=\binom64^2=225.
\]

Hence

\[
A_{6,3}=36\cdot400-225=14175.
\]

One six-factor Chow term contributes at most

\[
B_{6,3}=36\cdot20-15=705.
\]

The ordinary ratio gives 21; the shadow-removal theorem removes one certified term and gives 22.

## Exact target reduction

To prove the conjectural exact value 32, assume a 31-term decomposition and fix 11 terms with sum `R`. The residual 20 terms have flattening capacity

\[
20\cdot705=14100.
\]

It is enough to prove

\[
\operatorname{rank}K_{6,3}(P_6-R)\ge14101
\]

for every such `R`; proving the stronger lower bound 14175 would also suffice.

The central catalecticant `C_{3,3}` is self-transpose. This removes the specific odd-degree row/column image mismatch that complicated the `n=5` proof, but it does not remove all coupling or degeneration issues.

## Hidden assumptions

1. **Glynn is optimal for unrestricted Chow rank.** This may be false even if it is optimal in a restricted row-homogeneous model.
2. **The `n=5` finite-frontier method scales.** State growth may become intractable or the relevant boundary may acquire new positive-dimensional components.
3. **The central first-Koszul flattening is sufficient.** It may saturate far below 32 even after refined intersection accounting.
4. **Torus degeneration preserves a classifiable boundary.** Non-reduced limits and intersection jumps may dominate.

## Assume every assumption is false

Then the correct program is not to enlarge a fixed-state SAT search. It is to run two falsification tracks first:

- search for structured decompositions with fewer than 32 terms;
- search for explicit 11-term sums `R` that make the central residual rank unusually small.

Any such example must be treated as a counterexample to the proposed proof route, not as a numerical nuisance.

## Minority complete logic

A plausible alternative objective is an asymptotically stronger lower bound rather than exact Glynn optimality. Higher Koszul, recursive Koszul, or nonlinear secant equations may improve the central-binomial scale without solving the exact rank. This route is mathematically valuable even if the exact conjecture fails.

## Optimistic frame

- self-transpose `C_{3,3}` collapses the `J/H` semantic split;
- the permanent derivative basis is multiplicity-free for the row-column torus;
- shadow compression may reduce the dangerous intersections to finitely many small orbit types;
- a fixed-11 reduction could expose a strict rank margin of only 75, which is small enough for refined accounting.

## Pessimistic frame

- the 75-rank margin may be consumed by a three-dimensional intersection;
- global prolongation bounds in a quotient of `Sym^3(V_6)` may be too weak;
- non-reduced torus limits may require Hilbert-scheme or Kuranishi analysis at substantially greater complexity than `n=5`;
- a 31-term decomposition may exist.

## Recommended minimal program

### N6-0 — deterministic baseline

Keep the formulas, exact bound table, and regression tests stable. No large certificate framework.

### N6-1 — shadow frontier

Study the lower derivative shadow of coordinate families in

\[
\binom{[6]}3\times\binom{[6]}3.
\]

Start with compression and exact enumeration only for the small intersection dimensions that can consume the 75-rank margin.

### N6-2 — route falsification

Construct random and structured 11-term Chow sums over small finite fields as **diagnostics only**. Record the smallest observed residual rank and all intersection dimensions. No finite-field equality may be promoted to characteristic-zero evidence.

### N6-3 — exact representative replay

For any dangerous orbit representative, rebuild the relevant integer matrix and establish rank with a rational computation or a certified nonzero integer minor.

### N6-4 — geometry only after a finite frontier exists

Introduce Hilbert-scheme, SAT/DRAT, or Kuranishi machinery only after the dangerous states are mathematically proved finite and small. Do not create managers, registries, dispatchers, or multi-repository orchestration.

## Strongest objection to this recommendation

The two-track approach may spend substantial effort on lower bounds that cannot approach 32. A direct decomposition search could be more decisive. The response is to time-box N6-1 and N6-2: if no strict structural margin appears, the central-Koszul exact route should be rejected rather than expanded indefinitely.
