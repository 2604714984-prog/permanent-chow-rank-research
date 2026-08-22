# Reversible lower-50 Hilbert signatures

## Status

`H-01-COMPLETE; H-02-COMPLETE.`

An independent implementation replays the 84 formal first-difference
sequences.  They compress reversibly to seven theorem-relevant signatures:
one each for F1, F2, and F4, and two each for F3 and F5 according to the
degree-six tail.

Each signature records the complete parameter range `delta2=10,...,21`, the
formula for `delta3`, the fixed later differences, `H3` through stabilization,
`q3` through `q6`, and `dim I4`, `dim I5`, `dim I6`.  Expanding the seven rows
recovers exactly the 84 frozen vectors.

The only gauge-free target-integrability subcase is the F3 signature with
`H6=42`, hence `(q5,q6)=(2,0)`.  This is the input selected for the first
pencil theorem.

## Replay

```text
python scripts/n7_b1_hilbert_triples_independent.py
python scripts/n7_lower50_hilbert_signatures.py --verify data/n7_lower50_hilbert_signatures.json
python -m unittest tests.test_n7_b1_hilbert_triples_independent tests.test_n7_lower50_hilbert_signatures -v
```

## Boundary

Compression does not strengthen Macaulay admissibility into geometric
realizability.  The signatures are inputs to H-03 and the corrected TI/W
operators, not point components or lower-bound certificates.
