# N7-008: the dual Koszul shadow tower gives ordinary lower 47

## Result

Over characteristic zero,

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge47.
\]

The input lower bound 46 is N7-007.  This note proves ordinary rank only;
the resulting interval is \([47,64]\).

## Recursive degree-five section

Let \(E_r=D_r(\operatorname{perm}_7)\).  Repeated use of

\[
\dim(E\cap(A+B))\le\dim(E\cap A)+\dim B
\]

and the exact bivariate product-shadow capacities gives the following nested
chain for arbitrary selected Chow terms:

\[
\begin{aligned}
C_2(5)&=3\cdot21+\phi_2(14)=85,\\
C_3(20)&=15\cdot35+\phi_3(85)=589,\\
C_4(42)&=22\cdot35+\phi_4(589)=1111,\\
C_5(46)&=4\cdot21+\phi_5(1111)=405.
\end{aligned}
\]

Here \(C_r(q)\) bounds
\(\dim(E_r\cap\sum_{i=1}^qD_r(T_i))\), and \(\phi_r\) is the exact
two-dimensional Ferrers capacity at degree \(r\).  The new finite value is

\[
\phi_5(1111)=321.
\]

Its area-321 witness \((21,15^{20})\) has shadow 1105, while every
area-322 diagram has shadow at least 1113.

## Correct dual Koszul degree

For a degree-seven form, the double-quotient loss for \(K_m\) is controlled
by the *dual catalectic degree* \(7-m\).  For \(m=2\), put

\[
b=\dim(E_5\cap D_5(R)).
\]

The double-quotient and prolongation estimates give

\[
\operatorname{rank}K_2(P-R)
\ge (49\cdot441-1225)-49b
=20384-49b.                                  \tag{1}
\]

N7-007 permits selecting 46 terms.  The recursive tower gives \(b\le405\),
so (1) is at least

\[
20384-49\cdot405=539>0.
\]

Thus those 46 terms cannot already sum to \(P\); at least one further term
is necessary, proving lower 47.  Equivalently, under a hypothetical
46-term decomposition one would have \(R=P\) and hence \(b=\dim E_5=441\),
contradicting \(b\le405\).

## Endpoint warning

The scan uses \(m=2,\ldots,6\) and the corresponding dual degrees
\(5,\ldots,1\).  It deliberately excludes \(m=1\): although a formal index
substitution would suggest a stronger number, \(E_1=V\) has prolongation
\(E_1^{(1)}=\operatorname{Sym}^2V\), not \(E_2\).  Therefore the cancellation
behind (1) is unavailable at that endpoint.

Likewise, \(K_4\) is controlled by degree 3, not degree 5.  Substituting a
degree-five cap into \(K_4\) is an invalid index match and does not prove
exact rank 64.

Replay with

```powershell
python scripts/n7_lower47_dual_koszul_shadow_tower.py --verify-json data/n7_lower47_dual_koszul_shadow_tower.json
python -m unittest tests.test_n7_lower47_dual_koszul_shadow_tower -v
```
