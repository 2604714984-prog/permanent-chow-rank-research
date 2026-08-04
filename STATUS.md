# Research status ledger

Status vocabulary:

- `VERIFIED_BASELINE`: independently checked small-`n` result.
- `PROOF_DRAFT_COMPLETE`: complete internal proof draft; not externally reviewed.
- `COMPUTATION_REPLAYED`: deterministic computation rerun successfully.
- `ROUTE_DIAGNOSTIC`: exact finite result used to assess a proof route, not itself a Chow-rank theorem.
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
| G-006 | `SUPERSEDED` | `ChowRank(perm_6)>=22` | G-005 with `(m,d,q)=(3,1,1)`; superseded by G-011 and N6-013 |
| G-007 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=L_K(n)` | closed determinantal rank locus |
| G-008 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=binom(n,floor(n/2))+1` | central-degree corollary of G-007 |
| G-009 | `PROOF_DRAFT_COMPLETE` | `L_SR(n)>=L_K(n)+Omega(a^n/sqrt(n))`, `a=(1+sqrt(2))/2` | entropy optimization and Stirling estimates |
| G-010 | `PROOF_DRAFT_COMPLETE` | even-degree multidimensional-shadow bound | `docs/even_n_multidimensional_shadow_bound.md`; special case of G-014 |
| G-011 | `SUPERSEDED` | `ChowRank(perm_6)>=23` | G-014 with `m=3`, `q=4`, and complementary intersection cap 40; superseded by N6-013 |
| G-012 | `PROOF_DRAFT_COMPLETE` | for even `n`, the G-010 additive gain over `L_K(n)` is `(1/(e log 2)+o(1))*binom(n,n/2)/n` | gamma-ratio expansion and one-variable optimization |
| G-013 | `PROOF_DRAFT_COMPLETE` | the G-010 route independently excludes seven terms for `perm_4` | fix two terms, intersection cap 6, residual rank `464>5*92` |
| G-014 | `PROOF_DRAFT_COMPLETE` | for arbitrary `n>=4`, `rank K_m(perm_n-R)>=A-n^2 b`, where `b=dim(D_{n-m}(perm_n) intersect D_{n-m}(R))`; Bukh shadows convert this into a computable Chow-rank lower bound | `docs/general_multidimensional_shadow_bound.md` |
| G-015 | `PROOF_DRAFT_COMPLETE` | reviewed exact-rational bounds include `ChowRank(perm_5)>=13`, `ChowRank(perm_7)>=41`, `ChowRank(perm_9)>=141`, `ChowRank(perm_11)>=506`, and `ChowRank(perm_15)>=6879` | `data/multishadow_bounds.json` and regression tests |
| G-016 | `PROOF_DRAFT_COMPLETE` | exact refinement `rank K_m(perm_n-R)>=A-n^2 b+Gamma`, where `Gamma` is the quotient Koszul image gain | `docs/quotient_koszul_gain.md` |
| G-017 | `PROOF_DRAFT_COMPLETE` | the odd-degree one-step multishadow gain is `(2/(e log 2)+o(1))*binom(n,floor(n/2))/n`, twice the even constant in this normalization | `docs/general_multishadow_parity_asymptotics.md` |
| G-018 | `PROOF_DRAFT_COMPLETE` | among all fixed integer output-degree offsets and fixed constant witness defects, the G-014 parity coefficients are uniquely maximized at the central lower output degree; the constants remain `1/(e log 2)` for even `n` and `2/(e log 2)` for odd `n` in `binom(n,floor(n/2))/n` normalization | `docs/general_multishadow_offset_optimality.md` and exact finite diagnostics |
| N6-001 | `OPEN` | exclude a 31-term decomposition of `perm_6` | `docs/n6_research_program.md` |
| N6-002 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | all 79,800 coordinate pairs in `D_3(perm_6)` have first-catalectic ranks `9,13,15,16,17,18`; the coordinate rank-nine tangent space has affine dimension 19 | `scripts/n6_coordinate_secant_audit.py` |
| N6-003 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | exact optimization of the former one-step Bukh-shadow formula over `m=2,3,4` stops at 23; its central `q=4` shadow cap 40 is attained by an explicit coordinate family | `scripts/n6_multishadow_route_barrier.py` |
| N6-004 | `SUPERSEDED`, `COMPUTATION_REPLAYED` | the explicit diagonal Chow term has full quotient Koszul gain `Gamma=705` | superseded by N6-006 |
| N6-005 | `COMPUTATION_REPLAYED` | every degree-six coordinate monomial `M` satisfies `im K_3(perm_6) intersect im K_3(M)=0`; all 167 row/column/transpose orbits are replayed | finite coordinate input to N6-006: `docs/n6_coordinate_monomial_full_gain.md` and exact `K_2,3` minors |
| N6-006 | `PROOF_DRAFT_COMPLETE` | every nonzero degree-six Chow term `T`, including repeated and linearly dependent factors, satisfies `im K_3(perm_6) intersect im K_3(T)=0`, hence its quotient gain equals `rank K_3(T)` | torus degeneration of the factor span plus N6-005; `docs/n6_universal_single_term_full_gain.md` |
| N6-007 | `PROOF_DRAFT_COMPLETE` | for every nonzero scalar `alpha` and degree-six Chow term `T`, `rank K_3(perm_6-alpha T)=14175+rank K_3(T)` | `D_3(perm_6) intersect D_3(T)=0`, N6-006, and the double-quotient inequality; `docs/n6_single_term_residual_additivity.md` |
| N6-008 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | the fixed-four projection, shadow, and central-catalectic inequalities first give the raw range `20<=b<=27`, `0<=d<=b-20`, and 36 states | individual quadratic intersection cap 3, projection shadow cap 48, Bukh compression, and symmetric middle catalectic; `docs/n6_fixed_four_coupled_frontier.md` |
| N6-009 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | every six-plane `L` with `dim(D_2(perm_6) intersect Sym^2 L)=3` is a disjoint-support `2 x 3` or `3 x 2` tensor-product plane; the reduced extremal locus has 5,580 seven-dimensional components, and each coordinate fixed point has exactly 432 local branches | exact `163/17/13` local certificate, squarefree multiplicity closure, and projective torus globalization; `docs/n6_extremal_six_plane_classification.md` |
| N6-010 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | equality in the four omitted-factor projection bounds at `b=27` forces a common 12-dimensional quadratic quotient, direct quadratic derivative sum of dimension 60, and coupled middle-catalectic rank 80, contradicting the residual upper bound 34 | `docs/n6_b27_common_quotient_exclusion.md` and revised frontier replay |
| N6-011 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | at `b=26`, the 24 exact defect patterns either force the quadratic sum to be direct or leave one quadratic relation; maximal quadratic dimension implies cubic dimension 20 and no pure cube, so the one-relation factorization lemma forces central rank at least 60, contradicting the residual upper bound 32 | `docs/n6_b26_one_relation_exclusion.md` and exact term-profile matrices |
| N6-012 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | at `b=25`, 213 exact defect patterns split into 189 direct, 23 one-relation, and one two-relation pattern; all cases contradict the residual upper bound 30 and leave the historical 15-state range `20<=b<=24` | `docs/n6_b25_two_relation_exclusion.md` and `scripts/n6_fixed_four_coupled_frontier.py` |
| N6-013 | `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED` | componentwise Macaulay prolongation and a block-Sylvester inequality exclude every `b=22,23,24` defect pattern; the three `b=20,21` states are already Koszul-strict, hence `ChowRank(perm_6)>=24` | `docs/n6_component_prolongation_exclusion.md`, `scripts/n6_component_prolongation_exclusion.py`, and frozen exact payload |
| N6-014 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | for a hypothetical 24-term decomposition, exact fixed-`q` arithmetic with `q=4,5,6` leaves respectively 260, 184, and 179 states after component-central pruning; `q=6` still has 141 structural states and is not promoted as a proof route | `docs/n6_lower25_fixed_q_diagnostic.md`, `scripts/n6_lower25_fixed_q_diagnostic.py`, and frozen state-summary hashes |
| C-001 | `CONJECTURE` | `ChowRank(perm_n)=2^(n-1)` for all `n>=2` | Glynn upper bound; exact only for reviewed small `n` |

## Unverified items

- Literature novelty of G-001 through G-018 and N6-006 through N6-014 has not been exhaustively checked.
- No independent full replay of the omitted lower-15 SAT/DRAT layer for `n=5` is stored here.
- No exact `n=6` claim is made; the current in-repository interval is `24<=ChowRank(perm_6)<=32`.
- The frozen rational witnesses certify the displayed general lower bounds but are not proved globally optimal within G-014.
- G-018 proves optimality only for fixed integer output-degree offsets and fixed constant defects; it does not classify `n`-dependent offsets or defects.
- N6-002 shows that coordinate low-catalectic points lie on positive-dimensional branches; it does not classify the full rank-nine locus.
- N6-003 is a barrier for the former scalar one-step formula only; it does not rule out higher fixed-term arguments, positive quotient gain, higher coupled shadows, or different flattenings.
- N6-006 and N6-007 are one-term theorems. They do not imply additivity of quotient gain for `K_3(T_1+...+T_q)`.
- N6-009 classifies individual equality planes and their factor-frame base locus, not arbitrary coupled frames.
- N6-013 excludes 23 terms only. It does not prove a 25-term lower bound, a border-rank lower bound of 24, or the conjectural exact value 32.
- N6-014 is deliberately fail-closed: it does not exclude a 24-term decomposition and does not select `q=6` without a new structural invariant.
