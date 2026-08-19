# The quartic four-block zero theorem at order six

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`, `EXACT_FINITE_INTERFACES_REPLAYED`.

Let `T_1,...,T_4` be arbitrary degree-six Chow terms. Then

\[
\boxed{
\mathcal D_4(\operatorname{perm}_6)\cap
\sum_{i=1}^4\mathcal D_4(T_i)=0.
}
\tag{0.1}
\]

This closes `(m,n,q)=(4,6,4)`. It is a literal derivative-space theorem; it does not determine `ChowRank(perm_6)`, identify a coupled image with a literal sum, or make a border-rank or novelty claim.

## 1. Pair-supported polars

Assume

\[
0\ne f=f_1+f_2+f_3+f_4\in\mathcal D_4(\operatorname{perm}_6),
\qquad f_i\in\mathcal D_4(T_i).
\]

Put `E=Ess(f)`, `e=dim E`, and `M_i=Ess(f_i)`, `r_i=dim M_i<=6`. The permanent linear-shadow theorem gives `e>=16`.

Fix `I={i,j}` and complementary `J={k,l}`. The restrictions to `E` of covectors annihilating `W_J=M_k+M_l` form

\[
A_I=\operatorname{Ann}_{E^*}(E\cap W_J),
\qquad
\dim A_I=e-\dim(E\cap W_J)\ge e-\dim W_J\ge4.
\tag{1.1}
\]

The polar map on `E` is injective. Extending each covector to annihilate `W_J` therefore gives a space `S_I` of the same dimension with

\[
S_I\subseteq\mathcal D_3(\operatorname{perm}_6)
\cap\bigl(\mathcal D_3(T_i)+\mathcal D_3(T_j)\bigr)
\cap\operatorname{Sym}^3(M_i+M_j).
\tag{1.2}
\]

Thus every pair supports a nonzero cubic two-term witness.

## 2. Cubic pair equality at order six

### Lemma 2.1

If

\[
0\ne g=g_1+g_2\in\mathcal D_3(\operatorname{perm}_6),
\qquad g_a\in\mathcal D_3(U_a)
\]

for degree-six Chow terms, and `N_a=Ess(g_a)`, then

\[
\boxed{
\dim N_1=\dim N_2=6,
\quad\dim(N_1\cap N_2)=3,
\quad\dim(N_1+N_2)=9.
}
\tag{2.1}
\]

### Proof

Write `s_a=dim N_a`, `h=dim(N_1 intersect N_2)`, and `d=s_1+s_2-h`. The permanent shadow floor gives `d>=9`, while `s_a<=6` gives `h<=3`.

Private covectors annihilating the opposite component give quadratic spaces

\[
Q_a\subseteq\mathcal D_2(\operatorname{perm}_6)\cap\operatorname{Sym}^2N_a,
\qquad\dim Q_a=s_a-h.
\]

The exact product-shadow value is `F_(6,2)(4)=8`. If `dim Q_a>=4`, its linear derivative shadow has dimension at least eight but is contained in the at-most-six-dimensional `N_a`. Hence `s_a-h<=3`. Therefore

\[
9\le d=s_1+s_2-h\le h+6,
\]

so `h=3`; equality then forces `s_1=s_2=6` and `d=9`. QED.

Applying the lemma to a nonzero member of each `S_I` forces, for every pair,

\[
\boxed{
dim M_i=6,
\quad dim(M_i\cap M_j)=3,
\quad dim(M_i+M_j)=9.
}
\tag{2.2}
\]

## 3. Second pair-supported squeeze

Equation (2.2) applies to the complementary pair, so `dim W_J=9`. Equation (1.1) sharpens to

\[
\boxed{\dim S_I\ge e-9\ge7.}
\tag{3.1}
\]

In particular `S_I` contains a two-plane `S`. The exact order-two shadow tier for cubic permanent derivatives says

\[
\dim S=2\quad\Longrightarrow\quad\dim\partial^2S\ge12.
\tag{3.2}
\]

But (1.2) puts `S` inside `Sym^3(M_i+M_j)`, so all second derivatives are linear forms in the nine-dimensional space `M_i+M_j`. Thus `dim partial^2 S<=9`, contradicting (3.2). This proves (0.1).

## 4. Boundary and verification

The theorem gives

\[
\boxed{\mu(6,4)\ge5,}
\]

where `mu(n,m)` is the least literal Chow-block size with nonzero intersection. Padding the eight-term decomposition of `perm_4` gives `mu(6,4)<=8`; sizes five through seven remain open.

At total `qn=24`:

```text
(12,4,2) NONZERO -- sharp pair construction
(8,4,3)  OPEN
(6,4,4)  ZERO    -- this theorem
(4,4,6)  ZERO    -- ChowRank(perm_4)=8.
```

The primary replay checks `F_(6,2)(4)=8`, the unique pair-equality state, and all 79,800 coordinate pairs yielding the cubic two-plane linear-shadow minimum 12. An independent implementation reconstructs the same interfaces without importing the primary module.
