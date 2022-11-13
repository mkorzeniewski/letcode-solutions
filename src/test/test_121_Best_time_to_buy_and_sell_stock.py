from typing import List

import pytest

from _121_Best_Time_to_Buy_and_Sell_Stock import BestTimeToBuyAndSellStock

testdata = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]


@pytest.mark.parametrize("stock, expected", testdata)
def test_maximizeProfit(stock: List[int], expected):
    assert BestTimeToBuyAndSellStock.maxProfit(stock) == expected
