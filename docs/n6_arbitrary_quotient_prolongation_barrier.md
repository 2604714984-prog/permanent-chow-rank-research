# An arbitrary thirteen-plane defeats dimension-only prolongation

**Status.** `PURE_EXPLICIT_COUNTEREXAMPLE`, `EXACT_QQ_REPLAY`,
`ROUTE_BARRIER` (G-041).  This note shows that no theorem depending only on

\[
 E_2\subset A,
 \qquad \dim(A/E_2)=13
\]

can force `dim A^(1)<457`.  It does not contradict the extremal-containing
caps of N6-047 or the actual `alpha=1` closure theorem of N6-048.

## 1. The explicit quotient thirteen-plane

Use the five variables

\[
 x_{00},x_{02},x_{03},x_{04},x_{05}
\]

in row zero.  Let `W` be spanned in `Sym^2 V/E_2` by:

1. all ten pair products of distinct variables in this list; and
2. the three square axes
   \[
   x_{02}^2,\quad x_{03}^2,\quad x_{04}^2.
   \]

These are thirteen distinct same-row or square quotient axes, so

\[
 \dim W=13.
\]

Put

\[
 A=E_2+W.
\]

## 2. Exact prolongation dimension

The coefficient equations defining

\[
 A^{(1)}={g\in\operatorname{Sym}^3V:
 \partial_\xi g\in A\text{ for all }\xi\in V^*\}
\]

split into the `3136` row-column weight blocks used in N6-047.  Starting from

\[
 \dim E_2^{(1)}=\dim E_3=400,
\]

the thirteen displayed quotient directions increase the nullity in exactly
75 blocks, by one in each block.  Therefore

\[
 \boxed{\dim A^{(1)}=400+75=475.}
\tag{2.1}

The replay establishes (2.1) twice:

- direct Gaussian elimination over `Fraction` computes every relevant block
  rank over the rationals;
- reduction modulo the prime `1000003` independently returns the same 475.

The equality in characteristic zero comes from the rational computation; no
finite-field equality is extrapolated.

In particular,

\[
 475>457.
\]

Thus the proposed dimension-only bound

\[
 \dim A^{(1)}<457
 \quad\text{for every }A/E_2\text{ of dimension }13
\]

is false.

## 3. Exact boundary

This example is an arbitrary coordinate thirteen-plane in the quadratic
quotient.  It is **not** asserted to be the common quadratic quotient of six
actual Chow terms with `(epsilon,alpha)=(0,1)`.  Consequently it does not
prove that an all-`alpha=1` fixed-six state is realizable.

It also does not contradict N6-047.  That theorem assumes the ambient
quadratic space contains the quotient of an actual extremal term and obtains
its caps on that strictly smaller incidence.  N6-048 obtains a universal
`alpha=1` cap by retaining the closure geometry of an actual Chow term,
which this arbitrary thirteen-plane ignores.

The conclusion is only:

> after forgetting Chow realizability and retaining only
> `dim(A/E_2)=13`, scalar prolongation dimension is too large to exclude the
> remaining states.

## 4. Replay

Run

```text
python scripts/n6_arbitrary_quotient_prolongation_barrier.py \
  --json data/n6_arbitrary_quotient_prolongation_barrier.json
python -m unittest tests/test_n6_arbitrary_quotient_prolongation_barrier.py -v
```

Expected outputs include

```text
selected_axis_count=13
changed_cubic_weight_block_count=75
exact_QQ_prolongation_dimension=475
modular_regression_prolongation_dimension=475
strict_excess_over_457=18
N6_ARBITRARY_QUOTIENT_PROLONGATION_BARRIER_PASS
```
