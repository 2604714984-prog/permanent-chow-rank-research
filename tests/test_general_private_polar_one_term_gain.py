from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/"scripts"/"general_private_polar_one_term_gain.py"
INDEPENDENT=ROOT/"scripts"/"general_private_polar_one_term_gain_independent.py"
FROZEN=ROOT/"data"/"general_private_polar_one_term_gain.json"

def load_module():
    spec=importlib.util.spec_from_file_location("general_private_polar_one_term_gain_test",SCRIPT)
    if spec is None or spec.loader is None: raise RuntimeError(SCRIPT)
    module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module); return module

AUDIT=load_module()

class PrivatePolarOneTermGainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload=AUDIT.build_payload(); cls.frozen=json.loads(FROZEN.read_text(encoding="utf-8"))
    def test_frozen_payload(self):
        self.assertEqual(self.payload,self.frozen); self.assertEqual(self.payload["core_sha256"],"d7d6715b6ca5a6fb5d3c996178cc7dfc596f1323f13e374951e56928b102bf3e")
    def test_pair_corollary(self):
        for m in range(4,30): self.assertEqual(AUDIT.strict_new_nmax(m,2),(m-1)**2-1)
    def test_named_rows_beyond_parent(self):
        for m,q,n in [(4,3,7),(5,3,12),(6,2,24),(7,2,35),(8,3,31),(10,3,49)]:
            self.assertLessEqual(n,AUDIT.strict_new_nmax(m,q)); self.assertGreater(q*n,m*m+m)
    def test_shifted_equality_rows(self):
        self.assertEqual(AUDIT.equality_row(6,4),12); self.assertEqual(AUDIT.equality_row(8,5),16); self.assertEqual(AUDIT.equality_row(10,6),20); self.assertEqual(AUDIT.equality_row(12,7),24)
    def test_independent_replay(self):
        completed=subprocess.run([sys.executable,str(INDEPENDENT)],check=True,capture_output=True,text=True,timeout=300)
        self.assertIn("GENERAL_PRIVATE_POLAR_ONE_TERM_GAIN_INDEPENDENT_PASS",completed.stdout); self.assertIn("independent_simplex_cases=",completed.stdout)

if __name__=="__main__": unittest.main()
