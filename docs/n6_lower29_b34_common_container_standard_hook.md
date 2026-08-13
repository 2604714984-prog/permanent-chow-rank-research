# The common quadratic container and one excluded standard-hook branch

**Status.** PURE_COMMON_A2_CONTAINER_REDUCTION,
PURE_A72_KAPPA3_STANDARD_HOOK_EXCLUSION,
EXACT_FINITE_GRAPH_AND_SHADOW_REPLAY (N6-103). The base field is
algebraically closed of characteristic zero.

This note continues N6-100--N6-102. It proves a common-container statement
for at least nineteen residual terms and excludes one of the two N6-101
geometries at

\[
 (a_2,\kappa_2,t_2)=(72,3,15).
\tag{0.1}
\]

The biflag rectangle hook at (0.1) remains open.

## 1. At least nineteen terms lie in one quadratic container

Fix the all-zero critical six-set \(C\) supplied by N6-102. Write \(U_i\)
for its twenty-dimensional literal cubic images, \(F_i=\partial U_i\), and

\[
 L_C=\bigoplus_{i\in C}U_i,\qquad
 X_C=E_3\cap L_C,\qquad \dim X_C=46.
\tag{1.1}
\]

N6-102 gives at least nineteen residual indices with

\[
 \varepsilon_j=0,\qquad \dim F_j=\dim q(F_j)=15.
\tag{1.2}
\]

For any such \(j\notin C\), the seven-set \(C\cup\{j\}\) is one of the
hereditary equality sets of N6-100. Hence

\[
 \dim\bigl(E_3\cap(L_C\oplus U_j)\bigr)=66.
\tag{1.3}
\]

The kernel of the projection of (1.3) to
\((L_C\oplus U_j)/L_C\simeq U_j\) is \(X_C\), of dimension \(46\).
The image therefore has dimension \(20\), so it is all of \(U_j\). Thus

\[
 U_j\subset E_3+L_C.
\tag{1.4}
\]

Differentiate (1.4). Since \(\partial E_3\subset E_2\), one obtains

\[
 F_j\subset A_2:=E_2+\sum_{i\in C}F_i.
\tag{1.5}
\]

If \(Q_C=q(\sum_{i\in C}F_i)\) and \(t_2=\dim Q_C\), then

\[
 \dim A_2=225+t_2\le243,\qquad q(F_j)\subset Q_C
\tag{1.6}
\]

for at least nineteen actual Chow terms. This is stronger than a statement
about the selected six alone.

There is also an exact directness consequence. The selected critical sum
has dimension \(90-3=87\). For an external zero-defect term \(j\), the
seven-set \(C\cup\{j\}\) has total quadratic relation kernel at most three
by the hereditary N6-080 envelope. Since it already contains the critical
three-dimensional relation kernel, equality is forced:

\[
 \dim\left(\sum_{i\in C}F_i+F_j\right)=105-3=102=87+15.
\tag{1.7}
\]

Thus \(F_j\cap\sum_{i\in C}F_i=0\). In particular \(F_j\cap F_i=0\) for
every \(i\in C\). The common-\(W_{15}\) section difference between \(F_j\)
and \(F_i\) is therefore a fifteen-plane in \(E_2\). Its universal product
shadow has dimension at least twelve and is contained in \(L_j+L_i\), so

\[
 L_j\cap L_i=0,\qquad \partial D_{ij}=L_j\oplus L_i.
\tag{1.8}
\]

There are at least thirteen such external indices \(j\).

Finally, \(A_2=E_2+F_j\) for every one of the nineteen zero-defect terms,
because both quotients are the same (W_{15}). Its first prolongation
contains (E_3+L_C), of dimension

\[
 400+120-46=474.
\tag{1.9}
\]

The existing actual-term (t_2=15) caps give at most (458) whenever
(\alpha_j\le2). Hence

\[
 \boxed{(\varepsilon_j,\alpha_j)=(0,3)}
\tag{1.10}
\]

for all at least nineteen terms.

## 2. The relation graph and the factor-span hook

Now assume \(a_2=72\). N6-102 gives

\[
 t_2=18-\kappa_2,\qquad 0\le\kappa_2\le3.
\tag{2.1}
\]

On the six vertices \(C\), join \(i\) and \(j\) when
\(F_i\cap F_j\ne0\). If a forest in this graph has \(e\) edges, choose a
nonzero vector in every corresponding pair intersection. The resulting
\(e\) relations in \(\bigoplus_iF_i\) are independent by leaf elimination.
Consequently every spanning forest has at most \(\kappa_2\) edges. The
intersection graph has at least \(6-\kappa_2\) connected components, and
its complement is connected.

For a complementary edge \(ij\), one has \(F_i\cap F_j=0\). Put
\(Q_i=q(F_i)\). Since each \(Q_i\) has dimension fifteen in the
\(t_2\)-plane \(Q_C\),

\[
 \dim(Q_i\cap Q_j)\ge30-t_2=12+\kappa_2.
\tag{2.2}
\]

The difference of the two quotient sections over \(Q_i\cap Q_j\) is an
injective actual section-difference space \(D_{ij}\subset E_2\). For
\(\kappa_2\ge1\), (2.2) gives \(\dim D_{ij}\ge13\). The universal product
shadow of a thirteen-plane in \(E_2\) has dimension at least twelve, while

\[
 \partial D_{ij}\subset L_i+L_j,\qquad \dim(L_i+L_j)\le12.
\tag{2.3}
\]

Thus equality holds in (2.3): \(L_i\cap L_j=0\) and
\(\partial D_{ij}=L_i\oplus L_j\). N6-101 gives
\(M:=\partial K\) of dimension twenty-three, where

\[
 K=E_2\cap\sum_{i\in C}F_i.
\]

Every complementary edge puts both endpoint planes inside \(M\). Since
the complementary graph is connected, all six \(L_i\) lie in \(M\). The
reverse containment follows from \(K\subset\sum_iF_i\). Hence

\[
 \boxed{M=\sum_{i\in C}L_i}\qquad(\kappa_2=1,2,3).
\tag{2.4}
\]

The exact replay enumerates all \(2^{15}\) simple graphs and confirms the
finite graph implication. The proof above is the characteristic-zero
argument.

## 3. A separated bound with quadratic relations

We need a slight strengthening of N6-059. Suppose six actual terms are
separated by the same columns, their cubic spaces are literal direct, their
quadratic spaces have the common quotient \(W_{15}\), and

\[
 \dim\sum_iF_i=90-\kappa.
\tag{3.1}
\]

For a column pair \(J\), let \(r_J\) be the dimension of its quadratic
block and put \(\delta_J=6-r_J\). Multidegrees are direct, so

\[
 \sum_J\delta_J=\kappa.
\tag{3.2}
\]

The common quotient contributes one nonzero line in every pair block.
Therefore

\[
 \dim(E_{2,J}\cap H_{2,J})=r_J-1=5-\delta_J.
\tag{3.3}
\]

For a column triple \(T\), the one-factor squarefree shadow sequence for a
subspace of dimensions zero through six is

\[
 (0,3,5,6,6,8,9).
\tag{3.4}
\]

Applying (3.3)--(3.4) to each of the three pairs in \(T\), then summing the
twenty disjoint cubic multidegrees, gives the exact maxima

\[
\begin{array}{c|cccc}
\kappa&0&1&2&3\\ \hline
\dim(E_3\cap\sum_iU_i)&\le40&\le36&\le36&\le33.
\end{array}
\tag{3.5}
\]

The script enumerates the distributions of at most three deficits among
the fifteen pairs. Equation (3.5) also has a direct finite proof: every
defective pair lowers all four incident triple bounds, with further losses
when a deficit exceeds one.

## 4. Excluding the standard hook at \(\kappa_2=3\)

Take the state (0.1). Here \(t_2=15\), so all six quotient planes equal
one \(W_{15}\), while (2.4) identifies the sum of the factor planes with
the N6-101 second shadow \(M\).

Suppose some row block or column block of one \(X_i:k^6\to R\otimes C\)
is invertible. The connected complementary graph supplies a transverse
partner \(j\) with \(F_i\cap F_j=0\). N6-069 makes that pair commonly
column-separated or row-separated. Its common-quotient propagation
argument uses only \(q(F_k)=W_{15}\), so all six terms have the same
separation. Equation (3.5) then gives

\[
 46=\dim X_C\le33,
\]

a contradiction. Hence all row and column blocks of all six terms are
singular.

In fact the same conclusion holds for all at least nineteen zero-defect
terms. If an external term has an invertible block, pair it with any
critical term using (1.8). If a critical term has an invertible block, pair
it with any external term. N6-069 supplies common separation of the pair,
and the common-\(W_{15}\) propagation makes all zero-defect terms separated.
Applying (3.5) to the original critical six again contradicts
\(\dim X_C=46\). Hence every row and column block of every one of these
nineteen terms is singular.

Assume now that \(M\) is the standard flag hook

\[
 R_4\otimes C_5+R_3\otimes C,\qquad R_3\subset R_4,
\tag{4.1}
\]

or its transpose. The proof in Sections 2--6 of N6-072 uses precisely:

1. injectivity of the six factor matrices;
2. the common quotient \(W_{15}\), which synchronizes same-row and
   distinct-row quotient-block images;
3. the identity \(M=\sum_iL_i\);
4. the standard hook contractions (4.1); and
5. singularity of every row and column block.

Quadratic literal directness is not used in that block argument. With
(2.4), all five inputs hold here. More explicitly, the common quotient
synchronizes the six same-row compression ranks and images. A full hook row
cannot use the common full-rank alternative, so its six blocks are
coordinate-domain rank-one blocks whose images form a basis. Comparing two
full rows through the true diagonal-plus-wedge quotient makes the label
partition independent of the color. Injectivity forces the number of label
classes to equal the number of full rows and the long-column contractions
bound that number by four. The four-full-row case contradicts the rank-four
long columns; the three-full-row case contradicts the required one nonfull
contribution on each long column. None of these steps invokes a relation
among the six \(F_i\). This excludes the standard hook and its transpose in
(0.1).

## 5. Exact boundary

Proved: at least nineteen zero-defect actual terms lie in the common
container (1.5); every external zero-defect quadratic space is direct from
the critical quadratic sum; all nineteen terms have \(\alpha=3\); and all
nineteen have only singular row and column blocks. For the three
\(a_2=72,\ \kappa_2\ge1\) states, the six
factor planes span the N6-101 second shadow. At
\((a_2,\kappa_2,t_2)=(72,3,15)\), the standard flag-hook geometry and its
transpose are impossible.

Still open:

- the biflag rectangle hook at (0.1);
- both N6-101 geometries for the other three \(a_2=72\) scalar states;
- all \(a_2=73,74,75\) states;
- ordinary lower 29 and border rank.

Replay:

    python scripts/n6_lower29_b34_common_container_standard_hook.py \
      --verify-json data/n6_lower29_b34_common_container_standard_hook.json
    python -m unittest \
      tests.test_n6_lower29_b34_common_container_standard_hook -v
