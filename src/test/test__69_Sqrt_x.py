import pytest

from src.solutions._69_Sqrt_x import SqrtX

testdata = [
    (4, 2),
    (5, 2),
    (9, 3),
    (16, 4),
    (1, 1),
    (15, 3),
    (999998000000, 999998)
]


@pytest.mark.parametrize("num, expected", testdata)
def test_my_sqrt(num, expected):
    assert SqrtX.my_sqrt(num) == expected
