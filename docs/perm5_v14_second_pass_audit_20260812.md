# Second-pass audit of the repaired `perm_5` lower-16 proof

Date: 2026-08-12

Audited PR: #29, `Repair perm5 lower-16 mathematical audit gaps`

Audited head: `649ab071eeef40a32bdfefc9a831d210cb072839`

## Verdict

```text
FATAL_LOGICAL_DEFECT_FOUND=false
LOWER_16_PROOF_CHAIN=PASS_ON_SECOND_PASS
EXACT_COMPUTATION_REPLAY=PASS
PROGRAM_FREE_CHARACTERIZATION=REJECT
FRESH_INDEPENDENT_HUMAN_REVIEW=PENDING
```

This audit found no new mathematical counterexample or missing implication in
the repaired lower-16 chain.  At the audited head, the packet supports

\[
\operatorname{ChowRank}(\operatorname{perm}_5)=16
\]

as a computer-assisted characteristic-zero theorem candidate with exact finite
certificates.  It must not be described as a completely program-free proof:
the completeness of the one-intersection endpoint classification, the
`s=19,d=9` equality count, and several shifted/orbit classifications is carried
by reproducible exact enumeration.

This is a second internal adversarial audit, not a substitute for fresh
independent human review or proof-assistant formalization.

## Frozen artifacts

| Artifact | SHA-256 |
| --- | --- |
| `perm345_chow_rank_v14_repaired_zh_ams.pdf` | `960402FCB7BF16B51FC7C1FB4E641C5E982583A15EF1F38A9F5E6E866F94A7C8` |
| `perm345_reviewer_submission_v14_repaired_20260812.zip` | `CE8F639C532B754B4E0A8EEC959D97E461426C9F9402B923D6A13056F46DFF33` |

The reviewer ZIP contains 110 manifest-controlled files.  Manifest verification
passed before and after every replay performed in a fresh temporary copy.

## Proof-chain audit

### 1. Entry and finite state space

The base Koszul argument excludes fewer than ten terms.  The padding lemma then
turns every hypothetical decomposition of length at most fifteen into a
fixed-six decomposition plus a nine-term remainder without importing the old
lower-15 SAT/DRAT archive.

The fixed-six inequalities leave exactly 58 states.  The eight routes form the
disjoint exhaustive partition

\[
38+1+1+9+2+1+1+5=58.
\]

The use of the near-maximal coupling lemma is confined to the states with
`h >= 57`; it is not silently applied to the exceptional `h=54` state.

### 2. The `d=9` routes

For `(s,d,t,h)=(19,9,45,54)`, independent exact replay reconstructed all 800
coordinate equality flags, 100 ordinary and 35 mixed prolongation weights, and
the uniform bound

\[
\dim (T+X)^{(1)}\le 44<54.
\]

The calculation is exhaustive integer set combinatorics, not random sampling.
The written argument correctly uses torus degeneration and upper
semicontinuity; the finite table is nevertheless a computation premise and
should be labelled as such.

For `(22,9,48,57)`, the repaired universal one-intersection theorem now gives a
stronger and cleaner exclusion: every ten-plane containing the nine-dimensional
quotient image has prolongation at most 26, contradicting the required value at
least 35.

### 3. The `d=11,12` routes

The no-crossing formula, simultaneous compression, triangle envelope, and
crossing marginal inequalities were checked for direction and scope.  The exact
integer diagnostics independently reproduce

\[
p_{11}\le55,\qquad p_{12}\le61.
\]

The five annihilator states are then excluded by the strict comparisons

\[
43>42,\qquad 49>48,\qquad 48>42.
\]

No field-dependent numerical rank is used in these finite graph bounds.

### 4. Universal one-intersection flag theorem

The repaired projective incidence argument preserves the nine-dimensional
quotient image at the torus-fixed endpoint and includes the arbitrary tenth
quotient direction.  Upper semicontinuity is used in the correct direction.

The standalone endpoint certificate rebuilt the integral divided-power
matrices and checked

\[
864864+21600=886464
\]

flags exactly.  The maximum is 26.  Reduction modulo 3 is used only through
the valid inequality `rank_F3 <= rank_Q`, so the finite calculation proves the
required characteristic-zero kernel upper bound.

### 5. The nine `d=10` states

The shifted stability and inverse-compression diagnostics reproduce the 14
remaining nonuniform family states and the three terminal orbits `0`, `1`, and
`13`.  The independent witness-forest implementation does not import the
original generator.

- **Orbit 1.**  Exhaustive comparison of all `2^15=32768` subsets and all 3003
  ten-weight subsets gives maximum 36 with exactly four maximizers.  The three
  `W_b` branches have local fibre `QQ[B]/(B^2)` of length two.  The fourth
  `W_M` branch is excluded by the same-row valuative assignment argument; its
  small rational rank lemmas replay at ranks 24 and 25.
- **Orbit 13.**  The structural crossing bound gives at most 36, below the
  required 39.  The exact rational diagnostic finds the sharper maximum 26.
- **Orbit 0.**  The full-flag tangent graph has kernel dimension eight over
  every field.  Column rigidity, Boolean Fourier shortening, and the first
  Koszul map give
  \[
  2215>9\cdot245=2205,
  \]
  excluding the nine-term remainder.

### 6. Completion

All 58 states are excluded, hence the repaired chain proves the lower bound 16.
Glynn's 16-term identity supplies the matching upper bound.

## Independent replay summary

The following high-risk finite components were replayed from the extracted
reviewer packet with bytecode generation disabled:

- package manifest before and after replay: 110 files, pass;
- `s=19,d=9`: 800 flags, 135 weights, prolongation bound 44, pass;
- one-intersection endpoints: 886,464 flags, maximum 26, pass;
- no-crossing and crossing integer bounds for `p_9,p_11,p_12`, pass;
- shifted stability, inverse shift, and independent witness forests, pass;
- orbit-1 terminal formula, length-two fibre, and `W_M` small lemmas, pass;
- orbit-13 structural bound, pass;
- orbit-0 tangent graph and Fourier/Koszul bounds, pass.

No GPU approximation, floating-point rank, random diagnostic, historical 10 GB
archive, or unpublished data is needed for these checks.

## Requested external-review focus

Fresh reviewers should concentrate on the non-finite bridges rather than merely
rerunning the scripts:

1. closedness and quotient-rank preservation in the one-intersection incidence;
2. the fixed-six padding lemma and the 58-state logical firewall;
3. the relative Grassmannian argument in the `d=11,12` annihilator route;
4. formal column rigidity and the passage from the orbit-0 tangent calculation
   to the completed local ring;
5. the Boolean shortening/prolongation argument leading to `2215 > 2205`;
6. whether every finite table used for completeness is labelled as an exact
   computation premise rather than as a program-free derivation.

Until that review is complete, the appropriate repository status is
`REPAIRED_INTERNAL_DRAFT_FRESH_EXTERNAL_REVIEW_PENDING`.
