from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'scripts'/'general_quartic_zero_leading_first_order.py'
spec=importlib.util.spec_from_file_location('zero_leading',SCRIPT)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def test_payload():
    p=mod.payload()
    assert p['supports_checked']==14893
    assert p['maximum_first_order_matching_envelope']==6
    assert p['equality_supports']==288
    assert p['equality_row_column_orbits']==2
    assert p['orbit_sizes']==[144,144]
    assert p['explicit_four_frame_cover_union']==24
    assert p['zero_leading_count_reduction']=='NOT_PROVED_BY_SUPPORT_ONLY'
