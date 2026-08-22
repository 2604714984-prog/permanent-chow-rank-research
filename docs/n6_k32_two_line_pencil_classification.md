# N6-128: two-line pencils in the full first-Schur chart

## Result

At the (K_{3,2}) collision (L=M=A_3\otimes P_2), N6-126 gives 44
fixed rank-three first-Schur directions: 24 row-changing anti-diagonal
directions and 20 same-row sign directions.  For every unordered pair
((A,B)) of these directions, the exact characteristic-zero pencil
[
    P(t)=tA+B
]
has one of the following two behaviors:

* 102 pencils have rank at most three identically in (t);
* the remaining 844 pencils have no nonzero finite (t) with rank at most
  three.

There are no exceptional nonzero finite ratios.  The endpoints (t=0) and
(t=\infty) are the original two fixed directions and are not counted as
mixed pencils.

## Exact certificate

The script
[`n6_k32_two_line_pencil_classification.py`](../scripts/n6_k32_two_line_pencil_classification.py)
rebuilds the 44 integer (33\times15) matrices from N6-126 and processes all
(inom{44}{2}=946) pairs one at a time.

For a (4\times4) minor of (tA+B), the degree is at most three: the
constant term vanishes because (operatorname{rank}(B)=3), and the leading
term vanishes because (operatorname{rank}(A)=3).  Therefore five exact
sample values certify an identically rank-three pencil once all sampled ranks
are at most three.

If a sampled rank is at least four, a nonzero minor is selected by a modular
pivot certificate and then evaluated over (mathbb Q) by four-point
interpolation.  The gcd of these actual minors is sufficient: a constant gcd
(after removing the endpoint factor (t)) proves that no nonzero common root
can exist.  When a nonconstant candidate factor appears, the script checks
the corresponding rational root by an exact QQ rank and adds a new nonzero
minor if the root is spurious.  The final frozen payload is
[`n6_k32_two_line_pencil_classification.json`](../data/n6_k32_two_line_pencil_classification.json).

The replay output is:

```text
candidate_count=44
pair_count=946
identical=102
no_nonzero_root=844
exceptional_ratio_count=0
status=PASS
```

## Interpretation and boundary

This closes pairwise mixing among the already identified 44 torus-fixed
first-Schur rays at this chart.  It does not classify sums of three or more
weights, arbitrary invertible (6\times6) graph operators, or nonlinear lifts
away from the first-Schur chart.  In particular it does not prove ordinary
lower (29), exact ChowRank((\operatorname{perm}_6)=32), or any border-rank
statement.
