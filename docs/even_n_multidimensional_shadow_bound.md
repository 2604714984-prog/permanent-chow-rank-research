# Even-degree multidimensional-shadow lower bounds

## Status

`PROOF_DRAFT_COMPLETE` — every algebraic implication below has been checked, and the displayed finite examples have exact-rational certificates in `src/permanent_chow_rank/even_multishadow.py`. External peer review and a complete literature novelty review have not been performed.

## 1. Statement and scope

Let

\[
P_n=\operatorname{perm}_n,
\qquad
V=\operatorname{span}\{x_{ij}:1\le i,j\le n\},
\qquad
N=\dim V=n^2.
\]

This note treats the even case

\[
n=2k\ge4.
\]

Write

\[
E=\mathcal D_k(P_n)
=\operatorname{im}C_{k,k}(P_n).
\]

The middle catalecticant is self-transpose. Its image has dimension

\[
e:=\dim E=\binom nk^2,
\]

and its first prolongation is

\[
E^{(1)}=\mathcal D_{k+1}(P_n),
\qquad
\dim E^{(1)}=\binom n{k+1}^2.
\]

Consequently the central first-Koszul rank is

\[
A_n
:=
\operatorname{rank}K_k(P_n)
=
N\binom nk^2-inom n{k+1}^2.
\tag{1.1}
\]

For one degree-`n` Chow term, the same flattening has rank at most

\[
B_n
:=
N\binom nk-inom n{k+1}.
\tag{1.2}
\]

The result proved below combines the self-transpose middle catalecticant with a two-dimensional shadow inequality.

### Theorem 1.1

Let `x` be a real number with `k<=x<=2k`, and define

\[
q_x
=
\left\lfloor
\frac{\binom{x}{k-1}^2}{\binom{2k}{k-1}}
\right\rfloor,
\qquad
s_x
=
\left\lfloor\binom{x}{k}^2\right\rfloor.
\tag{1.3}
\]

If `q_x>=1`, then

\[
\boxed{
\operatorname{ChowRank}(P_{2k})
\ge
q_x+
\left\lceil
\frac{A_{2k}-(2k)^2s_x}{B_{2k}}
\right\rceil
}
\tag{1.4}
\]

whenever the numerator in the last fraction is positive. The maximum of the right-hand side and the ordinary central first-Koszul bound is always valid.

This is an ordinary Chow-rank statement. No border-rank promotion is claimed, because the proof selects actual terms from an actual decomposition.

## 2. A central residual-rank inequality

Suppose a form `R` is fixed, and set

\[
H=\mathcal D_k(R),
\qquad
h=\dim H,
\qquad
S=E\cap H,
\qquad
s=\dim S.
\]

Let

\[
G=\mathcal D_k(P_n-R)
=\operatorname{im}\bigl(C_{k,k}(P_n)-C_{k,k}(R)\bigr).
\]

### Lemma 2.1 — middle-catalectic residual dimension

\[
\dim G\ge e+h-2s.
\tag{2.1}
\]

#### Proof

Both middle catalectic matrices are symmetric. Their horizontal and vertical concatenations therefore have the same rank

\[
\dim(E+H)=e+h-s.
\]

Applying the double-quotient rank inequality to the two catalectic matrices gives

\[
\begin{aligned}
\dim G
&\ge
2(e+h-s)-e-h\\
&=e+h-2s.
\end{aligned}
\]

This is the point at which even degree removes the row-image/column-image asymmetry that occurs for an odd middle split. ∎

### Lemma 2.2 — quotient prolongation bound

\[
\dim(E+H)^{(1)}
\le
\dim E^{(1)}+N(h-s).
\tag{2.2}
\]

#### Proof

For `g in (E+H)^(1)`, take all first derivatives and reduce them modulo `E`. This defines a linear map

\[
(E+H)^{(1)}
\longrightarrow
\operatorname{Hom}\bigl(V^*,(E+H)/E\bigr).
\]

Its kernel is exactly `E^(1)`. Hence it induces an injection

\[
(E+H)^{(1)}/E^{(1)}
\hookrightarrow
(E+H)/E\otimes V^*.
\]

The quotient `(E+H)/E` has dimension `h-s`, so the target has dimension `N(h-s)`. ∎

### Proposition 2.3 — only the intersection costs rank

\[
\boxed{
\operatorname{rank}K_k(P_n-R)
\ge
A_n-Ns.
}
\tag{2.3}
\]

#### Proof

Because `G subset E+H`, one has

\[
G^{(1)}\subseteq(E+H)^{(1)}.
\]

The Koszul kernel-prolongation identity, Lemma 2.1, and Lemma 2.2 give

\[
\begin{aligned}
\operatorname{rank}K_k(P_n-R)
&=N\dim G-\dim G^{(1)}\\
&\ge
N(e+h-2s)
-\bigl(\dim E^{(1)}+N(h-s)\bigr)\\
&=Ne-\dim E^{(1)}-Ns\\
&=A_n-Ns.
\end{aligned}
\]

Thus the dimensions of `H` and its quotient cancel. The entire loss is controlled by the central derivative-space intersection `S`. ∎

## 3. Multidimensional shadows bound the intersection

The row-column torus acts diagonally on the permanent derivative basis

\[
\{P_{I,J}:I,J\in\tbinom{[n]}k\}.
\]

Every basis vector has a distinct torus character.

For a family

\[
\mathcal F\subseteq
\binom{[n]}k\times\binom{[n]}k,
\]

write `partial F` for the family of pairs of `(k-1)`-subsets obtained by deleting one element in each coordinate.

### Lemma 3.1 — subspace shadow inequality

Let `0!=S subset E` have dimension `s`, and let `y>=k` be the unique real number satisfying

\[
s=\binom yk^2.
\]

Then

\[
\boxed{
\dim\partial S
\ge
\binom y{k-1}^2.
}
\tag{3.1}
\]

Here `partial S` is the span of all first derivatives of elements of `S`.

#### Proof

Choose a generic one-parameter subgroup of the row-column torus. Since the permanent derivative basis is multiplicity-free, the Grassmann limit of `S` is a coordinate subspace

\[
S_0=\operatorname{span}\{P_{I,J}:(I,J)\in\mathcal F\}
\]

with `|F|=s`.

The derivative matrix specializes along the degeneration, so its rank cannot increase at the special fiber. Therefore

\[
\dim\partial S
\ge
\dim\partial S_0
=|\partial\mathcal F|.
\]

Bukh's multidimensional Kruskal--Katona theorem, with dimension parameter `d=2`, gives

\[
|\partial\mathcal F|
\ge
\binom y{k-1}^2.
\]

Combining the two inequalities proves the lemma. ∎

Reference: Boris Bukh, *Multidimensional Kruskal--Katona theorem*, arXiv:1009.2375.

### Proposition 3.2 — intersection cap after fixing `q` Chow terms

Let

\[
R=T_1+\cdots+T_q
\]

be a sum of `q` degree-`n` Chow terms, and let

\[
S=E\cap\mathcal D_k(R).
\]

If `x>=k` satisfies

\[
q\binom n{k-1}
\le
\binom x{k-1}^2,
\tag{3.2}
\]

then

\[
\boxed{
\dim S\le\binom xk^2.
}
\tag{3.3}
\]

#### Proof

The claim is trivial when `S=0`. Otherwise write

\[
\dim S=\binom yk^2
\]

with `y>=k`. Lemma 3.1 gives

\[
\binom y{k-1}^2
\le
\dim\partial S.
\]

Since `S subset D_k(R)`, every first derivative of `S` lies in `D_{k-1}(R)`. A single Chow term has degree-`(k-1)` derivative-space dimension at most `binom(n,k-1)`, so

\[
\dim\partial S
\le
\dim\mathcal D_{k-1}(R)
\le
q\binom n{k-1}.
\]

By (3.2),

\[
\binom y{k-1}^2
\le
\binom x{k-1}^2.
\]

The generalized binomial coefficient is strictly increasing on `[k-1,infinity)`, hence `y<=x`, which gives (3.3). ∎

## 4. Proof of the main theorem

Take `q=q_x` from (1.3). Then

\[
q\binom{2k}{k-1}
\le
\binom{x}{k-1}^2.
\]

Moreover, because `x<=2k`,

\[
q
\le
\binom{2k}{k-1}
<
\binom{2k}{k}.
\]

The ordinary central Koszul bound is at least `binom(2k,k)`, so every hypothetical decomposition contains at least `q` terms. Select any `q` of them and call their sum `R`.

Proposition 3.2 gives

\[
s=\dim\bigl(E\cap\mathcal D_k(R)\bigr)
\le s_x.
\]

Proposition 2.3 then yields

\[
\operatorname{rank}K_k(P_{2k}-R)
\ge
A_{2k}-(2k)^2s_x.
\]

The residual is a sum of the remaining Chow terms, and each contributes rank at most `B_{2k}`. Therefore

\[
r-q
\ge
\left\lceil
\frac{A_{2k}-(2k)^2s_x}{B_{2k}}
\right\rceil,
\]

which is exactly (1.4). ∎

## 5. Exact small-even-degree certificates

The rational witnesses below are checked with `fractions.Fraction`; no floating-point comparison enters the certificate.

| `n` | central Koszul bound | fixed `q` | intersection cap `s_x` | residual rank floor | residual terms | resulting lower bound |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 7 | 2 | 6 | 464 | 6 | **8** |
| 6 | 21 | 4 | 40 | 12,735 | 19 | **23** |
| 8 | 71 | 12 | 496 | 278,720 | 64 | **76** |
| 10 | 253 | 42 | 7,084 | 5,597,900 | 225 | **267** |
| 12 | 925 | 179 | 125,640 | 104,224,320 | 789 | **968** |
| 14 | 3,434 | 623 | 1,673,882 | 1,971,511,423 | 2,945 | **3,568** |
| 16 | 12,875 | 2,422 | 25,470,785 | 35,751,651,840 | 10,890 | **13,312** |

The exact witness fractions are recorded in `REVIEWED_WITNESSES` and in `data/even_multishadow_bounds.json`.

### Corollary 5.1

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_6)\ge23.
}
\]

For the frozen witness,

\[
q=4,
\qquad
s\le40,
\]

so

\[
\operatorname{rank}K_{6,3}(P_6-R)
\ge
14175-36\cdot40
=12735.
\]

The remaining terms have capacity 705 each, and

\[
\left\lceil\frac{12735}{705}\right\rceil=19.
\]

Thus every decomposition contains at least `4+19=23` terms.

### Corollary 5.2 — a shorter alternative lower proof for `n=4`

The same theorem gives `q=2`, `s<=6`, and

\[
560-16\cdot6=464>5\cdot92=460.
\]

Hence a seven-term decomposition is impossible. This supplies an alternative to the stronger low-rank-classification and 659-by-659 chart argument already used in the independently replayed `n=4` proof.

## 6. Asymptotic additive gain

Let

\[
C_k=\binom{2k}{k}.
\]

Take

\[
x_k=2k-c
\]

for a fixed real `c>1/2`. Standard gamma-ratio expansions give

\[
\frac{\binom{2k-c}{k}}{\binom{2k}{k}}
=
2^{-c}
\left(
1+\frac{c(1-c)}{4k}+O(k^{-2})
\right)
\tag{6.1}
\]

and

\[
\frac{\binom{2k-c}{k-1}}{\binom{2k}{k-1}}
=
2^{-c}
\left(
1+\frac{c(1-c)}{4k}+\frac{c}{k}+O(k^{-2})
\right).
\tag{6.2}
\]

The floors and ceilings contribute only `O(1)`. Substituting (6.1)--(6.2) into Theorem 1.1 and comparing with the central first-Koszul ratio gives

\[
L_{\mathrm{MS}}(2k)-L_K(2k)
\ge
4^{-c}(2c-1)\frac{C_k}{k}
+O\left(\frac{C_k}{k^2}\right).
\tag{6.3}
\]

The function

\[
f(c)=(2c-1)4^{-c}
\]

has its unique maximum at

\[
c_*
=
\frac{1+1/\log 2}{2},
\]

where

\[
f(c_*)=rac{1}{2e\log2}.
\]

Therefore:

### Theorem 6.1

As `k` tends to infinity,

\[
\boxed{
\operatorname{ChowRank}(P_{2k})
\ge
L_K(2k)
+
\left(
\frac{1}{2e\log2}+o(1)
\right)
\frac{\binom{2k}{k}}{k}.
}
\tag{6.4}
\]

Equivalently, for even `n`,

\[
\boxed{
\operatorname{ChowRank}(P_n)
\ge
L_K(n)
+
\left(
\frac{1}{e\log2}+o(1)
\right)
\frac{\binom n{n/2}}{n}.
}
\tag{6.5}
\]

The additive gain has scale

\[
\Theta\left(\frac{2^n}{n^{3/2}}\right).
\]

It is stronger than the previously recorded zero-intersection shadow-removal additive term, but it still leaves a multiplicative gap of order `sqrt(n)` from Glynn's `2^(n-1)` upper bound.

## 7. What this result does not prove

1. It does not prove `ChowRank(perm_n)=2^(n-1)`.
2. It does not prove `ChowRank(perm_6)=32`; the current certified interval is `23<=rank<=32`.
3. It does not classify equality in the subspace degeneration step.
4. It does not extend as written to odd `n`, because the proof uses a self-transpose middle catalecticant.
5. It does not provide a border Chow-rank improvement beyond the ordinary determinantal Koszul bound.
6. The literature novelty of this exact combination of central catalectics and multidimensional shadows remains unverified.

## 8. Reproduction

```bash
python -m unittest tests.test_even_multishadow -v
python scripts/generate_even_multishadow_bounds.py
```

Both commands use only the Python standard library and exact rational/integer arithmetic.
