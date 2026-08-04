# Fixed-`q` diagnostics for the `n=6` lower-25 problem

## Status

`COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

The current theorem in this repository is

\[
24
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

This note tests whether the fixed-term arithmetic that excluded 23 terms can
be extended directly to exclude 24 terms. It does not prove a lower bound of
25.

The exact replay is

```text
scripts/n6_lower25_fixed_q_diagnostic.py
```

with a frozen state-summary identity in

```text
data/n6_lower25_fixed_q_diagnostic.json
```

## 1. Hypothetical 24-term decomposition

Assume only for route analysis that

\[
P=\operatorname{perm}_6
=T_1+\cdots+T_{24}.
\]

Fix `q` terms, where

\[
q\in\{4,5,6\},
\]

and write

\[
R=T_1+\cdots+T_q,
\qquad
Q=P-R.
\]

At central degree three put

\[
E_3=\mathcal D_3(P),
\qquad
H_3=\mathcal D_3(R),
\]

\[
b=\dim(E_3\cap H_3),
\qquad
h=\dim H_3,
\qquad
d=h-b.
\]

At quadratic degree put

\[
E_2=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+\cdots+G_q.
\]

The calculation uses only inequalities already proved in the repository and
their direct fixed-`q` extensions.

## 2. Central-catalectic state inequalities

The middle catalectic of `P` has rank 400. The residual has `24-q` terms and
therefore central rank at most

\[
20(24-q).
\]

The symmetric double-quotient inequality gives

\[
400+h-2b
\le
20(24-q).
\]

Hence

\[
\boxed{
h\le2b+80-20q
}
\tag{2.1}
\]

and

\[
\boxed{
0\le d\le b+80-20q.
}
\tag{2.2}
\]

Also `h<=20q`. Thus, for one `b`,

\[
0\le d\le
\min(20q-b,\ b+80-20q).
\tag{2.3}
\]

In particular, the central intersection must satisfy

\[
b\ge\max(0,20q-80).
\tag{2.4}
\]

## 3. Exact shadow certificates

The omitted-factor projection cap is

\[
\boxed{
\dim(E_2\cap U)
\le
15(q-1)+3.
}
\tag{3.1}
\]

The generator stores exact rational separators for every

\[
1\le b\le65.
\]

For a recorded pair `(x,m)`, it verifies

\[
\binom{x}{3}^2\le b,
\qquad
\binom{x}{2}^2>m-1.
\]

Bukh shadow monotonicity then gives the integer lower bound

\[
\dim\partial S\ge m
\]

for every `b`-dimensional

\[
S\subseteq\mathcal D_3(\operatorname{perm}_6).
\]

The endpoint certificates relevant to the fixed-`q` ranges are:

| `q` | projection cap | first excluded `b` | certified shadow |
|---:|---:|---:|---:|
| 4 | 48 | 28 | 49 |
| 5 | 63 | 45 | 64 |
| 6 | 78 | 65 | 79 |

Therefore the exact arithmetic ranges are

\[
\begin{array}{c|c}
q&b\text{ range}\\
\hline
4&0\le b\le27,\\
5&20\le b\le44,\\
6&40\le b\le64.
\end{array}
\tag{3.2}
\]

## 4. Componentwise central-rank exclusions

For a certified quadratic shadow lower bound `m`, define

\[
\varepsilon_i=15-\dim G_i,
\qquad
\alpha_i=3-\dim(E_2\cap G_i).
\]

The omitted-factor inequalities become

\[
\sum_{i\ne j}\varepsilon_i+\alpha_j
\le
15(q-1)+3-m.
\tag{4.1}
\]

For fixed `epsilon`, setting every `alpha_i=0` maximizes the available
quadratic relation-kernel cap and therefore gives the weakest certified
central-rank lower bound. The diagnostic consequently optimizes exactly over
the feasible labelled `epsilon` profiles whenever this arithmetic can
exclude at least the state `h=b`.

It uses the same conservative individual profile table as the lower-24
proof:

\[
\begin{array}{c|rrrrrr}
\dim\mathcal D_2(T)&10&11&12&13&14&15\\
\hline
\dim\mathcal D_3(T)\text{ lower bound}
&0&14&\text{impossible}&18&20&20.
\end{array}
\tag{4.2}
\]

The zero at quadratic dimension ten is intentional. It prevents the
diagnostic from claiming any unproved classification at that profile.

If the quadratic relation kernel has dimension at most `kappa`, the
componentwise Macaulay theorem gives a cubic relation-kernel cap

\[
(q-1)\kappa^{\langle2\rangle}.
\]

The block-Sylvester inequality then gives

\[
\operatorname{rank}C_{3,3}(R)
\ge
\sum_i\dim\mathcal D_3(T_i)
-
2(q-1)\kappa^{\langle2\rangle}.
\tag{4.3}
\]

When the feasible all-zero profile already has a lower bound at most `b`,
the script returns zero rather than performing a broad enumeration. This is
fail-closed: it weakens the diagnostic and cannot create a false exclusion.

## 5. Quotient-Koszul route labels

The residual has `24-q` terms, so its first-Koszul capacity is

\[
705(24-q).
\]

The exact residual lower bound remains

\[
14175-36b+\Gamma.
\]

Thus the quotient gain required for strictness is

\[
\boxed{
g_{\mathrm{req}}
=
705(24-q)+1-(14175-36b).
}
\tag{5.1}
\]

Since the quotient dimension is `d`, the elementary maximum gain is `36d`.
Every state receives exactly one label:

1. `component_central_rank_exclusion` if `h` is below the certified
   component lower bound;
2. `quotient_koszul_already_strict` if `g_req<=0`;
3. `structural_exclusion_or_stronger_invariant_required` if
   `36d<g_req`;
4. `relative_prolongation_cap_can_close` otherwise, with sufficient cap
   \[
   p\le36d-g_{\mathrm{req}}.
   \]

No geometric state is deleted without one of these explicit inequalities.

## 6. Exact results

### Four fixed terms

```text
b range:                         0..27
states before central pruning:    406
component-central exclusions:     146
surviving states:                 260
automatic Koszul states:            6
relative-prolongation states:      60
structural states:                194
sufficient p caps:               2, 38, 74
```

Each displayed `p` cap occurs in 20 states.

### Five fixed terms

```text
b range:                        20..44
states before central pruning:    325
component-central exclusions:     141
surviving states:                 184
automatic Koszul states:            3
relative-prolongation states:      34
structural states:                147
sufficient p caps:              23, 59
```

Each displayed `p` cap occurs in 17 states.

### Six fixed terms

```text
b range:                        40..64
states before central pruning:    325
component-central exclusions:     146
surviving states:                 179
automatic Koszul states:            3
relative-prolongation states:      35
structural states:                141
sufficient p caps:               8, 44
```

The cap 8 occurs in 17 states and the cap 44 in 18 states.

## 7. Route decision

Among `q=4,5,6`, six fixed terms leave the fewest states:

\[
179.
\]

They also leave the fewest structural states:

\[
141.
\]

This is not a usable finite proof frontier. The improvement over five fixed
terms is only five surviving states and six structural states, while the
six-fixed relative-prolongation caps

\[
8,\ 44
\]

are stricter than the five-fixed caps

\[
23,\ 59.
\]

Therefore the diagnostic does **not** select `q=6` as the next proof
program.

### Diagnostic conclusion

\[
\boxed{
\text{The lower-24 proof does not extend mechanically to lower 25.}
}
\]

None of the tested fixed-term counts is promoted beyond
`ROUTE_DIAGNOSTIC`.

## 8. Hidden assumptions

The fixed-`q` route would need all of the following to be favorable:

1. state count is a useful proxy for geometric complexity;
2. a uniform relative-prolongation theorem can reach the displayed caps;
3. the structural states share a small number of Chow-realizable profiles;
4. increasing `q` does not make the coupled relation geometry harder faster
   than it improves the arithmetic;
5. there is no 24-term decomposition.

The diagnostic proves none of these assumptions.

## 9. Assume every assumption is false

Then choosing `q=6` from its state count would be a category error. The
correct next step is not a larger state registry. It is one of:

- derive a stronger invariant that acts on many structural states at once;
- exploit more information about the projections of the quadratic relation
  kernel, rather than only its dimension;
- combine first and second derivative shadows;
- search exactly for structured decompositions with at most 24 terms;
- change flattening.

No SAT/DRAT or Hilbert-scheme layer is justified by the current output.

## 10. Strongest objection to the route decision

The arithmetic deliberately ignores some Chow-realizability restrictions
and assigns central rank zero to all quadratic profiles of dimension at most
ten. Therefore the 179-state count can substantially overstate the true
frontier.

That objection does not support promoting `q=6`. It means that the next
research result must be a structural theorem reducing the states in bulk.
Without such a theorem, expanding the enumeration would add complexity
without a credible path to a lower bound of 25.

## 11. Claim boundary

This note does not exclude a 24-term decomposition and does not prove

\[
\operatorname{ChowRank}(\operatorname{perm}_6)\ge25.
\]

It also does not change the certified interval

\[
24
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

## 12. Reproduction

Run

```bash
python scripts/n6_lower25_fixed_q_diagnostic.py \
  --json /tmp/n6_lower25_fixed_q_diagnostic.json
python -m unittest tests.test_n6_lower25_fixed_q_diagnostic -v
```

Expected compact output contains

```text
"fewest_surviving_states_fixed_terms": 6
"fewest_surviving_states": 179
"fewest_structural_states": 141
N6_LOWER25_FIXED_Q_DIAGNOSTIC_PASS
```
