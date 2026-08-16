# Iterated product shadows and nonzero block projection

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_REPLAYED`, `GENERAL_N_PROGRESS`.

This note extends the exact simultaneous product-shadow theorem from first
derivatives to every derivative order.  It then combines the higher-shadow
intersection cap with a linear block-projection lemma.  The resulting ordinary
characteristic-zero bounds are

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge45,}
\]

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_8)\ge79.}
\]

The theorem does not determine either rank exactly, change the current
`perm_6` status, imply a border-rank bound, or prove the general Glynn
conjecture.  Literature novelty has not been established.

## 1. Arbitrary-order product shadows

Fix

\[
1\le a<m<n
\]

and put

\[
E_m=\mathcal D_m(\operatorname{perm}_n).
\]

The standard basis is

\[
\left\{
 p_{R,C}:R,C\in\binom{[n]}m
\right\}.
\]

For a coordinate family

\[
\mathcal A\subseteq
\binom{[n]}m\times\binom{[n]}m,
\]

its order-`a` derivative space is indexed by the simultaneous lower shadow

\[
\partial_\times^a\mathcal A
=
\left\{
(I,J):
\begin{array}{l}
I,J\in\binom{[n]}{m-a},\\
I\subset R,\ J\subset C
\text{ for some }(R,C)\in\mathcal A
\end{array}
\right\}.
\tag{1.1}
\]

Define

\[
F^{(a)}_{n,m}(b)
=
\min_{\substack{S\subseteq E_m\\\dim S=b}}
\dim\partial^aS.
\tag{1.2}
\]

## 2. Coordinate specialization

### Proposition 2.1

Every `b`-plane `S subset E_m` specializes under the row-column diagonal
torus to a coordinate `b`-plane `S_0` satisfying

\[
\dim\partial^aS_0\le\dim\partial^aS.
\tag{2.1}
\]

### Proof

The subpermanent basis consists of pairwise distinct torus weights.  The
closure of the orbit of `[S]` in the complete Grassmannian contains a
torus-fixed coordinate point.  Order-`a` differentiation is the image of a
map from the tautological bundle tensored with
`Sym^a(V_n^*)`; matrix rank cannot increase under specialization. ∎

## 3. Two-sided higher colex compression

Put

\[
q=\binom nm
\]

and list the `m`-subsets in colex order:

\[
A_0,A_1,\ldots,A_{q-1}.
\]

For `0<=t<=q`, let

\[
k^{(a)}_{n,m}(t)
=
\left|
\partial^a\{A_0,\ldots,A_{t-1}\}
\right|.
\tag{3.1}
\]

The iterated Kruskal--Katona theorem says that a colex initial segment
minimizes every lower shadow, and its order-`a` shadow is again a colex
initial segment.

Apply colex compression to every row fiber of a coordinate product family.
For a fixed lower row set, the column-shadow fiber before compression is a
union of order-`a` shadows.  Its size is at least the maximum of the
corresponding `k^(a)` values.  After compression those shadows are nested
colex initial segments, so the union has exactly that maximum.  Hence the
first compression does not increase the simultaneous shadow.

Apply the symmetric compression to the column fibers.  The first compression
makes the column heights nonincreasing, so the second operation produces a
Ferrers family

\[
\mathcal A_\lambda
=
\{(i,j):0\le i<q,\ 0\le j<\lambda_i\}
\tag{3.2}
\]

with

\[
q\ge\lambda_0\ge\cdots\ge\lambda_{q-1}\ge0,
\qquad
\sum_i\lambda_i=b.
\tag{3.3}
\]

## 4. Exact higher-shadow objective

For a lower set

\[
I\in\binom{[n]}{m-a},
\]

let `f_a(I)` be the least colex index of an `m`-set containing `I`, and put

\[
w_i^{(a)}
=
|\{I:f_a(I)=i\}|.
\tag{4.1}
\]

If

\[
c_i=\min([n]\setminus A_i)
\]

under zero-based indexing, then

\[
\boxed{w_i^{(a)}=\binom{c_i}{a}.}
\tag{4.2}
\]

Indeed, `A_i` contains every integer below `c_i`.  A lower set first contained
in `A_i` is obtained by deleting an `a`-subset of
`{0,...,c_i-1}`; conversely every such deletion has `A_i` as its first colex
container.

For the Ferrers family, the lower-column fiber over `I` has size

\[
k^{(a)}_{n,m}(\lambda_{f_a(I)}).
\]

Therefore:

### Theorem 4.1 -- exact iterated product shadow

\[
\boxed{
F^{(a)}_{n,m}(b)
=
\min_{\substack{
q\ge\lambda_0\ge\cdots\ge\lambda_{q-1}\ge0\\
\sum_i\lambda_i=b}}
\sum_{i=0}^{q-1}
\binom{c_i}{a}
 k^{(a)}_{n,m}(\lambda_i).
}
\tag{4.3}
\]

### Proof

Proposition 2.1 and the two compressions prove that the right side is no
larger than the derivative dimension of an arbitrary subspace.  Formula
(4.2) computes each Ferrers shadow exactly.  Conversely every partition in
(4.3) defines a coordinate Ferrers plane attaining its displayed value. ∎

The same integer recurrence as in the first-shadow theorem computes (4.3):

\[
D(i,u,s)
=
\min_x
\left\{
\binom{c_i}{a}k^{(a)}_{n,m}(x)
+D(i+1,x,s-x)
\right\}.
\tag{4.4}
\]

## 5. Exact intersection cap for a block of Chow terms

Let

\[
d\ge2
\]

and let `T_1,...,T_s` be degree-`n` Chow terms.  Set

\[
E=\mathcal D_d(\operatorname{perm}_n),
\qquad
U_I=\sum_{i=1}^s\mathcal D_d(T_i).
\]

For every

\[
A\subseteq E\cap U_I
\]

and every `1<=a<d`,

\[
\partial^aA
\subseteq
\sum_{i=1}^s\mathcal D_{d-a}(T_i).
\]

One Chow term has degree-`d-a` derivative dimension at most

\[
\binom n{d-a}.
\]

Hence

\[
F^{(a)}_{n,d}(\dim A)
\le
s\binom n{d-a}.
\tag{5.1}
\]

Define

\[
\beta_{n,d}(s)
=
\min_{1\le a<d}
\max\left\{
 b:F^{(a)}_{n,d}(b)
 \le s\binom n{d-a}
\right\}.
\tag{5.2}
\]

Then

\[
\boxed{
\dim\left(
E\cap\sum_{i=1}^s\mathcal D_d(T_i)
\right)
\le\beta_{n,d}(s).
}
\tag{5.3}
\]

This includes the pre-existing zero-intersection theorem as the special case
in which the right side is zero, but it retains a sharp nonzero defect when a
block is larger.

## 6. Projection away from a nonzero-intersection block

Let `F_i subseteq W` be arbitrary linear spaces, let `E subseteq W`, and put

\[
U=\sum_{i=1}^qF_i.
\]

Fix a label block `I subset [q]`.  Let

\[
A=E\cap U.
\]

Choose a linear section

\[
\tau:A\longrightarrow\bigoplus_{i=1}^qF_i
\]

of the summation map.  Project `tau` to the components outside `I`.  The
kernel maps under summation into

\[
E\cap\sum_{i\in I}F_i.
\]

Because `tau` is a section, that map is injective.  Thus:

### Lemma 6.1 -- block projection

\[
\boxed{
\dim(E\cap U)
\le
\sum_{i\notin I}\dim F_i
+\dim\left(E\cap\sum_{i\in I}F_i\right).
}
\tag{6.1}
\]

For `F_i=D_d(T_i)` and `|I|=s`, equations (5.3) and (6.1) give

\[
\boxed{
\dim\left(
E_d\cap\sum_{i=1}^qD_d(T_i)
\right)
\le
(q-s)\binom nd+\beta_{n,d}(s).
}
\tag{6.2}
\]

Only literal derivative-space sums occur in this lemma.

## 7. Coupled sum and outer product shadow

Fix `q` named terms in a hypothetical decomposition and write their coupled
sum as

\[
R=T_1+\cdots+T_q.
\]

Let

\[
r=n-m,
\qquad
S=\mathcal D_r(\operatorname{perm}_n)
\cap\mathcal D_r(R),
\qquad b=\dim S.
\]

Differentiation gives the valid containments

\[
\partial S
\subseteq
\mathcal D_{r-1}(R)
\subseteq
\sum_{i=1}^q\mathcal D_{r-1}(T_i).
\tag{7.1}
\]

No equality between the coupled image and the literal sum is used.  Applying
(6.2) at `d=r-1` yields

\[
F^{(1)}_{n,r}(b)
\le
(q-s)\binom n{r-1}
+
\beta_{n,r-1}(s).
\tag{7.2}
\]

The exact transition of the left side provides a complementary-intersection
cap.  The repository's residual first-Koszul theorem then gives the remaining
term count.

## 8. Application to `perm_7`

Choose

\[
n=7,\qquad m=3,\qquad r=4,\qquad q=19,\qquad s=4.
\]

At the inner degree `d=3`, use derivative order one.  The exact transition is

\[
F^{(1)}_{7,3}(64)=84,
\qquad
F^{(1)}_{7,3}(65)=87.
\tag{8.1}
\]

Since

\[
4\binom72=84,
\]

we have

\[
\beta_{7,3}(4)\le64.
\tag{8.2}
\]

The projected outer capacity is therefore

\[
(19-4)\binom73+64
=15\cdot35+64
=589.
\tag{8.3}
\]

The exact outer transition is

\[
F^{(1)}_{7,4}(341)=586,
\qquad
F^{(1)}_{7,4}(342)=590,
\tag{8.4}
\]

so `b<=341`.

The Koszul numbers are

\[
A_{7,3}=58,800,
\qquad B_{7,3}=1,680.
\]

Thus the residual needs at least

\[
\left\lceil
\frac{58,800-49\cdot341}{1,680}
\right\rceil
=26
\]

terms.  Adding the nineteen fixed terms proves

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)
\ge19+26=45.
}
\tag{8.5}
\]

The global first-Koszul lower bound is 36, so selecting nineteen terms is
legitimate.

## 9. Application to `perm_8`

Choose

\[
n=8,\qquad m=r=4,\qquad q=17,\qquad s=2.
\]

At the inner degree `d=3`, use derivative order two.  The exact transition is

\[
F^{(2)}_{8,3}(16)=16,
\qquad
F^{(2)}_{8,3}(17)=18.
\tag{9.1}
\]

Since

\[
2\binom81=16,
\]

we have

\[
\beta_{8,3}(2)\le16.
\tag{9.2}
\]

The projected outer capacity is

\[
(17-2)\binom83+16
=15\cdot56+16
=856.
\tag{9.3}
\]

The exact outer transition is

\[
F^{(1)}_{8,4}(625)=850,
\qquad
F^{(1)}_{8,4}(626)=858,
\tag{9.4}
\]

so `b<=625`.

The first-Koszul values are

\[
A_{8,4}=310,464,
\qquad B_{8,4}=4,424.
\]

Therefore the residual needs at least

\[
\left\lceil
\frac{310,464-64\cdot625}{4,424}
\right\rceil
=62
\]

terms.  Adding the seventeen fixed terms gives

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)
\ge17+62=79.
}
\tag{9.5}
\]

The global first-Koszul lower bound is 71, so selecting seventeen terms is
legitimate.

## 10. Reproduction

Run

```bash
python scripts/general_iterated_product_shadow_blocks.py \
  --json /tmp/general_iterated_product_shadow_blocks.json
python scripts/general_iterated_product_shadow_blocks_independent.py
python -m unittest tests.test_general_iterated_product_shadow_blocks -v
```

Expected markers:

```text
GENERAL_ITERATED_PRODUCT_SHADOW_BLOCKS_AUDIT_PASS
GENERAL_ITERATED_PRODUCT_SHADOW_BLOCKS_INDEPENDENT_PASS
```

The independent implementation imports none of the primary audit.  It
reconstructs all eight decisive finite values from explicit subset families
and a forward Ferrers dynamic program.

## 11. Hidden assumptions and strongest objection

The load-bearing assumptions are:

1. arbitrary-order derivative rank cannot increase under torus
   specialization;
2. colex initial segments minimize every iterated lower shadow;
3. the section projection retains only an additive block-intersection defect;
4. the coupled derivative image is used only through the containments (7.1).

All four are explicit in the proof.

The strongest objection is asymptotic: a finite tower of scalar shadow
cardinalities may still remain on central-binomial scale.  The new theorem
uses more structure than one shadow and gives strict finite improvements, but
it does not establish that iterating the construction can reach
`2^(n-1)`.  The next valid interface is the equality and near-equality
structure of the inner block caps, not a larger undifferentiated dynamic
program.
