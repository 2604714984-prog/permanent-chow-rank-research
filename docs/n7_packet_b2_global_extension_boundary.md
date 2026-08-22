# The global-extension boundary for arbitrary Packet B

## Status and scope

`PROVED GLOBAL LINEAR-ALGEBRA BOUNDARY; COMMON-CODE REDUCTION OPEN.`

This note records exactly what the full rectangular Sylvester equality forces
for an arbitrary mixed Packet B.  It also explains why the 35-block
common-code argument is not defined before a separate termwise synchronization
theorem.  No common-code theorem, full mixed counterexample, lower-50 result,
or border-rank statement is proved here.

## 1. The intrinsic maps

Retain all term labels and let

\[
 K=\bigoplus_{i=1}^{49}K_i,
 \qquad \dim K=7\cdot25+42\cdot35=1645.
\]

The minimal rectangular factorizations give

\[
 C:H_3^*\longrightarrow K,
 \qquad B:K\longrightarrow H_4,
 \qquad D:=BC.
\]

For a hypothetical 49-term equality packet for `perm_7`, the composite is the
middle permanent catalectic and

\[
 \operatorname{rank}D=1225.                       \tag{1.1}
\]

No common graph, point code, row-subset grading, or identification among the
42 rank-seven middle spaces is assumed.

## 2. The global extension theorem

There is always a well-defined surjection

\[
 \overline B:K/\operatorname{im}C
 \longrightarrow \operatorname{im}B/\operatorname{im}D,
 \qquad [k]\longmapsto[Bk].                       \tag{2.1}
\]

It is well-defined because

\[
 B(\operatorname{im}C)=\operatorname{im}(BC)=\operatorname{im}D.
\]

Moreover,

\[
 \ker\overline B
 =B^{-1}(\operatorname{im}D)/\operatorname{im}C
 =(\ker B+\operatorname{im}C)/\operatorname{im}C.\tag{2.2}
\]

Indeed, if `Bk=Dtheta=B(Ctheta)`, then `k-Ctheta` lies in `ker B`, proving the
second equality in (2.2).  Consequently the following statements are
equivalent:

1. `ker B subset im C`;
2. the map (2.1) is an isomorphism;
3. the restriction of `B` gives a short exact sequence

   \[
   0\longrightarrow\ker B\longrightarrow\operatorname{im}C
   \xrightarrow{\ B\ }\operatorname{im}D\longrightarrow0;
   \tag{2.3}
   \]

4. the rank equality

   \[
   \operatorname{rank}B+\operatorname{rank}C
   =\dim K+\operatorname{rank}D                 \tag{2.4}
   \]

   holds.

For completeness, the defect in (2.4) is exactly

\[
\begin{aligned}
 &\dim K-\operatorname{rank}B-\operatorname{rank}C
   +\operatorname{rank}D\\
 &=\dim\ker B-
   \dim(\ker B\cap\operatorname{im}C)\\
 &=\dim\bigl(\ker B/(\ker B\cap\operatorname{im}C)\bigr).
                                                               \tag{2.5}
\end{aligned}
\]

Thus (2.4) is equivalent to the vanishing of this nonnegative dimension and
hence to item 1.  Under equality, (2.1) supplies the second canonical exact
description

\[
 K/\operatorname{im}C
 \simeq\operatorname{im}B/\operatorname{im}D.      \tag{2.6}
\]

In the Packet-B dimensions, (1.1), (2.4), and `dim K=1645` give

\[
 \operatorname{rank}B+\operatorname{rank}C=2870.  \tag{2.7}
\]

Equations (2.3) and (2.6) are the complete synchronization data forced by
Sylvester equality at the level of abstract linear algebra.  They are global:
neither exact sequence splits canonically across the 49 summands `K_i`.

## 3. Why the 35 blocks are not yet defined

In a common-graph packet, every rank-seven term has one factor in each fixed
row direction.  Its degree-three and degree-four products are homogeneous for
the row torus, and complementary row subsets index 35 common weight blocks.
The matrices in each block can then be written as degree-three and degree-four
evaluation codes.

An arbitrary graph complement has an independent quotient frame

\[
 q_{t,0},\ldots,q_{t,6}
\]

and an independent graph map

\[
 A_t:Q\longrightarrow U_0\oplus\cdots\oplus U_6.
\]

A nonmonomial quotient frame mixes diagonal row weights.  An off-block graph
component mixes the corresponding `U_i` weights.  Products of these factors
are therefore sums of several row weights, and the local middle space `K_t`
does not carry the common 35-block decomposition used by the point-code
model.

The permanent identity makes the composite image `im D` stable under the
permanent row torus.  It does not imply that the larger space `im B` is torus
stable, that `im C` has a compatible torus action, or that the decomposition
`K=direct-sum K_i` is preserved term by term.  Without those facts,
`im B/im D` is not a quotient torus representation and (2.6) cannot be split
by torus weights.  Characteristic-zero semisimplicity cannot be invoked before
the relevant torus modules have actually been constructed.

Accordingly, "simultaneous equality in all 35 blocks" is not a valid premise
for an arbitrary mixed packet.  It becomes meaningful only after proving the
termwise row-weight structure which it is intended to deduce.

## 4. The missing theorem

A valid common-code reduction needs an additional identifiability or
torus-compatible termwise-splitting lemma.  At minimum it must prove, from the
permanent identity together with (2.3), that:

1. the target row torus acts compatibly on the lifts `im C`, `K`, and `im B`;
2. this action preserves each relevant term summand `K_t`, up to the finite
   factor relabellings and scalings allowed for a Chow product;
3. the induced weight decomposition gives one factor line in every row and
   transports the local degree-three/four relations consistently across
   overlapping complementary subsets;
4. the transported data force monomial quotient frames, block-diagonal graph
   maps, and one common projective tail per graph term, or produce a proved
   finite list of exceptional extension types.

One possible route to item 2 would be identifiability of the 49-term Chow
decomposition modulo the standard gauges.  The connected target torus could
then not move a finite set of labelled terms except by their allowed scalings.
However, the rectangular condition `ker B subset im C` is a statement about
the catalectic extension (2.3), not about the tangent space or dimension of the
fiber of the Chow-sum parameterization.  No implication from (2.3) to such
identifiability is currently proved.

Therefore the missing lemma is substantive; it is not a choice of basis or a
normalization.

## 5. What the low-layer survivors do and do not show

The exact quotient-shear and transposition-slice controls show that the
quotient identity, the zero `U1 Q6` layer, selected `U2 Q5` transposition
targets, and even a local unprojected Sylvester equality can coexist with
nonmonomial quotient frames.  They invalidate attempts to infer common-code
synchronization from those local conditions alone.

Those controls contain two or four graph terms in restricted variable slices.
They are not 42-complement packets, do not realize the complete permanent
identity, and do not satisfy the global ranks (1.1) and (2.7).  Hence they are
not counterexamples to a future theorem which uses the full mixed equality
system.  Conversely, they prevent the local block heuristics from being
promoted to such a theorem without the missing global splitting argument.

The correct current conclusion is therefore:

```text
B2-M1/M2: intrinsic variables and residual moduli identified.
B2-M3: global extension (2.3) and quotient isomorphism (2.6) proved.
B2-M4: common-code reduction neither proved nor exactly falsified on the
       complete mixed equality locus.
```
