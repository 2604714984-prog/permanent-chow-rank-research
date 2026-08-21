# One-term Glynn compression and the seven-block quartic witness

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_COMBINATORIAL_REPLAYED`, `EXPLICIT_NONZERO_FAMILY`.

Let `mu(n,m)` be the least number of degree-`n` Chow derivative blocks whose
literal output-degree-`m` sum has nonzero intersection with
`D_m(perm_n)`. This note proves

\[
\boxed{
 n\ge m+2\quad\Longrightarrow\quad
 \mu(n,m)\le 2^{m-1}-1
}
\tag{0.1}
\]

for every `m>=3` over a characteristic-zero field.

At `(n,m)=(6,4)` this gives an explicit seven-block witness. Combined with the
inherited five-block zero theorem,

\[
\boxed{6\le\mu(6,4)\le7.}
\tag{0.2}
\]

Thus seven blocks are now known nonzero; six blocks remain open. This does not
change the unrestricted ordinary Chow-rank interval for `perm_6`, gives no
border-rank improvement, and makes no literature-novelty claim.

## 1. Glynn notation

For

\[
\Delta_m=\{\delta\in\{\pm1\}^m:\delta_1=1\},
\qquad
\chi(\delta)=\prod_{r=1}^m\delta_r,
\]

write

\[
L_{\delta,j}=\sum_{r=1}^m\delta_r x_{rj}.
\]

Glynn's identity is

\[
\operatorname{perm}_m
=
2^{1-m}
\sum_{\delta\in\Delta_m}
\chi(\delta)
\prod_{j=1}^m L_{\delta,j}.
\tag{1.1}
\]

Fix one sign vector `delta^0` in `Delta_m`. Split the columns into

\[
J=\{1,\dots,m-2\},
\qquad
\{a,b\}=\{m-1,m\},
\]

and set

\[
A_\delta=\prod_{j\in J}L_{\delta,j},
\qquad
B_\delta=L_{\delta,a}L_{\delta,b}.
\]

## 2. The missing Walsh character

### Lemma 2.1

\[
\boxed{
\sum_{\delta\in\Delta_m}\chi(\delta)A_\delta=0.
}
\tag{2.1}
\]

### Proof

Take one coefficient of the left side. It is indexed by a choice of one row in
each of the `m-2` columns of `J`, and equals

\[
\sum_{\delta\in\Delta_m}
\chi(\delta)
\prod_{j\in J}\delta_{r_j}.
\]

After fixing `delta_1=1`, the character `chi` is the full character in the
`m-1` free signs. The second factor contains at most `m-2` free signs with odd
multiplicity, so it cannot equal the full character. Walsh orthogonality makes
the sum zero. This remains true when row indices repeat. ∎

The relation is sharp at this tensor order: the order-`m-2` sign tensors have
rank `2^(m-1)-1`; the only missing Walsh character is the full character.

## 3. Remove one Glynn term

Multiply (2.1) by `B_(delta^0)` and subtract it from (1.1). The term
`delta=delta^0` vanishes, giving

\[
\boxed{
\operatorname{perm}_m
=
2^{1-m}
\sum_{\substack{\delta\in\Delta_m\\\delta\ne\delta^0}}
\chi(\delta)
A_\delta
\bigl(B_\delta-B_{\delta^0}\bigr).
}
\tag{3.1}
\]

There are exactly `2^(m-1)-1` summands.

For every retained sign vector define the degree-`m+2` Chow term

\[
T_\delta
=
A_\delta
L_{\delta,a}L_{\delta,b}
L_{\delta^0,a}L_{\delta^0,b}.
\tag{3.2}
\]

Its factors are linearly independent: the first `m-2` factors lie in distinct
column spaces, while each of the last two column spaces contains the two
independent forms belonging to `delta` and `delta^0`. Therefore both

\[
A_\delta B_\delta,
\qquad
A_\delta B_{\delta^0}
\]

are literal squarefree `m`-factor subproducts in `D_m(T_delta)`. Hence

\[
A_\delta(B_\delta-B_{\delta^0})\in D_m(T_\delta).
\tag{3.3}
\]

This proves (0.1) at `n=m+2`. Multiplying each `T_delta` by additional
independent factors and differentiating them away proves the same upper bound
for every `n>m+2`.

## 4. Exact quartic witness at degree six

Take `m=4`, choose `delta^0=(1,1,1,1)`, share columns 1 and 2, and use columns 3
and 4 for the two alternative tails. Formula (3.1) becomes

\[
\operatorname{perm}_4
=
\frac18
\sum_{\substack{\delta_1=1\\\delta\ne(1,1,1,1)}}
\chi(\delta)
L_{\delta,1}L_{\delta,2}
\left(
L_{\delta,3}L_{\delta,4}
-
L_{\delta^0,3}L_{\delta^0,4}
\right).
\tag{4.1}
\]

For each of the seven retained signs, the corresponding quartic lies in the
fourth derivative space of

\[
T_\delta=
L_{\delta,1}L_{\delta,2}
L_{\delta,3}L_{\delta,4}
L_{\delta^0,3}L_{\delta^0,4}.
\tag{4.2}
\]

A selected `4 x 4` subpermanent belongs to `D_4(perm_6)`, so (4.1) proves

\[
D_4(\operatorname{perm}_6)
\cap
\sum_{\delta\ne\delta^0}D_4(T_\delta)
e0.
\tag{4.3}
\]

Consequently seven arbitrary degree-six blocks are nonzero.

The same construction at `m=3,n=5` gives three blocks and recovers the known
cubic value `mu(5,3)=3` from a different uniform identity.

## 5. Sharpness inside the paired-column family

The quartic construction lies in the broader family

\[
\sum_{i=1}^q
 a_i(x_{\cdot,1})
 b_i(x_{\cdot,2})
 Q_i(x_{\cdot,3},x_{\cdot,4}),
\tag{5.1}
\]

where each `Q_i` is an arbitrary bilinear form. Seven terms are optimal even
in this enlarged family.

Group the permanent tensor as

\[
V_1\otimes V_2\otimes(V_3\otimes V_4).
\]

Contraction in the last factor has image

\[
S_0=\{A\in\operatorname{Mat}_{4\times4}:A^T=A,\ \operatorname{diag}A=0\},
\]

the six-dimensional space of symmetric zero-diagonal matrices. A
representation (5.1) implies

\[
S_0\subseteq\operatorname{span}\{a_i b_i^T:1\le i\le q\}.
\tag{5.2}
\]

If `q<=6`, dimension forces `q=6` and equality in (5.2), so every nonzero
rank-one matrix `a_i b_i^T` would lie in `S_0`. But `S_0` contains no nonzero
rank-one matrix: if `ab^T` has zero diagonal and is symmetric, choose an index
with `a_r!=0`; then `a_r b_r=0` gives `b_r=0`, and symmetry gives
`a_r b_s=a_s b_r=0` for every `s`, hence `b=0`.

Thus `q>=7`. The seven retained sign outer products span the
seven-dimensional space `S_0 plus kI`, so (4.1) attains this lower bound.
Therefore

\[
\boxed{\text{paired-column quartic threshold}=7.}
\tag{5.3}
\]

This restricted sharpness does not exclude a genuinely mixed six-block
witness.

## 6. Deterministic replay

The primary exact replay checks:

```text
compressed coefficient identity: m=3,4,5,6
row assignments checked:          27, 256, 3125, 46656
Walsh relation by parity masks:    m=3,...,10
quartic matching coefficients:     24 at value 8
quartic nonmatching coefficients:  232 at value 0
paired flattening rank:            6
seven sign outer-product rank:     7
factor count per envelope:        m+2
```

An independent bit-mask implementation reconstructs the complete quartic
tensor and verifies both ranks modulo `1,000,003` without importing the primary
implementation.

Frozen theorem core:

```text
045dcbd80846a35e6b9716771721c542ed86b0c1a246cf716cebb8e57df65a0e
```

## 7. Strict boundary

```text
five-block literal sum at (6,4) = ZERO
six-block literal sum at (6,4) = OPEN
seven-block literal sum at (6,4) = NONZERO
mu(6,4) = OPEN IN [6,7]
paired-column quartic threshold = 7
new unrestrcted Chow-rank bound = false
border-rank improvement = false
literature novelty = NOT ESTABLISHED
```
