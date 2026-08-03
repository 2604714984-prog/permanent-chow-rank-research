# Research status ledger

Status vocabulary:

- `VERIFIED_BASELINE`: independently checked small-`n` result.
- `PROOF_DRAFT_COMPLETE`: complete internal proof draft; not externally reviewed.
- `COMPUTATION_REPLAYED`: deterministic computation rerun successfully.
- `CONDITIONAL`: depends on evidence not fully regenerated in this repository.
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
| G-005 | `PROOF_DRAFT_COMPLETE` | shadow-removal lower bound `L_SR(n)` | intersection lemma and double-quotient argument |
| G-006 | `PROOF_DRAFT_COMPLETE` | `ChowRank(perm_6)>=22` | G-005 with `(m,d,q)=(3,1,1)` |
| G-007 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=L_K(n)` | closed determinantal rank locus |
| G-008 | `PROOF_DRAFT_COMPLETE` | `border-ChowRank(perm_n)>=binom(n,floor(n/2))+1` | central-degree corollary of G-007 |
| C-001 | `CONJECTURE` | `ChowRank(perm_n)=2^(n-1)` for all `n>=2` | Glynn upper bound; exact only for reviewed small `n` |
| N6-001 | `OPEN` | exclude a 31-term decomposition of `perm_6` | `docs/n6_research_program.md` |

## Unverified items

- Literature novelty of G-001 through G-008 has not been exhaustively checked.
- No independent full replay of the omitted lower-15 SAT/DRAT layer for `n=5` is stored here.
- No exact `n=6` rank claim beyond the lower bound 22 is made.
