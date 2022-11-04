import pytest

from src.solutions._88_Merge_sorted_arrays import MergeSortedArrays

testdata = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6, 9], 4, [1, 2, 2, 3, 5, 6, 9]),
    ([5, 6, 7, 0, 0, 0, 0], 3, [1, 2, 3, 4], 4, [1, 2, 3, 4, 5, 6, 7]),
    ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
    ([-1,-1,0,0,0,0], 4, [-1,0], 2, [-1,-1,-1,0,0,0]),
    ([1], 1, [], 0, [1]),
    ([0], 1, [], 0, [0])
]


@pytest.mark.parametrize("num1, n, num2, m, expected", testdata)
def test_merge(num1, n, num2, m, expected):
    in_place_array = num1.copy()
    MergeSortedArrays.merge(in_place_array, n, num2, m)
    assert in_place_array == expected

    in_place_array = num1.copy()
    MergeSortedArrays.simple(in_place_array, n, num2, m)
    assert in_place_array == expected
