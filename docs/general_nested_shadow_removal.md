# Nesting zero-intersection removal inside multishadow bounds

## Status and novelty boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_ARITHMETIC_REPLAYED`,
`GENERAL_N_PROGRESS`.

The permanent-side derivative-shadow rigidity and the corresponding
zero-intersection criterion are **not new in this note**. They were already
proved as Lemmas 5.1--5.2 and Corollary 5.3 of
`docs/general_n_koszul_bounds.md`, with their asymptotics in
`docs/shadow_removal_asymptotics.md`.

The new step is to use one certified zero-intersection block *inside* the later
nonzero-intersection multishadow argument. A section-and-projection lemma lets
the old derivative capacity apply after fixing more terms. Combined with the
exact product-shadow theorem, this gives

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge43,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge78.
}
\]

The reviewed general `n=15` certificate also improves from `6,879` to `6,883`.
No exact-rank, border-rank, unrestricted `perm_6`, or literature-novelty claim
is made.

## 1. Existing zero-intersection input

Let

\[
E_k=\mathcal D_k(\operatorname{perm}_n).
\]

The existing derivative-shadow theorem says that every nonzero `g in E_k`
satisfies, for every derivative order `a`,

\[
\dim\partial^a g\ge\binom ka^2.
\tag{1.1}
\]

For one degree-`n` Chow term `T` and every `g in D_k(T)`, the corresponding
upper bound is

\[
\dim\partial^a g
\le
M_{n,k,a}
:=
\min\left\{
\binom na,
\binom n{k-a}
\right\}.
\tag{1.2}
\]

Therefore a block of `s` Chow terms is disjoint from `E_k` whenever

\[
sM_{n,k,a}<\binom ka^2
\tag{1.3}
\]

for at least one `a`.

Define the largest certified block size

\[
\boxed{
\sigma(n,k)
=
\max_{1\le a<k}
\left\lfloor
\frac{\binom ka^2-1}
{M_{n,k,a}}
\right\rfloor.
}
\tag{1.4}
\]

Then every `sigma(n,k)`-term block satisfies

\[
E_k\cap
\sum_{i=1}^{\sigma(n,k)}\mathcal D_k(T_i)=0.
\tag{1.5}
\]

## 2. The new omitted-block projection lemma

### Lemma 2.1

Let

\[
F_i\subseteq W,
\qquad
U=F_1+\cdots+F_q,
\qquad
E\subseteq W.
\]

Assume that for a label set `I subset [q]`,

\[
E\cap\sum_{i\in I}F_i=0.
\tag{2.1}
\]

Then

\[
\boxed{
\dim(E\cap U)
\le
\sum_{i\notin I}\dim F_i.
}
\tag{2.2}
\]

### Proof

Let

\[
\pi:\bigoplus_{i=1}^qF_i\longrightarrow U
\]

be summation. Choose a linear section of `pi` over `E intersect U`, and
project that section to the direct sum of the components outside `I`. If an
element maps to zero, its selected lift is supported only on `I`; its sum lies
in the intersection in (2.1), hence is zero. Since the section is injective,
the original element is zero. Thus the projection is injective and (2.2)
follows. ∎

### Corollary 2.2

For degree-`n` Chow terms and `k>=2`,

\[
\boxed{
\dim\left(
E_k\cap\sum_{i=1}^q\mathcal D_k(T_i)
\right)
\le
(q-\sigma(n,k))\binom nk.
}
\tag{2.3}
\]

The actual coupled image of `R=sum_iT_i` is only contained in the literal sum:

\[
\mathcal D_k(R)
\subseteq
\sum_i\mathcal D_k(T_i).
\tag{2.4}
\]

Equations (2.3)--(2.4) are the only way the lemma enters the coupled
multishadow proof. No equality between coupled and literal images is assumed.

## 3. Nesting inside the nonzero-intersection theorem

Choose a Koszul output degree `m` and put

\[
r=n-m,
\qquad
k=r-1.
\]

For a fixed part

\[
R=T_1+\cdots+T_q,
\]

let

\[
S=
\mathcal D_r(\operatorname{perm}_n)
\cap
\mathcal D_r(R),
\qquad b=\dim S.
\tag{3.1}
\]

Differentiation gives

\[
\partial S
\subseteq
E_k\cap\mathcal D_k(R).
\tag{3.2}
\]

By Corollary 2.2,

\[
\boxed{
\dim\partial S
\le
(q-\sigma(n,k))\binom nk.
}
\tag{3.3}
\]

Suppose an existing multishadow certificate fixed `q_0` terms and used
capacity

\[
q_0\binom nk.
\]

If the global baseline guarantees at least

\[
q=q_0+\sigma(n,k)
\]

terms, fix `q` instead. Equation (3.3) gives the **same** capacity:

\[
(q-\sigma(n,k))\binom nk
=q_0\binom nk.
\tag{3.4}
\]

Therefore the old shadow intersection cap and the residual Koszul term count
remain valid, while the fixed-term contribution increases by
`sigma(n,k)`.

This differs from the original shadow-removal theorem. The original theorem
uses a zero intersection at the complementary derivative degree and restores
the full permanent Koszul rank. Here the zero-intersection block is one degree
lower and is used only to sharpen the capacity in a genuinely nonzero
intersection problem.

## 4. Reviewed general certificates

Applying (3.4) to the frozen general multishadow certificates gives:

| `n` | shadow degree `k` | safe block | former bound | nested bound |
|---:|---:|---:|---:|---:|
| 7 | 3 | 1 | 41 | 42 |
| 8 | 3 | 1 | 76 | 77 |
| 9 | 4 | 1 | 141 | 142 |
| 10 | 4 | 1 | 267 | 268 |
| 11 | 5 | 2 | 506 | 508 |
| 12 | 5 | 2 | 968 | 970 |
| 13 | 6 | 2 | 1,853 | 1,855 |
| 14 | 6 | 2 | 3,568 | 3,570 |
| 15 | 7 | 4 | 6,879 | 6,883 |
| 16 | 7 | 3 | 13,312 | 13,315 |

At `n=15,k=7`, the best zero-intersection witness uses derivative order five,
or equivalently output degree two:

\[
4\binom{15}{2}=420
<
\binom72^2=441.
\tag{4.1}

Thus four terms can be projected away while retaining the old degree-seven
capacity.

## 5. Exact product-shadow applications

### 5.1 `perm_7`

The parent exact-shadow theorem proves

\[
F_{7,4}(238)=452,
\qquad
F_{7,4}(239)=456.
\tag{5.1}

Take fourteen fixed terms. Since `sigma(7,3)=1`, equation (3.3) gives

\[
\dim\partial S
\le(14-1)\binom73=455.
\]

Hence `b<=238`. The residual still requires 29 terms, and

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)
\ge14+29=43.
}
\tag{5.2}

### 5.2 `perm_8`

Similarly,

\[
F_{8,4}(560)=784,
\qquad
F_{8,4}(561)=793.
\tag{5.3}

Take fifteen fixed terms and use `sigma(8,3)=1`:

\[
\dim\partial S
\le(15-1)\binom83=784.
\]

Thus `b<=560`. The residual still requires 63 terms, proving

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)
\ge15+63=78.
}
\tag{5.4}

## 6. Asymptotic size and limitation

The existing shadow-removal asymptotic theorem already proves, for the central
sequence,

\[
\sigma(n,k)
=
\Theta\left(
\frac{((1+\sqrt2)/2)^n}{\sqrt n}
\right)
\tag{6.1}
\]

along an explicit derivative-order choice. The nested theorem transfers that
entire zero-intersection block into any compatible nonzero-intersection
certificate whose fixed-term budget stays below the global baseline.

This is an exponential additive saving, but its base is about `1.2071`, far
below the leading central-binomial scale and Glynn's upper-bound scale. It does
not solve the general conjecture.

## 7. Strongest objection and next target

The pure derivative-shadow rigidity was already known in the repository. The
only new mathematical content here is the omitted-block projection and its
integration with the nonzero-intersection machinery. That distinction must be
preserved in any paper or status ledger.

The next target is the **near-zero intersection regime**: classify or bound

\[
E_k\cap\sum_{i=1}^{\sigma(n,k)+t}\mathcal D_k(T_i)
\]

for small positive `t`. A result growing sublinearly in `t` would improve the
capacity by more than the current all-or-nothing omitted block. No new state or
solver architecture is justified before such a theorem is stated.

## 8. Reproduction

Run

```bash
python scripts/general_nested_shadow_removal.py \
  --json /tmp/general_nested_shadow_removal.json
python -m unittest tests.test_general_nested_shadow_removal -v
```

Expected marker:

```text
GENERAL_NESTED_SHADOW_REMOVAL_AUDIT_PASS
```
