import pytest
from src.solutions._13_Roman_to_Integer import RomanToInteger

testdata = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
]


@pytest.mark.parametrize("s,expected", testdata)
def test_roman_to_int(s, expected):
    assert RomanToInteger.roman_to_int(s) == expected
