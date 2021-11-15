class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r, x in enumerate(nums) :
            k -= 1 - x
            if k < 0 :
                k += 1 - nums[l]
                l += 1
        return r - l + 1

#     def longestOnes(self, nums: List[int], k: int) -> int:
#         # 0 -> 1 -> 0 -> 1 ..
#         cnt = [0]
#         prev = 0
        
#         for x in nums :
#             if x == prev :
#                 cnt[-1] += 1
#             else :
#                 cnt.append(1)
#                 prev = x
        
#         res, n = min(k, len(nums)), len(cnt)
#         for i in range(1, n, 2) :
#             now, remain = cnt[i], k
            
#             for j in range(i+1, n, 2) :
#                 if not remain :
#                     break
#                 elif remain >= cnt[j] and j != n-1 :
#                     now += cnt[j+1]
#                 remain -= min(remain, cnt[j])
#             res = max(res, now + k + min(cnt[i-1]-remain, 0))
        
#         return res
