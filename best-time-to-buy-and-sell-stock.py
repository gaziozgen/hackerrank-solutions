# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 25.10.2020


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        buy_price = prices[0]
        maxP = 0

        for current_price in prices[1:]:
            buy_price = min(buy_price,current_price)
            maxP = max(maxP,current_price - buy_price)

        return maxP
