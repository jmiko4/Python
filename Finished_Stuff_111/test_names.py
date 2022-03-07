from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('John', 'Smith') == 'Smith; John'
    assert make_full_name('Dave', 'Brown') == 'Brown; Dave'
    assert make_full_name('Justin', 'Mikolajcik') == 'Mikolajcik; Justin'
    assert make_full_name('George', 'Washington') == 'Washington; George'

def test_extract_family_name():
    assert extract_family_name('Smith; John') == 'Smith'
    assert extract_family_name('Brown; Dave') == 'Brown'
    assert extract_family_name('Mikolajcik; Justin') == 'Mikolajcik'
    assert extract_family_name('Mc\'donald; Ronald') == 'Mc\'donald'

def test_extract_given_name():
    assert extract_given_name('Smith; John') == 'John'
    assert extract_given_name('Brown; Dave') == 'Dave'
    assert extract_given_name('Mikolajcik; Justin') == 'Justin'
    assert extract_given_name('Mc\'donald; Ronald') == 'Ronald'

pytest.main(["-v", "--tb=line", "-rN", __file__])