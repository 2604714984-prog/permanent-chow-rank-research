# N6-134: fixed-matching average exclusion in the (K_{3,2}) graph chart

## Theorem and scope

Let (A) have dimension (3), let (P,Q) have dimension (2), and fix a
(2+2) column matching (Pleftrightarrow Q).  Normalize the relative map
to (T=I_6) by the diagonal/monomial coordinate changes preserving the
squarefree column spaces.  For an arbitrary (6	imes6) average matrix (S),
consider

\[
 L=\operatorname{graph}(I+S),\qquad
 M=\operatorname{graph}(S-I).
\]

N6-134 proves, in characteristic zero,

\[
 \operatorname{rank}\beta_{E_{34}}(L,M)\le6
 \quad\Longrightarrow\quad S=0.
\]

Thus the whole average direction is excluded in this fixed matching slice,
not merely its tangent space at (S=0).  The conclusion is still a restricted
graph theorem: it does not prove that an arbitrary invertible relative map
has a matching, and it does not cover non-graph charts.

## 1. Annihilator equation

With respect to (P\oplus Q), write a target tensor as

\[
 R=\begin{pmatrix}A&B\\B^{\mathsf T}&C\end{pmatrix},
 \qquad
 A\in\mathcal A, B\in\mathcal B, C\in\mathcal C,
\]

where

\[
 \dim(\mathcal A,\mathcal B,\mathcal C)=(3,12,3).
\]

The annihilator condition is the (6\times6) matrix equation

\[
 F_S(A,B,C)=A+B(S-I)+(S+I)^{\mathsf T}B^{\mathsf T}
 +(S+I)^{\mathsf T}C(S-I)=0. \tag{1.1}
\]

The rank of this (36\times18) linear map is exactly the cross-image rank.
Since (A\mapsto A) is injective, a kernel of dimension at least twelve
projects injectively to the (B,C) variables.

Taking the skew part of (1.1) gives

\[
 \operatorname{skew}(B+S^{\mathsf T}C)=0. \tag{1.2}
\]

The skew image of (mathcal B) is the three-dimensional space (U) whose
row-edge blocks are scalar multiples of
\(\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\).  If the cross rank is at most six,
the skew subsystem has rank at most three.  Consequently

\[
 \operatorname{skew}(S^{\mathsf T}\mathcal C)\subseteq U. \tag{1.3}
\]

## 2. The six-dimensional exceptional average subspace

Comparing the 36 coefficient equations in (1.3) gives the exact form

\[
 S=\operatorname{diag}(S_0,S_1,S_2),qquad
 S_i=\begin{pmatrix}
 (\tau+\delta_i)/2&u\\
 v&(\tau-\delta_i)/2
 \end{pmatrix}. \tag{2.1}
\]

The parameters are (\tau,u,v,\delta_0,\delta_1,\delta_2).  The coefficient
matrix has exact rational rank (30) and nullity (6); this is the first
part of the frozen certificate.

## 3. Row-edge rank-three minors

Because (S) is block diagonal, (1.1) splits over the three row edges.  For a
row pair (i<j), the variables are one (A)-coordinate, four entries of the
corresponding (B_{ij}), and one (C)-coordinate.  The resulting matrix is
an (8\times6) matrix (M_{ij}).  It always has rank at least two: a fixed
(2\times2) minor equals (2).

If (\operatorname{rank}M_{ij}\le2), the following exact (3\times3) minors
must vanish:

\[
 4v,quad 4u,quad 2(\delta_i-\delta_j),quad
 \delta_i+\delta_j+2\tau,quad
 \delta_i+\delta_j-2\tau. \tag{3.1}
\]

In characteristic zero this forces

\[
 u=v=\delta_i=\delta_j=\tau=0. \tag{3.2}
\]

If the full cross rank is at most six, the three row-edge ranks sum to at most
six.  Their lower bound two therefore forces every row-edge rank to be two.
Applying (3.2) to pairs ((0,1)) and ((0,2)) gives all six parameters zero.
Hence (S=0).

## Evidence and boundary

The coefficient ranks and minors are exact over (mathbb Q), not finite-field
or random evidence.  The accompanying script regenerates the 36-by-36
exceptional-space rank and the symbolic (8\times6) minors.

This theorem covers only a fixed relative matching (T=I) up to diagonal or
monomial normalization.  N6-129 separately proves the matching lemma for
the average-zero symmetric graph pair \(\operatorname{graph}(T),
\operatorname{graph}(-T)\); the two results do not combine automatically for
a general coupled pair \(\operatorname{graph}(S+T),
\operatorname{graph}(S-T)\), where both the average and relative operators
vary.  N6-134 also does not cover non-graph charts or the transpose endpoint,
and it does not exclude the relaxed matching product pair from being an
actual Chow section difference (N6-115 still gives block projection rank at
most nine).  It therefore does not yet prove ordinary lower (29), exact
\(\operatorname{ChowRank}(\operatorname{perm}_6)\), or the general
\(2^{n-1}) conjecture.

Replay:

```text
python scripts/n6_k32_fixed_matching_average_exclusion.py \\
  --verify-json data/n6_k32_fixed_matching_average_exclusion.json
python -m unittest tests.test_n6_k32_fixed_matching_average_exclusion -v
```
