class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        delete, head = 0, 0
        
        for i in range(n) :
            if not nums[i] :
                delete += 1     # delete element
            
            if delete > 1 :     # delete count > 1 => slide window
                if not nums[head] : 
                    delete -= 1         # (if kick 0 out the window, can delete another element)
                head += 1
        
        return n - head - 1
        
        
        
#     def longestSubarray(self, nums: List[int]) -> int:
#         cnt = [nums[0]]
#         for x in nums[1:] :
#             if x and cnt[-1] : cnt[-1] += 1
#             else : cnt.append(x)
        
#         n = len(cnt)
#         return max(cnt[:2] + [ cnt[i-2] + cnt[i] for i in range(2, n) if cnt[i] ]) if n > 1 else cnt[0] - 1
