import pytest

from src.solutions._80_remove_duplicates_from_sorted_array_2 import DuplicatesSortedArray2

testdata = [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3, None]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3, None, None]),
    ([1, 1], 2, [1, 1]),
    ([1, 1, 1], 2, [1, 1, None]),
    ([1, 2, 2], 3, [1, 2, 2]),
    ([1, 1, 2], 3, [1, 1, 2])
]


@pytest.mark.parametrize("nums, output, res", testdata)
def test_remove_duplicates_from_array(nums, output, res):
    assert DuplicatesSortedArray2.remove(nums) == output
    assert nums[:output] == res[:output]
