# Exceptional-source criterion for coordinate second-order lifts

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_COORDINATE_SECOND_ORDER_REDUCTION`,
`NOT_A_ZERO_THEOREM`.

Consider regular quartic component families obtained from coordinate initial
six-factor frames. Expand the labeled squarefree source branches as

\[
g(t)=\sum_\beta c_\beta(t)P_\beta(t),
\qquad
P_\beta(0)=x_{Q_\beta},
\]

where `Q_beta` is a four-cell coordinate multiset. Assume the total order-zero
and order-one quartics vanish.

Fix a perfect matching `M` which is not reachable from any initial component by
changing at most one factor. Suppose every active order-zero source capable of
reaching `M` by two factor motions satisfies all of the following:

1. its specialized source fiber is injective at the active branch;
2. its monomial `Q` has exactly two active branch occurrences, with
   coefficients `a` and `-a`;
3. every relevant one-factor intermediate monomial is absent from the complete
   initial source image; and
4. every relevant one-factor intermediate monomial is tangent to no other
   active order-zero source monomial.

Then the order-two coefficient of `M` is zero.

Equivalently, a nonzero second-order target outside all one-factor envelopes
requires at least one of four exceptional mechanisms:

```text
TRIPLE_SOURCE:       at least three active branches over one source monomial;
SOURCE_JET_ABSORPTION: a relevant intermediate monomial lies in the initial source image;
TANGENT_COLLISION:    a relevant intermediate monomial is tangent to another active source;
INTERNAL_FIBER:       repeated factors create a nontrivial specialized source fiber.
```

This criterion is the general form of the pair-cancellation argument used to
exclude the canonical fixed-`3 x 3` six-`C6` cover. It does not assert that any
exceptional mechanism is sufficient for a lift and does not change

\[
6\le\mu(6,4)\le8.
\]

## Proof

Group active branches by their specialized source monomial `Q`. Total
order-zero cancellation gives

\[
\sum_{\beta:Q_\beta=Q}c_\beta(0)=0.
\tag{1.1}
\]

Under condition 2, write the two active branches as `beta_+` and `beta_-`, with
coefficients `a` and `-a`.

Let

\[
R=M\cap Q,
\qquad |R|=2,
\qquad Q\setminus R=\{e,f\},
\qquad M\setminus R=\{y,z\}.
\]

The four relevant first-order intermediate monomials are

\[
x_{Q-e+y},\quad x_{Q-e+z},\quad
x_{Q-f+y},\quad x_{Q-f+z}.
\tag{1.2}
\]

Conditions 1, 3, and 4 imply that the coefficient of each monomial in (1.2)
in the total first derivative comes only from the two active `Q` branches. If
`lambda_(plus,e)(y)` denotes the coefficient of `y` in the first velocity of
factor `e`, vanishing of the first derivative gives

\[
a\lambda_{+,e}(y)-a\lambda_{-,e}(y)=0,
\]

and likewise for the other three choices. Hence all four relevant first factor
velocities agree between the two branches.

Because `M` lies outside every one-factor envelope, source-coefficient jets,
factor accelerations, and mixed source-factor terms cannot produce it. The
only contribution is the quadratic two-factor term. Its sum over the two
branches is

\[
\begin{aligned}
a(&\lambda_{+,e}(y)\lambda_{+,f}(z)
 +\lambda_{+,e}(z)\lambda_{+,f}(y))\\
-a(&\lambda_{-,e}(y)\lambda_{-,f}(z)
 +\lambda_{-,e}(z)\lambda_{-,f}(y)),
\end{aligned}
\]

which vanishes by the velocity equalities. Repeating this for every source
monomial capable of reaching `M` proves the criterion.

## Research consequence

A finite search for coordinate second-order survivors should not enumerate
arbitrary jet coefficients first. It should enumerate only support collections
carrying at least one exceptional mechanism for every target outside the
one-factor envelope union. The four exception labels above are a complete
necessary filter.

The next exact computation is therefore a support-orbit classification of
exceptional covers, followed only then by coefficient matrices on the surviving
orbits.
