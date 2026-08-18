from __future__ import annotations
import importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SCRIPT=ROOT/'scripts'/'general_private_polar_shadow_amplification.py'; INDEPENDENT=ROOT/'scripts'/'general_private_polar_shadow_amplification_independent.py'; FROZEN=ROOT/'data'/'general_private_polar_shadow_amplification.json'
def load():
    spec=importlib.util.spec_from_file_location('private_shadow_amp_test',SCRIPT)
    if spec is None or spec.loader is None: raise RuntimeError(SCRIPT)
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
A=load()
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.payload=A.build_payload(); cls.frozen=json.loads(FROZEN.read_text())
    def test_frozen(self): self.assertEqual(self.payload,self.frozen); self.assertEqual(self.payload['core_sha256'],'a158faee3d5aa7e5fe5081fdf485ba3168c58877279e7d270fc7ed383bfab6cd')
    def test_tiers(self):
        for r in range(2,14):
            self.assertEqual(A.exact_linear_shadow(r,1),r*r)
            for b in range(2,r+2): self.assertEqual(A.exact_linear_shadow(r,b),r*(r+1))
            self.assertEqual(A.exact_linear_shadow(r,r+2),r*(r+2))
    def test_pair_boundary(self):
        for m in range(4,30): self.assertGreater(A.exact_linear_shadow(m-1,m+1),m*m-m-1); self.assertEqual(A.exact_linear_shadow(m-1,m),m*m-m)
    def test_independent(self):
        c=subprocess.run([sys.executable,str(INDEPENDENT)],check=True,capture_output=True,text=True,timeout=300); self.assertIn('GENERAL_PRIVATE_POLAR_SHADOW_AMPLIFICATION_INDEPENDENT_PASS',c.stdout)
if __name__=='__main__': unittest.main()
