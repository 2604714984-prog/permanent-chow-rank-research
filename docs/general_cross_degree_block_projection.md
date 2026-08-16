# Cross-degree projection for permanent derivative blocks

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_REPLAYED`,
`GENERAL_N_BLOCK_PROJECTION_THEOREM`.

This note combines the exact permanent product-shadow theorem with a linear
section/projection argument **one derivative degree lower**.  It proves the
ordinary characteristic-zero bounds

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge45}
\]

and

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_8)\ge80}.
\]

The argument concerns literal sums of Chow derivative spaces.  For an actual
polynomial sum it uses only the valid containment

\[
\mathcal D_d\!\left(\sum_iT_i\right)
\subseteq
\sum_i\mathcal D_d(T_i).
\]

It does not identify a coupled catalectic image with the literal sum, improve a
border-rank bound, determine either exact rank, or prove general Glynn
optimality.

## 1. Setup

Let

\[
E_d(n)=\mathcal D_d(\operatorname{perm}_n).
\]

For a degree-\(n\) Chow term \(T\), write

\[
F_d(T)=\mathcal D_d(T).
\]

The exact product-shadow theorem already proved in the repository defines

\[
\mathfrak F^{(a)}_{n,d}(b)
=
\min_{\substack{A\subseteq E_d(n)\\\dim A=b}}
\dim\partial^a A,
\qquad 1\le a<d.
\tag{1.1}
\]

For \(a=1\), this is the exact Ferrers integer program from PR #35.  Every
value used below is an exact characteristic-zero minimum for arbitrary
subspaces, not a coordinate-only diagnostic.

## 2. A one-term cap at a lower derivative degree

Fix \(e\ge2\).  Define

\[
c_{n,e}
=
\max\left\{
b:
\mathfrak F^{(e-1)}_{n,e}(b)\le n
\right\}.
\tag{2.1}
\]

### Lemma 2.1

For every degree-\(n\) Chow term \(T\), including a degenerate term,

\[
\boxed{
\dim\bigl(E_e(n)\cap F_e(T)\bigr)
\le c_{n,e}.
}
\tag{2.2}
\]

### Proof

Let \(L_T\) be the span of the factors of \(T\).  Then

\[
\dim L_T\le n,
\qquad
F_e(T)\subseteq\operatorname{Sym}^eL_T.
\]

For

\[
B=E_e(n)\cap F_e(T),
\]

every order-\((e-1)\) derivative lies in \(L_T\), so

\[
\dim\partial^{e-1}B\le n.
\]

By the defining exact minimum (1.1),

\[
\mathfrak F^{(e-1)}_{n,e}(\dim B)
\le n.
\]

Equation (2.1) gives (2.2).  No factor independence is required. ∎

## 3. Section/projection at the lower degree

Let \(T_1,\ldots,T_q\) be Chow terms and put

\[
G_i=F_e(T_i),
\qquad
U=G_1+\cdots+G_q,
\qquad
B=E_e(n)\cap U.
\]

### Lemma 3.1 -- projected lower-degree cap

\[
\boxed{
\dim B
\le
(q-1)\binom ne+c_{n,e}.
}
\tag{3.1}
\]

### Proof

Let

\[
\pi:\bigoplus_{i=1}^qG_i\longrightarrow U
\]

be the summation map.  Choose a linear section

\[
s:B\longrightarrow\bigoplus_iG_i
\]

of \(\pi\) over \(B\).  Project \(s(B)\) to any chosen \(q-1\) summands.
The image has dimension at most

\[
(q-1)\binom ne.
\]

If an element lies in the projection kernel, its selected lift is supported in
the omitted summand, and its sum belongs to

\[
E_e(n)\cap G_j.
\]

Because \(s\) is a section, the kernel maps injectively to that intersection.
Lemma 2.1 bounds the kernel by \(c_{n,e}\), proving (3.1).

No direct-sum hypothesis is used. ∎

## 4. Cross-degree transfer

Let \(d>e\), set \(a=d-e\), and define

\[
A
=
E_d(n)\cap
\sum_{i=1}^qF_d(T_i).
\]

Differentiation gives

\[
\partial^a A
\subseteq
E_e(n)\cap
\sum_{i=1}^qF_e(T_i).
\tag{4.1}
\]

Combining (4.1) with Lemma 3.1 and the exact shadow minimum yields:

### Theorem 4.1 -- cross-degree block projection

\[
\boxed{
\mathfrak F^{(a)}_{n,d}(\dim A)
\le
(q-1)\binom ne+c_{n,e}.
}
\tag{4.2}
\]

Equivalently,

\[
\boxed{
\dim A
\le
\max\left\{
b:
\mathfrak F^{(a)}_{n,d}(b)
\le
(q-1)\binom ne+c_{n,e}
\right\}.
}
\tag{4.3}
\]

This is the new step.  Earlier block estimates bounded the lower derivative
space by the crude capacity \(q\binom ne\).  Formula (4.3) first removes one
summand up to its exact permanent-relative defect and only then inverts the
upper-degree shadow.

## 5. The four-term cubic cap for `perm_7`

Take

\[
n=7,\qquad d=3,\qquad e=2,\qquad q=4.
\]

The exact lower-degree transition is

\[
\mathfrak F^{(1)}_{7,2}(3)=6,
\qquad
\mathfrak F^{(1)}_{7,2}(4)=8.
\tag{5.1}
\]

Hence

\[
c_{7,2}=3.
\tag{5.2}
\]

Lemma 3.1 gives

\[
\dim\left(
E_2(7)\cap\sum_{i=1}^{4}F_2(T_i)
\right)
\le
3\binom72+3
=66.
\tag{5.3}
\]

At the cubic level,

\[
\mathfrak F^{(1)}_{7,3}(41)=66,
\qquad
\mathfrak F^{(1)}_{7,3}(42)=69.
\tag{5.4}
\]

Therefore:

### Corollary 5.1

For arbitrary four degree-seven Chow terms,

\[
\boxed{
\dim\left(
E_3(7)\cap\sum_{i=1}^{4}F_3(T_i)
\right)
\le41.
}
\tag{5.5}
\]

The previous arbitrary-subspace block cap used in the route optimization was
64.

## 6. The five-term cubic cap for `perm_8`

Take

\[
n=8,\qquad d=3,\qquad e=2,\qquad q=5.
\]

The exact lower-degree transition is

\[
\mathfrak F^{(1)}_{8,2}(6)=8,
\qquad
\mathfrak F^{(1)}_{8,2}(7)=9.
\tag{6.1}
\]

Thus

\[
c_{8,2}=6.
\tag{6.2}
\]

Lemma 3.1 gives

\[
\dim\left(
E_2(8)\cap\sum_{i=1}^{5}F_2(T_i)
\right)
\le
4\binom82+6
=118.
\tag{6.3}
\]

The upper transition is

\[
\mathfrak F^{(1)}_{8,3}(112)=118,
\qquad
\mathfrak F^{(1)}_{8,3}(113)=120.
\tag{6.4}
\]

Hence:

### Corollary 6.1 -- five-term cubic cap

For arbitrary five degree-eight Chow terms,

\[
\boxed{
\dim\left(
E_3(8)\cap\sum_{i=1}^{5}F_3(T_i)
\right)
\le112.
}
\tag{6.5}
\]

This is strictly stronger than the cap 146 previously identified as
sufficient for lower 80.  It is also compatible with the coordinate cap 40:
the latter is stronger on fixed coordinate terms, while (6.5) is uniform over
all characteristic-zero terms and does not pass through a flat coordinate
limit.

## 7. Application: `ChowRank(perm_7)>=45`

The base stack already excludes ranks below 44, so under a hypothetical
rank-at-most-44 decomposition one may fix seventeen terms.  Select four of
them as the block in Corollary 5.1.

At output degree three, the complementary permanent derivative degree is four.
The first derivative of the complementary intersection lies in the cubic
literal sum.  Projecting away the four-term block gives capacity

\[
13\binom73+41
=455+41
=496.
\tag{7.1}
\]

The exact outer transition is

\[
\mathfrak F^{(1)}_{7,4}(263)=494,
\qquad
\mathfrak F^{(1)}_{7,4}(264)=497.
\tag{7.2}
\]

Therefore the complementary intersection has dimension at most 263.  The
first-Koszul values are

\[
A_{7,3}=58,800,
\qquad
B_{7,3}=1,680.
\]

The residual requires

\[
\left\lceil
\frac{58,800-49\cdot263}{1,680}
\right\rceil
=
\left\lceil\frac{45,913}{1,680}\right\rceil
=28
\]

terms.  Adding the seventeen fixed terms proves

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge45.
}
\tag{7.3}
\]

## 8. Application: `ChowRank(perm_8)>=80`

The base stack proves the ordinary lower bound 79.  Under a hypothetical
rank-at-most-79 decomposition, fix seventeen terms and select five as the
block in Corollary 6.1.

At central output degree four, the first derivative of the complementary
intersection lies in the cubic literal sum.  The projected capacity is

\[
12\binom83+112
=672+112
=784.
\tag{8.1}
\]

PR #35 proves the exact outer transition

\[
\mathfrak F^{(1)}_{8,4}(560)=784,
\qquad
\mathfrak F^{(1)}_{8,4}(561)=793.
\tag{8.2}
\]

Thus the complementary intersection has dimension at most 560.  The central
first-Koszul numbers are

\[
A_{8,4}=310,464,
\qquad
B_{8,4}=4,424.
\]

The residual needs at least

\[
\left\lceil
\frac{310,464-64\cdot560}{4,424}
\right\rceil
=
\left\lceil\frac{274,624}{4,424}\right\rceil
=63
\]

terms.  Therefore

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)
\ge17+63=80.
}
\tag{8.3}
\]

Combined with Glynn,

\[
80
\le
\operatorname{ChowRank}(\operatorname{perm}_8)
\le128.
\]

## 9. Next exact target

The same central arithmetic shows that the sufficient next target

\[
\dim\left(
E_3(8)\cap\sum_{i=1}^{5}F_3(T_i)
\right)
\le90
\tag{9.1}
\]

would prove `ChowRank(perm_8)>=81`: fix twenty-one terms, retain sixteen
outside terms, and obtain projected capacity

\[
16\binom83+90=986.
\]

Since

\[
\mathfrak F^{(1)}_{8,4}(773)=987,
\]

the outer intersection would be at most 772, leaving sixty residual terms.
The present theorem proves 112, so the next structural improvement required by
this sufficient route is 22 dimensions.

No assertion is made here that 90 is the unique or globally minimal route to
81.

## 10. Deterministic reproduction

Primary replay:

```bash
python scripts/general_cross_degree_block_projection.py \
  --json /tmp/general_cross_degree_block_projection.json
```

Independent replay:

```bash
python scripts/general_cross_degree_block_projection_independent.py
```

Focused tests:

```bash
python -m unittest tests.test_general_cross_degree_block_projection -v
```

Expected terminal markers:

```text
GENERAL_CROSS_DEGREE_BLOCK_PROJECTION_AUDIT_PASS
GENERAL_CROSS_DEGREE_BLOCK_PROJECTION_INDEPENDENT_PASS
```

The primary implementation reuses the canonical exact product-shadow class.
The independent implementation imports none of it and reconstructs every
colex layer, lower shadow and first-container weight from explicit finite
sets.
