# Adversarial review: complete first-excess zero theorem

## Review boundary

Reviewed new claim:

\[
\mathcal D_3(\operatorname{perm}_5)
\cap
\left(
\mathcal D_3(T_1)+\mathcal D_3(T_2)
\right)=0
\]

for arbitrary degree-five Chow terms.  Together with the parent first-excess
circuit theorem, this closes `q*n=m^2+1` for every `m>=3` and `q>=2`.

The review assumes the exact arbitrary-subspace product-shadow theorem and the
parent one-hot first-excess reduction.  It does not assess literature novelty
or border rank.

## Findings

### C-01 — Is `(5,3,2)` really the only missing arithmetic row?

**Attack.**  A second cubic divisor row could be omitted.

**Resolution.**  `q*n=3^2+1=10`, with `n>=3` and `q>=2`.  The only factorization
is `n=5,q=2`; `n=10,q=1` is outside the multi-term theorem.  Both the parent
and independent scans check this exactly.  `PASS`.

### C-02 — Does the argument use only coordinate quadratic subspaces?

**Attack.**  Enumerating two coordinate rectangles is insufficient for an
arbitrarily oriented subspace of `D_2(perm_5)`.

**Resolution.**  The coordinate enumeration is only the finite interface of
the already proved exact product-shadow theorem.  That theorem first
specializes an arbitrary subspace by the row-column torus without increasing
its derivative shadow and then applies two coordinatewise colex
compressions.  Consequently the coordinate minimum `F_(5,2)(2)=6` is the
minimum for every two-plane, not only coordinate ones.  `PASS`.

### C-03 — Is the two-rectangle minimum actually six?

**Attack.**  Two distinct `2 x 2` derivative supports might overlap in three
cells and have union five.

**Resolution.**  Each support is a Cartesian product `A x B` with
`|A|=|B|=2`.  Distinct products intersect in at most two cells: intersection
size is `|A_1 intersect A_2| |B_1 intersect B_2|`, and size four would make the
rectangles equal.  Thus the union has at least `4+4-2=6`.  Equality is attained
by keeping one two-set fixed and allowing the other two-sets to share one
element.  The independent implementation checks all 4,950 unordered pairs.
`PASS`.

### C-04 — Does shadow budget five imply intersection dimension at most one?

**Attack.**  The inverse threshold could be off by one.

**Resolution.**  Exact values are

```text
F_(5,2)(1)=4
F_(5,2)(2)=6.
```

Therefore `Gamma_(5,2)(5)=1`.  Every quadratic in `Sym^2 L` has all first
derivatives in `L`, so a five-plane supplies shadow budget at most five.
Hence `dim(E_2(5) intersect Sym^2 L)<=1`.  `PASS`.

### C-05 — Why does conciseness give five independent polar quadrics?

**Attack.**  A concise cubic might have a nontrivial directional derivative
kernel.

**Resolution.**  If a nonzero covector `alpha` satisfies
`alpha contraction f_i=0`, choose a coordinate in the direction `alpha`.
Characteristic zero then implies that `f_i` is independent of that variable,
so its essential space is a proper subspace.  Thus the polar map from
`L_i^*` is injective for a concise cubic.  The direct branch produces a
five-dimensional polar space.  `PASS`.

### C-06 — Can every direct-branch polar be isolated from the second term?

**Attack.**  The ambient covector extending a covector on `L_1` might affect
`f_2`.

**Resolution.**  In the direct branch `U=L_1 direct_sum L_2`.  Every covector
on `L_1` has an extension annihilating `L_2`.  Contracting the selected
intersection element therefore gives exactly the corresponding polar of
`f_1`, and it remains in `D_2(perm_5)`.  `PASS`.

### C-07 — Is the circuit private covector space four-dimensional?

**Attack.**  The restrictions of covectors annihilating the other block could
be smaller than the full annihilator of the overlap line.

**Resolution.**  For subspaces `L_1,L_2` with five-dimensional blocks and
one-dimensional intersection, the restriction map

```text
Ann(L_2) -> L_1^*
```

has image exactly `Ann(L_1 intersect L_2)`.  This follows by extending any
functional on `L_1` that vanishes on the intersection to the quotient
`(L_1+L_2)/L_2`.  Its dimension is four.  `PASS`.

### C-08 — Could the four circuit polars become dependent?

**Attack.**  Restricting the polar map to a four-plane might lower its rank.

**Resolution.**  The full polar map is injective by conciseness, so every
restriction is injective.  The private circuit polar subspace has dimension
four, still larger than the inverse capacity one.  `PASS`.

### C-09 — Does the proof silently claim the components themselves lie in the
permanent derivative space?

**Attack.**  Only the sum `f=f_1+f_2` belongs to `E_3(5)`.

**Resolution.**  The proof never asserts `f_i in E_3(5)`.  It uses ambient
covectors that annihilate the other component.  The isolated polar is then
literally a derivative of `f`, so it belongs to `E_2(5)`, while simultaneously
being a polar of `f_i` supported in `L_i`.  `PASS`.

### C-10 — Is the statement overpromoted to one term or second excess?

**Attack.**  The one-term endpoint has an embedded subpermanent
counterexample, and no argument treats `q*n=m^2+2`.

**Resolution.**  The theorem explicitly requires `q>=2` and stops at
`q*n<=m^2+1`.  The next open excess is recorded as two.  `PASS`.

## Independent finite replay

The primary replay invokes the canonical exact product-shadow implementation
and reconstructs the parent divisor boundary.  A separate implementation
imports neither source: it enumerates all one hundred coordinate rectangles
and all 4,950 unordered pairs, obtaining minimum union six and an explicit
equality witness.

The finite computation verifies the sharp numerical interface.  Transfer to
arbitrary subspaces is the already proved exact product-shadow theorem, not a
finite-field or coordinate extrapolation.

## Final review decision

```text
FATAL=0
MAJOR=0
MINOR=0
DECISION=PROOF_DRAFT_COMPLETE_FIRST_EXCESS_CLOSED
```

No exact-rank, border-rank or literature-novelty conclusion is promoted.
