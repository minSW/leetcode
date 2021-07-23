class Solution:
    # iterative
    def arrayNesting(self, nums: List[int]) -> int:
        checked, res = [0] * len(nums), 0
        
        for i in range(len(nums)) :
            count = 0
            while not checked[i] :
                checked[i] = 1
                count += 1
                i = nums[i]
            res = max(res, count)
        
        return res

    # recursive
#     def arrayNesting(self, nums: List[int]) -> int:
#         checked = [0] * len(nums)
        
#         def dfs(k: int) -> int :
#             if checked[k] :
#                 return 0
#             checked[k] = 1
#             return 1 + dfs(nums[k])
        
#         return max([ dfs(i) for i in range(len(nums)) if not checked[i] ])
