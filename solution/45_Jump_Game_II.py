class Solution:
    def jump(self, nums: List[int]) -> int:
        res = n = len(nums)
        if n == 1 : 
            return 0
        
        for i in range(n-2, -1, -1) :
            if i + nums[i] >= n-1 :
                res = i
        
        return 1 + self.jump(nums[:res+1])

    # Time Limit Exceeded Solution
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [n] * n
        
#         def dfs(index: int, cnt: int) -> int :
#             if dp[index] <= cnt :
#                 return
#             dp[index] = cnt
            
#             if index + nums[index] >= n-1 :
#                 dp[-1] = min(dp[-1], cnt + 1)
#                 return
            
#             for i in range(1, nums[index]+1) :
#                 if index + i < n-1 :
#                     dfs(index+i, cnt+1)
        
#         dfs(0, 0)
#         return dp[-1]
