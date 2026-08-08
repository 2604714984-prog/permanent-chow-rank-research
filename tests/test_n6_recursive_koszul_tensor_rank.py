from __future__ import annotations

import importlib.util
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n6_recursive_koszul_tensor_rank_audit.py"
FROZEN = ROOT / "data" / "n6_recursive_koszul_tensor_rank_audit.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("n6_recursive_koszul_tensor_rank_audit", SCRIPT)


def compact(payload: dict[str, object]) -> dict[str, object]:
    prime_replays = payload["prime_replays"]
    first = prime_replays["1000003"]
    return {
        "status": payload["status"],
        "source_identity": {
            key: payload["source_identity"][key]
            for key in (
                "paper",
                "upstream_repository",
                "upstream_main_commit",
                "upstream_per6_blob",
                "upstream_rank_helper_blob",
            )
        },
        "matrix_dimension": payload["flattening"]["matrix_rows"],
        "generated_integer_entries": payload["flattening"][
            "generated_integer_entries"
        ],
        "canonical_edge_stream_sha256": payload["flattening"][
            "canonical_edge_stream_sha256"
        ],
        "component_count": payload["flattening"][
            "bipartite_component_count"
        ],
        "rank_one_normalization": payload["flattening"][
            "rank_one_normalization"
        ],
        "component_histogram": first["component_histogram"],
        "prime_total_ranks": {
            prime: row["total_rank"]
            for prime, row in sorted(prime_replays.items())
        },
        "characteristic_zero_rank_lower_bound": payload[
            "characteristic_zero_rank_lower_bound"
        ],
        "border_tensor_rank_lower_bound": payload[
            "border_tensor_rank_lower_bound"
        ],
        "ordinary_tensor_rank_lower_bound": payload[
            "ordinary_tensor_rank_lower_bound"
        ],
        "restricted_family_intervals": {
            "row_homogeneous": payload["restricted_family_consequences"][
                "row_homogeneous_interval"
            ],
            "two_defect_sign": payload["restricted_family_consequences"][
                "two_defect_sign_interval"
            ],
        },
        "route_decision": payload["route_decision"],
        "claim_boundary": payload["claim_boundary"],
    }


class N6RecursiveKoszulTensorRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = AUDIT.build_payload()

    def test_matrix_and_component_invariants(self) -> None:
        flattening = self.payload["flattening"]
        self.assertEqual(flattening["matrix_rows"], 162_000)
        self.assertEqual(flattening["matrix_columns"], 162_000)
        self.assertEqual(flattening["generated_integer_entries"], 1_800_000)
        self.assertEqual(flattening["stored_nonzero_entries"], 1_800_000)
        self.assertEqual(flattening["entry_values"], [-1, 1])
        self.assertEqual(flattening["bipartite_component_count"], 2_932)
        self.assertEqual(flattening["rank_one_normalization"], 2_500)

    def test_prime_replays_and_rank_bound(self) -> None:
        replays = self.payload["prime_replays"]
        self.assertEqual(set(replays), {"1000003", "1000033"})
        self.assertEqual(
            [replays[prime]["total_rank"] for prime in sorted(replays)],
            [70_692, 70_692],
        )
        self.assertEqual(
            replays["1000003"]["component_histogram"],
            replays["1000033"]["component_histogram"],
        )
        self.assertEqual(
            sum(
                row["component_count"]
                for row in replays["1000003"]["component_histogram"]
            ),
            2_932,
        )
        self.assertEqual(
            sum(
                row["rank_contribution"]
                for row in replays["1000003"]["component_histogram"]
            ),
            70_692,
        )
        self.assertEqual(math.ceil(70_692 / 2_500), 29)
        self.assertEqual(self.payload["border_tensor_rank_lower_bound"], 29)
        self.assertEqual(self.payload["ordinary_tensor_rank_lower_bound"], 29)

    def test_route_boundary(self) -> None:
        consequences = self.payload["restricted_family_consequences"]
        self.assertEqual(consequences["row_homogeneous_interval"], [29, 32])
        self.assertEqual(consequences["two_defect_sign_interval"], [29, 32])
        self.assertEqual(consequences["one_defect_exact_repository_result"], 32)
        decision = self.payload["route_decision"]
        self.assertEqual(
            decision["row_homogeneous_decomposition_with_at_most_28_terms"],
            "impossible",
        )
        self.assertFalse(decision["sign_family_can_falsify_unrestricted_lower_26"])
        self.assertFalse(decision["broad_sign_optimization_authorized"])

    def test_frozen_summary(self) -> None:
        frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(compact(self.payload), frozen)


if __name__ == "__main__":
    unittest.main()
