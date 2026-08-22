# Projected Koszul quotients for `perm_7`

## Result

This certificate tests a smaller family of exact Koszul flattenings without
constructing the full central matrix.  It does **not** improve the current
ordinary lower bound (49), but it identifies a concrete computational
boundary:

- the row projection has rank (29120) and gives the familiar lower bound
  (35);
- the cyclic projection
  \[
    x_{ij}\longmapsto e_{i+j\bmod 7}
  \]
  has exact rank (33920), hence gives lower bound
  \(lceil33920/832\rceil=41\);
- forty seeded seven-character Fourier quotients were replayed exactly.  Their
  best rank was (32928), again below the cyclic projection;
- none reaches the lower-50 threshold
  \(49\cdot832=40768\).

In fact the adjacent (K_{5,*}) calculations turn this observation into a
larger universal route barrier:

- no seven-dimensional projected (K_{4,3}) flattening gives more than
  lower (41);
- after adjoining inactive quotient directions and checking every wedge
  degree, **no projected (K_{4,p}) flattening with quotient dimension
  (7\leq k\leq49) can improve the established lower bound (49)**.

The largest capacity anywhere in this family has integer ceiling (47).

The ordinary bound remains

\[
49\leq \operatorname{ChowRank}(\operatorname{perm}_7)\leq64.
\]

## The projected flattening

For a linear quotient \(\pi:V\to Z\), define

\[
K^{\pi}_{4,3}(F):D_4(F)\otimes\bigwedge^3Z
 \longrightarrow D_3(F)\otimes\bigwedge^4Z
\]

by differentiating once and wedging the derivative variable after applying
\(\pi\).  Here \(\dim Z=7\).  For one seven-factor Chow term, the factor span
has dimension at most seven.  The exact generic one-term rank of this map is
(832); dependent or repeated factors are specializations and cannot increase
the rank.  Consequently a rank (R) for `perm_7` gives the ordinary inequality

\[
  \operatorname{ChowRank}(\operatorname{perm}_7)\geq\left\lceil R/832\right\rceil.
\]

The ambient projected matrix is only (42875\times42875), compared with the
intractable full central wedge matrix.

## Cyclic Fourier reduction

For \(\pi(x_{ij})=e_{i+j}\), row and column cyclic shifts give an action of
\(\mathbb Z_7^2\).  Every source and target state has a free orbit of size
(49), so the matrix decomposes into forty-nine (875\times875) Fourier
blocks.  Scaling and transposition reduce these to six character classes with
multiplicities

\[
1,12,6,6,12,12.
\]

The exact block ranks are (686,693,693,688,693,693).  Their weighted sum is
(33920).  Both split primes (1009) and (953) give the same ranks.  A
nonzero modular minor lifts to characteristic zero (over the seventh
cyclotomic field), so this is an exact characteristic-zero rank lower bound,
not a floating-point estimate.

## Universal seven-dimensional ceiling

For the same cyclic quotient, compute the preceding Koszul arrow

\[
K^\pi_{5,2}:D_5(\operatorname{perm}_7)\otimes\bigwedge^2Z
\longrightarrow
D_4(\operatorname{perm}_7)\otimes\bigwedge^3Z.
\]

Its source has dimension (9261).  Fourier reduction gives rectangular
(875\times189) blocks.  Their six class ranks are (183,182,182,182,182,182),
with weighted total

\[
8919.
\]

This value is again identical modulo (1009) and (953).  Matrix rank is
maximal on a nonempty Zariski-open set of seven-dimensional quotients.  Hence
the generic rank of (K^\pi_{5,2}) is at least (8919).  The open loci on
which the adjacent and central arrows have their respective maximal ranks
intersect.  Since consecutive Koszul arrows compose to zero,

\[
\operatorname{rank}K^\pi_{4,3}
 \leq 42875-8919=33956
\]

on that generic locus, and every special quotient has no larger central rank.
Therefore every seven-dimensional projected flattening in this family obeys

\[
\left\lceil\operatorname{rank}K^\pi_{4,3}/832\right\rceil\leq41.
\]

This is a route-capacity theorem, not merely a negative sample search.

## All quotient dimensions from 7 through 49

The cyclic seven-dimensional calculation supplies the exact adjacent ranks

\[
(r_{5,0},\ldots,r_{5,6})
=(441,3038,8919,14413,13741,7266,1225).
\]

Both split primes give the same seven values.  Now let (Z) have dimension
(k\geq7), specialize seven directions to the cyclic quotient, and leave
(k-7) directions inactive.  Splitting the exterior power by the number of
inactive wedge directions gives the exact special adjacent rank

\[
R_{\rm in}(k,p)=
\sum_s {k-7\choose s}r_{5,p-1-s}.
\]

Rank is maximal on a nonempty open subset of
\(\operatorname{Hom}(V,Z)\).  The maximal-rank opens for consecutive Koszul
arrows intersect, and their composition is zero.  Consequently every
projected central arrow satisfies

\[
\operatorname{rank}K^\pi_{4,p}
\leq
\min\left\{
1225{k\choose p}-R_{\rm in}(k,p),
1225{k\choose p+1}
\right\}.
\]

For one independent seven-factor Chow term, the seven active ranks are

\[
(35,224,595,832,595,224,35,0),
\]

and the exact cap after adjoining inactive directions is the corresponding
binomial convolution.  Dependent-factor terms are specializations and cannot
increase it.

The certificate checks all (1204) pairs
\(7\leq k\leq49\), (0\leq p<k\) with exact integer arithmetic.  The unique
largest ratio occurs at ((k,p)=(31,20)):

\[
\frac{54{,}331{,}402{,}125}{1{,}177{,}066{,}055}
=\frac{42{,}949{,}725}{930{,}487}\approx46.1584.
\]

Its integer ceiling is (47).  Thus this entire (k\geq7) projected-Koszul
family is now closed as a route to lower (50).

## Seven-character search

More generally, choose seven characters from the forty-nine characters of
\(\mathbb Z_7^2\).  This gives a seven-dimensional equivariant quotient and the
same forty-nine-block decomposition.  The frozen search streams forty seeded
character sets.  The best set was

\[
\{(0,1),(1,6),(2,0),(3,1),(4,5),(5,0),(6,6)\},
\]

with total rank (32928) at both split primes.  The finite search does not
classify every seven-character quotient; it only shows that these sampled
equivariant quotients do not approach the lower-50 threshold.

## Replay

```bash
python scripts/n7_cyclic_projected_koszul_rank.py \
  --json data/n7_cyclic_projected_koszul_rank.json

python scripts/n7_character_quotient_koszul_search.py \
  --candidates 40 --workers 20 --seed 20260820 \
  --json data/n7_character_quotient_koszul_search.json

python -m unittest tests.test_n7_projected_koszul_quotients -v
```

The full forty-candidate unit-test replay is opt-in through
`RUN_EXPENSIVE_REPLAYS=1`; ordinary tests read the frozen payload and replay the
one-second cyclic certificate.

## Boundary

This is an ordinary matrix-rank computation.  It gives no border-rank claim.
The finite character search does not classify arbitrary nonequivariant
quotients; nevertheless, the adjacent-map and inactive-wedge argument supplies
the stated universal ceiling for every quotient dimension from seven through
forty-nine.  Quotient dimensions below seven are not included in the unified
barrier.  Numerical CP-ALS, homotopy, and sparse-LU probes remain discovery
diagnostics and are not used in the theorem statement.
