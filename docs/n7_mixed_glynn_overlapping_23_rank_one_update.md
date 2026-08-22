# Perm7 overlapping (2,3)/(3,2) rank-one updates

This note records an exact characteristic-zero computation in the synchronized
mixed-Glynn two-transform endpoint model.  It proves invalid-tail rank 42 for
every nonidentity invertible rank-one update in the projective support closure
of the overlapping support shapes \((2,3)\) and \((3,2)\).  It is not a proof
of ordinary lower 50 for \(\operatorname{perm}_7\).

## Dense exact-support charts

For a two-coordinate core \(\{a,b\}\) and an extra coordinate \(c\), the two
affine normal forms are

\[
\begin{aligned}
u&=e_a+r e_b,
&v&=t(s e_a^*+e_b^*+w e_c^*),\\
u&=e_a+r e_b+w e_c,
&v&=t(s e_a^*+e_b^*).
\end{aligned}
\]

In both cases

\[
\det(I+uv^T)=1+t(r+s).
\]

There are

\[
2\binom62\cdot4\cdot5=600
\]

oriented support, extra-coordinate, and positive identity/update multiplicity
cases.  The 20-worker exact replay completed all 600 in 427.38 seconds.

The first selected exact \(42\times42\) minor covers 193 rows directly.  The
other 407 have exactly one additional factor, \(1+st\).  Restricting exactly to
\(1+st=0\) covers 357 of those rows by a single minor.  The remaining 50, all
in the \((2,3)\) orientation, have the sole additional factor \(1+rt\) on that
face.  Restricting again to

\[
1+st=1+rt=0
\]

covers all 50 by a monomial minor.  The double-face calculation clears the
Laurent denominator by multiplying each feature column by the appropriate
power of the nonzero coordinate \(t\); this is a column rescaling and therefore
preserves rank on the face torus.  The regression test verifies this identity
symbolically.  No multivariate-gcd inference is used at any stage.

The dense certificate is
`data/n7_mixed_glynn_overlapping_23_rank_one_update_tail_rank.json`.  It has
776,088 bytes and SHA-256
`23d928d9e2d7933cfed664b92e5a0e501ff562a55b1a1082856ebdbf39a061c0`.

## Singleton-versus-triple boundary

The only proper projective support family not already covered by the
coincident-\((2,2)\) and overlap-one-\((2,2)\) certificates has support sizes
one and three.  Both orientations use the normal forms

\[
u=e_a,\quad v=t(e_a^*+s e_b^*+w e_c^*),
\]

or

\[
u=e_a+s e_b+w e_c,\quad v=t e_a^*,
\]

for distinct \(a,b,c\).  Their determinant is \(1+t\).  The inventory is
again

\[
2\cdot6\binom52\cdot5=600.
\]

Every one of the 600 rows is covered by its first exact minor.  The 20-worker
replay took 57.30 seconds, with 300 rows in each orientation and no unresolved
factor.  Its 489,493-byte certificate is
`data/n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.json`, with
SHA-256
`86e0e405a33bb8a4874f46254f16d9a57a09d85fe2cd79735570f2d6f4379530`.
The two-coordinate faces use the exact singleton-overlap certificate; the
projective face where the normalized shared coefficient vanishes is an exact
disjoint two-direction shear.

## Projective support closure

Use homogeneous coefficients as follows.  Each coordinate hyperplane reduces
to one previously certified projective family.

| Dense shape | Homogeneous support | Coordinate face | Exact family |
|---|---|---|---|
| extra right | \(u=x e_a+y e_b\), \(v=p e_a^*+q e_b^*+h e_c^*\) | \(x=0\) or \(y=0\) | singleton versus triple |
| extra right | same | \(p=0\) or \(q=0\) | overlap-one \((2,2)\) |
| extra right | same | \(h=0\) | coincident \((2,2)\) |
| extra left | \(u=x e_a+y e_b+z e_c\), \(v=p e_a^*+q e_b^*\) | \(x=0\) or \(y=0\) | overlap-one \((2,2)\) |
| extra left | same | \(z=0\) | coincident \((2,2)\) |
| extra left | same | \(p=0\) or \(q=0\) | singleton versus triple |

Intersections of these hyperplanes only drop to proper support faces already
included in the imported projective-closure certificates.  The lightweight
audit
`data/n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.json`
freezes this map and the 193/357/50 internal coverage split.  Its SHA-256 is
`a998aa8a7f645a0ce73c6b178e49ffaca38ef993ecba2166da11bce4435714d0`.

Consequently every nonidentity invertible rank-one update in these two
projective support closures has invalid-tail rank 42 in the synchronized
mixed-Glynn packet.

## Replay

```bash
python scripts/n7_mixed_glynn_overlapping_23_rank_one_update_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_overlapping_23_rank_one_update_tail_rank.json
python scripts/n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_singleton_triple_rank_one_update_tail_rank.json
python scripts/n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.py \
  --json data/n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.json
```

## Claim boundary

This closes one finite nonnilpotent rank-one support layer in one restricted
endpoint model.  It does not cover larger nonnilpotent supports, higher-rank
perturbations, arbitrary \(\mathrm{GL}_6\), arbitrary endpoint-B packets,
ordinary lower 50, exact rank 64, or border rank.
