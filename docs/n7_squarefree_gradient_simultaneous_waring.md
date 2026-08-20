# Squarefree septic gradient: simultaneous Waring certificate

## Status

`EXACT_COLUMN_UNIFORM_ENDPOINT_EXCLUSION`.

Let

\[
M_i=\partial_{x_i}(x_0x_1\cdots x_6)=\prod_{j\ne i}x_j.
\]

This note proves

\[
63\leq \operatorname{rk}_{\mathrm{sim}}\{M_0,\ldots,M_6\}\leq64.
\]

Consequently, a putative 49-term endpoint cannot express all seven sextics
using a common set of 49 sixth powers.  This excludes the column-uniform, or
already tensor-split, endpoint.  It does **not** prove that an arbitrary
49-term Chow decomposition has that form.

## The apolar lower bound

In the dual ring \(T=\mathbb C[Y_0,\ldots,Y_6]\), direct monomial
membership gives

\[
H:=\bigcap_i M_i^\perp
  =(Y_0^2,\ldots,Y_6^2,Y_0Y_1\cdots Y_6).
\]

Carlini--Ventura Proposition 2.1 says that, for any linear form \(L\), the
length of

\[
T/\bigl((L)+(H:(L))\bigr)
\]
is a lower bound for simultaneous Waring rank.  Set \(L=Y_0\).  The standard
monomials are precisely the squarefree monomials in
\(Y_1,\ldots,Y_6\), except their full product.  Their Hilbert vector is

\[
(1,6,15,20,15,6,0),
\]

so their number is \(2^6-1=63\).

The script independently checks the common apolar ideal on all \(3^7=2187\)
bounded exponent vectors and enumerates the 63 standard monomials.

## The upper bound

The exact polarization identity

\[
x_0\cdots x_6=
\frac{1}{2^6 7!}
\sum_{\epsilon_0=1,\ \epsilon_i=\pm1}
\left(\prod_i\epsilon_i\right)
\left(\sum_i\epsilon_i x_i\right)^7
\]

uses 64 linear forms.  Differentiating it expresses every \(M_i\) using the
same 64 sixth powers.  The replay checks all
\(\binom{13}{6}=1716\) degree-seven coefficients exactly over the integers.

## Boundary

The stronger gradient formula in Carlini--Ventura Proposition 3.8 assumes all
exponents of the original monomial are strictly greater than one, so it is not
invoked here.  The present lower bound uses their general Proposition 2.1.
No ordinary lower-50 or border-rank claim follows until a general endpoint is
shown to be column-uniform.

Replay:

```text
python scripts/n7_squarefree_gradient_simultaneous_waring.py --verify-json data/n7_squarefree_gradient_simultaneous_waring.json
python -m unittest tests.test_n7_squarefree_gradient_simultaneous_waring
```
