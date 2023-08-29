import utils
import pytest

lsw_url = ""

def test_get_matching_recipes():
    assert get_matching_recipes("lemon,sugar,water") == requests.get(lsw_url).json().get("hits")
    assert 
