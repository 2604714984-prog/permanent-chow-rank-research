# Rectangular half-defect barrier for \(\operatorname{perm}_7\)

## Status

`PURE SINGLE-MIDDLE-LAYER ROUTE BARRIER; NOT A CHOW-RANK LOWER BOUND.`

The natural rectangular analogue of the exact \(n=6\) proof cannot prove
\(\operatorname{ChowRank}(\operatorname{perm}_7)=64\). The global reduction
is valid, but the local inequality it would require is false for a full
seven-factor term.

## 1. Valid rectangular global bound

For maps \(A_i:X^*\to Y\) of ranks \(u_i\), choose factorizations
\(A_i=B_iJ_iC_i^*\). If \(D_+\) and \(D_-\) are the dimensions of the
summed output and input spaces, Sylvester gives

\[
\operatorname{rank}\Bigl(\sum_iA_i\Bigr)
\ge D_++D_- -\sum_i u_i. \tag{1.1}
\]

For \(A_i=C_{3,4}(T_i)\), put \(\delta_i=35-u_i\) and
\(\Delta=\sum_i\delta_i\). The permanent rectangular catalectic has rank
\(35^2=1225\), so

\[
h_++h_-\le35N-1225-\Delta. \tag{1.2}
\]

The two derivative-tower kernel identities are also valid:

- \(\mathcal D_4(T_i)\to V\otimes(\sum_i\mathcal D_3(T_i)/E_3)\)
  has global rank \(h_+\), using \(E_3^{(1)}=E_4\);
- \(\mathcal D_3(T_i)\to V\otimes(\sum_i\mathcal D_2(T_i)/E_2)\)
  has global rank \(h_-\), using \(E_2^{(1)}=E_3\).

These statements correctly account for overlaps among term spaces.

## 2. The false local target

Since the factor spans fill 49 variables, a direct analogue of N6-140 would
need

\[
\operatorname{rank}\beta_i^+
+\operatorname{rank}\beta_i^-+\delta_i
\ge\frac{145}{7}d_i. \tag{2.1}
\]

Summing (2.1) would give \(h_++h_-\ge1015-\Delta\), which together with
(1.2) would force \(N\ge64\).

However, take a product of seven independent factors and the full quotient
of its seven-dimensional factor span. Then \(\delta_i=0\), while

\[
\dim\mathcal D_4(T_i)=35,qquad
\dim\mathcal D_3(T_i)=35.
\]

Consequently the left side of (2.1) is at most \(70\), whereas the right
side is

\[
\frac{145}{7}\cdot7=145.
\]

Thus (2.1) is false with gap 75. No refinement of the permanent
intersection can repair this domain-dimension obstruction.

## 3. Useful surviving local data

Torus degeneration of a factor-span-\(\ell\) term to a monomial with a
positive exponent partition of seven gives central rectangular ranks equal
to the coefficient of \(t^3\) in
\(\prod_j(1+t+\cdots+t^{a_j})\). The sharp degeneration floors are

\[
\begin{array}{c|rrrrrrr}
\ell&1&2&3&4&5&6&7\\ \hline
u&1&2&4&8&15&25&35.
\end{array}
\]

These ranks remain useful inputs for a multi-degree invariant, but they do
not rescue the single-middle-layer filtration.

## 4. Correct next target

A successful \(n=7\) proof must charge information after the total linear
factor span is already full. The next object should therefore combine the
adjacent derivative maps in degrees two through five, or use their coupled
relation/homology module. The immediate task is to formulate an invariant
with:

1. coordinate invariance;
2. a uniform cap for every degenerate seven-factor Chow term;
3. subadditivity or a hereditary global inequality;
4. a permanent value sufficient to force 64 terms; and
5. an exact low-dimensional feasibility test before large computation.

## 5. Replay

```text
python scripts/n7_rectangular_half_defect_reduction.py \
  --verify-json data/n7_rectangular_half_defect_reduction.json
python -m unittest tests.test_n7_rectangular_half_defect_reduction -v
```
