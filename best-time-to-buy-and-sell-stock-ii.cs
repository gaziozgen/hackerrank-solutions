// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
// 13.3.2024

public class Solution {
    public int MaxProfit(int[] prices) {

        int possibleBuy = 10000;
        int profit = 0;

        for(int i = 0; i < prices.Length; i++) {
            if (prices[i] > possibleBuy)
                profit += prices[i] - possibleBuy;
            possibleBuy = prices[i];
        }
        return profit;
    }
}
