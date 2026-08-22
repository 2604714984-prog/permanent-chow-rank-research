# An abstract colored-differential barrier at the b=50 endpoint

**Status.** `PURE_LINEAR_CONSTRUCTION + EXACT_MODULAR_RANK_CERTIFICATE`
(G-046).  The construction is over \(\mathbb Q\).  It proves that the common
quadratic kernels, the recorded color-subset caps, and even surjective
four-, five-, and six-color differential shadows do not by themselves
exclude the last N6-060 endpoint.  It is not an actual Chow or permanent
configuration.

## 1. Construction

Let

\[
 U=\mathbb Q^5,\qquad W=\mathbb Q^{15},\qquad
 Z=\mathbb Q^{70}\subset U\otimes W,
\]

where \(Z\) is spanned by the first seventy vectors in the row-major tensor
basis.  For each of six colors let \(C_i=\mathbb Q^{20}\).  At the 120
distinct integer nodes \(t=1,\ldots,120\), put

\[
 v_t=(1,t,t^2,\ldots,t^{69})\in Z.
\]

Define \(\beta_i:C_i\to Z\) by sending the twenty coordinate vectors of
color \(i\) to its consecutive block of twenty \(v_t\)'s.  For a nonempty
set of colors \(I\), set

\[
 S_I=\ker\left(\bigoplus_{i\in I}C_i
      \xrightarrow{\ \sum_i\beta_i\ } Z\right).
\tag{1.1}
\]

Every set of at most seventy Vandermonde columns is independent over
\(\mathbb Q\).  Hence, writing \(q=|I|\),

\[
 \boxed{\dim S_I=\max(0,20q-70).}
\tag{1.2}
\]

In particular the dimensions for \(q=1,\ldots,6\) are

\[
 0,0,0,10,30,50.
\tag{1.3}
\]

These obey the endpoint product-shadow caps

\[
 0,2,10,20,40,50.
\tag{1.4}
\]

## 2. The common kernels and colored differentials

Give each color a copy \(W_i\) of \(W\), and define

\[
 K_I=\ker\left(\bigoplus_{i\in I}W_i
             \xrightarrow{\ \sum_i\ }W\right),
 \qquad \dim K_I=15(q-1).
\tag{2.1}
\]

For \(a=0,\ldots,4\), contract \(U\otimes W\) with the \(a\)-th coordinate
covector on \(U\).  Applied separately in every color, this defines

\[
 D_a:\bigoplus_{i\in I}C_i\longrightarrow
       \bigoplus_{i\in I}W_i.
\tag{2.2}
\]

If \(c\in S_I\), then \(\sum_i\beta_i(c_i)=0\).  Contracting this equality
shows \(D_a(c)\in K_I\).  Thus the abstract colored shadow

\[
 \partial_cS_I=\sum_{a=0}^4D_a(S_I)
\tag{2.3}
\]

is contained in \(K_I\).

Exact elimination gives

\[
\begin{array}{c|rrrrrr}
q&1&2&3&4&5&6\\ \hline
\dim S_I&0&0&0&10&30&50\\
\dim\partial_cS_I&0&0&0&45&60&75\\
\dim K_I&0&15&30&45&60&75.
\end{array}
\tag{2.4}
\]

The displayed values hold for every subset \(I\) of the indicated size.
In particular, every five-color shadow is all of its sixty-dimensional
kernel, not merely a subspace of codimension at most three.

## 3. Why the certificate is characteristic zero

The script checks all 63 nonempty color subsets modulo
\(p=1{,}000{,}003\).  This is an exact certificate for the stated rational
ranks, not a random finite-field diagnostic:

1. the kernel dimensions over \(\mathbb Q\) follow directly from nonzero
   Vandermonde minors at distinct integer nodes;
2. the Vandermonde pivot minor is nonzero modulo \(p\), so the
   reduced-echelon kernel basis lifts over \(\mathbb Z_{(p)}\); the computed
   colored-shadow matrix is its reduction and its rational rank is at least
   its modular rank;
3. equation (2.3) gives the rational upper bound
   \(\dim\partial_cS_I\leq\dim K_I\).

For \(q=4,5,6\), the modular ranks are respectively \(45,60,75\), exactly
the dimensions of \(K_I\).  The matching lower and upper bounds therefore
prove equality over \(\mathbb Q\).

## 4. Strict conclusion and boundary

The model simultaneously has:

- \(\dim S=50\);
- every endpoint color-subset cap;
- the common kernels \(K_I\);
- full five-color shadows of dimension sixty; and
- a full six-color shadow of dimension seventy-five.

Consequently no contradiction can follow from only these abstract data.
Any successful colored argument must use an additional actual-Chow input,
such as the squarefree cubic coproduct, factor-frame integrability, or the
common-section cocycle constraints.

This construction does **not** consist of sextic Chow terms, does not embed
the spaces as the derivative tower of \(\operatorname{perm}_6\), and is not
a 27-term decomposition or a realization of the \(b=50\) endpoint.  It
therefore neither proves nor refutes `ChowRank(perm_6)>=28`, the exact Chow
rank, or any border-rank statement.

```text
python scripts/n6_colored_differential_barrier.py \
  --json data/n6_colored_differential_barrier.json
python -m unittest tests.test_n6_colored_differential_barrier -v
```
