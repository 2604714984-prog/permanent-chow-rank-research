# Exact simultaneous product shadows for permanent derivative spaces

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `EXACT_INTEGER_DP_REPLAYED`,
`GENERAL_N_PROGRESS`.

This note proves an exact finite formula for the minimum first-derivative
shadow of an arbitrary subspace of a permanent derivative space. It strictly
refines the continuous multidimensional Kruskal--Katona cap used by the
existing general multishadow theorem and gives the new ordinary-rank bounds

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge 42},
\qquad
\boxed{\operatorname{ChowRank}(\operatorname{perm}_8)\ge 77}.
\]

The result does **not** prove `ChowRank(perm_n)=2^(n-1)`, determine `perm_7`
or `perm_8` exactly, improve the current specialized `perm_6` lower bound, or
make a border-rank claim. Literature novelty has not been established.

## 1. Permanent derivative spaces and simultaneous shadows

Fix integers

\[
1\le m\le n-1
\]

and let

\[
E_m=\mathcal D_m(\operatorname{perm}_n).
\]

For row and column sets

\[
R,C\in\binom{[n]}m,
\]

write `p_(R,C)` for the corresponding `m x m` subpermanent. The vectors

\[
\{p_{R,C}:R,C\in\tbinom{[n]}m\}
\]

form a basis of `E_m`. Their derivatives are

\[
\partial_{ij}p_{R,C}
=
\begin{cases}
p_{R\setminus\{i\},C\setminus\{j\}},&i\in R,\ j\in C,\\
0,&\text{otherwise}.
\end{cases}
\tag{1.1}
\]

Thus a coordinate family

\[
\mathcal A\subseteq
\binom{[n]}m\times\binom{[n]}m
\]

has derivative dimension equal to the cardinality of its simultaneous lower
shadow

\[
\partial_\times\mathcal A
=
\left\{
(I,J):
\begin{array}{l}
I\in\binom{[n]}{m-1},\ J\in\binom{[n]}{m-1},\\
I\subset R,\ J\subset C\text{ for some }(R,C)\in\mathcal A
\end{array}
\right\}.
\tag{1.2}
\]

## 2. Coordinate specialization is universal

### Proposition 2.1

For every `b`-dimensional subspace

\[
S\subseteq E_m
\]

there is a coordinate `b`-plane `S_0` such that

\[
\dim\partial S_0\le \dim\partial S.
\tag{2.1}
\]

### Proof

The row-column diagonal torus acts on `E_m`. The basis vectors `p_(R,C)` have
pairwise distinct torus weights. The closure of the torus orbit of `[S]` in
the complete Grassmannian `Gr(b,E_m)` contains a torus-fixed point; every
such point is a coordinate plane.

On `Gr(b,E_m)`, first differentiation is the image of the tautological bundle
map

\[
\mathcal S\otimes V_n^*\longrightarrow E_{m-1}.
\tag{2.2}
\]

Its rank is constant along the torus orbit and cannot increase under
specialization. This proves (2.1). Scalar extension to an algebraic closure
does not change any dimension, so the conclusion holds over every
characteristic-zero field. ∎

## 3. Two colex compressions give a Ferrers family

Put

\[
q=\binom nm
\]

and order the `m`-subsets of `[n]` by colex order:

\[
A_0,A_1,\ldots,A_{q-1}.
\]

For `0<=t<=q`, let

\[
k_{n,m}(t)
=
\left|\partial\{A_0,\ldots,A_{t-1}\}\right|.
\tag{3.1}
\]

The ordinary Kruskal--Katona theorem says that every family of `t` `m`-sets
has lower shadow at least `k_(n,m)(t)`, and the shadow of a colex initial
segment is again a colex initial segment.

Represent a coordinate family by its `q x q` zero-one matrix. For each row
`A_i`, replace its column fiber by the colex initial segment of the same
cardinality. Fix a lower row set

\[
I\in\binom{[n]}{m-1}.
\]

Before compression, its column-shadow fiber is

\[
\bigcup_{A_i\supset I}\partial\mathcal A_{A_i}.
\tag{3.2}
\]

Its cardinality is at least

\[
\max_{A_i\supset I}k_{n,m}(|\mathcal A_{A_i}|).
\tag{3.3}
\]

After compression, the shadows in (3.2) are nested colex initial segments,
so their union has exactly the value in (3.3). Summing over `I` proves that
row-fiber compression does not increase the product shadow.

Apply the symmetric operation to every column. It also does not increase the
product shadow. After the first compression, column heights are nonincreasing
from left to right. The second compression replaces every column by an
initial row segment while preserving those heights. Hence the result is a
Ferrers family

\[
\mathcal A_\lambda
=
\{(i,j):0\le i<q,\ 0\le j<\lambda_i\}
\tag{3.4}
\]

for a partition

\[
q\ge\lambda_0\ge\lambda_1\ge\cdots\ge\lambda_{q-1}\ge0,
\qquad
\sum_i\lambda_i=b.
\tag{3.5}
\]

This argument proves exact reduction for arbitrary subspaces through
Proposition 2.1. It is not a generic-coordinate-support assumption.

## 4. Closed Ferrers objective

For a lower set

\[
I\in\binom{[n]}{m-1},
\]

let `f(I)` be the least colex index of an `m`-set containing `I`, and define

\[
w_i=|\{I:f(I)=i\}|.
\tag{4.1}
\]

Because `lambda_i` is nonincreasing and `k_(n,m)` is nondecreasing, the
column-shadow fiber over `I` in the Ferrers family has size

\[
k_{n,m}(\lambda_{f(I)}).
\]

Therefore

\[
\boxed{
\Phi_{n,m}(\lambda)
=
\sum_{i=0}^{q-1}w_i k_{n,m}(\lambda_i).
}
\tag{4.2}
\]

The weights have a simple closed form. If

\[
c_i=\min([n]\setminus A_i),
\]

then

\[
\boxed{w_i=c_i.}
\tag{4.3}
\]

Indeed, the lower sets first contained in `A_i` are exactly

\[
A_i\setminus\{a\},
\qquad 0\le a<c_i.
\]

All integers below `c_i` belong to `A_i`, while `c_i` does not. Thus there
are precisely `c_i` such lower sets.

### Theorem 4.1 -- exact product-shadow formula

Let

\[
F_{n,m}(b)
=
\min_{\substack{S\subseteq E_m\\\dim S=b}}
\dim\partial S.
\]

Then

\[
\boxed{
F_{n,m}(b)
=
\min_{\substack{
q\ge\lambda_0\ge\cdots\ge\lambda_{q-1}\ge0\\
\sum_i\lambda_i=b}}
\sum_{i=0}^{q-1}w_i k_{n,m}(\lambda_i).
}
\tag{4.4}
\]

### Proof

Proposition 2.1 reduces an arbitrary subspace to a coordinate family with no
larger shadow. The two compressions reduce that family to a Ferrers family
without increasing its shadow. Formula (4.2) computes the Ferrers shadow
exactly. Conversely every partition in (4.4) defines a coordinate Ferrers
plane realizing its displayed objective. Hence both inequalities are sharp.
∎

### Lemma 4.2 -- monotonicity

The function `F_(n,m)(b)` is nondecreasing in `b`.

### Proof

Every `(b+1)`-plane contains a `b`-plane. Differentiating the smaller plane
gives a subspace of the derivative image of the larger plane. Thus every
`(b+1)`-plane has derivative dimension at least `F_(n,m)(b)`. Taking the
minimum over all `(b+1)`-planes gives

\[
F_{n,m}(b+1)\ge F_{n,m}(b).
\]
∎

This elementary monotonicity permits a binary search for every exact
intersection threshold. It is a runtime reduction only; it changes neither
the theorem nor the finite objective.

## 5. Exact integer dynamic programming

Let

\[
D(i,u,s)
\]

be the minimum contribution from rows `i,...,q-1`, assuming `lambda_i<=u`
and the remaining partition sum is `s`. Then

\[
D(i,u,s)
=
\min_x
\left\{
 w_i k_{n,m}(x)+D(i+1,x,s-x)
\right\},
\tag{5.1}
\]

where

\[
\left\lceil\frac{s}{q-i}\right\rceil
\le x\le\min(u,s,q).
\tag{5.2}
\]

The lower limit is exactly the condition that the remaining `q-i-1` parts
can be at most `x`. The terminal values are

\[
D(q,u,0)=0,
\qquad
D(q,u,s)=+\infty\quad(s>0).
\tag{5.3}
\]

The recurrence uses only integers, enumerates every partition exactly once,
and returns the minimum, the number of minimizing partitions and a witness.
Lemma 4.2 then locates the last admissible family size by exact binary search.

## 6. Exact refinement of the general multishadow theorem

Let

\[
r=n-m,
\qquad
A_{n,m}=n^2\binom nm^2-\binom n{m+1}^2,
\]

\[
B_{n,m}=n^2\binom nm-\binom n{m+1}.
\tag{6.1}
\]

Fix a sum `R` of `q_0` Chow terms and put

\[
S=
\mathcal D_r(\operatorname{perm}_n)
\cap
\mathcal D_r(R),
\qquad b=\dim S.
\]

Differentiation gives

\[
\partial S\subseteq\mathcal D_{r-1}(R).
\]

One Chow term has degree-`r-1` derivative-space dimension at most
`binom(n,r-1)`, so

\[
F_{n,r}(b)
\le q_0\binom n{r-1}.
\tag{6.2}
\]

Define the exact intersection cap

\[
\beta_{n,r}(q_0)
=
\max\left\{
 b:F_{n,r}(b)\le q_0\binom n{r-1}
\right\}.
\tag{6.3}
\]

The complementary-intersection residual theorem already proved in the
repository gives

\[
\operatorname{rank}K_m(\operatorname{perm}_n-R)
\ge A_{n,m}-n^2b.
\tag{6.4}
\]

Therefore:

### Corollary 6.1 -- exact finite multishadow bound

Whenever the globally optimized first-Koszul lower bound guarantees at least
`q_0` terms and the numerator below is positive,

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_n)
\ge
q_0+
\left\lceil
\frac{A_{n,m}-n^2\beta_{n,r}(q_0)}{B_{n,m}}
\right\rceil.
}
\tag{6.5}
\]

This replaces the real-binomial Bukh cap by the exact finite shadow function.
It cannot weaken the earlier bound because `F_(n,r)` is the true minimum.
The global first-Koszul selection bound and the ratio at the chosen output
degree are recorded separately in the frozen certificate.

## 7. Application: `ChowRank(perm_7)>=42`

Take

\[
n=7,
\qquad m=3,
\qquad r=4,
\qquad q_0=13.
\]

The globally optimized first-Koszul lower bound is 36, while the selected
output degree `m=3` by itself certifies 35. Either value is already above
thirteen, so selecting thirteen terms is legitimate. Their degree-three
derivative cap is

\[
13\binom73=455.
\tag{7.1}
\]

The exact Ferrers dynamic program gives

\[
F_{7,4}(238)=452,
\qquad
F_{7,4}(239)=456.
\tag{7.2}
\]

Hence

\[
\beta_{7,4}(13)=238.
\tag{7.3}
\]

The relevant Koszul numbers are

\[
A_{7,3}
=49\binom73^2-\binom74^2
=58,800,
\]

\[
B_{7,3}
=49\binom73-\binom74
=1,680.
\tag{7.4}
\]

The residual therefore requires at least

\[
\left\lceil
\frac{58,800-49\cdot238}{1,680}
\right\rceil
=29
\tag{7.5}
\]

terms. Adding the fixed thirteen terms proves

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)
\ge13+29=42.
}
\tag{7.6}
\]

Glynn gives the independent upper bound 64, so this note records the ordinary
interval

\[
42\le\operatorname{ChowRank}(\operatorname{perm}_7)\le64.
\]

## 8. New application: `ChowRank(perm_8)>=77`

Take

\[
n=8,
\qquad m=r=4,
\qquad q_0=14.
\]

The ordinary first-Koszul lower bound is 71, so selecting fourteen terms is
legitimate. Their degree-three derivative cap is

\[
14\binom83
=
14\cdot56
=
784.
\tag{8.1}
\]

The exact Ferrers dynamic program gives the sharp transition

\[
F_{8,4}(560)=784,
\qquad
F_{8,4}(561)=793.
\tag{8.2}
\]

Thus

\[
\beta_{8,4}(14)=560.
\tag{8.3}
\]

There are exactly two minimizing Ferrers partitions at each of the two
displayed sizes. One witness at size 560 is

\[
(\underbrace{15,\ldots,15}_{35},
 \underbrace{1,\ldots,1}_{35}),
\tag{8.4}
\]

and one witness at size 561 replaces the first trailing `1` by `2`.

The relevant Koszul numbers are

\[
A_{8,4}
=
64\binom84^2-\binom85^2
=
310,464,
\]

\[
B_{8,4}
=
64\binom84-\binom85
=
4,424.
\tag{8.5}
\]

Therefore the residual requires at least

\[
\left\lceil
\frac{310,464-64\cdot560}{4,424}
\right\rceil
=
\left\lceil
\frac{274,624}{4,424}
\right\rceil
=
63
\tag{8.6}
\]

terms. Adding the fixed fourteen terms gives

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_8)
\ge14+63=77.
}
\tag{8.7}
\]

This improves the previous in-repository general multishadow bound 76 by one.
Glynn gives the upper bound 128, so the new ordinary interval is

\[
77\le\operatorname{ChowRank}(\operatorname{perm}_8)\le128.
\]

The improvement is small in absolute terms but structurally useful: it
confirms that the exact finite product shadow can strictly beat the continuous
Bukh surrogate beyond the first odd-degree example.

## 9. Regression and independent replay

For `(n,m)=(6,3)`, the general recurrence exactly reproduces the specialized
N6-056 table, including

\[
F_{6,3}(53)=81,
\qquad
F_{6,3}(60)=84,
\qquad
F_{6,3}(65)=87.
\]

The primary implementation is

```text
scripts/general_exact_product_shadow.py
```

and a second implementation, which imports none of its functions and uses a
forward state dynamic program, is

```text
scripts/general_exact_product_shadow_independent.py
```

The independent replay obtains

```text
F_7,4(238)=452
F_7,4(239)=456
perm_7 residual terms=29
perm_7 lower bound=42

F_8,4(560)=784
F_8,4(561)=793
perm_8 residual terms=63
perm_8 lower bound=77
```

## 10. Hidden assumptions and strongest objection

### Hidden assumptions

1. The torus specialization must preserve the subspace dimension and may only
   decrease derivative rank.
2. Alternating the two one-dimensional colex compressions must actually yield
   a Ferrers family after the second operation.
3. The general residual theorem must use the intersection at the complementary
   derivative degree `r`, not the output degree `m`.
4. The threshold search must rely only on proved monotonicity, not on observed
   numerical monotonicity of the generated table.

All four points are explicit in the proof. The second point uses the fact
that row compression makes column heights nonincreasing; replacing each
column by an initial row segment with those same heights therefore produces a
Ferrers diagram immediately. Lemma 4.2 supplies the fourth point.

### Assume all assumptions are false

Then the numerical values 42 and 77 have no mathematical force. The
appropriate response would be to retain only the finite dynamic programs as
coordinate diagnostics and remove the general-subspace and Chow-rank claims.
The regression and independent implementation do not substitute for the
specialization, compression and complementary-intersection proofs.

### Strongest objection

An exact product-shadow theorem may sharpen finite instances without changing
the asymptotic central-binomial scale. That objection is correct. This note is
a real general-`n` improvement and a reusable exact interface, but it is not
by itself a plausible complete proof of Glynn optimality. A complete solution
still needs a second invariant controlling equality or near-equality
families, coupled relations among fixed terms, or a recurrence retaining more
than shadow cardinality.

The two new lower bounds reinforce this diagnosis. Exact finite optimization
improves 41 to 42 and 76 to 77, not to 64 and 128. Further expansion of the
same scalar shadow dynamic program is therefore not promoted as the main
route.

## 11. Reproduction

Run

```bash
python scripts/general_exact_product_shadow.py \
  --json /tmp/general_exact_product_shadow.json
python scripts/general_exact_product_shadow_independent.py
python -m unittest tests.test_general_exact_product_shadow -v
```

Expected terminal markers:

```text
GENERAL_EXACT_PRODUCT_SHADOW_AUDIT_PASS
GENERAL_EXACT_PRODUCT_SHADOW_INDEPENDENT_PASS
```
