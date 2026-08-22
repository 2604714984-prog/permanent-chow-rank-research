# A squarefree-coproduct colored barrier at the b=50 endpoint

**Status.** `PURE_SUPPORT_UPPER_BOUND + EXACT_MODULAR_RANK_CERTIFICATE`
(G-047), over \(\mathbb Q\).  This strengthens G-046: every color now uses
the canonical squarefree cubic coproduct.  The result remains a route
barrier, not an actual Chow or permanent configuration.

## 1. Six canonical color maps

Let \(U=\mathbb Q^6\), \(W=\bigwedge^2U\), and, for every color \(i\), use
the canonical coproduct

\[
 \Delta:\bigwedge^3U\longrightarrow U\otimes\bigwedge^2U,
 \qquad
 e_a\wedge e_b\wedge e_c\mapsto
 \sum_{x\in\{a,b,c\}}(\pm)e_x\otimes e_{\{a,b,c\}\setminus\{x\}}.
\tag{1.1}
\]

Choose six invertible integer maps \(q_i:W\to W\), and put

\[
 \beta_i=(1_U\otimes q_i)\Delta.
\tag{1.2}
\]

The frozen JSON records all ninety diagonal coefficients and five off-diagonal
shears.  In lexicographic pair order, every shear goes from a source pair to
a disjoint target pair.  Each \(q_i\) is upper triangular with nonzero
diagonal, hence is invertible over \(\mathbb Q\).

For a color set \(I\), define

\[
 S_I=\ker\left(\bigoplus_{i\in I}\bigwedge^3U
     \xrightarrow{\ \sum_i\beta_i\ }U\otimes W\right).
\tag{1.3}
\]

Thus the per-color differential is not arbitrary: it is exactly the
squarefree cubic-to-quadratic coproduct, followed by an invertible map on the
quadratic factor.

## 2. A pure rank-seventy upper bound

If all six \(q_i\) were diagonal, the combined image would lie in the sixty
coordinate axes \(e_a\otimes e_{bc}\) with distinct \(a,b,c\).  Consider a
shear from the source pair \(bc\) to a disjoint target pair \(de\).  Of the
four possible omitted indices outside \(bc\), the two indices outside
\(bcde\) give axes already in the diagonal support; only the target endpoints
\(d,e\) can give new axes.  Hence one shear introduces at most two new axes,
and five shears give

\[
 \operatorname{rank}_{\mathbb Q}\sum_{i=1}^6\beta_i\leq60+2\cdot5=70.
\tag{2.1}
\]

The exact modular calculation gives rank at least seventy over \(\mathbb Q\),
so equality holds and

\[
 \boxed{\dim S_{\{1,\ldots,6\}}=120-70=50.}
\tag{2.2}
\]

## 3. All subset caps

All 63 nonempty color subsets are checked.  In lexicographic subset order,
the modular nullities, hence upper bounds for their rational kernel
dimensions, are:

\[
\begin{array}{c|l|c}
|I|&\text{upper bound for }\dim_{\mathbb Q} S_I&\text{endpoint cap}\\ \hline
1&0,0,0,0,0,0&0\\
2&0\text{ for all 15 subsets}&2\\
3&0\text{ for all 20 subsets}&10\\
4&12,14,14,14,14,18,13,13,16,16,12,12,14,14,13&20\\
5&30,30,34,34,32,30&40\\
6&50&50.
\end{array}
\tag{3.1}
\]

Hence every recorded product-shadow subset cap at the last endpoint is
satisfied, even after imposing the canonical per-color coproduct.  For
\(|I|\leq3\) the zero upper bounds are exact.  The table does not claim that
the positive proper-subset upper bounds are equalities over \(\mathbb Q\).

The matrices have fixed integer entries.  Their ranks modulo
\(p=1{,}000{,}003\) are exact.  For an integer matrix,
\(\operatorname{rank}_{\mathbb Q}\geq\operatorname{rank}_{\mathbb F_p}\),
so every displayed modular nullity is a rational upper bound.  This direction
is sufficient for all subset caps.  For all six colors, it combines with the
pure support upper bound (2.1) to give the exact rational value fifty.

## 4. Strict conclusion and boundary

Canonical squarefree coproduct structure, invertible per-color quadratic
maps, and all known subset caps remain mutually consistent with a
fifty-dimensional total kernel.  Therefore these ingredients alone cannot
exclude the endpoint.

This is still **not** an actual six-term Chow configuration.  The six colors
abstractly identify the same \(U\).  They do not realize six pairwise
transverse ambient factor spaces \(L_i\), literal-direct quadratic Chow
spaces \(F_i\), or the common-section cocycle forced by a single permanent
quotient.  Those cross-color ambient constraints are precisely the missing
input.  The construction is not a 27-term decomposition and neither proves
nor refutes `ChowRank(perm_6)>=28`, the exact Chow rank, or any border-rank
statement.

```text
python scripts/n6_squarefree_coproduct_colored_barrier.py \
  --json data/n6_squarefree_coproduct_colored_barrier.json
python -m unittest tests.test_n6_squarefree_coproduct_colored_barrier -v
```
