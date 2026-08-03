# Permanent Chow Rank Research

Pure-mathematics research on the Chow (product/split) rank of permanent polynomials.

**Language:** all mathematical proofs, research notes, certificate specifications, and audit reports in the active repository are written in English. See `LANGUAGE_POLICY.md`.

> **Repository boundary:** this repository is not a quantitative-finance, trading, market-data, brokerage, recommendation, or portfolio project. It must remain operationally and semantically separate from `quant-proj`, `A_Share_Monitor`, `US_Stock_Monitor`, `market_data`, and every other finance repository.

## Repository role

This is the **active mainline pure-mathematics research repository** for:

- exact and lower-bound results for `ChowRank(perm_n)`;
- deterministic symbolic and integer computations;
- proof drafts with explicit status labels;
- small, independently replayable certificates;
- research plans for general `n`, beginning with `n=6`.

The repository does **not** own large upstream proof bundles. External submissions and multi-gigabyte SAT/DRAT assets remain evidence inputs, identified by immutable hashes in `evidence/`.

## Current research status

| Item | Status | Claim |
|---|---|---|
| `n=3` | accepted baseline | `ChowRank(perm_3)=4` |
| `n=4` | independently exact-replayed | `ChowRank(perm_4)=8` |
| `n=5` | conditional external review | source submission claims `16`; the lower-16 overlay was replayed, while the omitted ~10 GB lower-15 SAT layer has not been independently regenerated here |
| General `n` derivative tower | proof draft complete | `dim D_m(perm_n)=binom(n,m)^2` and `D_m(perm_n)^(1)=D_{m+1}(perm_n)` |
| General Koszul lower bound | proof draft complete | exact computable formula in `docs/general_n_koszul_bounds.md` |
| Border Chow-rank lower bound | proof draft complete | the same closed determinantal obstruction gives `border-ChowRank(perm_n) >= L_K(n)` |
| Shadow-removal lower bound | proof draft complete | improves the ordinary Koszul bound for `n>=6`; for example `ChowRank(perm_6)>=22` |
| Exact general formula | conjectural | working conjecture `ChowRank(perm_n)=2^(n-1)` |

“Proof draft complete” means the argument is written in the repository and its arithmetic implementation is tested. It does **not** mean external peer review or literature novelty review has been completed.

## Reproduce the bound table

```bash
python -m unittest discover -s tests -v
python scripts/generate_bounds.py --max-n 50
```

The generator uses only the Python standard library and exact integer/rational arithmetic.

## Layout

```text
src/permanent_chow_rank/   exact bound implementation
scripts/                   deterministic table generation
tests/                     regression tests
docs/                      English proofs, assumptions, literature notes, and research program
data/                      generated exact bound tables
evidence/small_n/          read-only audit snapshots and source identities
```

## Fail-closed rule

A result may be promoted to `proved` only when:

1. every mathematical implication is written explicitly;
2. every finite computation has a deterministic generator or independently checkable certificate;
3. finite-field calculations are used only in a direction justified over characteristic zero;
4. all source artifacts are bound to immutable hashes;
5. unexecuted tests and unavailable evidence remain explicitly unverified.
