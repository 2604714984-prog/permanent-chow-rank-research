# Exact output-degree-two second-Koszul homology for `perm_6`

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

This note closes the characteristic-zero rank window left by the first
higher-wedge audit at output degree two. It also gives an exact six-term
counterexample to scalar homology subadditivity. The current Chow-rank interval
is unchanged:

\[
26\le \operatorname{ChowRank}(\operatorname{perm}_6)\le 32.
\]

This route does not prove lower 26. N6-030 supplies the ordinary lower bound by
a different average-subset argument. No border-lower-26 or exact-32 claim is made.

## 1. The relevant complex and its apolar interpretation

Let `V` be the 36-dimensional variable space. For a degree-six form `f`, write
`D_m(f)` for its degree-`m` derivative space. The output-degree-two part of the
first higher-wedge complex is

\[
D_3(f)\otimes V
\xrightarrow{\delta_1}
D_2(f)\otimes\Lambda^2V
\xrightarrow{\delta_2}
D_1(f)\otimes\Lambda^3V.
\tag{1.1}
\]

Let

\[
A_f=\operatorname{Sym}(V^*)/f^\perp
\]

be the apolar Artinian Gorenstein algebra. Catalectic duality identifies
`D_m(f)^*` with `(A_f)_m`. After dualizing (1.1), one obtains the total-degree
four strand

\[
(A_f)_1\otimes\Lambda^3V^*
\longrightarrow
(A_f)_2\otimes\Lambda^2V^*
\longrightarrow
(A_f)_3\otimes V^*
\]

of the standard Koszul complex of `A_f`. Therefore

\[
\dim\frac{\ker\delta_2}{\operatorname{im}\delta_1}
=
\beta_{2,4}(A_f).
\tag{1.2}
\]

Equation (1.2) is the missing structural input. The earlier torus-block audit
used only the inclusion `im(delta_1) subset ker(delta_2)` and therefore could
record only a rank window.

## 2. Exact rank for the permanent

Alper and Rowlands prove for the apolar algebra of the permanent that

\[
\beta_{2,4}(A_{\operatorname{perm}_n})
=
2\binom n2\binom n4.
\tag{2.1}
\]

For `n=6`, this gives

\[
\beta_{2,4}(A_{\operatorname{perm}_6})
=
2\binom62\binom64
=450.
\tag{2.2}
\]

The middle space in (1.1) has dimension

\[
\dim D_2(\operatorname{perm}_6)\binom{36}{2}
=
\binom62^2\binom{36}{2}
=141750.
\]

The preceding first-Koszul image has the already-proved rank

\[
\operatorname{rank}\delta_1=14175.
\]

Using (1.2)-(2.2),

\[
\boxed{
\operatorname{rank}\delta_2(\operatorname{perm}_6)
=141750-14175-450
=127125.
}
\tag{2.3}
\]

Thus the modular lower bound `127125` from the earlier audit is the exact
characteristic-zero rank; the former upper endpoint `127575` is superseded.

## 3. Exact rank for one independent Chow term

Let

\[
T=\ell_1\ell_2\ell_3\ell_4\ell_5\ell_6
\]

with independent factors. After a linear change of variables, take
`T=x_1x_2x_3x_4x_5x_6`. In the 36-variable ambient ring, its apolar algebra is
the complete intersection defined by 30 inactive linear variables and the six
active squares

\[
X_1^2,\ldots,X_6^2.
\]

In homological degree two and internal degree four, the Koszul resolution of
this complete intersection contributes exactly the pairs of active quadratic
generators. Hence

\[
\beta_{2,4}(A_T)=\binom62=15.
\tag{3.1}
\]

The middle space in (1.1) has dimension

\[
\binom62\binom{36}{2}=9450,
\]

and the preceding image has rank `705`. Therefore

\[
\boxed{
\operatorname{rank}\delta_2(T)
=9450-705-15
=8730.
}
\tag{3.2}
\]

Rank cannot increase under specialization of the six factors. Consequently
`8730` is also an upper bound for every degenerate degree-six Chow term.
Combining (2.3) and (3.2) gives only

\[
\left\lceil\frac{127125}{8730}\right\rceil=15.
\]

Closing the homology gap therefore does not improve the integer flattening
bound.

## 4. A coupled six-term family with larger scalar homology

The scalar homology dimension might still appear useful if it were
subadditive, or if sums of a small number of Chow terms had a uniform cap well
below 450. The following exact family disproves that premise.

Choose a common variable `c` and pairwise disjoint five-element coordinate
sets

\[
B_i=\{b_{i1},\ldots,b_{i5}\},
\qquad 1\le i\le r,
\]

inside the 36-dimensional variable space, and define

\[
T_i=c\prod_{a=1}^5 b_{ia},
\qquad
F_r=\sum_{i=1}^r T_i.
\tag{4.1}
\]

The audit uses `1<=r<=6`, so at most 31 variables are active.

### 4.1 Coupled derivative images are reconstructed, not assumed

Two supports in (4.1) meet only in `c`. Any monomial differential operator of
order three that is nonzero on `T_i` contains at least two variables from
`B_i`; one of order four contains at least three. It therefore annihilates
every `T_j` with `j!=i`. Conversely, each coordinate basis element of
`D_3(T_i)` or `D_2(T_i)` is obtained by its complementary monomial
differential operator, which isolates that summand. By linearity, the
catalectic images of the sum satisfy

\[
D_3(F_r)=\bigoplus_{i=1}^rD_3(T_i),
\qquad
D_2(F_r)=\bigoplus_{i=1}^rD_2(T_i).
\tag{4.2}
\]

This is a proof of equality for this family. It is not an identification of a
coupled image with a literal sum by notation. In particular, the preceding
first-Koszul images are direct and have total rank `705r`.

Set

\[
I_i=\delta_2\bigl(D_2(T_i)\otimes\Lambda^2V\bigr).
\]

Each `I_i` has dimension `8730` by (3.2). Since the non-common linear outputs
of distinct summands lie in disjoint coordinate spaces, an intersection
between different `I_i` can have polynomial output only in the line `kc`.

### 4.2 Exact pairwise intersections

Define the pure-common-output part

\[
P_i=I_i\cap\bigl(kc\otimes\Lambda^3V\bigr).
\]

Then

\[
P_i
=
k c\otimes\bigl(c\wedge B_i\wedge V\bigr).
\tag{4.3}
\]

For the forward inclusion, if `b in B_i`, then

\[
\delta_2(cb\otimes(c\wedge v))
=\pm c\otimes(c\wedge b\wedge v).
\]

Conversely, suppose `c tensor phi` lies in `I_i`. The next Koszul differential
annihilates every vector in `I_i`, so

\[
c\wedge\phi=0.
\]

Thus `phi` is divisible by `c`. A pure `c` output under `delta_2` can arise
only by differentiating the `b` factor of a quadratic `cb`, so `phi` also has
a factor in `B_i`. This proves (4.3).

For `i!=j`, equations (4.2)-(4.3) give

\[
I_i\cap I_j
=
k c\otimes(c\wedge B_i\wedge B_j),
\]

and hence

\[
\dim(I_i\cap I_j)=5\cdot5=25.
\tag{4.4}
\]

The pair intersections have disjoint coordinate wedge support, and there is no
triple intersection: a degree-three wedge cannot contain `c` and one variable
from each of three disjoint blocks. More precisely,

\[
I_i\cap\sum_{j<i}I_j
=
\bigoplus_{j<i}(I_i\cap I_j).
\tag{4.5}
\]

Therefore

\[
\boxed{
\operatorname{rank}\delta_2(F_r)
=8730r-25\binom r2.
}
\tag{4.6}
\]

Using the domain dimension `9450r` and the preceding rank `705r`, the exact
homology dimension is

\[
\boxed{
h_{2,4}(F_r)
=15r+25\binom r2.
}
\tag{4.7}
\]

For `r=1,...,6`, the values are

```text
15, 55, 120, 210, 325, 465.
```

In particular,

\[
h_{2,4}(F_2)=55>30=2h_{2,4}(T)
\]

and

\[
h_{2,4}(F_6)=465>450=h_{2,4}(\operatorname{perm}_6).
\]

The polynomial `F_6` is explicitly represented by six Chow terms. No claim
about its minimal Chow rank is required.

Let `M(r)` be any universal upper bound for scalar `h_{2,4}` on forms
represented by at most `r` Chow terms. The example forces

\[
M(6)\ge465>450=h_{2,4}(\operatorname{perm}_6).
\]

Therefore the standard comparison `h_{2,4}(f)>M(r)` cannot prove even that
`perm_6` needs more than six terms, much less 26. This does not rule out a
new exact-value classification based on the scalar integer alone; no such
classification theorem is currently available.

## 5. Deterministic replay

The script

```text
scripts/n6_second_koszul_homology_audit.py
```

performs two independent checks.

1. It evaluates the exact Betti-number and rank formulas, obtaining `450`,
   `15`, `127125`, and `8730`.
2. For every `1<=r<=6`, it reconstructs the full sparse matrix of `delta_2`
   for the coupled polynomial `F_r` from (4.1), ranks it over
   `F_1000003`, and checks agreement with the characteristic-zero formula
   (4.6).

The modular equality is a cross-check, not the source of the
characteristic-zero upper bound. The upper bound and exactness come from the
intersection proof (4.2)-(4.5).

The frozen payload is

```text
data/n6_second_koszul_homology_audit.json
```

and the regression test is

```text
tests/test_n6_second_koszul_homology.py
```

## 6. Route decision

```text
OUTPUT_DEGREE_TWO_RANK_WINDOW=CLOSED_EXACTLY
BASE_RANK_RATIO=15_NO_IMPROVEMENT
SCALAR_HOMOLOGY_UPPER_BOUND=REJECTED_FOR_LOWER_26
MULTIGRADED_OR_REPRESENTATION_STRUCTURE=OPEN_NOT_PROMOTED
ROUTE_SELECTED=NONE
```

The exact homology dimension is mathematically useful: it explains the former
rank gap and identifies its apolar origin. It is not a viable monotone scalar
upper-bound invariant. No large representation computation or new state tree is
authorized from this result alone.

## 7. Hidden assumptions and strongest objection

The rejected premise was that the size of the higher-Koszul homology should be
small or nearly additive on short Chow sums, so that a universal scalar ceiling
would separate the permanent from low-rank sums. The family (4.1) disproves that
premise exactly.

The strongest objection is that the permanent's 450-dimensional homology is
not an unstructured vector space. Alper and Rowlands place its minimal
quadratic relations in row-column multidegrees of type
`(2+2,1+1+1+1)` and their transposes. A multigraded or
representation-theoretic obstruction could survive even though scalar
dimension fails.

That objection is valid. This note does not close structural homology. It also
does not justify promoting that route: a first useful test would need an exact
invariant that is stable under arbitrary linear changes and coupled sums, not
merely under the coordinate torus of the permanent.

## 8. Reference and novelty boundary

The Betti formula (2.1) is from:

- Jarod Alper and Rowan Rowlands, *Syzygies of the apolar ideals of the
  determinant and permanent*, arXiv:1709.09286, Theorem 1.2(b).

The paper explicitly studies the quadratic relations of the permanent apolar
ideal. This repository does not claim novelty for that formula. The
identification with the present higher-wedge rank gap and the common-factor
route diagnostic require separate literature review before any novelty claim.

## 9. Reproduction

Run

```bash
python scripts/n6_second_koszul_homology_audit.py \
  --json /tmp/n6_second_koszul_homology_audit.json
python -m unittest \
  tests.test_n6_second_koszul_homology -v
```

Expected final marker:

```text
N6_SECOND_KOSZUL_HOMOLOGY_AUDIT_PASS
```
