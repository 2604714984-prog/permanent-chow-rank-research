# A relation budget for quotient Koszul gain

## Status and scope

`PROOF_DRAFT_COMPLETE`, `ROUTE_DIAGNOSTIC`.

This note rewrites the quotient Koszul gain of a fixed sum as the rank of a
sum of quotient maps and applies a block-Sylvester inequality.  For `perm_6`,
the universal one-term full-gain theorem makes every individual quotient map
lossless.  The result identifies the two genuinely coupled relation spaces
that must still be controlled.  It does not bound them sharply enough to prove
lower 26.

## 1. Quotient maps

Let `P=perm_6`, let

\[
 R=T_1+\cdots+T_q,
\]

and work with the central first-Koszul flattening.  Write

\[
 K_0=K_3(P),\qquad K_i=K_3(T_i),qquad
 Y_0=\operatorname{im}K_0.
\]

Let `pi` be the quotient map from the Koszul target to the quotient by `Y_0`
and put

\[
 \overline K_i=\pi K_i,qquad r_i=\operatorname{rank}K_i.
\]

The universal single-term theorem gives

\[
 \operatorname{im}K_i\cap Y_0=0
\]

for every nonzero sextic Chow term.  Hence

\[
 \operatorname{rank}\overline K_i=r_i.             \tag{1.1}
\]

Let `E=D_3(P)` and `H=D_3(R)`.  The quotient gain from
`docs/quotient_koszul_gain.md` is

\[
 \Gamma_E(H)
 =\dim\frac{\delta_3((E+H)\otimes V)}{delta_3(E\otimes V)}.
\]

Because the catalecticant and the Koszul flattening are linear in the form,

\[
 \boxed{
 \Gamma_E(H)
 =\operatorname{rank}\left(\sum_{i=1}^q\overline K_i\right).
 }                                                   \tag{1.2}

Thus quotient gain is a coupled rank problem for individually lossless maps.

## 2. Input and output relation dimensions

For maps `B_i:X -> Z`, each of rank `r_i`, define

\[
\begin{aligned}
 \kappa_{\rm out}
 &=\sum_i r_i-dim\sum_i\operatorname{im}B_i,\\
 \kappa_{\rm in}
 &=\sum_i r_i-dim\sum_i\operatorname{im}B_i^*.
\end{aligned}                                      \tag{2.1}

These are respectively the relation dimensions among the column spaces and
the row spaces.

### Lemma 2.1 — block-Sylvester

\[
 \operatorname{rank}\left(\sum_iB_i\right)
 \ge
 \sum_i r_i-\kappa_{\rm out}-\kappa_{\rm in}.       \tag{2.2}
\]

### Proof

Choose rank factorizations `B_i=P_i Q_i` through spaces of dimension `r_i`.
Let `P` be the block row with blocks `P_i` and `Q` the block column with blocks
`Q_i`.  Then

\[
 \sum_iB_i=PQ,
\]

while

\[
 \operatorname{rank}P=\sum_i r_i-\kappa_{\rm out},
 \qquad
 \operatorname{rank}Q=\sum_i r_i-\kappa_{\rm in}.
\]

Sylvester's rank inequality for `PQ` proves (2.2).

## 3. The input relation cap

Let

\[
 U_i=\operatorname{im}C_{3,3}(T_i)
\]

and define the literal central image-relation dimension

\[
 \rho=dim\ker\left(igoplus_iU_i\longrightarrow\sum_iU_i\right).
\]

The row space of `overline K_i` is contained in the row space of `K_i`, which
is contained in

\[
 U_i\otimes V^*.
\]

Here the central catalecticants are symmetric, so their row and column image
spaces are identified.  Relations among the smaller row spaces inject into
relations among the spaces `U_i tensor V^*`.  The latter relation space is
the tensor product of the central relation space with `V^*` and has dimension
`36 rho`.  Consequently

\[
 \boxed{\kappa_{\rm in}\le36\rho.}                 \tag{3.1}
\]

## 4. The exact output obstruction

Put

\[
 Y_i=\operatorname{im}K_i,qquad S=\sum_iY_i,
\]

and define

\[
 \eta=\sum_i r_i-\dim S,
 \qquad
 j=\dim(S\cap Y_0).                                \tag{4.1}

The number `eta` measures relations internal to the fixed terms' ordinary
Koszul output spaces.  The number `j` measures an aggregate collision with the
permanent Koszul image.  Although each `Y_i` meets `Y_0` trivially, their sum
can meet `Y_0` nontrivially.

Since quotienting `S` by `Y_0` lowers its dimension by exactly `j`,

\[
 \dim\sum_i\operatorname{im}\overline K_i
 =\dim S-j.
\]

Using (1.1), this gives the exact identity

\[
 \boxed{\kappa_{\rm out}=\eta+j.}                  \tag{4.2}

Combining (1.2), (2.2), (3.1), and (4.2) proves the main bound:

### Theorem 4.1

\[
 \boxed{
 \Gamma_E(H)
 \ge
 \sum_{i=1}^q r_i-36\rho-\eta-j.
 }                                                   \tag{4.3}

The right side may be replaced by its maximum with zero.

## 5. Why this does not yet prove lower 26

The theorem cleanly separates three losses:

1. `36 rho`, an upper bound for row-space relations inherited from central
   image overlap;
2. `eta`, relations already present among the fixed terms' Koszul output
   spaces;
3. `j`, a genuinely aggregate collision with the permanent Koszul image.

The universal one-term theorem controls none of `eta+j` beyond showing that
`j=0` for a single fixed term.  Moreover `36 rho` can exceed the total
individual rank budget in the large-relation states left by the lower-26
diagnostic.  Thus (4.3) is frequently vacuous with the currently proved
dimension bounds.

For a state with fixed count `q`, central intersection `b`, and required gain

\[
 g_{\rm req}
 =\max\{0,705(25-q)+1-(14175-36b)\},
\]

a sufficient new estimate would be

\[
 36\rho+\eta+j
 \le\sum_i r_i-g_{\rm req}.                         \tag{5.1}

No such uniform inequality is proved here.  Equation (5.1) is the precise
finite interface that a successor must address.  A bound on `rho` alone, or
another repetition of single-term full gain, cannot control the aggregate
collision `j`.

N6-026 gives a sharp warning about the form of any successor.  It constructs
a fixed sum of exact Chow rank six with

\[
 \rho=0,\qquad \eta=0,\qquad j=72.
\]

Therefore neither minimum length nor any inequality bounding `j` solely by
`rho` and `eta` can prove (5.1).  A lower-26 argument must use the additional
residual constraint that the fixed sum is a partial sum in an equality
`perm_6=R+Q` with `Q` of Chow rank at most `25-q`, or replace this scalar
relation budget by a genuinely coupled invariant.

For the N6-026 example the central intersection with the permanent derivative
space is only `b=2`.  The lower-26 six-fixed frontier instead forces `b>=20`.
Thus the smallest surviving refinement is to combine aggregate collision with
this high-intersection condition; N6-026 does not falsify such a statement.
