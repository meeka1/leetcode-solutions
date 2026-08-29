class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_t1 = float('inf')  # stores the cheapest price for t1
        profit_t1 = 0  # stores max profit for t1
        buy_t2 = float('inf')  # stores the cheapest price for t2
        profit_t2 = 0  # best profit after second sell (t2)

        for price in prices:
            buy_t1 = min(buy_t1, price)
            profit_t1 = max(profit_t1, price - buy_t1)

            # second transaction can only use profit already earned from first transaction
            buy_t2 = min(buy_t2, price - profit_t1)
            profit_t2 = max(profit_t2, price - buy_t2)
        
        return profit_t2



