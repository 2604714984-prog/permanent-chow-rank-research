# A literal-six shadow exclusion for the layers `b=34,...,47`

**Status.** `PURE_LINEAR_ALGEBRA_REDUCTION`, `EXACT_INTEGER_DP_REPLAY`,
`B34_TO_B47_EXCLUDED`, `LOWER_28_FRONTIER_REDUCED_TO_B50` (N6-060).
The base field is algebraically closed of characteristic zero.  This note
continues the N6-058 fixed-six reduction under a hypothetical ordinary
twenty-seven-term Chow decomposition of `perm_6`.

The argument excludes every N6-058 layer

\[
 b=34,35,\ldots,46.
\]

It also excludes \(b=47\) directly, although that layer was already removed
by a term-prolongation cap.  The only N6-058 frontier left by this argument is
the all-alpha-three endpoint \(b=50\).

## 1. The residual permanent intersection

Write the hypothetical decomposition as

\[
 P=R+Q,
 \qquad P=\operatorname{perm}_6,
\tag{1.1}
\]

where \(R\) is the fixed sum of six Chow terms and \(Q\) is the sum of the
remaining twenty-one terms.  Put

\[
 E=\mathcal D_3(P),\qquad H=\mathcal D_3(R),\qquad
 G=\mathcal D_3(Q),
\tag{1.2}
\]

and write

\[
 \dim E=400,\qquad \dim H=h,\qquad
 b=\dim(E\cap H),\qquad g=\dim G.
\tag{1.3}
\]

Let

\[
 S=E\cap G.
\tag{1.4}
\]

The symmetric double-quotient inequality used in N6-058 gives

\[
 g\geq400+h-2b.
\tag{1.5}
\]

Linearity of derivative spaces gives

\[
 E\subseteq H+G,\qquad G\subseteq E+H,
 \qquad H\subseteq E+G.
\]

Therefore

\[
 E+G=H+G=E+H.
\]

Comparing dimensions gives

\[
 \dim S=g-h+b.
\tag{1.6}
\]

Combining (1.5) and (1.6),

\[
 \boxed{\dim S\geq400-b.}
\tag{1.7}
\]

## 2. A six-color literal lift

For the twenty-one residual terms write

\[
 U_j=\mathcal D_3(T_j),
 \qquad L=\sum_{j=1}^{21}U_j.
\tag{2.1}
\]

The coupled derivative space satisfies \(G\subseteq L\), so \(S\subseteq L\).
Choose any six residual indices \(A\), and let \(B\) be their fifteen-index
complement.  Set

\[
 L_A=\sum_{j\in A}U_j,
 \qquad L_B=\sum_{j\in B}U_j.
\tag{2.2}
\]

Every sextic Chow term has middle derivative rank at most twenty.  Therefore

\[
 \dim L_B\leq15\cdot20=300.
\tag{2.3}
\]

Moreover \(L=L_A+L_B\).  The image of \(S\) in \(L/L_A\) consequently has
dimension at most \(\dim L_B\).  Its kernel is \(S\cap L_A\).  Thus

\[
\begin{aligned}
 \dim(S\cap L_A)
 &\geq \dim S-\dim L_B\\
 &\geq (400-b)-300.
\end{aligned}
\]

Hence the literal six-color lift gives the uniform bound

\[
 \boxed{\dim(S\cap L_A)\geq100-b.}
\tag{2.4}
\]

Notice that no equality between a coupled derivative space and a literal
sum is being asserted here.  Only the inclusions \(S\subseteq G\subseteq L\)
and the decomposition \(L=L_A+L_B\) are used.

## 3. Product shadow versus the six-term projection cap

Suppose \(34\leq b\leq47\).  Equation (2.4) gives

\[
 \dim(S\cap L_A)\geq100-b\geq53.
\tag{3.1}
\]

Choose a 53-dimensional subspace

\[
 W\subseteq S\cap L_A.
\tag{3.2}
\]

Because \(W\subseteq E=\mathcal D_3(P)\), differentiation gives

\[
 \partial W\subseteq E_2.
\tag{3.3}
\]

Because \(W\subseteq L_A=\sum_{j\in A}\mathcal D_3(T_j)\), it also gives

\[
 \partial W\subseteq\sum_{j\in A}\mathcal D_2(T_j).
\tag{3.4}
\]

Therefore

\[
 \partial W\subseteq
 E_2\cap\sum_{j\in A}\mathcal D_2(T_j).
\tag{3.5}
\]

The exact product-shadow theorem N6-056 applies to every 53-plane in \(E\),
not only to coordinate subspaces.  Its exact integer minimum is

\[
 \dim\partial W\geq81.
\tag{3.6}
\]

On the other hand, the universal fixed-six quadratic projection bound is

\[
 \dim\left(E_2\cap
 \sum_{j\in A}\mathcal D_2(T_j)\right)\leq78.
\tag{3.7}
\]

Equations (3.5)--(3.7) give \(81\leq78\), a contradiction.  We have proved:

> **Theorem 3.1.** In the N6-058 fixed-six reduction, no layer
> \(34\leq b\leq47\) is realizable.

Since N6-058 had already reduced the unresolved lower-28 frontier to

\[
 \{34,35,\ldots,46,50\},
\]

Theorem 3.1 leaves only

\[
 \boxed{b=50.}
\tag{3.8}
\]

## 4. Exact integer replay and claim boundary

The script reuses the N6-056 colex-compression dynamic program and recomputes
the exact value \(m_{53}=81\).  It then checks (1.7), (2.4), and the strict
inequality \(81>78\) for each integer \(b=34,\ldots,47\).  This arithmetic
replay is supplementary; Sections 1--3 contain the mathematical proof.

```text
python scripts/n6_literal_six_shadow_b34_47_exclusion.py \
  --json data/n6_literal_six_shadow_b34_47_exclusion.json
python -m unittest tests.test_n6_literal_six_shadow_b34_47_exclusion -v
```

This result does not exclude the all-alpha-three \(b=50\) endpoint, prove
`ChowRank(perm_6)>=28`, determine the exact ordinary Chow rank, or make a
border-rank claim.
