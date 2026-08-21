import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "n7_mixed_glynn_lower_overlap_torus_audit_status.py"
    spec = importlib.util.spec_from_file_location("n7_lower_overlap_audit", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LowerOverlapTorusAuditStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_script()
        cls.payload = json.loads(
            (
                ROOT / "data" / "n7_mixed_glynn_lower_overlap_torus_audit_status.json"
            ).read_text(encoding="utf-8")
        )

    def test_frozen_status_replays_exactly(self):
        self.assertEqual(self.module.build_payload(), self.payload)

    def test_audit_gate_is_complete(self):
        self.assertEqual(self.payload["multi_minor_row_count"], 1189)
        self.assertEqual(self.payload["audited_multi_minor_row_count"], 1189)
        self.assertEqual(self.payload["pending_multi_minor_row_count"], 0)
        self.assertTrue(self.payload["status"].startswith("EXACT_ALL_"))


if __name__ == "__main__":
    unittest.main()
