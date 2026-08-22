# N6-138: same-target rank-one quadratic diagnostic

**Status.** `EXACT_QQ_SAME_TARGET_RANK_ONE_QUADRATIC_DIAGNOSTIC` in
characteristic zero.

This is the remaining rank-one support type not covered by the complete
two-branch germ statement N6-137.

## Exact quadratic support

At the finite pair \(L=\operatorname{graph}(D)\),
\(M=\operatorname{graph}(-D)\), where \(D\) has one target-row block
\(\left[\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\right]\), the exact Schur
Jacobian has shape \(360\times72\), rank \(64\), and kernel dimension \(8\).
The quadratic initial generators are

\[
 x_3(x_0-x_2),\ x_4(x_0-x_2),\ x_1x_3,\ x_1x_4,
 x_1x_6,\ x_1x_7,\ x_3x_4,\ x_3x_5,\ x_3x_6,\ x_3x_7,
 x_4^2,\ x_4x_5,\ x_4x_6,\ x_4x_7,\ x_5x_6,\ x_5x_7.
\]

The radical has three linear components:

\[
\begin{aligned}
P_1&=(x_4,x_3,x_1,x_5),\\
P_2&=(x_4,x_3,x_6,x_7),\\
P_3&=(x_4,x_0-x_2,x_1,x_5,x_6,x_7).
\end{aligned}
\]

Indeed, \(x_4^2\) gives \(x_4=0\). On the locus \(x_3=0\), the remaining
graph ideal is the four-cycle on \(\{x_1,x_5,x_6,x_7\}\), whose minimal
coordinate covers are \(\{x_1,x_5\}\) and \(\{x_6,x_7\}\). On the other
locus \(x_3\ne0\), the factor \(x_3(x_0-x_2)\) gives \(x_0=x_2\), and
the four edges incident to \(x_3\) force
\(x_1=x_5=x_6=x_7=0\), giving \(P_3\).

## Straight branch check

Substitution into the full cross matrix gives generic cross ranks

\[
 6,\ 6,\ 6
\]

for \(P_1,P_2,P_3\). Their generic operator ranks are \(1,2,1\), hence the
corresponding sums have ranks \(7,8,7\). All three straight branches are
therefore noncomplementary.

This remains a quadratic support diagnostic rather than a complete germ
theorem: it does not rule out higher-order nonlinear lifts outside these
quadratic components or in other charts.

## Boundary

The certificate does not cover higher-order nonlinear lifts outside this
quadratic support, non-graph charts, coupled six-term cocycles, the full
\(K_{3,2}/K_{2,3}\) normal cone, ordinary lower 29, exact
\(\operatorname{ChowRank}(\operatorname{perm}_6)\), or border rank.

Replay:

```text
python scripts/n6_k32_same_target_rank_one_quadratic_diagnostic.py --verify-json data/n6_k32_same_target_rank_one_quadratic_diagnostic.json
python -m unittest tests.test_n6_k32_same_target_rank_one_quadratic_diagnostic -v
```
