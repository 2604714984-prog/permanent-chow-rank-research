# `n=6` research program

## Status

`OPEN`. The current in-repository proof-draft interval is

\[
25
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

The lower bound 25 is the fixed-six relation-module argument in
`docs/n6_fixed_six_lower25.md`. The upper bound is Glynn's 32-term
decomposition. No lower-26, border-lower-25, or exact-32 claim is made.

The central first-Koszul fixed-count route, the first higher-wedge ratio route,
the scalar second-shadow route, the scalar second-Koszul homology route, and
two explicit low-base sign-aggregate constructions have now been tested. None
proves lower 26 or produces a sub-32 decomposition.

## 1. Exact numerical baseline

At central derivative degree three,

\[
\dim\mathcal D_3(\operatorname{perm}_6)=400,
\qquad
\operatorname{rank}K_{6,3}(\operatorname{perm}_6)=14175.
\]

One degree-six Chow term contributes at most 20 to the middle catalectic and
at most 705 to the first Koszul flattening.

The lower-bound history is

```text
ordinary first-Koszul ratio:            21
zero-intersection shadow removal:       22
multidimensional-shadow intersection:   23
fixed-four scalar prolongation:         24
fixed-six vector relation module:       25
```

## 2. What closed the 24-term problem

Assume a hypothetical 24-term decomposition and fix six terms. The residual
has eighteen terms. The quadratic projection cap is

\[
5\cdot15+3=78.
\]

Bukh compression and the symmetric middle catalectic give

\[
40\le b\le64,
\]

where

\[
b
=
\dim\left(
\mathcal D_3(\operatorname{perm}_6)
\cap
\mathcal D_3(R)
\right).
\]

The layers `b=40,41` are first-Koszul strict. For the other layers, the
vector-valued Macaulay theorem controls the complete colored relation module:

\[
\dim\mathcal K^{(1)}
\le
(\dim\mathcal K)^{\langle2\rangle}.
\]

A block-Sylvester inequality gives

\[
\operatorname{rank}C_{3,3}(R)
\ge
\sum_i\operatorname{rank}C_{3,3}(T_i)
-
2(\dim\mathcal K)^{\langle2\rangle}.
\]

Exact defect arithmetic excludes every `42<=b<=64`; the smallest strict
margins are two at `b=43,44`.

The proof preserves the coupled-catalectic boundary: `D_3(R)` is always the
image of the catalectic of the sum. Literal sums of individual derivative
spaces are used only as ambient spaces and explicit relation modules.

## 3. Reusable vector-valued Macaulay theorem

For arbitrary finite-dimensional `W,V` and

\[
\mathcal K\subseteq W\otimes\operatorname{Sym}^2V,
\qquad
\dim\mathcal K=k,
\]

the first prolongation satisfies

\[
\boxed{
\dim\mathcal K^{(1)}\le k^{\langle2\rangle}.
}
\]

The proof uses a universal Grassmannian kernel, upper semicontinuity, an
explicit colored-monomial one-parameter subgroup, scalar apolar Macaulay
growth, and superadditivity. The small finite-field replay is diagnostic only.

## 4. Completed lower-26 fixed-count diagnostic

A lower bound of 26 would require excluding a 25-term decomposition. Exact
fixed-count arithmetic evaluated

\[
q\in\{6,7,8\}
\]

fixed terms:

| fixed terms | initial states | central-pruned survivors | structural states | maximum relation cap |
|---:|---:|---:|---:|---:|
| 6 | 1,035 | 327 | 269 | 37 |
| 7 | 1,225 | 355 | 290 | 33 |
| 8 | 1,520 | 635 | 584 | 33 |

Six fixed terms are arithmetically smallest, but the frontier is not compact.
No fixed count is selected and the central first-Koszul state route is
suspended for lower 26.

## 5. Completed alternative-route diagnostics

### 5.1 First higher-wedge Koszul differential

For

\[
\delta_2:
D_m(f)\otimes\Lambda^2V
\to
D_{m-1}(f)\otimes\Lambda^3V,
\]

the exact output-degree ranks give integer ratios

```text
m=2: 15
m=3: 21
m=4: 16
```

identical to the corresponding ordinary first-Koszul integer bounds. The first
higher wedge does not improve the base ratio.

### 5.2 Scalar second shadow

If

\[
b=\binom{x}{3}^2,
\]

then the iterated two-dimensional shadow bound gives

\[
\dim\partial^2S\ge x^2.
\]

For every tested fixed count `q>=6`, however,

\[
\dim D_1(R)\le\min(36,6q)=36,
\]

so the result is only `b<=400`, the full ambient central dimension.

### 5.3 Scalar second-Koszul homology

The output-degree-two complex has exact ranks

\[
\operatorname{rank}\delta_2(\operatorname{perm}_6)=127125,
\qquad
\operatorname{rank}\delta_2(T)=8730
\]

for one independent Chow term. The integer ratio is 15.

A coupled common-factor family satisfies

\[
h_{2,4}\left(\sum_{i=1}^rT_i\right)
=15r+25\binom r2.
\]

At `r=6` this equals 465, already larger than the permanent's 450. Hence a
monotone scalar homology upper bound cannot prove lower 26.

### Diagnostic decision

```text
CENTRAL_FIXED_COUNT_ROUTE=SUSPENDED
HIGHER_WEDGE_BASE_RATIO=NO_IMPROVEMENT
SCALAR_SECOND_SHADOW=VACUOUS
SCALAR_HOMOLOGY_UPPER_BOUND=REJECTED
```

These are route diagnostics, not impossibility theorems for lower 26.

## 6. Xu--Gnang author postmortem

Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
arXiv:2311.05890, is the repository owner's own earlier line. It is withdrawn
and treated as disproved. Its row-homogeneous optimality claim is not a theorem
dependency, an external novelty gate, or a positive input to the current
program.

The postmortem remains useful only for recording the failed projection,
product-tensor dependence, and automorphism-rigidity steps so that they are not
reintroduced.

## 7. Completed sign-family results

Let `G=(Z/2Z)^5` index normalized six-entry sign vectors.

### 7.1 Uniform Glynn family

The 32 fixed column-uniform Glynn products are linearly independent, and the
unique expression of the permanent in their span uses every term. This is a
strict-subfamily result only.

### 7.2 One-defect family

Allow one column to use a second sign vector. The family has 5,984 distinct
terms and span dimension 987. Exact Fourier-parity analysis gives

\[
\boxed{
\operatorname{OneDefectSignRank}(\operatorname{perm}_6)=32.
}
\]

### 7.3 Two-defect parity blocks

Allow two columns to use independent defect vectors. The family has 467,264
distinct terms and exact parity-block ranks

```text
406, 406, 406, 322, 322, 207,
```

with total span dimension 11,533.

A quadratic separator first reduced base-aggregate support to 24. Exact
fixed-base atomic ranks

\[
\rho_2(f)=\rho_2(1-f)=46
\]

show that this fixed assignment costs exactly 744 actual terms.

A count-product separator

\[
g(r)=n_4(r)n_5(r)
\]

then reduced aggregate support to 16. A row retraction

```text
1,2,3 -> 0
0,4,5 fixed
```

reduces the full fixed-base dictionary for `g` to sign labels
`{0,8,16,24}` without increasing support. Exact local normal forms and a
complete extra-budget search prove

\[
\boxed{\rho_2(g)=36.}
\]

Therefore the 16-base assignment costs exactly

\[
16\cdot36=576
\]

actual terms.

### Sign-route conclusion

```text
UNIFORM_MINIMUM=32
ONE_DEFECT_MINIMUM=32
FIRST_TWO_DEFECT_FIXED_ASSIGNMENT_COST=744
SECOND_TWO_DEFECT_FIXED_ASSIGNMENT_COST=576
GLOBAL_TWO_DEFECT_MINIMUM=OPEN
```

Low aggregate support is not a reliable proxy for actual term support. Both
explicit separator constructions are closed constructive failures.

## 8. Current mathematical target: a joint aggregate-cost invariant

A two-defect decomposition can be grouped by its unique majority base. Let

\[
W_a
\]

be the pairwise aggregate attached to base label `a in G`. Fourier
transformation in the base label gives, for every parity `p`, the constraints

\[
\left.
\sum_{a\in G}\chi_p(a)W_a
\right|_{X_p}
=
\begin{cases}
1,&p=31,\\
0,&p\ne31.
\end{cases}
\tag{8.1}
\]

The actual term objective is

\[
\sum_{a\in G}\rho_2(W_a),
\tag{8.2}
\]

not the number of nonzero `W_a`.

The next sign-family theorem must act on the complete vector-valued assignment
`a -> W_a`. Candidate ingredients that remain sufficiently small are:

1. the direct sum of the 15 pure pair ANOVA blocks;
2. matrix-rank lower bounds on each pair block;
3. the exact kernels of the 32 parity-fiber restriction maps; and
4. Fourier/Reed--Muller constraints on the base-label dependence.

A useful theorem would prove a lower bound on (8.2) directly, or reduce the
search for an actual sub-32 decomposition to a small exact interface.

## 9. Hidden assumptions and their negation

### Assumptions

1. The two-defect family is broad enough to contain a shorter decomposition
   near Glynn's construction.
2. The Fourier-fiber constraints contain a joint cost invariant not visible in
   base support alone.
3. Pair-block rank and ordinary corrections can be combined without a broad
   dictionary search.
4. A useful reduction remains independently replayable.

### Assume all are false

Then the sign-family route should stop. The correct state would remain a
restricted one-defect theorem, exact two-defect block diagnostics, two failed
separator constructions, and an open unrestricted interval `25..32`.

The program must not build a generic sparse optimizer merely to preserve the
route.

## 10. Falsification first

Before promoting a joint invariant, search for a compact exact counterexample:

- an aggregate assignment satisfying (8.1) with certified actual support at
  most 31;
- a pair-block rank cancellation invalidating a proposed additive lower bound;
- a base-label Fourier codeword with support below the assumed minimum;
- a term represented under two different majority bases; or
- a finite-field compression that disappears over characteristic zero.

A dangerous example changes a characteristic-zero conclusion only after exact
rational elimination, an integer minor, or a proved semicontinuity bridge.

## 11. Next authorized sequence

### N6-24A — derive the joint lower-bound candidate

Write an explicit inequality

\[
L((W_a)_a)
\le
\sum_a\rho_2(W_a)
\]

using pair-block ranks and ordinary support. Prove it for every fixed-base
atom. Do not implement a search before this inequality is stated.

### N6-24B — optimize the linearized invariant under Fourier fibers

If `L` is explicit, compute its exact ceiling under (8.1) using symmetry and
rational linear algebra. Proceed only if the ceiling can reach at least 32 or
produces a small counterexample.

### N6-24C — independent reconstruction

Any promoted finite result must have a second implementation that rebuilds the
parity fibers, restriction kernels, and objective without importing the first
generator.

### N6-24D — stop rule

Suspend the sign route if `L` has ceiling below 32, if the optimization needs a
large nonlinear dictionary before a theorem is stated, or if the finite
interface cannot be independently reconstructed.

## 12. Fail-closed exit criteria

Suspend a route if any of the following occurs:

- it yields only an already-known integer rank ratio;
- it needs hundreds of structural states before a new theorem is stated;
- its shadow dimension is bounded only by the ambient dimension;
- it assumes equality between a coupled catalectic image and a literal sum;
- it relies on finite-field equality without characteristic-zero transfer;
- it optimizes aggregate count while ignoring actual atomic cost;
- its symmetry quotient cannot be reconstructed independently; or
- an exact decomposition or counterexample invalidates its premise.

## 13. Strongest objection

Even an exact lower bound of 32 inside the full two-defect sign family would
remain a theorem for a highly special proper subfamily. It would not prove
unrestricted Chow rank 32 or lower 26.

That objection is decisive for project scope. N6-24 is authorized only because
it may either construct a shorter explicit decomposition or supply a reusable
Fourier-cost invariant. It is not grounds for a full column-sign solver,
row-homogeneous tensor-rank program, or new process architecture.
