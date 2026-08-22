# Fork-diagram audit for a selected \(\beta_{2,3}\) invariant

## Status

`EXACT NO-GO FOR ADDITIVE HOMOLOGY-FORK SELECTORS AND MAPPING-CONE RANKS.`

No rank-64 invariant was obtained.  The audit closes the unadorned
homology-level fork

\[
 \mathsf B(A_f)\ \xleftarrow{\ a\ }\ \mathsf B(R)
 \ \xrightarrow{\ b\ }\ \bigoplus_i\mathsf B(A_{T_i}),
 \qquad \mathsf B(-)=\operatorname{Tor}_2^S(-,K)_3,
 \tag{0.1}
\]

as a source of an additive selected subquotient.  It also closes the ordinary
mapping cone/homotopy pushout and the most promising coupled image
\(\mathsf B(A_f)/a(\ker b)\).

The decisive new calculation is specific to the legal 64-term Glynn
decomposition.  A \(9310\)-dimensional all-distinct-column block of
\(\mathsf B(R_G)\) dies in every term algebra.  Consequently the coupled
target survivor has dimension at most

\[
 18816-9310=9506,
\]

far below the required \(18523\).  By contrast, the homotopy pushout has
dimension at least \(19600\), already \(784\) above the 64-atom budget.

This is a no-go theorem only for constructions determined by the bare fork of
Tor vector spaces (and derived mapping-cone constructions made from it).  A
construction using multiplication, the Frobenius trace, or another
\(GL(V)\)-natural structure not visible in (0.1) is not ruled out.

## 1. The six exact fork coordinates

Let

\[
 D=(Y\xleftarrow{a}X\xrightarrow{b}Z)
\]

be a finite-dimensional fork over a field.  Put

\[
 x=\dim X,\quad y=\dim Y,\quad z=\dim Z,
 \quad r_a=\operatorname{rank}a,\quad r_b=\operatorname{rank}b,
 \quad r=\operatorname{rank}(a,b).
\]

Define

\[
\begin{array}{lll}
 p=r_a+r_b-r,&u=r-r_b,&v=r-r_a,\\
 s=x-r,&t=y-r_a,&w=z-r_b.
\end{array}
\tag{1.1}
\]

All six integers are nonnegative.  The fork is isomorphic to the direct sum
of

\[
 pI_{XYZ}\oplus uI_{YX}\oplus vI_{XZ}\oplus sI_X
 \oplus tI_Y\oplus wI_Z,
\tag{1.2}
\]

where each \(I\) is one-dimensional at the displayed vertices, zero at the
other vertices, and has identity nonzero arrows.

Here is a direct proof, so no classification theorem is needed as a black
box.  Let \(K_a=\ker a\), \(K_b=\ker b\), and \(K=K_a\cap K_b\).
Split \(K\) off from \(X\), then split complements of \(K\) in \(K_a\) and
\(K_b\), and finally split a complement of \(K_a+K_b\).  On the last
complement both arrows are injective.  Split the corresponding images in
\(Y\) and \(Z\), and then split the two cokernels.  The dimensions are
exactly (1.1).  This also proves uniqueness because (1.1) recovers every
multiplicity from isomorphism-invariant ranks.

For literature grounding, the complete general statement is: for any fixed
orientation \(\tau\) of the path \(A_n\) over a field, the indecomposable
finite-dimensional \(\tau\)-modules are precisely the interval modules
\(I_\tau(b,d)\), \(1\le b\le d\le n\); equivalently every \(\tau\)-module is
a direct sum of interval modules, uniquely up to order by Krull--Schmidt.
This is Carlsson--de Silva, *Zigzag Persistence*,
`paper_id=CarlssonDeSilva_ZigzagPersistence`, arXiv:0812.0197, Theorem 2.5
(Gabriel); their constructive proof is Theorem 4.1.  Their definitions of a
zigzag module and interval module specialize to (1.2) for the orientation
\(Y\leftarrow X\to Z\).  The downloaded source, including the proof, is
`downloads/zigzag_0812.0197_source/zigzagARXIV.tex`.

## 2. Persistent images and the pushout

Let

\[
 H=(Y\oplus Z)/\{(a(x),-b(x)):x\in X\}.
\tag{2.1}
\]

Then the following dimensions are exact:

\[
\begin{aligned}
 \dim H&=p+t+w,\\
 \dim\operatorname{im}(Y\to H)&=p+t,\\
 \dim\operatorname{im}(Z\to H)&=p+w,\\
 \dim\bigl(\operatorname{im}Y\cap\operatorname{im}Z\bigr)&=p.
\end{aligned}
\tag{2.2}
\]

Indeed, the kernel of \(Y\to H\) is \(a(\ker b)\), of dimension \(u\),
and similarly the kernel of \(Z\to H\) is \(b(\ker a)\), of dimension
\(v\).  Thus the most generous target subquotient produced by the pushout is

\[
 Q(D)=Y/a(\ker b),\qquad
 \dim Q(D)=y+\operatorname{rank}b-\operatorname{rank}(a,b)=p+t.
\tag{2.3}
\]

This formula is invariant under arbitrary changes of coordinates.  It is the
natural construction that simultaneously deletes classes dying on the right
and retains target-only classes created by the left quotient.

For a diagram of chain complexes, the homotopy pushout gives no additional
cancellation.  The cone long exact sequence gives

\[
0\to\operatorname{coker}H_q(a,-b)
 \to H_q\operatorname{Cone}(a,-b)
 \to\ker H_{q-1}(a,-b)\to0.
\tag{2.4}
\]

Hence its dimension is

\[
 p_q+t_q+w_q+s_{q-1}.
\tag{2.5}
\]

In particular a target-only bar is retained with positive multiplicity and
cannot be canceled by the cone; the adjacent kernel only adds dimension.

## 3. Exact common-factor barcode

For

\[
 F_2=c\prod_{i=1}^6a_i+c\prod_{j=1}^6b_j,
\]

the prior exact audit gives

\[
 x=y=2016,\qquad z=588,\qquad a=\mathrm{id},qquad
 \operatorname{rank}b=540.
\]

Thus \(r=2016\), and (1.1) becomes

\[
 (p,u,v,s,t,w)=(540,1476,0,0,0,48).
\tag{3.1}
\]

Consequently the persistent interval has dimension \(540\), the target
survivor (2.3) has dimension \(540\), and the pushout has dimension
\(540+48=588\).  This explains categorically why the persistent construction
deletes enough common-factor classes while the full target does not.

## 4. Glynn column-multidegree kernel

Let \(I_G\) be the intersection of the annihilators of the 64 Glynn terms,
let \(R_G=S/I_G\), and let \(J=\operatorname{Ann}(\operatorname{perm}_7)\).
The common-quadratic calculation gives:

* within one matrix column, \((I_G)_2\) has dimension \(28\), namely every
  quadric on the seven variables in that column;
* in a pair of distinct columns, \((I_G)_2\) has dimension \(27\);
* in three distinct columns, \((R_G)_3\) has dimension
  \(7+\binom73=42\).

There are no common linear annihilators.  Therefore

\[
 X=\mathsf B(R_G)
 =\ker\bigl(V^*\otimes(I_G)_2\longrightarrow S_3\bigr)
\tag{4.1}
\]

and it can be counted one column multidegree at a time.

For a fixed column \(j\), the degree \(3e_j\) block has domain dimension
\(7\cdot28=196\) and image dimension \(\binom93=84\), hence kernel
dimension \(112\).

For a fixed ordered pair \(j\ne k\), the degree \(2e_j+e_k\) block has
domain dimension

\[
 7\cdot28+7\cdot27=385.
\]

The same-column quadrics already generate the entire degree block, of
dimension \(\binom82\cdot7=196\).  Its kernel therefore has dimension
\(189\).

For a fixed unordered triple \(\{j,k,l\}\), the all-distinct degree block
has domain dimension

\[
 3\cdot7\cdot27=567.
\]

Its full polynomial space has dimension \(7^3=343\), and the quotient has
dimension \(42\), so the image has dimension \(301\) and the kernel has
dimension \(266\).

Summing gives

\[
\begin{array}{c|c|c}
\text{column type}&\text{number of blocks}&\text{total kernel dimension}\\ \hline
3e_j&7&7\cdot112=784\\
2e_j+e_k&42&42\cdot189=7938\\
e_j+e_k+e_l&35&35\cdot266=9310.
\end{array}
\tag{4.2}
\]

The total is \(784+7938+9310=18032\), independently reproducing the known
dimension of the common linear-syzygy space.

Each Glynn term has one independent factor in each column.  In its essential
seven-variable ring the apolar ideal is generated by one square in each
column.  The other 42 ambient directions are linear annihilators, six in
each column.  Hence its internal-degree-three \(\operatorname{Tor}_2\) is
the tensor product of one inactive linear generator and one essential square.
Every such class has column degree \(3e_j\) or \(2e_j+e_k\); there is no
all-distinct-column class.

The right map \(b\) preserves column multidegree.  It therefore kills the
entire \(9310\)-dimensional third row of (4.2), so

\[
 \operatorname{rank}b\le 784+7938=8722.
\tag{4.3}
\]

The left map \(a:X\to\mathsf B(A_P)\) is injective.  Indeed, both \(I_G\)
and \(J\) have zero linear part, \((I_G)_2\subset J_2\), and their
\(\beta_{2,3}\) spaces are literal kernels of multiplication.  Inclusion of
the quadratic-generator spaces therefore includes the first kernel in the
second.

Write \(q=\operatorname{rank}b\).  Since \(a\) is injective, the Glynn
barcode is

\[
 p=q,\quad u=18032-q,\quad v=s=0,\quad t=18816-18032=784,
 \quad w=18816-q.
\tag{4.4}
\]

Equations (4.3)--(4.4) imply

\[
 u\ge9310,qquad p+t\le8722+784=9506.
\tag{4.5}
\]

Thus the coupled target survivor (2.3) misses the requested \(18523\) by at
least \(9017\).

The pushout fails in the opposite direction.  Because \((a,b)\) is
injective,

\[
 \dim H=y+z-x=18816+18816-18032=19600>18816=64\cdot294.
\tag{4.6}
\]

So the mapping cone keeps the 784 target-only classes and also all unused
right-only classes; the known 64-term decomposition itself violates the
required atom budget.

## 5. No additive target selector can pass both tests

Consider an additive functor from finite-dimensional forks to vector spaces
which is, pointwise, a subquotient of the target vertex \(Y\).  On each of
the six one-dimensional interval forks its value has dimension zero or one.
Only \(I_{XYZ},I_{YX},I_Y\) have nonzero target vertex.  Hence for fixed
\(c_p,c_u,c_t\in\{0,1\}\), every such selector has dimension

\[
 c_pp+c_uu+c_tt.
\tag{5.1}
\]

If \(c_u=1\), the \(F_2\) value is at least \(1476>588\), so the two-atom
cap fails.  If \(c_u=0\), its value on the legal Glynn diagram is at most
\(p+t\le9506<18523\).  Therefore:

> **Fork-selector no-go theorem.** No additive functorial subquotient of the
> target vertex, determined solely by the homology-level fork (0.1), both
> obeys the sharp two-Chow-atom cap on \(F_2\) and retains the required
> \(18523\) permanent classes on the Glynn diagram.

Even fractional retention does not repair the capacity.  If
\(0\le c_p,c_u,c_t\le1\), the \(F_2\) cap is

\[
 540c_p+1476c_u\le588.
\]

Maximizing the Glynn value under \(q\le8722\) gives

\[
 c_p=1,\qquad c_u=\frac4{123},\qquad c_t=1,
\]

and the exact ceiling

\[
 8722+9310\frac4{123}+784
 =\frac{1206478}{123}<9809<18523.
\tag{5.2}
\]

There is also a completely abstract obstruction.  Any nonnegative
direct-sum-additive scalar invariant \(\Phi\) is a nonnegative weighting of
the six interval multiplicities.  If \(\Phi(D)\le C\dim Z\) for every fork,
then applying the inequality to \(I_{YX},I_X,I_Y\), whose \(Z\)-vertex is
zero, forces their weights to vanish.  In particular the target-only weight
is zero: a universally right-endpoint-chargeable additive rank can never
retain quotient-created classes.

## 6. Monotonicity warning

Global/persistent ranks do not automatically have the two monotonicities
needed by the apolar span diagram.  For the sink fork

\[
 K\longrightarrow K^2\longleftarrow K
\]

with images \(Ke_1\) and \(Ke_2\), the intersection/global rank is zero.
After quotienting the middle vertex by \(K(e_1-e_2)\), the two images become
the same nonzero line and the global rank becomes one.

Dualizing gives the source-fork version.  Let \(X=K^2\), \(Y=Z=K\),
\(a(s,t)=s\), and \(b(s,t)=t\).  Its full-interval multiplicity is zero,
but the subrepresentation with source \(K(1,1)\) and full endpoint spaces is
\(I_{XYZ}\), so its full-interval multiplicity is one.  Thus the persistent
rank increases under a subobject.  A left-quotient/right-injection argument
cannot invoke monotonicity without a new algebra-specific proof.

## 7. Exact boundary and next possible escape

The following candidates are closed:

1. the full interval/persistent rank \(p\);
2. the target-to-pushout image \(p+t=\dim Y/a(\ker b)\);
3. every additive target subquotient of the bare fork;
4. the ordinary homotopy-pushout/mapping-cone homology;
5. every universally right-endpoint-dominated nonnegative additive fork
   rank.

An escape must use structure forgotten by the fork of Tor vector spaces,
for example a multiplication-compatible map between different internal
degrees, the Frobenius trace induced by \(f=\sum_iT_i\), or a genuinely
nonadditive construction with a separately proved atom-wise inequality.
Schur/Fitting constructions do not evade the theorem merely by being
coordinate-free: they must supply a new subadditivity proof, and any
construction whose matrices remain block diagonal on direct sums falls back
under the additive barcode argument.

## 8. Reproduction

Run

```text
python results/perm7_theory_first_20260822/exact64_syzygy/diagram_invariant/fork_barcode_audit.py
```

The expected final marker is

```text
FORK_BARCODE_AUDIT_PASS
```

The script uses exact integer and rational arithmetic only.
