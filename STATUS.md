# Research status ledger

Status vocabulary:

- `VERIFIED_BASELINE`: independently checked small-`n` result.
- `PROOF_DRAFT_COMPLETE`: complete internal proof draft; not externally reviewed.
- `COMPUTATION_REPLAYED`: deterministic computation rerun successfully.
- `ROUTE_DIAGNOSTIC`: exact finite result used to assess a proof route, not itself a Chow-rank theorem.
- `LITERATURE_RECONCILED`: a source-bound full-text comparison with explicit version and claim boundaries.
- `RESTRICTED_FAMILY_THEOREM`: an exact theorem for a stated proper subclass, with no inference to unrestricted Chow rank.
- `RESTRICTED_AGGREGATE_THEOREM`: an exact theorem for a fixed aggregate function or fixed aggregate assignment, with no inference to all decompositions in the surrounding family.
- `CONDITIONAL`: depends on evidence not fully regenerated in this repository.
- `SUPERSEDED`: valid but strictly weaker than a later in-repository result.
- `CONJECTURE`: proposed statement without proof.
- `OPEN`: defined research target.

| ID | Status | Statement | Evidence |
|---|---|---|---|
| S3-001 | `VERIFIED_BASELINE` | `ChowRank(perm_3)=4` | reviewed source and exact arithmetic |
| S4-001 | `VERIFIED_BASELINE`, `COMPUTATION_REPLAYED` | `ChowRank(perm_4)=8` | independent 560/92/659 exact audit |
| S5-001 | `CONDITIONAL` | `ChowRank(perm_5)=16` | lower-16 overlay replayed; omitted lower-15 SAT layer not regenerated here |
| G-001 | `PROOF_DRAFT_COMPLETE` | `dim D_m(perm_n)=binom(n,m)^2` | `docs/general_n_koszul_bounds.md` |
| G-002 | `PROOF_DRAFT_COMPLETE` | `D_m(perm_n)^(1)=D_{m+1}(perm_n)` for `2<=m<=n-1` | coefficient propagation proof |
| G-003 | `PROOF_DRAFT_COMPLETE` | generalized first-Koszul lower bound `L_K(n)`; unique optimizer `m=ceil(n/2)` | exact formula, optimizer proof, and tests |
| G-004 | `PROOF_DRAFT_COMPLETE` | `ChowRank(perm_n)>=binom(n,floor(n/2))+1` for `n>=3` | corollary of G-003 |
| G-005 | `PROOF_DRAFT_COMPLETE` | zero-intersection shadow-removal lower bound `L_SR(n)` | intersection lemma and double-quotient argument |
| G-006 | `SUPERSEDED` | `ChowRank(perm_6)>=22` | G-005 with `(m,d,q)=(3,1,1)`; superseded by G-011, N6-013, and N6-014 |
| G-007 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=L_K(n)` | closed determinantal rank locus |
| G-008 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=binom(n,floor(n/2))+1` | central-degree corollary of G-007 |
| G-009 | `PROOF_DRAFT_COMPLETE` | `L_SR(n)>=L_K(n)+Omega(a^n/sqrt(n))`, `a=(1+sqrt(2))/2` | entropy optimization and Stirling estimates |
| G-010 | `PROOF_DRAFT_COMPLETE` | even-degree multidimensional-shadow bound | `docs/even_n_multidimensional_shadow_bound.md`; special case of G-014 |
| G-011 | `SUPERSEDED` | `ChowRank(perm_6)>=23` | G-014 with `m=3`, `q=4`, and complementary intersection cap 40; superseded by N6-013 and N6-014 |
| G-012 | `PROOF_DRAFT_COMPLETE` | for even `n`, the G-010 additive gain over `L_K(n)` is `(1/(e log 2)+o(1))*binom(n,n/2)/n` | gamma-ratio expansion and one-variable optimization |
| G-013 | `PROOF_DRAFT_COMPLETE` | the G-010 route independently excludes seven terms for `perm_4` | fix two terms, intersection cap 6, residual rank `464>5*92` |
| G-014 | `PROOF_DRAFT_COMPLETE` | for arbitrary `n>=4`, `rank K_m(perm_n-R)>=A-n^2 b`, where `b=dim(D_{n-m}(perm_n) intersect D_{n-m}(R))`; Bukh shadows convert this into a computable Chow-rank lower bound | `docs/general_multidimensional_shadow_bound.md` |
| G-015 | `PROOF_DRAFT_COMPLETE` | reviewed exact-rational bounds include `ChowRank(perm_5)>=13`, `ChowRank(perm_7)>=41`, `ChowRank(perm_9)>=141`, `ChowRank(perm_11)>=506`, and `ChowRank(perm_15)>=6879` | `data/multishadow_bounds.json` and regression tests |
| G-016 | `PROOF_DRAFT_COMPLETE` | exact refinement `rank K_m(perm_n-R)>=A-n^2 b+Gamma`, where `Gamma` is the quotient Koszul image gain | `docs/quotient_koszul_gain.md` |
| G-017 | `PROOF_DRAFT_COMPLETE` | the odd-degree one-step multishadow gain is `(2/(e log 2)+o(1))*binom(n,floor(n/2))/n`, twice the even constant in this normalization | `docs/general_multishadow_parity_asymptotics.md` |
| G-018 | `PROOF_DRAFT_COMPLETE` | among all fixed integer output-degree offsets and fixed constant defects, the G-014 parity coefficients are uniquely maximized at the central lower output degree | `docs/general_multishadow_offset_optimality.md` and exact finite diagnostics |
| G-019 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | for every `K subset W tensor Sym^2 V` of dimension `k`, the vector-valued first prolongation satisfies `dim K^(1)<=k^{<2>}` | universal Grassmannian kernel, explicit colored-monomial one-parameter subgroup, scalar Macaulay growth, superadditivity, and `scripts/vector_valued_macaulay_audit.py` |
| G-020 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `RESTRICTED_FAMILY_THEOREM` | the `2^(n-1)` fixed column-uniform Glynn sign products are linearly independent, and the unique expansion of `perm_n` in their span uses every term with nonzero coefficient | Walsh-Hadamard proof and `scripts/glynn_family_rigidity_audit.py`; strict subfamily theorem only |
| N6-001 | `OPEN` | improve the lower bound beyond 25 or find a shorter decomposition of `perm_6` | `docs/n6_research_program.md` |
| N6-002 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | all 79,800 coordinate pairs in `D_3(perm_6)` have first-catalectic ranks `9,13,15,16,17,18`; the coordinate rank-nine tangent space has affine dimension 19 | `scripts/n6_coordinate_secant_audit.py` |
| N6-003 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | exact optimization of the former one-step Bukh-shadow formula over `m=2,3,4` stops at 23; its central `q=4` shadow cap 40 is attained | `scripts/n6_multishadow_route_barrier.py` |
| N6-004 | `SUPERSEDED`, `COMPUTATION_REPLAYED` | the explicit diagonal Chow term has full quotient Koszul gain `Gamma=705` | superseded by N6-006 |
| N6-005 | `COMPUTATION_REPLAYED` | every degree-six coordinate monomial `M` satisfies `im K_3(perm_6) intersect im K_3(M)=0`; all 167 row/column/transpose orbits are replayed | finite coordinate input to N6-006 |
| N6-006 | `PROOF_DRAFT_COMPLETE` | every nonzero degree-six Chow term `T`, including repeated and linearly dependent factors, satisfies `im K_3(perm_6) intersect im K_3(T)=0`, hence its quotient gain equals `rank K_3(T)` | `docs/n6_universal_single_term_full_gain.md` |
| N6-007 | `PROOF_DRAFT_COMPLETE` | for every nonzero scalar `alpha` and degree-six Chow term `T`, `rank K_3(perm_6-alpha T)=14175+rank K_3(T)` | `docs/n6_single_term_residual_additivity.md` |
| N6-008 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | the fixed-four projection, shadow, and central-catalectic inequalities first give the raw range `20<=b<=27`, `0<=d<=b-20`, and 36 states | `docs/n6_fixed_four_coupled_frontier.md` |
| N6-009 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | every six-plane `L` with `dim(D_2(perm_6) intersect Sym^2 L)=3` is a disjoint-support `2 x 3` or `3 x 2` tensor-product plane; the reduced locus has 5,580 seven-dimensional components | `docs/n6_extremal_six_plane_classification.md` |
| N6-010 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | equality in the four omitted-factor projection bounds at `b=27` forces coupled middle-catalectic rank 80, contradicting the residual upper bound 34 | `docs/n6_b27_common_quotient_exclusion.md` |
| N6-011 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | the `b=26` defect patterns have relation-kernel cap zero or one and force central rank at least 60, contradicting the residual upper bound 32 | `docs/n6_b26_one_relation_exclusion.md` |
| N6-012 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | the `b=25` defect patterns have relation-kernel cap at most two and force central rank at least 78, contradicting the residual upper bound 30 | `docs/n6_b25_two_relation_exclusion.md` |
| N6-013 | `SUPERSEDED`, `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | componentwise scalar Macaulay prolongation and a block-Sylvester inequality exclude 23-term decompositions, proving the historical lower bound 24 | `docs/n6_component_prolongation_exclusion.md` |
| N6-014 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | under a hypothetical 24-term decomposition, fixing six terms gives `40<=b<=64`; `b=40,41` are Koszul-strict and G-019 plus block-Sylvester and exact defect arithmetic exclude every `42<=b<=64`, hence `ChowRank(perm_6)>=25` | `docs/n6_fixed_six_lower25.md`, `scripts/n6_fixed_six_lower25_audit.py`, independent `16^6` labelled replay, and compact frozen payload |
| N6-015 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | under a hypothetical 25-term decomposition, exact `q=6,7,8` fixed-count arithmetic leaves respectively 327, 355, and 635 states after vector-Macaulay central pruning; no fixed count is selected and the central first-Koszul route is suspended for lower 26 | `docs/n6_lower26_fixed_q_diagnostic.md`, `scripts/n6_lower26_fixed_q_diagnostic.py`, and frozen table hashes |
| N6-016 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | for output degrees `2,3,4`, the first higher-wedge Koszul rank ratios certify only `15,21,16`, identical to the ordinary first-Koszul integer bounds; a dimension-only second shadow is vacuous for `q>=6`; the column-uniform Glynn family requires all 32 terms | `docs/n6_alternative_route_ceiling_comparison.md`, exact torus-block ranks, and G-020 |
| N6-017 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | the output-degree-two homology has dimensions `450` for `perm_6` and `15` for one independent Chow term, closing the exact ranks at `127125` and `8730`; a coupled common-factor six-term family has scalar homology `465`, so monotone scalar homology upper bounds cannot prove lower 26 | `docs/n6_second_koszul_homology_closure.md`, `scripts/n6_second_koszul_homology_audit.py`, and exact sparse replay |
| N6-018 | `LITERATURE_RECONCILED`, `ROUTE_DIAGNOSTIC` | the repository owner's Xu--Gnang arXiv:2311.05890 line is self-authored, withdrawn, and treated as disproved; its v2 row-homogeneous claim is not a theorem dependency or an external novelty gate | `docs/xu_gnang_v2_reconciliation.md`, exact v2 source hashes, and acquisition artifact `8922769747` |
| N6-019 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `RESTRICTED_FAMILY_THEOREM` | among the 5,984 normalized one-defect column-sign terms, `perm_6` has exact minimum support 32; the family span has dimension 987 and contains no representation with at most 31 terms | `docs/n6_one_defect_sign_rigidity.md`, primary and independent audits, exact integer minors, and frozen payload |
| N6-020 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | the 467,264-term normalized two-defect family has exact parity-block ranks `406,406,406,322,322,207` and span dimension 11,533; an explicit quadratic separator gives an exact permanent representation in only 24 base-labelled aggregate spaces, so the N6-019 32-base support mechanism does not extend | `docs/n6_two_defect_sign_block_diagnostic.md`, `scripts/n6_two_defect_sign_block_audit.py`, exact rational elimination, and frozen payload |
| N6-021 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `RESTRICTED_AGGREGATE_THEOREM` | the N6-020 separator functions satisfy `rho_2(f)=rho_2(1-f)=46`; therefore the specific 24-base aggregate assignment has exact actual-term cost 744 and cannot yield a decomposition with at most 25 terms | `docs/n6_two_defect_aggregate_atomic_rank.md`, `scripts/n6_two_defect_aggregate_atomic_rank_audit.py`, exact local support classification, and frozen payload |
| N6-022 | `SUPERSEDED`, `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | the count-product separator `g=n_4 n_5` gives an exact permanent representation in 16 nonzero base-labelled two-defect aggregate spaces; the former atomic-rank window `31<=rho_2(g)<=36` is superseded by N6-023 | `docs/n6_two_defect_sixteen_base_aggregate.md`, `scripts/n6_two_defect_sixteen_base_aggregate_audit.py`, exact local support enumeration, and frozen payload |
| N6-023 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `RESTRICTED_AGGREGATE_THEOREM` | the row retraction `1,2,3 -> 0` reduces the full fixed-base two-defect dictionary for `g=n_4 n_5` to labels `{0,8,16,24}`; exact local normal forms and a complete extra-budget search prove `rho_2(g)=36`, so the N6-022 16-base assignment has exact cost 576 | `docs/n6_two_defect_separator_rank36.md`, `scripts/n6_two_defect_separator_rank36_audit.py`, exact `Fraction` elimination, meet-in-the-middle coverage, and frozen payload |
| C-001 | `CONJECTURE` | `ChowRank(perm_n)=2^(n-1)` for all `n>=2` | Glynn upper bound; exact only for reviewed small `n` |

## Unverified items

- Literature novelty of G-001 through G-020 and N6-006 through N6-023 has not been exhaustively checked.
- No independent full replay of the omitted lower-15 SAT/DRAT layer for `n=5` is stored here.
- No exact unrestricted `n=6` claim is made; the current in-repository interval is `25<=ChowRank(perm_6)<=32`.
- N6-014 has an internal adversarial review and two independent finite replays but has not received external mathematical peer review.
- N6-014 does not prove `ChowRank(perm_6)>=26`, a border Chow-rank lower bound of 25, or the conjectural exact value 32.
- N6-015 through N6-017 are route diagnostics. They do not prove that lower 26 is impossible; they identify tested fixed-count, scalar-shadow, base-ratio, sign-family, and scalar-homology-upper-bound routes that do not supply a strict global margin.
- N6-017 uses the published Alper--Rowlands `beta_2,4` formula as an external theorem; this repository checks the `n=6` arithmetic, rank consequences, and common-factor falsification family but does not reprove that formula.
- N6-017 does not rule out an exact-value classification, multigraded homology, representation-theoretic homology, or quotient-coupled homology obstructions.
- N6-018 is an internal postmortem of a self-authored, withdrawn, disproved line; no result from that paper is used as a positive theorem input.
- G-020 is restricted to the 32 fixed column-uniform Glynn products. It does not control arbitrary row-sign, column-sign, row-homogeneous, or unrestricted Chow terms.
- N6-019 is exact only for the normalized one-defect sign family. The full column-sign family, row-sign family, arbitrary complex row-homogeneous tensor rank, and unrestricted Chow rank remain open.
- N6-019 supplies no unrestricted lower-26 implication and does not change the active interval `25..32`.
- N6-020 determines linear block ranks and base-aggregate support, not minimum term support. Its 24-base aggregate representation is not a 24-term decomposition and gives no new upper bound.
- N6-021 proves the exact cost 744 only for the fixed N6-020 aggregate assignment. It is not a lower bound for other aggregate assignments or for the global two-defect family.
- N6-023 proves `rho_2(g)=36` only for the fixed-base separator `g=n_4 n_5`; it does not prove 16-base minimality, lower-bound another aggregate assignment, or determine the global two-defect minimum.
- The N6-022 16-base aggregate assignment now has exact cost 576. This closes that construction as a route to at most 25 terms but does not rule out another two-defect assignment with smaller actual support.
- No decomposition with at most 25 two-defect terms has been found or ruled out. Broad sparse optimization remains unauthorized until the aggregate-assignment problem has a compact exact reduction.
- The small `F_2` calculation in the G-019 audit is diagnostic only; the characteristic-zero theorem rests on the universal-bundle and torus-degeneration proof.
- The frozen rational witnesses certify the displayed general lower bounds but are not proved globally optimal within G-014.
- G-018 proves optimality only for fixed integer output-degree offsets and fixed constant defects; it does not classify `n`-dependent offsets or defects.
- N6-002 shows that coordinate low-catalectic points lie on positive-dimensional branches; it does not classify the full rank-nine locus.
- N6-006 and N6-007 are one-term theorems and do not imply termwise additivity for a coupled sum.
