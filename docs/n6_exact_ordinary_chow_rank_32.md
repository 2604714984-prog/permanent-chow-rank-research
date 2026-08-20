# Exact ordinary Chow rank of the six-by-six permanent

## Status and scope

`PURE/EXACT ORDINARY-RANK THEOREM; TWO INDEPENDENT SCOPE AUDITS PASS.`

Over an algebraically closed field of characteristic zero,

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_6)=32.}
\]

This theorem concerns ordinary Chow rank. It makes no border-rank claim and
does not prove the conjectural formula for general \(n\).

The adjacent script replays the finite rank rows and final arithmetic. The
geometric scope, degeneration, and filtration arguments are proved below and
are not delegated to the replay.

## 1. Symmetric image-span lemma

Let \(A_i:W^*\to W\) be symmetric linear maps, let
\(r_i=\operatorname{rank}A_i\), and put
\(D=\dim\sum_i\operatorname{im}A_i\). Then

\[
\operatorname{rank}\Bigl(\sum_iA_i\Bigr)
\ge 2D-\sum_i r_i. \tag{1.1}
\]

Symmetry gives \(\ker A_i=(\operatorname{im}A_i)^\perp\). Choose
\(B_i:k^{r_i}\to W\) onto the image. The induced form on the rank quotient
is nondegenerate, so \(A_i=B_iJ_iB_i^*\) for an invertible symmetric
\(J_i\). For \(B=[B_1\ \cdots\ B_N]\) and block diagonal \(J\), Sylvester's
rank inequality applied to \(BJB^*\) proves (1.1). Singular \(A_i\) are
therefore included.

## 2. Half-defect quotient-symbol lemma

For a nonzero degree-six Chow term \(T\), put

\[
L=\langle\ell_1,\ldots,\ell_6\rangle,\qquad
U=\mathcal D_3(T),\qquad u=\dim U,
\]

\[
F=\mathcal D_2(T),\qquad R=F\cap E_2.
\]

For every quotient \(P:L\to D\) of rank \(d\), the actual permanent
quotient symbol satisfies

\[
\boxed{
\operatorname{rank}\beta_{P,R}+\frac{20-u}{2}
\ge\frac{10}{3}d.} \tag{2.1}
\]

The word *every* is load-bearing: \(P\) may be the quotient by an arbitrary
previous factor span. The result is not restricted to coordinate quotients
or to six independent formal labels.

For factor-span dimension at most four, a diagonal one-parameter subgroup
degenerates \(T\) to a monomial with all active exponents positive. Middle
catalectic rank is upper semicontinuous, giving the floors

\[
1,2,4,8
\]

for span dimensions one through four. The permanent-quadratic intersection
has dimension at most one, the kernel-preimage estimate treats intermediate
quotients, and a full quotient is injective because
\(E_2^{(1)}=E_3\) while a nonzero permanent cubic has at least nine
essential variables.

For factor-span dimension six, the established actual symbol row is

\[
(0,7,10,10,15,17,20).
\]

For factor-span dimension five, the five normal forms

\[
x_1x_2x_3x_4x_5(x_1+\cdots+x_s),\qquad1\le s\le5,
\]

have the following valid rows for
\(\operatorname{rank}\beta+(20-u)/2\):

\[
\begin{array}{c|c}
s&d=0,\ldots,5\\ \hline
5&(0,7,10,10,15,17)\\
4&(0,8,12,13,16,19)\\
3&(1,8,11,11,16,18)\\
1,2&(3,9,9,10,16,17).
\end{array}
\]

The \(s=1,2\) row uses the seven-dimensional directional-shadow floor and
the one-dimensional-kernel gap at quotient rank four. Every displayed entry
dominates \(10d/3\), proving (2.1) for every factor rank, including repeated
factors.

## 3. Global derivative symbol

Delete zero summands and suppose

\[
\operatorname{perm}_6=\sum_{i=1}^N T_i.
\]

Using the natural divided-power pairing, let
\(A_i=C_{3,3}(T_i):W^*\to W\) be the symmetric middle catalectic and set

\[
U_i=\operatorname{im}A_i,quad u_i=\dim U_i,quad
\delta_i=20-u_i,quad \Delta=\sum_i\delta_i.
\]

Put \(U=\sum_iU_i\) and \(h=\dim(U/E_3)\). Since the permanent middle
catalectic has rank 400 and image \(E_3\), (1.1) gives

\[
\boxed{h\le10N-200-\frac{\Delta}{2}.} \tag{3.1}
\]

Let \(F=\sum_i\mathcal D_2(T_i)\) and \(Q=F/E_2\). Differentiating the
decomposition twice gives \(E_2\subset F\). The global quotient derivative
symbol

\[
\widetilde\beta:\bigoplus_iU_i\longrightarrow V\otimes Q
\]

factors through the summation map. Its kernel is exactly

\[
\left\{(g_i):\sum_i g_i\in E_3\right\},
\]

because \(E_2^{(1)}=E_3\). Thus its image is an injective copy of
\(U/E_3\) and has dimension exactly \(h\). Overlaps among the \(U_i\) are
already included in this kernel; no literal-directness assumption appears.

## 4. Factor filtration and cancellation

Let \(L_i\) be the actual factor span of \(T_i\). Since
\(E_2\subset F\) and \(\partial E_2=V\), the \(L_i\) span all 36 variables.
Choose any ordering, put \(W_i=\sum_{j\le i}L_j\), and let
\(d_i=\dim(W_i/W_{i-1})\). Then \(\sum_i d_i=36\).

Projection to \((W_i/W_{i-1})\otimes Q\) kills all earlier symbol blocks.
For the current block, the quotient

\[
P_i:L_i\longrightarrow L_i/(L_i\cap W_{i-1})
\]

is an arbitrary quotient of rank \(d_i\), precisely the scope of (2.1).
Moreover,

\[
F_i/(F_i\cap E_2)\longrightarrow F/E_2=Q
\]

is injective. Hence the target remains the same fixed global quotient at
every step, and the projected ranks add. Summing (2.1) gives

\[
\boxed{h\ge120-\frac{\Delta}{2}.} \tag{4.1}
\]

Comparing (3.1) and (4.1) cancels the complete individual-rank defect:

\[
120-\frac{\Delta}{2}
\le10N-200-\frac{\Delta}{2},
\]

so \(N\ge32\). Glynn's 32-term identity supplies the matching ordinary
upper bound.

## 5. Reproduction and boundary

```text
python scripts/n6_exact_ordinary_chow_rank_32.py \
  --verify-json data/n6_exact_ordinary_chow_rank_32.json
python -m unittest tests.test_n6_exact_ordinary_chow_rank_32 -v
```

The older fixed-six and \(b=40,\ldots,46\) programs remain independent
structural evidence but are not dependencies of this theorem. Border rank
and the unrestricted general-\(n\) formula remain open.
