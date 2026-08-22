# General-`n` handoff: quotient-symbol capacity and Koszul relation profile

## Active context

```text
repository: 2604714984-prog/permanent-chow-rank-research
base branch: main
base head: 107912a550cc4688b160e69008e7f7bb33650447
research branch: research/general-n-middle-symbol-capacity
Draft PR: #95
```

The branch begins the post-`perm_6` general-`n` program. It does not resume
finite `perm_6` block classification.

## 1. Middle-symbol capacity result

The repaired exact `perm_6` proof belongs to a precisely defined
single-middle-layer route. For every even `n`, that route can certify at most

\[
\binom{n}{n/2}+2n.
\]

It matches Glynn at `n=6` and is strictly below Glynn for every even `n>=8`.
A parallel branch already contained the same underlying feasibility
observation; this branch supplies a clean main-based packet and independent
replay rather than a priority claim.

## 2. Exact raw quotient-symbol profile

For the independent term `z_1*...*z_n`, every rank-`d` factor quotient obeys

\[
\min\operatorname{rank}\partial_{k,P}
=
\binom nk-\binom{n-d}{k}.
\]

Direct sums over adjacent or all degrees remain exactly additive. Merely
reusing the same quotient is not a coupled invariant.

```text
theorem core:
de3f17005702e35de8bf1fe0b14d562f9575dcd9d052e1123abce31365d06b98
```

## 3. Exact first Koszul relation-homology cap

For the genuine two-step complex

\[
\operatorname{Sq}^{k+1}(F)
\longrightarrow
D\otimes\operatorname{Sq}^{k}(F)
\longrightarrow
\bigwedge^2D\otimes\operatorname{Sq}^{k-1}(F),
\]

let `H^1_(n,k)(P)` be its middle homology. Then

\[
\boxed{
\max_{\operatorname{rank}P=d}
\dim H^1_{n,k}(P)
=
d\binom{n-d}{k-1}.
}
\]

The maximum is attained by coordinate quotients. The proof uses upper
semicontinuity on `Gr(n-d,F)`, a torus-fixed maximum, and an exact support
splitting of the coordinate complex.

Consequently,

\[
\max_P
\left(
\dim H^1_{n,k}(P)+\dim H^1_{n,k+1}(P)
\right)
=
d\binom{n-d+1}{k},
\]

and

\[
\max_P\sum_{k=1}^n\dim H^1_{n,k}(P)
=
d2^{n-d}.
\]

The all-degree cap is largest at `d=1` or `d=2`, where it equals `2^(n-1)`.
This is an independent-term local capacity, not a permanent lower bound.

```text
theorem core:
7beab85037ef5c9f0e4b6efc22a19d98ee9fc7b88bc3b7eac9e1f0288c4dbf8c
```

## 4. Current trusted numerical context

```text
ChowRank(perm_3)=4
ChowRank(perm_4)=8
ChowRank(perm_5)=16             repaired internal proof draft
ChowRank(perm_6)=32             repaired post-audit internal proof
50<=ChowRank(perm_7)<=64        current main proof draft
general exact value             OPEN
```

## 5. Validation

```text
middle-capacity focused tests                           6/6 PASS
raw symbol-profile focused tests                        6/6 PASS
Koszul-homology focused tests                           6/6 PASS
Koszul independent sparse checks                         270
coordinate equality checks                                90
noncoordinate upper-bound checks                         180
normal Python, python -O, frozen JSON, py_compile       PASS
```

## 6. Strict boundary

```text
new general Chow-rank lower bound                       NO
single-middle constant-slope route                      CLOSED
block-diagonal adjacent shared quotient                 EXACTLY ADDITIVE
first Koszul relation homology, independent term        EXACT
arbitrary repeated/dependent term profile               OPEN
permanent-side relation homology                        OPEN
sum/subquotient inequality                              OPEN
general Glynn optimality                                OPEN
border-rank improvement                                 NO
literature novelty                                      NOT ESTABLISHED
```

## 7. Next single task

Stress-test the homology cap on the complete one-relation Chow normal forms

\[
x_1\cdots x_{n-1}(x_1+\cdots+x_s),
\qquad1\le s\le n-1.
\]

First determine whether dependent factors can exceed the independent-term cap
`d*2^(n-d)`. A counterexample rejects this invariant before any permanent-side
calculation; a uniform bound authorizes the permanent-side and subquotient
work. No generic solver or full parameter sweep is authorized.
