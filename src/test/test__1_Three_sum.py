from typing import List

import pytest

from _15_three_sums import ThreeSums

testdata = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1,0,1,2,-1,-4,-2,-3,3,0,4], [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])
]


@pytest.mark.parametrize("l, expected", testdata)
def test_two_sums(l: List[int], expected):
    assert {tuple(x) for x in ThreeSums.threeSum(l)} == {tuple(x) for x in expected}
