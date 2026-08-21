# Research handoff

Canonical operational handoff for the active permanent Chow-rank research stack.

Last updated: **2026-08-22**

## 1. Active GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/quartic-six-circuit-compatibility
active Draft PR: #92
parent branch: research/quartic-six-term-frontier
parent PR: #89
parent exact head: 4804e9a948fa0602c062d167f0474d1346dbcab9
first-order-eight-term theorem core: 8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
current engineering-fix head: 21ae89f5fdd7fb4524c7aa2fde4a9ccc18eaa68e
current workflow: exact-bound-tests run #851, in progress at this update
stack tail: PR #82 -> #83 -> #84 -> #85 -> #86 -> #87 -> #88 -> #89 -> #92
```

Keep the stack narrow. Do not introduce a manager, registry, database, broad
solver framework, or second control plane.

## 2. Current unrestricted boundary

For arbitrary degree-six Chow terms over a characteristic-zero field,

\[
\mathcal D_4(\operatorname{perm}_6)
\cap
\sum_{i=1}^{5}\mathcal D_4(T_i)=0.
\]

Hence

\[
\boxed{6\le\mu(6,4)\le8},
\qquad
\boxed{28\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32}.
\]

Six and seven arbitrary literal blocks remain open. Eight are nonzero by the
padded order-four decomposition.

## 3. Inherited PR #89 interfaces

PR #89 supplies the five-block zero theorem, exact natural-family barriers,
partition-Laplace essential stratification, the 15-dimensional common-source
mixed-slice interface, and the unique full-support six-element quotient
circuit for a hypothetical six-block witness.

Key frozen cores:

```text
five-block zero:
72a73cc0012e7113f1a483150b61c8e7444310c38542b1d5bca40c9182c15171

partition-Laplace essential stratification:
1bcbe6b3d3594f649171a21d8837b2a811596858f60dd2b41c52268484525e6c

common-source / quotient circuit:
d82e88706313fb20bd8cf0e51d7ab7a7fadac00d9805d72d2fd1b2ccd1d6d85c
```

## 4. PR #92 coordinate results

### 4.1 All-positive regular coordinate two-jets

Two-supported leading circuits are six-cycle, theta, tight handcuff, or loose
handcuff. Their exact regular two-jet matching-support maxima are `6,5,8,6`.
Positive-singleton circuits are square-lollipop, double-edge-tail, or
endpoint-marked `P5`; their exact second-order maxima are `22,22,23`.
All are below the 24 perfect matchings of `perm_4`.

Frozen cores:

```text
two-supported:
0435988b71e2697ba07a8eed4290b4b58be3792612d2737d4126f72a914ff2a9

positive-singleton:
a17aa6de25348a88773f81a05d6d2eaa9212d1d8d213804a365b3015a1f7e99f
```

### 4.2 Zero-leading first-order envelope

For any coordinate six-frame support `A`, one regular factor motion can create
only

\[
F_1(A)=\{M:|M\cap A|\ge3\},
\qquad |F_1(A)|\le6.
\]

The corrected exhaustive scan checks 14,893 distinct supports, with 288
equality supports in two row-column orbits of size 144. A previous draft
`6+5z` inference was retracted: positive-leading components can acquire new
first-order matching coordinates through nonmatching source coefficients.

Corrected frozen core:

```text
ec39aab2c48fc038f66fcaaaee2a8bb1f2b662d640f065ed0ff4e6a3c2f1aedf
```

The extremal four-zero exact 24-cover subcase is separately closed; its frozen
core is

```text
da8f9cf8d79ef2c6ba40babdb0d632449492d3c638a207ad4007b0b14fdca125
```

### 4.3 Complete regular coordinate first-order barrier

For an unordered coordinate six-frame multiset `gamma`, let

```text
E(gamma) = all perfect matchings retaining at least three frame cells
D(gamma) = perfect matchings already contained in the frame
K(gamma) = matchings reachable at first order from the internal source kernel
S(gamma) = D(gamma) union K(gamma).
```

The exact internal-kernel criterion is: `M in K(gamma)` iff there exist a
three-edge submatching `P` of `M` contained in the frame and a frame cell `c`
with multiplicity

\[
m_c\ge2+\mathbf1_{c\in P}.
\]

Exhaustion of all

\[
\binom{21}{6}=54,264
\]

unordered six-frame multisets, with an independent source-fiber replay, proves

\[
\boxed{|E(\gamma)|+|S(\gamma)|\le6}.
\]

There are 864 equality frames: 288 with profile `(6,0,0,0)` and 576 with
profile `(4,0,2,2)`, forming four row-column orbits of sizes
`144,144,288,288`.

For `q` components whose order-zero sum vanishes, target matchings in
`union_i S_i` need at least one envelope incidence; all other target matchings
need at least two because their nonzero order-zero source monomial must cancel
in another component. Therefore

\[
\sum_i|E_i|\ge48-\sum_i|S_i|,
\]

while the local theorem gives

\[
\sum_i|E_i|\le6q-\sum_i|S_i|.
\]

Hence

\[
\boxed{q\ge8}.
\]

Thus every regular coordinate first-order degeneration with `q<=7` is
incompatible with a nonzero diagonal-torus transform of `perm_4`.

Frozen theorem core:

```text
8f0d2f3e746582c581e23f519c776733654e9f907af1b88bd29daea8a65f892b
```

This is a strict route theorem, not an unrestricted six- or seven-block zero
theorem.

## 5. Validation / CI

The new eight-term first-order packet passes all seven focused tests, including
complete 54,264-frame enumeration and an independent source-fiber replay.
Hosted run #845 reached 929 tests and failed only because the older singleton
primary CLI redundantly launched the expensive independent replay under
`python -O`; all other singleton tests passed. Commit
`21ae89f5fdd7fb4524c7aa2fde4a9ccc18eaa68e` separates the primary and
independent replays without removing either mathematical check. Run #851 is
the hosted verification of that repair.

Do not describe full hosted CI as green until run #851 completes successfully.

## 6. Exact next research task

The coordinate first-order route is closed for six and seven components. Do
not continue splitting cases by the number of zero-leading components.

The next narrow interface is a **six-component coordinate degeneration whose
order-zero and order-one sums vanish and whose first nonzero coefficient is
order two**.

Current exact diagnostic: allowing up to two factor motions and an enlarged
internal source-kernel second-order envelope over all 54,264 coordinate
multisets gives

```text
maximum |E2| + |S2_tilde| = 20
equality frames = 288
row-column equality orbits = 2
representatives = (0,0,1,2,7,11) and transpose type
```

This diagnostic is deliberately an over-envelope because it does not yet
impose componentwise/global first-order vanishing. It is not promoted to a
six-block theorem.

Next prove coefficient-level restrictions on these equality / near-equality
states, preferably through the shared order-zero quartic fibers and their
second fundamental-form terms. Support counting alone is insufficient: three
size-eight two-replacement matching supports can partition all 24 matchings.

Only if an exact second-order survivor remains should the project open a
third-order expansion.

## 7. Strict claim boundary

```text
five-block literal sum = ZERO
six-block literal sum = OPEN
seven-block literal sum = OPEN
eight-block literal sum = NONZERO
mu(6,4) = OPEN in [6,8]
coordinate regular first-order q<=7 = ZERO
coordinate regular first-order q=8 existence = OPEN
all-positive coordinate regular two-jets = CLOSED
zero-leading first-nonzero-order-two coordinate degenerations = OPEN
noncoordinate / singular / multigrade degenerations = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```

Every new mathematical result must be synchronized to GitHub and reflected in
this handoff or an immediate receipt update.
