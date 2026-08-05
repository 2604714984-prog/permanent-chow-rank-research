# Literature status

This file intentionally separates known references from novelty claims.

## Known context

- Product rank, split rank, and Chow rank are synonymous in the relevant literature.
- Glynn's identity supplies a `2^(n-1)`-term upper bound.
- Prior work proves product rank 4 for `perm_3` and gives general lower bounds of central-binomial scale.
- Ilten--Teitler prove product rank `4` for `perm_3` and border product rank strictly greater than `n` for `perm_n`, `n>=3`.
- Shafiei determines the apolar ideal and Hilbert function of the determinant and permanent of a generic matrix.
- Alper--Rowlands determine quadratic syzygy data for the apolar ideals of the determinant and permanent; N6-017 uses their `beta_(2,4)` formula as an external theorem.
- Guan constructs flattening and Koszul--Young equations for Chow varieties and their secant varieties; these must be compared directly with the border-Koszul theorem in this repository.
- Recent recursive Koszul work concerns tensor rank and does not automatically imply unrestricted Chow-rank bounds.

## Xu--Gnang full-text reconciliation

The repository has completed a source-bound review of

- Rongyu Xu and Edinah Gnang, *On the Chow-rank of the permanent*,
  arXiv:2311.05890.

The reviewed mathematical source is version 2, submitted on 2025-01-04. The
later version 3, submitted on 2025-03-24, is withdrawn with the arXiv comment

```text
Incorrect statement Thm 4.2
```

Version 2 defines degree-one row-homogeneous decompositions as sums of terms

\[
\prod_i\left(\sum_j b_{ij}x_{ij}\right),
\qquad b_{ij}\in\mathbb C.
\]

This is the row-oriented tensor-rank model, strictly narrower than unrestricted
Chow rank.

Theorem 4.2 of version 2 is the claimed optimality of Glynn's
row-homogeneous decomposition. Because the later arXiv version withdraws that
theorem as incorrect, it is not used as a repository dependency. The displayed
version-2 proof also contains unsupported projection, tensor-dependence, and
automorphism-rigidity steps. The exact analysis and source hashes are in

```text
docs/xu_gnang_v2_reconciliation.md
```

The downstream parametrization section may still define algebraic families of
length `2^(n-1)` decompositions, but its minimality interpretation relies on
the withdrawn theorem.

## Sign-family consequence

The repository's G-020 result is classified as

```text
INDEPENDENT_STRICT_SUBFAMILY_RIGIDITY
```

It proves rigidity only inside the span of the 32 fixed Glynn sign terms. It
does not establish optimality among arbitrary row-sign, row-homogeneous, or
unrestricted Chow terms.

The finite one-defect sign pilot is not redundant with a valid theorem in
arXiv:2311.05890 and may resume as a restricted exact diagnostic. Failure to
find a shorter sign decomposition is not a general lower bound. Novelty claims
remain forbidden.

## Novelty status

The formulas and shadow-removal argument in this repository were derived independently in the present research process. Their novelty relative to all published and unpublished literature is **not verified**. Do not describe them as new in a paper, abstract, repository description, or press statement until a dedicated literature review is complete.

G-020 and every extension of the Glynn sign family must likewise remain free
of novelty claims. Full-text reconciliation determines family scope and
logical dependence; it does not establish literature novelty.

## Primary references to compare

- N. Ilten and Z. Teitler, *Product Ranks of the 3 x 3 Determinant and Permanent*, arXiv:1503.00822.
- M. S. Shafiei, *Apolarity for Determinants and Permanents of Generic Matrices*, arXiv:1212.0515.
- J. Alper and R. Rowlands, *Syzygies of the Apolar Ideals of the Determinant and Permanent*, arXiv:1709.09286.
- R. Xu and E. Gnang, *On the Chow-rank of the Permanent*, arXiv:2311.05890; version 3 withdrawn for an incorrect Theorem 4.2.
- Y. Guan, *Flattenings and Koszul Young Flattenings Arising in Complexity Theory*, arXiv:1510.00886.
- K. Efremenko, J. M. Landsberg, H. Schenck, and J. Weyman, *On Minimal Free Resolutions of Sub-Permanents and Other Ideals Arising in Complexity Theory*, arXiv:1504.05171.
- J. I. Han, J.-H. Ju, and Y. Kim, *Recursive Koszul Flattenings of Determinant and Permanent Tensors*, arXiv:2503.12032.
