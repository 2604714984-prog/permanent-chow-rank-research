from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "n7_lower50_section_caps_audit.py"
SPEC = importlib.util.spec_from_file_location("n7_lower50_section_caps_audit", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class Lower50SectionCapsAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.build_certificate()
        MODULE.validate(cls.payload)

    def test_load_bearing_caps(self) -> None:
        caps = self.payload["full_section_cap_table"]
        self.assertEqual(caps["6"][47], 37)
        self.assertEqual(caps["6"][48], 44)

    def test_two_dp_and_small_bruteforce_controls(self) -> None:
        control = self.payload["small_coordinate_control"]
        self.assertEqual(control["families_checked"], 512)
        self.assertEqual(
            control["minimum_simultaneous_shadow_by_area"],
            [0, 4, 6, 6, 8, 8, 9, 9, 9, 9],
        )

    def test_frozen_payload(self) -> None:
        frozen = json.loads(
            (ROOT / "data" / "n7_lower50_section_caps_audit.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.payload, frozen)


if __name__ == "__main__":
    unittest.main()
