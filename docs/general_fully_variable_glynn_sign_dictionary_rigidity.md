# Correction: fully variable quartic Glynn sign dictionary

## Status and claim boundary

`CORRECTED_PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FOUR_DIRECTION_CLASSIFICATION`, `PARTIAL_ROUTE_BARRIER`.

This note supersedes theorem identifier
`G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1`.  The previous claim that the
full 336-atom sign dictionary has exact threshold seven was based on an
incorrect projected-support minimum.  The exact diagonal projection minimum is
four, not six.

The corrected result is:

\[
\boxed{
\begin{array}{c}
\text{the diagonal projection has exactly sixteen minimal four-direction states;}\\
\text{all 186,624 full-tensor lifts of those states fail.}
\end{array}}
\]

Five atoms are impossible by the inherited unrestricted five-block zero
theorem.  Six sign atoms remain open.  Therefore the exact threshold of the
full sign dictionary is currently

\[
\boxed{6\le q_{\rm sign}^{\rm full}\le7},
\]

not a proved equality.

The global quartic frontier remains

\[
\boxed{6\le\mu(6,4)\le7}.
\]

## 1. Dictionary

Let

\[
\Delta=\{v\in\{\pm1\}^4:v_1=1\}.
\]

For distinct signs `v,u` and a two-column shared set `J`, define

\[
C_{v,u,J}
=\bigotimes_{j\in J}v
 \otimes
 \left(
   \bigotimes_{k\notin J}v-
   \bigotimes_{k\notin J}u
 \right).
\]

There are

\[
8\cdot7\cdot\binom42=336
\]

atoms.  Every atom belongs to one degree-six Chow derivative block.

## 2. Corrected diagonal projection

Evaluate all four column slots at the same anchored sign.  Column splits are
forgotten, and the 336 atoms collapse to 40 directions:

- eight same-parity directions `L_v=32e_v`;
- 32 opposite-parity directions `C_(v,u)`.

The normalized target is `3 epsilon`, where `epsilon(v)=chi(v)`.

An exact scan over the Mersenne prime

\[
p=2^{61}-1
\]

checks

\[
\sum_{j=1}^{4}\binom{40}{j}=102,090
\]

supports.  The Hadamard bound is far below `p`, so the rank result is a
characteristic-zero certificate.

There are no one-, two-, or three-direction representations.  There are
exactly sixteen minimal four-direction supports.  For each opposite-parity pair
`(e,o)`, the support is

\[
\boxed{\{L_e,L_o,C_{e,o},C_{o,e}\}}.
\]

The coefficients are unique:

\[
\boxed{
\frac32L_e-\frac32L_o-\frac32C_{e,o}+\frac32C_{o,e}=3\epsilon.
}
\]

This identity is precisely the state that the previous six-star-only scan
missed.

## 3. Restore all atom labels and column splits

A same-parity direction `L_e` has 18 actual lifts: three possible same-parity
bases and six column splits.  An opposite-parity direction `C_(e,o)` has six
lifts, one for each split.  Thus each projected state has

\[
18^2\cdot6^2=11,664
\]

full-tensor assignments, and all sixteen states give

\[
16\cdot11,664=186,624.
\]

After clearing denominators, every possible identity has the form

\[
3A_{L_e}-3A_{L_o}-3A_{C_{e,o}}+3A_{C_{o,e}}
=2\operatorname{perm}_4.
\]

Every assignment is checked on all 256 row-index coefficients over the
integers.  The exact solution count is zero.

Therefore

\[
\boxed{\text{the sixteen four-direction projected states do not lift.}}
\]

## 4. What remains open

The diagonal projection also contains representations supported on five and
six distinct directions.  They were omitted from the superseded packet because
that packet stopped at the first incorrectly assumed six-direction minimum.
This correction does not classify those states and does not exclude a genuine
six-atom identity in the 336-atom dictionary.

The valid boundary is:

```text
four-atom sign representation = ZERO
five-atom representation = ZERO by inherited five-block theorem
six-atom fully variable sign representation = OPEN
seven-atom sign representation = EXPLICIT
full sign-dictionary threshold = OPEN IN [6,7]
```

The next finite task is to classify the projected five- and six-direction
states, preferably through the quotient matroid of the 168 mixed tensors rather
than another unsupported candidate restriction.

## 5. Deterministic replay

```bash
python scripts/general_fully_variable_glynn_sign_dictionary_rigidity.py \
  --json /tmp/general_fully_variable_glynn_sign_dictionary_rigidity.json
python -O scripts/general_fully_variable_glynn_sign_dictionary_rigidity.py
python scripts/general_fully_variable_glynn_sign_dictionary_rigidity_independent.py

g++ -O3 -std=c++20 \
  scripts/general_fully_variable_glynn_sign_dictionary_projection_scan.cpp \
  -o /tmp/full_sign_projection_correction
/tmp/full_sign_projection_correction /tmp/full_sign_projection_correction.json
```

Frozen corrected core:

```text
7e838f0507771694d3ecf4598cfd90851eada69be0f26c476abc694f65b83c42
```

## Strict boundary

```text
superseded threshold-seven theorem = RETRACTED
corrected diagonal minimum = 4
minimal four-direction states = 16
full lifts checked = 186,624
four-direction full solutions = 0
six-atom sign dictionary = OPEN
arbitrary six-block literal sum = OPEN
mu(6,4) = OPEN IN [6,7]
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
