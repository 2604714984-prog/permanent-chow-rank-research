import importlib.util,json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'scripts'/'general_quartic_three_block_zero.py';I=ROOT/'scripts'/'general_quartic_three_block_zero_independent.py';D=ROOT/'data'/'general_quartic_three_block_zero.json'
def load():
 s=importlib.util.spec_from_file_location('x',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.p=load()
 def test_table(self):self.assertEqual([x['shadow'] for x in self.p.exact_shadow_table()[0]],[4,6,6,8,8,8,9,9])
 def test_no_disjoint_state(self):self.assertEqual(self.p.disjoint_pair_states(self.p.exact_shadow_table()[0]),[])
 def test_core(self):self.assertEqual(self.p.core()['mu_8_4'],4)
 def test_payload(self):self.assertEqual(self.p.payload(),json.loads(D.read_text()))
 def test_independent(self):
  r=subprocess.run([sys.executable,str(I)],cwd=ROOT,check=True,capture_output=True,text=True);self.assertIn('INDEPENDENT_PASS',r.stdout)
if __name__=='__main__':unittest.main()
