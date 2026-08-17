# Adversarial review: exact higher-Koszul Chow-term ranks

## Verdict

The simplex-block formula, complete-intersection recurrence, Gorenstein
duality, and low-wedge complexity gate are valid characteristic-zero
statements.

The result supplies an exact universal one-term denominator. It does not
compute the permanent-side middle-wedge rank and therefore does not create a
new Chow-rank lower bound.

## 1. Output-degree convention

The space `D_d(T)` is the degree-`d` derivative output space, not the space of
differential operators of order `d`. For a degree-`n` polynomial the
corresponding differentiation order is `n-d`.

Changing this convention reverses several binomial indices and invalidates the
formula.

## 2. The ambient dimension is `N=n^2`

Only `n` variables occur in an independent Chow term after a linear change of
coordinates, but the exterior factor is `Lambda^p(V)` for the complete ambient
space of dimension `N=n^2`.

The `N-n` inactive variables are essential. They generate the factor

```text
C(N-n,p-q)
```

in the exact rank formula and the linear generators in the complete-
intersection resolution. Replacing `N` by `n` computes a different map.

## 3. The intersection parameter `h=d` contributes zero

When `S` is contained in `W`, every possible differential variable is already
in the wedge, so the map vanishes. The rank sum therefore stops at `h<=d-1`.

Including the `h=d` block with an undefined negative binomial index is an
implementation error; treating it as a nonzero block is a mathematical error.

## 4. Directness of the block decomposition

The labels

```text
inactive support J
active intersection I
active union U
```

are preserved by the differential. They define distinct multidegrees and
therefore give a direct decomposition of source and target.

The proof does not merely partition source columns while allowing target
overlap.

## 5. Simplex-boundary rank

For a set of `r` vertices, the oriented boundary from `a`-subsets to
`(a-1)`-subsets has rank `C(r-1,a-1)`.

The statement uses the augmented simplex complex. It is not the rank of an
arbitrary incidence matrix and does not require a genericity assumption.

## 6. Degenerate Chow terms

The formula is exact for linearly independent factors. The denominator in a
rank-ratio lower bound must control every Chow term, including repeated or
dependent factors.

This is valid because all term matrices are polynomial in the factor
parameters and rank cannot increase under specialization. The theorem does
not claim that every degenerate term has the same rank.

## 7. Complete-intersection indexing

The term apolar ideal has

```text
N-n linear generators
n quadratic generators.
```

A Koszul-homology basis element using `d` quadratic and `p-d` linear
generators has homological degree `p` and polynomial degree `d`. Therefore

```text
dim H_(d,p)=C(n,d)C(N-n,p-d).
```

Using `C(N-n,p)` or `C(N-n,p-2d)` is an indexing regression.

## 8. The `d=1,p=1` exception

For output degrees `d>=2`,

```text
R_(n,d,1)=n^2*C(n,d)-C(n,d+1).
```

At `d=1`, inactive linear annihilators contribute homology and this familiar
formula is not valid without an extra correction. The replay checks the
first-Koszul regression only for `d>=2`.

## 9. Gorenstein duality changes both indices

The dual map is

```text
(d,p) <-> (n-d+1,n^2-p-1).
```

Changing only `p`, or using `n-d`, loses the source-target transpose pairing.

## 10. The low-wedge denominator uses only one sector

The inequality

```text
R_(n,d,p)>=C(n,d)C(N-n,p)
```

retains the `q=0` sector. It is a lower bound on the exact denominator, not an
equality except in special cases.

This is sufficient for a route ceiling because a larger true denominator can
only weaken the flattening ratio.

## 11. Route ceiling versus rank lower bound

The numerator in the low-wedge theorem is bounded by a source dimension.
Hence the result proves an upper limit on what the named rank-ratio method can
certify.

It does not prove:

- that the permanent map attains the source or target cap;
- a Chow-rank upper bound;
- a lower bound equal to a source/target diagnostic; or
- an exact permanent-side rank.

The `n=6,d=3,p=12` diagnostic value 30 is not a proof of
`ChowRank(perm_6)>=30`.

## 12. Exterior distance and the logarithmic estimate

The relevant parameter is

```text
p_bar=min(p,n^2-p-1),
```

because of Gorenstein duality.

For `r=p_bar<=N-n`,

```text
log[C(N,r)/C(N-n,r)]
 <= r*n/(N-n-r+1).
```

The conclusion `r>=(1/2-o(1))*n*log(n)` additionally assumes `r=o(N)`.
Without that assumption the theorem states only the coarser `Omega(n log n)`
requirement in the range `r<=N/2`.

## 13. Relation to existing higher-wedge computations

The previous `n=6,p=2` audit used modular lower bounds and a complex-theoretic
upper bound. The present exact term formula resolves the previously open
one-term degree-two window as

```text
R_(6,2,2)=8730.
```

It does not retroactively promote any unresolved modular permanent rank to a
characteristic-zero equality.

## 14. Strongest objection

The low-wedge barrier leaves the exterior middle range almost entirely open.
The finite source/target diagnostics suggest that the strongest members of the
route occur there.

This objection is correct. The present result is a complexity gate, not a
complete higher-Koszul ceiling. A valid continuation must either:

1. prove a uniform middle-wedge ceiling;
2. compute a permanent-side middle-wedge rank with a characteristic-zero
   certificate; or
3. retain representation-valued homology rather than only total image
   dimension.

## 15. Independent replay boundary

The primary implementation evaluates the simplex-block formula.

The independent implementation:

- imports none of the primary functions;
- reconstructs ranks from complete-intersection Koszul homology;
- builds full sparse higher-Koszul matrices for every bidegree at `n=2,3`;
- checks Gorenstein duality through `n=16`; and
- reproduces the exact `n=6,p=2` term ranks.

## 16. Final classification

```text
exact independent-term rank formula        PASS
degenerate-term universal upper bound      PASS
complete-intersection recurrence           PASS
Gorenstein rank duality                     PASS
low-wedge route ceiling                     PASS
o(n log n) exterior distance reaches Glynn NO
middle-wedge route                          OPEN
new numerical Chow-rank lower bound         NO
permanent-side middle-wedge rank            OPEN
border-rank claim                           NO
exact rank for n>=6                         OPEN
literature novelty                          NOT ESTABLISHED
merge readiness                             PENDING EXACT-HEAD HOSTED CI
```
