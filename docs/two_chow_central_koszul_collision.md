# Central transversality does not imply Koszul transversality

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` (G-032).
This is a pure characteristic-zero counterexample theorem with an exact
rational coefficient replay.  It is a route barrier, not a decomposition of
a permanent.

## 1. Statement

Let `V` contain a direct sum of three-planes

\[
 A=\langle a_1,a_2,a_3\rangle,
 \qquad
 B=\langle b_1,b_2,b_3\rangle.
\]

Put

\[
\begin{aligned}
 p_A&=a_1a_2a_3,
 &p'_A&=(a_1+a_2)(a_1+a_3)(a_2+a_3),\\
 p_B&=b_1b_2b_3,
 &p'_B&=(b_1+b_2)(b_1+b_3)(b_2+b_3),
\end{aligned}
\]

and define two sextic Chow terms

\[
 T_0=p_Ap_B,
 \qquad
 T_1=p'_Ap'_B.                                    \tag{1.1}
\]

The six factors of each term are linearly independent.  Write

\[
 U_i=\mathcal D_3(T_i),
 \qquad
 Y_i=\delta_3(U_i\otimes V).
\]

### Theorem 1.1

Over every field of characteristic zero,

\[
 \boxed{U_0\cap U_1=0}                            \tag{1.2}
\]

but

\[
 \boxed{\dim(Y_0\cap Y_1)=18.}                   \tag{1.3}
\]

If `dim V=N`, then

\[
 \dim Y_0=\dim Y_1=20N-15,
 \qquad
 \dim(Y_0+Y_1)=40N-48.                            \tag{1.4}
\]

In particular, in the 36-variable ambient space used for `perm_6`, the two
individual ranks are 705 while their output sum has rank 1392, not 1410.

## 2. The middle derivative spaces are disjoint

For a ternary cubic `p`, write `D_r(p)` for its output-degree-`r` derivative
space.  Put

\[
 Q_A=D_2(p_A),
 \qquad
 Q'_A=D_2(p'_A),
\]

and define `Q_B,Q'_B` analogously.  Explicitly,

\[
 Q_A=\langle a_1a_2,a_1a_3,a_2a_3\rangle.
\]

Modulo `Q_A`, the three pairwise products of

\[
 a_1+a_2,quad a_1+a_3,quad a_2+a_3
\]

are respectively `a_1^2,a_2^2,a_3^2`.  Hence

\[
 Q_A\oplus Q'_A=\operatorname{Sym}^2A,            \tag{2.1}
\]

and similarly `Q_B direct_sum Q'_B=Sym^2 B`.

The central derivative space of a product on `A direct_sum B` splits by
bidegree:

\[
 \mathcal D_3(p_Ap_B)
 =\bigoplus_{r=0}^3D_r(p_A)\otimes D_{3-r}(p_B).  \tag{2.2}
\]

At bidegrees `(1,2)` and `(2,1)`, equation (2.1) makes the corresponding
spaces for `T_0` and `T_1` complementary.  At the two endpoint bidegrees,
`p_A,p'_A` and `p_B,p'_B` are linearly independent.  Therefore (2.2) proves
(1.2), and each `U_i` has dimension 20.

Writing `F=U_0 direct_sum U_1`, the same argument gives the more useful
description

\[
\begin{aligned}
F={}&\langle p_A,p'_A\rangle
\oplus(\operatorname{Sym}^2A\otimes B)\\
&\oplus(A\otimes\operatorname{Sym}^2B)
\oplus\langle p_B,p'_B\rangle.                   \tag{2.3}
\end{aligned}
\]

## 3. The endpoint pencil has no prolongation

Put `P_A=span(p_A,p'_A)`.  Every nonzero element of `P_A` is concise in the
three variables of `A`.  Indeed, for

\[
 u=u_1\partial_{a_1}+u_2\partial_{a_2}+u_3\partial_{a_3},
\]

the square coefficients of `partial_u p'_A` are

\[
 (u_2+u_3,\ u_1+u_3,\ u_1+u_2).                  \tag{3.1}
\]

The matrix of (3.1) has determinant two.  Thus, if the coefficient of `p'_A`
in a pencil member is nonzero, a vanishing directional derivative forces
`u=0`; if that coefficient is zero, the three derivatives of `p_A` are
visibly independent.

Consequently

\[
 \boxed{P_A^{(1)}=0.}                             \tag{3.2}
\]

For if a nonzero quartic had every first derivative in the two-plane `P_A`,
its essential-variable space would have dimension at most two.  Some nonzero
cubic derivative would then depend on at most two variables, contradicting
the conciseness of every nonzero pencil member.  The same proof gives
`P_B^(1)=0`.

## 4. The 48-dimensional prolongation

The prolongation `F^(1)` splits into quartic bidegrees.  Equation (2.3) and
(3.2) give

\[
\begin{array}{c|ccccc}
\text{bidegree}&(4,0)&(3,1)&(2,2)&(1,3)&(0,4)\\ \hline
F^{(1)}&0&P_A\otimes B&
\operatorname{Sym}^2A\otimes\operatorname{Sym}^2B&
A\otimes P_B&0.
\end{array}                                       \tag{4.1}
\]

Therefore

\[
 \boxed{\dim F^{(1)}=0+6+36+6+0=48.}             \tag{4.2}
\]

The same calculation remains valid after embedding `A direct_sum B` in a
larger `V`: a quartic involving a variable outside `A direct_sum B` cannot
have all derivatives in `F`.

For any subspace `W subset Sym^3 V`, the kernel of the first Koszul map on
`W tensor V` is `W^(1)`.  Each `U_i` is the middle derivative space of a
six-independent-factor term, so

\[
 \dim U_i^{(1)}=\binom64=15.
\]

It follows that

\[
\begin{aligned}
\dim Y_i&=20N-15,\\
\dim(Y_0+Y_1)
&=\operatorname{rank}\delta_3(F\otimes V)
=40N-48.
\end{aligned}
\]

Subtracting proves (1.3).

## 5. Exact replay and consequence

Run

```text
python scripts/two_chow_central_koszul_collision.py \
  --json data/two_chow_central_koszul_collision.json
python -m unittest tests/test_two_chow_central_koszul_collision.py
```

The script constructs the two central derivative spaces, verifies their
combined rank 40, and builds all coefficient constraints defining the first
prolongation of their sum.  Exact elimination over `Fraction` gives nullity
48 and hence Koszul intersection 18.  No finite-field or floating-point
inference is used.

The theorem closes one tempting lower-27 shortcut.  Even when every residual
term has full middle rank and the individual middle images are in direct sum,
ordinary first-Koszul output collisions need not vanish.  A successful
lower-27 argument must retain the actual cross-degree relation module or the
specific equation with `perm_6`; central transversality alone is insufficient.
