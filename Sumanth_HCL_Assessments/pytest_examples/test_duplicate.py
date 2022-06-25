import math_func
import pytest


# @pytest.mark.add
def test_add():
    assert math_func.add(2, 3) == 5
    assert math_func.add(9, 2) == 11
    assert math_func.add(20, 30) == 50
    assert math_func.add(28, 32) == 60


def test_product():
    assert math_func.product(2, 3) == 6
    assert math_func.product(10, 5) == 50
    # assert not math_func.product(10, 3) == 30


def test_add_strings():
    assert math_func.add("ketharaju", "Sumanth") == "ketharajuSumanth"
    assert math_func.add("Pamujula", "Sunil") == "PamujulaSunil"


def test_product_strings():
    assert math_func.product("Sumanth", 2) == "SumanthSumanth"
    assert math_func.product("Pamujula", 2) == "PamujulaPamujula"
    assert math_func.product("Sunil", 2) == "SunilSunil"

