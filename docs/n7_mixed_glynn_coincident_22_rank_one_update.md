# Coincident two-coordinate rank-one updates at the perm7 mixed endpoint

## Status

This is an exact characteristic-zero theorem for a restricted synchronized
mixed-Glynn endpoint family.  It is not an ordinary lower-50 theorem and does
not concern border rank.

On a selected coordinate pair, write

\[
u=(1,r),\qquad v=t(s,1),\qquad
A=I+uv^{\mathsf T}.
\]

Then

\[
\det A=1+t(r+s).
\]

The exact-support chart has \(rst\ne0\).  There are
\(\binom62\cdot5=75\) coordinate-support and positive multiplicity-split
cases.

## Exact cover

For 19 cases, one exact \(42\times42\) minor factors only over \(t\) and
\(\det A\).  In the other 56 cases the same construction has the additional
factor \(1+st\).  On that divisor, substituting \(s=-1/t\) before column
selection gives a second exact minor in \(\mathbb Z[r,t]\).

Thirty-six of those face minors are coordinate monomials.  The remaining 20
factor as a coordinate monomial times \(1+rt\).  At the simultaneous face

\[
1+st=1+rt=0,
\]

the update restricts to

\[
A=\begin{pmatrix}0&t\\t^{-1}&0\end{pmatrix},
\]

which is an invertible monomial transform and is covered by the imported
monomial packet classification.  Hence all 75 valid invertible nonidentity
updates in this coincident \((2,2)\) family have invalid-tail rank 42 and zero
local target intersection.

The four-worker WSL replay took 170.61 seconds.  It stores only the selected
minors and their exact factorizations; unresolved-factor count is zero.

## Boundary and replay

This does not cover larger coincident supports, distinct or partially
overlapping supports, higher-rank perturbations, arbitrary \(\mathrm{GL}_6\),
arbitrary endpoint-B packets, ordinary lower 50, exact rank 64, or border
rank.

```bash
python scripts/n7_mixed_glynn_overlapping_22_rank_one_update_tail_rank.py \
  --max-candidates 75 --workers 4 \
  --json data/n7_mixed_glynn_overlapping_22_rank_one_update_tail_rank.json
```
