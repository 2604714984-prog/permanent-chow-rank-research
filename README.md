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
| `n=5` | repaired proof draft complete; conditional model-assisted external audit | `ChowRank(perm_5)=16`; v14 supplies a characteristic-zero projective degeneration and a deterministic exact endpoint certificate over 886,464 flags; named independent human review remains pending |
| General derivative tower | proof draft complete | `dim D_m(perm_n)=binom(n,m)^2` and `D_m(perm_n)^(1)=D_{m+1}(perm_n)` |
| General first-Koszul bound | proof draft complete | exact formula; its unique optimizing output degree is `m=ceil(n/2)` |
| Border Chow-rank bound | proof draft complete | the determinantal first-Koszul obstruction gives `border-ChowRank(perm_n)>=L_K(n)` |
| Zero-intersection shadow removal | proof draft complete | additive gain at least `Omega(((1+sqrt(2))/2)^n/sqrt(n))` |
| General multidimensional-shadow bound | proof draft complete | valid for every `n>=4`; reviewed examples include `ChowRank(perm_5)>=13`, `ChowRank(perm_6)>=23`, `ChowRank(perm_7)>=41`, and `ChowRank(perm_9)>=141` |
| Parity-sensitive multishadow asymptotics | proof draft complete | additive scale `Theta(2^n/n^(3/2))`; the odd constant is twice the even constant in `binom(n,floor(n/2))/n` normalization |
| Fixed-offset multishadow optimization | proof draft complete | among every fixed integer output-degree offset and constant witness defect, the unique asymptotic optimizer is the central lower output degree |
| Quotient Koszul gain | proof draft complete | exact residual refinement `rank K_m(perm_n-R)>=A-n^2 b+Gamma` |
| Vector-valued Macaulay relation cap | proof draft complete; finite interfaces replayed | for `K subset W tensor Sym^2 V`, `dim K^(1)<=dim(K)^{<2>}`; the proof uses a universal Grassmannian kernel and an explicit colored-monomial degeneration |
| Glynn column-uniform sign family | proof draft complete; exact Walsh replay | the `2^(n-1)` sign products are linearly independent and the unique expansion of `perm_n` in their span uses every term |
| Scalar derivative-profile ceiling | proof draft complete; exact replay | every monotone homogeneous subadditive profile method is capped at `binom(n,floor(n/2))`; nonnegative weighted scalar catalecticant sums cannot beat the central degree |
| Full column-sign and row-sign families | proof draft complete; primary and independent Walsh replay | `ColumnSignRank(perm_n)=RowSignRank(perm_n)=2^(n-1)`; the same lower bound holds for arbitrary off-diagonal coefficients with nonzero row-zero anchors and sign-valued normalized diagonal ratios |
| General relation tableau and central pairing | proof draft complete; exact sparse replay | arbitrary-degree vector Macaulay growth and noncentral block-Sylvester control coupled sums; the exact central correction is a restricted relation pairing, but it can vanish on a strict two-term Chow sum |
| Central relation-radical falsification | proof draft complete; exact rational replay; diagnostic only | an explicit six-term squarefree presentation has `rho=47` and `rank(beta|R)=24`, so its radical has dimension `23>4(6-1)`; the presentation is not proved minimum, and the minimum-decomposition version remains open |
| Three-monomial radical classification | proof draft complete; exact rational replay; restricted family | for three distinct squarefree sextic coordinate monomials, central rank above the two-term cap 40 forces radical dimension at most `8=4(3-1)`; the bound is sharp for a certified minimum three-term sum |
| Central-minimality radical bound | proof draft complete | if the middle catalecticant itself certifies a `q`-term degree-`2m` decomposition as minimum, then `dim rad(beta|R)<=floor((binom(2m,m)-1)/2)`; for sextics this is 9 |
| First-Koszul-minimality radical bound | proof draft complete | if the standard first-Koszul flattening itself certifies a `q`-term degree-`2m` decomposition as minimum, then `dim rad(beta|R)<=floor((N binom(2m,m)+(q-1)binom(2m,m+1)-1)/(2N))`; this remains conditional and does not certify 25 terms for `perm_6` |
| Quotient Koszul relation budget | proof draft complete; diagnostic only | after quotienting by `im K_3(perm_6)`, the fixed-sum gain is the rank of a sum of individually lossless maps and satisfies `Gamma>=sum r_i-36 rho-eta-j`; the unresolved aggregate collision `j` prevents a lower-26 conclusion |
| General quadratic psi chart | pure proof draft; exact replay for `n=3..6` | for every `n>=3`, `ker psi_v=span([v^2])`; one new quadratic direction adds at least `n^2-1` first-Koszul dimensions, but gains from several directions need not add |
| General derivative-degree psi chart | pure proof draft; selected exact replay through `n=6` | for every `n>=3` and `2<=m<=n-1`, `ker psi_(m,v)=span([v^m])`; one new degree-`m` direction adds at least `n^2-1`, without an additivity claim |
| Higher-wedge psi extrapolation barrier | pure counterexample; exact rational replay | at `n=3,m=2,p=3`, adjoining `x_00^2` has quotient gain exactly `47<binom(8,3)=56`; nine explicit independent relations show that the proved `p=1` chart has no formal binomial amplification |
| Two-Chow central/Koszul separation | pure proof draft; exact rational replay | two full-rank sextic Chow terms can have disjoint 20-dimensional middle images while their internal Koszul-output intersections are `(0,18,96,100,48,9,0)` across wedge degrees `0..6`; after embedding in 36 variables the middle third-Koszul loss is `10,810`, so higher wedges can amplify rather than remove the collision |
| Hereditary central/Koszul barrier | pure counterexample; exact integer replay | an explicit twenty-term sum has middle rank 384, all `2^20-1` nonempty displayed sub-sums are centrally certified minimum, and all terms have middle rank 20, yet its middle third-Koszul collision is at least 286,260; central heredity alone cannot close lower 27 |
| Rank-20 Chow homology profiles | exact characteristic-zero replay; route barrier | four full-middle-rank sextic Chow terms have ambient third-Koszul homology dimensions `20,320,1105,13961`; scalar homology is not controlled by central rank, while the factor-labelled cycle map remains only a candidate invariant |
| Colored initial-module barrier | pure combinatorial counterexample; exact integer replay | even a 336-dimensional colored cubic relation space, twenty active labels, per-label caps, torus initiality, and zero hereditary defect can coexist with only 203 quadratic relations; dimension/capacity data alone cannot improve the permanent-specific bound |
| Aggregate labelled-cycle barrier | exact rational and strict modular replay | five explicit full-factor-span rank-20 Chow terms make their boundary sum equal the entire 840-dimensional six-variable Koszul kernel, so all 100 labelled cycles vanish in the uncolored aggregate-boundary quotient |
| General recursive-row slice barrier | pure theorem; exact integer replay | mixed derivative/restriction maps have one-term cap `binom(n,m)`; the coordinate last-row permanent ratio is exactly `binom(n-1,m)`, and overlapping cofactor derivative spaces prevent a doubling recurrence |
| `n=6` one-step route barrier | computation replayed; diagnostic only | exact continuous optimization of the former scalar formula stops at 23 |
| `n=6` universal single-term full gain | proof draft complete | every nonzero degree-six Chow term `T`, including degenerate terms, satisfies `im K_3(perm_6) intersect im K_3(T)=0`, hence `Gamma=rank K_3(T)` |
| `n=6` fixed-four projection frontier | proof draft complete; exact arithmetic replayed | the raw range is `20<=b<=27`; common-quotient and low-relation arguments exclude `b=27,26,25` |
| `n=6` component-prolongation closure | superseded proof draft; exact arithmetic replayed | excludes 23-term decompositions and proves the historical lower bound 24 |
| `n=6` fixed-six lower-25 closure | proof draft complete; primary and independent arithmetic replayed | fixing six terms in a hypothetical 24-term decomposition gives `40<=b<=64`; vector-valued Macaulay growth and block-Sylvester exclude every state, so `ChowRank(perm_6)>=25` |
| `n=6` lower-26 fixed-count diagnostic | computation replayed; no route selected | `q=6,7,8` leave 327, 355, and 635 states after central pruning, so the central first-Koszul fixed-count route is suspended |
| `n=6` average-subset lower-26 closure | proof draft complete; exact rational/integer replay | conditional submodular averaging selects six terms of any hypothetical 25-term decomposition with central rank at least 87; the residual forces `b>=54`, while the exact fixed-six shadow/Macaulay cap gives `b<=53`, so `ChowRank(perm_6)>=26` |
| `n=6` single-term middle-rank gap | proof draft complete; exact integer/rational replay | a sextic Chow term cannot have middle-catalectic rank 19; for four-dimensional factor span the central determinant is the squared product of the fifteen four-factor brackets up to a nonzero constant |
| `n=6` hereditary lower-27 residual reduction | proof draft complete; exact integer/rational replay | a hypothetical 26-term decomposition forces a twenty-term residual of middle rank at least 384; all its nonempty sub-sums are centrally certified minimum and at least twelve residual terms have individual middle rank 20 |
| `n=6` lower-27 cross-degree relation frontier | proof draft complete; exact integer/rational replay | the residual central relation defect is at most 16, its quartic relation space at most 25, and its permanent-relative quadratic intersection at least 203; the fixed-six dual quartic intersection is at most 22, but these scalar consequences remain compatible and do not prove lower 27 |
| `n=6` fixed-six off-central `C_(4,2)` ceiling | proof draft complete; exact rational/integer replay | `t_2<=90-Shadow(b)` and `rank C_(4,2)(Q)<=315-Shadow(b)<=251`; at `b=64`, `(h,d_2,a_2,t_2)=(120,90,78,12)` and the residual rank lies in `215..237`, ruling out only the naive rank-above-300 criterion |
| `n=6` same-operator colored mapping cone | pure exact sequences; exact rational replay | synchronized colored relations sharpen the cubic lower bound from 320 to 336; ordinary relation dimension neither determines nor monotonically lower-controls the labelled quotient kernel, so weight-refined connecting maps remain necessary along this route |
| `n=6` symmetric two-level orbit rank | pure restricted-family theorem; exact symbolic replay | allowing arbitrary complex two-level ratios in the full `S_6` row-subset orbit ansatz still requires exactly 32 terms; the only 31-term orbit shape is excluded by explicit determinants and a final partition functional |
| `n=6` alternative-route ceilings | proof draft complete; computation replayed; diagnostic only | the first higher-wedge ratios at output degrees `2,3,4` remain `15,21,16`; a scalar second shadow is vacuous for `q>=6`; the full sign-family construction route is closed at 32 by the general Boolean-slice theorem |
| `n=6` complete standard Koszul--Young ceiling | proof draft complete; exact rational and strict modular replay | for every output degree and every exterior degree, the rank ratio is strictly below 26; this entire standard flattening family cannot prove lower 27 and does not change `26<=ChowRank(perm_6)<=32` |
| `n=6` linear-restriction Koszul--Young ceiling | proof draft complete; pure triangular and strict modular replay | after every linear restriction to `1<=k<=36` variables, every standard Koszul--Young ratio is still strictly below 26; linear compression cannot rescue a lower-27 proof by this family |
| `n=6` complete shifted-partial ceiling | pure dimension theorem; exact integer replay | for every derivative degree and every nonnegative shift, the rank ratio is at most `843600/35009<25`; the entire shifted-partial family cannot even certify lower 26 |
| `n=6` middle third-Koszul rank | proof draft complete; exact local and strict modular replay; lower-27 interface | exact rank `2715505`, forty explicit homology classes, and one-term cap `133545`; a hypothetical six-term complement must create two-sided row/column overlap defect at least `44605` |
| `n=6` second-Koszul homology closure | proof draft complete; computation replayed; diagnostic only | the output-degree-two ranks are exactly `127125` for `perm_6` and `8730` for one independent Chow term; a six-term common-factor family has scalar homology `465>450`, rejecting monotone scalar homology upper bounds for lower 26 |
| `n=6` extremal six-plane classification | proof draft complete; exact local replay | equality `dim(D_2(perm_6) intersect Sym^2 L)=3` forces a disjoint-support `2 x 3` or `3 x 2` tensor plane; the reduced locus has 5,580 seven-dimensional components |
| `n=6` coordinate-monomial audit | computation replayed; theorem input | all 167 coordinate orbits replay the exact local rectangle-space certificate used by the universal theorem |
| `n=6` two-permutation-monomial quotient transversality | proof draft complete; exact rational replay; restricted family | all 11 relative cycle types have aggregate collision `j=0`; the sum of either pair of permutation-monomial Koszul output spaces remains disjoint from `im K_3(perm_6)` |
| `n=6` six-permutation aggregate collision | proof draft complete; exact rational replay; diagnostic only | six permutation monomials sharing three complement factors have `eta=1143` and aggregate collision `j=36`; their sum has a four-term Chow expression, so the six-term presentation is not minimum |
| `n=6` minimum six-permutation aggregate collision | proof draft complete; exact rational replay; diagnostic only | a block-diagonal six-permutation sum has exact Chow rank six, `rho=eta=0`, and aggregate collision `j=72`; therefore minimum length and vanishing central/internal relations do not force quotient-Koszul transversality |
| `n=6` six-permutation central-intersection cap | proof draft complete; restricted family; exact diagnostic replay | every six permutation monomials satisfy `dim(D_3(perm_6) intersect H)<=2`; hence this entire coordinate subfamily misses the hypothetical six-fixed lower-26 requirement `b>=20` |
| `n=6` six-coordinate-monomial central-intersection cap | proof draft complete; restricted family; pure proof | every six degree-six coordinate monomials satisfy `dim(D_3(perm_6) intersect H)<=19`; equality in the initial counting cap 20 would force all six terms to be permutation monomials and contradict the cap two |
| `n=6` six column-uniform sign-term residual exclusion | proof draft complete; restricted fixed part; pure proof | six distinct column-uniform sign terms have coupled central dimension `h=120` and intersection `b<=40`, contradicting the residual necessity `h<=2b-20` in every hypothetical 25-term decomposition, even if the other nineteen terms are arbitrary |
| `n=6` diagonal quotient-gain audit | superseded diagnostic | the former one-term example `Gamma=705` is contained in the universal theorem |
| `n=6` coordinate secant audit | computation replayed; diagnostic only | all 79,800 coordinate pairs classified; the rank-nine locus has projective tangent dimension 18 at every coordinate point |
| Exact unrestricted general formula | conjectural | working conjecture `ChowRank(perm_n)=2^(n-1)` |

“Proof draft complete” means the argument is written in the repository and its arithmetic implementation is tested. It does **not** mean external peer review or literature novelty review has been completed.

The current in-repository unrestricted interval for `n=6` is

```text
26 <= ChowRank(perm_6) <= 32.
```

The full sign-family rank is exactly 32. The new lower bound 26 is for ordinary Chow rank; no border-lower-26 or exact unrestricted-32 claim is made.

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

These are the values of the general multidimensional-shadow theorem. The specialized `n=6` average-subset argument improves its row from 23 to the current best in-repository proof-draft lower bound 26. The frozen rational witnesses are certificates of the displayed general values; they are not claimed to be globally optimal.

## Reproduce the deterministic results

```bash
python scripts/check_english_only.py
python evidence/small_n/v14_repaired/verify_assets.py --replay
python -m unittest discover -s tests -v
python scripts/generate_bounds.py --max-n 50
python scripts/generate_multishadow_bounds.py
python scripts/generate_multishadow_asymptotic_diagnostics.py
python scripts/generate_even_multishadow_bounds.py
python scripts/n6_coordinate_secant_audit.py
python scripts/n6_multishadow_route_barrier.py
python scripts/n6_quotient_gain_audit.py
python scripts/n6_coordinate_monomial_full_gain_audit.py
python scripts/n6_two_permutation_monomial_quotient_audit.py
python scripts/n6_six_permutation_collision_audit.py
python scripts/n6_fixed_four_coupled_frontier.py
python scripts/n6_extremal_six_plane_audit.py
python scripts/n6_b24_three_relation_frontier.py
python scripts/n6_component_prolongation_exclusion.py
python scripts/vector_valued_macaulay_audit.py
python scripts/n6_fixed_six_lower25_audit.py
python scripts/n6_fixed_six_lower25_independent_audit.py
python scripts/n6_lower26_fixed_q_diagnostic.py
python scripts/n6_lower26_average_subset_audit.py
python scripts/n6_second_koszul_rank_audit.py
python scripts/n6_second_koszul_homology_audit.py
python scripts/glynn_family_rigidity_audit.py
python scripts/general_column_row_sign_rank_audit.py
python scripts/general_relation_tableau_audit.py
python scripts/general_relation_radical_counterexample.py
python scripts/degree6_three_monomial_radical_classification.py
python scripts/general_derivative_profile_ceiling_audit.py
python scripts/general_higher_wedge_psi_barrier.py
python scripts/general_column_sign_rigidity_audit.py
python scripts/general_column_sign_rigidity_independent.py
```

The bound generators use only the Python standard library and exact integer/rational arithmetic. The asymptotic diagnostic evaluates exact finite certificates with `Fraction`; decimal constants are display-only checks of the proved formulas. The coordinate tangent audit uses a finite-field rank only in the valid direction: a rank-381 certificate modulo `1,000,003`, together with 19 explicit characteristic-zero tangent directions, proves exact affine tangent dimension 19 over `Q`.

The scalar derivative-profile theorem proves a structural ceiling rather than a numerical promotion. Even using all derivative degrees with arbitrary nonnegative weights cannot beat the central binomial coefficient. The raw adjacent differentiation-map kernel dimension is also determined by the profile. The general program therefore moves to coordinate-invariant natural maps, higher compatibility quotients, syzygies, and coupled relation modules.

The full column-sign theorem uses a Boolean diagonal coefficient slice. Every normalized column-sign term becomes one Walsh character determined by its diagonal signs, while the permanent becomes a delta function. Walsh inversion forces all `2^(n-1)` signature aggregates to be nonzero, and Glynn supplies the matching upper bound. For `n=6`, this closes the entire `2^30` normalized column-sign family at 32 terms without enumerating it. Arbitrary complex row-homogeneous and unrestricted Chow terms remain outside the theorem.

The universal single-term theorem first degenerates the at-most-six-dimensional factor span to a coordinate subspace while keeping the relevant quadratic intersection at fixed dimension. The coordinate audit then supplies the only local cases: no rectangle, one rectangle, or a `K_2,3` / `K_3,2` rectangle space. The last case is eliminated by regenerated integer minors of determinant `-1` in orders 18 and 45.

The fixed-four projection and Bukh argument first gives the raw range `20<=b<=27` and 36 states. Equality at `b=27` forces a common 12-dimensional quadratic quotient, a direct quadratic sum of dimension 60, and coupled middle-catalectic rank 80, contradicting the residual upper bound 34. Low-relation arguments exclude the next two layers, and componentwise scalar Macaulay growth closes the historical 23-term frontier, proving lower 24.

The lower-25 proof does not mechanically reuse that state table. Under a hypothetical 24-term decomposition it fixes six terms and leaves eighteen. Projection and Bukh compression give `40<=b<=64`; the layers `b=40,41` are already Koszul-strict. For every remaining layer, the full colored quadratic relation module has dimension at most 16. The vector-valued Macaulay theorem bounds its cubic relation module by `k^{<2>}`, and a block-Sylvester inequality converts that cap into a coupled middle-catalectic lower bound. Exact defect arithmetic gives a positive margin in every layer; the smallest margin is two at `b=43,44`. A second implementation independently scans all `16^6=16,777,216` labelled defect tuples.

The lower-26 fixed-count diagnostic tests `q=6,7,8` under a hypothetical 25-term decomposition and leaves hundreds of states when the fixed subset is arbitrary. N6-030 supplies the missing selection step. If `U_i` are the individual middle-catalectic images, condition on a term of maximum central rank and apply submodular averaging to the other five choices. The relation-pairing identity then selects six indices with coupled central rank at least 87. The nineteen-term residual forces central intersection `b>=54`. Exact rational Bukh-shadow endpoints and an integer enumeration of at most 33 symmetric defect profiles per terminal layer prove the universal fixed-six cap `b<=53`. This contradiction proves the ordinary lower bound 26. The argument does not prove border rank 26 or exact unrestricted rank 32.

For the lower-27 program, the single-term central rank 19 is now excluded. In factor-span dimension four, a dependent four-set produces two independent cubic apolar operators; divisibility and multidegree then factor the 20 by 20 determinant as a nonzero constant times the squared product of all four-factor brackets. The five-dimensional dependence normal forms have exact ranks `14,14,18,20,20`. Thus the surviving maximum-single-term-rank frontier is forced to rank 20, but this does not yet close lower 27.

The next reduction selects six terms from any hypothetical 26-term decomposition and forces the twenty-term residual to have middle-catalectic rank at least 384. Hence every `s`-term sub-sum of that residual has middle rank at least `20s-16`, strictly certifying Chow rank `s`; every central relation-pairing radical is at most nine and at least twelve residual summands have individual middle rank 20. Its middle image intersects the permanent middle space in dimension `336..380`, and its colored relation space modulo the permanent has dimension at least 320. The unresolved step is to exclude this hereditary central-minimal residual using that cross-degree quotient module. Scalar shadow and submodular averaging alone do not do so.

The output-degree-two homology closure identifies the middle higher-Koszul homology with `Tor_2(A_f,k)_4`. The Alper--Rowlands formula gives dimension 450 for `perm_6`, while a six-factor Chow complete intersection gives 15. Hence the exact ranks are `127125` and `8730`, still yielding ratio 15. An independently reconstructed common-factor family has scalar homology dimensions `15,55,120,210,325,465` for one through six terms, so monotone scalar homology upper bounds cannot separate `perm_6` from low-term sums. Multigraded and representation-theoretic refinements remain open.

The vector-valued Macaulay audit checks 3,996 distinct colored quadratic weights, all six-part successor inequalities through total dimension 16, and all 2,825 subspaces of a small divided-power `F_2` model. The finite-field calculation is a deterministic counterexample search only; it is not used to transfer an equality to characteristic zero.

The earlier first higher-wedge audit split the `p=2` matrices by exact row-column torus weight and performed sparse rank over `F_1000003`. Its output-degree-two modular value was used only as a characteristic-zero lower bound. The later homology theorem supplies the exact characteristic-zero equality and supersedes the former rank window.

The extremal six-plane theorem remains an independent structural result. At a coordinate `K_2,3` point, the exact local rank chart has Jacobian rank `163`, a 17-dimensional tensor-product tangent kernel, and 13 independent second-order disjoint-support obstructions. A squarefree multiplicity comparison gives exactly 432 local branches; projective torus globalization gives 5,580 seven-dimensional support components.

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
