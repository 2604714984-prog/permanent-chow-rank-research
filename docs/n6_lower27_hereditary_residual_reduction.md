# A hereditary central-minimal residual forced by twenty-six terms

**Status.** `PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`,
`LOWER_27_REDUCTION` (N6-032).  The base field has characteristic zero.
This note proves a necessary consequence of a hypothetical 26-term
decomposition of `perm_6`; it does not exclude such a decomposition.

## 1. The reduction theorem

Put

\[
 P=\operatorname{perm}_6,
 \qquad E=\mathcal D_3(P),
 \qquad \dim E=400.
\]

### Theorem 1.1

If

\[
 P=T_1+\cdots+T_{26}                              \tag{1.1}
\]

is a Chow decomposition, then six indices can be chosen so that, after
renumbering and putting

\[
 H=\mathcal D_3(T_1+\cdots+T_6),
 \qquad
 Q=T_7+\cdots+T_{26},
\]

one has

\[
 \boxed{\operatorname{rank}C_{3,3}(Q)\ge384.}     \tag{1.2}
\]

Consequently the displayed twenty-term expression for `Q` is minimum and is
hereditarily central-minimum: for every nonempty subset
`S subseteq {7,...,26}` of size `s`,

\[
 \boxed{
 \operatorname{rank}C_{3,3}\left(\sum_{i\in S}T_i\right)
 \ge20s-16>20(s-1).
 }                                                  \tag{1.3}
\]

In particular,

\[
 \operatorname{ChowRank}\left(\sum_{i\in S}T_i\right)=s.   \tag{1.4}
\]

For every such subset, the radical of the central relation pairing has
dimension at most nine.  At least twelve of the twenty residual terms have
individual middle-catalectic rank 20.

## 2. The maximum individual middle rank is 20

Write

\[
 A_i=C_{3,3}(T_i),\quad U_i=\operatorname{im}A_i,quad
 r_i=\dim U_i,quad r=\max_i r_i,
\]

and

\[
 D=\dim\sum_iU_i,qquad R=\sum_i r_i.
\]

Every `U_i` is disjoint from `E`, by the essential-variable theorem for
cubics in `E`.  If `r_j=r`, then `D>=400+r`.  Put

\[
 D=400+z.                                          \tag{2.1}
\]

Thus `z>=r`.  Let `rho` be the relation dimension among the `U_i`, and let
`tau` be the rank of the central relation pairing.  The exact relation-pairing
identity gives

\[
 400=R-2\rho+\tau,qquad \rho=R-D,
\]

and hence

\[
 \boxed{R=400+2z+\tau.}                            \tag{2.2}
\]

Since `R<=26r`, equations (2.1)--(2.2) imply `r>=17`.

The single-term profile theorem used below is:

\[
\begin{array}{c|ccccc}
\dim\mathcal D_2(T)&11&12&13&14&15\\ \hline
\text{possible?}&\text{yes}&\text{no}&\text{yes}&\text{yes}&\text{yes}\\
\dim\mathcal D_3(T)\text{ lower}&14&-&18&20&20.
\end{array}                                         \tag{2.3}
\]

If the factor span has dimension at most four, the quadratic dimension is at
most ten.  N6-031 additionally proves that middle rank 19 never occurs.

Fix a maximum-rank term and conditionally average over six-subsets containing
it.  The same submodular argument as N6-030 gives a six-subset with coupled
middle rank `h` satisfying

\[
 h\ge r+\frac5{25}(2D-R-r)
 \ge160-4r.                                        \tag{2.4}
\]

Let

\[
 b=\dim(E\cap H).
\]

The other twenty terms have middle rank at most 400.  The symmetric
double-quotient inequality gives `h<=2b`.

If `r=17`, (2.3) gives `dim D_2(T_i)<=11` for every term.  Equation (2.4)
gives `h>=92`, hence `b>=46`.  The quadratic projection cap for six fixed
terms is therefore at most

\[
 5\cdot11+3=58,                                    \tag{2.5}
\]

whereas the exact Bukh shadow of a 46-dimensional subspace of `E` is at
least 65.  This is impossible.

If `r=18`, then (2.3) gives the individual quadratic cap 13 and hence the
fixed-six projection cap

\[
 5\cdot13+3=68.                                    \tag{2.6}
\]

Moreover (2.2) and `R<=26*18=468` give `z<=34`.  Equation (2.4) gives
`h>=88`.  Since `E+H` is contained in the total literal span,

\[
 h-b=\dim(E+H)-400\le z,                           \tag{2.7}
\]

so `b>=54`.  Its exact quadratic shadow is at least 71, contradicting
(2.6).

There is no rank-19 term by N6-031.  Therefore

\[
 \boxed{r=20.}                                     \tag{2.8}
\]

## 3. Selecting the residual

With `r=20`, use (2.2) in the conditional average.  Some six-subset satisfies

\[
 h\ge20+\frac15(2D-R-20)
 =96-\frac{\tau}{5}.                               \tag{3.1}
\]

Because `R<=520`, (2.2) gives

\[
 \tau\le120-2z.                                    \tag{3.2}
\]

Equations (2.7), (3.1), and (3.2) imply

\[
 h\ge72+\frac25z
 \ge72+\frac25(h-b),
\]

or equivalently

\[
 \boxed{h\ge120-\frac23b.}                        \tag{3.3}
\]

The shadow cap for six fixed terms gives `b<=64`, since the exact shadow at
`b=65` is 79 while the quadratic projection cap is 78.

We claim

\[
 h\ge2b-16.                                        \tag{3.4}
\]

For `b<=51`, this follows immediately from (3.3).  For `52<=b<=64`, the exact
fixed-six vector-Macaulay calculation gives:

\[
\begin{array}{c|rrrrrrrrrrrrr}
b&52&53&54&55&56&57&58&59&60&61&62&63&64\\ \hline
h\text{ lower}&88&92&96&98&98&100&110&112&112&116&118&118&120\\
2b-16&88&90&92&94&96&98&100&102&104&106&108&110&112.
\end{array}                                         \tag{3.5}
\]

Every entry is regenerated by exact rational shadow separators and integer
Macaulay arithmetic.

Now `P=Q+(T_1+...+T_6)`.  The symmetric double-quotient inequality and
(3.4) yield

\[
\begin{aligned}
\operatorname{rank}C_{3,3}(Q)
&\ge400+h-2b\\
&\ge384,
\end{aligned}
\]

which proves (1.2).

## 4. Hereditary central minimality

Let `S` be any `s` of the twenty displayed residual terms.  The complement
inside `Q` is a sum of `20-s` Chow terms and has middle rank at most
`20(20-s)`.  Rank subadditivity applied to `Q` gives

\[
\begin{aligned}
\operatorname{rank}C_{3,3}\left(\sum_{i\in S}T_i\right)
&\ge384-20(20-s)\\
&=20s-16.
\end{aligned}                                       \tag{4.1}

This is strictly larger than `20(s-1)`, so the displayed `s`-term expression
is minimum and is certified by the middle catalectic itself.  The central
minimality radical theorem then gives radical dimension at most

\[
 \left\lfloor\frac{20-1}{2}\right\rfloor=9.
\]

Finally, (1.2) implies that the sum of the twenty individual middle ranks is
at least 384.  N6-031 says every non-full term loses at least two from the
cap 20.  Total deficit is at most 16, so at most eight terms are non-full;
at least twelve have middle rank 20.  This finishes the proof.

## 5. Reproduction and boundary

Run

```text
python scripts/n6_lower27_hereditary_residual_audit.py \
  --json data/n6_lower27_hereditary_residual_audit.json
python -m unittest tests/test_n6_lower27_hereditary_residual.py
```

The script replays (2.3), the shadow endpoints 65 and 71, the rank-19 gap
interface, and all thirteen rows of (3.5), using only exact integer/rational
arithmetic.

The remaining problem is geometric: exclude a twenty-term residual whose
every sub-sum is centrally certified minimum, whose full middle rank is at
least 384, which contains at least twelve full-rank Chow terms, and which is
the difference of `perm_6` and six Chow terms.  None of the current scalar
shadow or submodular inequalities excludes this structure.  Therefore N6-032
is not a lower-27 theorem and makes no border-rank claim.
