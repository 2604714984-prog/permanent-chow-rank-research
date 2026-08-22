# Fully variable quartic Glynn sign-dictionary rigidity

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_CLASSIFICATION`, `STRICT_SIGN_DICTIONARY_ROUTE_THEOREM`.

Let

\[
\Delta=\{v\in\{\pm1\}^4:v_1=1\},
\qquad \chi(v)=\prod_{r=1}^4v_r.
\]

For an ordered pair `v != u` and a two-column shared set
`J subset {1,2,3,4}`, define the quartic atom

\[
C_{v,u,J}
=\bigotimes_{j\in J}v
 \otimes
 \left(
   \bigotimes_{k\notin J}v-
   \bigotimes_{k\notin J}u
 \right),
\tag{0.1}
\]

with the tensor factors restored to their original column positions. Each atom
belongs to the fourth derivative space of a degree-six Chow term. There are

\[
8\cdot7\cdot\binom42=336
\]

such atoms.

The theorem proved here is

\[
\boxed{
\operatorname{perm}_4
\text{ requires at least seven atoms from the full 336-atom dictionary.}
}
\tag{0.2}
\]

The inherited one-term Glynn compression uses seven atoms, so the threshold in
this full sign dictionary is exactly seven. Both the deleted base and the
shared/tail column split may vary independently from atom to atom.

This is not a six-block zero theorem for arbitrary degree-six Chow derivative
blocks. It leaves genuinely non-sign mixed frames, singular paths, and remote
six-block configurations open. Thus

\[
\boxed{6\le\mu(6,4)\le7}
\]

remains the unrestricted boundary.

## 1. Eight-point diagonal evaluation

For `a in Delta`, evaluate all four column slots on `a`. The result is
independent of `J`:

\[
\mathcal E(C_{v,u,J})(a)
=(a\cdot v)^2\big((a\cdot v)^2-(a\cdot u)^2\big).
\tag{1.1}
\]

Identify `Delta` with the three-cube and let `e_v` be the coordinate function
at `v`. Put `epsilon(v)=chi(v)`. Since

\[
(a\cdot v)^2
=16e_v(a)+2-2\epsilon(v)\epsilon(a),
\tag{1.2}
\]

one obtains the exact formulas

\[
\frac18\mathcal E(C_{v,u,J})=
\begin{cases}
32e_v,&\epsilon(u)=\epsilon(v),\\[2mm]
24e_v-8e_u+\mathbf1-\epsilon(v)\epsilon,&
\epsilon(u)=-\epsilon(v).
\end{cases}
\tag{1.3}
\]

The target satisfies

\[
\frac18\mathcal E(\operatorname{perm}_4)=3\epsilon.
\tag{1.4}
\]

Thus the 336 atoms collapse to 40 distinct evaluation directions:

- eight same-parity coordinate directions; and
- 32 directed opposite-parity directions.

No information about the column split is used at this stage. The evaluation is
only a necessary projection, so every projected survivor is checked later in
the complete 256-coordinate tensor space.

## 2. Exact projected six-support classification

The 40 directions and the target were scanned through support size six. The
number of tested supports is

\[
\sum_{j=1}^{6}\binom{40}{j}=4,598,478.
\tag{2.1}
\]

The rank scan is performed modulo the Mersenne prime

\[
p=2^{61}-1=2,305,843,009,213,693,951.
\]

After the normalization in (1.3), all entries have absolute value at most 32.
Every relevant matrix has at most seven columns, and Hadamard's bound gives

\[
|\det|\le(32\sqrt7)^7<3.2\cdot10^{13}<p.
\tag{2.2}
\]

Therefore a nonzero characteristic-zero minor cannot disappear modulo `p`,
and the finite-field rank classification is also an exact rational
classification.

There is no projected representation using five or fewer directions. Exactly
16 support-minimal six-direction representations remain. Write

\[
\Delta=E\sqcup O,
\qquad
E=\{v:\chi(v)=1\},
\qquad
O=\{v:\chi(v)=-1\}.
\]

For every pair `(e,o) in E x O`, the unique support is

\[
\boxed{
\{C_{v,o}:v\in E\setminus\{e\}\}
\cup
\{C_{w,e}:w\in O\setminus\{o\}\}.
}
\tag{2.3}
\]

All 16 supports are independent in the evaluation space, so their coefficients
are uniquely fixed:

\[
\boxed{
\frac16\sum_{v\in E\setminus\{e\}}C_{v,o}
-
\frac16\sum_{w\in O\setminus\{o\}}C_{w,e}.
}
\tag{2.4}
\]

Here the split labels have been suppressed because evaluation forgets them.
The support is a pair of directed three-stars: every retained even sign points
to the omitted odd sign, and every retained odd sign points to the omitted
even sign. Same-parity directions and all other directed patterns are excluded
already by the eight-point projection.

The same classification can also be read from the two tetrahedral zero-sum
spaces on `E` and `O`: the four centered coordinate vectors in either parity
class have one relation, with all four coefficients equal. Coupling the source
spikes and opposite-parity defects leaves only the two three-stars in (2.3).
The complete support scan is retained as an exact independent certificate of
that elementary reduction.

## 3. Restore all column splits

For a projected survivor `(e,o)`, each of its six atoms may independently
choose any of the six two-column shared sets. The only possible full tensor
identity is therefore

\[
\sum_{v\in E\setminus\{e\}} C_{v,o,J_v}
-
\sum_{w\in O\setminus\{o\}} C_{w,e,J_w}
=6\operatorname{perm}_4.
\tag{3.1}
\]

There are exactly

\[
16\cdot6^6=746,496
\tag{3.2}
\]

assignments. Every assignment is checked on all `4^4=256` row-index
coefficients over the integers. The scan finds

\[
\boxed{0\text{ exact solutions}.}
\tag{3.3}
\]

The primary replay uses a `3+3` meet-in-the-middle split. For each omitted pair,
all 216 positive-star sums are hashed after subtracting `6 perm_4`, then all 216
negative-star sums are queried. This is an exact reorganization of all 46,656
assignments for that pair, not a heuristic pruning. The independent replay
reconstructs the atom coefficients directly from XOR characters rather than
from products of stored sign vectors.

## 4. Consequence

The evaluation classification is necessary for any six-atom identity, and
Section 3 exhausts every way to lift its 16 survivors back to the full tensor.
Hence no six atoms in the fully variable sign dictionary represent
`perm_4`. Since the one-term Glynn compression gives seven atoms,

\[
\boxed{
\text{fully variable quartic Glynn sign-dictionary threshold}=7.
}
\tag{4.1}
\]

This closes all compression attempts that retain sign linear forms while
allowing both of the following to vary atom by atom:

1. the deleted/base sign; and
2. the shared/tail two-column split.

A six-block witness, if one exists, must leave this 336-atom sign dictionary and
use genuinely mixed factor frames or ambient common-source cancellation.

## 5. Deterministic replay

```bash
python scripts/general_fully_variable_glynn_sign_dictionary_rigidity.py \
  --json /tmp/general_fully_variable_glynn_sign_dictionary_rigidity.json

python -O scripts/general_fully_variable_glynn_sign_dictionary_rigidity.py

python scripts/general_fully_variable_glynn_sign_dictionary_rigidity_independent.py

g++ -O3 -std=c++20 \
  scripts/general_fully_variable_glynn_sign_dictionary_projection_scan.cpp \
  -o /tmp/full_sign_projection_scan
/tmp/full_sign_projection_scan /tmp/full_sign_projection_scan.json
```

Expected markers:

```text
GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_RIGIDITY_PASS
GENERAL_FULLY_VARIABLE_GLYNN_SIGN_DICTIONARY_RIGIDITY_INDEPENDENT_PASS
```

Theorem identifier:

```text
G-FULLY-VARIABLE-SIGN-DICTIONARY-RIGIDITY-v1
```

## Strict boundary

```text
fully variable 336-atom quartic sign threshold = 7
six-atom sign-dictionary representation = ZERO
seven-atom sign-dictionary representation = EXPLICIT
arbitrary six-block literal sum = OPEN
mu(6,4) = OPEN IN [6,7]
non-sign mixed frames = OPEN
singular / Puiseux / remote six-block paths = OPEN
unrestricted Chow-rank improvement = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
