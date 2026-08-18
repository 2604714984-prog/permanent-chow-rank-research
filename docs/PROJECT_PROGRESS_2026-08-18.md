# Permanent Chow-rank research progress — 2026-08-18

## Purpose and evidence boundary

This document is a compact project snapshot. It consolidates the currently
accessible mathematical boundaries, the active pull-request stack, the result
from the immediately preceding research session, and the current integration
status. It does not replace `RESEARCH_LEDGER.md` or `STATUS.md`.

The repository must continue to distinguish:

- merged or accepted baseline results;
- open stacked proof drafts;
- restricted-family theorems and route ceilings;
- numerical lower bounds versus exact ranks;
- mathematical proof status versus repository-integration status.

No route ceiling below is an upper bound on actual Chow rank unless explicitly
stated.

## 1. Accepted small-order baseline

The current small-order theorem chain is

```text
ChowRank(perm_3) = 4
ChowRank(perm_4) = 8
ChowRank(perm_5) = 16
```

The `n=3` proof is linear algebra. The `n=4` proof uses the first Koszul
flattening, low-rank quadratic classification, the exact `psi_v` chart, and
the double-quotient inequality. The repaired `n=5` proof preserves the
coupled-catalectic firewall and uses exact finite certificates. The clean
`n=5` review boundary was merged in PR #30.

## 2. Current accessible numerical frontiers

The current accessible repository boundaries are:

| Object | Boundary | Status |
|---|---:|---|
| `perm_3` | `4` | accepted baseline |
| `perm_4` | `8` | accepted baseline |
| `perm_5` | `16` | repaired computer-assisted proof boundary |
| `perm_6` | `28..32` | lower 29 remains open in PR #31 |
| `perm_7` | `49..64` | stacked scalar-tower draft, PR #51 |
| `perm_8` | `90..128` | stacked scalar-tower draft, PR #51 |
| `perm_9` | `164..256` | stacked scalar-tower draft, PR #51 |
| `perm_10` | `307..512` | stacked scalar-tower draft, PR #51 |

The accessible PR #31 does not prove unrestricted
`ChowRank(perm_6)=32`. It closes ordinary lower 28 and records a partial
lower-29 frontier. The sign-family theorem gives exact rank 32 only inside its
named restricted family.

The general upper bound remains Glynn's `2^(n-1)`-term Chow decomposition.

## 3. General-`n` progress by route

### 3.1 Exact derivative shadows and the scalar tower

The exact product-shadow work proves that minimum derivative shadows in
permanent derivative spaces reduce to Ferrers integer programs. Cross-degree
projection, recursive derivative capacities, direct saturation, the full
prefix envelope, and shadow-complement duality produce the stacked numerical
bounds through `n=10` above.

The same program also proves a route ceiling:

```text
complete exact scalar derivative tower
  = O(n^(1/4) * binom(n,floor(n/2)))
  = O(2^n / n^(1/4)).
```

Thus larger scalar shadow tables cannot by themselves prove general Glynn
optimality. A successful shadow continuation must add a uniform
Chow-realizability defect rather than another arbitrary-subspace capacity.

### 3.2 Restricted sign and slice results

The full normalized row-sign and column-sign families have exact rank
`2^(n-1)`. The affine-Segre analysis shows that the same Boolean slice has only
linear rank in the continuous anchored complex family. The exponential sign
proof is therefore a restricted-family theorem, not an unrestricted Chow-rank
proof.

### 3.3 Apolar, matrix-image, Fitting, and representation barriers

The current stack proves route ceilings or obstructions for:

- one- and two-direction homogeneous power profiles;
- fixed binary ideals and growing maximal-ideal powers;
- bounded common-degree and nonuniform shifted matrix-image ranks;
- raw Fitting and raw Betti profiles without the required subquotient
  monotonicity;
- one-direction Jordan and Fitting valuation profiles;
- unprojected standard Koszul--Young maps;
- fixed matching-projected linear postprocessing;
- exact-additive graded `K_0` scalarizations;
- full-orbit and stabilizer-efficient exact-additive isotype profiles.

These results sharply narrow the search space. They do not rule out nonlinear
multiplication-tensor invariants, minimal syzygy functors with a proved
monotone envelope, valuative flat-sum data, or Chow-realizability defects.

### 3.4 Apolar multiplication-tensor route

PR #68 opens a legal nonlinear route. It proves that each Chow-term apolar
algebra is controlled by a Boolean algebra subquotient, and that the permanent
apolar algebra is the diagonal Segre product of two Boolean algebras. The
current ordinary and border multiplication-tensor baselines do not improve
the existing Chow-rank bounds. Smoothability, border-rank excess, homogeneous
multiplication slices, and stronger asymptotic tensor functionals remain open.

## 4. Result from the immediately preceding research session

PR #70 records the latest theorem:

```text
PR #70
branch: research/closed-factor-span-endpoint-zero-blocks
exact head: de735d516c683f66a3cb5c86860f0a64d5fdac84
frozen theorem core:
7d78c0e595d25130a9bf2f9dd843ef88f3be737004f33b3f85f3be1170eb376a
```

Let

```text
E_m = D_m(perm_n)
F_i = D_m(T_i)
L_i = factor span of T_i.
```

If

```text
m >= 3,
q >= 2,
L_1 + ... + L_q is a direct sum,
sum_i dim L_i <= m^2,
```

then

```text
E_m intersect (F_1 + ... + F_q) = 0.
```

The proof combines the permanent derivative shadow lower bound with
minimal-shadow direct-sum indecomposability. A nonzero intersection element
would have essential dimension exactly `m^2` and would be forced to split
nontrivially across the direct factor spaces, contradicting the scalar-center
theorem.

Consequently the strict term-count endpoint is closed:

```text
q*n = m^2,
m >= 3,
q >= 2

=>
E_m intersect sum_i D_m(T_i) = 0.
```

The guaranteed zero-block size is

```text
zeta(n,m)
 = floor((m^2-1)/n)
   + indicator(m>=3, n divides m^2, m^2/n>=2).
```

The hypotheses are sharp: the theorem fails for `q=1` at `n=m^2`, and for
`m=2` via `perm_2` itself.

This is a genuine general-`n` Chow-realizability result. It adds no new best
numerical Chow-rank lower bound. The next mathematical interface is the
near-endpoint regime

```text
q*n = m^2 + s,
```

with small positive `s`, where a quantitative intersection defect is needed.

## 5. Current integration status

PR #70 is mathematically organized as a complete proof draft with deterministic
finite replays, but its current full inherited GitHub Actions run is failing.
The failure is an integration regression, not a demonstrated counterexample
to the PR #70 theorem.

Observed failures in run `32098702656`:

1. four inherited modules call `ExactProductShadow.transition(threshold)`, but
   the current canonical exact-shadow class exposes `minimum()` and a
   standalone transition search rather than that compatibility method;
2. one principal-ideal regression test expects the word `central` in a theorem
   string although the theorem records the equivalent explicit expression
   `binom(n,floor(n/2))`.

Until those compatibility issues are repaired and the full suite is rerun:

```text
PR70 mathematical status = proof draft complete
PR70 focused evidence status = replayed
PR70 full integration status = failing
PR70 merge readiness = false
```

## 6. Immediate integration actions

The next repository-maintenance PR should remain narrow and should:

1. restore the legacy `ExactProductShadow.transition(threshold)` compatibility
   wrapper by delegating to the existing exact binary-search logic;
2. replace the brittle wording assertion with a mathematical formula check;
3. rerun the complete inherited suite under normal and optimized Python modes;
4. record the exact-head workflow receipt;
5. consolidate `RESEARCH_LEDGER.md` through PR #70 after the stacked branch is
   green.

These changes must not alter frozen theorem values or relabel an open stacked
result as canonical.

## 7. Research priorities after integration

Priority order:

1. **Near-endpoint Chow-realizability defect.** Quantify the intersection when
   `q*n=m^2+s` with small `s`.
2. **Apolar multiplication tensor.** Seek a permanent-specific rank or border
   rank excess over the Boolean denominator.
3. **Valuative flat-sum data.** Control leading relation packets that are
   invisible in literal termwise limits.
4. **Minimal relation or syzygy functors.** Promote only after proving the
   necessary additivity and subquotient monotonicity.
5. **Lower-29 `perm_6` frontier.** Retain as a regression test, not the primary
   general-`n` objective.

## 8. Strict claim boundary

```text
perm_3 exact = 4
perm_4 exact = 8
perm_5 exact = 16
perm_6 exact = open
perm_n exact for n>=6 = open
general Glynn optimality = open
PR70 introduces a general realizability theorem, not a new numerical bound
PR70 full repository CI = currently failing
```
