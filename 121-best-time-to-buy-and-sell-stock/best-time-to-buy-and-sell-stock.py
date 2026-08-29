class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10001

        for price in prices:

            # keeping track of the cheapest price (so far)
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            

        return max_profit
        