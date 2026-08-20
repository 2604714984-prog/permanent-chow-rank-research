import os
import unittest

from scripts import n6_resource_policy as policy


class ResourcePolicyTests(unittest.TestCase):
    def test_parse_auto_and_explicit(self):
        self.assertEqual(policy.parse_worker_argument("auto"), 0)
        self.assertEqual(policy.parse_worker_argument(" 4 "), 4)
        with self.assertRaises(ValueError):
            policy.parse_worker_argument("0")

    def test_explicit_and_gpu_resolution(self):
        self.assertEqual(
            policy.resolve_worker_count(
                3,
                max_workers=12,
                estimated_bytes_per_worker=policy.GIB,
            ),
            3,
        )
        self.assertEqual(
            policy.resolve_worker_count(
                0,
                max_workers=12,
                estimated_bytes_per_worker=policy.GIB,
                gpu=True,
            ),
            1,
        )
        with self.assertRaises(ValueError):
            policy.resolve_worker_count(
                2,
                max_workers=12,
                estimated_bytes_per_worker=policy.GIB,
                gpu=True,
            )
        with self.assertRaises(ValueError):
            policy.resolve_worker_count(
                9,
                max_workers=12,
                estimated_bytes_per_worker=policy.GIB,
            )

    def test_auto_is_bounded(self):
        workers = policy.resolve_worker_count(
            0,
            max_workers=12,
            estimated_bytes_per_worker=policy.GIB,
        )
        self.assertGreaterEqual(workers, 1)
        self.assertLessEqual(workers, 12)
        self.assertLessEqual(
            workers,
            max(1, (os.cpu_count() or 1) - policy.CPU_RESERVE),
        )
        self.assertLessEqual(
            workers * policy.GIB,
            policy.AUTO_MEMORY_BUDGET_BYTES,
        )


if __name__ == "__main__":
    unittest.main()
