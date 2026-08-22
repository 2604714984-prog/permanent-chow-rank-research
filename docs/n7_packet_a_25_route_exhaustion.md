# Exhaustion of the Packet-A `2/5` route

## Status

`DECISIVE NEGATIVE RESULT: THE 2/5 ENDPOINT CONDITION IS AUTOMATIC AFTER TARGET CONTAINMENT AND ENDPOINT DIMENSION EQUALITY.`

The previously proposed `>196` array-rigidity contradiction is wrong and is
withdrawn.  For every true target identity, the relevant kernel has dimension
exactly `196+dim K2`; it is therefore strictly greater than 196 on the
remaining `K2 != 0` branch.  This is forced by the target, not a pathology to
exclude.

## 1. Labelled maps and the target composite

Let

\[
 M_2=\bigoplus_{i=1}^{49}\bigoplus_{|I|=2}ke_{i,I},
 \qquad
 M_5=\bigoplus_{i=1}^{49}\bigoplus_{|J|=5}kf_{i,J},
\]

so

\[
 \dim M_2=\dim M_5=49\binom72=1029.
\]

Write

\[
 A_2:M_2\longrightarrow\operatorname{Sym}^2(V),
 \qquad
 A_5:M_5\longrightarrow\operatorname{Sym}^5(V),
\]

and put

\[
 K_2=\ker A_2,
 \qquad K_5=\ker A_5,
 \qquad k_d=\dim K_d.
\]

The complement map `P:M5 -> M2` sends a five-subset label to its complementary
two-subset label while preserving its term label.  The diagonal map `D` has
the nonzero external coefficient `c_i` on the 21 labels of term `i`.

For a true identity with target `F=perm_7`, the labelled factorization of its
`5 -> 2` catalectic is

\[
 \operatorname{Cat}_{5,2}(F)
 =A_2DPA_5^{\mathsf T},
\tag{1}
\]

up to one common nonzero polarization scalar, which has no effect on images,
kernels, or ranks.

## 2. Target containment forces `ker A2^T subset F2^perp`

Let

\[
 E_2(F)=\operatorname{im}\operatorname{Cat}_{5,2}(F)
\]

be the degree-two derivative space and let

\[
 H_2=\operatorname{im}A_2.
\]

Equation (1) immediately gives

\[
 E_2(F)\subseteq H_2.
\tag{2}
\]

Equivalently, the same inclusion follows from `E6(F) subset H6`: differentiate
the six-factor target containment four more times, observing that every
fourth derivative of a six-factor product is a linear combination of its
two-factor subproducts.

The quadratic apolar space is the annihilator of the degree-two derivative
space:

\[
 F_2^\perp=E_2(F)^\perp.
\]

Taking annihilators in (2) proves

\[
 \boxed{
 \ker A_2^{\mathsf T}=H_2^\perp
 \subseteq E_2(F)^\perp=F_2^\perp.}
\tag{3}
\]

There is also a direct matrix proof.  If `A2^T h=0`, transpose (1) to obtain

\[
 \operatorname{Cat}_{5,2}(F)^{\mathsf T}h
 =A_5P^{\mathsf T}D A_2^{\mathsf T}h=0.
\]

Thus `h` is quadratic-apolar to `F`, which is exactly (3).

## 3. Exact kernel and rank of apolar induction

The apolar-induction map is

\[
 \Phi:F_2^\perp\longrightarrow K_5,
 \qquad
 \Phi=P^{\mathsf T}D A_2^{\mathsf T}|_{F_2^\perp}.
\]

Because `P^T D` is invertible,

\[
 \ker\Phi=F_2^\perp\cap\ker A_2^{\mathsf T}.
\]

In view of (3), this intersection is not a smaller transverse kernel.  It is
the complete transpose kernel:

\[
 \boxed{\ker\Phi=\ker A_2^{\mathsf T}.}
\tag{4}
\]

Now

\[
 \dim\operatorname{Sym}^2(V)=\binom{49+1}{2}=1225
\]

and

\[
 \operatorname{rank}A_2=1029-k_2.
\]

Therefore

\[
\begin{aligned}
 \dim\ker\Phi
 &=1225-\operatorname{rank}A_2\\
 &=1225-(1029-k_2)\\
 &=\boxed{196+k_2}.
\end{aligned}
\tag{5}
\]

The permanent quadratic apolar space has dimension

\[
 \dim F_2^\perp=1225-\binom72^2=1225-441=784.
\]

Rank-nullity and (5) give

\[
\begin{aligned}
 \operatorname{rank}\Phi
 &=784-(196+k_2)\\
 &=\boxed{588-k_2}.
\end{aligned}
\tag{6}
\]

These identities use the true target containment but do not use a genericity
assumption, random frame, or row-separated model.

## 4. Endpoint equality makes `Phi` automatically surjective

At the rectangular endpoint, the exact dimension equality is

\[
 k_2+k_5=588.
\tag{7}
\]

Combining (6) and (7) yields

\[
 \operatorname{rank}\Phi=588-k_2=k_5=\dim K_5.
\]

The target composite already proves `im Phi subset K5`.  Equality of
dimensions therefore forces

\[
 \boxed{\operatorname{im}\Phi=K_5.}
\tag{8}
\]

The transverse obstruction was identified as

\[
 \mathcal O_{2/5}\cong K_5/\operatorname{im}\Phi.
\]

Equation (8) proves

\[
 \boxed{\mathcal O_{2/5}=0}
\tag{9}
\]

automatically for every true target identity satisfying the endpoint
dimension equality.

In the remaining branch `k2>0`, equation (5) says

\[
 \dim\ker\Phi=196+k_2>196.
\]

Thus the earlier proposal to prove

\[
 \dim(F_2^\perp\cap\ker A_2^{\mathsf T})\le196
\]

has the inequality in the wrong direction.  It is not an open lemma and must
not be used as a Packet-A gate.  The row-separated controls merely exhibited
one visible instance of a kernel whose largeness is in fact forced generally
by (3).

## 5. Consequence for the research route

The `2/5` interface has now been exhausted:

- the Hessian-generated `K5` relations pair trivially with `K2` by a
  derivative tautology;
- all other `K5` relations are reached by quadratic apolar induction once
  the endpoint dimension equality holds;
- the quotient obstruction `O_(2/5)` therefore vanishes automatically.

No additional `2/5` torus block, apolar quadratic subspace, or transverse
syzygy can contradict the same endpoint without adding genuinely new
information outside this interface.

The next required workstream is **A-13: the labelled degree `3/4` coupled
module**.  It must retain term labels, the correct complementary coefficient
transport, the permanent target composite, and cross-block compatibility.
This is the first central degree not consumed by the automatic argument
above.

Packet A, the ordinary lower bound 50, and every border-rank claim remain
unresolved until the degree `3/4` endpoint is excluded or an exact survivor is
classified.
