# Second-pass audit report: repaired exact ordinary Chow rank of `perm_6`

**Audit date:** 2026-08-21  
**Repository:** `2604714984-prog/permanent-chow-rank-research`  
**Audit type:** adversarial internal mathematical review and artifact-consistency review  
**Reviewer:** GPT-5.6 Pro, acting as an AI-assisted internal reviewer rather than a named human external referee  
**Claim boundary:** ordinary Chow rank over an algebraically closed field of characteristic zero; no border-Chow-rank claim is reviewed

## 1. Supersession notice

This second-pass report replaces the first-pass verdict previously stored at this path. The earlier report is preserved in Git history at commit

```text
180efad2e8ee874190c3c76443d3359a4308d4ad
```

and was correct for the artifacts then reviewed: the old exact-rank candidate gave a valid conditional global reduction but did not prove its unrestricted local quotient-symbol proposition.

The repaired proof subsequently exposed and removed a genuine additional defect in the old local argument: formal squarefree factor-label product spaces had been conflated with the actual derivative spaces of two five-variable normal forms. The current audit reviews the repaired proof, not the superseded candidate.

## 2. Frozen review boundary

| Item | Frozen reference |
|---|---|
| Pull request | PR #31, `agent/general-column-sign-rank` |
| Reviewed head | `d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5` |
| Reviewed tree | `91abdeacf11fca57eac3b1aea66b6dc66bd8b157` |
| Commit message | `Repair exact perm6 half-defect proof` |
| Base branch head | `main` at `111a022c8de36619c32a0c2cf660aa4dd5b5aeab` |
| Associated CI run | `exact-bound-tests` run `32469992061`, run number `801` |
| CI merge commit | `3e793ea830f54b650d1f506029362cc913db4ab8` |

Primary reviewed artifacts, pinned to the repaired head:

- [`docs/n6_exact_ordinary_chow_rank_32.md`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/docs/n6_exact_ordinary_chow_rank_32.md)
- [`docs/n6_exact_ordinary_chow_rank_32.tex`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/docs/n6_exact_ordinary_chow_rank_32.tex)
- [`docs/n6_exact_ordinary_chow_rank_32_audit_closure.md`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/docs/n6_exact_ordinary_chow_rank_32_audit_closure.md)
- [`scripts/n6_exact_ordinary_chow_rank_32.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/scripts/n6_exact_ordinary_chow_rank_32.py)
- [`tests/test_n6_exact_ordinary_chow_rank_32.py`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/tests/test_n6_exact_ordinary_chow_rank_32.py)
- [`data/n6_exact_ordinary_chow_rank_32.json`](https://github.com/2604714984-prog/permanent-chow-rank-research/blob/d96bfe57ce3c2ab431f745869cf86d5ee33c1dd5/data/n6_exact_ordinary_chow_rank_32.json)

This report does not automatically cover later modifications to any load-bearing lemma or artifact.

## 3. Executive verdict

The repaired theorem is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_6)=32.}
\]

### Audit disposition

| Severity | Count | Disposition |
|---|---:|---|
| Fatal mathematical findings | 0 | none found |
| Major mathematical findings | 0 | none found |
| Minor findings | 1 | TeX spacing-command typo; no mathematical effect |
| Final internal verdict | **PASS** | exact ordinary-rank proof accepted within this audit scope |

The previous `CONDITIONAL` hold on exact rank 32 is closed for the repaired head. The unrestricted local half-defect quotient-symbol estimate is now proved by a combination of written characteristic-zero arguments and exact finite derivations from the underlying objects.

The proof may be described internally as:

> Over an algebraically closed field of characteristic zero, the ordinary Chow rank of the six-by-six permanent is exactly 32.

It must not be described as a border-Chow-rank theorem, a proof of the general formula for all `n`, a proof-assistant formalization, or named external peer review.

## 4. What the repair changed

For

\[
T_s=x_1x_2x_3x_4x_5(x_1+\cdots+x_s),
\qquad 1\le s\le5,
\]

exact differentiation gives

\[
\begin{array}{c|cc|cc}
s&\dim \mathcal D_2(T_s)&\dim \mathcal D_3(T_s)&
\dim F_{\mathrm{formal}}&\dim U_{\mathrm{formal}}\\ \hline
1&11&14&11&14\\
2&11&14&12&17\\
3&13&18&13&19\\
4&14&20&14&20\\
5&15&20&15&20.
\end{array}
\]

Thus the old formal-to-actual identification fails for `s=2` in degrees two and three and for `s=3` in degree three. The repair is substantive:

1. the false shortcut is explicitly rejected;
2. negative regression tests require the failed equalities to remain false;
3. the squarefree fixed-point table is used only for six independent factors, where it is valid;
4. all five-dimensional factor-span cases are handled through the actual derivative spaces of the displayed normal forms; and
5. weaker but sufficient local rank rows replace the invalid old rows.

The final arithmetic did not need to change because the repaired rows still dominate the required slope.

## 5. Audit of the local half-defect theorem

Let

\[
T=\ell_1\cdots\ell_6\ne0,
\quad L=\langle\ell_1,\ldots,\ell_6\rangle,
\quad U=\mathcal D_3(T),
\quad F=\mathcal D_2(T),
\]

put `u=dim U` and `R=F cap E_2`, and let

\[
P:L\twoheadrightarrow D
\]

be an arbitrary quotient of rank `d`. The repaired proposition states

\[
\boxed{
\operatorname{rank}\beta_{P,R}+\frac{20-u}{2}
\ge \frac{10}{3}d.}
\]

The audit checked every factor-span dimension `1 <= dim L <= 6`.

### 5.1 Permanent derivative tower and small intersections

The proof establishes

\[
\dim E_3=400,
\qquad
\dim E_2=225,
\qquad
E_2^{(1)}=E_3.
\]

It also uses the valid rank floors

\[
0\ne q\in E_2\Longrightarrow \operatorname{rank}(q)\ge4,
\qquad
0\ne g\in E_3\Longrightarrow \operatorname{essdim}(g)\ge9.
\]

For a linear space `L` of dimension at most six, the closed torus-fixed-point reduction gives

\[
\dim(E_2\cap\operatorname{Sym}^2L)\le3,
\]

with the sharper upper bound one when `dim L <= 5`. At a fixed point this is the exact statement that a bipartite graph with at most five edges contains at most one four-cycle and a graph with six edges contains at most three four-cycles. The finite replay independently reconstructs the coordinate maxima

```text
0, 0, 0, 0, 1, 1, 3
```

for edge counts zero through six.

The specialization and semicontinuity directions are correct: a coordinate fixed point can only have smaller or equal matrix rank, so its lower bound transfers to the original configuration.

### 5.2 Kernel-preimage estimate

Polarization gives an injective map

\[
\delta:\operatorname{Sym}^3L\longrightarrow L\otimes\operatorname{Sym}^2L.
\]

For `S=ker P`, the proof correctly identifies

\[
\ker((P\otimes1)\delta)=\operatorname{Sym}^3S
\]

and obtains the conservative inverse-image bound

\[
\dim\delta^{-1}(D\otimes R)
\le \binom{\ell-d+2}{3}+d\dim R,
\qquad \ell=\dim L.
\]

No transversality or generic-position assumption is inserted.

### 5.3 Factor-span dimension at most four

A diagonal one-parameter degeneration sends the term to a positive-support monomial

\[
x_1^{m_1}\cdots x_\ell^{m_\ell},
\qquad m_j\ge1,
\qquad \sum_jm_j=6.
\]

Middle catalectic rank cannot increase in the limit. Exact positive-partition counting yields the conservative floors

```text
ell = 1, 2, 3, 4
u  >= 1, 2, 4, 8.
```

Combining these floors with the kernel-preimage estimate and full-symbol injectivity produces the displayed rows

\[
\begin{array}{c|c}
\ell&\operatorname{rank}\beta_{P,R}+(20-u)/2\\ \hline
4&(0,9/2,8,10,14)\\
3&(5,15/2,9,12)\\
2&(8,9,11)\\
1&(19/2,21/2).
\end{array}
\]

Each entry dominates `10d/3`.

At full quotient rank, injectivity follows because a kernel cubic would lie simultaneously in `E_2^(1)=E_3` and in a cubic space supported on at most six essential variables, contradicting the nine-variable floor for nonzero elements of `E_3`.

### 5.4 Six independent factors

Here the actual derivative spaces are exactly the squarefree quadratic and cubic spaces. The common diagonal-torus reduction acts simultaneously on the quotient kernel and the subspace `R`.

The replay derives, rather than merely restates, all 45,696 coordinate fixed-point cases and obtains

\[
\begin{array}{c|rrrrrrr}
r\backslash d&0&1&2&3&4&5&6\\ \hline
0&0&10&16&19&20&20&20\\
1&0&9&14&16&16&20&20\\
2&0&8&12&13&16&19&20\\
3&0&7&10&10&15&17&19.
\end{array}
\]

Full-symbol injectivity improves the last entry of the final row from 19 to 20, giving

\[
(0,7,10,10,15,17,20).
\]

This row satisfies the required slope for every quotient rank.

### 5.5 Five-dimensional factor span: actual normal forms

The unique relation among six factors spanning a five-space reduces, after coordinate changes and rescaling, to exactly one support size `s=1,...,5` in the normal form `T_s` above.

Exact differentiation gives

\[
\begin{array}{c|rrrrr}
s&1&2&3&4&5\\ \hline
\dim F&11&11&13&14&15\\
u&14&14&18&20&20.
\end{array}
\]

For `s=3`, the actual middle space contains the nine squarefree cubics other than `x_1x_2x_3`; for `s=4,5`, it contains all ten squarefree cubics. A nonzero rank-one quotient specializes to a coordinate functional. Coordinate incidence gives directional-rank floors five and six respectively; quotienting the quadratic target by `R` loses at most one rank.

Together with the general kernel estimate and full-symbol injectivity, this yields

\[
\begin{array}{c|c}
s&\operatorname{rank}\beta_{P,R}+(20-u)/2\\ \hline
4,5&(0,5,8,13,15,20)\\
3&(1,5,7,12,14,19).
\end{array}
\]

These are weaker than the invalid old formal-space rows but remain sufficient.

### 5.6 The `s=1,2` directional-rank cases

For `s=1`, the actual cubic space is spanned by the ten squarefree cubics and the four cubics `x_1^2 x_j`, `2 <= j <= 5`. Every nonzero direction has derivative rank at least seven: a direction involving some `x_j`, `j >= 2`, exposes seven independent quadratic outputs modulo `x_j L`, while the pure `x_1` direction has rank ten.

For `s=2`, the displayed fourteen-vector basis separates the directional analysis into two exhaustive cases:

- a direction involving some `x_j`, `j >= 3`, gives five distinct pair monomials and two additional independent quadrics modulo `x_j L`; or
- a direction contained in `span(partial_1, partial_2)` gives three pair monomials on `x_3,x_4,x_5`, three nonzero outputs in disjoint two-dimensional blocks, and one nonzero quadratic in the `x_1,x_2` block.

Thus every nonzero direction again has rank at least seven. After quotienting by `R`, every positive-rank symbol has rank at least six.

### 5.7 The rank-four quotient kernel

For `s=1,2` and `d=4`, let `S=ker P` be one-dimensional and let `v` lie in the symbol kernel. The four complementary derivatives of `v` span a subspace of `R`, hence a space of dimension at most one.

If that span were nonzero, a change of complement basis would leave only one nonzero complementary derivative. The cubic `v` would then depend on at most the one kernel direction and one complement direction. Its nonzero quadratic derivative would be a nonzero member of `E_2` supported on at most two variables, contradicting the rank-four floor for `E_2`.

Therefore every complementary derivative vanishes and

\[
v\in\operatorname{Sym}^3S.
\]

The kernel has dimension at most one. Together with full-symbol injectivity at `d=5`, the final row is

\[
(3,9,9,10,16,17),
\]

which also dominates `10d/3`.

### 5.8 Local theorem verdict

The repaired proof covers all actual factor spans and arbitrary quotients. The audit found no remaining unsupported orbit restriction, formal/actual identification, genericity assumption, or unproved local table entry.

## 6. Audit of the global argument

Suppose

\[
\operatorname{perm}_6=\sum_{i=1}^N T_i.
\]

Let `u_i` be the middle catalectic rank of `T_i`, put `delta_i=20-u_i`, and let

\[
\Delta=\sum_i\delta_i.
\]

If the sum of the individual middle images has dimension `400+h`, the symmetric image-span inequality gives

\[
h\le10N-200-\frac{\Delta}{2}.
\]

The proof then forms the global quotient derivative symbol. Its rank is exactly `h`: its kernel consists precisely of tuples whose sum lies in `E_3`, using the proved identity `E_2^(1)=E_3`.

The actual factor spans generate all 36 ambient variables. After ordering the terms, define

\[
W_i=\sum_{j\le i}L_j,
\qquad
d_i=\dim(W_i/W_{i-1}),
\qquad
\sum_i d_i=36.
\]

For the accumulated local symbol images `H_i`, projection to

\[
(W_i/W_{i-1})\otimes Q
\]

kills `H_{i-1}` and proves the increment inequality

\[
\dim H_i-\dim H_{i-1}\ge\dim\pi_i(Z_i).
\]

This is the required dimension argument; local ranks are not simply assumed to add directly.

Applying the local half-defect theorem to each actual quotient gives

\[
h\ge\sum_i\left(\frac{10}{3}d_i-\frac{\delta_i}{2}\right)
=120-\frac{\Delta}{2}.
\]

Comparison cancels the complete individual middle-rank defect:

\[
120-\frac{\Delta}{2}
\le10N-200-\frac{\Delta}{2},
\]

hence

\[
N\ge32.
\]

Glynn's identity supplies a 32-term ordinary Chow decomposition, so equality follows. The constants, inequality directions, quotient injections, filtration increments, and defect cancellation are consistent.

## 7. Exact replay and CI evidence

The repaired replay derives the finite theorem-facing data from underlying combinatorial and polynomial objects:

- coordinate four-cycle intersection maxima through six variables;
- all 45,696 squarefree fixed-point symbol cases;
- exact rational differentiation of all five dependent-factor normal forms;
- the contained squarefree subspaces and directional-incidence floors;
- the failed formal/actual equalities as negative regressions;
- the low-factor-span monomial floors;
- every repaired half-defect row; and
- the final `N=31` gap and `N=32` equality boundary.

The associated GitHub Actions run completed successfully:

```text
workflow: exact-bound-tests
run:      32469992061 (#801)
result:   success
English-only scan: pass
unit tests: 983 passed, 14 opt-in tests skipped
new exact-rank-32 focused tests: 9/9 passed
```

The skipped tests are explicitly gated expensive or GPU replays. The standard hosted suite and the exact-rank repair tests passed; the separate `full-replay` job was not executed in this run.

## 8. Remaining minor finding

The TeX source contains one spacing-command typo in the `s=2` basis display:

```tex
x_2^2x_j+2x_1x_2x_j,qquad
```

It should be

```tex
x_2^2x_j+2x_1x_2x_j,\qquad
```

This is a source/PDF presentation defect only. It does not alter a polynomial, basis vector, rank computation, or logical step. It should be corrected and the PDF rebuilt before final publication.

## 9. Scope limitations

This audit is not:

- a proof-assistant formalization;
- named external human peer review;
- a literature-priority determination;
- a border-Chow-rank result; or
- a proof of `ChowRank(perm_n)=2^(n-1)` for general `n`.

The accepted statement is restricted to ordinary Chow rank of `perm_6` over an algebraically closed characteristic-zero field.

## 10. Final repository disposition

At the frozen repaired head, the internally supported theorem status is

\[
\boxed{\operatorname{ChowRank}(\operatorname{perm}_6)=32.}
\]

Recommended minimal closeout:

1. fix the single TeX `\qquad` typo and rebuild the synchronized PDF;
2. retain the repaired exact script, frozen JSON, and negative regression tests;
3. treat PR #90 as a superseded historical conditional candidate rather than the current proof; and
4. keep the exact head and tree in any merge or release receipt.

No additional proof architecture, solver layer, or broad repository re-audit is required for this claim. Any later modification to the local half-defect theorem, the permanent prolongation identity, the symmetric image-span inequality, or the global filtration requires a new exact-head review.