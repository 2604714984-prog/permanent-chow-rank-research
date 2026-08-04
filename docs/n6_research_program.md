# `n=6` research program

## Status

`OPEN`. The current in-repository proof draft gives

\[
24
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 24 excludes a 23-term decomposition by closing the fixed-four frontier. The upper bound is Glynn's 32-term decomposition. Neither a lower bound of 25 nor the exact value 32 has been proved.

## 1. Current exact baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
A_{6,3}=14175.
\]

One degree-six Chow term has capacities

\[
\operatorname{rank}C_{3,3}(T)\le20,
\qquad
\operatorname{rank}K_3(T)\le705.
\]

The proved ordinary-rank history is:

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
component-prolongation closure:         24
```

The last step fixes four terms under a hypothetical 23-term decomposition and uses:

- the individual quadratic intersection cap three;
- exact Bukh-shadow defect budgets;
- scalar Macaulay first-prolongation caps;
- componentwise cubic-relation bounds;
- a coupled block-Sylvester middle-catalectic inequality;
- the exact degree-six term profiles;
- the quotient-Koszul budget for the final low-intersection states.

No border-rank lower bound of 24 follows from this argument.

## 2. The next milestone is lower 25, not exact 32

To prove

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge25,
\]

one must exclude a hypothetical 24-term decomposition

\[
P=T_1+\cdots+T_{24}.
\]

Fix `q` terms with sum `R` and residual `Q=P-R`. The residual capacities are

\[
20(24-q)
\]

at the middle catalectic and

\[
705(24-q)
\]

at the first Koszul flattening.

The exact relation between the central intersection and quotient data must be regenerated for this 24-term hypothesis. The closed 23-term state table must not be reused by changing one constant.

## 3. Hidden assumptions

The lower-25 program would be unsound if it silently assumed any of the following.

1. The fixed-four decomposition is still the best choice after the residual count changes from 19 to 20.
2. The componentwise prolongation bound remains strict on the new extremal layers.
3. The exact term profile is determined by its quadratic dimension at every new defect level.
4. A finite list of exceptional relation spaces can be classified cheaply.
5. Positive quotient Koszul gain is close to additive for several coupled terms.
6. Glynn's 32-term upper bound is the exact answer.

None is currently promoted to a theorem.

## 4. Assume every assumption is false

Then the fixed-term central route may have reached its natural limit at lower bound 24. A hypothetical 24-term decomposition could occupy a positive-dimensional family with:

- broad quadratic relation kernels;
- large cubic prolongations;
- substantial cancellation in the coupled middle catalectic;
- quotient gain too small to exceed the residual Koszul capacity.

In that case, enumerating more defect states would not constitute progress. It would only encode the failure of the invariant more elaborately.

## 5. No-background assessment

Without relying on the previous route history, the mathematically natural next checks are:

1. recompute the fixed-`q` arithmetic for the 24-term hypothesis;
2. measure the size of the surviving state sets before proving new geometry;
3. reject any `q` whose structural frontier remains broad;
4. only then choose between a stronger relation-space theorem and a different flattening.

This assessment does not justify SAT, Hilbert-scheme, Kuranishi, manager, registry, dispatcher, or multi-repository machinery.

## 6. Minority but complete alternative

A reasonable minority position is to stop pursuing small-`n` exactness now and move to general asymptotic lower bounds.

The logic is:

- lower 24 already required a long chain of special `n=6` geometry;
- the gap from 24 to 32 remains eight terms;
- each additional exact step may need a qualitatively stronger invariant;
- the general multidimensional-shadow theorems apply to every `n` and may have higher research leverage.

This alternative becomes preferable if the first lower-25 diagnostic fails to produce a small frontier.

## 7. Recommended minimal program

### N6-14 — completed fixed-`q` arithmetic diagnostic

For `q=4,5,6`, the exact diagnostic independently rebuilt:

- the Bukh-shadow intersection range;
- the central double-quotient state range;
- the relation-kernel caps;
- the component-prolongation central lower bounds;
- the quotient-gain requirement;
- any sufficient relative-prolongation cap.

The result was:

```text
q=4: 406 initial states, 260 after component pruning
q=5: 325 initial states, 184 after component pruning
q=6: 325 initial states, 179 after component pruning
```

The post-pruning counts include the already strict quotient-Koszul states. Removing those gives unresolved counts

```text
q=4: 254
q=5: 181
q=6: 176
```

Six fixed terms are numerically smallest, but the frontier remains broad: 141 of its 176 unresolved states require structural exclusion or a stronger invariant. Therefore no fixed term count is promoted to the proof route.

### N6-15 — projection-profile theorem or route rejection

For every remaining high-intersection state, study

\[
\mathcal K
=
\ker\left(
\bigoplus_i\mathcal D_2(T_i)
\longrightarrow
\sum_i\mathcal D_2(T_i)
\right)
\]

and its projected spaces

\[
P_i=\operatorname{pr}_i\mathcal K.
\]

The next useful theorem would bound

\[
\sum_i\dim P_i^{(1)}
-
\dim\left(\sum_iP_i^{(1)}\right)
\]

more sharply than the universal componentwise Macaulay cap. A result that does not eliminate a whole interval of `(b,d)` states is too weak to justify further classification.

### N6-16 — alternative invariant comparison

If N6-15 does not produce bulk elimination, compare only a small set of alternatives:

- another Koszul output degree;
- a Young or shifted-partial flattening;
- coupled first and second derivative shadows;
- a border-sensitive determinantal obstruction.

For each candidate, compute the per-term capacity and the required residual rank before implementing a large matrix.

### N6-17 — falsification search

Search structured families for:

- a reproducible 24-term decomposition;
- fixed sums with central and Koszul ranks near the derived capacities;
- relation kernels attaining the Macaulay component caps;
- quotient gains below the level required by every tested fixed-`q` route.

Finite-field results remain diagnostic until lifted by exact rational elimination, an integer minor, or a proved semicontinuity argument.

### N6-18 — exact 32 only after another strict lower bound

Do not launch a direct 31-term exclusion, a global secant search, or a large decomposition solver before lower 25 or another comparably strict theorem is established.

## 8. Promotion rule

A new `n=6` result may enter the status ledger only if:

1. the hypothetical decomposition size is explicit;
2. the residual term count is recomputed from that hypothesis;
3. every coupled derivative space comes from the catalectic of the sum;
4. every replacement by a literal sum has a separate directness or relation-kernel proof;
5. every state table has a deterministic generator and frozen identity;
6. modular ranks have matching characteristic-zero justification;
7. the final claim is no stronger than the proved strict inequality.

## 9. Fail-closed exit criteria

Suspend the lower-25 central route if any of the following occurs:

- the smallest exact fixed-`q` frontier remains broad;
- the new relation-kernel cap permits cubic prolongations large enough to consume the full rank margin;
- the remaining cases form an uncontrolled positive-dimensional family;
- a structured 24-term candidate is found;
- a different flattening has a clearly stronger capacity ratio;
- the next proof requires broad infrastructure before a finite theorem has been identified.

## 10. Optimistic and pessimistic frames

### Optimistic

The 24-term hypothesis may have a new extremal layer whose equality conditions force high-dimensional individual derivative spaces and a small relation kernel. A module-level prolongation theorem could then eliminate many states at once and produce lower 25 without a case registry.

### Pessimistic

The extra residual term may remove every strict margin. If so, dimension-only component bounds will plateau, projected relation spaces will vary in positive-dimensional families, and the current central invariant will not prove lower 25.

The first exact fixed-`q` diagnostic supports the pessimistic frame for the current dimension-only bound: even the best tested choice leaves 176 unresolved states.

## 11. Strongest objection to the recommendation

The strongest objection is that rejecting the current route after the broad diagnostic may be premature: a single module-level theorem for vector-valued quadratic relation spaces could improve the prolongation bound simultaneously across all states.

That objection is valid and defines N6-15. It does not justify a state registry. The theorem must be formulated and tested as a bulk inequality first; if it fails to remove a wide interval, the route should be suspended.
