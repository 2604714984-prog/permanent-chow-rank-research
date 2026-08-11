# A six-term counterexample to an unconditional central-radical cap

## Status and scope

`PROOF_DRAFT_COMPLETE`, `COMPUTATION_REPLAYED`, `ROUTE_DIAGNOSTIC`.

This note gives an exact characteristic-zero counterexample to the proposed
presentation-wise bound

\[
 \dim\operatorname{rad}(\beta|_R)\le 4(q-1)
\]

for a sum presented by `q` degree-six Chow terms.  The displayed six-term
presentation is **not** proved to be a minimum Chow decomposition.  Therefore
the result does not disprove a version of the bound that is restricted to
minimum decompositions.

It also disproves the more elementary proposal that the central radical is the
raw derivative shadow of the next relation space.

## 1. The six terms

Work over a field of characteristic zero with variables `x_0,...,x_9`.  For a
six-element set `A`, write `x_A=prod_(a in A) x_a`.  Let

\[
\begin{aligned}
A_1&=\{0,2,3,4,8,9\},&
A_2&=\{0,1,3,6,8,9\},\\
A_3&=\{0,4,6,7,8,9\},&
A_4&=\{0,2,3,6,7,9\},\\
A_5&=\{0,1,2,7,8,9\},&
A_6&=\{0,1,2,4,6,9\},
\end{aligned}
\]

and set

\[
 T_i=x_{A_i},\qquad f=\sum_{i=1}^6T_i.
\]

Each `T_i` is a squarefree degree-six Chow term.

## 2. The central relation space

Put `U_i=D_3(T_i)`.  It has the monomial basis

\[
 \{x_S:S\subset A_i,\ |S|=3\}
\]

and dimension 20.  Let

\[
 \sigma:\bigoplus_{i=1}^6U_i\longrightarrow
 \sum_{i=1}^6U_i,
 \qquad (u_i)_i\longmapsto\sum_i u_i,
 \qquad R=\ker\sigma.
\]

For each triple `S`, let `I_S={i:S subset A_i}`.  Because distinct monomials
are linearly independent, `R` is the direct sum over `S` of the zero-sum
spaces on `I_S`.  A basis is

\[
 e_{i,S}-e_{i_0,S}
 \quad (i\in I_S\setminus\{i_0\}).
\]

The multiplicity distribution of triples is

| multiplicity `|I_S|` | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| number of triples | 36 | 30 | 4 | 3 |

and hence

\[
 \rho:=\dim R=30+2\cdot4+3\cdot3=47.
\]

## 3. Exact restricted pairing rank

On each `U_i`, the middle catalecticant of `T_i` gives the nondegenerate
symmetric form

\[
 \beta_i(x_S,x_Q)=
 \begin{cases}
 1,&Q=A_i\setminus S,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Let `beta=direct_sum_i beta_i`.  In the preceding explicit 47-element basis of
`R`, the integer matrix of `beta|_R` has exact rational rank 24.  Fraction-free
elimination produces a 24 by 24 minor of determinant

\[
 256\ne0,
\]

and exact rational row reduction leaves exactly 24 pivots.  Thus both rank
inequalities are certified and

\[
 \boxed{\dim\operatorname{rad}(\beta|_R)=47-24=23.}
\]

Since `4(6-1)=20`, this proves

\[
 \boxed{23>20}
\]

and disproves the unconditional presentation-wise cap.

As a consistency check, the exact central identity from
`docs/general_relation_tableau_pairing.md` gives

\[
 \operatorname{rank}C_{3,3}(f)
 =6\cdot20-2\cdot47+24=50.
\]

Direct rational elimination of the 120 by 120 central catalecticant also gives
rank 50, with a displayed 50 by 50 minor of determinant `-256`.

## 4. The raw higher-relation shadow also fails

The fourth-derivative relation space is computed in the same monomial basis.
Its four-subset multiplicities are 60 labels of multiplicity one and 15 labels
of multiplicity two, so

\[
 \dim R_4=15.
\]

Differentiate its 15 basis relations by all variables.  The 60 nonzero
vectors obtained in `R` have exact span dimension 47.  Therefore their raw
derivative shadow is all of `R`, whereas the radical has dimension only 23.
Moreover, the shadow-to-`R` pairing matrix has rank 24.  Consequently

\[
 \partial R_4=R\ne\operatorname{rad}(\beta|_R).
\]

Any useful relation homology must therefore retain the pairing or a compatible
Koszul differential; quotienting by the raw derivative shadow loses all of
the central relation space in this example.

## 5. Why this is not yet a minimum-decomposition counterexample

All six supports contain `0` and `9`, so

\[
 f=x_0x_9g
\]

for an explicit sum `g` of six squarefree quartic monomials.  The exact middle
flattening of `g` has rank 18.  Since one quartic Chow term has middle rank at
most 6, this proves only

\[
 \operatorname{ChowRank}(g)\ge3.
\]

It does not prove `ChowRank(g)=6` or `ChowRank(f)=6`.  Searching for a
six-term presentation that is independently certified minimum and still has
radical dimension above 20 is outside the exact certificate in this note.

The surviving research question is therefore:

> Does a bound of the form
> `dim rad(beta|R) <= 4(q-1)` hold for a **minimum** degree-six Chow
> decomposition, or can a strictly certified minimum counterexample be found?

## 6. Reproduction

Run

```bash
python scripts/general_relation_radical_counterexample.py
python -m unittest tests.test_general_relation_radical_counterexample -v
```

The audit uses only the Python standard library.  All stated ranks use exact
`Fraction` elimination over `Q`; the reported nonzero minors are computed by
the fraction-free Bareiss algorithm.  No finite-field rank and no random
sample is used in the proof.
