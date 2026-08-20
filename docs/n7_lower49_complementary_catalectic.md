# N7-009: the complementary catalectic gives ordinary lower 49

## Result

Over characteristic zero,

\[
\operatorname{ChowRank}(\operatorname{perm}_7)\ge49.
\]

The proof uses N7-007 to select 46 terms, the recursive shadow tower through
degree six, and the raw complementary catalectic \(C_{6,1}\).  It is an
ordinary-rank statement; exact rank and border rank remain open.

## The sixth-degree section

N7-008 gives the five-degree bound

\[
\dim\left(E_5\cap\sum_{i=1}^{46}D_5(T_i)\right)\le405.
\]

Let

\[
S=E_6\cap D_6(R),\qquad R=\sum_{i=1}^{46}T_i.
\]

Every derivative of \(S\) lies in the preceding five-degree intersection.
The exact \(r=6\) bivariate product-shadow capacity at budget 405 is 33.
The Ferrers witness \((7,7,7,3,3,3,3)\) has area and shadow \((33,405)\),
while area 34 first appears at shadow 411.  Thus

\[
b_6:=\dim(E_6\cap D_6(R))\le33.             \tag{1}
\]

## The raw complementary catalectic

The row space of \(C_{6,1}(P)\) is \(E_6\), while its column space is
\(E_1=V\).  The column space of \(C_{6,1}(R)\) is automatically contained in
\(V\), so that column intersection cancels completely in the double-quotient
rank inequality.  Equation (1) gives

\[
\operatorname{rank}C_{6,1}(P-R)
\ge49-b_6
\ge16.                                      \tag{2}
\]

Each Chow term has first-derivative span of dimension at most seven, hence
rank at most seven under this catalectic.  Equation (2) requires at least
three residual terms.  Together with the 46 selected terms,

\[
46+\left\lceil\frac{16}{7}\right\rceil=49.
\]

There is no circular use of lower 49: the already independent lower 46 from
N7-007 is exactly what permits selecting the first 46 terms.

The endpoint is intentionally stated with the raw catalectic.  A tempting
\(K_1\) argument is invalid because \(E_1=V\) has
\(E_1^{(1)}=\operatorname{Sym}^2V\), not \(E_2\).

Replay with

```powershell
python scripts/n7_lower49_complementary_catalectic.py --verify-json data/n7_lower49_complementary_catalectic.json
python -m unittest tests.test_n7_lower49_complementary_catalectic -v
```
