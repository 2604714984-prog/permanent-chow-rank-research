from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from permanent_chow_rank.multishadow import reviewed_general_certificates  # noqa: E402


class MultishadowCsvTests(unittest.TestCase):
    def test_frozen_csv_matches_exact_certificates(self) -> None:
        with (ROOT / "data" / "multishadow_bounds.csv").open(
            "r", encoding="utf-8", newline=""
        ) as handle:
            rows = {int(row["n"]): row for row in csv.DictReader(handle)}

        certificates = {
            certificate.n: certificate
            for certificate in reviewed_general_certificates()
        }
        self.assertEqual(set(rows), set(certificates))

        integer_fields = [
            "output_degree",
            "complementary_degree",
            "witness_numerator",
            "witness_denominator",
            "local_koszul_bound",
            "global_koszul_bound",
            "fixed_terms",
            "complementary_intersection_cap",
            "permanent_koszul_rank",
            "chow_term_koszul_cap",
            "residual_koszul_rank_floor",
            "residual_term_count",
            "lower_bound",
        ]

        for n, certificate in certificates.items():
            row = rows[n]
            self.assertEqual(row["witness"], str(certificate.witness))
            live = certificate.to_dict()
            for field in integer_fields:
                self.assertEqual(int(row[field]), live[field], (n, field))


if __name__ == "__main__":
    unittest.main()
