# The same-operator colored mapping cone and its scalar barrier

**Status.** `PURE_EXACT_SEQUENCE`, `EXACT_QQ_REPLAY`,
`LOWER_27_ROUTE_BARRIER` (G-039).  The base field has characteristic zero.
This note strengthens one colored dimension in N6-037, but it does not prove
`ChowRank(perm_6)>=27` and makes no border-rank claim.

## 1. Three relation objects that must not be conflated

Let `f=sum_(i=1)^r T_i` be a displayed sum of sextic Chow terms.  Put

\[
 A_m=\operatorname{Sym}^{6-m}(V^*),\qquad
 C_{i,m}:A_m\longrightarrow U_{i,m}=\mathcal D_m(T_i),
\tag{1.1}
\]

and `L_m=sum_i U_(i,m)`.  The ordinary colored output-relation space is

\[
 \mathcal R_m=\ker\left(\bigoplus_iU_{i,m}\longrightarrow L_m\right).
\tag{1.2}
\]

It allows unrelated preimages in the different summands.  To retain one
common differential operator, define

\[
 \Gamma_m:A_m\longrightarrow\bigoplus_iU_{i,m},\qquad
 x\longmapsto(C_{1,m}x,\ldots,C_{r,m}x),
 \quad X_m=\operatorname{im}\Gamma_m .
\tag{1.3}
\]

The synchronized cancellation space is

\[
 \mathcal S_m=X_m\cap\mathcal R_m
 =\Gamma_m(\ker C_{f,m}).
\tag{1.4}
\]

The equality is literal: the component sum of `Gamma_m(x)` is `C_(f,m)x`.
In particular, `S_m` can be much smaller than `R_m`; replacing one by the
other loses precisely the common-domain condition.

Now fix the permanent `P` and put `E_m=D_m(P)`.  The ordinary quotient-colored
relation space is

\[
 \overline{\mathcal R}_m=
 \ker\left(\bigoplus_iU_{i,m}\longrightarrow(L_m+E_m)/E_m\right).
\tag{1.5}
\]

Its synchronized part is

\[
 \overline X_m=X_m\cap\overline{\mathcal R}_m.
\tag{1.6}
\]

If `G_m=D_m(f)`, component summation gives the exact sequence

\[
 0\longrightarrow\mathcal S_m
 \longrightarrow\overline X_m
 \longrightarrow E_m\cap G_m\longrightarrow0.
\tag{1.7}
\]

Surjectivity follows by choosing a common operator `x` with
`C_(f,m)x=y` for each `y in E_m cap G_m`.  Thus

\[
 \dim\overline{\mathcal R}_m
 \ge \dim\overline X_m
 =\dim\mathcal S_m+\dim(E_m\cap G_m).
\tag{1.8}
\]

For the N6-032 twenty-term residual `Q`, (1.8) improves the previously stated
middle colored bound `320` to the strict common-domain bound

\[
 \boxed{\dim\overline{\mathcal R}_3\ge336.}
\tag{1.9}
\]

Its first shadow is still the already known
`dim(E_2 cap D_2(Q))>=203`; hence (1.9) does not close lower 27.

## 2. The equation-coupled kernel sequence

Assume `P=H+Q`.  Let

\[
 K(f)=f^\perp\subseteq\operatorname{Sym}(V^*)
\tag{2.1}
\]

be the graded apolar ideal.  For `x in K(Q)`, one has

\[
 x\mathbin\lrcorner P=x\mathbin\lrcorner H.
\tag{2.2}
\]

Define the same-operator diagonal image module

\[
J^{\rm diag}=
 \{x\mathbin\lrcorner P:x\in K(Q)\}
 =\{x\mathbin\lrcorner H:x\in K(Q)\}.
\tag{2.3}
\]

We grade `J^diag` by the order of the operator producing its elements.
Multiplication of differential operators corresponds to further
differentiation, so this is a graded module.  The map in (2.3) has kernel
`K(P) cap K(H)`.  Therefore there is a short exact sequence of graded
modules

\[
 \boxed{
 0\longrightarrow K(P)\cap K(H)
 \longrightarrow K(Q)
 \longrightarrow J^{\rm diag}\longrightarrow0.}
\tag{2.4}
\]

This is the legitimate common-domain mapping cone.  There is generally no
inclusion `K(P)+K(H) subset K(Q)`: for `u in K(P)` and `v in K(H)`,

\[
 (u+v)\mathbin\lrcorner Q
 =-u\mathbin\lrcorner H+v\mathbin\lrcorner P,
\tag{2.5}
\]

which need not vanish.  This observation rules out a tempting but false
kernel-sum sequence.

After grading the target by operator order, applying the Koszul functor to
(2.4) gives the standard long exact sequence

\[
 \cdots\to
 \operatorname{Tor}_p(K(P)\cap K(H),\mathbf k)
 \to\operatorname{Tor}_p(K(Q),\mathbf k)
 \to\operatorname{Tor}_p(J^{\rm diag},\mathbf k)
 \to\operatorname{Tor}_{p-1}(K(P)\cap K(H),\mathbf k)
 \to\cdots .
\tag{2.6}
\]

In the actual 36-variable operator domain, `C_(3,3)(P)` has rank 400 but its
domain has dimension 8436.  Thus `K(P)_3` is large; it is essential not to
replace the full domain by the 400-dimensional apolar quotient, because
`K(Q)_3` has no natural injection into that quotient.  What follows directly
from (2.3) is only

\[
 J^{\rm diag}_3\subseteq E_3\cap H_3,
 \qquad \dim J^{\rm diag}_3\le b\le64.
\tag{2.7}
\]

The exact sequence therefore reorganizes rather than sharpens the existing
middle data.  An Euler characteristic by itself supplies no new inequality.
A stronger argument would have to control its connecting maps or permanent
weight pieces, not only the dimensions in (2.6).

## 3. Exact relation--homology counterexamples in six variables

The most direct scalar continuation would try to bound the kernel of the
factor-labelled cycle presentation by the ordinary middle relation dimension

\[
 \rho=\sum_i\dim\mathcal D_3(T_i)
       -\dim\sum_i\mathcal D_3(T_i).
\tag{3.1}
\]

Three exact small-matrix examples disprove this.

| tuple | `rho` | labelled cycles | aggregate boundary | quotient rank | quotient kernel |
|---|---:|---:|---:|---:|---:|
| G-034 completed three-term block | 4 | 60 | 570 | 60 | 0 |
| G-037 two full-span terms | 4 | 40 | 380 | 33 | 7 |
| G-037 full-span plus rank-five term | 2 | 40 | 380 | 28 | 12 |

All ranks are over `Q`.  G-034 certifies the middle rank 56 by an exact
integer determinant and gives aggregate ranks `570`, `60`, and `630` for
boundary, labelled cycles, and their joint span.  G-037 reconstructs both
pair rows by exact `Fraction` elimination.

The first two rows have the same `rho=4` but quotient kernels zero and seven.
The third has a smaller `rho=2` and a larger kernel twelve.  Consequently
`rho` does not determine the quotient kernel, the kernel is not monotone
increasing with `rho`, and even the direct bound `kernel<=rho` is false:

\[
 \boxed{\text{ordinary relation dimension alone neither determines nor
 monotonically lower-controls labelled-cycle quotient homology.}}
\tag{3.2}
\]

These examples do not exclude every possible inequality involving `rho`, the
number and strata of the terms, or further permanent-specific data.  They are
not permanent decompositions, so they leave a weight-refined use of (2.6)
open.

## 4. What remains open

The exact sequences (1.7) and (2.4) are valid and retain the common operator
domain.  Their dimension-only consequences do not improve the current
ordinary interval

\[
 26\le\operatorname{ChowRank}(\operatorname{perm}_6)\le32.
\]

One surviving target is the connecting map in (2.6), split into the
row-heavy and column-heavy twenty-dimensional weight pieces of
`H_(3,6)(P)`.  Any continuation along this route would need to use the
permanent-specific
data

\[
 \dim H_{3,6}(P)=40,\qquad
 \dim(E_3\cap G_3)\ge336,\qquad
 \dim(E_2\cap G_2)\ge203,
\tag{4.1}
\]

and the fixed-six constraints.  G-039 shows that replacing the relevant
connecting-map data only by `rho`, or assuming `kernel<=rho`, cannot work.

## 5. Replay

```text
python scripts/n6_colored_mapping_cone_barrier.py \
  --json data/n6_colored_mapping_cone_barrier.json
python -m unittest tests.test_n6_colored_mapping_cone_barrier -v
```

The two G-037 pair rows are rebuilt over `Fraction` in six variables.  The
G-034 triple row is a frozen exact certificate from its independent replay.
No floating-point or random rank is used.
