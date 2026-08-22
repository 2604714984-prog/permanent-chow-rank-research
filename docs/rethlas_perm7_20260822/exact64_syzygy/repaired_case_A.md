# Repaired endpoint-A exclusion with quadratic restriction defects

This note replaces the false use of local quadratic surjectivity in the
old endpoint-A argument.  It is conditional only on the already derived
49-term slope equality and case-A packet classification.

Throughout,

\[
B=k[e_1,\ldots,e_7]/(e_1^2,\ldots,e_7^2)
\]

is the local apolar algebra of a rank-seven Chow term.

## Lemma 1 (Boolean propagation of a three-dimensional defect)

If \(Q\subset B_2\) has codimension at most three, then

\[
 \dim B_1Q\ge 34,\qquad B_1^2Q=B_4.
\]

Moreover, if \(W\subset B_3\) and \(\dim B_1W\le7\), then
\(\dim W\le2\).

### Proof

Choose a generic diagonal one-parameter subgroup on the seven variables.
The initial subspace of \(Q\) is spanned by \(21-c\) squarefree quadratic
monomials, where \(c\le3\).  Since

\[
 \operatorname{in}(B_1Q)\supseteq B_1\operatorname{in}(Q),
\]

the degree-three quotient is bounded by the number of triples all three of
whose two-subsets lie among the \(c\) omitted pairs.  At most one such
triple exists.  A surviving four-subset would require all six of its pairs
to be omitted, impossible for \(c\le3\).  This proves the first two
claims.

Apply the same degeneration to \(W\).  Its coordinate initial family
consists of \(\dim W\) triples, and its upper four-shadow is contained in
the initial space of \(B_1W\).  One triple has four upper neighbors, two
distinct triples have at least seven, and three distinct triples have at
least nine.  Hence an upper-shadow bound seven forces \(\dim W\le2\).

## Proposition 2 (case A is impossible despite local defects)

Assume a hypothetical 49-term identity has the slope-equality case-A
packet: every term has seven independent factors and the factor planes
form a simple rank-seven \(7\)-multilinear matroid.  Then the identity is
impossible.

### Proof

Choose a matroid basis of seven term planes.  Let \(R_d\) be the labelled
permanent relation module, so quadratic generation gives
\(R_3=C_1R_2\), \(R_4=C_1^2R_2\), and slope equality gives

\[
 \dim R_3+\dim R_4=490. \tag{1}
\]

For a basis term \(i\), let \(Q_i\subset (A_i)_2\) be the restriction
image of the permanent quadrics.  Correct apolar duality identifies its
cokernel dual with \(D_2(T_i)\cap E_2\), so the audited small-intersection
lemma gives \(\operatorname{codim}Q_i\le3\).  Put

\[
 U_i=(A_i)_1Q_i\subset(A_i)_3.
\]

Lemma 1 gives \(\dim U_i\ge34\) and
\((A_i)_1^2Q_i=(A_i)_4\).

Because the seven basis planes sum directly to the ambient 49-space,
degree-one labelled codewords can be supported on any one basis block.
Multiplying lifts of \(Q_i\) by such codewords shows that the basis
projection of \(R_3\) contains

\[
 U:=\bigoplus_{i=1}^7U_i,\qquad \dim U\ge238,
\]

and that the basis projection of \(R_4\) is onto the full
\(7\cdot35=245\)-dimensional quartic block.  If \(K_4\) is the kernel of
the latter projection, then (1) gives

\[
 \dim K_4=\dim R_4-245=245-\dim R_3\le7. \tag{2}
\]

Choose a linear section \(S=\bigoplus_iS_i\subset R_3\) of \(U\), with
\(S_i\) mapping isomorphically to \(U_i\) in basis block \(i\).  Since
\(\dim R_3\le245\), choose a complement \(H\) with

\[
 R_3=S\oplus H,qquad \dim H=\dim R_3-\dim U\le7. \tag{3}
\]

Fix a nonbasis term \(t\).  Its fundamental circuit contains at least two
basis indices.  Relative to the direct basis decomposition, every block
restriction \(P_{tj}:(A_j)_1\to(A_t)_1\) is either zero or invertible, and
it is invertible precisely on the circuit.

For each \(i\), choose a circuit index \(j\ne i\).  Let
\(W_i\subset(A_t)_3\) be the projection of \(S_i\) to term \(t\).
Multiplying \(S_i\) by a linear codeword supported on basis block \(j\)
has zero component on every basis block, hence belongs to \(K_4\).  At
term \(t\) its component runs through \((A_t)_1W_i\), because \(P_{tj}\)
is invertible.  Therefore (2) and Lemma 1 imply

\[
 \dim (A_t)_1W_i\le7,qquad \dim W_i\le2. \tag{4}
\]

Equations (3)--(4) bound the entire cubic projection at \(t\):

\[
 \dim\operatorname{pr}_t(R_3)
 \le\sum_{i=1}^7\dim W_i+\dim H
 \le14+7=21. \tag{5}
\]

On the other hand, the local quadratic restriction image
\(Q_t\subset(A_t)_2\) also has codimension at most three.  Since
\(R_3=C_1R_2\) and \(C_1\to(A_t)_1\) is onto, Lemma 1 gives

\[
 (A_t)_1Q_t\subseteq\operatorname{pr}_t(R_3),
 \qquad \dim\operatorname{pr}_t(R_3)\ge34, \tag{6}
\]

contradicting (5).  There are 49 terms but a matroid basis has only seven,
so a nonbasis term \(t\) exists.  Thus case A is empty.

## Scope

The proposition does not repair endpoint case B and therefore does not by
itself prove the lower bound 50.  The plus/minus pair
\(\prod_c(x_{1c}+x_{2c})\), \(\prod_c(x_{1c}-x_{2c})\) shows why case B
cannot be repaired by any bound using only individual local defects: both
individual defects vanish while the joint defect contains the full
21-dimensional two-row permanent block.
