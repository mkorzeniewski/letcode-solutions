import pytest

from src.solutions._125_valid_palindrome import ValidPalindrome

testdata = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("a.", True)
]


@pytest.mark.parametrize("s, expected", testdata)
def test_valid_palindrome(s: str, expected):
    assert ValidPalindrome.isPalindrome(s) == expected
