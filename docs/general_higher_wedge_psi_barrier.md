# The one-direction psi theorem has no naive higher-wedge amplification

**Status.** `PURE_COUNTEREXAMPLE`, `EXACT_RATIONAL_REPLAY` (G-033).
The nine displayed relations prove the obstruction in characteristic zero.
The accompanying `Fraction` elimination determines the complete rank profile
but is not needed to refute the extrapolation.

## 1. The false extrapolation

Let

\[
 E=\mathcal D_1(\operatorname{perm}_3)
   \subset\operatorname{Sym}^2V,
 \qquad \dim V=9,
\]

and let

\[
 \delta_{2,p}:\operatorname{Sym}^2V\otimes\Lambda^pV
 \longrightarrow V\otimes\Lambda^{p+1}V
\]

be the standard Koszul differential.  The proved psi theorem says that one
quadratic direction outside `E` adds at least `8` dimensions when `p=1`.
For a pure square, this is exactly

\[
 \binom{8}{1}=8.
\]

A tempting extrapolation is that the gain at exterior degree `p` is always at
least `binom(8,p)`.  It is false already at `p=3`.

### Theorem 1.1

Put `q=x_(00)^2`.  Then `q` is not in `E`, but

\[
\boxed{
 \operatorname{rank}\delta_{2,3}((E+\langle q\rangle)\otimes\Lambda^3V)
 -\operatorname{rank}\delta_{2,3}(E\otimes\Lambda^3V)
 =47<56=\binom83.
}
\tag{1.1}
\]

Thus neither the psi chart nor the statement that one new direction adds
`n^2-1` first-Koszul dimensions has a formal binomial amplification to higher
exterior degree.

## 2. Nine explicit characteristic-zero relations

Use the abbreviations

\[
 e=x_{00},\quad a=x_{01},\quad b=x_{02},\quad
 c=x_{10},\quad d=x_{20},
\]

\[
 t=x_{11},\quad u=x_{12},\quad v=x_{21},\quad w=x_{22},
\]

and

\[
 P_{ij}=e x_{ij}+x_{0j}x_{i0}in E
 \qquad(i,j\in\{1,2\}).
\]

Write `[r,s,z]` for `r wedge s wedge z`, in the displayed coordinate order,
and abbreviate `delta_(2,3)` to `delta`.  Direct application of the Koszul
sign rule gives the following nine identities:

\[
\begin{aligned}
0={}&2\delta(P_{22}\otimes[e,b,d])
       +\delta(q\otimes[b,d,w]),\\
0={}&2\delta(P_{21}\otimes[e,b,d])
       +2\delta(P_{22}\otimes[e,a,d])
       +\delta(q\otimes[a,d,w])+\delta(q\otimes[b,d,v]),\\
0={}&2\delta(P_{21}\otimes[e,a,d])
       +\delta(q\otimes[a,d,v]),\\
0={}&-2\delta(P_{12}\otimes[e,b,d])
       -2\delta(P_{22}\otimes[e,b,c])
       -\delta(q\otimes[b,c,w])+\delta(q\otimes[b,u,d]),\\
0={}&-2\delta(P_{11}\otimes[e,b,d])
       -2\delta(P_{12}\otimes[e,a,d])
       -2\delta(P_{21}\otimes[e,b,c])
       -2\delta(P_{22}\otimes[e,a,c])\\
   &\hspace{1.5em}-\delta(q\otimes[a,c,w])
       +\delta(q\otimes[a,u,d])
       -\delta(q\otimes[b,c,v])
       +\delta(q\otimes[b,t,d]),\\
0={}&-2\delta(P_{11}\otimes[e,a,d])
       -2\delta(P_{21}\otimes[e,a,c])
       -\delta(q\otimes[a,c,v])+\delta(q\otimes[a,t,d]),\\
0={}&2\delta(P_{12}\otimes[e,b,c])
       +\delta(q\otimes[b,c,u]),\\
0={}&2\delta(P_{11}\otimes[e,b,c])
       +2\delta(P_{12}\otimes[e,a,c])
       +\delta(q\otimes[a,c,u])+\delta(q\otimes[b,c,t]),\\
0={}&2\delta(P_{11}\otimes[e,a,c])
       +\delta(q\otimes[a,c,t]).
\end{aligned}
\tag{2.1}
\]

The `q`-wedge supports occurring in different lines of (2.1) are disjoint.
Consequently their `q`-parts are nine linearly independent elements of
`q tensor Lambda^3 V`.  Each maps into
`delta(E tensor Lambda^3 V)`.  Since multiplication by `q=e^2` kills exactly
the wedges already containing `e`, the raw new source has dimension
`binom(8,3)=56`.  Therefore the quotient gain is at most `56-9=47`.  This
already proves the strict inequality in (1.1) without computation.

## 3. Exact rank closure

Exact rational elimination gives

\[
\begin{array}{c|rrrrrrrrr}
p&0&1&2&3&4&5&6&7&8\\ \hline
\operatorname{rank}\delta_{2,p}(E)&9&80&315&720&934&720&315&80&9\\
\operatorname{rank}\delta_{2,p}(E+\langle q\rangle)
 &10&88&343&767&966&720&315&80&9\\
\text{gain}&1&8&28&47&32&0&0&0&0
\end{array}
\tag{3.1}
\]

In particular the nine relations in (2.1) account for the complete `p=3`
defect, so the upper bound 47 is exact.

Run

```text
python scripts/general_higher_wedge_psi_barrier.py \
  --json data/general_higher_wedge_psi_barrier.json
python -m unittest tests/test_general_higher_wedge_psi_barrier.py
```

The script constructs all matrices from coefficient dictionaries and performs
sparse Gaussian elimination over `Fraction`.  It uses neither floating point
nor a finite field.

## 4. Consequence for the lower-27 program

The proved `p=1` psi theorem remains valid.  What fails is the inference that
one can exterior-shadow its `n^2-1` new dimensions into a universal higher
wedge gain.  At higher degree the relevant kernel is a higher relative Koszul
homology group, and (2.1) shows that it contains relations invisible to the
first psi chart.  The exact middle third-Koszul rank for `perm_6` must
therefore be coupled to these relative homology modules directly; a binomial
amplification of the old chart cannot close lower 27.
