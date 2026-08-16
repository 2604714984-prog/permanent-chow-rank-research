# Adversarial review of the derivative-tower capacity theorem

## Verdict

```text
GENERAL_RECURRENCE=PASS_AS_PROOF_DRAFT
COUPLED_LITERAL_BOUNDARY=PASS
PERM7_ARITHMETIC=PASS_SUBJECT_TO_EXACT_REPLAY
PERM8_ROLE=REGRESSION_ONLY
GENERAL_GLYNN_OPTIMALITY=NOT_PROVED
NEW_FATAL_COUNTEREXAMPLE_FOUND=false
```

## 1. Load-bearing statement

For arbitrary degree-`n` Chow terms `T_1,...,T_q`, the theorem claims

\[
\dim\left(
\mathcal D_d(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_d(T_i)
\right)
\le B_{n,d}(q),
\]

where the array `B` is defined from four operations only:

1. the ambient dimension;
2. the literal one-term dimension;
3. one adjacent exact permanent shadow; and
4. a section/projection inequality for a retained subblock.

No numerical row is logically responsible for the general induction.

## 2. Hidden assumptions checked

### 2.1 Differentiating an intersection

For

\[
A\subseteq
\mathcal D_d(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_d(T_i),
\]

one has

\[
\partial A
\subseteq
\mathcal D_{d-1}(\operatorname{perm}_n)
\cap
\sum_i\mathcal D_{d-1}(T_i).
\]

Only containment is required. Equality is neither true in general nor used.

### 2.2 Exact shadow inversion

The inference

\[
\mathfrak F_{n,d}(\dim A)\le C
\quad\Longrightarrow\quad
\dim A\le\Gamma_{n,d}(C)
\]

uses the exact monotone product-shadow function. It is not a generic-support
or coordinate-subspace assumption: the torus-specialization theorem already
reduces arbitrary permanent subspaces to coordinate spaces with no larger
shadow, and Ferrers compression computes the true minimum.

### 2.3 Projection without a direct sum

Let `U_i=D_d(T_i)` and choose a linear section of

\[
\bigoplus_i U_i\longrightarrow\sum_iU_i
\]

over the permanent-relative intersection. Projection to the components
outside a retained block has kernel that injects into the permanent-relative
intersection of the retained block. The argument does not require the spaces
`U_i` to be independent.

### 2.4 Degenerate Chow terms

For every degree-`n` Chow term, including repeated or dependent factors,

\[
\dim\mathcal D_d(T)\le\binom nd
\]

and the factor span has dimension at most `n`. These are upper bounds, so
specialization can only make the theorem easier to satisfy.

### 2.5 Induction order

The adjacent-shadow step uses degree `d-1`, already proved by induction on
`d`. The projection step uses fewer terms at the same degree, already proved
by induction on `q`. Thus the lexicographic induction is not circular.

## 3. Strongest objections

### Objection A -- the theorem is still a disguised `perm_8` calculation

It is not. The recurrence contains no fixed value of `n`; `perm_7` and
`perm_8` are the first finite evaluations. Nevertheless, the objection is
useful as a research-governance warning: further work must study uniform
properties of `B_(n,d)(q)` rather than indefinitely optimizing one finite row.

### Objection B -- repeated recursive minimization may overcount compatible
constraints

Every recurrence branch is an independently valid upper bound, and taking the
minimum of valid upper bounds is valid. No claim is made that all branches can
be simultaneously attained or that `B` is the exact Chow-realizable maximum.

### Objection C -- the recurrence may never reach the exponential Glynn scale

This is the strongest substantive objection and is unresolved. The recurrence
retains only derivative-shadow dimensions. It can improve finite bounds while
remaining asymptotically on a central-binomial scale. The result must not be
presented as a complete route to `2^(n-1)` until a uniform asymptotic analysis
or a non-scalar defect is supplied.

### Objection D -- fixing twenty terms in the `n=7` application is illegitimate

The stacked dependency already proves `ChowRank(perm_7)>=45`. To prove lower
46, a counterexample would therefore have exactly 45 nonzero terms, so twenty
can be selected. The argument does not assume a decomposition with fewer than
the previously certified lower bound.

## 4. Assume every optimistic assumption is false

Suppose:

- the recurrence has no useful asymptotic gain;
- all near-minimizers are Chow-realizable;
- no uniform equality classification exists; and
- unrestricted ranks eventually fall below Glynn's count.

The general recurrence and the finite lower bound 46 remain valid. What fails
is only the interpretation of the recurrence as a route to the exact general
answer. The correct response would then be to retain this theorem as a finite
capacity engine and move to a frame-sensitive, multigraded or
representation-valued invariant.

## 5. Evidence responsibilities

The proof is mathematical. Computation is responsible only for the displayed
finite rows and the `perm_7` arithmetic.

Required deterministic checks:

```text
n=7 rows through degree 3 and q=5
n=8 rows through degree 3 and q=5
F_(7,4)(341)=586
F_(7,4)(342)=590
residual count=26
frozen payload equality
independent no-import replay
```

Finite-field equality, random search, floating thresholds and heuristic
optimization have no role.

## 6. Claim boundary

```text
GENERAL_DERIVATIVE_TOWER_CAPACITY=PROOF_DRAFT_COMPLETE
PERM7_ORDINARY_LOWER_BOUND=46
PERM8_ORDINARY_LOWER_BOUND=80_REGRESSION
PERM7_EXACT_RANK=OPEN
PERM8_EXACT_RANK=OPEN
BORDER_RANK=UNCHANGED
GENERAL_GLYNN_OPTIMALITY=OPEN
ASYMPTOTIC_TOWER_GAIN=OPEN
LITERATURE_NOVELTY=NOT_ESTABLISHED
```
