import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = (
        ROOT
        / "scripts"
        / "n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.py"
    )
    spec = importlib.util.spec_from_file_location("n7_overlap23_closure", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Overlapping23RankOneUpdateSupportClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT
                / "data"
                / "n7_mixed_glynn_overlapping_23_rank_one_update_support_closure.json"
            ).read_text(encoding="utf-8")
        )

    def test_exact_certificates_are_frozen(self):
        self.assertEqual(
            self.payload["status"],
            "EXACT_ALL_OVERLAPPING_23_32_PROJECTIVE_SUPPORT_CLOSURE",
        )
        self.assertEqual(
            self.payload["certificate_statuses"],
            {
                label: expected_status
                for label, (_filename, expected_status) in self.module.CERTIFICATES.items()
            },
        )

    def test_dense_internal_faces_are_complete(self):
        self.assertEqual(
            self.payload["dense_chart_summary"],
            {
                "candidate_count": 600,
                "direct_primary_minor_rows": 193,
                "first_internal_face_rows": 357,
                "second_internal_face_rows": 50,
                "unresolved_rows": 0,
            },
        )

    def test_every_projective_coordinate_face_has_an_exact_family(self):
        self.assertEqual(
            self.payload["boundary_face_map"], self.module.FACE_MAP
        )
        known = set(self.payload["certificate_statuses"])
        for shape in ("extra_left", "extra_right"):
            face_map = self.payload["boundary_face_map"][shape]
            mapped = {
                family
                for equation, family in face_map.items()
                if equation != "homogeneous_coordinates"
            }
            self.assertTrue(mapped <= known)
            self.assertEqual(len(face_map) - 1, 5)

    def test_claim_boundary_stays_restricted(self):
        self.assertIn("invalid-tail rank 42", self.payload["conclusion"])
        boundary = " ".join(self.payload["claim_boundary"])
        self.assertIn("no multivariate-gcd inference", boundary)
        self.assertIn("ordinary lower 50", boundary)
        self.assertIn("border rank", boundary)


if __name__ == "__main__":
    unittest.main()
