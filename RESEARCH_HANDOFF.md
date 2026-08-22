# Research handoff

Canonical handoff for the active post-`perm_6` general-`n` stack.

Last updated: **2026-08-22**

## GitHub context

```text
repository: 2604714984-prog/permanent-chow-rank-research
active branch: research/general-n-middle-symbol-capacity
active Draft PR: #95
base branch: main
base exact head: 107912a550cc4688b160e69008e7f7bb33650447
```

Keep the stack narrow. Do not add a manager, registry, database, broad solver
framework, or second control plane.

## 1. Mainline route ceiling

The even middle-symbol capacity packet places an existing parallel-branch
feasibility result on current `main` with an independent replay. For even `n`,
a proof using one symmetric middle catalecticant, symmetric image-span, one
factor-span filtration, and one constant-slope half-defect symbol has capacity

\[
B_{\rm mid}(n)=\binom n{n/2}+2n.
\]

Thus `n=6` saturates the route at 32, while every even `n>=8` lies strictly
below `2^(n-1)`. This is a route ceiling, not a Chow-rank upper bound.

```text
core: 29310e7c02e0ec22a4622acc57fccb5cc5582f23f1c15c950fbf3b28dfcd2aaf
```

## 2. Exact independent-term quotient-symbol profile

For the independent Chow term `z_1*...*z_n` and every rank-`d` quotient
`P:F->D`,

\[
\min\operatorname{rank}\partial_{k,P}
=
\binom nk-\binom{n-d}{k}.
\]

Using one quotient on adjacent or all degrees but retaining a direct-sum target
is exactly additive. Merely sharing a quotient is not a coupled invariant.

```text
core: de3f17005702e35de8bf1fe0b14d562f9575dcd9d052e1123abce31365d06b98
```

## 3. Exact independent-term first Koszul homology

For

\[
\operatorname{Sq}^{k+1}(F)
\longrightarrow
D\otimes\operatorname{Sq}^{k}(F)
\longrightarrow
\bigwedge^2D\otimes\operatorname{Sq}^{k-1}(F),
\]

the maximum middle homology over rank-`d` quotients is

\[
\max\dim H^1_{n,k}(P)
=d\binom{n-d}{k-1}.
\]

Coordinate quotients attain equality. Across all positive degrees the maximum
one-term value is `d*2^(n-d)`, reaching `2^(n-1)` at `d=1,2`.

```text
core: 7beab85037ef5c9f0e4b6efc22a19d98ee9fc7b88bc3b7eac9e1f0288c4dbf8c
```

## 4. New route counterexample: one full-support relation

For every `n>=5`, the actual degree-`n` Chow term

\[
T_n=x_1\cdots x_{n-1}(x_1+\cdots+x_{n-1})
\]

has factor-span dimension `n-1`. At the identity quotient and output degree
`k=2`, its actual derivative-space complex

\[
\mathcal D_3(T_n)
\longrightarrow
L\otimes\mathcal D_2(T_n)
\longrightarrow
\bigwedge^2L\otimes\mathcal D_1(T_n)
\]

has

\[
\boxed{\dim H^1=\binom n2.}
\]

The independent-term cap at the same `(n,d,k)` is only `n-1`; the gap is

\[
\binom{n-1}{2}.
\]

The proof uses the actual apolar Hilbert function, absence of quadratic apolar
relations, `binom(n,2)` minimal cubic generators, and Gorenstein resolution
duality. An independent sparse replay constructs both differentials directly
for `5<=n<=9`.

Consequences:

```text
independent-term homology theorem                    RETAINED
uniform extension to dependent/repeated terms        FALSE
raw H1 as a uniform one-term Chow invariant          REJECTED
factor-rank-deficit-only repair                      INSUFFICIENT
```

## 5. Validation

```text
middle-capacity focused tests                         6/6 PASS
raw quotient-symbol focused tests                     6/6 PASS
independent-term Koszul focused tests                 6/6 PASS
one-relation counterexample focused tests             6/6 PASS
one-relation primary and python -O                     PASS
one-relation independent sparse matrices, n=5..9      PASS
frozen JSON comparisons                               PASS
py_compile                                             PASS
```

Hosted Actions must complete on the current head before the branch is called
green.

## 6. Strict claim boundary

```text
new unrestricted general-n Chow-rank lower bound      NO
single-middle route                                   CLOSED
raw adjacent shared quotient                          EXACTLY ADDITIVE
raw first Koszul H1, independent term                 EXACT
raw first Koszul H1, arbitrary Chow term              NOT UNIFORMLY CAPPED
permanent-side corrected relation module              OPEN
sum/subquotient inequality                            OPEN
general ChowRank(perm_n)=2^(n-1)                      OPEN
border-rank improvement                               NO
literature novelty                                    NOT ESTABLISHED
```

## 7. Exact next task

Do not compute the permanent-side module yet. First test the smallest repair on
the complete one-relation family

```text
x_1*...*x_(n-1)*(x_1+...+x_s),  1<=s<=n-1.
```

The selected candidate is the cubic-generator-corrected degree-two homology:
separate the high Koszul class forced by minimal cubic apolar generators from
the quotient-dependent remainder. Determine whether the remainder satisfies a
uniform independent-scale cap for every quotient rank. A failure rejects this
repair; a theorem authorizes the first permanent-side and sum/subquotient test.

A synchronized result must include proof or counterexample, primary and
independent replay, frozen data, tests, exact claim boundary, and the next
single mathematical interface.
