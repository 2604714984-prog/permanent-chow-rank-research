# `perm_7` lower-51: redundant-image residual propagation

## Statement

Let `B` be a direct factor-plane basis in a hypothetical 50-term identity.
For an outside rank-seven term `t`, write

\[
 W_{tc}=\operatorname{im}\bigl(P_{tc}:(A_c)_1\to(A_t)_1\bigr).
\]

Assume the **deletion-spanning condition**

\[
 \sum_{j\in B\setminus\{c\}}W_{tj}=(A_t)_1
 \quad\text{for every }c\in B.                    \tag{1}
\]

Then evaluation is onto:

\[
 \operatorname{ev}_t:K_4\twoheadrightarrow(A_t)_4. \tag{2}
\]

Consequently `dim K4 >= 35`.  If the branch residual cap is strictly less
than 35, that branch is impossible.  If
`dim K3+dim K4 <= 35`, then necessarily

\[
 \boxed{K_3=0,\qquad \dim K_4=35,\qquad
 K_4\xrightarrow{\sim}(A_t)_4.}                    \tag{3}
\]

This is `RESIDUAL-MULTIPLICATION-REDUNDANT` and
`RESIDUAL-PROPAGATION-REDUNDANT`, not the unrestricted residual theorem.

## Proof

Put `Z_t=ev_t(K4)`.  Corrected cubic localization makes the projection to
the basis blocks onto, while the individual map `R3 -> (A_t)_3` is onto.
Thus an arbitrary `q in (A_t)_3` is the `t`-component of

\[
 r=\sum_{c\in B}r_c(u_c)+k,
 \qquad k\in K_3,                                  \tag{4}
\]

where `r_c(u_c)` has basis support only at `c`.

For `j != c`, multiply `r_c(u_c)` by a degree-one codeword supported at
the basis block `j`.  Its restriction to every basis block is zero, so the
product lies in `K4`; at `t` these products contain

\[
 W_{tj}\,\Phi_{tc}(u_c).
\]

Summing over `j != c` and using (1) puts the full shadow
`(A_t)_1 Phi_tc(u_c)` in `Z_t`.  Multiplying `k` by global linear classes
likewise puts `(A_t)_1 k_t` in `Z_t`.  Equation (4) therefore gives

\[
 (A_t)_1q\subseteq Z_t.
\]

Since `q` was arbitrary and Boolean multiplication satisfies
`(A_t)_1(A_t)_3=(A_t)_4`, (2) follows.  The dimension consequences are
immediate.

## What the theorem removes

For a mixed rank-six/rank-seven direct basis, the exact cap is

\[
 35-C_B-C_0.
\]

Hence any outside rank-seven term satisfying (1) is incompatible with every
positive basis or outside rank-six cost.  This removes all redundant-image
rows of the mixed scalar frontier without enumerating its 11,683,105 count
patterns.

For an all-rank-seven basis the cap is exactly 35.  The theorem recovers the
rigid middle pair (3), after which the code-transport argument may be used;
it does not by itself close partial-block packets.

## Sharp boundary and remaining cores

Condition (1) is essential.  It fails for precisely the configurations the
current proof must still analyze: deleting an essential projection block
leaves a proper subspace of `(A_t)_1`.  The exchange table permits, among
these minimal spanning cores,

1. one rank-seven pivot;
2. a transverse rank-one/rank-six pair;
3. two rank-six blocks with distinct kernel lines.

Thus the theorem makes the next gap smaller and explicit, but it neither
constructs the permanent connecting map nor proves `LOWER-51-PROMOTABLE`.
The arithmetic boundary is replayed by
`scripts/n7_lower51_residual_redundancy.py`.
