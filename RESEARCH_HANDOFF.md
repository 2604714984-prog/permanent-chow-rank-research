# Research handoff

Canonical handoff for the active post-`perm_6` general-`n` stack.

Last updated: **2026-08-23**

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

## 1. Single-middle route ceiling

For even `n`, a proof using one symmetric middle catalecticant, symmetric
image-span, one factor-span filtration, and a constant-slope half-defect symbol
has capacity

\[
B_{\rm mid}(n)=\binom n{n/2}+2n.
\]

Thus `n=6` saturates the route at 32, while every even `n>=8` lies strictly
below `2^(n-1)`.

```text
core: 29310e7c02e0ec22a4622acc57fccb5cc5582f23f1c15c950fbf3b28dfcd2aaf
```

## 2. Raw quotient symbols and independent-term Koszul homology

For the independent Chow term and rank-`d` quotient,

\[
\min\operatorname{rank}\partial_{k,P}
=\binom nk-\binom{n-d}{k}.
\]

Direct sums across degrees remain exactly additive. The first genuine two-step
Koszul quotient has

\[
\max\dim H^1_{n,k}(P)=d\binom{n-d}{k-1}.
\]

```text
raw-symbol core: de3f17005702e35de8bf1fe0b14d562f9575dcd9d052e1123abce31365d06b98
Koszul core:     7beab85037ef5c9f0e4b6efc22a19d98ee9fc7b88bc3b7eac9e1f0288c4dbf8c
```

## 3. Raw-homology failure and full-quotient identity

The one-relation term

\[
x_1\cdots x_{n-1}(x_1+\cdots+x_{n-1})
\]

has raw full-quotient `H1=C(n,2)`, exceeding the independent cap `n-1`.
Therefore raw first Koszul homology is not uniformly capped over arbitrary
Chow terms.

For every concise form,

\[
H^1_{\rm full}\otimes\det(L^*)
\simeq\operatorname{Tor}_{1,3}(A_f,k)^*,
\]

so raw full-quotient homology is exactly dual to the minimal cubic apolar
generator space.

## 4. New corrected partial-quotient theorem

For a concise form with apolar ideal `I`, a quotient dual subspace `W subset V`
gives

\[
H_1(W;A)_3\simeq\frac{I_3\cap W S_2}{W I_2}.
\]

The natural map to full cubic generators has kernel

\[
\boxed{
K_W(I)=\frac{V I_2\cap W S_2}{W I_2}
\simeq\operatorname{Tor}_1^S(S/(I_2),S/(W))_3.
}
\]

Thus the cubic-generator-corrected remainder is exactly quadratic base-change
torsion.

If `I_2` is simultaneously diagonalizable, with actual factor-span dimension
`r`, quadratic dimension `q`, and quotient rank `d`, then

\[
\boxed{
\dim K_W(I)\le(r-d)\min(q,d)\le d(r-d).
}
\]

The independent squarefree term attains `d(r-d)`, so this scale is sharp.

Every one-relation normal form

\[
x_1\cdots x_r(x_1+\cdots+x_s)
\]

has simultaneously diagonalizable `I_2`, with

\[
\dim I_2=r-s+\mathbf1_{s=2},
\]

and satisfies the bound for every quotient rank.

```text
theorem id: G-PARTIAL-QUOTIENT-KOSZUL-TORSION-v1
core: f8c9b5ff8a9f09c9dd31dd9c4d123ce68aa6a0ea49e593ecc97da548dbd82bd2
```

## 5. Validation boundary

```text
primary fixed-point scan through r=8                   PASS
all one-relation supports and quotient ranks to r=12  PASS
independent ordered-monomial replay                    PASS
frozen JSON equality                                   PASS
focused tests                                           6/6 PASS
python -O / py_compile / no-bare-assert                PASS
```

Hosted Actions must complete on the current head before the branch is called
green.

## 6. Strict claim boundary

```text
new unrestricted general-n Chow-rank lower bound       NO
single-middle route                                     CLOSED
raw adjacent shared quotient                            EXACTLY ADDITIVE
raw first Koszul H1, independent term                   EXACT
raw first Koszul H1, arbitrary Chow term                NOT UNIFORMLY CAPPED
corrected partial H1                                    QUADRATIC BASE-CHANGE TORSION
simultaneously diagonalizable quadratic spaces          CAPPED
complete one-relation Chow family                       PASS
arbitrary multi-relation Chow term                      OPEN
sum/subquotient inequality                              OPEN
general ChowRank(perm_n)=2^(n-1)                        OPEN
border-rank improvement                                 NO
literature novelty                                      NOT ESTABLISHED
```

## 7. Exact next task

Do not compute the permanent-side module yet. Determine whether every product
of linear forms has a simultaneously diagonalizable quadratic apolar space,
or prove directly that

\[
\dim K_W(I)\le d(r-d)
\]

for arbitrary Chow terms. One exact counterexample rejects the candidate. A
positive theorem authorizes the first permanent-side computation and the still
missing sum/subquotient inequality.
