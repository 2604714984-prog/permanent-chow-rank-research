# Adversarial review: all-wedge standard Koszul--Young route ceiling

## Verdict

The one-term quarter-rank theorem and the resulting

```text
4*binom(n,floor(n/2))
```

ceiling are valid for the standard exterior Koszul--Young flattenings and
finite block-diagonal direct sums of them.

The theorem is a ceiling on a named lower-bound mechanism, not an upper bound
on actual Chow rank.

## 1. Definition boundary

The map must be the standard polarization followed by the algebraic exterior
derivative.  The theorem does not automatically cover:

- a projection to selected Schur isotypes;
- an arbitrary Pieri map;
- nonlinear minors or joint determinantal data;
- a higher differential in a minimal free resolution; or
- a matrix obtained after term-dependent preprocessing.

Calling all of these objects “Young flattenings” does not place them inside the
proved class.

## 2. Why one independent term is enough

A Chow-rank lower bound from matrix rank divides by an upper bound valid for
every one-term rank, equivalently by the maximum one-term rank.  To prove a
route ceiling it is enough to exhibit one term with large rank.

The proof uses an independent-factor term.  It does not claim that degenerate
terms obey the same quarter-rank lower bound.

## 3. The ambient complement is essential

The term has only `n` active factors in `N=n^2` ambient directions.  The
exterior power decomposes according to the number of active and inactive
wedge directions.  Omitting the inactive multiplicities gives the wrong term
denominator for the permanent problem.

## 4. Simplex component rank

For fixed intersection and union of the monomial support and wedge support,
the active differential is the oriented boundary of a simplex.  Its rank is

```text
binom(r-1,q-1)
```

over characteristic zero.  The argument would fail in characteristics where
the relevant boundary ranks change.  The repository theorem is explicitly
characteristic zero.

The smaller side is determined by `a<=m-1` versus `a>=m`; it is independent of
the component intersection size.  This independence is what permits the
one-half active estimate after summing components.

## 5. Hypergeometric coupling

The adjacent exterior-layer overlap uses two different complete dimensions:

```text
A=binom(n,m)*binom(N,p)
B=binom(n,m-1)*binom(N,p+1).
```

The sum of reachable target blocks omits the all-inactive wedge component.
The proof does not incorrectly identify that sum with `B`.  Instead it uses
`B_a/B` as the probability that a uniform `(p+1)`-subset has exactly `a+1`
active elements.

After orienting so `A<=B`, the coupling obtained by adding one random element
leaves only the event `X=Y=m` uncovered.  The adjacent-probability comparison
is derived from `A<=B`; it is not a generic median assertion.

If `m-1` is outside the support while `m` is inside, direct substitution shows
`A>B`, so this boundary case cannot occur in the selected orientation.

## 6. The constant four is safe, not claimed optimal

Two factors of one half enter:

1. the simplex boundary rank versus its smaller chain group;
2. the overlap between adjacent active-wedge decompositions.

Finite diagnostics suggest a smaller best constant, but no optimization of the
constant is claimed.  The asymptotic route classification needs only a fixed
constant.

## 7. Transpose duality

When the term source is larger than the target, the proof invokes

```text
K_(m,p)^T = +/- K_(n-m+1,N-p-1).
```

Both the permanent rank and every one-term rank are preserved.  Applying the
quarter-rank argument without this reorientation would leave an unjustified
case.

## 8. Coupled/literal boundary

The route uses a flattening linear in the polynomial, so rank subadditivity is
legitimate.  It does not identify the catalectic image of a sum with the
literal direct sum of termwise derivative spaces.

## 9. Direct sums only

A block-diagonal direct sum preserves the ceiling because the same independent
term supplies all term denominators simultaneously.  An arbitrary projection
or quotient of the block diagonal map may reduce the term ranks more than the
permanent rank; such representation-selective operations are not covered.

## 10. Strongest objection

The standard maps may be too coarse precisely because they retain the full
ambient exterior modules.  A carefully chosen `S_n x S_n` isotype projection
could, in principle, remove most of an arbitrary Chow term while preserving a
large permanent component.

This objection is correct.  The theorem closes the unprojected standard route
and directs the next research toward representation-valued projections rather
than another exterior degree scan.

## 11. Final classification

```text
standard Koszul--Young maps, all p,m=PASS
finite block-diagonal direct sums=PASS
route ceiling=4*central binomial
new numerical Chow-rank lower bound=NO
actual Chow-rank upper bound=NO
representation-projected Young maps=OPEN
arbitrary Pieri maps=OPEN
higher syzygy modules=OPEN
Chow-realizability defects=OPEN
border-rank improvement=NO
exact rank for n>=6=OPEN
literature novelty=NOT ESTABLISHED
```
