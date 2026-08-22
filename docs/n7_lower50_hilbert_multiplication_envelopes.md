# `perm_7` H-03 multiplication-rank envelopes

## Result

For a point ideal `I` in seven variables, Macaulay growth gives

\[
\dim(S_1I_d)\geq \dim S_{d+1}-H_d^{\langle d\rangle}.
\]

Together with `S1 I_d subset I_(d+1)`, this bounds the ranks of

\[
I_4\otimes S_1\longrightarrow I_5,
\qquad
I_5\otimes S_1\longrightarrow I_6.
\]

There is no additional rank variable for the displayed H-03 degree-six map:
because `S1 I4 subset I5`, one has

\[
S_2I_4+S_1I_5=S_1I_5.
\]

Applying these bounds to the seven reversible H-02 signatures gives a
Cartesian envelope of 1,894 candidate rank pairs. Each signature represents
12 formal O-sequences, so the fully labelled Cartesian envelope contains
22,728 candidates. The script stores only
the seven intervals and their counts; it never materializes that expansion.

## Claim boundary

Every interval is a necessary numerical envelope. Nonemptiness does not show
that any rank pair is realized by a saturated ideal of 42 distinct points,
and it does not impose permanent-target containment or weighted coupling.
Consequently H-03 alone excludes none of F1 through F5. Its purpose is to
give H-05 and the joint target/coupling tests a finite, memory-bounded input.

## Replay

```text
python scripts/n7_lower50_hilbert_multiplication_envelopes.py --verify data/n7_lower50_hilbert_multiplication_envelopes.json
python -m unittest tests.test_n7_lower50_hilbert_multiplication_envelopes -v
```
