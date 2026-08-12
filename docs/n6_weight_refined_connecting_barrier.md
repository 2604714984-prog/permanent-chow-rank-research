# The forty permanent weights and the G-039 connecting-map frontier

**Status.** `PURE_WEIGHT_CLASSIFICATION`, `EXACT_QQ_REPLAY`,
`APOLAR_QUOTIENT_ROUTE_BARRIER` (G-040).  This note defines the legitimate
permanent-relative refinement of the G-039 connecting map.  It does not prove
`ChowRank(perm_6)>=27`, and it neither proves nor disproves a nontrivial cap
for actual six-term Chow sums.

The field has characteristic zero.  Let `V` be the 36-dimensional matrix
variable space with basis `x_(ij)`, put `S=Sym(V^*)`, and write

\[
 P=\operatorname{perm}_6,
 \qquad A_P=S/I_P,
 \qquad I_f=f^\perp.
\]

## 1. Exact labels of the forty classes

For three-subsets `A,B subset [6]`, let

\[
 p_{A,B}=\operatorname{perm}(x_{ij})_{i\in A,j\in B}
 \in E_3=\mathcal D_3(P).
\tag{1.1}
\]

Fix a row triple `A`.  For each column triple `B` and bijection
`sigma:A -> B^c`, take the wedge in increasing ambient-variable order and put

\[
 z_A^{\rm row}
 =\sum_{|B|=3}\ \sum_{\sigma:A\overset\sim\longrightarrow B^c}
 p_{A,B}\otimes
 \bigwedge_{i\in A}x_{i,\sigma(i)}.
\tag{1.2}
\]

Every summand has row-column torus weight

\[
 \alpha_A^{\rm row}
 =\bigl(2\mathbf1_A;\mathbf1_{[6]}\bigr).
\tag{1.3}
\]

The Leibniz signs cancel, so `delta_(3,3)(z_A^row)=0`.  In the representative
weight block, exact rational elimination gives

\[
 \dim(\text{domain})=120,
 \qquad \operatorname{rank}\delta_{3,3}=119,
\tag{1.4}
\]

and the all-ones coefficient vector in (1.2) spans the kernel.  Row
permutations prove the same result for all twenty row triples.

No preceding boundary has this weight.  An element of `E_4(P)` is a
four-by-four subpermanent and hence uses four distinct rows.  Adding a
two-fold wedge cannot remove row support, whereas (1.3) is supported on only
three rows.  Therefore `[z_A^row]` is nonzero in `H_(3,6)(P)`.

Transposition gives twenty column-heavy classes with weights

\[
 \alpha_B^{\rm col}
 =\bigl(\mathbf1_{[6]};2\mathbf1_B\bigr).
\tag{1.5}
\]

The forty displayed weights are pairwise distinct.  The exact global
calculation `dim H_(3,6)(P)=40` therefore proves

\[
 \boxed{
 H_{3,6}(P)=\mathcal R\oplus\mathcal C,
 \quad
 \mathcal R=\bigoplus_{|A|=3}\mathbf k[z_A^{\rm row}],
 \quad
 \mathcal C=\bigoplus_{|B|=3}\mathbf k[z_B^{\rm col}].}
\tag{1.6}
\]

## 2. Correct Tor index and the pushout identity

Assume hypothetically that `P=H+Q`, with six selected terms in `H` and a
twenty-term residual `Q`.  Since an operator killing any two of `P,H,Q`
kills the third,

\[
 M:=I_P\cap I_H=I_P\cap I_Q.
\tag{2.1}
\]

Put `J=I_Q/M`.  The G-039 module `J^diag`, defined as the image of
`I_Q -> E(P)`, `u |-> u lrcorner P`, is canonically isomorphic to `J`: its
kernel is `I_Q cap I_P=M`, and its differential-operator action is inherited
from contraction.

The G-039 exact sequence is

\[
 0\longrightarrow M\longrightarrow I_Q\longrightarrow J\longrightarrow0.
\tag{2.2}
\]

To reach permanent homology, one must compose its degree-six connecting map
with the map induced by `M -> I_P`:

\[
 \Theta_{P,H}:\operatorname{Tor}_3^S(J,\mathbf k)_6
 \longrightarrow\operatorname{Tor}_2^S(M,\mathbf k)_6
 \longrightarrow\operatorname{Tor}_2^S(I_P,\mathbf k)_6.
\tag{2.3}
\]

This composite has a simpler description.  Pushing (2.2) out along
`M -> I_P` gives

\[
 0\longrightarrow I_P\longrightarrow I_P+I_Q
 \longrightarrow J\longrightarrow0.
\tag{2.4}
\]

Indeed `(I_P+I_Q)/I_P` is `I_Q/(I_P cap I_Q)=J`.  Naturality of the long exact
Tor sequence identifies (2.3) with the connecting map of (2.4).  Hence

\[
 \operatorname{im}\Theta_{P,H}
 =\ker\left(
 \operatorname{Tor}_2^S(I_P,\mathbf k)_6
 \longrightarrow
 \operatorname{Tor}_2^S(I_P+I_Q,\mathbf k)_6
 \right).
\tag{2.5}
\]

For any proper homogeneous ideal `I`, the sequence
`0 -> I -> S -> S/I -> 0` and the vanishing of positive Tor of `S` give,
for `i>=1`,

\[
 \operatorname{Tor}_i^S(I,\mathbf k)_j
 \simeq\operatorname{Tor}_{i+1}^S(S/I,\mathbf k)_j.
\tag{2.6}
\]

Thus, with `B=S/(I_P+I_Q)`, equation (2.5) becomes

\[
 \boxed{
 \operatorname{im}\Theta_{P,H}
 =\ker\left(
 \operatorname{Tor}_3^S(A_P,\mathbf k)_6
 \longrightarrow
 \operatorname{Tor}_3^S(B,\mathbf k)_6
 \right).}
\tag{2.7}
\]

The internal degree is six: the relevant standard Koszul strand is

\[
 (A_P)_2\otimes\Lambda^4V^*
 \longrightarrow(A_P)_3\otimes\Lambda^3V^*
 \longrightarrow(A_P)_4\otimes\Lambda^2V^*.
\tag{2.8}
\]

Dualizing (2.8) by catalectic pairing and the coordinate exterior pairing
gives exactly

\[
 E_4(P)\otimes\Lambda^2V
 \longrightarrow E_3(P)\otimes\Lambda^3V
 \longrightarrow E_2(P)\otimes\Lambda^4V.
\tag{2.9}
\]

Consequently

\[
 \operatorname{Tor}_3^S(A_P,\mathbf k)_6^*
 \simeq H_{3,6}(P)=\mathcal R\oplus\mathcal C.
\tag{2.10}
\]

Equations (2.7)-(2.10) rigorously locate the G-039 connecting map.  Projecting
its target to `R^*` and `C^*` gives a permanent-relative pair of ranks, each
between zero and twenty.  Row and column permutations preserve the pair,
diagonal stabilizer elements rescale its one-dimensional weight factors, and
transposition exchanges the two entries.

## 3. Where the `336/203` intersections enter

The quotient `B` in (2.7) is not unrelated to the derivative intersections.
Its graded dual is

\[
 B_m^*=(I_P+I_Q)_m^\perp
 =E_m(P)\cap E_m(Q)=:F_m.
\tag{3.1}
\]

Therefore the known bounds say

\[
 \dim F_3\ge336,
 \qquad \dim F_2\ge203.
\tag{3.2}
\]

Moreover `F=direct_sum F_m` is an inverse-system submodule: differentiation
maps `F_m` into `F_(m-1)`.  Dualizing the Tor map in (2.7) gives the homology
map induced by the inclusion of complexes

\[
 F_4\otimes\Lambda^2V\to F_3\otimes\Lambda^3V
 \to F_2\otimes\Lambda^4V
 \quad\subseteq\quad (2.9).
\tag{3.3}
\]

Thus (3.1) is the correct bridge omitted by a dimension-only reading of
G-039.  The remaining question is whether the two dimensions in (3.2), plus
the fact that `F` comes from the particular residual `Q=P-H`, force any of
the forty classes in (1.6) into the image of (3.3).

## 4. A permanent-apolar quotient barrier to scalar dimensions

The answer is negative if one retains only that `F` is a differential
submodule of the permanent inverse system satisfying (3.2).

Index the 400 basis vectors of `E_3(P)` by the grid

\[
 (A,B),\qquad |A|=|B|=3.
\]

Choose a bijection between the twenty row triples and twenty column triples,
and delete the corresponding perfect matching of twenty grid cells.  Define

\[
 F_3=\operatorname{span}\{p_{A,B}:(A,B)\text{ is not deleted}\},
 \quad F_2=E_2(P),
 \quad F_1=E_1(P),
 \quad F_0=E_0(P),
\tag{4.1}
\]

and put `F_m=0` for `m>=4`.  This is a differential submodule: derivatives
of every retained three-by-three subpermanent lie in the full space `F_2`,
and the lower closure is automatic.  Its relevant dimensions are

\[
 \dim F_3=380\ge336,
 \qquad \dim F_2=225\ge203.
\tag{4.2}
\]

Because `F` is a graded inverse submodule of `E(P)=A_P^*`, it is the graded
dual of an actual quotient algebra of `A_P`.

Now fix a row triple `A`.  The perfect matching deletes one of the twenty
six-column cells from its 120-column heavy block.  The full block has rank
119 and a one-dimensional kernel generated by the all-nonzero all-ones
vector.  Hence the 114 retained columns are independent.  The verifier also
checks their rank directly over `Q`.  Therefore the `A` row-heavy homology of
(3.3) is zero.  The same argument applies to all row triples and, by the
matching property, to all column triples.  Since `F_4=0`, no hidden preceding
boundary changes this conclusion.  Thus the image of (3.3) in (1.6) is zero.

Equivalently, for this quotient-algebra model the kernel in (2.7) is the full
forty-dimensional space.  At the other extreme, `F=E(P)` satisfies (3.2) and
the map is the identity, so that kernel is zero.  Hence:

\[
 \boxed{
 \text{the scalar bounds }\dim F_3\ge336,\ \dim F_2\ge203,
 \text{ even with inverse-system closure, do not bound the refined kernel.}}
\tag{4.3}
\]

The matching-erasure quotient is not asserted to be `S/(I_P+I_Q)` for a
sextic `Q=P-H` with `H` a six-term Chow sum and `Q` a twenty-term Chow sum.
It therefore does not disprove an actual six-term cap.  It proves that such a
cap must use precisely this additional Chow-realizability constraint.

## 5. G-034/G-037 pressure test and strict boundary

The exact small examples give the pairs

\[
 (\rho,\text{labelled kernel})=(4,0),(4,7),(2,12).
\tag{5.1}
\]

Thus neither ordinary middle relation dimension nor the scalar labelled
kernel can replace the missing realizability theorem.  These examples are
replayed over `Q`, but they are not permanent connecting maps.

What is proved:

1. the forty explicit row/column-heavy weight lines exhaust `H_(3,6)(P)`;
2. the correct connecting image is the kernel (2.7), with Tor index three and
   internal degree six;
3. its dual is the homology map of the actual intersection module (3.1); and
4. the `336/203` dimensions plus inverse-system closure alone allow both
   endpoints zero and forty, so they impose no nontrivial uniform bound.

What remains unresolved is a nontrivial estimate on (2.7) for every
**realizable** pair `P=H+Q` with six Chow terms in `H` and twenty in `Q`.
Accordingly G-040 is a strict route refinement and barrier, not lower 27.

## 6. Replay

```text
python scripts/n6_weight_refined_connecting_barrier.py \
  --json data/n6_weight_refined_connecting_barrier.json
python -m unittest tests.test_n6_weight_refined_connecting_barrier -v
```

All displayed ranks are exact over `Fraction`.  No random or finite-field
evidence is used.
