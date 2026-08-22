# The \(12\to11\) actual-pair exclusion

**Status.** PURE_CHARACTERISTIC_ZERO_SHADOW11_ACTUAL_PAIR_EXCLUSION;
PURE_PROJECTIVE_EQUALITY_LOCUS_GLOBALIZATION;
EXACT_QQ_LINEAR_AND_QUADRATIC_ELIMINATION;
EXACT_SYMBOLIC_432_BRANCH_REPLAY (N6-110). The base field is algebraically
closed of characteristic zero.

Let \(V=k^6\otimes k^6\), and let \(E_2\subset\operatorname{Sym}^2V\) be
the 225-dimensional space spanned by the permanent rectangles. This note
proves the following pair theorem.

> **Theorem.** Let \(L,M\subset V\) be six-planes and let
> \(D\subset E_2\cap(\operatorname{Sym}^2L+\operatorname{Sym}^2M)\) have
> dimension twelve. Then
>
> \[
>  \dim\partial D=12,\qquad L\cap M=0,\qquad
>  \partial D=L\oplus M.
> \tag{0.1}
> \]

Thus an actual twelve-dimensional section difference cannot occupy an
eleven-dimensional small hook. This is exactly the dimension that remained
uncontrolled at the \(a_2=72,\kappa_2=0\) critical six-term layer.

## 1. Coordinate \(12\to11\) equality supports

The product Kruskal--Katona theorem N6-056 gives

\[
 \dim D=12\quad\Longrightarrow\quad\dim\partial D\ge11.
\tag{1.1}
\]

Its exact Ferrers program has only two minimizing profiles:

\[
 (6,3,3),\qquad(3,3,3,1,1,1).
\tag{1.2}
\]

We also need the classification in the original, uncompressed support.
Write a coordinate support as row-edge fibers
\(B_R\subset\binom{[6]}2\). Its variable shadow is

\[
 \bigcup_R R\times\partial B_R.
\tag{1.3}
\]

For the first profile, let \(R_0\) be the six-element fiber. Its column
shadow has at least four vertices. Each three-element fiber has at least
three. Unless the three active row edges form a triangle, the endpoints
outside \(R_0\) already make (1.3) at least twelve-dimensional. Equality
therefore forces a row triangle. At the two endpoints of \(R_0\), the short
shadows must be contained in its four-set; at the third endpoint their union
has size three. Hence the two short fibers are the same triangle on a
three-set \(C_3\subset C_4\), while the long fiber is the complete edge set
of \(C_4\). The resulting eleven-cell hook and its twelve rectangles are

\[
 U=R_2\otimes C_4+R_3\otimes C_3,\qquad
 R_2\subset R_3,\quad C_3\subset C_4.
\tag{1.4}
\]

For the second profile, the three degree-three row edges must form a
triangle: otherwise their three-vertex shadows alone contribute at least
twelve. The other three row edges must share one new vertex, and equality
forces their singleton column fibers to be the same edge contained in the
common column triangle. This is the transpose of (1.4).

The finite one-factor equalities used above are replayed exhaustively:
there are respectively \(15,20,15\) edge families of sizes \(1,3,6\) with
minimum vertex shadows \(2,3,4\). There are

\[
 \binom63\binom32\binom64\binom43=3600
\tag{1.5}
\]

row-oriented supports and 3600 transpose supports, with no overlap. All
7200 have twelve rectangles and eleven variables.

## 2. The fixed cross-free schemes

At the standard point take

\[
 U_0=
 (\langle e_0,e_1\rangle\otimes\langle f_0,f_1,f_2,f_3\rangle)
 +(\langle e_0,e_1,e_2\rangle\otimes\langle f_0,f_1,f_2\rangle),
\tag{2.1}
\]

and \(D_0=E_2\cap\operatorname{Sym}^2U_0\). Thus

\[
 \dim U_0=11,\qquad\dim D_0=12.
\tag{2.2}
\]

For subspaces \(P,Q\subset U_0^*\), write

\[
 \beta_{D_0}(P,Q)=0
\tag{2.3}
\]

when every bilinear form in \(D_0\) vanishes on \(P\times Q\). The exact
coordinate scan evaluates all

\[
 \binom{11}{5}^2=213444
\tag{2.4}
\]

ordered coordinate five-plane pairs. There is exactly one solution, the
diagonal point \(P_0=Q_0\), where

\[
 P_0=
 \langle x_{03}^*,x_{13}^*,x_{20}^*,x_{21}^*,x_{22}^*\rangle.
\tag{2.5}
\]

The same exact scan finds no cross-free coordinate pair of dimensions

\[
 (5,6),\qquad(6,5),\qquad(6,6).
\tag{2.6}
\]

These are complete integer enumerations, not random samples.

## 3. The complete local germ at the diagonal point

Consider the projective incidence of tuples \((D,U,P,Q)\) with

\[
 \dim(D,U,P,Q)=(12,11,5,5),\qquad
 \partial D\subset U,\qquad\beta_D(P,Q)=0.
\tag{3.1}
\]

Use Grassmann graph coordinates at \((D_0,U_0,P_0,P_0)\). There are 2891
variables: 2556 for \(D\), 275 for \(U\), and 30 for each of \(P,Q\).
The row-column torus splits them into 1440 weight blocks. Exact rational
linear elimination gives

\[
 \begin{array}{c|c}
 \text{equations}&\text{nullity}\\ \hline
 \partial D\subset U&82\\
 \partial D\subset U,\ \beta_D(P,Q)=0&17.
 \end{array}
\tag{3.2}
\]

Every surviving tangent has zero \(P\)- and \(Q\)-coordinate. The seventeen
directions are exactly

\[
 \begin{array}{c|c|c}
 \text{axis}&\text{outside targets}&\text{sources per target}\\ \hline
 \text{row}&3,4,5&3\\
 \text{column}&4,5&4.
 \end{array}
\tag{3.3}
\]

After eliminating all linear equations, substitute these seventeen
directions into every grounded quadratic equation. Among the 153 quadratic
monomials, the exact cokernel rank is twenty-one. The twenty-one independent
initial equations are precisely the products of two distinct sources aimed
at the same target:

\[
 J=I(K_3)+I(K_3)+I(K_3)+I(K_4)+I(K_4).
\tag{3.4}
\]

No expected generator is missing, and no other monomial survives in the
linear cokernel.

Conversely choose one source for each of the five targets. The Boolean
row-column replacement formulas give

\[
 3^3\,4^2=432
\tag{3.5}
\]

exact five-parameter branches. The symbolic replay verifies, to all orders,

\[
 \partial D(\mathbf t)\subset U(\mathbf t),\qquad
 \beta_{D(\mathbf t)}(P_0,P_0)=0,
\tag{3.6}
\]

and the selected \(5\times5\) chart Jacobian is the identity on every
branch. Thus the branches give the reverse initial inclusion to (3.4).
The usual complete filtered-ideal lifting proves that the full formal germ
is scheme-theoretically their union. In particular every local branch is
contained in the diagonal \(P=Q\).

## 4. Projective globalization

Let \(X_{r,s}\) be the closed projective relative incidence of

\[
 (D,U,P,Q),\quad
 \dim(D,U,P,Q)=(12,11,r,s),\quad
 \partial D\subset U,\quad\beta_D(P,Q)=0.
\tag{4.1}
\]

Every irreducible component is preserved by the connected row-column
torus and contains a fixed point. At a fixed point, \(D\) and \(U\) are
coordinate; (1.1) makes \(U=\partial D\), and Section 1 reduces them to
(1.4) or its transpose.

The coordinate scan (2.6) therefore proves

\[
 X_{5,6}=X_{6,5}=X_{6,6}=\varnothing.
\tag{4.2}
\]

For \(X_{5,5}\), every component contains the unique diagonal fixed point
from (2.5), up to row-column permutations and transpose. Section 3 puts
the complete formal germ at that point in the closed diagonal locus. Hence
each component, and therefore all of \(X_{5,5}\), is contained in \(P=Q\):

\[
 X_{5,5}\subset\{P=Q\}.
\tag{4.3}
\]

This is a component argument using a closed projective incidence; it does
not reverse an individual torus specialization.

## 5. Proof of the actual-pair theorem

Assume for contradiction that \(\dim\partial D=11\), and put

\[
 U=\partial D\subset L+M.
\tag{5.1}
\]

Euler's identity gives \(D\subset\operatorname{Sym}^2U\). If
\(\dim(L\cap M)\ge2\), then \(\dim(L+M)\le10\), contradicting (5.1).

If \(\dim(L\cap M)=1\), then \(U=L+M\). The annihilators

\[
 P=L^\perp,\qquad Q=M^\perp\subset U^*
\tag{5.2}
\]

are disjoint five-planes and satisfy \(\beta_D(P,Q)=0\). But (4.3) forces
\(P=Q\), a contradiction.

It remains to consider \(L\cap M=0\). Put \(W=L\oplus M\), and let
\(kz=U^\perp\subset W^*\). The two six-dimensional annihilators
\(L^\perp,M^\perp\subset W^*\) descend to subspaces of \(U^*=W^*/kz\).
Their dimensions are \((6,6)\) if \(z\) lies in neither annihilator, and
\((5,6)\) or \((6,5)\) if it lies in one. Since \(D\) has radical \(z\),
the descended pair is cross-free for \(D\). This contradicts (4.2).

Thus \(\dim\partial D\ne11\). Equations (1.1) and
\(\partial D\subset L+M\) now give exactly (0.1).

## 6. The \(\kappa_2=0\) consequence

At the N6-101 critical layer

\[
 (a_2,\kappa_2,t_2)=(72,0,18),
\tag{6.1}
\]

the six quadratic Chow spaces are literal direct. For every pair \(i,j\),
their quotient fifteen-planes in the common eighteen-plane meet in
dimension at least twelve, producing an actual section difference
\(D_{ij}\subset K\). Choose any twelve-plane
\(D'_{ij}\subset D_{ij}\). The theorem gives

\[
 \partial D'_{ij}=L_i\oplus L_j.
\tag{6.2}
\]

In particular the full \(D_{ij}\) also has shadow \(L_i\oplus L_j\).
Consequently all six factor planes are pairwise transverse and lie in
\(M=\partial K\). The reverse containment follows from
\(K\subset\sum_iF_i\), so

\[
 \boxed{M=\sum_{i=1}^6L_i},\qquad\dim M=23,
\tag{6.3}
\]

now also for \(\kappa_2=0\).

## 7. Boundary and replay

N6-110 closes the shadow-eleven pair collision and supplies the missing
factor-span identity (6.3) at \(\kappa_2=0\). It does **not** yet exclude the
resulting standard-hook or biflag six-color configurations. It therefore
does not by itself prove ordinary lower \(29\), determine
\(\operatorname{ChowRank}(\operatorname{perm}_6)=32\), or prove a border-rank
bound.

Replay with

    python scripts/n6_shadow11_pair_incidence_diagnostic.py \
      --verify-json data/n6_shadow11_pair_incidence_exclusion.json
