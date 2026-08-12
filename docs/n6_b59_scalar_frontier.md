# The complete scalar frontier at `b=59`

**Status.** `PURE_INTEGER_STATE_ENUMERATION`, `EXACT_REPLAY`,
`ALL_ALPHA3_FRONTIER_REDUCTION` (N6-054). The base field is algebraically
closed of characteristic zero. Conditional on the fixed-six reduction of a
hypothetical twenty-six-term decomposition, this note reduces the complete
`b=59` scalar necessary-state layer to one all-alpha-three state. It does not
exclude that state or prove `ChowRank(perm_6)>=27`.

## 1. Inherited scalar constraints

For `b=59`, the exact N6-038 shadow certificate is

\[
 m_{59}=75,
 \qquad D_{59}=78-m_{59}=3.
\]

Consequently the omitted-factor, projection, relation, and individual
quotient inequalities are exactly the `D=3` inequalities displayed in
N6-050. The replay imports the already audited exhaustive integer generator,
but independently reads N6-038 and refuses to run unless the inherited values
are exactly `m_59=75` and `D_59=3`. All 367 resulting rows are stored in the
JSON certificate with new `b59_state_*` identifiers.

The exact histograms are

\[
 \#\{\kappa_2=0,1,2,3\}=(294,62,10,1),
\]

\[
 \#\{t_2=12,13,14,15\}=(32,111,140,84).
\]

For `kappa_2<=2`, the cube/binary-cubic obstruction of N6-025 and N6-050
proves directness of the cubic derivative spaces. The unique `kappa_2=3`
state is

\[
 ((\varepsilon_i,\alpha_i))=((0,0))^6,
 \quad(d_2,a_2,t_2)=(87,75,12),
\]

and is recorded honestly with only

\[
 112\le h\le120.
\]

Its prolongation lower bound is already

\[
 400+112-59=453>436,
\]

so N6-047 excludes it without choosing an unproved exact value of `h`.

## 2. Complete pruning by proved term caps

For every state, with `A=E_2+H_2`,

\[
 E_3+H_3\subseteq A^{(1)},
 \qquad\dim A^{(1)}\ge400+h-59.
\]

Applying only caps in their proved quotient dimensions gives the disjoint
partition

| certificate | excluded states |
|---|---:|
| N6-047 extremal, `t=12,13,14` | 226 |
| N6-048 alpha one, `t=13,14` | 51 |
| N6-049 alpha two, `t=14` | 6 |
| N6-051 extremal, `t=15` | 56 |
| N6-051 alpha one, `t=15` | 21 |
| N6-052 alpha two, `t=15` | 6 |
| not excluded | 1 |

The sole survivor is

```text
b59_state_366
```

with

\[
 ((\varepsilon_i,\alpha_i))=((0,3))^6,
 \qquad(d_2,a_2,t_2)=(90,75,15),
 \qquad h=120.
\]

It requires

\[
 \dim A^{(1)}\ge400+120-59=461.
\]

G-042 proves that a universal individual alpha-three prolongation cap cannot
exclude this state; a genuinely coupled six-term argument is still required.

## 3. Claim boundary and replay

This is a complete scalar **necessary-state** enumeration, not a geometric
realizability classification. It does not exclude the all-alpha-three state,
the `b=59` layer, a hypothetical twenty-six-term decomposition, prove
`ChowRank(perm_6)>=27`, or make a border-rank claim.

```text
python scripts/n6_b59_scalar_frontier.py --json data/n6_b59_scalar_frontier.json
python -m unittest tests.test_n6_b59_scalar_frontier -v
```
