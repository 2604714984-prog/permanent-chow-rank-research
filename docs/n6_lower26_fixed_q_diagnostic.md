# Fixed-count diagnostics for the `n=6` lower-26 problem

## Status

`COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`, `NO_FIXED_COUNT_SELECTED`.

The current in-repository theorem draft remains

\[
25
\le
\operatorname{ChowRank}(\operatorname{perm}_6)
\le
32.
\]

This note evaluates the exact arithmetic obtained from fixing six, seven, or
eight terms in a hypothetical 25-term decomposition. It does not exclude 25
terms and does not prove a lower bound of 26.

The deterministic replay is

```text
scripts/n6_lower26_fixed_q_diagnostic.py
```

and the compact frozen identity is

```text
data/n6_lower26_fixed_q_diagnostic.json
```

The script can optionally write the full layer and state tables with
`--full-json`; the frozen file binds those tables by canonical SHA-256 instead
of duplicating roughly one megabyte of generated rows.

## 1. Repository and proof boundary

This repository is the active pure-mathematics mainline. The diagnostic uses
the coupled catalectic of the fixed sum throughout. Literal sums of individual
derivative spaces occur only as ambient spaces and explicit relation modules.
No equality between a coupled image and an uncoupled sum is assumed.

The following prior results are inputs:

1. the individual quadratic intersection cap three;
2. the Bukh two-dimensional shadow inequality for permanent derivative
   spaces;
3. the vector-valued Macaulay theorem
   \[
   \dim\mathcal K^{(1)}\le(\dim\mathcal K)^{\langle2\rangle};
   \]
4. the block-Sylvester coupled middle-catalectic inequality;
5. the exact degree-six individual profile table; and
6. the quotient-Koszul residual inequality.

No new geometric classification, SAT layer, registry, or workflow abstraction
is introduced.

## 2. Hypothetical 25-term decomposition

Assume only for route analysis that

\[
P=\operatorname{perm}_6
=T_1+\cdots+T_{25}.
\]

Fix `q` terms, where

\[
q\in\{6,7,8\},
\]

and put

\[
R=T_1+\cdots+T_q,
\qquad
Q=P-R.
\]

At central degree three define

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

At quadratic degree define

\[
E_2=\mathcal D_2(P),
\qquad
G_i=\mathcal D_2(T_i),
\qquad
U=G_1+\cdots+G_q.
\]

The residual contains `25-q` terms.

## 3. Exact central state inequalities

The middle catalectic of `P` has rank 400, while the residual has central rank
at most

\[
20(25-q).
\]

The symmetric double-quotient inequality gives

\[
400+h-2b
\le
20(25-q).
\]

Therefore

\[
\boxed{
h\le2b+100-20q
}
\tag{3.1}
\]

and, since `h=b+d`,

\[
\boxed{
0\le d\le b+100-20q.
}
\tag{3.2}
\]

Also `h<=20q`. For one value of `b`, every initial integer state is therefore

\[
b\le h\le
\min\left(20q,\ 20(25-q)-400+2b\right).
\tag{3.3}
\]

Since `h>=b`, the central intersection lower endpoints are

\[
\begin{array}{c|ccc}
q&6&7&8\\
\hline
b_{\min}&20&40&60.
\end{array}
\tag{3.4}
\]

## 4. Exact Bukh shadow endpoints

The omitted-factor projection argument gives

\[
\boxed{
\dim(E_2\cap U)
\le
15(q-1)+3.
}
\tag{4.1}
\]

Thus the projection caps are 78, 93, and 108. For every relevant `b`, the
generator constructs rational lower and upper separators around the unique
real `x` satisfying

\[
\binom{x}{3}^2=b.
\]

The two separators prove the exact integer value

\[
m_b
=
\left\lceil\binom{x}{2}^2\right\rceil.
\]

The first excluded dimensions are:

| fixed terms `q` | projection cap | permitted `b` range | first excluded `b` | certified shadow |
|---:|---:|---:|---:|---:|
| 6 | 78 | `20..64` | 65 | 79 |
| 7 | 93 | `40..88` | 89 | 94 |
| 8 | 108 | `60..114` | 115 | 109 |

The compact payload binds all certificates for `20<=b<=115` by SHA-256.
No floating-point root or rounded decimal enters the result.

## 5. Full vector relation-module arithmetic

For one layer put

\[
D_b=15(q-1)+3-m_b.
\]

For every fixed term define

\[
\varepsilon_i=15-\dim G_i,
\qquad
\alpha_i=3-\dim(E_2\cap G_i).
\]

The omitted-factor projection inequalities are

\[
\sum_{i\ne j}\varepsilon_i+\alpha_j
\le D_b.
\tag{5.1}
\]

Let

\[
\mathcal K
=
\ker\left(
\bigoplus_{i=1}^qG_i
\longrightarrow U
\right),
\qquad
\kappa=\dim\mathcal K.
\]

Using only `alpha_i>=0`, equation (5.1) gives the conservative cap

\[
\boxed{
\kappa
\le
D_b-\sum_i\varepsilon_i+\min_i\varepsilon_i.
}
\tag{5.2}
\]

The cubic relation module has dimension at most

\[
\kappa^{\langle2\rangle}.
\]

For the individual middle-catalectic ranks, the diagnostic uses exactly the
previous conservative table:

\[
\begin{array}{c|rrrrrr}
\dim\mathcal D_2(T)&10&11&12&13&14&15\\
\hline
\dim\mathcal D_3(T)\text{ lower bound}
&0&14&\text{impossible}&18&20&20.
\end{array}
\tag{5.3}
\]

Every dimension below ten also receives lower bound zero. The zero entries are
intentional; unresolved low profiles cannot create a false exclusion.

For every nondecreasing epsilon type satisfying (5.1), the generator computes

\[
h
\ge
\sum_i c_i
-
2\kappa^{\langle2\rangle}.
\tag{5.4}
\]

It also verifies the finite colored-partition interface

\[
\max_{k_1+\cdots+k_q=k}
\sum_i k_i^{\langle2\rangle}
=
k^{\langle2\rangle}
\]

through `k=37` for `q=6` and through `k=33` for `q=7,8`.

## 6. Quotient-Koszul route labels

The residual first-Koszul capacity is

\[
705(25-q).
\]

For one state, the residual lower bound is

\[
14175-36b+\Gamma.
\]

The minimum quotient gain needed for strictness is therefore

\[
\boxed{
g_{\mathrm{req}}
=
\max\left(
0,
705(25-q)+1-(14175-36b)
\right).
}
\tag{6.1}
\]

The quotient dimension is `d`, so the elementary maximum gain is `36d`.
Every state receives exactly one label:

1. `vector_macaulay_central_exclusion` if its `h` is below (5.4);
2. `quotient_koszul_already_strict` if `g_req=0`;
3. `structural_exclusion_or_stronger_invariant_required` if
   `36d<g_req`; or
4. `relative_prolongation_cap_can_close` otherwise, with sufficient cap
   \[
   p\le36d-g_{\mathrm{req}}.
   \]

No state is removed by an unstated realizability assumption.

## 7. Exact result

| `q` | initial states | central exclusions | survivors | already Koszul-strict | relative-cap states | structural states |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 1,035 | 708 | 327 | 3 | 55 | 269 |
| 7 | 1,225 | 870 | 355 | 3 | 62 | 290 |
| 8 | 1,520 | 885 | 635 | 1 | 50 | 584 |

Additional exact boundaries are:

| `q` | surviving `b` range | maximum relation cap | sufficient relative caps | fully central-excluded layers |
|---:|---:|---:|---:|---:|
| 6 | `20..50` | 37 | 23 in 26 states; 59 in 29 states | 14 |
| 7 | `40..72` | 33 | 8 in 31 states; 44 in 31 states | 16 |
| 8 | `60..114` | 33 | 29 in 50 states | 0 |

For `q=8`, even the top shadow-permitted layer survives: at `b=114`, the
conservative coupled lower bound and the fixed-sum capacity both equal 160.
Thus increasing the fixed count does not produce a monotone improvement.

## 8. Route decision

Six fixed terms are arithmetically smallest, but the result is not a compact
frontier:

```text
surviving states: 327
structural states: 269
maximum quadratic relation cap: 37
```

Seven fixed terms are slightly worse, and eight fixed terms are substantially
worse. No value of `q` is selected for a lower-26 proof program.

This is stronger than a raw state-count objection. In the 31 surviving
six-fixed `b` layers, the all-full-profile epsilon vector is the unique
central-rank minimizer in 29 layers and tied in the other two. For seven fixed
terms it is unique in 30 surviving layers and tied in three. Therefore merely
classifying the currently unresolved quadratic profiles below dimension 11
cannot remove the broad six- or seven-fixed frontier.

### Diagnostic conclusion

\[
\boxed{
\text{The central first-Koszul fixed-count route is suspended for lower 26.}
}
\]

The diagnostic does not authorize a state registry, SAT/DRAT expansion, or a
large geometric classification.

## 9. Hidden assumptions

A continuation of this route would require all of the following:

1. hundreds of structural states collapse under one new invariant;
2. relation spaces as large as 33--37 admit a useful uniform refinement;
3. block-Sylvester is not too far below the true coupled rank;
4. quotient gain can be controlled simultaneously across many `d` values;
5. there is no 25-term decomposition.

None is established here.

## 10. Assume every assumption is false

Then the lower bound 25 is a natural saturation point for the present central
first-Koszul method. The next small experiment should compare, without a new
workflow layer:

- a higher Koszul flattening;
- a coupled first- and second-shadow inequality;
- a different derivative output degree; and
- exact structured decomposition search.

Only a route with a strict global numerical margin should be promoted.

## 11. Strongest objection to the stopping decision

The diagnostic remains conservative. It ignores some Chow-realizability
constraints, uses zero central lower bounds for all quadratic dimensions at
most ten, and replaces the actual relation module by its dimension cap. A new
bulk theorem could therefore eliminate many states at once.

That objection did not justify extending the state table. N6-030 later supplies
the missing bulk step by averaging over six-subsets and proves the ordinary
lower bound 26 without resolving the surviving arbitrary-subset states one by
one.

## 12. Reproduction

Run

```bash
python scripts/n6_lower26_fixed_q_diagnostic.py \
  --json /tmp/n6_lower26_fixed_q_diagnostic.json
python -m unittest tests.test_n6_lower26_fixed_q_diagnostic -v
```

To inspect the complete generated tables, add

```bash
--full-json /tmp/n6_lower26_fixed_q_diagnostic_full.json
```

Expected marker:

```text
N6_LOWER26_FIXED_Q_DIAGNOSTIC_PASS
```
