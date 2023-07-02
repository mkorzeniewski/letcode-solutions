import pytest

from src.solutions._3_longest_substring_without_repeating_chars import LongestSubstring

testdata = [
    ("abcabcbb", 3),
    ("bbbb", 1),
    ("pwwkew", 3),
    ("aab", 2),
    ("dvdf", 3),
    ("cdd", 2)
]


@pytest.mark.parametrize("strs, expected", testdata)
def test_longest_substring_without_repeating_chars(strs, expected):
    assert LongestSubstring.longest_substring(strs) == expected


@pytest.mark.parametrize("strs, expected", testdata)
def test_longest_substring_without_repeating_chars_set(strs, expected):
    assert LongestSubstring.longest_substring_set(strs) == expected
