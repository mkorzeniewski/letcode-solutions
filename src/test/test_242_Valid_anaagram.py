import pytest

from _242_valid_anagram import ValidAnagram

testdata = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aa", "a", False)
]


@pytest.mark.parametrize("s1, s2, expected", testdata)
def test_valid_anagram(s1: str, s2: str, expected):
    assert ValidAnagram.isAnagram(s1, s2) == expected
