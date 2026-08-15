# Hereditary derivative profiles inside permanent derivative spaces

## Status and scope

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_ARITHMETIC_REPLAYED`,
`GENERAL_N_PROGRESS`.

This note strengthens factor-span transversality. Every nonzero polynomial in
a degree-`d` permanent derivative space inherits, at every lower degree, at
least the derivative dimensions of `perm_d` itself. This produces a stronger
multi-term omission theorem and the reviewed ordinary lower bounds

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge43,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge78.
}
\]

It also raises the reviewed general `n=15` multishadow bound from `6,879` to
`6,883`; the factor-span theorem alone gave `6,882`.

The result does not determine `perm_7`, `perm_8`, or general `perm_n`
exactly, improve border Chow rank, or settle unrestricted `perm_6`.
Literature novelty has not been established.

## 1. A hereditary permanent profile

For a degree-`d` form `f`, write

\[
\mathcal D_j(f)
=
\operatorname{im}C_{d-j,j}(f),
\qquad 0\le j\le d.
\]

Let

\[
E_d=\mathcal D_d(\operatorname{perm}_n)
\]

be the degree-`d` permanent derivative space. It has the multiplicity-free
row-column torus basis

\[
\{p_{R,C}:R,C\in\tbinom{[n]}d\},
\tag{1.1}
\]

where `p_(R,C)` is a `d x d` subpermanent.

### Theorem 1.1 -- hereditary derivative profile

For every nonzero

\[
0\ne f\in E_d
\]

and every `0<=j<=d`,

\[
\boxed{
\dim\mathcal D_j(f)
\ge
\binom dj^2.
}
\tag{1.2}
\]

### Proof

Extend the base field to an algebraic closure. Choose a generic one-parameter
subgroup of the row-column diagonal torus that assigns distinct values to all
weights occurring in `f`. After rescaling by its smallest power of the
parameter, the limit of `f` is a nonzero scalar multiple of one basis vector

\[
p_{R,C}.
\tag{1.3}
\]

For a nonzero parameter, the torus acts invertibly on variables and on
differential operators, so

\[
\dim\mathcal D_j(t\cdot f)
=
\dim\mathcal D_j(f).
\]

Catalectic rank cannot increase under specialization. Hence

\[
\dim\mathcal D_j(f)
\ge
\dim\mathcal D_j(p_{R,C}).
\tag{1.4}
\]

The output degree-`j` derivatives of a `d x d` permanent are precisely its
`j x j` subpermanents. Their row and column supports are distinct, so they are
linearly independent and number

\[
\binom dj^2.
\]

Substituting this in (1.4) proves (1.2). Scalar extension does not change any
rank, so the theorem holds over every characteristic-zero field. ∎

At `j=1`, Theorem 1.1 says that every nonzero element of `E_d` has at least
`d^2` essential variables. Thus the sub-square factor-span theorem is the
first layer of the hereditary profile.

## 2. Multi-term profile transversality

Let

\[
T_i=\ell_{i1}\cdots\ell_{in}
\]

be degree-`n` Chow terms and put

\[
F_i=\mathcal D_d(T_i).
\]

### Theorem 2.1 -- derivative-profile block exclusion

If, for some `j` with `1<=j<d`,

\[
s\binom nj<\binom dj^2,
\tag{2.1}
\]

then every block of `s` Chow terms satisfies

\[
\boxed{
E_d\cap(F_1+\cdots+F_s)=0.
}
\tag{2.2}
\]

### Proof

Suppose `0!=f` lies in the intersection. Choose

\[
f=f_1+\cdots+f_s,
\qquad f_i\in F_i.
\]

Further differentiation gives

\[
\mathcal D_j(f_i)
\subseteq
\mathcal D_j(T_i).
\]

Therefore

\[
\mathcal D_j(f)
\subseteq
\sum_{i=1}^s\mathcal D_j(T_i),
\]

and a degree-`n` Chow term has

\[
\dim\mathcal D_j(T_i)\le\binom nj.
\]

Consequently

\[
\dim\mathcal D_j(f)
\le s\binom nj.
\tag{2.3}
\]

The hereditary profile theorem gives the contradictory lower bound

\[
\dim\mathcal D_j(f)
\ge\binom dj^2.
\]

Thus (2.2) holds. The argument includes repeated and dependent factors. ∎

Define the profile-safe omission count

\[
\boxed{
\sigma(n,d)
=
\max_{1\le j<d}
\left\lfloor
\frac{\binom dj^2-1}{\binom nj}
\right\rfloor.
}
\tag{2.4}
\]

The `j=1` term is exactly the factor-span count

\[
\left\lfloor\frac{d^2-1}{n}\right\rfloor,
\]

but higher derivative degrees can be stronger.

### Corollary 2.2 -- omitted profile block

For `q` fixed Chow terms, let

\[
U=\sum_{i=1}^q\mathcal D_d(T_i).
\]

Then

\[
\boxed{
\dim(E_d\cap U)
\le
(q-\sigma(n,d))\binom nd,
}
\tag{2.5}
\]

provided `q>=sigma(n,d)`.

### Proof

Choose any block of `sigma(n,d)` labels. Theorem 2.1 makes its literal
derivative-space sum disjoint from `E_d`. Choose a linear section of the
summation map

\[
\bigoplus_i\mathcal D_d(T_i)\longrightarrow U
\]

over `E_d intersect U`, and project away from the chosen block. The kernel
would sum to an element of the forbidden intersection, so the projection is
injective. The remaining `q-sigma(n,d)` components have dimension at most
`binom(n,d)` each. ∎

This proof uses the literal sum only as an ambient space. For the coupled sum
`R=sum_i T_i`, one uses the valid inclusion

\[
\mathcal D_d(R)\subseteq U,
\]

not an equality.

## 3. Multishadow consequence

Choose output degree `m`, put

\[
r=n-m,
\qquad d=r-1,
\]

and fix `q` terms with sum `R`. For

\[
S=
\mathcal D_r(\operatorname{perm}_n)
\cap
\mathcal D_r(R),
\]

differentiation and Corollary 2.2 give

\[
\dim\partial S
\le
(q-\sigma(n,d))\binom nd.
\tag{3.1}
\]

Combining (3.1) with either the existing Bukh multishadow certificate or the
exact product-shadow function leaves the same intersection cap available to
more fixed terms.

If a previous certificate fixed `q_0` terms, and the global baseline already
guarantees at least

\[
q_0+\sigma(n,d)
\]

terms, fix that many instead. Equation (3.1) has the unchanged right-hand
side

\[
(q_0+\sigma-\sigma)\binom nd
=q_0\binom nd.
\]

Thus the old intersection cap and residual term count remain valid while the
total lower bound rises by `sigma(n,d)`.

## 4. Reviewed general certificate table

| `n` | intersection degree `d` | best witness `j` | safe block | former bound | refined bound |
|---:|---:|---:|---:|---:|---:|
| 7 | 3 | 1 | 1 | 41 | 42 |
| 8 | 3 | 1 | 1 | 76 | 77 |
| 9 | 4 | 1 | 1 | 141 | 142 |
| 10 | 4 | 1 | 1 | 267 | 268 |
| 11 | 5 | 1 | 2 | 506 | 508 |
| 12 | 5 | 1 | 2 | 968 | 970 |
| 13 | 6 | 1 or 2 | 2 | 1,853 | 1,855 |
| 14 | 6 | 1 or 2 | 2 | 3,568 | 3,570 |
| 15 | 7 | 2 | 4 | 6,879 | 6,883 |
| 16 | 7 | 1 or 2 | 3 | 13,312 | 13,315 |

The `n=15` row is the first reviewed instance where a higher derivative layer
strictly improves the factor-span count.

## 5. Exact product-shadow bounds for `n=7,8`

For `n=7`, the exact product-shadow certificate has

\[
F_{7,4}(238)=452,
\qquad
F_{7,4}(239)=456.
\]

Here `sigma(7,3)=1`. Fix fourteen terms and omit one profile-safe term. The
capacity is still

\[
13\binom73=455,
\]

so the intersection cap remains 238. The residual requires 29 terms, proving

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge43.
}
\tag{5.1}
\]

For `n=8`,

\[
F_{8,4}(560)=784,
\qquad
F_{8,4}(561)=793,
\]

and `sigma(8,3)=1`. Fifteen fixed terms, one omitted term and the unchanged
capacity

\[
14\binom83=784
\]

retain cap 560. The residual requires 63 terms, proving

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)\ge78.
}
\tag{5.2}
\]

## 6. Asymptotic size of the safe block

In the central range, `d=n/2+O(1)`. Set

\[
j=\alpha n+O(1).
\]

Stirling's formula gives

\[
\frac{\binom dj^2}{\binom nj}
=
\exp\left(
 n\bigl(H(2\alpha)-H(\alpha)\bigr)+O(\log n)
\right),
\tag{6.1}
\]

where `H` is binary entropy with natural logarithms. The exponent is maximized
when

\[
2H'(2\alpha)-H'(\alpha)=0,
\]

or equivalently

\[
(1-2\alpha)^2=4\alpha(1-\alpha).
\]

The relevant solution is

\[
\alpha_*
=
\frac{1-1/\sqrt2}{2}.
\tag{6.2}
\]

At this point

\[
\exp(H(2\alpha_*)-H(\alpha_*))
=
\frac{1+\sqrt2}{2}.
\tag{6.3}
\]

Keeping the square-root factor in Stirling's formula gives

\[
\boxed{
\sigma(n,d)
=\Omega\left(
\frac{((1+\sqrt2)/2)^n}{\sqrt n}
\right)
}
\tag{6.4}
\]

along the central derivative degrees.

This is exponentially larger than the `j=1` factor-span saving, but still far
smaller than Glynn's `2^(n-1)` upper bound and smaller than the dominant
central-binomial-scale part of the current lower bounds.

## 7. Strongest objection and next target

The theorem is a true Chow-realizability correction, but it uses only scalar
derivative dimensions of a single polynomial in the intersection. It does
not constrain the geometry once every lower derivative capacity meets the
hereditary permanent profile.

The next target is therefore the equality case:

\[
\dim\mathcal D_j(f)=\binom dj^2
\]

for one or more degrees `j`. A useful classification would identify the
minimal-profile locus inside `E_d` and control how many such lines can arise
from one coupled block of Chow terms. Without such an equality theorem, adding
more profile degrees only refines the safe omitted block and does not approach
exact Glynn optimality.

## 8. Reproduction

Run

```bash
python scripts/general_hereditary_profile_transversality.py \
  --json /tmp/general_hereditary_profile_transversality.json
python -m unittest tests.test_general_hereditary_profile_transversality -v
```

Expected marker:

```text
GENERAL_HEREDITARY_PROFILE_TRANSVERSALITY_AUDIT_PASS
```
