# Erratum for the `n=5` C5 character certificate

Date: 2026-08-09

Status: the pre-2026-08-09 nontrivial-character aggregate is withdrawn and
superseded. The original uncompressed modulo-3 certificate is unaffected.

## Error

The former character-coordinate builder retained six positive fixed target
orbits in every nontrivial character of
`Sym^2(V) tensor Lambda^5(V)`. For a signed orbit of length `d`, sign product
`epsilon`, and character value `zeta`, the orbit contributes only when

```text
epsilon * zeta^d = 1.
```

The six length-one positive fixed orbits therefore occur only in the trivial
character. The correct block shapes are:

- trivial character: `12360 x 9900`;
- each nontrivial character: `12354 x 9900`.

## Superseded aggregate

- former name: `n5_glynn_residual_C5_character_certificate_F11.json`;
- retained upstream audit name:
  `n5_glynn_residual_C5_character_certificate_INVALID_superseded_F11.json`;
- SHA-256:
  `1eaa01886a6371693c4f56b4d63f790da5f3c2afe245785f13e2672aaeb18f45`;
- status: invalid and not citable.

## Corrected aggregate

- name: `n5_glynn_residual_C5_character_certificate_corrected_F11.json`;
- SHA-256:
  `2b254a51d0e641fa60eb0b7ced31f9ea7b299819b9dc49039a27c7a8c58bfb51`;
- total ranks for the two named four-term Glynn residuals: `43634` and
  `43642`;
- margins above `11 * 3846 = 42306`: `1328` and `1336`.

The corrected result is an exact finite-field nonzero-minor certificate for
the two named residuals. It is a route diagnostic, not a pure
characteristic-zero proof and not an unrestricted Chow-rank theorem. The
large SMS matrices and rank records remain external upstream evidence and are
not copied into this lightweight repository.
