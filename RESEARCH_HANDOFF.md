# Research handoff

This is the canonical operational handoff for the active permanent Chow-rank
research stack. Every synchronized result must update this file.

Last updated: **2026-08-19**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-natural-span-barriers
active PR: #88
active theorem head: 8d2a6119d9c37d6f3198ed38bbd6e55982e7acba
parent branch: research/quartic-three-block-zero
parent PR: #87
parent exact head: 93a6227b8fd3cc828d40e12f0b32d56c987366f0
stack ancestry: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88
```

Keep the stack narrow. Do not introduce a manager, registry, dispatcher,
database, broad solver framework, or second control plane.

## 2. Latest result

### Quartic natural-span compression barriers

The unrestricted interval remains

```text
5 <= mu(6,4) <= 8.
```

Two natural internal compression routes are now closed exactly.

#### `(2,2)` partition-Laplace span

Let `L_22` be the six-dimensional span of the fixed-row-split summands

```text
G_C = perm(X_{01,C}) perm(X_{23,C^c}), |C|=2.
```

For a nonzero combination with coefficient support `S`,

```text
dim Ess = 2*|union_(C in S) C| + 2*|union_(C in S) C^c|.
```

Hence every nonzero vector has essential dimension at least eight. Every
output-degree-four derivative of a degree-six Chow term has essential
dimension at most six, so

```text
L_22 intersect D_4(T) = 0
```

for every degree-six Chow term `T`.

#### Glynn sign span

Let `H` be the eight-dimensional order-four Glynn sign span. For every
nonzero `h in H`, row symmetry gives

```text
dim Ess(h) = 4 * mode_rank(h).
```

The vectors with essential dimension at most six are exactly the eight
original sign lines. Therefore `H intersect D_4(T)` is zero or one sign line
for every degree-six Chow term, and the internal degree-six block minimum for
expressing `perm_4` with components individually constrained to `H` is exactly
eight.

These are strict internal-span barriers. Components outside the natural
spaces may still cancel in the ambient quotient.

## 3. Proof spine

The Laplace theorem uses disjoint derivative supports. For a top-row
derivative, a selected pair `C={c,d}` leaves the unique row-one variable
`x_(1,d)`; different pairs cannot cancel. The bottom rows give the complement
formula. Summing the four row contributions yields the exact essential
Dimension formula.

For the Glynn span, every generator is `delta^(tensor 4)` after identifying
the four row spaces. If the essential dimension is at most six, the common
mode rank is one and the tensor is `c v^(tensor 4)`. Parity-zero Walsh
coordinates force

```text
v_i^4 = v_i^2 v_j^2 = v_j^4,
```

so all coordinates are nonzero and have equal squares. Up to scale, `v` is
one of the eight sign vectors. The unique Glynn expression of `perm_4` has
all eight coefficients nonzero.

## 4. Exact interfaces and validation

```text
Laplace basis vectors                              6
permanent monomials partitioned                   24
nonempty Laplace supports checked                 63
essential-dimension distribution      8:6, 12:12, 14:8, 16:37
Walsh parity classes                               8
ordered tensor coordinates checked               256
normalized low-essential sign lines                8
focused unit tests                              5/5 PASS
primary normal Python                             PASS
primary python -O                                 PASS
independent normal Python                         PASS
independent python -O                             PASS
py_compile                                        PASS
frozen JSON == regenerated payload               PASS
```

Frozen theorem-facing core:

```text
d40eef4be59483e19dced0f69232b79bdcead026531aac018f3490ee44104145
```

The independent implementation imports none of the primary code. It expands
all Laplace polynomials directly, computes rational derivative ranks, and
reconstructs the sign tensors on all ordered coordinates. Its odd-prime
projective enumeration is diagnostic only; the characteristic-zero theorem is
the explicit parity argument.

## 5. Files

```text
docs/general_quartic_natural_span_compression_barriers.md
docs/general_quartic_natural_span_compression_barriers_adversarial_review.md
docs/general_quartic_natural_span_compression_barriers_ledger_delta.md
scripts/general_quartic_natural_span_barriers.py
scripts/general_quartic_natural_span_barriers_independent.py
data/general_quartic_natural_span_barriers.json
tests/test_general_quartic_natural_span_barriers.py
RESEARCH_HANDOFF.md
```

## 6. Parent results retained

PR #87 proved

```text
D_4(perm_8) intersect sum_(i=1)^3 D_4(T_i) = 0
mu(8,4) = 4.
```

PR #86 proved

```text
D_4(perm_6) intersect sum_(i=1)^4 D_4(T_i) = 0
5 <= mu(6,4) <= 8.
```

The quartic `q*n=24` arithmetic boundary remains completely classified.

## 7. Hosted CI state

PR #88 hosted full CI is pending at this handoff update. The focused result has
a clean local exact replay. Do not describe the full repository suite as green
until the hosted run completes and the inherited exact-product-shadow
compatibility regression is resolved or reclassified.

## 8. Strict claim boundary

```text
classification = STRICT_ROUTE_BARRIER
(2,2) Laplace internal recombination = IMPOSSIBLE
Glynn internal degree-six minimum = 8
mu(6,4) exact unrestricted value = OPEN in [5,8]
new unrestricted Chow-rank bound = false
new exact Chow rank = false
border-rank improvement = NO
coupled/literal identification = NO
literature novelty = NOT ESTABLISHED
hosted full CI = PENDING
```

The following implications are forbidden:

```text
Glynn internal minimum 8 => mu(6,4)=8
L_22 intersect D_4(T)=0 => no six-term ambient-cancellation sum
finite-field diagnostic => characteristic-zero proof
```

## 9. Next executable task

Return to the unrestricted five-term problem. For a hypothetical

```text
0 != f = f_1 + ... + f_5 in D_4(perm_6),
```

annihilating a complementary pair of component essential spaces produces a
triple-supported cubic polar space of dimension at least four. Classify those
four-dimensional cubic three-block spaces using the exact cubic literal
minimum `mu(6,3)=2`, the PR #86 pair-equality state
`(6,6,intersection 3,joint 9)`, and exact quadratic shadow tables.

On the constructive side, every valid five-, six-, or seven-term search must
allow the components to leave both `H` and `L_22` and cancel outside the
natural span. Promote only an explicit construction, a universal zero theorem,
or another strict route barrier.

## 10. Mandatory synchronization rule

Every future synchronized result must record exact branch, PR and head;
theorem or route barrier; dependencies; scripts, data and tests; focused and
hosted validation; superseded statements; and one next executable task. A
result is not handed off merely because it appears in chat.

## 11. Handoff log

### 2026-08-19 -- quartic natural-span barriers

- proved the exact essential-dimension formula in the `(2,2)` Laplace span;
- proved that this span meets every degree-six Chow derivative component only
  at zero;
- classified the low-essential locus of the Glynn sign span;
- proved the Glynn-internal degree-six minimum is eight;
- retained the unrestricted interval `5<=mu(6,4)<=8`;
- returned the active frontier to the unrestricted five-term geometry.

### 2026-08-19 -- quartic three-block zero

- closed `(8,4,3)` as universal zero;
- proved `mu(8,4)=4`;
- completed the quartic `q*n=24` arithmetic classification.

### 2026-08-19 -- quartic four-block zero

- closed `(6,4,4)`;
- obtained `5<=mu(6,4)<=8`.

### 2026-08-19 -- exact cubic literal threshold

- proved the exact function `mu(n,3)`.
