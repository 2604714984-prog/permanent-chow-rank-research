# The apolar-surjectivity boundary for arbitrary Packet B

## Status and scope

`EXACT APOLAR REFORMULATION; TERMWISE ARRAY RIGIDITY OPEN.`

For a hypothetical 49-term Packet-B equality decomposition, the global
condition `ker B subset im C` is exactly the surjectivity of one restricted
degree-three apolar evaluation map.  Its rank, kernel, and cokernel are
computed below.  The map itself is an evaluation map; only its dual is a
transpose-evaluation map.  This reformulation does not prove that the 49 term
frames simultaneously split into the 35 common row-weight blocks.

## 1. The target apolar space

Let `V` have dimension 49, let

\[
 P=\operatorname{perm}_7\in\operatorname{Sym}^7V,
\]

and use divided-power contraction.  The middle target catalectic is

\[
 D=C_{3,4}(P):\operatorname{Sym}^3V^*
 \longrightarrow\operatorname{Sym}^4V.
 \tag{1.1}
\]

Its rank is

\[
 \operatorname{rank}D=\binom73^2=1225.
 \tag{1.2}
\]

Thus the source in the apolar reformulation is precisely the degree-three
piece of the apolar ideal,

\[
 I_3(P):=P^\perp_3=\ker C_{3,4}(P),
 \tag{1.3}
\]

not the degree-four apolar piece and not an ambient output cokernel.  Since

\[
 \dim\operatorname{Sym}^3V^*=\binom{51}{3}=20825,
\]

one has

\[
 \boxed{\dim I_3(P)=20825-1225=19600.}             \tag{1.4}
\]

## 2. Direction of the 49 term-frame maps

For term `i`, retain the formal four-subset labels

\[
 \widehat K_i=k\langle e_{i,I}:|I|=4\rangle
\]

and its seven labelled factors `ell_(i,0),...,ell_(i,6)`.  The incoming
formal map has coordinates

\[
 \widehat C_i(\theta)_I
 =\theta\!\left(\prod_{r\notin I}\ell_{i,r}\right).
 \tag{2.1}
\]

Thus a four-subset output label is paired with its complementary triple of
factor labels.  Passing to a minimal factorization of
`widehat B_i widehat C_i` gives a quotient map `pi_i` on
`im(widehat C_i)` and

\[
 C_i=\pi_i\widehat C_i:
 \operatorname{Sym}^3V^*\longrightarrow K_i.
 \tag{2.2}
\]

The three local middle types must not be conflated:

- for a rank-seven term, all 35 complementary-triple evaluations survive and
  `dim K_i=35`;
- for the rank-six `s=1` normal form, the 35 formal coordinates have incoming,
  outgoing, and composite rank 25, so `dim K_i=25`;
- for the rank-six `s=2` normal form, the incoming formal image has dimension
  29 and meets `ker(widehat B_i)` in dimension 4, leaving
  `dim K_i=25`.

In particular, an `s=2` block is not a 35-point evaluation block and is not
obtained by selecting 25 of the 35 formal labels.  Its four invisible
directions must first be quotiented intrinsically.

For the seven rank-six and 42 rank-seven terms, put

\[
 K=\bigoplus_iK_i,
 \qquad \dim K=7\cdot25+42\cdot35=1645,
 \]

and stack the maps in (2.2):

\[
 C=(C_1,\ldots,C_{49})^{\mathsf T}:
 \operatorname{Sym}^3V^*\longrightarrow K.
 \tag{2.3}
\]

The outgoing map is the sum of the local four-factor product maps,

\[
 B=[B_1\ \cdots\ B_{49}]:K\longrightarrow\operatorname{Sym}^4V.
 \tag{2.4}
\]

For a true permanent identity, `BC=D`.

## 3. Exact apolar-surjectivity theorem

Define the restricted stacked evaluation

\[
 E:=C|_{I_3(P)}:I_3(P)\longrightarrow\ker B.
 \tag{3.1}
\]

This direction is well-defined because `BC=D`: if `theta` lies in `I_3(P)`,
then `B(Ctheta)=Dtheta=0`.  Moreover,

\[
 \operatorname{im}E=\operatorname{im}C\cap\ker B. \tag{3.2}
\]

Indeed, one containment was just proved.  Conversely, if
`y=Ctheta` and `By=0`, then `Dtheta=BCtheta=0`, hence
`theta in I_3(P)` and `y=Etheta`.

It follows immediately that

\[
 \boxed{
 \ker B\subseteq\operatorname{im}C
 \quad\Longleftrightarrow\quad
 E:I_3(P)\twoheadrightarrow\ker B.}
 \tag{3.3}
\]

This is the exact apolar reformulation of the global extension condition.
The phrase "output relation space" in (3.3) means the relation space
`ker B` among the 1645 intrinsic middle directions.  It does not mean
`coker D` inside the 270725-dimensional ambient fourth symmetric power.

Write

\[
 b=\operatorname{rank}B,
 \qquad c=\operatorname{rank}C.
\]

Because `ker C subset ker D=I_3(P)`, the kernel of (3.1) is exactly
`ker C`.  Therefore

\[
 \operatorname{rank}E
 =19600-(20825-c)=c-1225.                          \tag{3.4}
\]

Since `dim ker B=1645-b`, its exact cokernel dimension is

\[
\begin{aligned}
 \dim\operatorname{coker}E
 &=(1645-b)-(c-1225)\\
 &=\boxed{2870-b-c}.
\end{aligned}                                      \tag{3.5}
\]

Thus (3.5) is the same nonnegative coupling defect as the global extension
defect.  Surjectivity is equivalent to `b+c=2870`.  On that locus the exact
sequence is

\[
 0\longrightarrow\ker C\longrightarrow I_3(P)
 \xrightarrow{\ E\ }\ker B\longrightarrow0,       \tag{3.6}
\]

and the sharp kernel threshold can be written in either form

\[
 \boxed{
 \dim\ker E=20825-c=19600-(1645-b)=17955+b.}
 \tag{3.7}
\]

Equations (3.4)--(3.7) are identities, not parameter counts for a component
of the Chow-decomposition locus.

## 4. Evaluation versus transpose evaluation

In the formal term labels, (3.1) sends a cubic differential `theta` to the
49 arrays

\[
 \left(
 \pi_i\bigl(
   \theta(\ell_{i,r}\ell_{i,s}\ell_{i,t})
 \bigr)_{\{r,s,t\}}
 \right)_{i=1}^{49},                               \tag{4.1}
\]

subject to the fact that the resulting middle vector lies in `ker B`.
This is a stacked term-frame evaluation map.

Its dual

\[
 E^{\mathsf T}:(\ker B)^*\longrightarrow I_3(P)^*
 \tag{4.2}
\]

is the transpose-evaluation map.  Therefore (3.3) is equivalently the
injectivity of (4.2), not the surjectivity of a transpose map in the same
direction.  Calling (3.1) itself a transpose evaluation reverses the
intrinsic source and target, exactly the kind of quotient-direction error
that occurs in the Packet-A endpoint analysis.

## 5. The remaining array-rigidity theorem

The apolar formulation turns the missing synchronization statement into a
concrete structured-array problem.  One must classify the 49 collections of
triple products in (4.1), including the two rank-six quotient types, under
the simultaneous constraints

\[
 \sum_iB_iC_i=C_{3,4}(P)
 \quad\hbox{and}\quad
 E:I_3(P)\twoheadrightarrow\ker B.                \tag{5.1}
\]

A sufficient theorem would say that every product-frame array satisfying
(5.1), up to factor permutations and product-preserving rescalings, admits a
single row-torus grading in which:

1. the 42 quotient frames are monomial relative to one common frame;
2. every graph map is supported on its matching row blocks;
3. the seven nonzero diagonal tails of each graph term define one projective
   point, compatibly across the complementary triple/four-subset labels.

Equivalently, this is a large simultaneous diagonalization or identifiability
statement for the structured evaluation arrays (4.1).  Abstract surjectivity
alone cannot supply it: (3.6) is invariant under arbitrary independent basis
changes of the `K_i`, whereas the three conclusions above concern the actual
factor-product realization of those spaces.  The permanent composite in
(5.1) and the Chow product structure must be used essentially.

The existing low-layer slice survivors show only that selected projected
target equations and local equality do not force this diagonalization.  They
do not satisfy the complete 49-term system (5.1), so they neither prove nor
disprove the required array-rigidity theorem.

The exact current boundary is therefore:

```text
global Sylvester equality
    = surjectivity I_3(perm_7) -> ker B
    = injectivity of its dual transpose-evaluation map;

common-code reduction
    requires an additional structured-array simultaneous-diagonalization
    theorem and remains open.
```
