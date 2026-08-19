# Natural-span compression barriers at `mu(6,4)`

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`, `STRICT_ROUTE_BARRIER`.

The exact value of

\[
5\le \mu(6,4)\le 8
\]

remains open. This note proves that neither of the two natural explicit spaces
containing a coordinate `perm_4` can be compressed internally from eight or
six displayed generators to fewer degree-six Chow derivative components.

More precisely:

1. every nonzero vector in the six-dimensional `(2,2)` partition-Laplace
   space has essential dimension at least eight, so that space has zero
   intersection with the output-degree-four derivative space of every
   degree-six Chow term;
2. in the eight-dimensional Glynn sign span, the vectors of essential
   dimension at most six are exactly the eight original sign lines;
3. consequently, a decomposition of `perm_4` by degree-six Chow derivative
   components that are individually constrained to remain in the Glynn span
   needs exactly eight components.

These are internal-span statements. They do **not** prove `mu(6,4)=8`, exclude
five-, six-, or seven-term decompositions whose components leave the natural
spaces and cancel outside them, or improve an unrestricted Chow-rank or
border-rank bound.

## 1. Essential-space cap for one degree-six Chow component

Let

\[
T=\ell_1\cdots\ell_6
\]

be an arbitrary, possibly degenerate, degree-six Chow term and put

\[
L_T=\operatorname{span}\{\ell_1,\ldots,\ell_6\}.
\]

Every output-degree-four derivative of `T` belongs to `Sym^4(L_T)`. Therefore
every

\[
h\in\mathcal D_4(T)
\]

satisfies

\[
\operatorname{Ess}(h)\subseteq L_T,
\qquad
\boxed{\dim\operatorname{Ess}(h)\le6.}
\tag{1.1}
\]

The two barriers below compare this universal cap with exact essential-space
loci inside the natural permanent spaces.

## 2. The `(2,2)` partition-Laplace space

Work in one `4 x 4` coordinate block

\[
X=(x_{rc})_{0\le r,c<4}
\]

and split the rows as

\[
\{0,1\}\sqcup\{2,3\}.
\]

For every two-subset `C` of the columns, define

\[
G_C
=
\operatorname{perm}(X_{\{0,1\},C})
\operatorname{perm}(X_{\{2,3\},C^c}).
\tag{2.1}
\]

The six summands have disjoint monomial supports and the partition-Laplace
identity is

\[
\operatorname{perm}_4
=
\sum_{C\in\binom{[4]}2}G_C.
\tag{2.2}
\]

Put

\[
L_{22}=\operatorname{span}\{G_C:C\in\tbinom{[4]}2\}.
\]

### Theorem 2.1 -- exact essential dimension in `L_22`

Let

\[
0\ne g=
\sum_C a_CG_C
\]

and let

\[
\mathcal S=\{C:a_C\ne0\}.
\]

Then

\[
\boxed{
\dim\operatorname{Ess}(g)
=
2\left|\bigcup_{C\in\mathcal S}C\right|
+
2\left|\bigcup_{C\in\mathcal S}C^c\right|.
}
\tag{2.3}
\]

In particular,

\[
\boxed{\dim\operatorname{Ess}(g)\ge8.}
\tag{2.4}
\]

### Proof

Fix the first matrix row. For a column `c`, the derivative
`partial_(0,c) g` is a sum over the selected sets `C` containing `c`. For
`C={c,d}`, every resulting cubic monomial contains `x_(1,d)` and uses the two
remaining columns in rows two and three. Different choices of `d` have
disjoint monomial supports, so this derivative is nonzero exactly when

\[
c\in\bigcup_{C\in\mathcal S}C.
\]

For two different columns `c`, the derivative supports are again disjoint:
every monomial in `partial_(0,c)g` uses all columns except `c`. Hence the four
first-row derivatives have rank equal to the size of the displayed union. The
same argument applies to row one.

For either bottom row, `partial_(r,c)g` is nonzero exactly when `c` belongs to
the complement of a selected `C`, and distinct columns again give disjoint
supports. Each bottom row therefore contributes

\[
\left|\bigcup_{C\in\mathcal S}C^c\right|.
\]

Derivatives leaving different matrix rows have different row multidegrees, so
their spans are disjoint. Summing the four row contributions proves (2.3). A
nonempty family of two-subsets has both unions of size at least two, which
proves (2.4). QED.

### Corollary 2.2 -- no internal Laplace component

For every degree-six Chow term `T`,

\[
\boxed{L_{22}\cap\mathcal D_4(T)=0.}
\tag{2.5}
\]

Indeed, a nonzero vector in the left space would have essential dimension at
least eight by Theorem 2.1 and at most six by (1.1).

Thus the six Laplace summands cannot be replaced by another basis of their own
span whose vectors are degree-six Chow derivative components. This does not
exclude a six-term decomposition with components outside `L_22` and
cancellation in the quotient by `L_22`.

## 3. The Glynn sign span

Let

\[
U=\mathbf k^4
\]

with basis indexed by the four columns. For

\[
\delta=(1,\varepsilon_1,\varepsilon_2,\varepsilon_3),
\qquad
\varepsilon_i\in\{\pm1\},
\]

define the row-homogeneous Chow term

\[
P_\delta
=
\prod_{r=0}^3
\left(
\sum_{c=0}^3\delta_cx_{rc}
\right).
\tag{3.1}
\]

Under the canonical identification of all four row spaces with `U`, this is
the symmetric tensor

\[
\delta^{\otimes4}.
\]

Put

\[
H=\operatorname{span}\{P_\delta\}.
\tag{3.2}
\]

The eight sign tensors are linearly independent: evaluation on the eight
parity classes of ordered four-tuples gives the `8 x 8` Walsh character
matrix. Hence

\[
\dim H=8.
\tag{3.3}
\]

### Lemma 3.1 -- essential dimension in the symmetric row span

For `0!=h in H`, let `rho(h)` be its mode rank as a tensor in
`U^(tensor 4)`. Since `h` is invariant under permutation of the four row
modes, every mode rank is `rho(h)`. The third derivatives that leave a linear
form in one fixed row span exactly the corresponding mode image. Different
row spaces are in direct sum. Therefore

\[
\boxed{
\dim\operatorname{Ess}(h)=4\rho(h).
}
\tag{3.4}
\]

If this dimension is at most six, then `rho(h)=1`. A symmetric tensor with
mode rank one is a fourth tensor power, so

\[
h=cv^{\otimes4}
\tag{3.5}
\]

for some nonzero `v in U` and scalar `c`.

### Lemma 3.2 -- fourth powers in the sign span

If

\[
0\ne v^{\otimes4}\in H,
\]

then, up to scale,

\[
\boxed{v=(1,\varepsilon_1,\varepsilon_2,\varepsilon_3),
\qquad\varepsilon_i\in\{\pm1\}.}
\tag{3.6}
\]

### Proof

Every ordered tensor coordinate in `H` depends only on the parity of the
numbers of indices equal to one, two, and three. This follows directly from

\[
(\delta^{\otimes4})_{i_1i_2i_3i_4}
=
\delta_{i_1}\delta_{i_2}\delta_{i_3}\delta_{i_4}.
\]

The parity-zero class contains the coordinates indexed by

\[
(i,i,i,i)
\quad\text{and}\quad
(i,i,j,j)
\]

for every `i,j`. Hence membership of `v^(tensor 4)` in `H` forces

\[
v_i^4=v_i^2v_j^2=v_j^4
\qquad\text{for all }i,j.
\tag{3.7}
\]

If one coordinate vanished, all fourth powers would vanish, contrary to
`v!=0`. Dividing (3.7) therefore gives

\[
v_i^2=v_j^2
\qquad\text{for all }i,j.
\]

Scale by the nonzero first coordinate. Characteristic zero then gives
`v_j=+1` or `-1`, proving (3.6). QED.

### Theorem 3.3 -- exact low-essential locus in `H`

\[
\boxed{
\{0\ne h\in H:\dim\operatorname{Ess}(h)\le6\}
=
\bigcup_\delta \mathbf k^*P_\delta.
}
\tag{3.8}
\]

This follows by combining Lemmas 3.1 and 3.2; the reverse inclusion is
immediate because every `P_delta` uses four essential row factors.

### Corollary 3.4 -- one Chow component meets at most one sign line

For every degree-six Chow term `T`, the linear space

\[
H\cap\mathcal D_4(T)
\]

is either zero or one of the eight lines `k P_delta`.

Every nonzero vector in the intersection has essential dimension at most six
by (1.1), so Theorem 3.3 places the whole intersection in a finite union of
lines. Over a characteristic-zero field, a linear subspace contained in a
finite union of lines has dimension at most one and, if nonzero, equals one of
those lines.

## 4. Exact internal minimum for the Glynn span

The order-four Glynn identity is

\[
\operatorname{perm}_4
=
\frac1{8}
\sum_{\delta=(1,\varepsilon_1,\varepsilon_2,\varepsilon_3)}
(\varepsilon_1\varepsilon_2\varepsilon_3)P_\delta.
\tag{4.1}
\]

All eight coefficients are nonzero. Since the eight sign tensors form a basis
of `H`, this expression is unique.

Define the internal degree-six block minimum

\[
\nu_H
=
\min\left\{
q:
\operatorname{perm}_4=h_1+\cdots+h_q,
\quad
h_i\in H\cap\mathcal D_4(T_i),
\quad
\deg T_i=6
\right\}.
\tag{4.2}
\]

Corollary 3.4 says that every summand occupies at most one sign-basis line. The
unique coordinate vector of `perm_4` in that basis has eight nonzero entries.
Therefore at least eight summands are necessary. Equation (4.1), with two
unused factors appended to every `P_delta`, gives eight summands. Thus

\[
\boxed{\nu_H=8.}
\tag{4.3}
\]

This excludes every internal linear regrouping of the Glynn decomposition,
even when the six factors defining each ambient Chow term are allowed to mix
rows. It does not exclude components outside `H` whose non-`H` parts cancel in
the total sum.

## 5. Consequence for the active search

The two most direct constructions now have exact stopping points:

```text
(2,2) partition-Laplace span:
  every nonzero vector has Ess >= 8
  intersection with every degree-six D_4(T) is zero

Glynn sign span:
  low-essential locus is exactly eight sign lines
  internal degree-six block minimum is exactly 8
```

Accordingly, any unrestricted five-, six-, or seven-term construction for
`mu(6,4)` must leave both natural spaces componentwise. It must use genuine
ambient cancellation, and a span-preserving basis search cannot find it.

The next valid lower-bound interface remains the five-term essential-space
problem. The first descendants are four-dimensional triple-supported cubic
polar spaces obtained by annihilating complementary component pairs. A useful
next theorem must classify those cubic three-block spaces or produce an
explicit ambient-cancellation construction.

## 6. Exact replay

Run

```bash
python scripts/general_quartic_natural_span_barriers.py \
  --json /tmp/general_quartic_natural_span_barriers.json
python scripts/general_quartic_natural_span_barriers_independent.py \
  --expect-sha256 d40eef4be59483e19dced0f69232b79bdcead026531aac018f3490ee44104145
python -m unittest tests.test_general_quartic_natural_span_barriers -v
```

The primary replay checks all 63 nonempty supports of the six Laplace basis
vectors. Their exact essential-dimension distribution is

```text
Ess dimension       support patterns
8                    6
12                  12
14                   8
16                  37
```

It also reconstructs the complete `8 x 8` Walsh interface and verifies the
Glynn identity on all 256 ordered tensor coordinates. The independent replay
expands every polynomial directly, computes rational derivative ranks, and
checks the projective low-rank locus over the odd primes `3,5,7,11`. The
finite-field enumeration is diagnostic only; the characteristic-zero
classification is the parity argument in Lemma 3.2.
