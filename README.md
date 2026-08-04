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
| General derivative tower | proof draft complete | `dim D_m(perm_n)=binom(n,m)^2` and `D_m(perm_n)^(1)=D_{m+1}(perm_n)` |
| General first-Koszul bound | proof draft complete | exact formula; its unique optimizing output degree is `m=ceil(n/2)` |
| Border Chow-rank bound | proof draft complete | the determinantal first-Koszul obstruction gives `border-ChowRank(perm_n)>=L_K(n)` |
| Zero-intersection shadow removal | proof draft complete | additive gain at least `Omega(((1+sqrt(2))/2)^n/sqrt(n))` |
| General multidimensional-shadow bound | proof draft complete | valid for every `n>=4`; reviewed examples include `ChowRank(perm_5)>=13`, `ChowRank(perm_6)>=23`, `ChowRank(perm_7)>=41`, and `ChowRank(perm_9)>=141` |
| Parity-sensitive multishadow asymptotics | proof draft complete | additive scale `Theta(2^n/n^(3/2))`; the odd constant is twice the even constant in `binom(n,floor(n/2))/n` normalization |
| Fixed-offset multishadow optimization | proof draft complete | among every fixed integer output-degree offset and constant witness defect, the unique asymptotic optimizer is the central lower output degree |
| Quotient Koszul gain | proof draft complete | exact residual refinement `rank K_m(perm_n-R)>=A-n^2 b+Gamma` |
| `n=6` one-step route barrier | computation replayed; diagnostic only | exact continuous optimization of the current scalar formula stops at 23 |
| `n=6` universal single-term full gain | proof draft complete | every nonzero degree-six Chow term `T`, including degenerate terms, satisfies `im K_3(perm_6) intersect im K_3(T)=0`, hence `Gamma=rank K_3(T)` |
| `n=6` fixed-four current frontier | proof draft complete; exact arithmetic replayed | the raw Chow-realizable cap gives `b<=27`; common-quotient rigidity excludes `b=27`, leaving `20<=b<=26` and 28 exact states |
| `n=6` extremal six-plane classification | proof draft complete; exact local replay | equality `dim(D_2(perm_6) intersect Sym^2 L)=3` forces a disjoint-support `2 x 3` or `3 x 2` tensor plane; the reduced locus has 5,580 seven-dimensional components |
| `n=6` coordinate-monomial audit | computation replayed; theorem input | all 167 coordinate orbits replay the exact local rectangle-space certificate used by the universal theorem |
| `n=6` diagonal quotient-gain audit | superseded diagnostic | the former one-term example `Gamma=705` is contained in the universal theorem |
| `n=6` coordinate secant audit | computation replayed; diagnostic only | all 79,800 coordinate pairs classified; the rank-nine locus has projective tangent dimension 18 at every coordinate point |
| Exact general formula | conjectural | working conjecture `ChowRank(perm_n)=2^(n-1)` |

“Proof draft complete” means the argument is written in the repository and its arithmetic implementation is tested. It does **not** mean external peer review or literature novelty review has been completed.

The current certified interval for `n=6` is

```text
23 <= ChowRank(perm_6) <= 32.
```

No exact-32 claim is made.

## Reviewed general lower-bound table

The current exact-rational multidimensional-shadow certificates give:

| `n` | first-Koszul `L_K(n)` | multidimensional-shadow lower bound | Glynn upper bound |
|---:|---:|---:|---:|
| 4 | 7 | 8 | 8 |
| 5 | 11 | 13 | 16 |
| 6 | 21 | 23 | 32 |
| 7 | 36 | 41 | 64 |
| 8 | 71 | 76 | 128 |
| 9 | 127 | 141 | 256 |
| 10 | 253 | 267 | 512 |
| 11 | 463 | 506 | 1,024 |
| 12 | 925 | 968 | 2,048 |
| 13 | 1,718 | 1,853 | 4,096 |
| 14 | 3,434 | 3,568 | 8,192 |
| 15 | 6,440 | 6,879 | 16,384 |
| 16 | 12,875 | 13,312 | 32,768 |

These are ordinary Chow-rank lower bounds. The frozen rational witnesses are certificates of the displayed values; they are not claimed to be globally optimal.

## Reproduce the deterministic results

```bash
python scripts/check_english_only.py
python -m unittest discover -s tests -v
python scripts/generate_bounds.py --max-n 50
python scripts/generate_multishadow_bounds.py
python scripts/generate_multishadow_asymptotic_diagnostics.py
python scripts/generate_even_multishadow_bounds.py
python scripts/n6_coordinate_secant_audit.py
python scripts/n6_multishadow_route_barrier.py
python scripts/n6_quotient_gain_audit.py
python scripts/n6_coordinate_monomial_full_gain_audit.py
python scripts/n6_fixed_four_coupled_frontier.py
python scripts/n6_extremal_six_plane_audit.py
```

The bound generators use only the Python standard library and exact integer/rational arithmetic. The asymptotic diagnostic evaluates exact finite certificates with `Fraction`; decimal constants are display-only checks of the proved formulas. The coordinate tangent audit uses a finite-field rank only in the valid direction: a rank-381 certificate modulo `1,000,003`, together with 19 explicit characteristic-zero tangent directions, proves exact affine tangent dimension 19 over `Q`.

The universal single-term theorem first degenerates the at-most-six-dimensional factor span to a coordinate subspace while keeping the relevant quadratic intersection at fixed dimension. The coordinate audit then supplies the only local cases: no rectangle, one rectangle, or a `K_2,3` / `K_3,2` rectangle space. The last case is eliminated by regenerated integer minors of determinant `-1` in orders 18 and 45.

The fixed-four projection and Bukh argument first gives the raw range `20<=b<=27` and 36 states. Equality at `b=27` forces four 15-dimensional quadratic derivative spaces, four three-dimensional permanent intersections, and a common 12-dimensional quotient. This in turn forces the four quadratic spaces to be direct and the coupled middle catalectic to have rank 80, contradicting the residual upper bound 34. The current frontier is therefore `20<=b<=26` with 28 states: 3 already strict, 10 addressable by relative-prolongation caps, and 15 still structural. The maximum remaining quotient-gain requirement is 157.

The extremal six-plane theorem independently classifies the individual equality geometry relevant to the near-endpoint layers. At a coordinate `K_2,3` point, the exact local rank chart has Jacobian rank `163`, a 17-dimensional tensor-product tangent kernel, and 13 independent second-order disjoint-support obstructions. A squarefree multiplicity comparison gives exactly 432 local branches; projective torus globalization gives 5,580 seven-dimensional support components.

## Layout

```text
src/permanent_chow_rank/   exact bound implementation
scripts/                   deterministic table generation and finite audits
tests/                     regression tests
docs/                      English proofs, assumptions, literature notes, and research program
data/                      generated exact bound tables and audit outputs
evidence/small_n/          read-only audit snapshots and source identities
```

## Fail-closed rule

A result may be promoted to `proved` only when:

1. every mathematical implication is written explicitly;
2. every finite computation has a deterministic generator or independently checkable certificate;
3. finite-field calculations are used only in a direction justified over characteristic zero;
4. all source artifacts are bound to immutable hashes;
5. unexecuted tests and unavailable evidence remain explicitly unverified.
