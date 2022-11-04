import pytest

testdata = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
]


@pytest.mark.parametrize("s,expected", testdata)
def test_roman_to_int(s, expected):
    assert RomanToInteger.roman_to_int(s) == expected
