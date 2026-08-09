# Content identities for small-`n` audit files

The following are Git blob object IDs for the exact files currently committed on `main`. They are content-addressed Git SHA-1 identifiers, **not** SHA-256 values.

| Path | Git blob ID |
|---|---|
| `perm345_v9_audit_summary.json` | `49b2dbace3b0e8cb1eda70e870e3cb78d9c12db2` |
| `perm345_v9_strict_external_audit.md` | `bfadee72a376f9749bbc66c9dc61e346e9ffaee4` |
| `perm4_independent_certificate_audit.py` | `c50cb90cf238ea4f9fda89507b718ca326c87220` |
| `perm345_v9_independent_math_audit.py` | `8ca5d319c815afe1b69ba09b74962752fcdd9db6` |
| `perm345_v9_independent_math_audit_output.txt` | `95a163257976146b7cd1eef8f57af46b338a481c` |
| `n5_c5_character_certificate_erratum.md` | `9581953f29c63bb20a639a3245f164dca2f46ddd` |
| `n5_c5_character_certificate_corrected_summary.json` | `052786ea7dbc8c8d1ead5f9d1ae9eeee4de9fd48` |

The original external submission identities remain SHA-256 values and are recorded in `README.md` and `perm345_v9_audit_summary.json`.

A prior `SHA256SUMS` file was removed because one locally reconstructed English report was not byte-identical to the earlier sandbox artifact whose digest had been copied. The current table records only identities verified against the committed GitHub blobs.
