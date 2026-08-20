# Tangent nonredundancy of the 64-term Glynn decomposition of perm7

## Status

`EXACT_LOCAL_RIGIDITY` — characteristic-zero rank certified by a modular
nonzero minor and upgraded by the Jacobian criterion.  This is not a global
Chow-rank lower bound.

Glynn's decomposition is indexed by the 64 sign characters with one sign
fixed.  Every term has seven independent column-separated factors.  The
affine tangent space to one Chow term therefore has dimension

\[
1+7(49-1)=337,
\]

after quotienting the six intrinsic factor-rescaling directions.  The full
ordered 64-term source consequently has effective tangent dimension 21,568.

## Walsh block calculation

Fourier transform in the six free signs separates the tangent map by Walsh
parity and by column multidegree.  Column-separated factors make the list of
multidegrees exhaustive: either all seven column degrees remain one, or one
column is missing and a different column is doubled.

For the multidegree containing one variable in every column, the six parity
weights \(0,1,\ldots,5\) have rank 43.  The all-ones parity has rank 37.  Its
rows are exactly the permutation matrices; their linear span has dimension
\((7-1)^2+1=37\).  The other blocks have the theoretical upper bound
\(49-6=43\), supplied by the six transformed intrinsic factor relations, and
the modular calculation reaches that bound.

There are 42 multidegrees with one missing column and one doubled column.
Each splits into 64 parity blocks of rank 7, hence has rank 448.  Thus the full
tangent rank is

\[
2746+42\cdot448=21562.
\]

The remaining kernel after intrinsic factor rescaling has dimension

\[
21568-21562=6.
\]

It is exactly the six-dimensional row-diagonal torus stabilizing the
permanent: infinitesimal row weights summing to zero move the individual
Glynn factors while their sum remains \(\operatorname{perm}_7\).  These six
directions survive the intrinsic factor gauge because they scale rows, while
the seven factors are separated by columns.  They attain the computed kernel
dimension, so no additional first-order kernel remains.

This also gives all-order local rigidity.  Work on the smooth ordered
64-term chart of nonzero independent-factor Chow points after quotienting the
intrinsic \((\mathbb G_m)^6\) gauge of every term.  The fiber of the summation
map over \(\operatorname{perm}_7\) has tangent dimension six.  The sum-zero
row torus \((\mathbb G_m)^6\) acts freely infinitesimally in this chart and
gives a six-dimensional orbit contained in the fiber.  Hence the local
dimension and tangent dimension both equal six.  In characteristic zero the
fiber is smooth and reduced at the Glynn point, and the stabilizer orbit is
open in a neighborhood of that point.  Modulo the stabilizer, the
decomposition is therefore an isolated reduced point.

The replay is `scripts/n7_glynn_tangent_nonredundancy.py`, with frozen payload
`data/n7_glynn_tangent_nonredundancy.json`.

## Boundary

This rules out hidden higher-order as well as first-order local branches near
the Glynn decomposition.  It does not exclude a disconnected or unrelated
63-term decomposition, and it makes no border-rank claim.

The same Walsh calculation has a uniform proof for every \(n\geq3\); see
`general_glynn_local_rigidity.md`.
