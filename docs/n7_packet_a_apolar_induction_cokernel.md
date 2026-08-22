# The Packet-A transverse obstruction as an apolar-induction cokernel

## Status

`EXACT REFORMULATION; ONE ARRAY-RIGIDITY LEMMA REMAINS.`

The transverse `2/5` obstruction is canonically the cokernel of a map that
induces degree-five factor relations from quadratic apolar operators of the
permanent.  At the endpoint, surjectivity of this map forces an unexpectedly
large kernel.  Excluding that kernel is now the unique remaining Packet-A
rigidity problem.

## 1. Maps and coefficient direction

Let

\[
 M_2=\bigoplus_{i=1}^{49}\bigoplus_{|I|=2}ke_{i,I},
 \qquad
 M_5=\bigoplus_{i=1}^{49}\bigoplus_{|J|=5}kf_{i,J},
\]

both of dimension 1029.  The aggregate maps are

\[
 A_2:M_2\longrightarrow\operatorname{Sym}^2(V),
 \qquad
 A_5:M_5\longrightarrow\operatorname{Sym}^5(V).
\]

The complement permutation

\[
 P:M_5\longrightarrow M_2
\]

sends `(i,hat{r,s})` to `(i,{r,s})`.  Let `D` be diagonal with the nonzero
external coefficient `c_i` repeated on the 21 labels of term `i`.  The
middle input map and the inverse-coefficient identification are

\[
 C=DPA_5^{\mathsf T},
 \qquad
 J=D^{-1}P:M_5\longrightarrow M_2.
\]

Thus

\[
 J^{-1}=P^{\mathsf T}D.
\tag{1}
\]

The order in (1) is forced: `D` first restores the external coefficient on a
two-label, and `P^T` then returns it to the complementary five-label.

## 2. Quadratic apolar induction

Put `F=perm_7` and let

\[
 F_2^\perp
 =\{h\in\operatorname{Sym}^2(V)^*:h\mathbin{\lrcorner}F=0\}
\]

be the quadratic apolar space.  Define

\[
 \Phi:F_2^\perp\longrightarrow M_5,
 \qquad
 \Phi(h)=P^{\mathsf T}D A_2^{\mathsf T}h.
\tag{2}
\]

For a true decomposition of `F`, the composite

\[
 A_2DPA_5^{\mathsf T}
\]

is the `5 -> 2` catalectic map of `F`, up to one harmless nonzero
polarization scalar.  Therefore

\[
\begin{aligned}
 A_5\Phi(h)
 &=A_5P^{\mathsf T}D A_2^{\mathsf T}h\\
 &=(A_2DPA_5^{\mathsf T})^{\mathsf T}h\\
 &=h\mathbin{\lrcorner}F=0.
\end{aligned}
\]

Hence

\[
 \boxed{\Phi(F_2^\perp)\subseteq K_5.}
\tag{3}
\]

Since `P^T D` is invertible, (2) also gives

\[
 \boxed{\ker\Phi=F_2^\perp\cap\ker A_2^{\mathsf T}.}
\tag{4}
\]

In factor coordinates, (4) says that `h` lies in the kernel precisely when

\[
 h(\ell_{i,r}\ell_{i,s})=0
 \qquad\text{for every }i\text{ and }r<s.
\tag{5}
\]

Thus the kernel consists of permanent-apolar quadratic operators whose
off-diagonal factor-pair evaluations vanish on all 49 factor frames.

## 3. The transverse obstruction is `coker Phi`

Recall the transverse obstruction

\[
 \mathcal O_{2/5}
 =\operatorname{im}\left(
 K_5\xrightarrow{J}M_2
 \longrightarrow M_2/\operatorname{im}A_2^{\mathsf T}
 \right).
\]

The kernel of this map on `K5` is

\[
\begin{aligned}
 \{z\in K_5:Jz\in\operatorname{im}A_2^{\mathsf T}\}
 &=K_5\cap J^{-1}(\operatorname{im}A_2^{\mathsf T})\\
 &=K_5\cap P^{\mathsf T}D A_2^{\mathsf T}
   (\operatorname{Sym}^2(V)^*).
\end{aligned}
\]

If `z=P^T D A2^T h` belongs to `K5`, then

\[
 0=A_5z=(A_2DPA_5^{\mathsf T})^{\mathsf T}h
   =h\mathbin{\lrcorner}F,
\]

so `h` automatically belongs to `F2^perp`.  The displayed kernel is therefore
exactly `im Phi`, and the first isomorphism theorem gives

\[
 \boxed{\mathcal O_{2/5}\cong K_5/\operatorname{im}\Phi
 =\operatorname{coker}\Phi.}
\tag{6}
\]

Consequently the rectangular endpoint condition is equivalent to

\[
 \boxed{\Phi:F_2^\perp\longrightarrow K_5\text{ is surjective}.}
\tag{7}
\]

The 196 same-row Hessian witnesses are the images under `Phi` of the
row-internal quadratic apolar operators.  Their automatic pairing vanishing
is therefore the first visible part of the induction image, not an endpoint
obstruction.

## 4. Explicit direct-sum basis of `F2^perp`

Write `partial_(u,b)` for differentiation by `x_(u,b)`.  The following three
families have disjoint leading monomial supports and form a direct sum.

### Row-internal family: dimension 196

\[
 \mathcal R
 =\left\langle
 \partial_{u,b}\partial_{u,d}:
 0\le u\le6,\ 0\le b\le d\le6
 \right\rangle.
\]

There are

\[
 7\binom{7+1}{2}=7\cdot28=196
\]

operators.  They annihilate the permanent because each monomial uses one
variable from each row.

### New column-internal family: dimension 147

\[
 \mathcal C
 =\left\langle
 \partial_{u,b}\partial_{v,b}:
 0\le u<v\le6,\ 0\le b\le6
 \right\rangle.
\]

The same-variable operators already occur in `R`, so this additional family
contains only distinct rows.  Its dimension is

\[
 \binom72\,7=21\cdot7=147.
\]

It annihilates the permanent because a permanent monomial uses each column
once.

### Rectangle-difference family: dimension 441

\[
 \mathcal X
 =\left\langle
 \partial_{u,b}\partial_{v,d}
 -\partial_{u,d}\partial_{v,b}:
 u<v,\ b<d
 \right\rangle.
\]

Both derivatives in a generator leave the same `5 x 5` permanent, obtained
by deleting rows `{u,v}` and columns `{b,d}`, so their difference annihilates
`F`.  There are

\[
 \binom72^2=21^2=441
\]

independent rectangle differences.

Every remaining quadratic differential has distinct rows and distinct
columns.  For each row pair and column pair, the two rectangle matchings have
the same catalectic image; one difference belongs to `X` and one complementary
direction maps to the corresponding nonzero `5 x 5` permanent.  Those 441
permanents have disjoint monomial supports.  Therefore

\[
 F_2^\perp=\mathcal R\oplus\mathcal C\oplus\mathcal X
\]

and

\[
 \boxed{\dim F_2^\perp=196+147+441=784.}
\tag{8}
\]

## 5. Endpoint kernel threshold

The preceding Packet-A branches prove that every remaining candidate has

\[
 K_2\ne0,\qquad K_5\ne0,
 \qquad \dim K_2+\dim K_5=588.
\tag{9}
\]

If the endpoint condition holds, (7) and rank-nullity give

\[
\begin{aligned}
 \dim\ker\Phi
 &=784-\dim K_5\\
 &=784-(588-\dim K_2)\\
 &=196+\dim K_2\\
 &>196.
\end{aligned}
\tag{10}
\]

Thus endpoint equality requires a subspace of dimension strictly greater than
196 in `F2^perp` whose every element satisfies all evaluations (5).  Here 196
is the dimension of the explicit row-internal summand `R`; this comparison is
only a threshold, not an assertion that `R` itself lies in `ker Phi`.

## 6. Unique remaining array-rigidity lemma

The exact final statement needed to close Packet A is now:

> **Permanent-apolar array-rigidity lemma.** For a non-row-separated packet of
> 49 rank-seven factor frames satisfying the surviving permanent
> gradient/Hessian equations and the simple-multilinear endpoint hypotheses,
> \[
> \dim\left(F_2^\perp\cap\ker A_2^{\mathsf T}\right)\le196.
> \]

Equivalently, there is no subspace of dimension greater than 196 among the
784 explicit permanent-apolar quadrics in `R direct-sum C direct-sum X` whose
off-diagonal factor-pair evaluations all vanish on all 49 frames.

The row-separated alternative has already been excluded by the tensor-rank
lower bound for `perm_7`.  No proof of the array-rigidity lemma is presently
known from the existing Packet-A interfaces.  It is not a dimension-only
statement: the evaluation map has 1029 target coordinates, but its entries
are coupled products from the same 49 seven-factor frames.

Proving the lemma would contradict (10) and close the remaining ordinary
Packet-A endpoint.  Until then, Packet A, the ordinary lower bound 50, and all
border-rank claims remain unresolved.
