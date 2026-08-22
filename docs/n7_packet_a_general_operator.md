# General Packet-A factor-plane operator foundation

## Status

`A-01/A-02 FOUNDATION EXECUTED; A-03--A-05 AND THE EQUALITY LOCUS REMAIN OPEN.`

This package implements the first bounded basis-level segment missing from
the labelled `2/5/6` smoke.  It accepts seven arbitrary nonzero linear factors
in a common ambient coordinate space and constructs the labelled maps

\[
 A_d:\bigoplus_{i,I,\ |I|=d} k e_{i,I}\longrightarrow
 \operatorname{Sym}^d(V),
 \qquad e_{i,I}\longmapsto\prod_{j\in I}\ell_{i,j},
 \quad d=2,5,6.
\]

All coefficient matrices, ranks, explicit right-kernel bases, the kernel-image defect, and the
degree-six target quotient operator in the executed control are exact over
`QQ`.  The complementary relation pairing is deliberately a separate
finite-field diagnostic over `F_65521`.

## Complementary labels and external coefficients

The permutation `P_(2<-5)` sends a degree-five label to the degree-two label
of its complementary factor subset, preserving the term label.  For
`sum_i c_i T_i`, the input map associated with the complementary degree is

\[
 C=\operatorname{diag}(c_i)P_{2\leftarrow5}A_5^{\mathsf T}.
\]

Consequently the relation pairing on the two aggregate kernels is

\[
 K_2^{\mathsf T}\operatorname{diag}(c_i)^{-1}
 P_{2\leftarrow5}K_5.
\]

The script constructs both directions explicitly.  The kernel-image defect
is computed over `QQ` from ranks of `A_2`, `C`, and `A_2C`; the displayed
restricted relation-pairing rank is computed only over the stated prime and
is not silently promoted to characteristic zero.

An actual factor-rescaling control makes the coefficient direction visible.
The second of two coordinate terms has its first factor scaled by two, and
the external coefficients are `(2,-1)`.  The exact `QQ` kernel-image defect
is zero.  Over `F_65521`, the inverse-coefficient restricted pairing has rank
zero while the erroneous direct-coefficient pairing has rank 21.

## Target quotient operator

For a supplied degree-six target matrix `T_6`, a row basis of
`ker(A_6^T)` gives an exact quotient operator `Q_6`.  Thus

\[
 Q_6T_6=0\quad\Longleftrightarrow\quad
 \operatorname{im}T_6\subseteq\operatorname{im}A_6.
\]

The frozen control uses two targets: one labelled degree-six column already
in the aggregate image, and the pure power `x_0^6`, which is outside it.  The
target quotient rank is exactly one over `QQ`.  These are interface controls,
not the 49 permanent sixth derivatives.

## Resource preflight and boundary

The executed example has two terms in ambient dimension seven.  Its largest
dense matrix has shape `462 x 42`, or 19,404 entries; the degree-six map has
shape `924 x 14`.  The conservative peak budget is 64 MiB.  Before
construction, the script also records the shapes that 49 terms would have,
but does not materialize them.  No subset search or unbounded collection
occurs.

The general-factor control uses an invertible sheared factor matrix and has
exact ranks `21,21,7`.  The incidence control uses two identical coordinate
factor planes with external coefficients `2,3`; it is designed to have a
nonzero kernel-image defect.  It is not a Packet-A equality candidate.

This closes only the A-01/A-02 operator foundation.  The permanent target,
the complete 49-term incidence equations, A-03 through A-05, `A-CLOSED`,
ordinary lower 50, and border rank remain unresolved.

Replay:

```text
python scripts/n7_packet_a_general_operator.py \
  --verify-json data/n7_packet_a_general_operator.json
python -m unittest tests.test_n7_packet_a_general_operator -v
```
