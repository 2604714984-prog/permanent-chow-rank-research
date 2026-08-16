# Adversarial review of cross-degree block projection

## Verdict

```text
MATHEMATICAL_TEXT=PASS_AS_INTERNAL_PROOF_DRAFT
EXACT_SHADOW_DEPENDENCY=REUSED_WITHOUT_RECLAIMING_NOVELTY
COUPLED_LITERAL_FIREWALL=PASS
PRIMARY_REPLAY=PENDING_HOSTED_CI
INDEPENDENT_REPLAY=PENDING_HOSTED_CI
NEW_COUNTEREXAMPLE_FOUND=false
BORDER_RANK_CLAIM=false
EXACT_RANK_CLAIM=false
```

The reviewed promotions are only

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge45,
\qquad
\operatorname{ChowRank}(\operatorname{perm}_8)\ge80.
\]

## 1. The new logical step

The exact product-shadow theorem and the linear section/projection lemma are
pre-existing inputs.  The new step is their composition across two derivative
degrees:

1. differentiate a permanent-relative block intersection;
2. bound the resulting lower-degree intersection by projecting away all but
   one term and retaining the exact one-term defect;
3. invert the exact permanent shadow at the original degree.

This attribution is explicit.  The result is not presented as a new proof of
Kruskal--Katona compression or of the general shadow formula.

## 2. Coupled versus literal sums

For

\[
R=\sum_iT_i,
\]

the argument uses only

\[
\mathcal D_d(R)
\subseteq
\sum_i\mathcal D_d(T_i).
\]

The block cap is proved for the larger literal sum and therefore applies to
the coupled image.  No equality is assumed, and no termwise derivative-space
sum is assigned the rank of a coupled catalectic matrix.

This is the same semantic firewall required by the repaired `perm_5` proof.

## 3. Single-term lower-degree cap

For a Chow term `T`, all factors lie in a space `L_T` of dimension at most
`n`, including repeated or dependent factors.  Therefore every order-`e-1`
derivative of a subspace of `D_e(T)` lies in `L_T`.

The exact permanent shadow gives

```text
n=7,e=2: cap 3 because F(3)=6 <=7 <8=F(4)
n=8,e=2: cap 6 because F(6)=8 <=8 <9=F(7).
```

The direction is correct: the exact shadow is a lower bound on the derivative
space of a permanent-side subspace, while the factor span supplies the upper
bound.

## 4. Section/projection kernel

Let

\[
\pi:\bigoplus_iG_i\to\sum_iG_i
\]

be summation, and choose a section over the permanent-relative intersection.
After projection to `q-1` components, a kernel vector is supported in the
omitted component.  Its sum lies in the permanent space and in that component.
The section makes this kernel-to-intersection map injective.

No direct-sum assumption among the `G_i` is used.  The resulting capacities
are exactly

```text
n=7: 3*binom(7,2)+3 = 66
n=8: 4*binom(8,2)+6 = 118.
```

## 5. Cross-degree transfer

If

\[
A\subseteq E_d(n)\cap\sum_iD_d(T_i),
\]

then every first derivative lies both in `E_(d-1)(n)` and in the lower-degree
literal sum.  Consequently

```text
dim partial(A) <= 66  for the n=7 four-term block,
dim partial(A) <=118  for the n=8 five-term block.
```

The exact upper-degree transitions are

```text
F_(7,3)(41)=66,  F_(7,3)(42)=69,
F_(8,3)(112)=118, F_(8,3)(113)=120.
```

Thus the block caps 41 and 112 follow with no monotonicity reversal.

## 6. Outer multishadow arithmetic

### `perm_7`

Seventeen fixed terms are legitimate because the base stack already excludes
smaller ranks.  The outside thirteen terms contribute at most `13*35=455` at
the cubic derivative level; the four-term block contributes at most 41.

```text
capacity=496
F_(7,4)(263)=494
F_(7,4)(264)=497
residual=ceil((58800-49*263)/1680)=28
total=17+28=45.
```

### `perm_8`

The base stack proves lower 79, so seventeen terms may be fixed under a
hypothetical counterexample to lower 80.

```text
outside capacity=12*56=672
five-term cap=112
capacity=784
F_(8,4)(560)=784
F_(8,4)(561)=793
residual=ceil((310464-64*560)/4424)=63
total=17+63=80.
```

Every ceiling is strict in the required direction.

## 7. Strongest objections

### Objection A -- the five-term coordinate theorem already gave 40

The coordinate cap is stronger but applies only to fixed coordinate Chow
terms.  Flat specialization can retain nonliteral relation directions.  The
new cap 112 is weaker numerically but applies directly to arbitrary
characteristic-zero terms and therefore closes lower 80 without a flat-limit
transfer.

### Objection B -- the section depends on arbitrary choices

Only its existence is used.  Every linear surjection admits a section over the
finite-dimensional intersection, and the dimension estimate is independent
of the chosen section.

### Objection C -- a degenerate Chow term may have a larger derivative space

It cannot.  Its factor span has dimension at most `n`, and its degree-`e`
derivative space is contained in `Sym^e(L_T)`.  The proof uses no generic-rank
equality.

### Objection D -- exact shadow computation could be circular

The primary audit calls the already established exact Ferrers implementation.
The independent audit reconstructs the colex data and recurrence without
importing it.  The written torus-specialization and compression theorem, not
the program alone, is responsible for universality over arbitrary subspaces.

### Objection E -- lower 80 solves `perm_8`

It does not.  Glynn gives upper 128.  The new interval is `80..128`, and no
border-rank or exact-rank statement is made.

## 8. Next fail-closed boundary

A sufficient next target for lower 81 is a five-term cubic cap of 90.  The
current theorem proves 112.  This is recorded as a sufficient interface, not
as a claim that every possible lower-81 argument must pass through that exact
number.

The appropriate repository status is

```text
PROOF_DRAFT_COMPLETE
EXACT_INTEGER_REPLAYED
ORDINARY_LOWER_BOUND_PROMOTION
```

only after exact-head hosted CI succeeds.
