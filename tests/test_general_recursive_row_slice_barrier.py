import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "general_recursive_row_slice_barrier.py"
FROZEN = ROOT / "data" / "general_recursive_row_slice_barrier.json"


spec = importlib.util.spec_from_file_location("recursive_row_slice", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class RecursiveRowSliceBarrierTests(unittest.TestCase):
    def test_frozen_payload(self):
        payload = module.build_payload()
        module.validate(payload)
        self.assertEqual(payload, json.loads(FROZEN.read_text(encoding="utf-8")))

    def test_last_row_rank_formula(self):
        for n in range(3, 7):
            for m in range(n):
                row = module.row_slice_entry(n, m)
                self.assertEqual(
                    row["permanent_rank"],
                    module.choose(n - 1, m) * module.choose(n, m),
                )

    def test_cofactor_intersection_formula(self):
        for n in range(3, 7):
            for m in range(n):
                for s in range(1, n + 1):
                    entry = module.intersection_entry(n, m, s)
                    self.assertEqual(
                        entry["intersection_dimension"],
                        module.choose(n - 1, m) * module.choose(n - s, m),
                    )

    def test_explicit_basis_union_and_intersections(self):
        for n in range(3, 7):
            for m in range(n):
                bases = [module.cofactor_basis(n, m, j) for j in range(n)]
                self.assertEqual(
                    len(set().union(*bases)),
                    module.choose(n - 1, m) * module.choose(n, m),
                )
                for s in range(1, n + 1):
                    self.assertEqual(
                        len(set.intersection(*bases[:s])),
                        module.choose(n - 1, m) * module.choose(n - s, m),
                    )

    def test_small_n_doubling_fails_at_even_steps(self):
        payload = module.build_payload()
        flags = {
            row["n"]: row["row_slice_doubling_from_previous_n"]["holds"]
            for row in payload["small_n"]
        }
        self.assertEqual(flags, {3: True, 4: False, 5: True, 6: False})

    def test_command_replay(self):
        run = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(json.loads(run.stdout), module.build_payload())


if __name__ == "__main__":
    unittest.main()
