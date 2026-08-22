# A colored initial-module barrier for the lower-27 program

**Status.** `PURE_COMBINATORIAL_INEQUALITY`,
`EXACT_INTEGER_REPLAY`, `ABSTRACT_ROUTE_BARRIER` (G-036).
This note neither constructs a Chow decomposition nor proves lower 27.  The
ordinary interval remains

\[
26\leq\operatorname{ChowRank}(\operatorname{perm}_6)\leq32.
\]

## 1. The question

N6-032 and N6-037 force, under a hypothetical 26-term decomposition, a
twenty-term residual.  Its colored cubic relation space modulo
`E_3=D_3(perm_6)` has dimension at least 320.  In fact, because its image in
`E_3` contains `E_3\cap D_3(Q)`, the same colored kernel has dimension at
least 336.  The actual permanent incidence separately gives the strict
quadratic bound

Indeed, put `S=E_3\cap G_3` and choose a linear section `sigma:S->Sym^3(V*)`
of `C_(3,3)(Q)` over `S`.  Then

\[
s\longmapsto
\bigl(C_{3,3}(T_7)\sigma(s),\ldots,
C_{3,3}(T_{26})\sigma(s)\bigr)
\]

lands in the colored quotient kernel because its component sum is
`s\in E_3`; the same component-sum identity makes this map injective.  Hence
the colored kernel has dimension at least `dim S>=336`.

\[
\dim\overline{\mathcal K}_2\geq203.               \tag{1.1}
\]

Can retaining the twenty summand labels during a row-column torus
degeneration force a number strictly larger than 203?

The answer is negative for every argument that uses only:

1. twenty preserved labels;
2. cubic and quadratic projection caps 20 and 15 per label;
3. a 336-dimensional colored cubic relation space;
4. differentiation
   `K_3\subseteq K_2^(1)`;
5. hereditary central defect at most 16; and
6. coordinate-torus stability after degeneration.

The permanent's specific row-column weight multiplicities, apolar pairing,
and Chow realizability would have to enter any successful strengthening.

## 2. A capacity-constrained Macaulay calculation

For a quadratic subspace of dimension `q`, write

\[
M(q)=q^{\langle2\rangle}
\]

for its degree-two Macaulay successor.  If a coordinate initial module splits
over twenty labels and the cubic projection in each label has dimension at
most 20, then label `i` can contribute at most

\[
\min\{20,M(q_i)\}
\]

cubic dimensions when its quadratic relation component has dimension
`q_i`.  Therefore the strongest lower bound available from this split model
is the integer program

\[
\min\sum_{i=1}^{20}q_i
\quad\text{subject to}\quad
0\leq q_i\leq15,
\qquad
\sum_{i=1}^{20}\min\{20,M(q_i)\}\geq k.           \tag{2.1}
\]

Dynamic programming with exact integers gives:

| cubic target `k` | unrestricted minimum | minimum with every label active |
|---:|---:|---:|
| 320 | 160 | 163 |
| 336 | 169 | 171 |

For `k=336`, unrestricted equality is attained by

\[
(q_i)=(0,0,0,9,10,\ldots,10),                    \tag{2.2}
\]

with sixteen entries equal to 10.  If every label must be active, equality
171 is attained by

\[
(q_i)=(1,1,1,8,10,\ldots,10).                    \tag{2.3}
\]

Indeed

\[
M(1)=1,\qquad M(8)=13,\qquad M(9)=16,
\qquad M(10)=20.                                  \tag{2.4}
\]

Thus label capacity by itself is weaker than (1.1), not stronger.

### Why (2.1) is rigorous but conditional

Once a compatible initial module actually splits into the twenty label
coordinates, differentiation preserves the label, scalar Macaulay applies
inside every label, and summing the twenty bounds proves (2.1).  What is not
automatic is that a row-column degeneration of an arbitrary Chow
decomposition retains all the geometric information needed later.  Initial
limits may acquire new one-label intersections with the permanent space, and
row-column weight spaces outside `E_3` have multiplicity.  We therefore use
(2.1) only as a ceiling on the dimension-and-capacity argument.

## 3. An exact all-label coordinate model at 203

The preceding numerical optimum is realized by monomial prolongations.  Let
`V` have basis `x_0,x_1,x_2,x_3`.  For `q=1,8,9,10`, let `P_q` be the first
`q` quadratic monomials in descending lexicographic order.  Direct
enumeration gives

\[
\dim P_1^{(1)}=1,
\quad\dim P_8^{(1)}=13,
\quad\dim P_9^{(1)}=16,
\quad\dim P_{10}^{(1)}=20.                        \tag{3.1}
\]

Take twenty independent label coordinates and put

\[
K_2^{\rm min}
=P_1\oplus P_1\oplus P_1\oplus P_8
 \oplus P_{10}^{\oplus16},                        \tag{3.2}
\]

\[
K_3
=P_1^{(1)}\oplus P_1^{(1)}\oplus P_1^{(1)}
 \oplus P_8^{(1)}\oplus(P_{10}^{(1)})^{\oplus16}.
\tag{3.3}
\]

Then every label is active and

\[
\dim K_3=336,
\qquad
\dim K_2^{\rm min}=171,
\qquad
K_3\subseteq(K_2^{\rm min})^{(1)}.               \tag{3.4}
\]

Enlarge each of the last sixteen quadratic components by two unused
coordinate quadrics in a five-variable ambient space.  The resulting
coordinate module `K_2` satisfies

\[
\dim K_2=171+32=203,
\qquad
K_3\subseteq K_2^{(1)},                           \tag{3.5}
\]

and its largest label projection has dimension 12, below the one-term cap
15.  The largest cubic projection is 20.  Both spaces are fixed by the
coordinate torus.

To realize the quotient-language dimensions formally, use a five-variable
space for each label.  Let `U_i=Sym^3(k^4)` inside the first four variables,
viewed as an independent 20-dimensional cubic space containing the
corresponding projection of `K_3`, and put

\[
G_3=\bigoplus_{i=1}^{20}U_i.
\]

Thus `dim G_3=400`.  Let `W_i=Sym^2(k^5)` be the corresponding
15-dimensional quadratic label space and put `G_2=direct_sum_i W_i`; the
chosen `K_(2,i)` lies in `W_i`, and differentiating each displayed cubic
component lands in it.  If `F_3` is an external 64-space, define

\[
E_3=K_3\oplus F_3
\quad\text{inside}\quad G_3\oplus F_3.             \tag{3.6}
\]

Then `dim E_3=400`, `E_3\cap G_3=K_3`, and the kernel of
`G_3 -> (G_3+E_3)/E_3` is exactly the displayed 336-space.  Similarly, with
an external 22-space `F_2`, put `E_2=K_2\oplus F_2` inside `G_2\oplus F_2`;
this has dimension 225 and `E_2\cap G_2=K_2` has dimension exactly 203.
These are formal coordinate differential modules, not claimed polynomial
derivative spaces.

Every nonempty subset `I` of the independent `U_i` has

\[
\dim\sum_{i\in I}U_i=20|I|,                       \tag{3.7}
\]

so its central defect is zero, stronger than the required upper bound 16.
Consequently all the abstract label, capacity, hereditary-defect, torus, and
cross-degree conditions coexist with equality 203 in (1.1).

## 4. Exact conclusion and boundary

### Strict conclusion

No theorem of the following form can be true:

> preserved summand labels, per-label dimensions, a 336-dimensional cubic
> relation space, hereditary defect at most 16, coordinate initiality, and
> differentiation alone force more than 203 quadratic relations.

The module (3.2)--(3.6) is an exact characteristic-zero counterexample to
that abstract implication.

### What remains open

The displayed module is not a collection of Chow derivative spaces and is
not asserted to be realizable by a degeneration of twenty Chow terms.  It
does not reproduce the permanent's row-column weight multiplicities or its
perfect apolar pairings.  Hence it is not a counterexample to lower 27 and
does not rule out a stronger theorem using:

- the actual non-one-label support of quotient relations before
  degeneration;
- the six-factor Chow matroid in every label;
- the permanent's multiplicity-free `E_3` weights together with the
  higher-multiplicity ambient weight spaces;
- the relation pairing or a Fitting ideal of the factor-labelled cycles; or
- simultaneous compatibility with the six-term complement.

The practical consequence is that a further pure torus argument must prove
a geometric non-realizability statement for the equality-203 abstract
module.  Repeating Macaulay with label capacities cannot do so.

## 5. Replay

Run

```text
python scripts/n6_colored_initial_module_barrier.py \
  --json data/n6_colored_initial_module_barrier.json
python -m unittest tests/test_n6_colored_initial_module_barrier.py
```

The replay uses only exact integer enumeration.  It checks the four sharp
lex prolongations, solves both twenty-color integer programs, constructs the
all-label 336-to-203 profile, and verifies the per-label caps and hereditary
defect formula.  No finite-field or random calculation is used.
