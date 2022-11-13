from typing import List


class BestTimeToBuyAndSellStock:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        best_transaction = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > best_transaction:
                best_transaction = price - min_price
        return best_transaction
