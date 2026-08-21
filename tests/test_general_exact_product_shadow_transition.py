from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_exact_product_shadow.py"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "general_exact_product_shadow_transition_test",
        SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load exact product-shadow module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ExactProductShadowTransitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_transition_matches_known_n6_boundaries(self) -> None:
        shadow = self.module.ExactProductShadow(6, 3)
        cases = {
            72: (46, 47, 72, 75),
            75: (50, 51, 75, 78),
            84: (64, 65, 84, 87),
        }
        for threshold, expected in cases.items():
            with self.subTest(threshold=threshold):
                last_good, first_bad = shadow.transition(threshold)
                self.assertEqual(
                    (
                        last_good.family_size,
                        first_bad.family_size,
                        last_good.shadow_size,
                        first_bad.shadow_size,
                    ),
                    expected,
                )

    def test_transition_fails_when_full_layer_is_allowed(self) -> None:
        shadow = self.module.ExactProductShadow(6, 3)
        full_shadow = shadow.minimum(shadow.layer_size**2).shadow_size
        with self.assertRaises(RuntimeError):
            shadow.transition(full_shadow)

    def test_existing_payload_is_unchanged(self) -> None:
        payload = self.module.build_payload()
        self.assertEqual(
            payload["core_sha256"],
            "18eb66f1b9460d2d793c69131cc4ebc0f1087c86b18f14e5638e71e6d629f567",
        )


if __name__ == "__main__":
    unittest.main()
