# A fixed-six relation-tableau proof of `ChowRank(perm_6)>=25`

## Status

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`. The exact arithmetic is replayed in

```text
scripts/n6_fixed_six_lower25_audit.py
```

The finite replay has been run by two independent implementations. The key
vector-valued prolongation lemma has a separate universal-bundle and explicit
one-parameter-subgroup proof in
`docs/vector_valued_macaulay_prolongation.md`. External peer review and an
exhaustive literature-novelty review have not been performed.

## 1. Statement and coupling boundary

Let

\[
P=\operatorname{perm}_6.
\]

The claim of this note is:

### Theorem 1.1

Over every characteristic-zero field,

\[
\boxed{\operatorname{ChowRank}(P)\ge25.}
\]

Assume for contradiction that

\[
P=T_1+\cdots+T_{24}
\tag{1.1}
\]

is a 24-term Chow decomposition. Fix six terms and put

\[
R=T_1+\cdots+T_6,
\qquad
Q=P-R.
\]

Thus `Q` is a sum of eighteen Chow terms.

All derivative spaces of `R` below are the **coupled catalectic images of
the sum**. Literal sums of the individual derivative spaces are used only
as ambient spaces or after an explicit relation-kernel argument. No
uncoupled/coupled rank equality is assumed.

At central degree three, set

\[
E_3=\mathcal D_3(P),
\qquad
H_3=\mathcal D_3(R),
\]

\[
b=\dim(E_3\cap H_3),
\qquad
h=\dim H_3.
\tag{1.2}
\]

At quadratic degree, put

\[
E_2=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+\cdots+G_6.
\tag{1.3}
\]

For every degree-six Chow term,

\[
\dim G_i\le15,
\qquad
\dim(E_2\cap G_i)\le3.
\tag{1.4}
\]

The second inequality is the universal individual-factor intersection
theorem already proved in the repository.

## 2. The raw fixed-six interval is `40<=b<=64`

### Lemma 2.1 — quadratic projection cap

\[
\boxed{\dim(E_2\cap U)\le78.}
\tag{2.1}
\]

### Proof

Let `X=E_2\cap U` and choose a section of the summation map

\[
G_1\oplus\cdots\oplus G_6\longrightarrow U
\]

over `X`. Project the lifted `X` to any five components. The image has
dimension at most `5*15=75`. The kernel maps injectively to the omitted
individual intersection `E_2\cap G_j`, whose dimension is at most three.
Thus `dim X<=75+3=78`. ∎

Let

\[
S=E_3\cap H_3.
\]

Every first derivative of `S` lies in both `E_2` and the coupled quadratic
image `D_2(R)`, hence

\[
\partial S
\subseteq
E_2\cap\mathcal D_2(R)
\subseteq E_2\cap U.
\]

Therefore

\[
\dim\partial S\le78.
\tag{2.2}
\]

Bukh's two-dimensional shadow theorem, applied after a generic row-column
torus degeneration of the multiplicity-free permanent derivative space,
then gives

\[
\boxed{b\le64.}
\tag{2.3}
\]

The exact replay uses the rational separator

\[
x_0=\frac{947}{200},
\]

for which

\[
\binom{x_0}{3}^2<65,
\qquad
\binom{x_0}{2}^2>78.
\]

Hence `b>=65` would force the integer shadow to be at least 79, contradicting
(2.2).

At central degree, the symmetric middle-catalectic double-quotient
inequality gives

\[
\operatorname{rank}C_{3,3}(Q)
\ge400+h-2b.
\]

The eighteen residual terms have total central rank at most `18*20=360`.
Consequently

\[
h\le2b-40.
\tag{2.4}
\]

Since `h>=b`, equations (2.3)--(2.4) give

\[
\boxed{40\le b\le64.}
\tag{2.5}
\]

## 3. The two lowest layers are already Koszul-strict

The quotient-Koszul residual inequality gives

\[
\operatorname{rank}K_3(Q)
\ge14175-36b+\Gamma,
\qquad
\Gamma\ge0.
\tag{3.1}
\]

The eighteen residual terms have total capacity

\[
18\cdot705=12690.
\]

For `b=40,41`, the right side of (3.1) with `Gamma=0` is respectively

\[
12735,
\qquad
12699,
\]

so both exceed 12690. Therefore `b=40,41` are impossible.

It remains to exclude

\[
42\le b\le64.
\tag{3.2}
\]

## 4. A vector-valued Macaulay lemma

Let `W` be a finite-dimensional color space and let

\[
\mathcal K\subseteq W\otimes\operatorname{Sym}^2V
\]

be a `k`-dimensional subspace. Define its first prolongation by

\[
\mathcal K^{(1)}
=
\left\{
F\in W\otimes\operatorname{Sym}^3V:
\partial_\xi F\in\mathcal K
\text{ for all }\xi\in V^*
\right\}.
\tag{4.1}
\]

Write `M(k)=k^{<2>}` for the degree-two Macaulay successor.

### Lemma 4.1 — vector-valued Macaulay cap

For arbitrary finite-dimensional `W` and every `k>=0`,

\[
\boxed{\dim\mathcal K^{(1)}\le M(k).}
\tag{4.2}
\]

The required values are

\[
\begin{array}{c|rrrrrrrrrrrrrrrrr}
k&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16\\
\hline
M(k)&0&1&2&4&5&7&10&11&13&16&20&21&23&26&30&35&36.
\end{array}
\tag{4.3}
\]

### Proof

Put

\[
A=W\otimes\operatorname{Sym}^2V,
\qquad
B=W\otimes\operatorname{Sym}^3V,
\]

and work on `Gr(k,A)`. Let `S` be the tautological subbundle and `Q` the
quotient bundle. Polarization gives a canonical map

\[
B\otimes\mathcal O
\longrightarrow
Q\otimes V,
\]

whose fiber kernel at `[K]` is exactly `K^(1)`. Fiber nullity is upper
semicontinuous.

Choose bases `e_a` of `W` and `x_i` of `V`. Set

\[
\beta_i=3^i,
\qquad
L=1+2\cdot3^{\dim V-1},
\qquad
\gamma_a=aL.
\]

The weights `gamma_a+beta_i+beta_j`, with `i<=j`, are pairwise distinct:
ternary pair sums are unique within one color, and their total range is
smaller than the color stride `L`. The resulting diagonal one-parameter
subgroup on `W` and `V` degenerates `K` to a coordinate colored-monomial
subspace

\[
\mathcal K_0
=
\bigoplus_a e_a\otimes P_a,
\qquad
\sum_a\dim P_a=k.
\]

Equivariance keeps the prolongation dimension constant away from the limit,
and upper semicontinuity gives

\[
\dim\mathcal K^{(1)}
\le
\dim\mathcal K_0^{(1)}.
\]

Differentiation preserves color, so

\[
\mathcal K_0^{(1)}
=
\bigoplus_a e_a\otimes P_a^{(1)}.
\]

The scalar Macaulay theorem gives

\[
\dim P_a^{(1)}
\le M(\dim P_a).
\]

The degree-two Macaulay successor is superadditive:

\[
M(a)+M(b)\le M(a+b).
\tag{4.4}
\]

Choose sharp scalar Macaulay spaces for `a` and `b` in disjoint variable
sets. Their direct sum has dimension `a+b`, and its prolongation contains
the direct sum of the two sharp prolongations. Applying the scalar bound to
that direct sum proves (4.4). Iteration now gives

\[
\dim\mathcal K^{(1)}
\le
\sum_aM(\dim P_a)
\le
M(k).
\]

The companion note supplies the apolar proof of the scalar identification,
the universal-bundle construction, and the explicit weight separation in
full detail. The exact audit verifies all six-part partition inequalities
through `k=16`; a separate exhaustive divided-power calculation scans all
2,825 subspaces in the smallest nontrivial two-color model as a diagnostic
counterexample search. ∎

This lemma concerns the full colored relation module. It is stronger than
bounding the six scalar component prolongations separately.

## 5. Quadratic relations bound all cubic relations

Let

\[
\mathcal K
=
\ker\left(
G_1\oplus\cdots\oplus G_6\longrightarrow U
\right),
\qquad
\kappa=\dim\mathcal K.
\tag{5.1}
\]

Let

\[
C_i=\mathcal D_3(T_i)
\]

and define the cubic relation kernel

\[
\mathcal R
=
\ker\left(
C_1\oplus\cdots\oplus C_6
\longrightarrow
C_1+\cdots+C_6
\right),
\qquad
\rho=\dim\mathcal R.
\tag{5.2}
\]

For every `(c_1,...,c_6)\in R` and every direction `xi`,

\[
(\partial_\xi c_1,\ldots,\partial_\xi c_6)\in\mathcal K.
\]

Therefore

\[
\mathcal R\subseteq\mathcal K^{(1)}.
\tag{5.3}
\]

Whenever `kappa<=16`, Lemma 4.1 gives

\[
\boxed{\rho\le M(\kappa).}
\tag{5.4}
\]

No classification of ternary, quaternary, or higher cubic relation
components is used.

## 6. Coupled central rank from the relation module

Let

\[
A_i=C_{3,3}(T_i),
\qquad
A=C_{3,3}(R)=A_1+\cdots+A_6,
\]

and use divided-power bases so that every `A_i` is symmetric. Put

\[
c_i=\operatorname{rank}A_i=\dim C_i,
\qquad
C=\sum_i c_i.
\]

### Lemma 6.1 — block-Sylvester bound

\[
\boxed{h=\operatorname{rank}A\ge C-2\rho.}
\tag{6.1}
\]

### Proof

Let `D=diag(A_1,...,A_6)`, let `Sigma` sum the six target copies, and let
`Delta` diagonally embed the common source. Then

\[
A=\Sigma D\Delta.
\]

Both `rank(Sigma D)` and `rank(D Delta)` equal `C-rho`: the first is the
dimension of the sum of the image spaces, and the second is the dimension
of the sum of the row spaces; symmetry identifies the latter with the
former. Since `rank D=C`, Frobenius--Sylvester gives

\[
\operatorname{rank}A
\ge(C-\rho)+(C-\rho)-C
=C-2\rho.
\]

∎

Combining (5.4) and (6.1),

\[
\boxed{h\ge\sum_i c_i-2M(\kappa).}
\tag{6.2}
\]

## 7. Exact defect arithmetic

For each fixed term define

\[
\varepsilon_i=15-\dim G_i,
\]

\[
\alpha_i
=
3-\dim(E_2\cap G_i).
\tag{7.1}
\]

Let `m_b` be the certified integer lower bound for the quadratic shadow of a
`b`-dimensional central permanent subspace. The exact values needed for
`42<=b<=64` are

\[
\begin{array}{c|rrrrrrrrrrrr}
b&42&43&44&45&46&47&48&49&50&51&52&53\\
\hline
m_b&62&62&63&64&65&66&66&67&68&69&69&70
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrr}
b&54&55&56&57&58&59&60&61&62&63&64\\
\hline
m_b&71&72&72&73&74&75&75&76&77&77&78.
\end{array}
\tag{7.2}
\]

Every row is certified by a rational separator, not by a floating root.

The omitted-factor projections give, for every `j`,

\[
\sum_{i\ne j}\varepsilon_i+\alpha_j
\le78-m_b.
\tag{7.3}
\]

Put

\[
D_b=78-m_b.
\]

The quotient image of `G_i` modulo `E_2` has dimension

\[
12-\varepsilon_i+\alpha_i.
\]

Since `dim(E_2\cap U)>=m_b`, the quadratic relation dimension satisfies

\[
\begin{aligned}
\kappa
&\le
90-\sum_i\varepsilon_i
-m_b
-\max_i(12-\varepsilon_i+\alpha_i)\\
&=
D_b-\sum_i\varepsilon_i-\max_i(\alpha_i-\varepsilon_i)\\
&\le
D_b-\sum_i\varepsilon_i+\min_i\varepsilon_i.
\end{aligned}
\tag{7.4}
\]

Equation (7.3) implies

\[
\sum_i\varepsilon_i-\min_i\varepsilon_i\le D_b,
\]

so the final cap in (7.4) is nonnegative and at most `D_b<=16`.

For the individual central ranks, the exact degree-six term profiles give

\[
\begin{array}{c|ccccc}
\dim G_i&11&12&13&14&15\\
\hline
\text{possible?}&\text{yes}&\text{no}&\text{yes}&\text{yes}&\text{yes}\\
c_i\text{ lower bound}&14&-&18&20&20.
\end{array}
\tag{7.5}
\]

The audit deliberately assigns lower bound zero when `dim G_i<=10`.
Thus no classification of those low profiles is used.

For every symmetric epsilon type satisfying (7.3), the script:

1. rejects any type containing the impossible dimension 12;
2. computes the conservative individual central-rank sum;
3. applies the relation cap (7.4);
4. applies `rho<=M(kappa)` and (6.2);
5. compares the result with the residual upper bound `h<=2b-40`.

The minimum coupled lower bounds are:

| `b` | `m_b` | `D_b` | minimum lower bound for `h` | residual upper bound `2b-40` | margin |
|---:|---:|---:|---:|---:|---:|
| 42 | 62 | 16 | 48 | 44 | 4 |
| 43 | 62 | 16 | 48 | 46 | 2 |
| 44 | 63 | 15 | 50 | 48 | 2 |
| 45 | 64 | 14 | 60 | 50 | 10 |
| 46 | 65 | 13 | 68 | 52 | 16 |
| 47 | 66 | 12 | 74 | 54 | 20 |
| 48 | 66 | 12 | 74 | 56 | 18 |
| 49 | 67 | 11 | 78 | 58 | 20 |
| 50 | 68 | 10 | 80 | 60 | 20 |
| 51 | 69 | 9 | 88 | 62 | 26 |
| 52 | 69 | 9 | 88 | 64 | 24 |
| 53 | 70 | 8 | 92 | 66 | 26 |
| 54 | 71 | 7 | 96 | 68 | 28 |
| 55 | 72 | 6 | 98 | 70 | 28 |
| 56 | 72 | 6 | 98 | 72 | 26 |
| 57 | 73 | 5 | 100 | 74 | 26 |
| 58 | 74 | 4 | 110 | 76 | 34 |
| 59 | 75 | 3 | 112 | 78 | 34 |
| 60 | 75 | 3 | 112 | 80 | 32 |
| 61 | 76 | 2 | 116 | 82 | 34 |
| 62 | 77 | 1 | 118 | 84 | 34 |
| 63 | 77 | 1 | 118 | 86 | 32 |
| 64 | 78 | 0 | 120 | 88 | 32 |

Every margin is strictly positive. Hence every layer in (3.2) contradicts
the eighteen-term central-rank upper bound.

## 8. Lower 25

Sections 3 and 7 exclude every integer state in (2.5). Therefore the
hypothetical 24-term decomposition (1.1) cannot exist.

Over an algebraic closure of any characteristic-zero base field,

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge25.
\]

A decomposition over the original field would survive scalar extension, so
the same lower bound holds over every characteristic-zero field.

Glynn's identity gives 32 terms. Thus the proposed new interval is

\[
\boxed{
25
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
}
\]

## 9. Dependency and adversarial audit

The proof does **not** assume any of the following:

- equality between a coupled catalectic image and the literal sum of
  individual derivative spaces;
- additivity of quotient Koszul gain;
- a classification of cubic relations by number of essential variables;
- a classification of degree-six terms with quadratic rank at most ten;
- the earlier `b=25,26,27` fixed-four exclusions;
- the extremal six-plane classification.

The new dependencies are:

1. the universal individual quadratic-intersection cap three;
2. Bukh's two-dimensional shadow theorem and its torus-semicontinuity bridge;
3. the scalar Macaulay theorem;
4. the colored-monomial degeneration and Macaulay superadditivity in Lemma 4.1;
5. symmetry of the middle catalectics and Frobenius--Sylvester;
6. the exact degree-six profiles at quadratic dimensions 11--15.

The principal former objection was Lemma 4.1. It is now written as an
explicit vector-bundle kernel on `Gr(k,W tensor Sym^2 V)`, with a concrete
integer one-parameter subgroup whose colored quadratic weights are all
distinct. The separate audit verifies that finite interface and the complete
six-color partition inequality through `k=16`. The remaining mathematical
uncertainty is external peer review, not an identified gap in the internal
proof chain.

## 10. Reproduction

Run

```bash
python scripts/n6_fixed_six_lower25_audit.py \
  --json /tmp/n6_fixed_six_lower25.json
```

Then run the independent labelled replay:

```bash
python scripts/n6_fixed_six_lower25_independent_audit.py
python scripts/vector_valued_macaulay_audit.py \
  --json /tmp/vector_valued_macaulay_audit.json
python -m unittest discover -s tests -v
```

Expected final markers:

```text
N6_FIXED_SIX_LOWER25_AUDIT_PASS
N6_FIXED_SIX_LOWER25_INDEPENDENT_AUDIT_PASS
VECTOR_VALUED_MACAULAY_AUDIT_PASS
```

The primary script validates all rational shadow separators, reconstructs
the degree-six term profiles, checks the module partition identity through
relation dimension 16, exhausts every symmetric epsilon type, and verifies
all strict margins. The independent implementation scans all
`binom(21,6)=54,264` nondecreasing epsilon multisets without importing the
primary generator and uses exact multinomial weights to account for all
`16^6` labelled tuples. Neither finite program replaces the algebraic
arguments in Sections 2, 4--6.
