# Applying the forty-seven-plane theorem at the last shadow-75 endpoints

**Status.** `PURE_ENDPOINT_APPLICATION`, `EXACT_INTEGER_PROFILE_REPLAY`,
`B33_AND_B47_EXCLUDED` (N6-079).

Inside the N6-074 fixed-six reduction, N6-079 applies the N6-078
47-to-50 extension theorem to the hereditary \(b=33\) layer and the original
fixed-six \(b=47\) layer.

## 1. The hereditary \(b=33\) layer

Retain

\[
 f_A=\dim(S\cap L_A),\qquad x_A=\dim(E_3\cap L_A),
\qquad \dim S\ge367.
\]

The 53-plane shadow is 81 against the six-term quadratic cap 78, so
\(x_A\le52\). Complementary shortening first gives

\[
 \ell_{16}\ge315,\qquad\ell_A\ge115.
\]

The cases \(x_A=51,52\) have defect zero and require prolongation dimensions
464 and 463, above the common-\(W_{12}\) cap 436.

The next three shortening levels are treated successively:

\[
\begin{array}{c|c|c}
\text{assumption}&\ell_{16}\text{ floor}&\ell_A\text{ floor}\cr
f_A=50&317&117\cr
f_A=49&318&118\cr
f_A=48&319&119.
\end{array}
\tag{1.1}
\]

At each level, \(f_A\le x_A\le50\). For every possible \(x_A\), the
required prolongation dimension is at least 467 and therefore exceeds the
applicable cap 458. The omitted-factor argument forces

\[
 \varepsilon=(0^6),\quad\alpha=(3^6),\quad\kappa_2=0,
 \qquad(d_2,a_2,t_2)=(90,75,15).
\tag{1.2}
\]

The six quadratic spaces, hence the six middle images, become literal
direct. The actual 50-, 49- or 48-plane is excluded respectively by N6-064,
N6-073 or N6-076 followed by the common geometric chain. At the last row of
(1.1), \(319>15\cdot20+18\), so the N6-031 rank-19 gap independently forces
every individual middle rank to be 20.

Thus every \(f_A\le47\). The 16-term capacity gives the reverse inequality
\(f_A\ge367-320=47\). Equality for every six-set forces

\[
 \dim S=367,qquad\ell_{16}=320,qquad\ell_A=120.
\tag{1.3}
\]

Now \(47\le x_A\le50\). The four required prolongation dimensions are 470,
471, 472 and 473. They again force (1.2). N6-064, N6-073, N6-076 and N6-078
exclude the four cases in order. Hence \(b=33\) is impossible.

## 2. The fixed-six \(b=47\) layer

The exact scalar replay again has 13 states. Twelve contain an
\(\varepsilon\)-zero term with \(\alpha\le2\) and are strictly excluded by
the caps 436, 440 or 453. The sole pre-geometric state is

\[
 \varepsilon=(0^6),\quad\alpha=(3^6),\quad\kappa_2=0,
 \qquad(d_2,a_2,t_2,h)=(90,75,15,120).
\]

Its required prolongation dimension is

\[
 400+120-47=473>458,
\]

so the \(t_2=15\) cap rules out any \(\alpha\le2\) subcase. Literal
directness gives an actual 47-plane with first shadow 75, and N6-078 extends
it to an N6-064 parent.

## 3. Shared contradiction and boundary

The extension theorem makes the second shadow a genuine 23-dimensional flag
hook. Product-shadow equality makes all six factor spans six-dimensional and
pairwise transverse. N6-069 plus N6-061/N6-059 excludes an invertible row or
column block; N6-072 excludes the all-singular remainder.

Therefore

\[
 \boxed{b=33\quad\text{and}\quad b=47}
\]

are impossible, and the fixed-six frontier becomes

\[
 \boxed{34\le b\le46}.
\]

The next boundary is qualitatively different: at \(b=34\), the best
shortening uses seven terms and gives a 66-plane with shadow 87 against
projection cap 93. This defect-six layer is not classified. N6-079 does not
prove \(\operatorname{ChowRank}(\operatorname{perm}_6)\ge29\) and makes no
border-rank claim.

```text
python scripts/n6_lower29_b33_b47_exclusion.py \
  --verify-json data/n6_lower29_b33_b47_exclusion.json
python -m unittest tests.test_n6_lower29_b33_b47_exclusion -v
```
