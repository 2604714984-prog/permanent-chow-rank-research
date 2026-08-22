# Exact squarefree quotient-symbol profile

## Status and claim boundary

`PROOF_COMPLETE`, `GENERAL_N_EXACT_LOCAL_THEOREM`,
`ADJACENT_ADDIVITY_ROUTE_BARRIER`, `EXACT_COMBINATORIAL_REPLAYED`.

Let \(F\) be an \(n\)-dimensional vector space with basis
\(z_1,\ldots,z_n\).  Put

\[
\operatorname{Sq}^k(F)
=
\operatorname{span}\{
z_I=\prod_{i\in I}z_i: I\subseteq[n],\ |I|=k
\}
\subseteq\operatorname{Sym}^kF.
\]

This is the degree-\(k\) derivative space of the independent Chow term

\[
T_0=z_1\cdots z_n.
\]

For a quotient \(P:F\twoheadrightarrow D\) of rank \(d\), define the quotient
symbol

\[
\partial_{k,P}:
\operatorname{Sq}^k(F)
\longrightarrow
D\otimes\operatorname{Sym}^{k-1}F
\]

by

\[
\partial_{k,P}(z_I)
=
\sum_{i\in I}P(z_i)\otimes z_{I\setminus\{i\}}.
\]

The main theorem is

\[
\boxed{
\min_{\operatorname{rank}P=d}
\operatorname{rank}\partial_{k,P}
=
\binom nk-\binom{n-d}{k}.
}
\tag{0.1}
\]

A coordinate quotient attains equality.

Consequently, using one common quotient \(P\) on two adjacent derivative
degrees but keeping their outputs in a direct sum gives exactly the sum of the
two separate caps:

\[
\boxed{
\min_P
\operatorname{rank}
(\partial_{k,P}\oplus\partial_{k+1,P})
=
\binom nk+\binom n{k+1}
-\binom{n-d}{k}-\binom{n-d}{k+1}.
}
\tag{0.2}
\]

Across all positive derivative degrees,

\[
\boxed{
\min_P
\sum_{k=1}^n\operatorname{rank}\partial_{k,P}
=
2^n-2^{n-d}.
}
\tag{0.3}
\]

Thus merely sharing the factor quotient does not create cross-degree
compression.  A useful multi-degree invariant must also quotient or measure
the commutation relations between the levels.

This is an exact theorem for the independent full-factor Chow term.  It does
not classify arbitrary repeated or dependent factors and does not produce a
new Chow-rank lower bound.

## 1. Kernel of the quotient symbol

Let

\[
K=\ker P,
\qquad
\dim K=n-d.
\]

### Lemma 1.1

For every \(1\le k\le n\),

\[
\boxed{
\ker\partial_{k,P}
=
\operatorname{Sq}^k(F)\cap\operatorname{Sym}^kK.
}
\tag{1.1}
\]

### Proof

Choose a complement \(F=K\oplus C\) and identify \(P\) with the projection onto
\(C\).  The full polarization map

\[
\delta_k:\operatorname{Sym}^kF
\longrightarrow
F\otimes\operatorname{Sym}^{k-1}F
\]

sends a polynomial to the tuple of its first derivatives.  The composite
\((P\otimes1)\delta_k\) records exactly the derivatives in the \(C\)
directions.

In characteristic zero, all those derivatives vanish if and only if the
polynomial is independent of the \(C\) variables, equivalently if and only if
it lies in \(\operatorname{Sym}^kK\).  Restricting to the squarefree subspace
proves (1.1).

## 2. Maximum squarefree intersection with a symmetric power

Put \(r=n-d\).

### Lemma 2.1

For every \(r\)-plane \(K\subseteq F\),

\[
\boxed{
\dim\bigl(
\operatorname{Sq}^k(F)\cap\operatorname{Sym}^kK
\bigr)
\le
\binom rk.
}
\tag{2.1}
\]

Equality is attained by every coordinate \(r\)-plane.

### Proof

Consider the Grassmannian \(\operatorname{Gr}(r,F)\).  The function

\[
K\longmapsto
\dim\bigl(
\operatorname{Sq}^k(F)\cap\operatorname{Sym}^kK
\bigr)
\]

is upper semicontinuous, because it is an intersection dimension of two
algebraic families of subspaces.  Its maximum locus is therefore nonempty,
closed, and invariant under the diagonal torus preserving
\(\operatorname{Sq}^k(F)\).

The closure of a torus orbit in a projective variety contains a torus-fixed
point.  Hence the maximum is attained at a torus-fixed \(r\)-plane.  Such a
plane is spanned by \(r\) coordinate vectors.  Its symmetric power meets the
squarefree space in the span of the squarefree monomials supported on those
\(r\) coordinates, of dimension \(\binom rk\).  This proves (2.1).

Combining Lemmas 1.1 and 2.1 gives

\[
\operatorname{rank}\partial_{k,P}
\ge
\binom nk-\binom{n-d}{k}.
\]

For a coordinate quotient, the kernel consists exactly of the squarefree
\(k\)-subsets contained in the coordinate kernel, so equality holds.  This
proves (0.1).

## 3. Adjacent degrees are exactly additive without a relation quotient

Define

\[
\Gamma_{k,P}
=
\partial_{k,P}\oplus\partial_{k+1,P}.
\]

The two summands land in different graded target spaces,

\[
D\otimes\operatorname{Sym}^{k-1}F
\quad\text{and}\quad
D\otimes\operatorname{Sym}^{k}F.
\]

Therefore, for every fixed \(P\),

\[
\operatorname{rank}\Gamma_{k,P}
=
\operatorname{rank}\partial_{k,P}
+
\operatorname{rank}\partial_{k+1,P}.
\tag{3.1}
\]

Theorem (0.1) bounds both terms below.  One coordinate quotient attains both
lower bounds simultaneously.  Hence (0.2) follows.

This is the exact obstruction to the first naive post-`perm_6` proposal:
using the same quotient at adjacent levels is not itself a coupling.  The
shared label does not reduce the one-term cap while the graded outputs remain
a direct sum.

## 4. The complete positive-degree profile

Summing (0.1) over \(k=1,\ldots,n\) gives

\[
\begin{aligned}
\sum_{k=1}^n
\left(
\binom nk-\binom{n-d}{k}
\right)
&=
(2^n-1)-(2^{n-d}-1)\\
&=
2^n-2^{n-d}.
\end{aligned}
\]

Again a coordinate quotient attains all degreewise minima simultaneously, so
(0.3) is exact.

In particular, a rank-one quotient has exact total symbol rank

\[
2^{n-1},
\]

while the full quotient has rank

\[
2^n-1.
\]

These large values do not prove the permanent conjecture: the permanent-side
global comparison and the arbitrary degenerate-term cap are separate
requirements.  The result only shows that a block-diagonal derivative tower
does not gain efficiency from reusing the quotient.

## 5. Consequence for the general-`n` program

The smallest candidate capable of escaping the middle-symbol ceiling must do
more than form

\[
\partial_{k,P}\oplus\partial_{k+1,P}.
\]

It must identify, quotient, or measure the common second-derivative relations.
The first natural next object is the two-step Koszul/mapping-cone fragment

\[
\operatorname{Sq}^{k+1}(F)
\longrightarrow
D\otimes\operatorname{Sq}^{k}(F)
\longrightarrow
\bigwedge^2D\otimes\operatorname{Sq}^{k-1}(F),
\]

or its permanent-relative quotient analogue.  Promotion requires a joint
one-term cap strictly below the additive value in (0.2), together with a
global sum or subquotient inequality.

## 6. Claim boundary

```text
single independent Chow term quotient profile    EXACT
adjacent direct-sum shared quotient               EXACTLY ADDITIVE
all positive degrees direct sum                   EXACTLY ADDITIVE
arbitrary dependent/repeated Chow term            OPEN
cross-degree Koszul homology quotient             OPEN
new ordinary Chow-rank lower bound                NO
new border-rank lower bound                       NO
general Glynn optimality                          OPEN
literature novelty                                NOT ESTABLISHED
```

## 7. Reproduction

```bash
python scripts/general_squarefree_quotient_symbol_profile.py \
  --verify-json data/general_squarefree_quotient_symbol_profile.json

python scripts/general_squarefree_quotient_symbol_profile_independent.py \
  --max-n 9

python -m unittest \
  tests.test_general_squarefree_quotient_symbol_profile -v
```
