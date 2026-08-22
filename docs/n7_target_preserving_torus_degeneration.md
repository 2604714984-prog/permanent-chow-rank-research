# Target-preserving torus degeneration for the `perm_7` B1 frontier

## Statement

Work over an algebraically closed field of characteristic zero. Let
`S=k[x0,...,x6]`, let `I` be the saturated homogeneous ideal of a length-42
projective scheme, and let `lambda` be a diagonal one-parameter subgroup.
Write `J=in_lambda(I)` for the homogeneous graded special-fibre ideal. Let

\[
T_6=\langle x_0\cdots\widehat{x_j}\cdots x_6:0\le j\le6\rangle.
\]

Every target monomial is a weight vector, so `T6` and `T6^perp` are
`lambda`-stable. The following facts are the H-04 interface.

1. The flat limit preserves every graded Hilbert value.
2. If `I6 subset T6^perp`, then `J6 subset T6^perp`.
3. Equivalently, target containment `T6 subset I6^perp` passes from the
   original scheme to the associated graded limit.
4. The converse is not automatic: target containment is a closed condition,
   so it may appear only on the special fibre.

For the second point, `lambda(t)I6` lies in the fixed closed Grassmannian
subvariety of subspaces of `T6^perp` for every nonzero `t`. Its Grassmannian
limit therefore lies there as well. Consequently, if every admissible
target-preserving monomial limit fails target containment, the original
stratum fails it too.

## Coupling and rank directions

Hilbert ranks survive because the family is flat, but weighted coupling needs
additional hypotheses. Matrices whose entries extend regularly to the
special fibre can only lose rank there:

\[
\operatorname{rank}M(0)\le\operatorname{rank}M(t)\quad(t\ne0).
\]

Thus relation dimensions can jump upward and a fixed inclusion can fail in
the limit. Nonvanishing of `D(0)` alone is not enough: for example,
`ker[t] subset im[t]` holds for `t != 0` and fails at zero. The inclusion
`R4 subset D C3` passes only after `R4` and `C3` have been extended as
constant-rank subbundles in one fixed ambient bundle and `D(t)` extends
invertibly; then it is a closed Grassmannian incidence. If these subbundle
hypotheses are absent, or if some weights vanish or blow up after projective
rescaling, the special fibre is only a boundary control and cannot certify
nonzero weighted coupling for the original component. No converse rank
inference is allowed.

## Reducedness, saturation, and flatness

Flatness preserves length and the graded quotient Hilbert function, not
reducedness. Distinct points may collide and the special fibre may be
nonreduced. The raw initial ideal `J` is the degree-by-degree flat algebra
used above. Its saturation `J^sat` defines the same `Proj`, but it can differ
from `J` in low degrees and therefore need not retain the displayed H4--H6
values. H-05 may replace `J` by a saturated point ideal only after proving
that the relevant graded pieces agree; irrelevant torsion cannot be silently
discarded or treated as points.

Minimal support, point distinctness, separator degrees, and nonzero term
weights therefore require separate survivor gates. Generic Borel-fixed
initial ideals after an arbitrary coordinate change are not target-preserving
unless the permanent target is transformed at the same time.

## Boundary

This completes H-04 and authorizes the one-way H-05 monomial-initial test. It
does not enumerate H-05 initials, preserve reducedness, preserve nonzero
weights on a toric boundary, or close any F frontier by itself.
