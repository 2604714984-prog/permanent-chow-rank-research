# `perm_7` F3, `H6=42`: sparse-ratio closure

## Theorem

Work over an algebraically closed field of characteristic zero. Assume a
target-compatible common-graph configuration in the F3 layer

\[
(H_3,H_4,H_5,H_6)=(34,38,40,42),
\qquad (q_5,q_6)=(2,0).
\]

If the nonzero relation-coordinate columns in `P(R5*)=P1` take at most two
values, then the configuration is impossible. Consequently the complete
two-dimensional non-Grassmannian pencil branch is closed. Within the
two-dimensional bivector-span branch, any survivor must be a Grassmannian
flag line using at least three distinct nonzero relation-coordinate values.

## Disjoint-circuit reduction

Two independent rows spanning `R5` cannot have a projective column image of
only one nonzero value. With at most two values there are therefore exactly
two. Changing the relation basis, and contragrediently changing the two
bivectors, gives a partition

\[
\{1,\ldots,42\}=A\sqcup B\sqcup Z,
\qquad R_5=k\rho_A\oplus k\rho_B,
\]

where `rho_A` and `rho_B` have disjoint supports and are nonzero at every
coordinate of their named blocks; all relation columns vanish on `Z`.
Writing the target coefficient columns and nonzero point columns as `c_i,a_i`,
automatic mixed-partial compatibility becomes

\[
c_i\wedge a_i=\rho_X(i)\gamma_X\quad(i\in X),
\qquad c_i\wedge a_i=0\quad(i\in Z).
\]

If `gamma_X` is nonzero, it is decomposable and every `a_i,c_i` in that block
lies in its two-plane. Since `H6=42`, the sixth powers are independent, so
the projective points are distinct. Any fifth-power relation supported
strictly inside `X` would lie in `R5`; disjointness then makes it a multiple
of `rho_X`. Thus `rho_X` is a circuit. On the degree-five rational normal
curve, at most six distinct points are independent and every seven are
dependent. Thus, for such a nonzero `gamma_X` block, `|X|=7`.

## Blockwise integration and Waring contradiction

The nonzero block is integrable on its own, not merely as part of the total
gradient: its mixed-partial defect is

\[
\gamma_X\sum_{i\in X}\rho_X(i)l_i^5=0.
\]

It therefore integrates to a homogeneous septic on the two-plane, hence to
a binary septic of Waring rank at most seven. If `gamma_X=0`, each term in
that block has `c_i` proportional to `a_i` and integrates individually to a
seventh power. The same termwise statement holds on `Z`. Each block costs at
most its support size, so adding the block primitives gives

\[
\operatorname{WaringRank}(x_0\cdots x_6)
\le |A|+|B|+|Z|=42,
\]

contradicting the established value 64.

## Boundary

This closes the at-most-two-ratio locus and hence the two-dimensional
non-Grassmannian pencil without weighted coupling. It does not close the
bivector-span-zero/one branch, the Grassmannian flag line, the `H6=41` gauge
branch, all of F3, ordinary lower 50, or border rank.
