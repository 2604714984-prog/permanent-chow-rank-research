# All-wedge leading-minor scan for `perm_7`

This certificate applies the same explicit lexicographic unitriangular rule
to every wedge degree of the output-degree-four Koszul map.  The sixteen
parent events for each output subpermanent are independent of wedge size, so
one bounded inclusion--exclusion histogram recovers all 49 fixed-size counts.

The computation streams exactly

\[
1225(2^{16}-1)=80,280,375
\]

small integer states and never materializes a Koszul matrix.  Each reported
rank is an integer-minor lower bound in characteristic zero.  The frozen
payload records all wedge degrees and the best exact ratio against the rank
of one product of seven independent linear forms.

## Result

No wedge degree passes the lower-50 test.  The best exact ratio is attained at
the two endpoint degrees \(p=0,48\):

\[
\frac{1225}{35}=35.
\]

The central degree \(p=24\) has the previously frozen rank
\(32,506,369,177,539,449\) and also does not improve the established ordinary
lower bound 49.  Thus changing only the wedge degree while retaining this
leading rule is exhausted and will not be pursued further.

The result is a route diagnostic, not a computation of the full Koszul rank.
Failure of this leading rule at every wedge degree does not rule out another
minor or a larger actual rank.  No border-rank statement is made.

Replay in WSL with all 20 guest CPUs:

```bash
.venv/bin/python scripts/n7_all_wedge_leading_minor_scan.py \
  --workers 20 --verify-json data/n7_all_wedge_leading_minor_scan.json
```
