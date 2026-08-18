# Exact integration of recursive Chow zero rows into the derivative tower

## Status and claim boundary

`EXACT_FINITE_DIAGNOSTIC`, `N3_TO_N10`, `EXACT_INTEGER_CPP_REPLAYED`.

PR #80 supplies recursive hard-zero counts for permanent derivative blocks.
This note inserts the strongest current direct seeds and their recursive
closure into the exact prefix min-plus derivative tower.

The exact result is:

\[
\boxed{
\text{all saturation thresholds for }3\le n\le10\text{ remain unchanged}.
}
\]

A few low-term capacities decrease, by at most two dimensions in the tested
range, but none of the published lower bounds changes.

This is not an asymptotic barrier theorem and does not imply that recursive
zero seeds are irrelevant for \(n\ge11\).

## 1. Seed closure

Let

\[
a_{n,d}=\left\lfloor\frac{d^2-1}{n}\right\rfloor.
\]

The current direct seed at degree \(d\) is the maximum of:

1. the strict factor-span count;
2. the endpoint/first-excess count for \(d\ge3\);
3. the PR #79 quartic count \(\lfloor(4^2+4+3)/n\rfloor\);
4. the PR #79 count \(\lfloor(d^2+d+4)/n\rfloor\) for \(d\ge5\), whenever
   the claimed count is at least two.

The recursive closure from PR #80 is

\[
\widehat Z_{n,d}
=
\max\left\{
\sigma_{n,d},
\widehat Z_{n,d-1}+a_{n,d}
\right\}.
\tag{1.1}
\]

For \(n=3,\ldots,10\), the resulting rows are

```text
n=3:  0,1,3
n=4:  0,0,2,5
n=5:  0,0,2,5,9
n=6:  0,0,1,3,7,12
n=7:  0,0,1,3,6,11,17
n=8:  0,0,1,2,5,9,15,22
n=9:  0,0,0,2,4,7,12,19,27
n=10: 0,0,0,2,4,7,11,17,25,34
```

The entries are indexed by output degree one through \(n\).

## 2. Tower insertion

The original direct cap is

\[
C_{n,d}(q)
=
\min\left\{
M_{n,d}^2,
qM_{n,d},
\Gamma_{n,d}(B_{n,d-1}(q))
\right\},
\]

where \(M_{n,d}=\binom nd\).

The seeded cap is

\[
\widetilde C_{n,d}(q)
=
\begin{cases}
0,&q\le\widehat Z_{n,d},\\
\min\{M_{n,d}^2,qM_{n,d},
\Gamma_{n,d}(\widetilde B_{n,d-1}(q))\},&q>\widehat Z_{n,d}.
\end{cases}
\tag{2.1}
\]

Both use the same exact prefix envelope:

\[
B_{n,d}(q)
=
qM_{n,d}
+
\min_{0\le t\le q}
\left(C_{n,d}(t)-tM_{n,d}\right).
\tag{2.2}
\]

The C++ implementation reconstructs every Ferrers inverse-shadow table from
colex order. No old capacity row is read from JSON.

## 3. Exact result

The baseline and seeded saturation thresholds are identical:

```text
n=3:  3,4
n=4:  4,7,8
n=5:  5,11,14,15
n=6:  6,16,24,26,27
n=7:  7,22,39,46,48,49
n=8:  8,29,59,80,87,89,90
n=9:  9,37,87,136,155,161,163,164
n=10: 10,46,123,219,280,299,305,307,307.
```

The exact capacity changes are small:

```text
n     changed cells     maximum reduction
3          0                   0
4          0                   0
5          2                   1
6          0                   0
7          1                   1
8          1                   1
9          2                   1
10         4                   2
```

Thus the currently published stacked numerical boundaries remain

\[
49,\ 90,\ 164,\ 307
\]

for \(n=7,8,9,10\), respectively.

## 4. Interpretation

The recursive zero theorem is mathematically stronger than the direct
factor-span seed and creates quadratic-size zero blocks at linear output
degree. Nevertheless, through \(n=10\), the exact scalar tower already has
stronger prefix-envelope deficits near its decisive saturation points.

This finite result does not prove that the same remains true asymptotically.
A uniform comparison between recursively seeded deficits and the central
tower variational problem remains open.

## 5. Reproduction

Primary:

```bash
python scripts/general_recursive_zero_seeded_tower.py
```

The driver compiles and runs the exact C++17 engine. It uses OpenMP when
available and falls back to a serial exact build.

Independent:

```bash
python scripts/general_recursive_zero_seeded_tower_independent.py
```

The independent implementation rebuilds all inverse shadows and both towers
for \(3\le n\le8\) without importing the primary code.
