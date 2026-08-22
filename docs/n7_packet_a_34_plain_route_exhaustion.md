# Exhaustion of the plain Packet-A `3/4` route

## Status

`PLAIN LABELLED 3/4 KERNEL-IMAGE COUPLING IS AUTOMATIC; A REFINED KOSZUL OR CROSS-WEIGHT GATE IS REQUIRED.`

The ordinary labelled degree `3/4` analogue of the exhausted `2/5` interface
does not provide a new Packet-A obstruction.  Target containment and the
endpoint rank equality force its apolar-induction map to be surjective.

## 1. Labelled middle spaces and target rank

For 49 rank-seven terms, put

\[
 M_3=\bigoplus_{i=1}^{49}\bigoplus_{|I|=3}ke_{i,I},
 \qquad
 M_4=\bigoplus_{i=1}^{49}\bigoplus_{|J|=4}kf_{i,J}.
\]

Both middle spaces have dimension

\[
 m=49\binom73=49\cdot35=1715.
\tag{1}
\]

Let

\[
 A_3:M_3\longrightarrow\operatorname{Sym}^3(V),
 \qquad
 A_4:M_4\longrightarrow\operatorname{Sym}^4(V),
\]

and write

\[
 K_3=\ker A_3,\quad K_4=\ker A_4,
 \qquad k_3=\dim K_3,\quad k_4=\dim K_4.
\]

The complement map `P:M4 -> M3` sends a four-subset label to its complementary
three-subset label, preserving the term label.  The diagonal map `D` repeats
the nonzero external coefficient `c_i` on the 35 labels of term `i`.

For a true identity with `F=perm_7`, the labelled target composite is

\[
 \operatorname{Cat}_{4,3}(F)
 =A_3DPA_4^{\mathsf T},
\tag{2}
\]

up to one common nonzero polarization scalar.

The degree-three derivative space of the permanent has one independent
`3 x 3` permanent for each retained set of three rows and three columns.
Distinct row/column choices have disjoint monomial supports, hence

\[
 \operatorname{rank}\operatorname{Cat}_{4,3}(F)
 =\binom73^2=35^2=1225.
\tag{3}
\]

At the plain rectangular endpoint, the proposed rank equality is

\[
 \operatorname{rank}A_3+\operatorname{rank}A_4=2940.
\tag{4}
\]

Since both source spaces have dimension 1715, equation (4) is equivalent to

\[
\begin{aligned}
 k_3+k_4
 &=2\cdot1715-2940\\
 &=\boxed{490}.
\end{aligned}
\tag{5}
\]

Notice also that

\[
 2940=1715+1225,
\]

so (4) is exactly the equality case of the ordinary Sylvester rank inequality
for the target composite (2).

## 2. Cubic apolar induction

Let

\[
 F_3^\perp
 =\ker\left(
 \operatorname{Cat}_{3,4}(F):
 \operatorname{Sym}^3(V)^*\to\operatorname{Sym}^4(V)
 \right)
\]

be the cubic apolar space.  Since `dim V=49`,

\[
 \dim\operatorname{Sym}^3(V)^*
 =\binom{49+3-1}{3}
 =\binom{51}{3}
 =20825.
\]

Together with (3), this gives

\[
 \boxed{\dim F_3^\perp=20825-1225=19600.}
\tag{6}
\]

Define the cubic apolar-induction map

\[
 \Phi_3:F_3^\perp\longrightarrow K_4,
 \qquad
 \Phi_3=P^{\mathsf T}D A_3^{\mathsf T}|_{F_3^\perp}.
\tag{7}
\]

Transposing (2) shows

\[
 A_4\Phi_3(h)
 =\operatorname{Cat}_{4,3}(F)^{\mathsf T}h=0
\]

for `h in F3^perp`, so the codomain in (7) is correct.

## 3. The transpose kernel is already cubic-apolar

Equation (2) gives the target containment

\[
 E_3(F)=\operatorname{im}\operatorname{Cat}_{4,3}(F)
 \subseteq H_3:=\operatorname{im}A_3.
\]

Taking annihilators yields

\[
 \ker A_3^{\mathsf T}=H_3^\perp
 \subseteq E_3(F)^\perp=F_3^\perp.
\tag{8}
\]

Equivalently, if `A3^T h=0`, the transpose of the target composite gives

\[
 \operatorname{Cat}_{4,3}(F)^{\mathsf T}h
 =A_4P^{\mathsf T}D A_3^{\mathsf T}h=0.
\]

Because `P^T D` is invertible, equations (7) and (8) imply

\[
 \boxed{\ker\Phi_3=\ker A_3^{\mathsf T}.}
\tag{9}
\]

Now

\[
 \operatorname{rank}A_3=1715-k_3,
\]

and therefore

\[
\begin{aligned}
 \dim\ker\Phi_3
 &=20825-\operatorname{rank}A_3\\
 &=20825-(1715-k_3)\\
 &=\boxed{19110+k_3}.
\end{aligned}
\tag{10}
\]

Rank-nullity inside the 19600-dimensional apolar domain gives

\[
\begin{aligned}
 \operatorname{rank}\Phi_3
 &=19600-(19110+k_3)\\
 &=490-k_3.
\end{aligned}
\tag{11}
\]

Using the endpoint identity (5), equation (11) becomes

\[
 \boxed{\operatorname{rank}\Phi_3=k_4=\dim K_4.}
\tag{12}
\]

Since `im Phi3 subset K4`, equality (12) forces

\[
 \boxed{\operatorname{im}\Phi_3=K_4.}
\tag{13}
\]

Thus the plain cubic apolar induction is automatically surjective.

## 4. Consequence for the kernel-image condition

The corresponding middle input map is

\[
 C_3=DPA_4^{\mathsf T}.
\]

The ordinary Sylvester endpoint condition

\[
 \ker A_3\subseteq\operatorname{im}C_3
\]

is equivalent to the vanishing of the complementary `3/4` relation pairing,
or equivalently to surjectivity of `Phi3`.  Equation (13) shows that this
condition follows automatically from the target composite and the endpoint
rank equality.  It cannot serve as a new Packet-A gate.

This is the exact central-degree analogue of the exhausted `2/5` route.  The
larger cubic apolar space changes the dimensions but not the logic.

## 5. Required refined A-13 gate

A useful A-13 workstream must add structure not visible to the plain
catalectic factorization.  At least one of the following is required:

- a Koszul or recursive-Koszul wedge component whose rank-one normalization
  is not determined by (2)--(5);
- a Plucker relation among labelled factor subspaces that survives after the
  ordinary catalectic induction is quotiented out;
- a cross-torus-weight compatibility condition coupling several permanent
  target blocks through the same factor coordinates;
- another representation component not obtained by applying
  `P^T D A3^T` to cubic apolar operators.

Merely constructing the plain `M3/M4` maps, computing their kernels, and
checking `ker A3 subset im C3` will reproduce the automatic identity above.
It must not be reported as progress toward excluding Packet A.

Packet A, the ordinary lower bound 50, and every border-rank claim remain
unresolved pending a genuinely refined Koszul, Plucker, or cross-weight
degree `3/4` obstruction.
