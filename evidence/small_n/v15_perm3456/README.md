# Repaired v15 `perm_3`--`perm_6` manuscript

This release adds the complete post-audit proof
`ChowRank(perm_6)=32` to the repaired `n=3,4,5` AMS manuscript. The unified
PDF is 46 A4 pages with 25 mm margins and 111 embedded reviewer attachments.

The `n=6` proof uses the permanent derivative tower, small permanent-quadratic
intersections, a kernel-preimage bound, an exact squarefree projected-symbol
table, repaired half-defect estimates for actual derivative spaces, a symmetric
image-span inequality, and a global filtration. Glynn's identity gives the
32-term upper bound. The finite replay derives all 45,696 coordinate cases and
the five dependent-factor profiles exactly.

The theorem concerns ordinary Chow rank in characteristic zero. It makes no
border-rank or general-`n` claim. This is an internally audited
computer-assisted proof package; named external peer review and proof-assistant
formalization remain outstanding.

Verify the release identities and replay every active `n=3,4,5,6` certificate:

```text
python -m pip install python-flint==0.8.0
python -B verify_assets.py --replay
```

The verifier checks both outer artifacts, validates the inner file manifest,
extracts to a temporary directory, runs the active exact proofs, and verifies
the untouched package again. Missing files, identity drift, finite-count
mismatches, or any proof regression terminate with a nonzero status.
