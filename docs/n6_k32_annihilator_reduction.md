# N6-129: cross-annihilator reduction for a general (K_{3,2}) graph

## Statement

Let (A) have dimension (3), let (P,Q) have dimension (2), and let
(T:A\otimes P\to A\otimes Q).  Put
[
L=\operatorname{graph}(T),qquad M=\operatorname{graph}(-T).
]
This is the symmetric relative graph subchart.  A general pair in the full
graph chart has an additional common average operator and is not covered by
this statement.

The target (E_2=S_0(A)\otimes S_0(P\oplus Q)) has dimension (18).
Relative to (P\oplus Q), every element of (E_2) has three independent
parts:

[
E_2=\mathcal A\oplus\mathcal B\oplus\mathcal C,qquad
\dim(\mathcal A,\mathcal B,\mathcal C)=(3,12,3).
]

(mathcal A) is the (P\!P) column edge, (mathcal C) is the (Q\!Q)
column edge, and (mathcal B) is the four (P\!Q) column edges.

Define
[
b(T)=\dim\{B\in\mathcal B:BT=(BT)^{\mathsf T}\},
]
where (B) is viewed as the (6\times6) (P\)-to-(Q) block.  Define
[
c(T)=\dim\{C\in\mathcal C:T^{\mathsf T}CT\in\mathcal A\}.
]

The membership test is membership in the full 3-dimensional linear space
(mathcal A), not merely support containment in its matrix positions.  The
replay takes the quotient by the left-nullspace of an exact (mathcal A) basis.
This matters for general coordinate permutations, which can mix several
row-edge components while preserving the same set of nonzero positions.

Then the cross rank satisfies the exact identity
[
\operatorname{rank}\beta(L,M)=18-b(T)-c(T).
]
Consequently,
[
\operatorname{rank}\beta(L,M)\le6
\quad\Longrightarrow\quad b(T)+c(T)\ge12
\quad\Longrightarrow\quad b(T)\ge9,
]
because (dimmathcal C=3).

## Proof of the reduction

Write a target annihilator (Rin E_2) in grouped coordinates
(A\otimes P\oplus A\otimes Q) as
[
R=\begin{pmatrix}A_0&B\\B^{\mathsf T}&C_0\end{pmatrix},
]
with (A_0in\mathcal A), (C_0in\mathcal C), and (Bin\mathcal B).
The graph bases are the columns of
[
X=\begin{pmatrix}I\\T\end{pmatrix},qquad
Y=\begin{pmatrix}I\\-T\end{pmatrix}.
]
The annihilator condition is (X^{\mathsf T}RY=0), namely
[
A_0-BT+T^{\mathsf T}B^{\mathsf T}-T^{\mathsf T}C_0T=0.
]
The first and last terms form a symmetric matrix, while the middle two form
a skew-symmetric matrix.  They therefore vanish separately:
[
A_0=T^{\mathsf T}C_0T,qquad BT=(BT)^{\mathsf T}.
]
The (C_0) and (B) variables are independent, so the annihilator dimension
is (c(T)+b(T)).  Rank-nullity in the 18-dimensional target gives the stated
identity.

The (B)-space has the concrete block description (B_{ii}=0) and
(B_{ij}=B_{ji}) as (2\times2) blocks for (i\ne j); this is the row-symmetric
but column-mixed tensor convention inherited from (S_0(A)\otimes S_0(P\oplus Q)).

### A proved diagonal-block subfamily

There is a small pure consequence that closes one useful restricted family.
Write
[
T=\operatorname{diag}(D_0,D_1,D_2),
\qquad D_i=\operatorname{diag}(a_i,b_i),
]
with all entries nonzero.  For the (2\times2) block (X=B_{ij}), the
condition (BT=(BT)^{\mathsf T}) is
[
X D_j=D_iX^{\mathsf T}.
]
Its diagonal variables contribute respectively
([a_i=a_j]) and ([b_i=b_j]).  The two off-diagonal variables contribute one
dimension exactly when (a_i b_i=a_j b_j), and otherwise contribute zero.
Consequently
[
b(T)=\sum_{i<j}\bigl([a_i=a_j]+[b_i=b_j]+[a_i b_i=a_j b_j]\bigr).
]
Each summand is at most three.  Therefore (b(T)\ge9) forces equality for
all three pairs, hence (D_0=D_1=D_2).  This is precisely the diagonal
(2+2)-matching subfamily; it does not address a general invertible (T).

The same argument works for arbitrary invertible (2\times2) blocks, not only
diagonal ones.  If (T=\operatorname{diag}(S_0,S_1,S_2)), the three blocks
(B_{ij}) are independent and each solves
[
X S_j=S_i^{\mathsf T}X^{\mathsf T}.
]
Writing out the four equations shows that the coefficient matrix has rank at
least one, and it has rank one exactly when (S_i=S_j): if the first and last
rows both vanish this is immediate; if only one vanishes, proportionality of
the remaining rows would make one of (S_i,S_j) singular.  Thus every pair
contributes at most three dimensions, with dimension three only for equal
blocks.  Hence (b(T)\ge9) forces (S_0=S_1=S_2=S).  In that case (c(T)=3)
is equivalent to
[
S^{\mathsf T}\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}S
]
having zero diagonal.  For an invertible (2\times2) matrix this says (S) is
diagonal or anti-diagonal.  Therefore the whole block-diagonal subfamily with
cross rank at most six is already monomial and preserves the (2+2) matching.

### A pure exclusion for a general block-upper-triangular slice

Let
[
T=\begin{psmallmatrix}A&U&R\\0&B&V\\0&0&C\end{psmallmatrix},
]
with (A),(B),(C) invertible (2\times2) blocks.  Projecting the equation
(BT=(BT)^{\mathsf T}) successively to the (0,1), (0,2), and (1,2) blocks
shows that its solution space has dimension at most
[
d(A,B)+d(A,C)+d(B,C)\le9,
]
where (d(S,T)) is the kernel dimension of
(X\mapsto XT-S^{\mathsf T}X^{\mathsf T}).  The preceding 2-by-2 lemma says
that (d(S,T)=3) exactly when (S=T).  Therefore (b(T)\ge9) forces
(A=B=C=S) and all three pairwise kernels to be used with full dimension.
Write the three variable blocks of (B) as (X,Y,Z), and put
\(P=XS\), \(Q=YS\), and \(R_0=ZS\).  The saturated dimension count is
important: the first kernel projection makes (P) range over all symmetric
2-by-2 matrices, and after the second equation is imposed the pair
\((P,Q)) ranges over two independent copies of that symmetric space.  The
upper-triangular equations are
[
P=P^{\mathsf T},\qquad Q^{\mathsf T}-Q=P S^{-1}V,
]
and
[
R_0^{\mathsf T}-R_0
  =P S^{-1}R-U^{\mathsf T}S^{-\mathsf T}Q^{\mathsf T}.
]
For every symmetric (P), the middle equation is solvable only if
\(\operatorname{sym}(P S^{-1}V)=0\).  The elementary 2-by-2 matrix-unit
lemma \(\operatorname{sym}(PW)=0\) for every symmetric (P) implies
\(W=0\), so (V=0).  Then (P) and (Q) are independent symmetric
matrices, and solvability of the last equation separately gives
\(\operatorname{sym}(P S^{-1}R)=0\) for every symmetric (P) and
\(\operatorname{sym}(U^{\mathsf T}S^{-\mathsf T}Q)=0\) for every symmetric
\(Q).  The same lemma gives (R=0) and (U=0).  Thus any such upper-triangular
operator with cross rank at most six is actually (diag(S,S,S)); the previous
block-diagonal result then forces (S) to be diagonal or anti-diagonal.  The
lower-triangular statement follows by reversing the three block indices.

### Common-diagonal cycle exclusion

The remaining directed-cycle support can also be closed when the three
diagonal blocks are equal.  Right multiplication on the (P\to Q) block by a
common invertible (2\times2) matrix is an automorphism of (mathcal B), so
left multiplication of (T) by the inverse common block preserves (b(T)).
It is therefore enough to take all diagonal blocks equal to (I).

For a reciprocal pair, say (D=T_{01}) and (H=T_{10}), with both nonzero
rank-one, the off-block equations are
[
X=X^{\mathsf T},\quad Y-Y^{\mathsf T}=(ZH)^{\mathsf T},
\quad Z-Z^{\mathsf T}=D^{\mathsf T}Y^{\mathsf T}.
]
Because a nonzero rank-one (2\times2) matrix cannot be skew-symmetric, the
last two equations force (ZH=0), (D^{\mathsf T}Y^{\mathsf T}=0), and make
(Y,Z) symmetric.  Thus the off-equation kernel has dimension at most
(3+1+1=5), already below nine.

For a directed 3-cycle (D=T_{01}, E=T_{12}, K=T_{20}), the off equations are
[
X-X^{\mathsf T}=K^{\mathsf T}Z^{\mathsf T},\quad
XE=Y^{\mathsf T}-Y,\quad
Z-Z^{\mathsf T}=D^{\mathsf T}Y^{\mathsf T}.
]
The same rank-one observation forces each right-hand side to vanish.  Each of
(X,Y,Z) is then symmetric and is annihilated by a nonzero rank-one block, so
each contributes at most one dimension.  Hence the kernel has dimension at
most three.  Consequently, with a common diagonal block, every nontrivial
2-cycle or 3-cycle is excluded from cross rank at most six.

### Universal rank-one obstruction on off-diagonal blocks

The rank condition also gives information for a completely arbitrary (T),
without any triangular assumption.  Write
[
T=\begin{psmallmatrix}A&D&G\\H&B&E\\K&L&C\end{psmallmatrix}.
]
Let (\Psi_T) be the projection of the skew part of (BT) to the three
off-diagonal (2\times2) blocks.  Since (b(T)\ge9) implies
(\operatorname{rank}\Psi_T\le3), restrict (\Psi_T) to one variable block at a
time.  On the (X)-subspace its last two output components are (XE,XG), whose
rank is
[
2\operatorname{rank}[E\;G].
]
Hence (\operatorname{rank}[E\;G]\le1).  On the (Y)-subspace the first and
third components are (YL) and (-D^{\mathsf T}Y^{\mathsf T}), so
(\operatorname{rank}L\le1) and (\operatorname{rank}D\le1).  On the (Z)-subspace
the first two components are (-K^{\mathsf T}Z^{\mathsf T},
-H^{\mathsf T}Z^{\mathsf T}); their combined rank is
[
2\operatorname{rank}\begin{bmatrix}K^{\mathsf T}\\H^{\mathsf T}\end{bmatrix},
]
so the displayed vertical stack has rank at most one.  In particular, every
off-diagonal block of a high-b operator is rank at most one, with the two
blocks in the first and third statements sharing the indicated column or row
line.  This is a pure necessary condition for the missing general matching
lemma; it is not yet sufficient to force a matching.

### A pure exclusion for a single off-diagonal block

Another useful slice is
[
T=\begin{psmallmatrix}I&U&0\\0&I&0\\0&0&I\end{psmallmatrix},
\qquad U\ne0.
]
Writing (B) by its three off-diagonal blocks (X,Y,Z), the equation
(BT=(BT)^{\mathsf T}) becomes
[
X=X^{\mathsf T},\quad Y=Y^{\mathsf T},\quad XU=(XU)^{\mathsf T},
\quad Z-Z^{\mathsf T}=U^{\mathsf T}Y.
]
The last equation leaves three arbitrary symmetric parameters in (Z), once
(U^{\mathsf T}Y) is skew.  On the 3-dimensional space of symmetric (X), the
condition (XU) symmetric has kernel dimension three only when (U) is a scalar
matrix, and otherwise dimension two.  On the symmetric (Y), the condition
that (U^{\mathsf T}Y) be skew has kernel dimension zero in the scalar case and
at most one otherwise: its coefficient matrix is
[
\begin{pmatrix}a&c&0\\0&b&d\\b&a+d&c\end{pmatrix}
]
for (U=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}), and has rank at
least two for every nonzero (U).  Hence (b(T)\le3+3=6).  Since (c(T)\le3),
cross rank is at least nine.  Thus every nontrivial single-block shear is
excluded from cross rank at most six.

### Unit-upper-triangular slice

The single-block argument extends to
[
T=\begin{psmallmatrix}I&U&0\\0&I&V\\0&0&I\end{psmallmatrix}.
]
If (V\ne0), the block equations include
[
X=X^{\mathsf T},\qquad XV=Y^{\mathsf T}-Y,
\qquad Z-Z^{\mathsf T}=U^{\mathsf T}Y^{\mathsf T},
\qquad ZV=(ZV)^{\mathsf T}.
]
The second equation forces (XV) to be skew.  The coefficient matrix of
the map (X\mapsto\operatorname{sym}(XV)) on symmetric (X) has rank at least
two for every nonzero (V), so (X) contributes at most one dimension.  Once
(X) is fixed, (Y) contributes at most four dimensions (its skew part is
determined), and the last equation leaves at most three dimensions in (Z).
Thus (b(T)\le1+4+3=8).  If (V=0), the previous single-block result applies
to (U).  Hence every nontrivial unit-upper-triangular member of this slice is
excluded from cross rank at most six.

### The graph matching lemma for the whole \(3\times3\) block support

The preceding rank-one obstruction actually closes the missing support
argument.  Let \(\Psi_T\) be the off-diagonal projection map above.  If
\(b(T)\ge9\), then the full 15-equation map has rank at most three, hence
\(\operatorname{rank}\Psi_T\le3\).

The target of \(\Psi_T\) is the direct sum of the three off-diagonal block
spaces \(O_{01}\oplus O_{02}\oplus O_{12}\), each of dimension four.  A
nonzero rank-one block contributes a two-dimensional image in the following
component:

| block of \(T\) | variable and target component |
| --- | --- |
| \(D=T_{01}\) | \(Y\mapsto-D^{\mathsf T}Y^{\mathsf T}\in O_{12}\) |
| \(G=T_{02}\) | \(X\mapsto XG\in O_{12}\) |
| \(H=T_{10}\) | \(Z\mapsto-H^{\mathsf T}Z^{\mathsf T}\in O_{02}\) |
| \(E=T_{12}\) | \(X\mapsto XE\in O_{02}\) |
| \(K=T_{20}\) | \(Z\mapsto-K^{\mathsf T}Z^{\mathsf T}\in O_{01}\) |
| \(L=T_{21}\) | \(Y\mapsto YL\in O_{01}\) |

The universal rank-one obstruction already proved that every nonzero
off-diagonal block has rank one.  Therefore each of the three reciprocal
pairs \((D,H)\), \((G,K)\), and \((E,L)\) gives two independent two-dimensional
images in distinct target components, so it forces
\(\operatorname{rank}\Psi_T\ge4\).  The same is true for either directed
three-cycle: \(D\!-!E\!-!K\) contains the disjoint pair \((D,K)\), while
\(G\!-!H\!-!L\) contains \((H,L)\).  Consequently the nonzero support of
\(T\) has no directed cycle.

After a permutation of the three 2-dimensional block indices, \(T\) is
block upper triangular.  Since \(T\) is invertible, its three diagonal blocks
are invertible.  The block-upper-triangular exclusion above then forces all
three diagonal blocks to be equal and every strict-upper block to vanish.
Thus \(b(T)\ge9\) implies \(T=\operatorname{diag}(S,S,S)\).  The exact
cross-rank identity additionally requires \(c(T)=3\), which is equivalent
to \(S\) being diagonal or anti-diagonal.  In other words, every graph pair
in this \(K_{3,2}\) slice with cross rank at most six preserves a \(2+2\)
column matching.

## Exact replay

[`n6_k32_annihilator_reduction.py`](../scripts/n6_k32_annihilator_reduction.py)
constructs the 18 target basis tensors and checks the identity over (mathbb Q)
on four exact invertible examples.  The table includes (T=I_6), a matching
diagonal, a row shear, and a permutation; in each case the direct cross rank
equals (18-b(T)-c(T)).

## Boundary

The symmetric graph-pair matching statement above is a pure characteristic-zero result
for this (K_{3,2}) graph slice.  It does not by itself prove lower (29):
one still needs the separate incidence argument that excludes the resulting
matching pairs in the full Chow decomposition.  It also does not classify
arbitrary Chow summands outside this graph slice, determine exact
\(\operatorname{ChowRank}(\operatorname{perm}_6)\), or prove the general
\(2^{n-1}\) conjecture.
