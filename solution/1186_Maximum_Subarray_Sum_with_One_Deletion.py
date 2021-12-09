class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp, dp_can_delete = [0] * n, [0] * n
        
        for i, x in enumerate(arr) :
            if i == 0 :
                dp[0] = dp_can_delete[0] = x
            elif i == 1 :
                dp[1] = dp_can_delete[1] = x + max(0, dp[i-1])
            else :
                dp[i] = x + max(0, dp[i-1])
                dp_can_delete[i] = x + max(0, dp_can_delete[i-1], dp[i-2])
        
        return max(dp_can_delete)
