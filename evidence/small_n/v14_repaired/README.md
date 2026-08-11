# Repaired v14 small-n manuscript

Version 14 addresses the two load-bearing mathematical gaps in the external
audit of PR #26:

- it proves the universal one-intersection flag theorem, including the closed
  incidence that preserves the nine-dimensional quotient image and the
  arbitrary tenth quotient direction;
- it restores the squarefree-binary-cubic exclusion as a named
  characteristic-zero lemma with an explicit second-derivative proof.

The flag theorem has one exact computational premise.  The standalone program
reconstructs the integral divided-power coordinate matrices, reduces those
integer matrices modulo 3, and exhausts 886,464 coordinate flags.  The modular
rank inequality is used only to upper-bound the characteristic-zero kernel.
The maximum is 26 (attached orbit), while the four-dimensional and external
maxima are 22.

Accordingly, v14 is described as a computer-assisted characteristic-zero
algebraic-geometric proof with finite combinatorial classifications.  It is not
described as program-free or purely combinatorial.

Run the outer and clean inner checks with:

```text
python -m pip install python-flint==0.8.0
python verify_assets.py --replay
```

The reviewer ZIP verifies its frozen manifest before and after replay, performs
all active `n=3`, `n=4`, and new `n=5` exact checks in a temporary copy, and can
optionally rebuild the 50-page PDF.  No historical 10 GB asset is included.
The `n=5` endpoint verifier itself uses only the Python standard library;
`python-flint` is required only by the independent `n=4` replay.

The equality claim remains a repaired internal research draft until a fresh
external mathematical review accepts the new bridge.
