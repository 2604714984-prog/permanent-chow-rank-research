# Applying the forty-eight-plane theorem at the next two endpoints

**Status.** `PURE_ENDPOINT_APPLICATION`, `EXACT_INTEGER_PROFILE_REPLAY`,
`B32_AND_B48_EXCLUDED` (N6-077). The base field is algebraically closed of
characteristic zero.

This note continues N6-075 inside the N6-074 fixed-six reduction for a
hypothetical ordinary 28-term Chow decomposition of
\(\operatorname{perm}_6\). It uses the N6-076 theorem that every
48-plane in the permanent cubic space with first shadow 75 extends to an
N6-064 50-plane with the same first shadow.

## 1. The hereditary \(b=32\) layer

For the 22 residual terms retain the N6-075 notation

\[
 U_i=\mathcal D_3(T_i),\qquad L_A=\sum_{i\in A}U_i,
 \qquad f_A=\dim(S\cap L_A),\qquad x_A=\dim(E_3\cap L_A).
\]

Now \(\dim S\ge 400-32=368\). The six-term quadratic projection cap is
78, whereas the product shadow at dimension 53 is 81, so \(x_A\le52\).
For a complementary six-set \(C\) and its 16-set complement \(B\), the
shortening sequence gives

\[
 \ell_B\ge368-f_C\ge316,
 \qquad \ell_A\ge316-10\cdot20=116.                 \tag{1.1}
\]

If \(x_A=51\) or 52, its product shadow is 78. The defect-zero
common-\(W_{12}\) cap is 436, while the required prolongation dimensions
are respectively 465 and 464. Hence \(x_A\le50\).

### 1.1 Excluding \(f_A=50\)

If some \(f_A=50\), then \(S\cap L_A=E_3\cap L_A\) is an actual
50-plane. Since every complementary six-set has \(f_C\le50\), shortening
improves (1.1) to

\[
 \ell_B\ge318,\qquad \ell_A\ge118.                 \tag{1.2}
\]

Let \(a_2=\dim(E_2\cap\sum_{i\in A}F_i)\). The 50-plane product shadow
gives \(75\le a_2\le78\). The omitted-factor defect is at most three, so
some \(\varepsilon_i=0\). If its \(\alpha_i\le2\), the applicable
prolongation cap is at most 458, but

\[
 \dim(E_3+L_A)\ge400+118-50=468>458.                \tag{1.3}
\]

Thus \(\alpha_i=3\), and its quotient image has dimension 15. Since
\(t_2\le90-75=15\), equality throughout forces

\[
 (d_2,a_2,t_2)=(90,75,15),\qquad
 \varepsilon=(0^6),\qquad\kappa_2=0.
\]

The same cap forces all six \(\alpha_i=3\). The six \(F_i\), and therefore
the six \(U_i\), are literal direct. N6-064 gives the flag hook; the
N6-069/N6-061/N6-059/N6-072 chain contradicts it. Thus every \(f_A\le49\).

### 1.2 Excluding \(f_A=49\)

If some \(f_A=49\), the new global bound gives \(\ell_B\ge319\). By the
N6-031 rank-19 gap, a 16-set containing a non-full term has dimension at
most

\[
 15\cdot20+18=318.
\]

Therefore all individual middle ranks are 20 and \(\ell_A\ge119\). The
only possibilities are \(x_A=50\) or 49. Their required prolongation
dimensions are 469 and 470, both above 458. The same equality profile gives
the common-\(W_{15}\) literal-direct configuration. The former case is
excluded by N6-064; the latter by N6-073 followed by N6-064. Hence every
\(f_A\le48\).

### 1.3 The forced 48-plane

The 16-term capacity also gives \(f_A\ge368-320=48\). Consequently every
\(f_A=48\), and equality in every shortening sequence yields

\[
 \dim S=368,qquad \ell_B=320,qquad \ell_A=120.
\]

Every 16-set, hence every six-set, is literal direct. Now
\(48\le x_A\le50\). The cases \(x_A=50,49,48\) require prolongation
dimensions 470, 471, 472. Each forces the all-\(\alpha=3\) common-\(W_{15}\)
profile and a 75-dimensional first shadow. N6-064 excludes the first case,
N6-073 extends and excludes the second, and N6-076 extends and excludes the
third. This contradicts \(b=32\).

## 2. The fixed-six \(b=48\) layer

The exact scalar replay again finds 13 states. Twelve contain an
\(\varepsilon\)-zero term with \(\alpha\le2\); their required prolongation
dimensions exceed the corresponding caps 436, 440, or 453. The sole
pre-geometric state is

\[
 \varepsilon=(0^6),\quad\alpha=(3^6),\quad\kappa_2=0,
 \qquad(d_2,a_2,t_2,h)=(90,75,15,120).
\]

The \(t_2=15\) cap 458 excludes every subcase with some \(\alpha_i\le2\),
because the required dimension is \(400+120-48=472\). Thus the six middle
images are literal direct and their 48-dimensional permanent intersection
has first shadow 75. N6-076 extends it to a 50-plane with the same shadow.

## 3. The shared geometric contradiction

N6-076 or N6-073 supplies an N6-064 parent, so the second shadow is a genuine
23-dimensional flag hook. The five anchored common-quotient difference
spaces span its 75-plane. The universal 15-plane product-shadow lower bound
forces every pair of factor spans to be six-dimensional and transverse.
N6-069 excludes any invertible row or column block after the N6-061/N6-059
separation propagation; N6-072 excludes the remaining all-singular case.

Therefore N6-077 excludes

\[
 \boxed{b=32\quad\text{and}\quad b=48},
\]

and the fixed-six frontier becomes

\[
 \boxed{33\le b\le47}.
\]

## 4. Boundary

The 47-plane shadow-75 plateau at \(b=33\) and \(b=47\) is not covered by
N6-073 or N6-076. This note does not prove
\(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\) and makes no
border-rank claim.

```text
python scripts/n6_lower29_b32_b48_exclusion.py \
  --verify-json data/n6_lower29_b32_b48_exclusion.json
python -m unittest tests.test_n6_lower29_b32_b48_exclusion -v
```
