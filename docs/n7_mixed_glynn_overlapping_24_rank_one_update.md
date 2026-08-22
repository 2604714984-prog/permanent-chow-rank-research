# Perm7 overlapping (2,4)/(4,2) rank-one updates

This note records an exact characteristic-zero computation in the synchronized
mixed-Glynn two-transform endpoint model.  It proves invalid-tail rank 42 for
every nonidentity invertible rank-one update in the projective support closure
of the overlapping support shapes ((2,4)) and ((4,2)).  It is not a proof
of ordinary lower 50 for (operatorname{perm}_7).

## Dense exact-support charts

For a two-coordinate core ({a,b}) and two extra coordinates (c,d), the
two affine normal forms are

\[
\begin{aligned}
u&=e_a+r e_b,
&v&=t(s e_a^*+e_b^*+w e_c^*+x e_d^*),\\
u&=e_a+r e_b+w e_c+x e_d,
&v&=t(s e_a^*+e_b^*).
\end{aligned}
\]

In both cases

\[
\det(I+uv^T)=1+t(r+s).
\]

There are

\[
2\binom62\binom42\cdot5=900
\]

oriented support and positive identity/update multiplicity cases.  The
20-worker exact WSL replay completed all 900 in 1079.65 seconds.

The first selected exact (42\times42) minor covers 325 rows directly.  The
other 575 have the sole internal factor (1+st).  Restricting exactly to
(1+st=0) covers 527 of those rows.  The remaining 48, all in the
((2,4)) orientation, have only (1+rt) on that face.  Restricting again to

\[
1+st=1+rt=0
\]

covers all 48 by a monomial minor.  The double-face calculation clears the
Laurent denominator by a columnwise power of the nonzero coordinate (t),
which preserves rank.  Regression tests verify the substitution identity.
No multivariate-gcd inference is used.

The dense (r+s=0) face imports the exact overlap-two nilpotent
((2,4)) and ((4,2)) certificates.  Their formerly multi-minor rows are
covered by the completed 1,189-row Laurent-torus audit, so this dependency is
not merely a multivariate-gcd claim.

The dense certificate is
`data/n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.json`.  It has
1,205,036 bytes and SHA-256
`d8e7fa55a31215f68d69b3814d5686619bd25dd888a1a530650eca45a5fdf394`.

## Singleton-versus-four boundary

When the two-coordinate factor loses one coefficient, the new proper support
type is singleton versus four.  Its two orientations are

\[
u=e_a,\qquad
v=t(e_a^*+s e_b^*+w e_c^*+x e_d^*),
\]

and their transpose.  The determinant is (1+t), and the inventory is

\[
2\cdot6\binom53\cdot5=600.
\]

Every row is covered by its first exact minor.  The 20-worker replay took
80.30 seconds, with 300 rows per orientation and no unresolved factor.
Coordinate faces import singleton-versus-triple closure; the projective face
where the normalized shared coefficient vanishes imports the exact disjoint
three-direction shear certificate.

The 509,267-byte certificate is
`data/n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.json`, with
SHA-256
`ff2043fd5928354df866ed3836a361ffd08e86d3583de117fbcdd7a03502aa4f`.

## Overlap-one (2,3)/(3,2) boundary

When one core coefficient on the four-coordinate side vanishes, the new
proper support type has overlap one.  The affine normal forms are

\[
\begin{aligned}
u&=e_a+r e_b,
&v&=t(s e_a^*+e_c^*+w e_d^*),\\
u&=e_a+r e_b+w e_c,
&v&=t(s e_a^*+e_d^*).
\end{aligned}
\]

Both have determinant (1+st).  The exact inventory is

\[
2\cdot6\cdot5\binom42\cdot5=1800.
\]

All 1,800 rows, 900 per orientation, use their first exact minor.  The
20-worker replay took 259.11 seconds.  Proper projective faces import exact
overlap-one ((2,2)), singleton-versus-triple, disjoint ((2,2)), or
disjoint three-direction certificates.

The 1,668,451-byte certificate is
`data/n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.json`, with
SHA-256
`8df30d10eafd01c39fe5447868ef9e084cded79a46bfa4c828ffe5f7f5ff0b4a`.

## Projective support closure

Write homogeneous coefficients for the dense shapes.  Every coordinate
hyperplane reduces to one certified projective family.

| Dense shape | Coordinate face | Exact family |
|---|---|---|
| (u=x e_a+y e_b), (v=p e_a^*+q e_b^*+h e_c^*+k e_d^*) | (x=0) or (y=0) | singleton versus four |
| same | (p=0) or (q=0) | overlap-one ((2,3)) |
| same | (h=0) or (k=0) | overlapping ((2,3)) |
| (u=x e_a+y e_b+z e_c+g e_d), (v=p e_a^*+q e_b^*) | (x=0) or (y=0) | overlap-one ((3,2)) |
| same | (z=0) or (g=0) | overlapping ((3,2)) |
| same | (p=0) or (q=0) | four versus singleton |

Intersections only drop to proper faces of the imported projective-closure
certificates.  The audit
`data/n7_mixed_glynn_overlapping_24_rank_one_update_support_closure.json`
freezes this map and the 325/527/48 internal split.  It has 2,742 bytes and
SHA-256
`a2dad7d1ddfcf84bfeac809b23b375fade63b800535c35c1a4583b56ac9ed502`.

Consequently every nonidentity invertible rank-one update in these two
projective support closures has invalid-tail rank 42 in the synchronized
mixed-Glynn packet.

## Replay

```bash
python scripts/n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.py \
  --max-candidates 900 --workers 20 \
  --json data/n7_mixed_glynn_overlapping_24_rank_one_update_tail_rank.json
python scripts/n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_singleton_four_rank_one_update_tail_rank.json
python scripts/n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.py \
  --max-candidates 1800 --workers 20 \
  --json data/n7_mixed_glynn_overlap_one_23_rank_one_update_tail_rank.json
python scripts/n7_mixed_glynn_overlapping_24_rank_one_update_support_closure.py \
  --json data/n7_mixed_glynn_overlapping_24_rank_one_update_support_closure.json
```

## Claim boundary

This closes one finite nonnilpotent rank-one support layer in one restricted
endpoint model.  It does not cover larger nonnilpotent supports, higher-rank
perturbations, arbitrary (mathrm{GL}_6), arbitrary endpoint-B packets,
ordinary lower 50, exact rank 64, or border rank.
