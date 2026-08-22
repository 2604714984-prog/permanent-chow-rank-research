# `perm_7` lower-51: the full-block direct-basis branch

## Claim and scope

Let a hypothetical minimal 50-term identity for `perm_7` consist entirely of
factor-rank-seven terms and admit a direct factor-plane basis

\[
 V=L_1\oplus\cdots\oplus L_7.
\]

For a nonbasis label `t`, let

\[
 P_{tc}:(A_c)_1\longrightarrow(A_t)_1
\]

be its restriction block relative to this basis.  Assume every `P_{tc}` is
either zero or an isomorphism.  Then the 50-term identity is impossible.

This strictly extends the imported simple-matroid branch by allowing planes
parallel to basis planes.  It does not cover a nonbasis plane having a
restriction block of rank `1,...,6`.

## 1. Parallel labels are bounded

Write `S_t={c:P_tc is nonzero}`.  If `|S_t|=1`, say `S_t={b}`, then
`L_t` is contained in `L_b`; both have dimension seven, so `L_t=L_b`.

The v7 three-label floor is

\[
 \dim(L_i+L_j+L_k)\ge12.
\]

Consequently a basis plane `L_b` has at most one nonbasis label parallel to
it: the basis label and two parallel labels would have joint span seven.
There are at most seven parallel nonbasis labels.  Since there are 43
nonbasis labels, at least 36 have support of size at least two.

## 2. The residual middle code is forced to `(K_3,K_4)=(0,35)`

Let `R_d` be the permanent-relative middle relation space and set

\[
 K_d=\ker\left(R_d\longrightarrow
       \bigoplus_{c=1}^7(A_c)_d\right).
\]

The corrected direct-basis localization and the 50-term Sylvester bound give

\[
 \dim K_3+\dim K_4\le35.                 \tag{1}
\]

Choose a nonparallel label `t`.  Its support has at least two elements and
every supported block is invertible.  The multiplication argument in the
imported simple-branch proof applies verbatim: for any basis-supported cubic
lift, multiplication by a different supported basis block moves its complete
linear shadow into the image of `K_4` at `t`.  Hence

\[
 K_4\twoheadrightarrow(A_t)_4.
\]

The target has dimension 35, so (1) forces

\[
 \boxed{K_3=0,\qquad\dim K_4=35,
 \qquad K_4\xrightarrow{\sim}(A_t)_4}       \tag{2}
\]

for every nonparallel label `t`.

For `b in S_t`, replacing `L_b` by `L_t` is again a direct factor basis,
because `P_tb` is invertible.  Corrected cubic localization therefore gives
the same invertibility of the cubic transfer block used in the imported
proof.

## 3. Every nonparallel label has the same support

Take two nonparallel labels `s,t`.  For `c in S_s`, choose
`b in S_s` distinct from `c`.  Multiply the cubic lift supported at `b` by a
linear codeword supported at `c`.  Evaluation at `s` can be chosen nonzero.
By (2), evaluation of `K_4` at `t` is injective, so its value at `t` is also
nonzero.  This is impossible if `c` is not in `S_t`.  Thus
`S_s` is contained in `S_t`; reversing the labels gives equality.

All nonparallel labels therefore have one common support `S`, with
`|S|>=2`.

## 4. Full support is impossible

If `S={1,...,7}`, the zero-radical Boolean multiplication comparison from
the imported proof shows that every nonparallel plane is the same plane.
There are at least 36 such labels, whereas the three-label floor prohibits
even three labels with one common seven-plane.  This is a contradiction.

## 5. Proper support gives a forbidden direct sum

Suppose `S` is proper.  Every nonparallel term lies in

\[
 V_S=\bigoplus_{c\in S}L_c.
\]

Every parallel nonbasis term lies in its corresponding `L_b`.  Group the
basis terms, parallel terms, and nonparallel terms according to whether their
supporting basis indices lie in `S` or its complement.  The actual identity
then has the form

\[
 \operatorname{perm}_7=F(V_S)+H(V_{S^c}).            \tag{3}
\]

Both label groups are nonempty.  Neither polynomial in (3) is zero: either
zero group would be a nonempty proper vanishing subpacket, contradicting
minimality of the 50-term identity.  Thus (3) is a nontrivial
Sebastiani--Thom decomposition.  The scalar-centroid theorem for the
permanent, proved in the imported simple-branch note, excludes it.

## Verdict

Both possible common supports are contradictory.  Hence:

> No all-rank-seven 50-term identity admits a direct factor basis when every
> nonzero basis restriction block has rank seven, even when parallel factor
> planes are allowed.

The remaining all-rank-seven direct-basis frontier consists precisely of
branches having at least one partial restriction block of rank `1,...,6`.

