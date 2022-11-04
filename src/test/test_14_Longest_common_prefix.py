import pytest

from src.solutions._14_Longest_Common_Prefix import LongestCommonPrefix

testdata = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
]


@pytest.mark.parametrize("strs, expected", testdata)
def test_longest_common_prefix(strs, expected):
    assert LongestCommonPrefix.longest_common_prefix(strs) == expected
