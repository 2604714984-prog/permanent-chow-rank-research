# N6-082: classification of the \(80\to90\) product-shadow locus

**Status.** PURE_CHARACTERISTIC_ZERO_B80_EQUALITY_LOCUS_CLASSIFICATION;
EXACT_INTEGER_LINEAR_AND_QUADRATIC_ELIMINATION;
EXACT_SYMBOLIC_16_BRANCH_REPLAY.

## 1. The theorem

Let \(X\subset E_3\) be an \(80\)-plane with \(\dim\partial X=90\).
Up to row-column transposition, there is a partition

\[
 [6]=B_1\sqcup B_2\sqcup B_3\sqcup B_4
\]

and nonzero vectors \(v_i\) supported on the disjoint blocks \(B_i\) such that

\[
 X=\left\langle v_iv_jv_k:1\le i<j<k\le4\right\rangle
      \otimes E_3(C),                                         \tag{1.1}
\]

\[
 \partial X=\left\langle v_iv_j:1\le i<j\le4\right\rangle
      \otimes E_2(C).                                         \tag{1.2}
\]

Consequently

\[
 \partial^2X=\langle v_1,v_2,v_3,v_4\rangle\otimes C,\qquad
 \dim\partial^2X=24.                                          \tag{1.3}
\]

There are \(S(6,4)=65\) row-partition components and \(65\) transposed
components. Each is a product of projective spaces of total dimension two.

## 2. Coordinate fixed points

The exact Ferrers minimizers are only

\[
 (20,20,20,20,0^{16}),\qquad (4^{20}).                        \tag{2.1}
\]

This is not used as a reverse-compression assertion. The first compression
preserves every row-fiber size and makes the rows left-justified. The second
preserves the conjugate column heights. Hence (2.1) is the sorted degree
profile of the original support.

In the first case there are four active row triples and every column fiber is
full. The shadow has size \(15|\partial\mathcal F|=90\), so the four triples
have six lower pairs. The one-factor equality case is

\[
 \mathcal F=\binom{U}{3},\qquad |U|=4.                         \tag{2.2}
\]

In the second profile every row fiber has four triples. Every active row pair
contributes at least six column pairs, and all fifteen row pairs occur.
Equality forces every fiber to be \(\binom{V_R}{3}\), \(|V_R|=4\), and
forces equal shadows for fibers whose row triples share a pair. The Johnson
graph on \(\binom{[6]}3\) is connected, so all \(V_R\) are one common \(V\).
This is the transpose of (2.2).

Thus there are thirty coordinate fixed points. At a standard point the full
coordinate inverse shadow

\[
 P_{E_3}(K)=\{f\in E_3:\partial f\subset K\}
\]

is exactly the original \(80\)-plane.

## 3. Complete local structure

At the standard row point take \(U=\{0,1,2,3\}\). The incidence
linearization has eight free roots and no \(\eta\)-only root:

\[
 a\longrightarrow4,\qquad a\longrightarrow5,\qquad a\in U.  \tag{3.1}
\]

After all linear equations are eliminated, the grounded quadratic rows have
exact rational rank twelve and unit span

\[
 J=I(K_4)_{\{a\to4\}}+I(K_4)_{\{a\to5\}}.                    \tag{3.2}
\]

The replay checks \(169200\) grounded equations; its \(1440\) nonzero rows
are integer multiples of exactly the twelve monomials in (3.2). The
transposed point has the same result.

The radical ideal (3.2) has sixteen facets, choosing one source for each
target. For every choice, the degree-three, degree-two, and degree-one
Boolean replacements satisfy both derivative containments symbolically, and
the selected \(2\times2\) chart Jacobian is the identity.

Both targets are absent from the original four-block support, so these
Boolean maps are restrictions of the same actual linear row shears in all
three degrees. No repeated-row collision term occurs.

The grounded forms give \(J\subset\operatorname{in}I\). The sixteen exact
branches give the reverse inclusion
\(\operatorname{in}I\subset\bigcap P_{ab}=J\). Complete filtered-ideal
lifting identifies the completed local ideal with their intersection.

## 4. Projective globalization

Let

\[
 \mathcal I_{80}=
 \{(X,K)\in\operatorname{Gr}(80,E_3)\times\operatorname{Gr}(90,E_2):
 \partial X\subset K\}.
\]

This is closed, projective, and torus stable. The lower bound \(m_{80}=90\)
makes \(K=\partial X\) at every closed point. Every irreducible component
contains a coordinate fixed point. Section 3 identifies its complete fixed
germ with the partitioned-product branches, whose projective images are
closed. Hence the entire component lies in the same image, proving
(1.1)--(1.2).

The universal second-shadow minimum at dimension \(90\) is \(24\).
Differentiating (1.2) supplies the matching upper product plane, proving
(1.3).

## 5. Boundary

This theorem classifies the equality locus and its second shadow. It does not
by itself exclude an actual seven-frame endpoint, global \(b=34\), or prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\). It makes no
border-rank claim.
