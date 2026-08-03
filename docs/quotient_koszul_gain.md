# The quotient Koszul gain and the next `n=6` obstruction

## Status

`PROOF_DRAFT_COMPLETE` — all linear-algebra implications below are written explicitly. The finite diagonal-term replay is deterministic and exact modulo a prime, with a matching characteristic-zero upper bound. External peer review and a complete literature novelty review have not been performed.

## 1. Setup

Let

\[
P_n=\operatorname{perm}_n,
\qquad
N=n^2,
\qquad
2\le m\le n-2,
\qquad
r=n-m.
\]

For a form `f`, write

\[
\mathcal D_j(f)=\operatorname{im}C_{n-j,j}(f).
\]

Fix a form `R` and set

\[
E_m=\mathcal D_m(P_n),
\qquad
H_m=\mathcal D_m(R),
\]

\[
E_r=\mathcal D_r(P_n),
\qquad
H_r=\mathcal D_r(R).
\]

Let

\[
h=\operatorname{rank}C_{r,m}(R),
\qquad
a=\dim(E_m\cap H_m),
\qquad
b=\dim(E_r\cap H_r).
\]

Thus

\[
\dim H_m=\dim H_r=h.
\]

The permanent first-Koszul rank at output degree `m` is

\[
A_{n,m}
=
N\binom nm^2-inom n{m+1}^2.
\]

## 2. Retaining the quotient gain

Define the relative prolongation dimension

\[
p_E(H_m)
:=
\dim\left((E_m+H_m)^{(1)}/E_m^{(1)}\right)
\]

and the **quotient Koszul gain**

\[
\Gamma_E(H_m)
:=
N(h-a)-p_E(H_m).
\tag{2.1}
\]

### Proposition 2.1 — exact residual form of the double-quotient estimate

\[
\boxed{
\operatorname{rank}K_m(P_n-R)
\ge
A_{n,m}-Nb+\Gamma_E(H_m).
}
\tag{2.2}
\]

### Proof

The asymmetric catalectic double-quotient inequality gives

\[
\dim\mathcal D_m(P_n-R)
\ge
\binom nm^2+h-a-b.
\]

Moreover,

\[
\mathcal D_m(P_n-R)^{(1)}
\subseteq
(E_m+H_m)^{(1)},
\]

so

\[
\dim\mathcal D_m(P_n-R)^{(1)}
\le
\binom n{m+1}^2+p_E(H_m).
\]

The Koszul kernel--prolongation identity therefore yields

\[
\begin{aligned}
\operatorname{rank}K_m(P_n-R)
&\ge
N\left(\binom nm^2+h-a-b\right)
-
\left(\binom n{m+1}^2+p_E(H_m)\right)\\
&=
A_{n,m}-Nb+
\left(N(h-a)-p_E(H_m)\right).
\end{aligned}
\]

This is (2.2). ∎

### Proposition 2.2 — intrinsic meaning of `Gamma`

\[
\boxed{
\Gamma_E(H_m)
=
\operatorname{rank}\delta_m((E_m+H_m)\otimes V)
-
\operatorname{rank}\delta_m(E_m\otimes V).
}
\tag{2.3}
\]

In particular,

\[
0\le\Gamma_E(H_m)\le N(h-a).
\]

### Proof

The rank formula gives

\[
\operatorname{rank}\delta_m((E_m+H_m)\otimes V)
=
N\left(\dim E_m+h-a\right)
-
\dim(E_m+H_m)^{(1)}
\]

and

\[
\operatorname{rank}\delta_m(E_m\otimes V)
=N\dim E_m-\dim E_m^{(1)}.
\]

Subtracting gives exactly (2.1). Nonnegativity follows because enlarging the domain subspace cannot shrink the image. ∎

The earlier multidimensional-shadow theorem used only

\[
\Gamma_E(H_m)\ge0.
\]

Any improvement beyond that theorem must obtain positive information about this quotient image or use a different invariant.

## 3. A transversality criterion for full gain

For `H subset Sym^m V`, write

\[
\partial H
=
\operatorname{span}\{\partial_v h:v\in V^*,\ h\in H\}
\subseteq
\operatorname{Sym}^{m-1}V.
\]

### Lemma 3.1 — derivative-transverse prolongations split

Let

\[
H_0,\ldots,H_t\subseteq\operatorname{Sym}^mV.
\]

If

\[
\partial H_0\oplus\cdots\oplus\partial H_t
\]

is a direct sum, then

\[
H_0\oplus\cdots\oplus H_t
\]

is a direct sum and

\[
\left(H_0\oplus\cdots\oplus H_t\right)^{(1)}
=
H_0^{(1)}\oplus\cdots\oplus H_t^{(1)}.
\tag{3.1}
\]

Consequently,

\[
\operatorname{rank}\delta_m\left(\left(\sum_iH_i\right)\otimes V\right)
=
\sum_i\operatorname{rank}\delta_m(H_i\otimes V).
\tag{3.2}
\]

### Proof

A relation

\[
\sum_i h_i=0,
\qquad h_i\in H_i,
\]

can be differentiated. Directness of the derivative spaces forces every first derivative of every `h_i` to vanish, and homogeneity then gives `h_i=0`. Thus the original sum is direct.

Now take

\[
g\in\left(\bigoplus_iH_i\right)^{(1)}.
\]

For each coordinate derivative, decompose uniquely

\[
\partial_a g=\sum_i h_{i,a},
\qquad h_{i,a}\in H_i.
\]

Equality of mixed derivatives gives

\[
\sum_i
\left(
\partial_bh_{i,a}-\partial_ah_{i,b}
\right)=0.
\]

The `i`th summand lies in `partial H_i`. Directness therefore forces every summand to vanish separately. Each homogeneous polynomial-valued one-form `(h_{i,a})_a` is curl-free, so it integrates to a unique homogeneous form `g_i` of degree `m+1` with

\[
\partial_ag_i=h_{i,a}.
\]

Then `g_i in H_i^(1)` and `g=sum_i g_i`. This proves (3.1). Formula (3.2) follows from the Koszul rank formula. ∎

### Corollary 3.2

If

\[
\partial E_m\cap\partial H_m=0,
\]

then

\[
\Gamma_E(H_m)
=
\operatorname{rank}\delta_m(H_m\otimes V).
\tag{3.3}
\]

Thus the entire Koszul rank of `H_m` survives in the quotient.

## 4. An exact full-gain example at `n=6`

Set

\[
T_{\mathrm{diag}}
=
\prod_{i=0}^{5}x_{ii}.
\]

Let

\[
E=\mathcal D_3(P_6),
\qquad
F=\mathcal D_3(T_{\mathrm{diag}}).
\]

Then

\[
\dim E=400,
\qquad
\dim F=20,
\]

and

\[
\partial E=\mathcal D_2(P_6),
\qquad
\partial F=\mathcal D_2(T_{\mathrm{diag}}).
\]

The latter space is spanned by the diagonal pair monomials

\[
x_{ii}x_{jj}.
\]

Every permanent quadratic basis vector containing such a monomial also contains the unique off-diagonal companion

\[
x_{ij}x_{ji}.
\]

No other permanent quadratic basis vector contains that companion. Hence

\[
\mathcal D_2(P_6)
\cap
\mathcal D_2(T_{\mathrm{diag}})
=0.
\]

Corollary 3.2 gives

\[
\Gamma_E(F)
=
\operatorname{rank}K_3(T_{\mathrm{diag}})
=705.
\]

Therefore

\[
\operatorname{rank}\delta_3((E+F)\otimes V)
=14175+705
=14880.
\tag{4.1}
\]

The independent script

```text
scripts/n6_quotient_gain_audit.py
```

rebuilds both sparse integer matrices from the definitions and obtains rank `14,880` modulo `1,000,003`. Subadditivity gives the matching characteristic-zero upper bound `14,175+705`, so (4.1) is exact over every characteristic-zero field.

This example proves that the quotient term is not merely formal: the maximal one-term gain can occur. It does **not** prove a uniform gain for arbitrary Chow terms.

## 5. The quantified `n=6` target

For the central split `m=3`,

\[
A_{6,3}=14175,
\qquad
B_{6,3}=705.
\]

The current one-step multidimensional-shadow certificates give the following dangerous states.

| fixed terms `q` | intersection cap `b` | rank floor before `Gamma` | residual terms needed for total 24 | minimum required `Gamma` |
|---:|---:|---:|---:|---:|
| 3 | 24 | 13,311 | 21 | 790 |
| 4 | 40 | 12,735 | 20 | **661** |
| 5 | 60 | 12,015 | 19 | 676 |

For example, after fixing four terms, a lower bound of 24 requires

\[
12735+\Gamma_E(H)\ge13396,
\]

or equivalently

\[
\boxed{\Gamma_E(H)\ge661.}
\tag{5.1}
\]

This is the smallest threshold among the three displayed one-step states.

## 6. The zero-quotient branch is impossible for a short partial sum

In the central `n=6` case, suppose

\[
H=\mathcal D_3(R)\subseteq E=\mathcal D_3(P_6).
\]

Then all third derivatives of `R` lie in `E`, so

\[
R\in E^{(3)}.
\]

The permanent derivative tower gives

\[
E^{(3)}=\mathcal D_6(P_6)=\operatorname{span}(P_6).
\]

Thus `R=lambda P_6`. If `R` is a nonzero sum of fewer than 23 Chow terms, this contradicts the already proved lower bound

\[
\operatorname{ChowRank}(P_6)\ge23.
\]

If `R=0` is a nonempty partial sum of a minimal decomposition, deleting that subset produces a shorter decomposition, also impossible. Therefore every nonempty partial sum of fewer than 23 terms in a minimal decomposition has

\[
\dim((E+H)/E)>0.
\]

This qualitative fact does not by itself imply the quantitative threshold (5.1).

## 7. Claim boundary and next step

The proved statements are:

1. the exact residual identity (2.2);
2. the intrinsic quotient interpretation (2.3);
3. the derivative-transversality splitting criterion;
4. the full gain `Gamma=705` for the explicit diagonal term;
5. the exact `Gamma>=661` target for the current four-term `n=6` frontier.

No uniform lower bound on `Gamma` for arbitrary four-term sums is claimed. The next high-value problem is to classify when

\[
\partial E_3
\cap
\partial\mathcal D_3(R)
\neq0
\]

and to convert that lower-degree intersection geometry into a quantitative lower bound for `Gamma_E(H)`.