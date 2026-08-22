# Report for `P64_ordinary_valuative`

## Verdict

The ordinary-valuative/residual route does **not** prove

\[
\operatorname{ChowRank}(\operatorname{perm}_7)=64.
\]

It reduces exact rank (64) to a sharp uniform hyperplane-section lemma,
proves rigidity of the standard 64-term Glynn packet under every hyperplane
restriction, and rules out the most natural scalar, local-jet, and projection
repairs.  A decomposition unrelated to the Glynn packet remains the exact
uncontrolled possibility.

Separately, the degree-three/four residual analysis repairs the two disputed
49-term endpoints.  Conditional on the already-audited lower-49 theorem,
slope-ten equality classification, quadratic generation, the rectangular
middle-degree cap, and (D_3(T)\cap E_3=0), it proves the ordinary lower bound

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge 50.
\]

The full repaired endpoint proof is in
[`lower50_corrected_middle_repair.md`](lower50_corrected_middle_repair.md).
An independent hostile audit returned **valid**, with the wording caveat that
global-symbol injectivity is asserted only on the direct-basis source
subspace, not on all packet summands.

## 1. Correctly graded lower-50 repair

Let (P=\sum_iT_i), (I=P^\perp), (J=\bigcap_iT_i^\perp),
(R=I/J), (A_i=S/T_i^\perp), and (E_d=D_d(P)).  For every subpacket
(B), perfect pairing gives the correctly graded formula

\[
\operatorname{coker}\!\left(R_d\longrightarrow
  \bigoplus_{b\in B}(A_b)_d\right)^*
=
\left\{(F_b)\in\bigoplus_{b\in B}D_d(T_b):
              \sum_bF_b\in E_d\right\}.                 \tag{1}
\]

The former degree-two argument was invalid because its singleton obstruction
is (D_2(T)\cap E_2), which can have dimension three.

### Direct-basis global-symbol lemma

Suppose (V=\bigoplus_{b\in B}L_b).  Restrict the global degree-three
minus-symbol and degree-four plus-symbol to
(\bigoplus_{b\in B}D_d(T_b)).  Ordering the basis blocks first makes each
symbol block triangular after projecting to successive new factor
directions.  Its diagonal blocks are the full local symbols

\[
\beta_b^-:D_3(T_b)\longrightarrow
L_b\otimes\bigl(D_2(T_b)/(D_2(T_b)\cap E_2)\bigr),
\]

\[
\beta_b^+:D_4(T_b)\longrightarrow L_b\otimes D_3(T_b).
\]

The first is injective: a kernel cubic has all first derivatives in
(D_2(T_b)\cap E_2), hence belongs to
(D_3(T_b)\cap E_2^{(1)}=D_3(T_b)\cap E_3=0).  The second is injective by
full polarization in characteristic zero (equivalently, its first
derivatives determine a positive-degree form).  Thus the restricted global
symbols are injective.  Since their kernels are respectively the tuples
summing into (E_3) and (E_4), equation (1) shows that

\[
R_3\twoheadrightarrow\bigoplus_{b\in B}(A_b)_3,
\qquad
R_4\twoheadrightarrow\bigoplus_{b\in B}(A_b)_4.          \tag{2}
\]

In endpoint A, both targets have dimension (7\binom73=245); the cap
(\dim R_3+\dim R_4\le490) makes both maps isomorphisms.  The usual
fundamental-circuit multiplication argument then kills every outside cubic
component, contradicting singleton surjectivity, whose dual obstruction is
now correctly (D_3(T_t)\cap E_3=0).

In endpoint B, both targets have dimension
(7\cdot25+35=210); the cap (420) again makes both maps isomorphisms.
For an outside graph term (L_t=\{v+N_t(v):v\in L_0\}), the pairwise span
condition gives (\operatorname{rank}N_t\ge5).  Multiplication by low-block
linear codewords gives

\[
Wq=0,
\qquad W=\operatorname{im}N_t^*\subset(A_t)_1,
\qquad \dim W\ge5.                                    \tag{3}
\]

For the Boolean complete intersection
(A_t=k[e_1,\ldots,e_7]/(e_1^2,\ldots,e_7^2)), the quotient (A_t/(W))
has at most two degree-one generators, each represented by an original
square-zero generator.  Hence ((A_t/(W))_4=0), or

\[
W(A_t)_3=(A_t)_4.                                     \tag{4}
\]

For every (p\in(A_t)_3), equations (3)--(4) and the perfect pairing
((A_t)_3\times(A_t)_4\to(A_t)_7) yield

\[
\langle q,wp\rangle=\langle wq,p\rangle=0;
\]

therefore (q=0).  All outside cubic components vanish, again contradicting
the singleton surjectivity dual to (D_3(T_t)\cap E_3=0).

## 2. Sharp ordinary hyperplane residual

For every degree-(d) form (F),

\[
R_{\rm Chow}(F)\ge
1+\min_{0\ne\ell\in V^*}R_{\rm Chow}(F|_{\ell=0}).      \tag{5}
\]

Indeed, choose a factor (\ell) of one atom in an actual minimal
decomposition; restriction kills that atom.  Hence the exact missing lemma

\[
R_{\rm Chow}(\operatorname{perm}_7|_{\ell=0})\ge63
\quad\text{for every }\ell\ne0                          \tag{6}
\]

would prove rank (64).

The number (63) is sharp.  Restrict normalized Glynn's 64-term expression
to a hyperplane defined by a factor of one displayed term; exactly that term
dies, leaving 63 atoms.

## 3. Rigidity of the Glynn packet

Let (G) be the span of the normalized atoms
(T_\delta=\prod_cv_{\delta,c}), with
(v_{\delta,c}=\sum_r\delta_rx_{rc}),
(\delta\in\{\pm1\}^7), and (\delta_1=1).  Then

\[
\dim\bigl(G\cap\ell\operatorname{Sym}^6V^*\bigr)=
\begin{cases}
1,&\ell\text{ is proportional to a Glynn factor},\\
0,&\text{otherwise}.
\end{cases}                                             \tag{7}
\]

A linear divisor of a nonzero column-multihomogeneous element of (G) must
lie in one column.  Deleting that column leaves 64 independent tensors: a
64-by-64 coordinate minor is the Walsh character table, indexed by subsets
of (\{2,\ldots,7\}).  Modulo (\ell), their independence forces every
active column factor to be proportional to (\ell), and normalized sign
vectors are pairwise nonproportional.  This proves (7).

Consequently a Glynn-factor hyperplane leaves 63 linearly independent
displayed atoms, while (x_{77}=0) leaves all 64 displayed atoms linearly
independent.  This is packet rigidity, **not** a Chow-rank lower bound: an
unrelated decomposition with at most 62 atoms has not been excluded.

## 4. Exact barriers to simpler repairs

1. Any subadditive invariant with a uniform atom cap whose sublevel sets are
   Zariski closed automatically lower-bounds border Chow rank.  Ordinary-only
   information must therefore be nonclosed or decomposition-dependent.
2. The functional in (5) is not subadditive.  On disjoint variable spaces,
   (F_1=u(ab+cd)) and (F_2=v(ef+gh)) satisfy
   (h(F_1)=h(F_2)=1) but (h(F_1+F_2)=3).
3. Scalar derivative-annihilator residuals have atom cap
   (\binom7s) and target cap (\binom7s^2), so even optimally they prove
   only (1+\binom7s\le36).  Stacking scalar orders does not improve this.
4. The legal atom
   (\prod_c(\sum_rx_{rc})) projects in row multidegree
   ((1,\ldots,1)) to (\operatorname{perm}_7), defeating any method that
   sees only that projection.
5. For
   (T_\pm=\prod_c(x_{1c}\pm x_{2c})), each individual intersection
   (D_2(T_\pm)\cap E_2) is zero, but
   \[
   (x_{1a}+x_{2a})(x_{1b}+x_{2b})
   -(x_{1a}-x_{2a})(x_{1b}-x_{2b})
   =2(x_{1a}x_{2b}+x_{2a}x_{1b})
   \]
   gives 21 independent joint defect directions.  This pair is already a
   complete two-atom normal jet after choosing one plus-factor as normal
   coordinate.  Thus individual/pair defect charging cannot work.
6. Repeated factors such as (z^2y_1\cdots y_5) first appear in the second
   normal jet, so a first-jet-only formulation is not uniform.
7. The exact constructible decomposition-fiber detector is tautological at
   the target point; scalarizing it by Euler characteristic loses
   nonemptiness information (already on (\mathbb G_m)).

The full residual proofs and exact replay are in
[`../p64_ordinary_valuative_residual/report.md`](../p64_ordinary_valuative_residual/report.md)
and
[`../p64_ordinary_valuative_residual/residual_barrier_audit.py`](../p64_ordinary_valuative_residual/residual_barrier_audit.py).

## 5. Small-(n) gate

The unrestricted border Chow rank of (\operatorname{perm}_4) was not
resolved: the available interval remains (7\) to (8).  The cited rank-8
result of Han--Ju--Kim is row-tensor border rank, not unrestricted Chow
border rank; Ilten--Teitler only gives a lower bound greater than (4).
An exhaustive audit of all one-step Koszul--Chow wedges
(K_{m,p}), (1\le m\le4), (1\le p\le15), gives a ceiling at most seven
after complex bounds and Gorenstein transpose duality.  The exact replay is
[`../diagnostics/n4_second_koszul_gate.py`](../diagnostics/n4_second_koszul_gate.py).

Thus the small-(n) border gate does not currently bootstrap to the ordinary
rank-seven problem.  Resolving it would require classifying Laurent leading
identities and their osculating jets, or finding a genuinely coupled secant
equation.

## 6. Exact missing lemmas and final status

The branch is **solved for the corrected endpoint repair** and **stuck for
exact rank 64**.

The clean sufficient missing lemma is (6).  An equivalent two-part target is:

1. prove that the minimum hyperplane-section Chow rank is attained at a
   Glynn-factor hyperplane; and
2. prove that such a section has Chow rank exactly (63).

Any replacement must be at least as strong as a global, relation-valued,
cross-degree normal-jet theorem for every actual decomposition.  It must
handle repeated factors and correlated atoms; scalar derivative images,
row-transversal projections, local defect sums, and rigidity of only the
standard Glynn packet are insufficient.

## 7. Reproduction

The following exact checks pass:

```text
python results/perm7_theory_first_20260822/p64_ordinary_valuative_residual/residual_barrier_audit.py
python results/perm7_theory_first_20260822/diagnostics/n4_second_koszul_gate.py
python results/perm7_theory_first_20260822/valuative_tangent_cubic_centroid.py
```

No shared blueprint file was modified by this branch.
