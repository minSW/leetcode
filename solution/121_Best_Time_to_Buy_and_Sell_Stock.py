class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [prices[i+1] - prices[i] for i in range(0, len(prices) - 1)]
        
        max_profit = 0
        if profits :
            sub = [profits[0]]
            for i in range(1, len(profits)):
                sub.insert(i, max(profits[i], sub[i-1] + profits[i]))
            max_profit = max(max(sub), 0)
        
        return max_profit
