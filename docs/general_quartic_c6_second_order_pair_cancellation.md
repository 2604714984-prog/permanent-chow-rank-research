# Pair cancellation for the canonical six-`C6` second-order cover

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`,
`CANONICAL_C6_SECOND_ORDER_ZERO`.

Use the six canonical equality frames

\[
A_\mu=\{(r,c):0\le r,c<3,\ c\ne\mu(r)\},
\qquad \mu\in S_3,
\]

inside a fixed `3 x 3` subblock of the `4 x 4` variable block. Let six regular
coordinate component families have these initial frames, total order-zero and
order-one quartics equal to zero, and first potentially nonzero total term at
order two.

Then every order-two perfect-matching coefficient whose matching does not
contain `(3,3)` is zero. There are eighteen such matchings. Consequently the
order-two term cannot be a nonzero diagonal-torus transform of `perm_4`.

Thus the explicit six-envelope cover from the raw second-order support theorem
does not lift to a coefficient-compatible second-order witness. This result is
restricted to the canonical six frames on one fixed `3 x 3` block. It does not
exclude arbitrary collections of coordinate frames, noncoordinate initial
frames, singular valuations, or higher-order first nonzero terms, and it does
not change

\[
6\le\mu(6,4)\le8.
\]

## 1. Order-zero source relations

The preceding source reduction proves that the ninety source coordinates have
a nine-dimensional kernel. For each cell `v=(r,c)` of the `3 x 3` block, put

\[
Q_v
=\{(r,d):d\ne c\}\cup\{(s,c):s\ne r\}.
\]

This source monomial occurs in exactly two frames, denoted `mu_v^+` and
`mu_v^-`, one even and one odd. Every order-zero relation is uniquely

\[
\sum_v a_v
\left(e_{\mu_v^+,Q_v}-e_{\mu_v^-,Q_v}\right).
\tag{1.1}
\]

All source monomials of multiplicity one have zero order-zero coefficient.

## 2. Boundary tangent monomials are source-separated

Let

\[
B=\{(r,c):r=3\text{ or }c=3\}
\]

be the seven cells outside the fixed `3 x 3` subblock. For `e in Q_v` and
`y in B`, moving the factor at `e` to the boundary cell `y` produces the
quartic monomial

\[
y\,x_{Q_v\setminus\{e\}}.
\tag{2.1}
\]

This monomial cannot be a one-factor boundary tangent of a different source
mode `Q_w`. Such a collision would require a common three-cell subset of
`Q_v` and `Q_w`, whereas distinct cross modes intersect in at most two cells.
It also cannot be driven by a multiplicity-one source, because every such
order-zero coefficient is zero.

Write

\[
\lambda_{\mu,e}(y)
\]

for the coefficient of `y` in the first factor velocity at the factor cell
`e` of frame `mu`. The coefficient of (2.1) in the total first derivative is
therefore exactly

\[
a_v\left(
\lambda_{\mu_v^+,e}(y)
-
\lambda_{\mu_v^-,e}(y)
\right).
\tag{2.2}
\]

Since the total first derivative is zero, whenever `a_v!=0` one has

\[
\boxed{
\lambda_{\mu_v^+,e}(y)
=
\lambda_{\mu_v^-,e}(y)
\quad
(e\in Q_v,\ y\in B).
}
\tag{2.3}
\]

## 3. Quadratic pair cancellation

Let `M` be a perfect matching not containing `(3,3)`. It has exactly two
internal cells and two boundary cells:

\[
M=R\sqcup\{y,z\},
\qquad |R|=2,
\qquad y,z\in B.
\tag{3.1}
\]

A source-coefficient motion, a factor acceleration, or a mixed source-factor
term changes at most one internal factor and therefore cannot produce (3.1).
The coefficient can only come from two first-order factor motions applied to an
order-zero source `Q_v` with

\[
R\subseteq Q_v.
\tag{3.2}
\]

For such a mode, write `Q_v\setminus R={e,f}`. The contribution of its two
endpoint frames is

\[
\begin{aligned}
a_v\bigl(&
\lambda_{\mu_v^+,e}(y)\lambda_{\mu_v^+,f}(z)
+
\lambda_{\mu_v^+,e}(z)\lambda_{\mu_v^+,f}(y)
\bigr)\\
-a_v\bigl(&
\lambda_{\mu_v^-,e}(y)\lambda_{\mu_v^-,f}(z)
+
\lambda_{\mu_v^-,e}(z)\lambda_{\mu_v^-,f}(y)
\bigr).
\end{aligned}
\tag{3.3}
\]

Equation (2.3) makes the two parentheses equal, so (3.3) is zero. If `a_v=0`,
the contribution is zero trivially. Summing over the exactly two source modes
whose crosses contain `R` proves

\[
\boxed{[M]\sum_{\mu\in S_3}g_\mu^{(2)}=0}
\tag{3.4}
\]

for all eighteen matchings not containing `(3,3)`.

A nonzero diagonal-torus transform of `perm_4` has all eighteen coefficients
nonzero. This proves the theorem.

## 4. Why lower-order coefficient jets do not repair the target

Every initial source monomial lies entirely inside the fixed `3 x 3` block.
Consequently:

- a second-order source coefficient changes no factor and creates no boundary
  cell;
- a factor acceleration creates at most one boundary cell;
- a first-order source coefficient times one factor velocity creates at most
  one boundary cell.

The eighteen matchings in (3.1) contain two boundary cells, so only the
quadratic factor-velocity term can reach them. The cancellation in Section 3
is therefore exhaustive.

## 5. Consequence for the active search

The raw six-envelope cover was the first apparent extremal survivor after the
first-order closure theorem. It is now excluded at coefficient level. Any
remaining coordinate second-order candidate must change at least one of the
following features:

1. use a different collection of equality or sub-equality frames;
2. allow an order-zero source monomial to occur in at least three active
   branches;
3. use overlapping `3 x 3` blocks so that boundary tangent monomials cease to
   be source-separated; or
4. leave the coordinate regular stratum.

The next finite task is therefore to classify six-frame second-order support
covers by source multiplicity and boundary-tangent collision type, not to
revisit the canonical cover.
