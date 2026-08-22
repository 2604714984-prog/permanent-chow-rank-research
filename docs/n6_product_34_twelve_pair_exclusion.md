# N6-118: twelve-dimensional (3\times4/4\times3) product endpoint obstruction

**Status.** EXACT_COORDINATE_PRODUCT_12_BLOCK_DIAGONAL_OBSTRUCTION.  The
calculation is conditional only on the local meaning of the already proved
N6-110, N6-111, and N6-112 interfaces.  It is an exact characteristic-zero
coordinate calculation; it is not a random search and it does not use a
finite-field rank claim.

## 1. Block-diagonal locus and imported interfaces

Fix one of the standard or biflag (23)-dimensional quadratic hooks (K)
and its derivative space (M=\partial K\).  On the block-diagonal locus
consider triples

\[
 (D,L,M_0),\qquad
 \dim D=12,\quad \dim L=\dim M_0=6,
 \quad D\subset K\cap(\operatorname{Sym}^2L+\operatorname{Sym}^2M_0),
 \quad L,M_0\subset M.
\tag{1.1}
\]

N6-110 applies to every actual point of (1.1) and gives

\[
 \partial D=L\oplus M_0,\qquad \dim\partial D=12.
\tag{1.2}
\]

If a point of this block-diagonal locus is torus fixed, (D,L,M_0) are
coordinate.  Put

\[
 U=L\oplus M_0,\qquad e(U)=\dim(K\cap\operatorname{Sym}^2U).
\tag{1.3}
\]

N6-112 classifies fixed points of the larger closed cross-free incidence,
and N6-111 handles its full (2\times6) product endpoint.  The present
certificate checks the remaining (3\times4) and (4\times3) fixed points,
including the standard and biflag hooks.  It does **not** claim that the
block-diagonal condition remains closed when (L\cap M_0) jumps; that is the
formal-boundary issue still handled by N6-113--117.

## 2. Exact fixed-point certificate

For a coordinate product (U=R\times C), the torus weights in
(K\cap\operatorname{Sym}^2U) are distinct permanent rectangles.  A
rectangle on rows (a,b) and columns (c,d) is block diagonal for the
coordinate partition (U=L\sqcup M_0) exactly when both opposite-corner
edges

\[
 \{(a,c),(b,d)\},\qquad \{(a,d),(b,c)\}
\tag{2.1}
\]

lie wholly in one side.  Therefore a coordinate (12)-plane (D) can be
block diagonal only if at least twelve of the available rectangles pass this
edge test.

The script enumerates the six row choices and six column choices defining
each product support, then all \(\binom{12}{6}=924\) coordinate partitions.
It never materializes the \(1.3\)-million twelve-subsets of the (23)-cell
hook.  The exact endpoint counts and maxima are:

| hook | product | endpoints | rectangle/max-safe histogram | maximum |
|---|---:|---:|---|---:|
| standard | (3\times4) | 30 | (6\times(15/9)+24\times(18/10)) | 10 |
| standard | (4\times3) | 10 | (10\times(18/10)) | 10 |
| biflag | (3\times4) | 20 | (20\times(18/10)) | 10 |
| biflag | (4\times3) | 14 | (14\times(18/10)) | 10 |

Here (r/s) means (r) available rectangle weights and at most (s) of
them can be block diagonal for any coordinate (6+6) partition.  Since
(s\le10<12), no torus-fixed (3\times4) or (4\times3) point belongs to
(1.1).

The replay is:

```text
python scripts/n6_product_34_twelve_pair_exclusion.py \
  --verify-json data/n6_product_34_twelve_pair_exclusion.json
python -m unittest tests.test_n6_product_34_twelve_pair_exclusion -v
```

## 3. Consequence and boundary

The exact result is the following fixed-point lemma: a coordinate (3\times4)
or (4\times3) product support in either hook cannot carry twelve distinct
permanent-rectangle directions that are block diagonal for a coordinate
six-plus-six partition.  This supplies the missing fixed-point obstruction
for the product equality layer.

It is not yet a global component theorem.  A projective closure of the
block-diagonal locus may acquire a boundary where (L\cap M_0)\ne0, so the
torus fixed-point argument cannot be applied without an additional formal
closure theorem.  N6-113--117 study precisely those noncoordinate
rank-three and rank-five/rank-six germs.

The branches with (a_2=73,74,75), the remaining (b=34) defect-six geometry,
ordinary lower 29, unrestricted rank 32, and border rank remain open.
