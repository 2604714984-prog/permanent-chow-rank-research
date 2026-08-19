from __future__ import annotations
import importlib.util, json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PRIMARY=ROOT/'scripts'/'general_quartic_four_block_zero.py'
INDEPENDENT=ROOT/'scripts'/'general_quartic_four_block_zero_independent.py'
DATA=ROOT/'data'/'general_quartic_four_block_zero.json'
def load():
    spec=importlib.util.spec_from_file_location('general_quartic_four_block_zero',PRIMARY)
    if spec is None or spec.loader is None: raise RuntimeError(PRIMARY)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.p=load()
    def test_pair_equality_state(self):
        self.assertEqual(self.p.pair_equality_states(),[{"r1":6,"r2":6,"intersection":3,"joint":9,"private1":3,"private2":3}])
    def test_exact_shadow_interfaces(self):
        self.assertEqual(self.p.product_shadow_minimum(6,2,4)[0],8)
        self.assertEqual(self.p.cubic_two_plane_linear_shadow()["minimum_linear_shadow"],12)
    def test_dimension_contradiction(self):
        core=self.p.theorem_core()
        self.assertEqual(core["initial_pair_supported_polar_floor"],4)
        self.assertEqual(core["forced_pair_span"],9)
        self.assertEqual(core["refined_pair_supported_polar_floor"],7)
        self.assertEqual(core["pair_span_two_plane_capacity"],1)
        self.assertEqual(core["conclusion"],"UNIVERSAL_ZERO")
    def test_frozen_payload(self):
        self.assertEqual(self.p.build_payload(),json.loads(DATA.read_text()))
    def test_independent(self):
        r=subprocess.run([sys.executable,str(INDEPENDENT)],cwd=ROOT,check=True,capture_output=True,text=True)
        self.assertIn('GENERAL_QUARTIC_FOUR_BLOCK_ZERO_INDEPENDENT_PASS',r.stdout)
if __name__=='__main__': unittest.main()
