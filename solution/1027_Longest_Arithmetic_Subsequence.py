class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp, n = dict(), len(nums)
        for i in range(n):
            for j in range(i+1, n) :
                diff = nums[j] - nums[i]
                dp[j, diff] = dp[i, diff] + 1 if (i, diff) in dp else 2
        return max(dp.values())
        
#     def longestArithSeqLength(self, nums: List[int]) -> int:
#         res, n = 0, len(nums)
#         indices = collections.defaultdict(list)
        
#         for i, x in enumerate(nums) : 
#             indices[x].append(i)
        
#         for i in range(n) : 
#             for j in range(i+1, n) :
#                 cnt, diff = 2, nums[j] - nums[i]
                
#                 if diff == 0 :
#                     cnt = len(indices[nums[i]])
#                 else :
#                     index = j
#                     while nums[index] + diff in indices :
#                         target = [ t for t in indices[nums[index] + diff] if t > index ]
#                         if not target :
#                             break
#                         cnt += 1
#                         index = target[0]
                
#                 res = max(res, cnt)
        
#         return res
