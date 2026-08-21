# Overlap-one two-coordinate rank-one updates at the perm7 mixed endpoint

## Status

This is an exact characteristic-zero theorem for a restricted synchronized
mixed-Glynn two-transform packet.  It is not an ordinary lower-50 theorem and
does not concern border rank.

For three distinct coordinates \(a,b,c\), write

\[
u=e_a+r e_b,\qquad
v=t(s e_a^*+e_c^*),\qquad
A=I+uv^{\mathsf T}.
\]

Then

\[
\det A=1+st.
\]

There are \(6\cdot5\cdot4=120\) ordered exact-support triples and five
positive identity/update multiplicity splits, hence 600 dense cases.

## Dense exact-support certificate

All 600 cases succeed at the first deterministic selection point.  Each uses
one exact \(42\times42\) determinant, so no multivariate-gcd inference is
involved.  Every determinant factors only over

\[
r,\qquad s,\qquad t,\qquad 1+st.
\]

The factor-support distribution is:

- 375 determinants use all four allowed factors;
- 165 omit \(s\);
- 60 use only \(t\) and \(1+st\).

Thus every dense exact-support point with \(rst(1+st)\ne0\) has invalid-tail
rank 42 and zero local target intersection.  The largest selected determinant
has total degree 79 and 21 terms.

The 20-worker WSL replay took 59.61 seconds.  The frozen JSON has 481,203
bytes and SHA-256
`2fb5b2c9fd97ac5d5750fbdd6e3618ef0f08ccc1569996eb4c69ffc736ff3e64`.
The 8 GiB field is the run-admission budget, not a measured memory peak.

## Projective support faces

The affine normalization does not display every projective coefficient face.
Both singleton-overlap orientations were therefore computed separately:

\[
u=e_a,\quad v=t(s e_a^*+e_c^*)
\]

and

\[
u=e_a+s e_b,\quad v=t e_a^*.
\]

They contribute \(2\cdot6\cdot5\cdot5=300\) cases.  Again every case succeeds
with its first single exact minor.  The 150 left-singleton determinants use
only \(t\) and \(1+st\); the 150 right-singleton determinants use only
\(s,t\), and \(1+t\).  The latter \(s=0\) face is an invertible diagonal
monomial transform and is covered by the imported monomial classification.
The replay took 29.00 seconds.  Its 225,681-byte JSON has SHA-256
`be4f7e8bf054e2cbf2fe58f5134daf9b6bd6f673823dad0e1c18931880084f2c`.
Its 4 GiB field is likewise a run-admission budget rather than telemetry.

For the 600-case chart, \(r=0\) and the projective \(v_c=0\) face are the two
singleton orientations.  The \(s=0\) and projective \(u_a=0\) faces are
disjoint coordinate-star updates covered by the exact two-direction shear
certificate.  The divisor \(t=0\) is the identity control, and \(1+st=0\) is
outside \(\mathrm{GL}_6\).  Hence every nonidentity invertible update in the
projective support closure of the overlap-one \((2,2)\) pattern is covered.

## Boundary and replay

This still does not cover larger overlapping non-nilpotent supports,
higher-rank perturbations, arbitrary \(\mathrm{GL}_6\), arbitrary endpoint-B
packets, ordinary lower 50, exact rank 64, or border rank.

```bash
python scripts/n7_mixed_glynn_singleton_overlap_rank_one_update_tail_rank.py \
  --max-candidates 300 --workers 20 \
  --json data/n7_mixed_glynn_singleton_overlap_rank_one_update_tail_rank.json

python scripts/n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank.py \
  --max-candidates 600 --workers 20 \
  --json data/n7_mixed_glynn_overlap_one_22_rank_one_update_tail_rank.json
```
