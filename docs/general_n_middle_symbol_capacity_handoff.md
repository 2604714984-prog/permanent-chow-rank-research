# General-`n` handoff: quotient-symbol capacity and first coupling barrier

## Active context

```text
repository: 2604714984-prog/permanent-chow-rank-research
base branch: main
base head: 107912a550cc4688b160e69008e7f7bb33650447
research branch: research/general-n-middle-symbol-capacity
Draft PR: #95
```

The branch begins the post-`perm_6` general-`n` program.  It does not resume
finite `perm_6` block classification.

## 1. Middle-symbol capacity result

The repaired exact `perm_6` proof belongs to a precisely defined
single-middle-layer route.  For every even `n`, that route can certify at most

\[
\binom{n}{n/2}+2n.
\]

It matches Glynn at `n=6` and is strictly below Glynn for every even `n>=8`.

A parallel research branch already contained the same underlying capacity
observation in `docs/general_middle_image_span_feasibility.md`.  The first
commit of this branch is therefore a clean main-based theorem packet and
independent replay, not a literature- or repository-priority claim.

## 2. New exact squarefree quotient-symbol theorem

For the independent Chow term `z_1*...*z_n`, let `Sq^k(F)` be its degree-`k`
squarefree derivative space.  For every rank-`d` quotient `P:F->D`, the exact
minimum quotient-symbol rank is

\[
\boxed{
\min_{\operatorname{rank}P=d}
\operatorname{rank}\partial_{k,P}
=
\binom nk-\binom{n-d}{k}.
}
\]

A coordinate quotient attains equality.  The same coordinate quotient
simultaneously minimizes every degree.

Consequently, placing adjacent degrees in a direct sum remains exactly
additive:

\[
\min_P\operatorname{rank}
(\partial_{k,P}\oplus\partial_{k+1,P})
=
\sum_{j=k}^{k+1}
\left(
\binom nj-\binom{n-d}{j}
\right).
\]

Across all positive degrees, the exact direct-sum minimum is

\[
2^n-2^{n-d}.
\]

Therefore merely reusing the same factor quotient is not a coupled invariant.
A viable next object must quotient or measure the common second-derivative
relations between the levels.

Theorem core:

```text
de3f17005702e35de8bf1fe0b14d562f9575dcd9d052e1123abce31365d06b98
```

## 3. Current trusted numerical context

```text
ChowRank(perm_3)=4
ChowRank(perm_4)=8
ChowRank(perm_5)=16             repaired internal proof draft
ChowRank(perm_6)=32             repaired post-audit internal proof
50<=ChowRank(perm_7)<=64        current main proof draft
general exact value             OPEN
```

## 4. Validation

```text
middle-capacity primary and independent replays        PASS
middle-capacity focused tests                           6/6 PASS
squarefree-profile primary and python -O                PASS
squarefree-profile independent bit-mask replay          PASS
squarefree-profile focused tests                        6/6 PASS
frozen JSON equality and py_compile                     PASS
```

## 5. Strict boundary

```text
new general Chow-rank lower bound                       NO
single-middle constant-slope route                      CLOSED
block-diagonal adjacent shared quotient                 EXACTLY ADDITIVE
arbitrary repeated/dependent term profile               OPEN
cross-degree Koszul or mapping-cone quotient            OPEN
general Glynn optimality                                OPEN
border-rank improvement                                 NO
literature novelty                                      NOT ESTABLISHED
```

## 6. Next single task

Study the first genuine two-step relation object

\[
\operatorname{Sq}^{k+1}(F)
\longrightarrow
D\otimes\operatorname{Sq}^{k}(F)
\longrightarrow
\bigwedge^2D\otimes\operatorname{Sq}^{k-1}(F),
\]

and its permanent-relative analogue.  Determine whether the homology or
relation quotient has a joint one-term cap strictly below the additive symbol
rank, including repeated and dependent factors.

Promotion requires a written natural map, a uniform degenerate-term cap, a
sum/subquotient inequality, and a nontrivial permanent-side ratio.  No generic
solver framework or large state database is authorized.
