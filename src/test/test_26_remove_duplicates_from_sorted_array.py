import pytest

from src.solutions._26_remove_duplicates_from_sorted_array import DuplicatesSortedArray

testdata = [
    ([1, 1, 2], 2, [1, 2, None]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, None, None, None, None, None])
]


@pytest.mark.parametrize("nums, output, res", testdata)
def test_remove_duplicates_from_array(nums, output, res):
    assert DuplicatesSortedArray.remove(nums) == output
    assert nums[:output] == res[:output]
