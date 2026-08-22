# Coordinate regular first-order closure at the quartic six-block frontier

## Status and claim boundary

`PROOF_DRAFT_COMPLETE`, `CHARACTERISTIC_ZERO`,
`EXACT_FINITE_INTERFACES_REPLAYED`,
`RESTRICTED_COORDINATE_REGULAR_FIRST_ORDER_ZERO`.

Work in one fixed `4 x 4` variable block. Let

\[
T_i(t)=\ell_{i,1}(t)\cdots\ell_{i,6}(t),
\qquad 1\le i\le6,
\]

be six regular one-parameter families of degree-six Chow terms. Assume every
factor at `t=0` is a matrix coordinate variable; repetitions are allowed. Let

\[
g_i(t)\in\mathcal D_4(T_i(t))
\]

be regular component families and suppose

\[
\sum_{i=1}^6 g_i(0)=0.
\tag{0.1}
\]

Then the perfect-matching projection of

\[
\sum_{i=1}^6 g_i'(0)
\]

cannot have all 24 perfect-matching coordinates nonzero. In particular it
cannot be a nonzero diagonal-torus transform of `perm_4`.

Thus every coordinate regular **first-order** six-block degeneration is zero
relative to the full-support permanent target. This does not exclude a
noncoordinate initial frame, a singular or multigrade valuation, or a lift
whose first nonzero term occurs at order at least two. Consequently the
unrestricted interval remains

\[
\boxed{6\le\mu(6,4)\le8}.
\]

## 1. One-component matching envelope

For component `i`, let `A_i` be the set of distinct coordinate cells among its
six specialized factors. Define

\[
E_i=\{M:\ M\text{ is a perfect matching and }|M\cap A_i|\ge3\}.
\tag{1.1}
\]

Every perfect matching in `g_i'(0)` lies in `E_i`. A derivative of the source
coefficients leaves four base factors and is possible only when the complete
matching lies in `A_i`. A derivative of one factor leaves three unchanged
base cells, so the target matching shares at least three cells with `A_i`.

Put

\[
D_i=\{M:M\subseteq A_i\},
\qquad e_i=|E_i|,
\qquad p_i=|D_i|.
\tag{1.2}
\]

The exact support profile for every set of at most six cells is

```text
|A|                         0  1  2  3  4  5  6
maximum |E(A)|              0  0  0  1  2  4  6
```

with the following refinements:

```text
|A|=5 and D(A) nonempty:       |D(A)|=1 and |E(A)|=2
|A|=6 and |D(A)|=1:            |E(A)|<=4
|A|=6 and |D(A)|=2:            |E(A)|=2
```

No six-cell support contains three perfect matchings. The complete scan checks

\[
\sum_{a=0}^6\binom{16}{a}=14893
\]

supports. There are 72 six-cell supports containing two perfect matchings;
each is the union of a transposition-adjacent pair.

## 2. Internal source-kernel tangents

Repeated coordinate factors require a separate treatment. Let

\[
\Phi_i:\operatorname{Sq}^4(\mathbf k^6)\longrightarrow
\operatorname{Sym}^4(V)
\]

be the specialized source-to-monomial map. Different four-label subsets can
map to the same quartic monomial when factors repeat.

Let `V_i` be the set of **non-direct** perfect matchings obtainable at first
order from a source vector in `ker(Phi_i)` by moving one factor, and put

\[
v_i=|V_i|.
\tag{2.1}
\]

The source fibers are products of choices among equal-cell labels. A motion
functional is nonzero on a fiber kernel exactly when it is nonconstant on that
fiber. Equivalently, choose two labels on the same repeated cell, remove them,
and complete a three-matching supported by the four residual labels. This
alternative description gives an independent implementation.

The complete multiset scan checks

\[
\binom{16+6-1}{6}=54264
\]

coordinate six-label frames and proves

\[
\boxed{e_i+p_i+v_i\le6.}
\tag{2.2}
\]

The maximum non-direct vertical support is two.

For clarity, the local proof splits by the number `a=|A_i|` of distinct cells.

- If `a=6`, `Phi_i` is injective and `v_i=0`. The refined support profile gives
  `e_i+p_i<=6`.
- If `a=5`, there is one doubled cell. Removing its two labels leaves four
  singleton cells, whose three-matchings have at most two distinct
  completions. Thus `v_i<=2`. If `p_i=0`, then `e_i<=4`; if `p_i=1`, then
  `e_i=2` and `v_i<=1`.
- If `a<=4`, then `e_i<=2`. Since `D_i` and `V_i` are disjoint subsets of
  `E_i`, one has `p_i+v_i<=e_i`, hence `e_i+p_i+v_i<=4`.

The primary audit verifies source-fiber functionals directly. The independent
audit removes two equal-cell labels and reconstructs the residual
three-matching envelope. The two sets agree on all 54,264 frames.

## 3. Degree-one incidence lemma

For a perfect matching `M`, write

\[
\nu(M)=|\{i:M\in E_i\}|.
\]

Suppose `M` is not direct, so `M` belongs to no `D_i`, and suppose
`nu(M)=1`, with unique envelope label `i`.

Any first-order contribution to `M` from component `i` comes from moving one
factor in a four-label source monomial. Group the source coefficients by their
specialized quartic monomial. If a group has nonzero aggregate coefficient,
(0.1) forces the same quartic monomial to occur with nonzero aggregate
coefficient in another component. That monomial contains the three unchanged
cells of `M`, so `M` would lie in the other component's envelope, contradicting
`nu(M)=1`.

Therefore every aggregate source coefficient driving `M` vanishes inside
component `i`; only a source-fiber kernel direction can remain. Hence

\[
M\in V_i.
\tag{3.1}
\]

This lemma explicitly includes internal cancellation caused by repeated
factors. It is the point missed by the earlier naive rule that every source
monomial must be shared across two components.

## 4. Global incidence contradiction

Assume the first derivative has all 24 perfect-matching coefficients nonzero.
Let

```text
d = number of target matchings that are direct in at least one component,
s = number of non-direct target matchings with envelope degree one.
```

Every direct target has envelope degree at least one. By Section 3, every
non-direct degree-one target belongs to some `V_i`. Every remaining target has
envelope degree at least two. Therefore

\[
\sum_{i=1}^6 e_i
\ge d+s+2(24-d-s)
=48-d-s.
\tag{4.1}
\]

Moreover

\[
d\le\sum_i p_i,
\qquad
s\le\sum_i v_i.
\tag{4.2}
\]

Combining (4.1) and (4.2) gives the necessary inequality

\[
\sum_{i=1}^6(e_i+p_i+v_i)\ge48.
\tag{4.3}
\]

But the local bound (2.2) gives

\[
\sum_{i=1}^6(e_i+p_i+v_i)\le6\cdot6=36,
\tag{4.4}
\]

a contradiction with margin twelve. This proves the theorem.

## 5. Verification

Run

```bash
python scripts/general_quartic_coordinate_first_order_closure.py \
  --json /tmp/general_quartic_coordinate_first_order_closure.json
python -O scripts/general_quartic_coordinate_first_order_closure.py \
  --json /tmp/general_quartic_coordinate_first_order_closure.opt.json
python scripts/general_quartic_coordinate_first_order_closure_independent.py
python -m unittest tests.test_general_quartic_coordinate_first_order_closure -v
```

The finite replay certifies the local support and source-fiber interfaces. The
global incidence argument is the written proof above.
