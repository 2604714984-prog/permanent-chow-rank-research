# A recursive permanent-relative capacity bound across the full derivative tower

## Status and boundary

`PROOF_DRAFT_COMPLETE`, `GENERAL_N_THEOREM`,
`EXACT_INTEGER_REPLAY_PENDING_HOSTED_CI`.

This note replaces the previous one-step cross-degree estimate by a recursive
capacity bound defined simultaneously at every permanent derivative degree.
The theorem is valid for arbitrary `n`, arbitrary degree-`n` Chow terms,
repeated or dependent factors, and arbitrary block sizes.

Its first new numerical consequence is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_7)\ge46.}
\]

The existing stacked bound

\[
\operatorname{ChowRank}(\operatorname{perm}_8)\ge80
\]

is recovered as a regression, not treated as the purpose of the theorem.
The theorem does not determine an exact unrestricted Chow rank, improve a
border rank, or prove general Glynn optimality.

## 1. Exact adjacent product shadows

For `1<=d<=n`, write

\[
E_d(n)=\mathcal D_d(\operatorname{perm}_n).
\]

Let

\[
\mathfrak F_{n,d}(b)
=
\min_{\substack{A\subseteq E_d(n)\\\dim A=b}}
\dim\partial A.
\tag{1.1}
\]

The exact product-shadow theorem already proved in the repository computes
(1.1) by a Ferrers integer program. Define its inverse capacity

\[
\Gamma_{n,d}(C)
=
\max\{b:\mathfrak F_{n,d}(b)\le C\}.
\tag{1.2}
\]

Every value in (1.2) is an exact finite integer. Iterating adjacent degrees is
sufficient to propagate information through the full derivative tower; no
separate all-orders shadow dependency is needed.

## 2. The recursive capacity

Put

\[
M_{n,d}=\binom nd,
\qquad
N_{n,d}=M_{n,d}^2=\dim E_d(n).
\]

For `q>=0`, define `B_(n,d)(q)` recursively. At output degree one,

\[
B_{n,1}(q)=\min\{n^2,qn\}.
\tag{2.1}
\]

For `d>=2`, set `B_(n,d)(0)=0` and

\[
\boxed{
\begin{aligned}
B_{n,d}(q)=\min\Bigg\{&N_{n,d},\ qM_{n,d},\\
&\Gamma_{n,d}\bigl(B_{n,d-1}(q)\bigr),\\
&\min_{1\le s<q}
\left((q-s)M_{n,d}+B_{n,d}(s)\right)
\Bigg\}.
\end{aligned}}
\tag{2.2}
\]

The first line is the ambient and literal one-term capacity. The second line
pushes the same block down one derivative degree and inverts the exact shadow.
The third line projects away an arbitrary retained subblock and preserves its
already proved permanent-relative defect.

## 3. General derivative-tower theorem

### Theorem 3.1

Let `T_1,...,T_q` be arbitrary degree-`n` Chow terms over a
characteristic-zero field. Then for every `1<=d<=n`,

\[
\boxed{
\dim\left(
E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i)
\right)
\le B_{n,d}(q).
}
\tag{3.1}
\]

### Proof

Proceed by induction on the lexicographically ordered pair `(d,q)`.

For `d=1`, one Chow term has factor-span dimension at most `n`; hence the
literal sum has dimension at most `qn`, while `E_1(n)` has dimension `n^2`.
This is (2.1).

Assume `d>=2`, and put

\[
A=E_d(n)\cap\sum_{i=1}^{q}\mathcal D_d(T_i).
\]

The ambient and literal estimates give

\[
\dim A\le N_{n,d},
\qquad
\dim A\le qM_{n,d}.
\tag{3.2}
\]

Differentiation gives the coupled-safe containment

\[
\partial A
\subseteq
E_{d-1}(n)\cap\sum_{i=1}^{q}\mathcal D_{d-1}(T_i).
\tag{3.3}
\]

The induction hypothesis bounds the right side by `B_(n,d-1)(q)`. By the
exact definition (1.1),

\[
\mathfrak F_{n,d}(\dim A)
\le B_{n,d-1}(q),
\]

and inversion gives

\[
\dim A\le
\Gamma_{n,d}\bigl(B_{n,d-1}(q)\bigr).
\tag{3.4}
\]

Finally choose any `s` labels, retain their degree-`d` derivative spaces, and
choose a linear section of the literal summation map over `A`. Projection to
the other `q-s` components has image dimension at most

\[
(q-s)M_{n,d}.
\]

Its kernel injects into the permanent-relative intersection of the retained
`s`-term block, whose dimension is at most `B_(n,d)(s)` by induction on `q`.
Thus

\[
\dim A\le(q-s)M_{n,d}+B_{n,d}(s).
\tag{3.5}
\]

Taking the minimum of (3.2)--(3.5) proves (3.1). ∎

## 4. Coupled/literal firewall

The theorem controls the literal space

\[
\sum_i\mathcal D_d(T_i).
\]

For an actual polynomial sum `R=sum_i T_i`, it uses only

\[
\mathcal D_d(R)
\subseteq
\sum_i\mathcal D_d(T_i).
\tag{4.1}
\]

No equality between a coupled catalectic image and a literal derivative-space
sum is assumed. No direct-sum hypothesis is used in (3.5).

## 5. First finite tower rows

For `n=7`, the exact recurrence gives

```text
q                  1   2   3   4   5
B_(7,1)(q)          7  14  21  28  35
B_(7,2)(q)          3  22  43  64  85
B_(7,3)(q)          0   4  17  40  64
```

The decisive transition at `q=5` is

\[
B_{7,2}(5)=85,
\]

followed by

\[
\mathfrak F_{7,3}(64)=84,
\qquad
\mathfrak F_{7,3}(65)=87,
\]

so `B_(7,3)(5)=64`.

For `n=8`, the same recurrence begins

```text
q                  1   2   3   4    5
B_(8,1)(q)          8  16  24  32   40
B_(8,2)(q)          6  34  62  90  118
B_(8,3)(q)          0  10  40  80  112
```

Thus the five-term cubic cap `112` from the preceding cross-degree theorem is
the degree-three row of a general tower, not an isolated `n=8` rule.

## 6. New application: `perm_7>=46`

Assume for contradiction that a 45-term decomposition exists. The preceding
stacked theorem already proves lower bound 45, so selecting twenty nonzero
terms is legitimate. Select five of the twenty as a retained block.

The tower theorem gives

\[
\dim\left(
E_3(7)\cap\sum_{i=1}^{5}\mathcal D_3(T_i)
\right)
\le64.
\tag{6.1}
\]

The other fifteen fixed terms contribute at most

\[
15\binom73=525
\]

cubic dimensions, giving total projected first-shadow capacity

\[
525+64=589.
\tag{6.2}
\]

The exact outer transition is

\[
\mathfrak F_{7,4}(341)=586,
\qquad
\mathfrak F_{7,4}(342)=590.
\tag{6.3}
\]

Therefore the complementary degree-four intersection has dimension at most
`341`. At first-Koszul output degree three,

\[
A_{7,3}=58,800,
\qquad
B_{7,3}=1,680.
\]

The residual requires at least

\[
\left\lceil
\frac{58,800-49\cdot341}{1,680}
\right\rceil
=26
\tag{6.4}
\]

terms. Together with the twenty fixed terms this forces at least 46 terms,
contradiction. Hence

\[
\boxed{
\operatorname{ChowRank}(\operatorname{perm}_7)\ge46.
}
\tag{6.5}
\]

Glynn gives the independent upper bound 64.

## 7. Why this is a general-`n` result rather than a `perm_8` project

The integers `7` and `8` enter only after Theorem 3.1, when evaluating the
first finite rows of a recurrence defined for every `n,d,q`. These instances
serve as regression and falsification tests:

1. they reject incorrect general recurrences before asymptotic promotion;
2. they verify that a new inequality changes a real unrestricted bound; and
3. they expose equality and near-equality configurations for the next
   structural theorem.

They are not the mathematical scope of the theorem. Further work should
analyze the recurrence uniformly in `n`, not continue indefinitely with an
`n=8`-specific state tree.

## 8. Strongest objection and route boundary

The strongest objection is that (2.2) still records only dimensions of
successive derivative shadows. Even after recursive composition, it may stay
on the central-binomial asymptotic scale and fail to approach the Glynn value
`2^(n-1)`.

That objection is valid. This theorem is a reusable general capacity engine
and yields a new finite lower bound, but it is not by itself a credible final
proof of general Glynn optimality. The next promoted result must do at least
one of the following:

- derive a uniform asymptotic gain from the tower recurrence;
- classify equality or near-equality families uniformly in `n`;
- add a frame-sensitive or representation-valued defect not determined by
  shadow cardinalities; or
- produce a doubling recurrence for unrestricted Chow rank.

No additional manager, registry, dispatcher, database, solver framework or
broad state architecture is authorized.

## 9. Reproduction

Run

```bash
python scripts/general_derivative_tower_capacity.py \
  --json /tmp/general_derivative_tower_capacity.json
python scripts/general_derivative_tower_capacity_independent.py
python -m unittest tests.test_general_derivative_tower_capacity -v
```

Expected terminal markers:

```text
GENERAL_DERIVATIVE_TOWER_CAPACITY_AUDIT_PASS
GENERAL_DERIVATIVE_TOWER_CAPACITY_INDEPENDENT_PASS
```
