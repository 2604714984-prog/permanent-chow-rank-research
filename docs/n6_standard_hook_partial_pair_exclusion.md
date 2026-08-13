# N6-109: the standard-hook partial-pair exclusion

## 1. Result and evidence level

Let

\[
 M=R_4\otimes C_5+R_3\otimes C_6
 \subset R_6\otimes C_6,
 \qquad
 K=E_2\cap\operatorname{Sym}^2M.
\tag{1.1}
\]

Thus \(\dim M=23\) and \(\dim K=75\). This note proves two
characteristic-zero statements.

1. Every \(U\in\operatorname{Gr}(12,M)\) satisfying
   \[
    \dim(K\cap\operatorname{Sym}^2U)\geq13
   \tag{1.2}
   \]
   is a tensor product of type \(2\times6\), \(3\times4\), or
   \(4\times3\).
2. The standard-hook alternatives at
   \[
    (a_2,\kappa_2,t_2)=(72,1,17),(72,2,16)
   \tag{1.3}
   \]
   cannot be actual six-term configurations.

The proof combines pure projective-torus arguments with finite exact
rational certificates. No random calculation or finite-field inference is
used.

## 2. Coordinate fixed points

Use the standard coordinate hook

\[
 \{0,1,2\}\times\{0,\ldots,5\}
 \ \cup\ \{3\}\times\{0,\ldots,4\}.
\tag{2.1}
\]

For a coordinate twelve-plane, the dimension of
\(K\cap\operatorname{Sym}^2U\) is the number of permanent rectangles whose
four corners lie in its support. The replay enumerates all

\[
 \binom{23}{12}=1,352,078
\]

supports. The high end of the exact histogram is

\[
\begin{array}{c|rrrrr}
\text{dimension}&10&11&12&15&18\\ \hline
\text{count}&7200&270&6120&3&40.
\end{array}
\tag{2.2}
\]

In particular dimensions \(13,14,16,17\) do not occur. The forty-three
fixed points at threshold thirteen are

\[
\begin{array}{c|c|c}
\text{type}&\text{row profile}&\text{count}\\ \hline
K_{2,6}&(6,6,0,0)&3\\
K_{3,4}&(4,4,4,0)&30\\
K_{4,3}&(3,3,3,3)&10.
\end{array}
\tag{2.3}
\]

The \(K_{3,4}\) points split into three hook-stabilizer orbits: core rows
and core columns, core rows with the sixth column, and a support using the
fourth row.

## 3. Relative normal leakage

At each fixed product \(U_0\), expand its base rectangle space in the
\(132\)-variable Grassmann graph chart. Reduce the first graph coefficient
modulo \(K+\operatorname{Sym}^2U_0\). A first normal direction can retain
thirteen dimensions only if its leakage rank is at most

\[
 \dim(K\cap\operatorname{Sym}^2U_0)-13,
\]

namely two at \(K_{2,6}\) and five at the other four types.

The exact characteristic-zero data are

\[
\begin{array}{c|c|c|c|c}
\text{type}&\text{base dimension}&\text{linear rank}&
\text{kernel}&\text{minimum nonproduct leakage}\\ \hline
K_{2,6}&15&130&2&5\\
K_{3,4}\text{ core}&18&121&11&6\\
K_{3,4}\text{ sixth column}&18&124&8&6\\
K_{3,4}\text{ fourth row}&18&125&7&6\\
K_{4,3}&18&126&6&6.
\end{array}
\tag{3.1}
\]

Explicit integer vectors identify every kernel with the tangent space to the
closed product incidence inside \(M\). The minimum ranks are exact: the
row-column torus separates every quotient weight, and the script checks the
minimum support rank over every fixed weight group by rational row
elimination.

### 3.1 The two nonlinear corners

Two \(K_{3,4}\) charts have compatible second-order product corners. Write
\(a\) and \(b\) for the row and column factor parameters and \(\gamma\) for
an available corner coordinate. The correct relative normal coordinate is

\[
 d=\gamma-a\otimes b,
\tag{3.2}
\]

not \(\gamma\) alone.

For the core chart, the replay finds twelve pure \(d\)-weights and twelve
pure missing-corner \(a_ib_j\)-weights. Every coordinate has leakage rank
six. For the fourth-row chart there are twelve pure \(d\)-weights, again all
of rank six, and no missing corner. Hence (1.2) forces

\[
 d=0,\qquad
 a_i b_j=0\quad\text{at every absent corner}.
\tag{3.3}
\]

Thus the kernel directions integrate exactly to the product incidence; the
calculation does not confuse a parabolic second-order product arc with a
nonproduct branch.

## 4. Product globalization

Let \(Z_{13}\) be the closed projective locus defined by (1.2), and let
\(\mathcal P\) be the closed projective image of

\[
 \{(A,B):A\otimes B\subset M,\ \dim A\dim B=12\}.
\]

Every irreducible torus-stable component of \(Z_{13}\) contains a coordinate
fixed point. Sections 2 and 3 show that the projectivized relative normal
cone to \(\mathcal P\) has no fixed point at any such point. Therefore every
component of \(Z_{13}\) lies in \(\mathcal P\).

The factor dimensions are necessarily

\[
 (2,6),\qquad(3,4),\qquad(4,3).
\tag{4.1}
\]

The restricted quadratic dimensions at threshold thirteen are respectively
\(15\), \(15\) or \(18\), and \(15\) or \(18\).

## 5. Partial \(2\times6\) transverse rigidity

Put \(S_0=S_0(k^6)\), of dimension fifteen. Three small pure lemmas replace
the full-\(S_0\) inputs in N6-061.

### 5.1 A thirteen-plane multiplier lemma

For \(X\in\operatorname{End}(k^6)\), define

\[
 \Phi_X(B)=\bigl(\operatorname{diag}(XB),\,XB-(XB)^{\mathsf T}\bigr),
 \qquad B\in S_0.
\tag{5.1}
\]

If \(XQ\subset S_0\) for a thirteen-plane \(Q\subset S_0\), then
\(\operatorname{rank}\Phi_X\leq2\). Projectivize \(X\) modulo scalars.
Under the diagonal torus, its fixed locus consists of nonscalar diagonal
classes and the off-diagonal matrix units. A nonscalar diagonal class has
rank at least five in (5.1), and every off-diagonal matrix unit has rank
exactly five. The projective rank-at-most-two locus is therefore empty:

\[
 XQ\subset S_0,\quad\dim Q\geq13
 \quad\Longrightarrow\quad X\text{ is scalar}.
\tag{5.2}
\]

### 5.2 An invertible member

The locus of thirteen-planes \(Q\subset S_0\) on which the determinant
vanishes identically is closed, projective, and torus-stable. Its fixed
points are coordinate thirteen-edge subspaces of \(K_6\). Deleting any two
edges from \(K_6\) leaves a perfect matching; the exact replay checks all
\(\binom{15}{13}=105\) cases. Hence every \(Q\) contains an invertible
\(B_0\).

### 5.3 The ratio algebra

If the algebra generated by \(QB_0^{-1}\) had a nonzero proper invariant
space \(H\), then with \(Z=B_0^{-1}H\),

\[
 Q\subset T(H,Z):=\{B\in S_0:BZ\subset H\}.
\tag{5.3}
\]

For each \(1\leq h=\dim H=\dim Z\leq5\), the projective rank-jump locus for
\(\dim T(H,Z)\geq13\) is torus-stable. At coordinate fixed pairs, the exact
maxima are

\[
 (11,10,12,10,11)\qquad(h=1,\ldots,5).
\tag{5.4}
\]

Thus the rank-jump locus is empty. Burnside's theorem gives

\[
 \operatorname{Alg}(QB_0^{-1})=\operatorname{End}(k^6).
\tag{5.5}
\]

Now repeat the graph proof of N6-061 with a section-difference space
\(D\subset E_{2,6}\) of dimension at least thirteen. Its two-row block image
is a subspace \(Q\subset S_0\) of the same dimension. Equation (5.2) makes
every graph block scalar, so

\[
 \partial D=P_2\otimes k^6.
\tag{5.6}
\]

If \(D\) is block diagonal for an actual complementary pair \(L\oplus M\),
choose the invertible \(B_0\) from Section 5.2. The ratios (5.5) preserve both
blocks, so

\[
 L=p\otimes k^6,\qquad M=q\otimes k^6.
\tag{5.7}
\]

Unlike N6-061, no claim about the two six-factor frames being coordinate is
needed here.

## 6. Excluding the two standard-hook states

Take either state in (1.3). N6-103 gives a connected complementary relation
graph on the six factor planes. Every complementary edge \(ij\) carries an
actual section difference

\[
 \dim D_{ij}\geq12+\kappa_2\geq13,\qquad
 \partial D_{ij}=L_i\oplus L_j,
\tag{6.1}
\]

and the six planes span the standard hook:

\[
 M=\sum_{i=1}^{6}L_i,\qquad \dim M=23.
\tag{6.2}
\]

By Section 4, every edge shadow is one of the products (4.1). N6-108 excludes
the \(3\times4\) and \(4\times3\) cases for a complementary actual pair with
a cross-free section of dimension at least thirteen. Hence every edge is
\(2\times6\). Section 5 then makes both endpoints complete row slices
\(p\otimes k^6\).

The complementary graph is connected, so all six \(L_i\) are complete row
slices. Their sum has dimension

\[
 6\dim\langle p_1,\ldots,p_6\rangle,
\]

a multiple of six, contradicting (6.2). This excludes both states (1.3).

## 7. Boundary and replay

The two \(a_2=72,\kappa_2=0\) geometries remain open because their guaranteed
section difference has dimension only twelve. All \(a_2=73,74,75\) states
also remain open. N6-109 is not an ordinary lower-29, exact-rank-32, or
border-rank theorem.

Replay with:

    python scripts/n6_standard_hook_partial_pair_exclusion.py --verify-json data/n6_standard_hook_partial_pair_exclusion.json
    python -m unittest tests.test_n6_standard_hook_partial_pair_exclusion -v
