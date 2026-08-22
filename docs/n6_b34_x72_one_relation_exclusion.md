# N6-094: excluding the \(x_A=72\) one-relation packet

**Status.** PURE_ACTUAL_B34_X72_ONE_RELATION_EXCLUSION;
EXACT_KERNEL_LINE_GRAPH_REPLAY.

Assume the second packet in N6-093 exists. Seven actual full-frame quadratic
spaces \(F_i\) have one common quotient \(W_{15}\), and

\[
 \dim\sum_iF_i=104,\qquad
 K=E_2\cap\sum_iF_i,\qquad \dim K=89.                         \tag{1.1}
\]

N6-092 places \(K\) as a hyperplane in a partitioned product
\(K_{90}\), with

\[
 M=\partial K=R_4\otimes C,\qquad\dim M=24.                  \tag{1.2}
\]

## 1. The pair graph loses at most one edge

Choose sections \(s_i:W\to F_i\). The six anchored difference maps combine
to

\[
 \Delta:W^{\oplus6}\longrightarrow K.                        \tag{1.3}
\]

Its domain has dimension 90 and its image has dimension 89, so
\(\ker\Delta\) is a line. For a pair \(i,j\), the section-difference plane
\[
 D_{ij}=\{s_i(w)-s_j(w):w\in W\}
\]
fails to have dimension fifteen only if \(\ker\Delta\) lies in the
corresponding pair-color subspace. Distinct pair-color subspaces intersect
trivially. Hence at most one of the 21 pairs is bad.

For every good pair,

\[
 12\le\dim\partial D_{ij}\le\dim(L_i+L_j)\le12.              \tag{1.4}
\]

Thus \(L_i\cap L_j=0\), and
\[
 L_i+L_j=\partial D_{ij}\subset M.                            \tag{1.5}
\]

The good-edge graph is \(K_7\) with at most one edge removed. Every vertex
has good degree at least five, so all seven \(L_i\) lie in \(M\). Since the
differences span \(K\),
\[
 \sum_iL_i=M.                                                 \tag{1.6}
\]

## 2. The invertible-block branch

Suppose some active row block is invertible. It belongs to a good pair, so
the pure N6-069 block theorem makes that pair commonly column-separated.
The N6-061 common-quotient domain argument then propagates the same column
separation to all seven frames.

For every good edge, N6-070 gives
\[
 L_i+L_j=P_{ij}\otimes C,\qquad\dim P_{ij}=2.                \tag{2.1}
\]

Let \(R_i\) be the span of the six row factors of frame \(i\). Then
\(\dim R_i\le2\). If some \(\dim R_i=2\), every good neighbor has row factors
in \(R_i\). Among five such neighbors, either one already has row span
\(R_i\), or two one-dimensional row spans are distinct because their good
edge has twelve-dimensional sum. Hence those neighbors span \(R_i\). The
possible unique bad neighbor has row span either contained in \(R_i\) or in
at most one extra line. Consequently all seven frames would lie in a row
space of dimension at most three, contradicting (1.6). Therefore every
\(R_i\) is a line.

After column rescaling,
\[
 F_i=p_i^2\otimes S_0(C).                                    \tag{2.2}
\]

It follows that
\[
 \dim\sum_iF_i=15\dim\langle p_i^2\rangle                   \tag{2.3}
\]

is a multiple of fifteen. This contradicts the value 104 in (1.1).

## 3. The all-singular branch

Assume every active row block is singular. N6-071 same-row synchronization
uses only the common quotient and the same-row zero part of \(E_2\), so it
applies unchanged. If one block in an active row had rank at least two, all
seven block images in that row would be one common subspace. Equation (1.6)
then forces that subspace to be all of \(C\), of rank six, contradicting
singularity.

Every active row block therefore has rank at most one. The factor planes lie
in the four-row product space \(M\), so every factor matrix has rank at most
four, contrary to the required rank six.

Both branches are impossible. The one-relation common-\(W_{15}\) packet is
excluded. The \(x_A=72\) frontier still contains the direct \(t_2=16\)
packet and the one-defective-term \(t_2=15\) packet. This theorem does not
exclude those packets, global \(b=34\), ordinary lower \(29\), or any
border-rank configuration.
