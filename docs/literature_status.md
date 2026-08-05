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

## Row-homogeneous decomposition gate

The arXiv abstract of Xu--Gnang, *On the Chow-rank of the permanent*, arXiv:2311.05890, states that the paper proves by an orbital argument that Glynn's formula is optimal among row-homogeneous Chow decompositions and gives a parametric description of rank-revealing row-homogeneous decompositions.

Only the arXiv metadata and abstract have been independently retrieved during the current review. The precise definition of `row-homogeneous`, the theorem hypotheses, the parametrization scope, and the relation to the repository's column-oriented sign families have not yet been checked from the full text.

Accordingly, implementation of the N6-17B column-dependent sign pilot is suspended by `docs/n6_sign_family_literature_gate.md`. This gate supersedes the earlier preauthorization in Section 7 of `docs/n6_research_program.md` until the full-text family-inclusion comparison is complete.

## Novelty status

The formulas and shadow-removal argument in this repository were derived independently in the present research process. Their novelty relative to all published and unpublished literature is **not verified**. Do not describe them as new in a paper, abstract, repository description, or press statement until a dedicated literature review is complete.

G-020 and every proposed extension of the Glynn sign family must also remain free of novelty claims until they are reconciled with Xu--Gnang arXiv:2311.05890. Depending on the paper's definitions, G-020 may be a known special case, an independent reformulation, or a theorem about a different family.

## Primary references to compare

- N. Ilten and Z. Teitler, *Product Ranks of the 3 x 3 Determinant and Permanent*, arXiv:1503.00822.
- M. S. Shafiei, *Apolarity for Determinants and Permanents of Generic Matrices*, arXiv:1212.0515.
- J. Alper and R. Rowlands, *Syzygies of the Apolar Ideals of the Determinant and Permanent*, arXiv:1709.09286.
- R. Xu and E. Gnang, *On the Chow-rank of the Permanent*, arXiv:2311.05890.
- Y. Guan, *Flattenings and Koszul Young Flattenings Arising in Complexity Theory*, arXiv:1510.00886.
- K. Efremenko, J. M. Landsberg, H. Schenck, and J. Weyman, *On Minimal Free Resolutions of Sub-Permanents and Other Ideals Arising in Complexity Theory*, arXiv:1504.05171.
- J. I. Han, J.-H. Ju, and Y. Kim, *Recursive Koszul Flattenings of Determinant and Permanent Tensors*, arXiv:2503.12032.
