# Quotient direction of the Packet-A Hessian witnesses

## Status

`EXACT DIRECTION THEOREM; THE W^all != 0 BRANCH IS NOT CLOSED.`

The forced Hessian witnesses do not define vectors that the rectangular
endpoint condition must kill in the middle quotient.  After the correct
complement and inverse-coefficient transport, they define nonzero covectors
of that quotient.  This distinction prevents a false closure of Packet A.

## 1. The labelled middle maps

Let

\[
 M_2=\bigoplus_{i=1}^{49}\bigoplus_{|I|=2}k e_{i,I},
 \qquad
 M_5=\bigoplus_{i=1}^{49}\bigoplus_{|J|=5}k f_{i,J}.
\]

Both spaces have dimension

\[
 m=49\binom72=1029.
\]

Write

\[
 B=A_2:M_2\longrightarrow \operatorname{Sym}^2(V)
\]

for the aggregate degree-two map, and let
`P:M_5 -> M_2` send a five-subset label to its complementary two-subset
label without erasing the term label.  If `D` is block diagonal with the
nonzero external coefficient `c_i` repeated 21 times, the input map in the
existing implementation is

\[
 C=DPA_5^{\mathsf T}:\operatorname{Sym}^5(V)^*\longrightarrow M_2.
\tag{1}
\]

Thus

\[
 K_2=\ker B\subset M_2,
 \qquad K_5=\ker A_5\subset M_5.
\]

The endpoint equality condition is

\[
 K_2=\ker B\subseteq\operatorname{im}C.
\tag{2}
\]

These are the directions implemented in
`n7_packet_a_general_operator.py`; reversing `D` changes the condition.

## 2. The quotient and its dual

Put

\[
 Q=M_2/\operatorname{im}C
\]

and use the labelled coordinate pairing to identify `M_2` with its dual.
Taking the transpose of (1) gives

\[
 C^{\mathsf T}=A_5P^{\mathsf T}D.
\]

Consequently the invertible map

\[
 J=D^{-1}P:M_5\longrightarrow M_2
\]

restricts to an isomorphism

\[
 J(K_5)=\ker C^{\mathsf T}
       =(\operatorname{im}C)^\perp
       \cong Q^*.
\tag{3}
\]

The familiar restricted relation matrix is exactly the evaluation pairing

\[
 K_2^{\mathsf T}J K_5
 =K_2^{\mathsf T}D^{-1}P K_5.
\tag{4}
\]

Equation (2) is equivalent to the vanishing of (4): every element of `K2`
already maps to zero in `Q`, so every quotient covector in `Q*`, including
those coming from `K5`, annihilates it.

This proves the direction theorem:

> A nonzero forced Hessian witness `w in K5` produces the nonzero quotient
> covector `Jw in Q*`.  The endpoint condition does not assert that `Jw`
> vanishes as a class in `Q`, nor is there a canonical identification
> `Q* -> Q` in the Packet-A data.

Treating `w` or `Jw` as a quotient vector that must lie in `im C` confuses the
middle space with the dual of its cokernel.  Forced Hessian alone therefore
does not give a non-disappearing quotient class that contradicts (2).

## 3. Dimensions imposed by a true 49-term permanent identity

For a genuine identity, the composite

\[
 BC=A_2DPA_5^{\mathsf T}
\]

is, up to harmless nonzero polarization scalars, the degree `5 -> 2`
catalectic map of `perm_7`.  Its image has one independent two-by-two
permanent for each choice of two remaining rows and two remaining columns.
The supports of different row/column choices are disjoint, so in
characteristic zero

\[
 \operatorname{rank}(BC)=\binom72^2=441.
\tag{5}
\]

Under the endpoint inclusion (2),

\[
 \operatorname{rank}(BC)
 =\operatorname{rank}C-\dim(\ker B)
 =\operatorname{rank}B+\operatorname{rank}C-m.
\]

Combining this with (5) yields

\[
 \operatorname{rank}B+\operatorname{rank}C=1029+441=1470
\]

and hence the exact kernel identity

\[
 \boxed{\dim K_2+\dim K_5=588.}
\tag{6}
\]

The completed Hessian witness space `W^all` is a subspace of `K5`.  Therefore
`W^all != 0` implies

\[
 \dim K_5\ge1,
 \qquad \operatorname{rank}C\le1028,
 \qquad \dim Q=\dim K_5\ge1.
\]

In particular, the `C`-surjective branch is impossible on `W^all != 0`.
However, (6) still permits

\[
 K_2=0,
 \qquad \dim K_5=588,
 \qquad \operatorname{rank}B=1029,
 \qquad \operatorname{rank}C=441.
\tag{7}
\]

In (7), the endpoint condition is vacuous and the quotient has dimension
588.  The nonzero Hessian covectors live naturally in its dual.  Neither the
matrix shapes nor the true permanent catalectic rank contradict this branch.

More generally, if the Hessian witnesses span an `s`-dimensional subspace of
`K5`, then (6) gives only

\[
 s\le \dim K_5\le588,
 \qquad \dim K_2=588-\dim K_5.
\]

It does not force `K2` to be nonzero unless one proves the additional bound
`dim K5<588` from permanent-specific equations.

## 4. Remaining theorem

The quotient route therefore precisely reduces, rather than closes, the
`W^all != 0` branch.  One must prove at least one genuinely new statement:

1. the full 49-term permanent equations force `dim K5<588`, hence `K2 != 0`,
   and then force a nonzero pairing contrary to (4); or
2. a permanent-specific construction produces a middle vector whose class
   in `Q` is nonzero but which endpoint equality requires to come from `K2`;
   or
3. the `K2=0`, `dim K5=588` locus in (7) is incompatible with the labelled
   gradient/Hessian equations for a reason stronger than dimensions.

Until one of these is established, nonzero `W^all`, endpoint equality, and a
nonzero quotient dual can coexist formally.  Packet A, the ordinary lower
bound 50, and all border-rank statements remain open on this branch.
