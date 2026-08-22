# Tangent diagnostic at the 64-term Glynn point

## Status

`EXACT FINITE-FIELD LOCAL RIGIDITY DIAGNOSTIC; NOT A GLOBAL RANK PROOF.`

The earlier bounded search found no 49-point solution of a `35 x 35`
squarefree-row mixed-catalectic block.  Instead of adding random samples,
this computation starts at a point known to be consistent: the complete 64
normalized sign points in Glynn's decomposition.  It asks whether the
consistent locus has infinitesimal directions capable of changing the term
coefficients independently, which would be a prerequisite for a local path
toward deleting fifteen terms.

Each projective point is normalized by `a_0=1`.  The variables are its six
remaining coordinates and one coefficient, hence `64 * 7 = 448` variables.
All ranks below are exact over `F_65521`.

## The 1,225-equation subblock is locally too weak

For the complementary `(3,4)` squarefree block alone, the Jacobian has shape
`1225 x 448` and rank 225.  Its kernel has dimension 223, and its projection
to the 64 coefficient variables has dimension 64.  Thus every first-order
coefficient change can be absorbed inside this subblock.  This explains why
the block is a useful fixed-sample obstruction but a poor system for Newton
continuation: most apparent directions are artifacts of omitted equations.

## The complete degree-seven system is locally rigid

The full Waring/mixed-partial identity uses all 1,716 degree-seven monomial
coefficients.  The script verifies first that the normalized Glynn
coefficients have exactly zero residual.  Its `1716 x 448` Jacobian has

- point-coordinate rank 379;
- coefficient-column rank 64;
- full rank 442;
- tangent dimension 6;
- coefficient-projection dimension 1.

The six tangent dimensions are exactly the expected diagonal changes of the
six free coordinates; their induced coefficient motion is only a common
one-dimensional rescaling.  Consequently there is no infinitesimal direction
on this local branch that independently drives fifteen selected nonzero
coefficients to zero.  In computational terms, the normalized Glynn point is
locally rigid modulo the evident diagonal torus.

This is a local statement at one characteristic-`65521` point.  It does not
exclude a disconnected 49-point component and is not a characteristic-zero
ordinary- or border-rank proof.  Its main routing consequence is negative but
sharp: continuation from Glynn64 is not a promising route to a 49-term
candidate; subsequent computation should target other determinantal
components or the mixed packet B equations.

The largest matrix occupies about 5.9 MiB as raw 64-bit integers.  Including
FLINT conversion, the conservative peak is below 0.15 GiB.  The frozen run
takes below one second on one CPU process; GPU acceleration would add overhead
without helping exact modular elimination at this size.

## Replay

```text
python scripts/n7_glynn64_mixed_catalectic_tangent.py \
  --json data/n7_glynn64_mixed_catalectic_tangent.json
python -m unittest tests.test_n7_glynn64_mixed_catalectic_tangent -v
```
