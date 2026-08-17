# Research-ledger delta: matching-orbit linear postprocessing

## Status

This delta belongs to the branch
`research/matching-orbit-postprocessing-ceiling` and supplements the canonical
`RESEARCH_LEDGER.md` until the stacked research chain is consolidated.

No numerical Chow-rank boundary changes.

## New theorem

Let `X` be a finite transitive `G`-set and let

```text
A:k^(X x X) tensor H -> Y
```

be arbitrary. Restrict `A` to the graph subspaces

```text
span{e_(g x) tensor e_(h x):x in X} tensor H.
```

Averaging their orthogonal projectors gives `I/|X|`. Applying this to the
kernel of `A` proves

```text
max_(g,h) rank(A restricted to graph(g,h) tensor H)
 >= rank(A)/|X|.
```

For `X=C([n],m)`, graph subspaces are exactly the matching-projected derivative
spaces of permutation-matching Chow terms. Consequently every fixed linear
postprocessing of the canonical matching-projected degree-`m` catalecticant is
capped by

```text
binom(n,m),
```

and every finite block-diagonal family is capped by the central binomial.

## Routes closed

```text
row-column projected catalecticants             CLOSED
matching-projected standard Koszul maps          CLOSED
row-column projections inside fixed Koszul maps  CLOSED
arbitrary fixed linear postprocessing after Q_m  CLOSED
finite block sums across derivative degrees      CLOSED
```

## Routes still open

```text
pre-catalecticant source projections
arbitrary Pieri maps not factoring through Q_m C_f
minimal representation-valued syzygy functors
nonlinear joint determinantal data
valuative flat-sum obstructions
Chow-realizability defects
```

## Claim boundary

The theorem is a route ceiling, not an upper bound on actual Chow rank. It
introduces no new finite-`n` lower bound and does not close nonlinear or
module-dependent relation constructions.
