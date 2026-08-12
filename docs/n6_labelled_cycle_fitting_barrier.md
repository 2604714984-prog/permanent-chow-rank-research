# Aggregate factor-labelled cycle presentations saturate in five terms

**Status.** `EXACT_CHARACTERISTIC_ZERO_ROUTE_COUNTEREXAMPLE` (G-037).
This note does not prove a new lower bound for the permanent.  It closes one
specific continuation of G-035.  The ordinary interval remains

\[
26\leq \operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## 1. The presentation-valued interface

Let `V` have dimension six and let

\[
d_{a,p}:\operatorname{Sym}^aV\otimes\Lambda^pV
 \longrightarrow
 \operatorname{Sym}^{a-1}V\otimes\Lambda^{p+1}V
\tag{1.1}
\]

be the standard Koszul differential.  For a factored sextic

\[
T=\ell_1\ell_2\cdots\ell_6
\]

put

\[
B(T)=d_{4,2}\bigl(\mathcal D_4(T)\otimes\Lambda^2V\bigr)
 \subseteq \ker d_{3,3}.
\tag{1.2}
\]

For each labelled three-subset `S` define the G-035 cycle

\[
z_S(T)=
 \left(\prod_{i\in S}\ell_i\right)
 \otimes
 \left(\bigwedge_{i\in S}\ell_i\right).
\tag{1.3}
\]

The Leibniz rule gives `d_(3,3) z_S(T)=0`.  Write `Z^ell(T)` for the
span of these twenty cycles.  Given an ordered tuple
`T_bold=(T_1,...,T_r)`, there is therefore a natural specialized
presentation

\[
\overline\Phi_{\mathbf T}:\bigoplus_{i=1}^r\mathbf k^{20}
 \longrightarrow
 \frac{\ker d_{3,3}}{\sum_i B(T_i)},
\qquad e_{i,S}\longmapsto[z_S(T_i)].
\tag{1.4}
\]

Its rank is

\[
\lambda(\mathbf T)=
 \dim\frac{\sum_i B(T_i)+\sum_iZ^\ell(T_i)}{\sum_iB(T_i)}.
\tag{1.5}
\]

At a fixed tuple, the determinantal or Fitting data of (1.4) are controlled
by this rank: a minor of size `lambda` is nonzero and every minor of size
`lambda+1` vanishes.  This is the most direct uncolored aggregate-boundary
realization of the candidate interface left open by G-035.

## 2. Exact two-term failure of additivity

Take `T_0=x_0x_1...x_5`.  A matrix below is written with its six factor
vectors as columns.

First let

\[
A_{\rm pair}=\begin{pmatrix}
1&1&1&1&1&1\\
0&1&1&1&1&1\\
0&0&1&1&1&1\\
0&0&0&1&1&1\\
0&0&0&0&1&1\\
0&0&0&0&0&1
\end{pmatrix}.
\tag{2.1}
\]

Both factor sets are bases of `V`.  Exact rational elimination gives

\[
\begin{array}{c|c}
\text{quantity}&\text{dimension}\\ \hline
B(T_0),B(T_1)&190,190\\
B(T_0)+B(T_1)&380\\
Z^\ell(T_0),Z^\ell(T_1)&20,20\\
Z^\ell(T_0)+Z^\ell(T_1)&40\\
\text{two individual images modulo the aggregate boundary}&19,17\\
\text{intersection of those quotient images}&3\\
\lambda(T_0,T_1)&33.
\end{array}
\tag{2.2}
\]

Thus the boundary spaces and the labelled-cycle spaces are separately
transverse, but the quotient presentation has a seven-dimensional kernel.
The loss is genuinely caused by cross-boundary and quotient coupling.

For comparison, take the cyclic-neighbour factor matrix

\[
(A_{\rm cyc})_{ij}=1_{i=j}+1_{i=j+1\pmod6}.
\tag{2.3}
\]

It has rank five, every factor triple is independent, and exact derivative
reconstruction gives `(dim D_3,dim D_4)=(20,15)`.  For this pair the
corresponding values are

\[
\dim(B_0+B_2)=380,\qquad
(\lambda_0,\lambda_2)=(20,10),\qquad
\dim(\overline Z_0\cap\overline Z_2)=2,
\qquad \lambda(T_0,T_2)=28.
\tag{2.4}
\]

Here `lambda_i` denotes the dimension of the image of the `i`-th labelled
cycle space modulo the aggregate boundary `B_0+B_2`; it is not the joint
rank `lambda(T_0,T_2)`.

This second row is not needed for the main obstruction, but it checks that
the dependence strata already visible in G-035 worsen the collision.

## 3. Five full-span terms kill the whole presentation

The homogeneous Koszul strand on six variables is exact.  In particular,

\[
\dim\ker\left(
d_{3,3}:\operatorname{Sym}^3V\otimes\Lambda^3V
 \longrightarrow \operatorname{Sym}^2V\otimes\Lambda^4V
\right)=840.
\tag{3.1}
\]

Indeed the domain has dimension `56*20=1120`; exactness of the strand gives
`rank d_(3,3)=280`.  The replay also reconstructs this rank over `Q`.

Now use the identity factor matrix and the following four integer matrices:

\[
\begin{split}
A_1={}&\begin{pmatrix}
2&1&1&-1&-2&1\\-2&-1&-1&-1&1&0\\1&2&2&1&1&1\\
-1&0&-2&-1&1&1\\-2&1&-2&1&-2&1\\1&2&-1&1&1&-1
\end{pmatrix},\\
A_2={}&\begin{pmatrix}
-2&0&1&-2&-1&-2\\-2&-2&0&2&-2&-2\\-2&1&0&0&-1&0\\
-1&-2&-1&-2&-2&0\\0&0&0&-2&-1&1\\-1&0&0&1&-1&2
\end{pmatrix},\\
A_3={}&\begin{pmatrix}
1&2&1&-1&-1&1\\1&-1&-1&1&1&2\\0&1&1&0&2&1\\
-1&2&-2&2&0&1\\-1&0&0&-1&2&-1\\-1&1&-2&0&-1&-1
\end{pmatrix},\\
A_4={}&\begin{pmatrix}
-1&0&2&0&2&0\\0&2&0&1&-2&2\\0&-2&-1&1&-1&0\\
2&-2&0&-2&1&-1\\2&1&-2&2&-2&-1\\2&-2&2&1&1&0
\end{pmatrix}.
\end{split}
\tag{3.2}
\]

Their determinants, including the identity first, are

\[
1,\ 184,\ -68,\ 9,\ -15.
\tag{3.3}
\]

Hence all five terms have six independent factors and central catalectic rank
twenty.  Deterministic sparse elimination modulo `p=1000003` gives the ranks
of the successive boundary sums

\[
190,\ 380,\ 570,\ 760,\ 840.
\tag{3.4}
\]

The last number equals the characteristic-independent upper bound (3.1).
Thus (3.4) proves over every characteristic-zero field that

\[
\sum_{i=0}^4B(T_i)=\ker d_{3,3}.
\tag{3.5}
\]

For an explicit modular minor certificate, the elimination selects 840
boundary columns and 840 pivot rows.  With the deterministic lexicographic
pivot order used by the script, the product of the diagonal entries of the
triangularized minor is

\[
859612\not\equiv0\pmod{1000003}.
\tag{3.6}
\]

Every one of the one hundred factor-labelled vectors is a cycle, so (3.5)
implies

\[
\boxed{\lambda(T_0,T_1,T_2,T_3,T_4)=0.}
\tag{3.7}
\]

Consequently every positive minor of the specialized map (1.4) vanishes at
this five-term tuple.  In particular, neither `20` per full-middle-rank term
nor any positive hereditary lower contribution can hold for (1.4).

## 4. What is and is not closed

The following route is now blocked:

> retain the twenty factor-labelled cycles, quotient by the sum of all term
> boundary spaces, and use the resulting ordinary determinantal/Fitting rank
> to count the at least twelve full-middle-rank residual summands.

It already vanishes on five explicit full-span terms.  Adding more terms only
enlarges the aggregate boundary, so the same fixed cycles remain zero.

This does **not** rule out a presentation that retains the term colors before
passing to a quotient, nor one that uses the common differential-operator
domain of the actual equation `Q=P-H`.  Such a successor must prevent the
cross-term boundary saturation in (3.5); otherwise it reduces to the blocked
interface above.

Evidence classification:

- pure mathematics: definitions (1.1)--(1.5), the cycle identity, Koszul
  exactness, and the implication from (3.4) to (3.7);
- exact rational computation: every number in the two-term tables and the
  derivative-space reconstruction in the rank-five example;
- strict modular certificate: the 840-rank minor in (3.4)--(3.6), which is a
  characteristic-zero lower-rank certificate matched by the pure upper bound;
- random evidence: none; the displayed matrices are frozen exact witnesses;
- unresolved: a genuinely colored or equation-coupled invariant capable of
  proving lower 27 for `perm_6`.

## 5. Replay

```text
python scripts/n6_labelled_cycle_fitting_barrier.py \
  --json data/n6_labelled_cycle_fitting_barrier.json
python -m unittest tests.test_n6_labelled_cycle_fitting_barrier -v
```

Expected marker:

```text
G037_LABELLED_CYCLE_FITTING_BARRIER_PASS
```
