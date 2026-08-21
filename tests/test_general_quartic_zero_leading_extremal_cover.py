from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'scripts'/'general_quartic_zero_leading_extremal_cover.py'
spec=importlib.util.spec_from_file_location('extcover',SCRIPT)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def test_payload():
    p=mod.payload()
    assert p['equality_frames']==288
    assert p['exact_24_matching_covers']==2016
    assert p['row_column_cover_orbits']==18
    assert p['global_maximum_reachable_matching_count']==7
    assert p['extremal_four_zero_cover_first_order']=='EXCLUDED'
