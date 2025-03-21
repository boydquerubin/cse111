from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city('525 S Center St, Rexburg, ID 83640') == 'Rexburg'
 
def test_extract_state():
    assert extract_state('525 S Center St, Rexburg, ID 83640') == 'ID'

def test_extract_zipcode():
    assert extract_zipcode('525 S Center St, Rexburg, ID 83640') == '83640'

pytest.main(["-v", "--tb=line", "-rN", __file__])