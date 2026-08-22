# A 49-term Glynn counterexample to the quadratic interface alone

## Status and claim boundary

`PURE EXACT COUNTEREXAMPLE`, `COMPUTATION REPLAYED`, `ROUTE BARRIER`.

This note does **not** give a 49-term decomposition of
\(\operatorname{perm}_7\), prove lower 50, or make a border-rank claim.  It
shows that the factor-span packet, containment in degree two, and every
currently proved scalar erasure lower bound do not by themselves force the
quadratic restriction rank to be at least 177.

## 1. The family

Normalize the 64 sign vectors by \(\delta_1=1\), order their remaining six
coordinates lexicographically with \(-1<1\), and retain the first 49.  Put

\[
 T_\delta=\prod_{r=1}^7 L_{r,\delta},\qquad
 L_{r,\delta}=\sum_{a=1}^7\delta_a x_{ra}.
\]

Every \(T_\delta\) is a seven-factor Chow term of factor rank seven.  The
seven row spaces are disjoint.  For distinct normalized signs \(\delta\) and
\(\epsilon\), the two lines in every row are distinct, so

\[
 L_\delta\cap L_\epsilon=0.
\]

Thus this family satisfies the strongest branch of the forced factor-span
packet.

## 2. Exact Walsh block ranks

Fix a set of \(d\) rows.  The corresponding derivative block of a sign term
has coefficients indexed by the Walsh characters whose sizes have the same
parity as \(d\) and are at most \(d\).  Rational elimination on the selected
49 evaluation rows gives:

| \(d\) | character count | block rank | \(\dim H_d\) |
|---:|---:|---:|---:|
| 1 | 7 | 7 | 49 |
| 2 | 22 | 22 | 462 |
| 3 | 42 | 38 | 1330 |
| 4 | 57 | 47 | 1645 |
| 5 | 63 | 49 | 1029 |
| 6 | 64 | 49 | 343 |

At degree two, the 22 characters are the constant character and the 21
quadratic characters \(\delta_a\delta_b\).  The rows with zero-based indices

\[
0,1,2,3,4,5,6,8,9,10,12,16,17,18,20,24,32,33,34,36,40,48
\]

form a square minor of determinant

\[
 68719476736=2^{36}.
\]

Hence the characteristic-zero block rank is exactly 22.

For a fixed row pair, the constant character gives the common diagonal
quadratic

\[
 \sum_a x_{ra}x_{sa},
\]

whereas the 21 size-two characters give exactly the permanent quadrics

\[
 x_{ra}x_{sb}+x_{rb}x_{sa},\qquad a<b.
\]

The 21 row-pair blocks are disjoint.  Consequently

\[
 E_2\subset H_2,qquad
 \dim H_2=21\cdot22=462,qquad
 \rho=\dim(H_2/E_2)=21.
\]

Every individual quadratic derivative space has dimension 21, so
\(\Delta_2=0\).  Thus

\[
 \boxed{\rho+\Delta_2=21<177.}
\]

## 3. Scalar bounds pass, coupled identity tests fail

The exact profile satisfies all current erasure dimension bounds:

\[
(H_2,H_3,H_4,H_5,H_6)
=(462,1330,1645,1029,343)
\ge(448,1293,1494,853,294).
\]

To distinguish dimension from containment, append to the selected Walsh row
space the coordinate subspace of characters of exact size \(d\).  Rational
rank gives

\[
\bigl(\dim(E_d\cap H_d)\bigr)_{d=1}^6
=(49,441,1085,875,231,14).
\]

In particular,

\[
 E_6\not\subset H_6.
\]

The family also violates the complementary inequalities forced by an actual
identity with the permanent:

\[
 H_2+H_5=462+1029=1491>1470,
\]

\[
 H_3+H_4=1330+1645=2975>2940.
\]

The pair \(1/6\) merely attains its numerical upper value
\(49+343=392\); it still fails the required degree-six containment.

## 4. Route decision

The proposed implication

\[
 \text{factor packet}+E_2\subset H_2+	ext{erasure dimensions}
 \Longrightarrow \rho+\Delta_2\ge177
\]

is false, even for 49 genuine Chow terms.  A surviving lower-50 lemma must
retain the full equation \(\sum_iT_i=\operatorname{perm}_7\) across
complementary degrees.  In particular it must use \(E_6\subset H_6\), the
degree \(2/5\) relation pairing, or an equivalent term-labelled
multiplication constraint.  Unlabelled Hilbert data and the quadratic
restriction map alone cannot close the gap.

## 5. Replay

```text
python scripts/n7_glynn49_quadratic_interface_counterexample.py \
  --verify-json data/n7_glynn49_quadratic_interface_counterexample.json
python -m unittest \
  tests.test_n7_glynn49_quadratic_interface_counterexample -v
```
