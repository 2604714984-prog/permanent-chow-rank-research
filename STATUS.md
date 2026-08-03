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
| G-006 | `SUPERSEDED` | `ChowRank(perm_6)>=22` | G-005 with `(m,d,q)=(3,1,1)`; superseded by G-011 |
| G-007 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=L_K(n)` | closed determinantal rank locus |
| G-008 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=binom(n,floor(n/2))+1` | central-degree corollary of G-007 |
| G-009 | `PROOF_DRAFT_COMPLETE` | `L_SR(n)>=L_K(n)+Omega(a^n/sqrt(n))`, `a=(1+sqrt(2))/2` | entropy optimization and Stirling estimates |
| G-010 | `PROOF_DRAFT_COMPLETE` | even-degree multidimensional-shadow bound of Theorem 1.1 | self-transpose middle catalecticant, quotient prolongation, and Bukh's shadow theorem |
| G-011 | `PROOF_DRAFT_COMPLETE` | `ChowRank(perm_6)>=23` | G-010 with an exact rational witness, `q=4`, and intersection cap 40 |
| G-012 | `PROOF_DRAFT_COMPLETE` | for even `n`, the G-010 additive gain over `L_K(n)` is `(1/(e log 2)+o(1))*binom(n,n/2)/n` | gamma-ratio expansion and one-variable optimization |
| G-013 | `PROOF_DRAFT_COMPLETE` | the G-010 route independently excludes seven terms for `perm_4` | fix two terms, intersection cap 6, residual rank `464>5*92` |
| N6-001 | `OPEN` | exclude a 31-term decomposition of `perm_6` | `docs/n6_research_program.md` |
| N6-002 | `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC` | all 79,800 coordinate pairs in `D_3(perm_6)` have first-catalectic ranks `9,13,15,16,17,18`; the coordinate rank-nine tangent space has affine dimension 19 | `scripts/n6_coordinate_secant_audit.py` |
| C-001 | `CONJECTURE` | `ChowRank(perm_n)=2^(n-1)` for all `n>=2` | Glynn upper bound; exact only for reviewed small `n` |

## Unverified items

- Literature novelty of G-001 through G-013 has not been exhaustively checked.
- No independent full replay of the omitted lower-15 SAT/DRAT layer for `n=5` is stored here.
- No exact `n=6` claim is made; the current in-repository interval is `23<=ChowRank(perm_6)<=32`.
- N6-002 shows that coordinate low-catalectic points lie on positive-dimensional branches; it does not classify the full rank-nine locus.
