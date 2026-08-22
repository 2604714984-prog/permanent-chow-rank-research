# N6-065: exclusion of the single-grade common-row-slice collision

**Status.** `PURE_SINGLE_GRADE_COMMON_ROWSLICE_EXCLUSION`,
`EXACT_QQ_LINEAR_REPLAY` (N6-065).

This note excludes one precise boundary layer at the unresolved (b=50)
endpoint.  All six factor planes collide to the same complete row slice, and
the five first nonzero relative section-difference spaces occur in one shared
grade and are direct.  Leading dependence, higher-order collision trees and
multiple valuation levels remain open.

## 1. The single-grade layer

Let \(A=C=k^6\), let \(p=e_0\in A\), and let the common limiting factor plane
be

\[
 L_0=p\otimes C.
\tag{1.1}
\]

Use color one as the base.  Suppose the other five relative differences first
appear in one common valuation grade, and their leading fifteen-planes are in
direct sum.  Equivalently, after dividing the five section differences by
their common order, their reductions form the 75-dimensional Grassmann flat
limit \(K_0\) of the actual spaces \(K(t)\).

At every nonzero fiber N6-064 gives
\(\dim\partial K(t)=23\).  Derivative rank cannot increase under
specialization, so \(\dim\partial K_0\le23\).  The universal product-shadow
lower bound for a 75-plane in \(E_2\) gives the reverse inequality.  Hence

\[
 \boxed{\dim\partial K_0=23.}
\tag{1.2}
\]

This argument does not assume strictness of an arbitrary filtered derivative
complex: direct leading spaces identify their sum with the ordinary
Grassmann limit \(K_0\), to which specialization and the universal lower
bound apply directly.

## 2. First-order quotient gauge

On the affine Grassmann chart at \(L_0\), a leading relative motion is a
normal graph

\[
 \phi:C\longrightarrow(A/\langle p\rangle)\otimes C.
\tag{2.1}
\]

Let \(F_0:S_0(C)\to\operatorname{Sym}^2V\) be the limiting full frame,
with \(F_0(e_ce_d)=x_{0c}x_{0d}\).  The first-order frame difference is

\[
 Q_\phi(e_ce_d)
 =x_{0c}\phi(e_d)+x_{0d}\phi(e_c).
\tag{2.2}
\]

There is no need to assume that the two quotient bases agree to first order.
An arbitrary common-quotient identification has the form
\(I+tB+O(t^2)\), and changes the leading section difference by \(F_0B\).
The image of \(F_0B\) has same-row weight \(\{0,0\}\), whereas
\(Q_\phi(S_0(C))\) has row-pair weights \(\{0,r\}\), \(r>0\).  The permanent
rectangle space \(E_2\) contains only distinct-row weights.  These weight
spaces are a direct sum.  Therefore

\[
 Q_\phi-F_0B\subset E_2
 \quad\Longrightarrow\quad F_0B=0
 \quad\Longrightarrow\quad B=0,
\tag{2.3}
\]

because \(F_0\) is injective.  Thus every actual leading section difference
in this layer is exactly \(Q_\phi(S_0(C))\subset E_2\), independently of the
chosen first-order quotient gauge.

## 3. Rectangle rigidity

Write

\[
 \phi(e_c)=\sum_{r=1}^{5}\sum_{a=0}^{5}a_{r,a,c}x_{ra}.
\tag{3.1}
\]

Fix \(c<d\).  In \(x_{0c}\phi(e_d)\), a monomial can lie in a permanent
rectangle only when its second column is \(d\).  The other summand gives the
analogous condition at \(c\).  Equality of the two rectangle corners gives

\[
 a_{r,a,d}=0\ (a\ne d),\qquad
 a_{r,a,c}=0\ (a\ne c),\qquad
 a_{r,d,d}=a_{r,c,c}.
\tag{3.2}
\]

As \(c<d\) is arbitrary, there is one
\(w\in A/\langle p\rangle\) such that

\[
 \boxed{\phi(e_c)=w\otimes e_c\quad\text{for every }c.}
\tag{3.3}
\]

Conversely every map (3.3) gives rectangle quadrics.  The exact replay writes
(3.2) as 825 sparse integral equations in the 180 coefficients of \(\phi\)
and obtains

\[
 \operatorname{rank}_{\mathbb Q}=175,
 \qquad \operatorname{nullity}_{\mathbb Q}=5.
\tag{3.4}
\]

## 4. Five direct colors force shadow 36

For a nonzero direction \(w\), the leading section-difference space is

\[
 D_w=(pw+wp)\otimes S_0(C),
 \qquad\dim D_w=15.
\tag{4.1}
\]

If the five \(D_{w_i}\) are direct, the five vectors \(w_i\) are independent
in the five-dimensional space \(A/\langle p\rangle\), hence form a basis.
Consequently

\[
 K_0=\bigoplus_{i=2}^{6}D_{w_i}
 =p(A/\langle p\rangle)\otimes S_0(C),
 \qquad\dim K_0=75.
\tag{4.2}
\]

The five row pairs \(\{0,r\}\), \(1\le r\le5\), meet every row, and every
column occurs in a column pair.  Therefore

\[
 \boxed{\dim\partial K_0=6\cdot6=36,}
\tag{4.3}
\]

contradicting (1.2).  The single-grade common-row-slice layer is impossible.
Transposition gives the same result for a common complete column slice.

## 5. Exact replay and boundary

```text
python scripts/n6_common_rowslice_collision_exclusion.py \
  --json data/n6_common_rowslice_collision_exclusion.json
python -m unittest tests.test_n6_common_rowslice_collision_exclusion -v
```

If the five leading spaces are dependent, higher-order terms can enter the
75-dimensional flat limit of \(K(t)\); then (4.2) does not describe that
limit.  Likewise, unequal valuations or successive clusters can create a
collision tree with new base slices.  N6-065 does not classify those cases,
exclude every common-row-slice or nonslice collision, remove the full
\(b=50\) endpoint, or prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge28\).
