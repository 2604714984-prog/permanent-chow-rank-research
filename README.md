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
| `n=6` `b=64` common-quotient rigidity | pure coordinate-fiber theorem; exact finite and strict modular replay | the endpoint forces six direct quadratic spaces over one common `W_12`; all 600 coordinate rectangle quotients have a unique actual Chow-space lift and are excluded, with fixed-fiber tangent rank 210 modulo six factor scalings; noncoordinate quotients remain open |
| `n=6` near-extremal fixed-six layers | proof draft complete; exact integer replay | at `b=62,63` the fixed central rank is 120, while at `b=61` it is 118 or 120; the scalar frontier has `73,11,11` states and several branches force four or five rectangle terms over a common `W_12`, but no layer is yet excluded |
| `n=6` weight-refined connecting barrier | pure Tor and weight theorem; exact rational replay | `H_(3,6)(perm_6)` consists of forty explicit row/column-heavy lines; the `336/203` intersection dimensions plus inverse-system closure permit connecting-kernel endpoints 0 and 40, so Chow realizability of `Q=P-H` is essential |
| `n=6` `b=64` frame-component specialization | pure component theorem; exact finite and strict modular replay | fixing the extremal six-plane makes the quotient map injective; Hall matching classifies all `5^6` component assignments, every admissible branch is generically quasi-finite, and one reduced noncoordinate fiber is certified, but exceptional cross-plane collisions remain open |
| `n=6` near-extremal six-plane frontier | pure dimension-five theorem; exact rational local replay | `dim L<=5` forces `dim(E_2 intersect Sym^2 L)<=1`; the six-plane rank-two stratum is nonempty and contains actual Chow terms with defects `(epsilon,alpha)=(0,1)`, so these terms require coupled rather than termwise exclusion |
| `n=6` `b=64` prolongation exclusion | pure projective fixed-point theorem; exact integer replay | the endpoint would require `dim(E_2+F)^(1)>=456`, while all 18,564 torus-fixed incidence candidates give the universal upper bound 436; hence `b=64` is impossible |
| `n=6` near-extremal quotient pruning | pure quotient-distance and prolongation theorems; exact rational/integer replay | distinct explicit star quotients intersect in dimension at most 11; independently, the extremal prolongation cap removes 21 scalar states, leaving `60,7,7` at `b=61,62,63`, but no complete layer is yet excluded |
| `n=6` global quotient-prolongation caps | pure projective fixed-point theorem; exact modular upper certificates | a quadratic space containing one actual extremal term has first-prolongation dimension at most `436,440,448` when its permanent quotient has dimension `12,13,14`; this removes `61,10,10` states at `b=61,62,63` |
| `n=6` `alpha=1` closure | pure projective theorem; exact state replay | actual `alpha=1` terms, including every fixed boundary degeneration, have caps `440,448` after zero or one extra quotient direction; all `b=62,63` states and all but one `b=61` state are excluded |
| `n=6` `alpha=2` prolongation exclusion | pure projective theorem; exact integer replay | an auxiliary six-plane covers both five- and six-dimensional factor spans; the universal term cap is 453, below the final `b=61` requirement 459, so the complete layers `b=61,62,63,64` are impossible |
| `n=6` arbitrary quotient-prolongation barrier | explicit characteristic-zero counterexample; exact rational replay | one thirteen-dimensional coordinate quotient has first prolongation 475, so dimension-only caps are false; the actual extremal/`alpha=1`/`alpha=2` incidence hypotheses are essential |
| `n=6` `b=60` scalar frontier | pure finite enumeration; exact integer replay | all 367 necessary states are classified; the existing term caps remove every state with quotient dimension at most 14, leaving exactly 84 states, all with `t_2=15`, direct quadratic sum, and fixed middle rank 120 |
| `n=6` global `t_2=15` prolongation cap | pure projective fixed-point theorem; exact parallel modular replay | a fifteen-dimensional quotient containing an extremal term, or lying in the actual `alpha=1` closure, has prolongation dimension at most 458; this removes 77 of the 84 `b=60` states |
| `n=6` `alpha=2`, `t_2=15` cap | pure projective fixed-point theorem; exact parallel modular replay | all one-rectangle fixed limits and the three-rectangle boundary have cap 458; six more `b=60` states are excluded, leaving only the all-`alpha=3` state |
| `n=6` individual `alpha=3` barrier | pure exact counterexample; exact rational/modular replay | the same-row Chow term has prolongation dimension exactly 520, so the last `b=60` state requires a genuinely six-term common-quotient/directness argument rather than another individual cap |
| `n=6` row/column `alpha=3` coupling | pure coupling theorem; exact rational replay | over the same-row or same-column common quotient, six literal-direct lifts force a sign-matrix rank at least four and hence permanent middle intersection at most 40, excluding both dangerous 520-dimensional endpoint families from the `b=60` state |
| `n=6` `alpha=3` common-quotient barrier | pure characteristic-zero counterexample; exact rational replay | six actual quadratic Chow spaces are literal direct and share one `W_15`, with `(d_2,a_2,t_2,h,b)=(90,75,15,120,0)`; common quotient plus directness alone cannot replace the cubic permanent-intersection condition |
| `n=6` coordinate `alpha=3` quotient injectivity | pure support-recovery theorem; exact finite replay | all 1,837,392 rectangle-free coordinate six-edge supports have distinct quotient `W_15` signatures; this coordinate injectivity does not extend literal directness through arbitrary noncoordinate degenerations |
| `n=6` pairing-parity barrier | pure characteristic-zero counterexample; exact rational replay | two full-middle-rank Chow terms have one nonisotropic central relation and sum rank exactly 39; one-dimensional relation loss need not be even, so the lower-28 near-direct endpoint requires permanent-relative geometry |
| `n=6` `b=59` scalar frontier | pure finite enumeration; exact integer replay | the same 367 necessary scalar states occur; all but the unique all-`alpha=3`, `t_2=15` state are excluded, and its required prolongation dimension rises to 461 |
| `n=6` product-shadow theorem | pure characteristic-zero theorem; exact integer DP replay | torus specialization and two-sided colex compression reduce every `b`-plane in the permanent cubic derivative space to a Ferrers support; the exact product shadow exceeds the fixed-six projection cap 78 for every `53<=b<=64` |
| `n=6` ordinary lower-27 completion | proof draft complete; independently audited exact integer replay | the product-shadow theorem removes `b=53,...,64`; exhaustive conservative defect/Macaulay arithmetic gives `h>2b` for every `45<=b<=52`, ruling out every hypothetical 26-term decomposition and proving `ChowRank(perm_6)>=27` |
| `n=6` lower-28 fixed-six reduction | proof draft complete; independently audited exact integer replay | conditional averaging, product shadows, and literal six-color lifting reduce every hypothetical 27-term decomposition to one all-`alpha=3` state at `b=50` |
| `n=6` literal-six shadow exclusion | pure characteristic-zero theorem; exact integer replay | any residual six-color literal span meets the permanent cubic space in dimension at least `100-b`; for `b<=47` its shadow is at least 81, contradicting the universal six-term quadratic projection cap 78 |
| `n=6` separated `alpha=3` exclusion | pure coupling theorem; exact integer replay; restricted family | six column-separated or row-separated terms with the common-`W_15`, direct quadratic/cubic data of the `b=50` endpoint satisfy `b<=40`; general nonseparated configurations remain open |
| `n=6` transverse-pair rigidity | pure characteristic-zero theorem; exact rational replay; restricted open locus | one pair whose twelve-dimensional section-difference shadow projects fully to two rows or two columns forces all six endpoint terms to be separated and hence `b<=40`; every pairwise row/column projection must therefore be singular in any surviving `b=50` configuration |
| `n=6` coordinate product-shadow equality | pure finite-support theorem; exact integer replay | every coordinate fifty-plane with product shadow 75 is one of two transposed hook supports; its second shadow has dimension 23, but no noncoordinate equality classification or lower-28 conclusion is claimed |
| `n=6` full product-shadow equality locus | pure characteristic-zero formal/projective theorem; exact rational and symbolic replay | the complete equality locus is the union of closures of 240 four-parameter Boolean-replacement branches and their transposes; every equality plane has second shadow 23 |
| `n=6` all-singular hook exclusion | pure characteristic-zero theorem; independently audited exact rational replay | the common quotient synchronizes all six row and column block images; the 23-dimensional flag hook leaves only three or four full contractions, and the remaining label and column-rank cases are contradictory, excluding the last `b=50` endpoint and proving `ChowRank(perm_6)>=28` |
| `n=6` lower-29 first frontier | pure fixed-six reduction; exact integer replay; partial | adapting literal-six lifting and the quotient prolongation caps excludes the new layers `b=28,29,30`; the first surviving layer `b=31` is a hereditary `49 -> 75` product-shadow equality configuration, while `b=31,...,46` remain open |
| `n=6` fixed `K_3,4` Fano exclusion | pure characteristic-zero projective theorem; exact finite replay | the rank-at-most-nine six-plane Fano scheme in `A_3 tensor B_4` consists of 18 reduced coordinate rectangles, and its cross-image-at-most-three pair incidence is diagonal; this excludes actual complementary pairs only in the fixed layer |
| `n=6` colored-differential barrier | explicit characteristic-zero linear model; exact modular certificate | all endpoint subset caps and the canonical common kernels coexist with surjective colored shadows in four, five, and six colors; any successful continuation must use actual Chow coproduct or integrability structure |
| `n=6` squarefree-coproduct colored barrier | canonical per-color coproduct construction; exact modular upper certificates | six squarefree cubic coproducts have total kernel exactly 50 while every proper color-subset kernel obeys the endpoint cap; the missing constraints are cross-color ambient directness and the common-section cocycle |
| `n=6` hook-plane projection barrier | explicit rational Grassmann arrangement; exact rational replay | six pairwise-transverse six-planes span a 23-dimensional equality hook while every candidate two-row and two-column pair projection is singular; hook dimensions alone cannot trigger transverse-pair rigidity |
| `n=6` central-to-quadratic converse barrier | pure characteristic-zero counterexample; exact rational replay | two Chow terms have literal relation dimensions `(kappa_2,kappa_3,kappa_4)=(1,0,0)` and coupled ranks `(29,40,29)`; central and quartic literal directness do not force quadratic literal directness |
| `n=6` alternative-route ceilings | proof draft complete; computation replayed; diagnostic only | the first higher-wedge ratios at output degrees `2,3,4` remain `15,21,16`; a scalar second shadow is vacuous for `q>=6`; the full sign-family construction route is closed at 32 by the general Boolean-slice theorem |
| `n=6` complete standard Koszul--Young ceiling | proof draft complete; exact rational and strict modular replay | for every output degree and every exterior degree, the rank ratio is strictly below 26; this entire standard flattening family cannot supply the now-proved coupled lower bound 27 |
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
28 <= ChowRank(perm_6) <= 32.
```

The full sign-family rank is exactly 32. The lower bound 28 is for ordinary Chow rank; no border-lower-28 or exact unrestricted-32 claim is made.

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

These are the values of the general multidimensional-shadow theorem.  For `n=6`, the average-subset argument first improves the row from 23 to 26, the fixed-six product-shadow argument gives 27, and the common-quotient flag-hook exclusion gives the current best in-repository proof-draft lower bound 28. The frozen rational witnesses are certificates of the displayed general values; they are not claimed to be globally optimal.

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
python scripts/n6_b64_common_quotient_rigidity.py
python scripts/n6_near_extremal_fixed_six_layers.py
python scripts/n6_weight_refined_connecting_barrier.py
python scripts/n6_b64_frame_component_specialization.py
python scripts/n6_near_extremal_six_plane_frontier.py
python scripts/n6_b64_prolongation_exclusion.py
python scripts/n6_near_extremal_star_quotient_rigidity.py
python scripts/n6_near_extremal_prolongation_pruning.py
python scripts/n6_global_quotient_prolongation_caps.py
python scripts/n6_alpha1_prolongation_closure.py
python scripts/n6_alpha2_prolongation_exclusion.py
python scripts/n6_arbitrary_quotient_prolongation_barrier.py
python scripts/n6_b60_scalar_frontier.py
python scripts/n6_global_t15_prolongation_cap.py
python scripts/n6_alpha2_t15_prolongation_cap.py
python scripts/n6_alpha3_individual_prolongation_barrier.py
python scripts/n6_alpha3_row_column_coupling_exclusion.py
python scripts/n6_alpha3_common_quotient_counterexample.py
python scripts/n6_alpha3_coordinate_quotient_injectivity.py
python scripts/n6_pairing_parity_counterexample.py
python scripts/n6_b59_scalar_frontier.py
python scripts/n6_product_shadow_b53_64_exclusion.py
python scripts/n6_lower27_completion.py
python scripts/n6_lower28_fixed_six_partial.py
python scripts/n6_literal_six_shadow_b34_47_exclusion.py
python scripts/n6_alpha3_separated_block_exclusion.py
python scripts/n6_two_row_transverse_rigidity.py
python scripts/n6_coordinate_product_shadow_b50_equality.py
python scripts/n6_product_shadow_b50_equality_locus.py
python scripts/n6_grassmann_closure_barrier.py
python scripts/n6_common_rowslice_collision_exclusion.py
python scripts/n6_row_pure_multigrade_exclusion.py
python scripts/n6_k34_rank_nine_fano_exclusion.py
python scripts/n6_k34_special_d_fano_exclusion.py
python scripts/n6_colored_differential_barrier.py
python scripts/n6_squarefree_coproduct_colored_barrier.py
python scripts/n6_hook_plane_projection_barrier.py
python scripts/n6_central_neardirect_quadratic_barrier.py
```

The bound generators use only the Python standard library and exact integer/rational arithmetic. The asymptotic diagnostic evaluates exact finite certificates with `Fraction`; decimal constants are display-only checks of the proved formulas. The coordinate tangent audit uses a finite-field rank only in the valid direction: a rank-381 certificate modulo `1,000,003`, together with 19 explicit characteristic-zero tangent directions, proves exact affine tangent dimension 19 over `Q`.

The scalar derivative-profile theorem proves a structural ceiling rather than a numerical promotion. Even using all derivative degrees with arbitrary nonnegative weights cannot beat the central binomial coefficient. The raw adjacent differentiation-map kernel dimension is also determined by the profile. The general program therefore moves to coordinate-invariant natural maps, higher compatibility quotients, syzygies, and coupled relation modules.

The full column-sign theorem uses a Boolean diagonal coefficient slice. Every normalized column-sign term becomes one Walsh character determined by its diagonal signs, while the permanent becomes a delta function. Walsh inversion forces all `2^(n-1)` signature aggregates to be nonzero, and Glynn supplies the matching upper bound. For `n=6`, this closes the entire `2^30` normalized column-sign family at 32 terms without enumerating it. Arbitrary complex row-homogeneous and unrestricted Chow terms remain outside the theorem.

The universal single-term theorem first degenerates the at-most-six-dimensional factor span to a coordinate subspace while keeping the relevant quadratic intersection at fixed dimension. The coordinate audit then supplies the only local cases: no rectangle, one rectangle, or a `K_2,3` / `K_3,2` rectangle space. The last case is eliminated by regenerated integer minors of determinant `-1` in orders 18 and 45.

The fixed-four projection and Bukh argument first gives the raw range `20<=b<=27` and 36 states. Equality at `b=27` forces a common 12-dimensional quadratic quotient, a direct quadratic sum of dimension 60, and coupled middle-catalectic rank 80, contradicting the residual upper bound 34. Low-relation arguments exclude the next two layers, and componentwise scalar Macaulay growth closes the historical 23-term frontier, proving lower 24.

The lower-25 proof does not mechanically reuse that state table. Under a hypothetical 24-term decomposition it fixes six terms and leaves eighteen. Projection and Bukh compression give `40<=b<=64`; the layers `b=40,41` are already Koszul-strict. For every remaining layer, the full colored quadratic relation module has dimension at most 16. The vector-valued Macaulay theorem bounds its cubic relation module by `k^{<2>}`, and a block-Sylvester inequality converts that cap into a coupled middle-catalectic lower bound. Exact defect arithmetic gives a positive margin in every layer; the smallest margin is two at `b=43,44`. A second implementation independently scans all `16^6=16,777,216` labelled defect tuples.

The lower-26 fixed-count diagnostic tests `q=6,7,8` under a hypothetical 25-term decomposition and leaves hundreds of states when the fixed subset is arbitrary. N6-030 supplies the missing selection step. If `U_i` are the individual middle-catalectic images, condition on a term of maximum central rank and apply submodular averaging to the other five choices. The relation-pairing identity then selects six indices with coupled central rank at least 87. The nineteen-term residual forces central intersection `b>=54`. Exact rational Bukh-shadow endpoints and an integer enumeration of at most 33 symmetric defect profiles per terminal layer prove the universal fixed-six cap `b<=53`. This contradiction proves the ordinary lower bound 26. The argument does not prove border rank 26 or exact unrestricted rank 32.

For the lower-27 program, the single-term central rank 19 is excluded. In factor-span dimension four, a dependent four-set produces two independent cubic apolar operators; divisibility and multidegree then factor the 20 by 20 determinant as a nonzero constant times the squared product of all four-factor brackets. The five-dimensional dependence normal forms have exact ranks `14,14,18,20,20`. Thus the surviving maximum-single-term-rank frontier is forced to rank 20; this is one input to the later fixed-six completion.

The next reduction selects six terms from any hypothetical 26-term decomposition and forces the twenty-term residual to have middle-catalectic rank at least 384. Hence every `s`-term sub-sum of that residual has middle rank at least `20s-16`, strictly certifying Chow rank `s`; every central relation-pairing radical is at most nine and at least twelve residual summands have individual middle rank 20. Its middle image intersects the permanent middle space in dimension `336..380`, and its colored relation space modulo the permanent has dimension at least 320. Several direct cross-degree approaches stop at this point, but the later product-shadow theorem bypasses that obstruction.

The lower-27 completion works inside the fixed-six cubic intersection `S=E_3 intersect H_3`.  Row-column torus specialization sends any `b`-plane `S` to a coordinate support without increasing its derivative shadow.  Successive colex compression in the row- and column-triple factors produces a Ferrers diagram, whose shadow is the exact integer potential `sum_i w_i k(lambda_i)`.  A 2,309-state dynamic program proves that this shadow exceeds the projection cap 78 for every `53<=b<=64`.  For `45<=b<=52`, the remaining defect budget is only 6, 3, or 0.  Exhausting every conservative six-term quadratic-defect profile and applying vector-valued Macaulay growth plus block-Sylvester gives `h` lower bounds `98,98,112,112,112,112,120,120`, all strictly larger than the twenty-term residual necessity `h<=2b`.  This rules out 26 terms and proves the ordinary interval `27..32`; it makes no border-rank or exact-rank-32 claim.

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
