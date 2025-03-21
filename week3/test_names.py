from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("George", "Saint-Pierre") == "Saint-Pierre; George"
    assert make_full_name("Bob", "Tim") == "Tim; Bob"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Saint-Pierre; George") == "Saint-Pierre"
    assert extract_family_name("Tim; Bob") == "Tim"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Toussaint; Marie") == "Marie"
    assert extract_given_name("Washington; George") == "George"
    assert extract_given_name("Saint-Pierre; George") == "George"
    assert extract_given_name("Tim; Bob") == "Bob"

pytest.main(["-v", "--tb=line", "-rN", __file__])