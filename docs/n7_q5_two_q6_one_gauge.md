# The `q5=2, q6=1` gauge does not create a survivor

## Theorem

Let `Z` be 42 distinct reduced points of `P6` in a target-compatible
common-graph equality packet over an algebraically closed field of
characteristic zero.  Suppose

\[
q_5=\dim R_5=2,\qquad q_6=\dim R_6=1.
\]

Then the packet is impossible.  In particular this closes both remaining
`q5=2` signatures:

- F1 with `(H3,H4,H5,H6)=(33,39,40,41)`;
- F3 with `(H3,H4,H5,H6)=(34,38,40,41)`.

The point is not that a bivector pencil is gauge invariant.  It is not.  The
point is that every coefficient representative produces an exhaustive
pencil trichotomy, and every branch admits a replacement of cost less than
64.  Changing gauge adds the zero vector field, so the replacement
contradiction applies in any chosen gauge.

## The canonical class and the gauge rank

Choose a nonzero generator `tau` of `R6`.  Coefficient representatives form
an affine space under `lambda in k7`:

\[
c_i\longmapsto c_i+\tau_i\lambda.
\]

The relation tensor changes by

\[
d_A(\lambda)_i=\tau_i(\lambda\wedge a_i),
\qquad
d_A:k^7\longrightarrow R_5\otimes\Lambda^2k^7.
\]

Thus only `[Psi] in coker(d_A)` is canonical.  A nonzero relation among
sixth powers of distinct points has support at least eight: degree-six
products of separating hyperplanes prove independence for every subset of
at most seven points.  If `d_A(lambda)=0`, then every `a_i` in this support
is proportional to `lambda`.  The support contains distinct points, so
`lambda=0`.  Consequently

\[
\ker d_A=0,\qquad \operatorname{rank}d_A=7,
\qquad \dim\operatorname{coker}d_A=42-7=35.
\]

Here the target dimension is `dim(R5 tensor Lambda2(k7))=2*21=42`.

There is also an explicit local slice.  Choose distinct
`i0,i1 in supp(tau)`.  The six gauge directions modulo `k a_i0` uniquely
kill `Psi_i0`.  The remaining direction `k a_i0` changes `Psi_i1` by the
nonzero vector `tau_i1 a_i0 wedge a_i1`; one chosen coordinate along that
vector can therefore be killed uniquely.  This is an ordered-pair-dependent
normal form, not a canonical pencil.

## Why gauge causes no replacement obstruction

For every representative `C`, automatic mixed-partial compatibility gives

\[
\Psi(C)\in R_5\otimes\Lambda^2k^7.
\]

Choose a basis `rho1,rho2` of `R5` and write

\[
c_i\wedge a_i=\rho_{1i}\beta_1+\rho_{2i}\beta_2.
\]

Every nonzero coordinate is decomposable, so the pencil theorem gives one
of three branches for this representative.  A gauge change may move between
the branches, but this is harmless because all three are closed below.
Moreover the gauge addition is literally zero as a vector field:

\[
\sum_i \tau_i\lambda l_i^6
=\lambda\left(\sum_i\tau_i l_i^6\right)=0.
\]

## Branch 1: bivector span at most one

Span zero makes every summand termwise integrable, with total Waring cost at
most 42.  In span one, the nonzero supported part lies in a fixed two-plane
and is closed by itself.  It integrates to a binary septic of rank at most
seven.  Its fifth-relation support has size at least seven, so adding the
termwise complement again costs at most 42.

## Branch 2: a non-Grassmannian line

There are at most two nonzero relation ratios.  There cannot be only one,
because two independent rows of `R5` would then be proportional.  After a
relation-basis change the two ratios give disjoint nonempty supports `A,B`
and disjoint fifth-power relations `rho_A,rho_B`.

For each block, a nonzero coefficient bivector puts its supported vector
field in a fixed two-plane, so that closed block integrates to a binary
septic of rank at most seven.  A zero coefficient bivector makes that block
termwise integrable.  Each nonzero fifth relation has support at least
seven.  Hence replacing the two blocks and the zero-column complement costs
at most 42.  This recovers the sparse-ratio contradiction without using
sixth-power independence; distinct reduced points suffice.

## Branch 3: a Grassmannian flag line

Put the line in the form

\[
\beta_1=p\wedge q,\qquad\beta_2=p\wedge r.
\]

All nonzero tensor columns have `a_i,c_i` in the fixed three-space and their
two-plane contains `p`.  Zero tensor columns integrate termwise, so the
nonzero supported vector field is closed by itself.

If no `a_i` is proportional to `p`, subtract one seventh power per supported
index.  The residual closed field has only the `p` coefficient direction
and integrates to one seventh power.  The full cost is at most 43.

If one `a_i` is proportional to `p` (there is at most one by distinctness),
subtract powers at all other supported indices.  The residual closed field
has coefficient directions in a fixed two-space and hence integrates to a
binary septic of rank at most seven.  The full cost is at most 48.

## Conclusion and boundary

Every gauge representative falls into a branch whose primitive has Waring
rank at most 48, contradicting

\[
\operatorname{WaringRank}(x_0x_1\cdots x_6)=64.
\]

Therefore both `q5=2,q6=1` common-graph signatures are empty.  Together with
the gauge-free F3 result, the complete `q5=2` class F1/F3 is closed.

This does not close the `q5=3` or `q5=4` signatures, arbitrary Packet B,
Packet A, ordinary lower 50, or border Chow rank.
