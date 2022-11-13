from typing import List

import pytest

from _1_two_sums import TwoSums

testdata = [
    ([2, 7, 11, 15], 9, [0, 1])
]


@pytest.mark.parametrize("l, num, expected", testdata)
def test_two_sums(l: List[int], num, expected):
    assert TwoSums.twoSum(l, num) == [0, 1]
