# Cross-degree relation constraints on the twenty-term `n=6` residual

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`LOWER_27_FRONTIER` (N6-037).  The base field has characteristic zero.
The relation, shadow, and duality statements below are strict mathematical
consequences of N6-032.  The aggregate integer state in Section 6 is only a
diagnostic showing that the present scalar interfaces do not close.  This
note does **not** prove `ChowRank(perm_6)>=27` and makes no border-rank claim.

## 1. Setup

Assume hypothetically that

\[
 P=\operatorname{perm}_6=T_1+\cdots+T_{26}.
\tag{1.1}
\]

Use the six indices selected by N6-032 and put

\[
 R=T_1+\cdots+T_6,
 \qquad Q=T_7+\cdots+T_{26}.
\tag{1.2}
\]

Write

\[
 E_m=\mathcal D_m(P),\quad H_m=\mathcal D_m(R),
 \quad G_m=\mathcal D_m(Q).
\tag{1.3}
\]

For the residual terms set

\[
 U_{i,m}=\mathcal D_m(T_i),\qquad
 L_m=\sum_{i=7}^{26}U_{i,m},
\tag{1.4}
\]

and define the ordinary colored relation space

\[
 \mathcal K_m=\ker\left(
 \bigoplus_{i=7}^{26}U_{i,m}\longrightarrow L_m
 \right),
 \qquad \kappa_m=\dim\mathcal K_m.
\tag{1.5}
\]

N6-032 proves

\[
 \dim G_3\ge384,\qquad
 336\le\dim(E_3\cap G_3)\le380,
\tag{1.6}
\]

and every nonempty sub-sum of the displayed twenty residual terms is
centrally certified minimum.

## 2. The ordinary middle relation budget

Put

\[
 C_3=\sum_{i=7}^{26}\dim U_{i,3},qquad
 \rho=\kappa_3,
\tag{2.1}
\]

and let `delta` be the radical dimension of the central relation pairing on
`K_3`.  The exact central relation-pairing identity gives

\[
 \dim G_3=C_3-\rho-\delta.
\tag{2.2}
\]

Every sextic Chow term has middle rank at most twenty.  Hence

\[
 C_3\le400.
\tag{2.3}
\]

Combining (1.6)--(2.3) proves the first new constraint:

### Proposition 2.1

\[
 \boxed{\rho+\delta\le16.}
\tag{2.4}
\]

The same proof applies to every nonempty `s`-term sub-sum.  Indeed, N6-032
gives coupled middle rank at least `20s-16`, while its sum of individual
middle ranks is at most `20s`.  Thus its own middle relation dimension plus
its own pairing-radical dimension is at most sixteen.  This is compatible
with, but logically different from, the sharper universal radical bound
`delta<=9` supplied by central minimality.

Differentiating a relation in `K_4` gives a relation in `K_3`.  Therefore

\[
 \mathcal K_4\subseteq\mathcal K_3^{(1)}.
\tag{2.5}
\]

The arbitrary-degree vector-valued Macaulay theorem now gives

\[
 \kappa_4\le\rho^{\langle3\rangle}
 \le16^{\langle3\rangle}=25.
\tag{2.6}
\]

Consequently:

### Corollary 2.2

\[
 \boxed{\kappa_4\le25.}
\tag{2.7}
\]

Again, the same upper bound holds for the ordinary quartic relation space of
every residual sub-sum.  Notice the direction: central minimality bounds the
next relation space from above; it does not force the many quadratic
relations needed for a contradiction.

## 3. Quotient-colored relations and the strict shadow `203`

The relation space relevant to the permanent is larger than (1.5).  Define

\[
 \overline{\mathcal K}_m=
 \ker\left(
 \bigoplus_{i=7}^{26}U_{i,m}
 \longrightarrow (L_m+E_m)/E_m
 \right),
 \qquad \bar\kappa_m=\dim\overline{\mathcal K}_m.
\tag{3.1}
\]

N6-032 proves

\[
 \bar\kappa_3\ge320.
\tag{3.2}
\]

Differentiation preserves a relation modulo the permanent derivative tower,
so

\[
 \overline{\mathcal K}_3
 \subseteq\overline{\mathcal K}_2^{(1)}.
\tag{3.3}
\]

The degree-two vector-valued Macaulay bound yields

\[
 320\le\bar\kappa_2^{\langle2\rangle}.
\tag{3.4}
\]

The exact endpoints are

\[
 73^{\langle2\rangle}=314,qquad
 74^{\langle2\rangle}=322,
\tag{3.5}
\]

so this dimension-only prolongation argument gives merely

\[
 \bar\kappa_2\ge74.
\tag{3.6}
\]

The specific incidence with the permanent gives a much stronger result.  Let

\[
 S=E_3\cap G_3.
\]

Then `dim S>=336`, and all first derivatives of `S` lie in

\[
 E_2\cap G_2.
\tag{3.7}
\]

Apply the exact two-dimensional Bukh shadow theorem to the multiplicity-free
permanent derivative space.  The rational separators

\[
 x_-={293\over50},\qquad x_+={5861\over1000}
\tag{3.8}
\]

satisfy

\[
 \binom{x_-}{3}^{\!2}<336<\binom{x_+}{3}^{\!2},
\qquad
 202<\binom{x_-}{2}^{\!2}
 <\binom{x_+}{2}^{\!2}<203.
\tag{3.9}
\]

Thus

\[
 \dim\partial S\ge203.
\tag{3.10}
\]

### Proposition 3.1

\[
 \boxed{
 \dim(E_2\cap G_2)\ge203,
 \qquad \dim G_2\ge203,
 \qquad \bar\kappa_2\ge203.
 }
\tag{3.11}

#### Proof of the last inequality

Write `A_i=C_(4,2)(T_i)` and `A_Q=sum_i A_i`.  Choose a subspace
`W\subset\partial S` of dimension 203, and choose a linear section of
`A_Q` over `W\subset E_2\cap G_2`.
The map

\[
 s\longmapsto(A_7x_s,\ldots,A_{26}x_s)
\tag{3.12}
\]

is injective because its component sum is `A_Qx_s=s`.  That sum lies in
`E_2`, so (3.12) lands in `bar K_2`.  This proves the claim.  ∎

In particular, the raw number `bar kappa_3>=320` adds no scalar force beyond
(3.11): its Macaulay consequence is only 74.  The gain from 74 to 203 comes
from the actual coupled intersection `E_3\cap G_3`, not from the dimension of
the colored relation space alone.

## 4. A fixed-six dual constraint in degree four

Put

\[
 h=\dim H_3,qquad b=\dim(E_3\cap H_3).
\tag{4.1}
\]

The N6-032 inequalities `h<=2b` and `h>=120-2b/3`, together with its shadow
cutoff, give

\[
 45\le b\le64.
\tag{4.2}
\]

Let

\[
 A=C_{3,3}(P),\qquad B=C_{3,3}(R),qquad
 Z=A(\ker B)\subseteq E_3.
\tag{4.3}
\]

The map `A` induces a nondegenerate symmetric form `beta_P` on `E_3`.  For
`x in ker B` and `y in E_3`,

\[
 \beta_P(Ax,y)=\langle x,y\rangle.
\]

Therefore

\[
 Z^{\perp_{\beta_P}}=E_3\cap\operatorname{im}B
 =E_3\cap H_3,
\tag{4.4}
\]

and hence

\[
 \boxed{\dim Z=400-b.}
\tag{4.5}

Now put

\[
 J_4=E_4\cap H_4.
\tag{4.6}
\]

The permanent apolar pairing between `E_2` and `E_4` is perfect.  If
`z=x\mathbin\lrcorner P\in Z`, with
`x\mathbin\lrcorner R=0`, and

\[
 y=alpha\mathbin\lrcorner P
  =alpha'\mathbin\lrcorner R\in J_4,
\]

then for every linear differential operator `xi`,

\[
 \left\langle\xi\mathbin\lrcorner z,y\right\rangle_P
 = (\xi x\alpha')\mathbin\lrcorner R=0.
\tag{4.7}
\]

Thus

\[
 \partial Z\subseteq J_4^{\perp}
\tag{4.8}
\]

inside the perfect 225-dimensional `E_2`--`E_4` pairing.  Applying Bukh's
shadow theorem to the `(400-b)`-plane `Z subset E_3` proves:

### Proposition 4.1

\[
 \boxed{
 \dim J_4\le225-\operatorname{Shadow}_{3\to2}(400-b).
 }
\tag{4.9}

The exact integer table is:

| `b` | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dim J_4` upper | 15 | 15 | 16 | 16 | 16 | 17 | 17 | 17 | 18 | 18 |

| `b` | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dim J_4` upper | 18 | 19 | 19 | 19 | 20 | 20 | 21 | 21 | 21 | 22 |

This is a genuine off-central restriction.  It is not yet large enough by
itself.  If

\[
 d_2=\dim H_2=\dim H_4,\quad
 a_2=\dim(E_2\cap H_2),\quad t_2=d_2-a_2,
\tag{4.10}
\]

then the asymmetric double-quotient inequality gives

\[
 \dim G_2\ge225+t_2-\dim J_4.
\tag{4.11}
\]

The partial sum `R` cannot have `H_2 subset E_2`: the permanent derivative
tower would give `R\in E_2^{(4)}=\operatorname{span}(P)`, contradicting
minimality of (1.1)
and the already proved lower bound 26.  Hence `t_2>=1`.  At the worst endpoint
`b=64`, (4.11) therefore gives only `dim G_2>=204`.  This barely improves
the direct shadow 203 and remains far below the twenty-term quadratic cap
`20*15=300`.

## 5. Why the scalar interface does not close

The proved constraints control four different objects:

1. the ordinary middle relations `rho` and their pairing radical `delta`;
2. their quartic prolongation `kappa_4`;
3. the much larger relation space modulo the permanent tower `bar kappa_m`;
4. the fixed-six dual intersection `J_4`.

There is no proved scalar inequality coupling the small ordinary budget
`rho+delta<=16` to the large quotient relation space `bar kappa_3>=320`.
The vector-valued Macaulay theorem has the wrong strength and direction:
it converts 320 into only `bar kappa_2>=74`, already dominated by the shadow
lower bound 203.  Likewise, (4.11) still contains the uncontrolled quotient
dimension `t_2`.

The shared-factor and two-Chow collision examples elsewhere in the repository
rule out silently replacing these missing couplings by additivity.  Any next
step must retain the maps, the relation pairing, or a compatible Koszul
homology class, rather than only the displayed dimensions.

## 6. A simultaneous aggregate integer state

The replay records the following integers:

\[
 b=64, h=120, d_2=90, a_2=78, \dim J_4=22;
\tag{6.1}
\]

for the residual central data,

\[
 C_3=400, \rho=4, \delta=4,
 \dim G_3=392, \dim L_3=396,
\tag{6.2}
\]

with coupled and literal quotient dimensions 56 and 60, and hence 340
colored middle relations modulo `E_3`; and at quadratic degree,

\[
 C_2=300, \kappa_2=75, \kappa_4=5,
 \dim L_2=225, \dim G_2=220,
 \dim(E_2\cap G_2)=203.
\tag{6.3}

Taking `\dim(E_2\cap L_2)=203` gives 278 colored quadratic relations.  These
numbers satisfy every displayed scalar dimension consequence of
(2.2), (2.4), (2.6), (3.3)--(3.11), (4.9), and (4.11), together with the
fixed-six central bounds and the noncentral block-Sylvester bound

\[
 \dim G_2\ge C_2-\kappa_2-\kappa_4=220.
\tag{6.4}
\]

This is **not** a construction of twenty Chow terms, not a polynomial, and
not a counterexample to lower 27.  It proves only that the current aggregate
integer inequalities have a simultaneous feasible point.  Hereditary
sub-sum geometry and realizability impose further conditions not represented
by this diagnostic.

## 7. Minimal next computation

The smallest unresolved interface is the fixed-six off-central tuple

\[
 (b,h,t_2,\dim J_4)
\tag{7.1}
\]

under the condition that `R` is a six-term partial sum in `P=R+Q` with
`ChowRank(Q)<=20`.  A useful computation should therefore search exact
six-term models with high `b` and `h`, and record the **joint** rank of

\[
 C_{4,2}(P-R),
\tag{7.2}
\]

not just separate bounds on `t_2` and `J_4`.  The first target is the extremal
layer `b=64,h=120`; proving that (7.2) has rank above 300 would exclude it,
while a realizable low-rank example would identify the missing geometric
parameter.  Random floating-point ranks would be diagnostic only; a usable
certificate must be an exact rational/integer computation or a strict modular
nonzero minor with a characteristic-zero bridge.

## 8. Replay and boundary

Run

```text
python scripts/n6_lower27_cross_degree_relation_audit.py \
  --json data/n6_lower27_cross_degree_relation_audit.json
python -m unittest tests/test_n6_lower27_cross_degree_relation.py
```

The script uses only exact integers and `Fraction`.  It replays the two
Macaulay endpoints, every rational Bukh separator in the twenty-row fixed-six
table, the `336 -> 203` shadow, and every equality or inequality asserted for
the aggregate diagnostic state.

The surviving problem is geometric, not an omitted integer optimization.
N6-037 narrows that geometry but does not exclude a hypothetical 26-term
decomposition and therefore is not a lower-27 theorem.
