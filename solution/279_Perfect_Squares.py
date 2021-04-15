import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10000] * (n+1)
        
        dp[0] = 0
        for i in range(1, n+1) :
            dp[i] = min(dp[i-j*j] for j in range(1, int(math.sqrt(i)) + 1)) + 1
        
        return dp[n]
    
    # Time Limit Exceeded Solution
#     def numSquares(self, n: int) -> int:
#         k = int(math.sqrt(n))
#         if n == k * k :
#             return 1
        
#         result = 10000
#         for i in range(k, 0, -1) :
#             tmp = self.numSquares(n-i*i)
#             result = min(result, tmp + 1)
#         return result
