class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = { 0 : 0 }
        
        for coin in coins :
            for i in range(coin, amount + 1) :
                if i - coin in dp :
                    dp[i] = min(dp[i], dp[i-coin] + 1) if i in dp else dp[i-coin] + 1
        
        return dp[amount] if amount in dp else -1
