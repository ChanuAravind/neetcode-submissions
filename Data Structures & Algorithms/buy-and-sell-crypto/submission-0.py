class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cur_min = float('inf')
        profit = 0

        for price in prices:
            if price < cur_min:
                cur_min = price
            cur_profit = price-cur_min
            if profit< cur_profit:
                profit = cur_profit
        return profit
        