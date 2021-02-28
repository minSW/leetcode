class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        elif len(nums) < 3:
            return max(nums)
        
        n = len(nums)
        dp0, dpnot0 = {}, {0: 0, 1: nums[1]}
        
        for i in range(len(nums)) :
            if i < 2 :
                dp0[i] = max(nums[:i+1])
            elif i == len(nums) - 1 :
                dpnot0[i] = max(nums[i]+dpnot0[i-2], dpnot0[i-1])
            else :
                dp0[i] = max(nums[i]+dp0[i-2], dp0[i-1])
                dpnot0[i] = max(nums[i]+dpnot0[i-2], dpnot0[i-1])
        
        return max(dp0[n-2], dpnot0[n-1])
    
    
    # Best Solution - O(n) time, O(1) memory
#     def rob(self, nums: List[int]) -> int:
#         def rob_with_range(nums, start, end) :
#             rob, not_rob = 0, 0
#             for i in range(start, end) :
#                 rob, not_rob = nums[i] + not_rob, max(rob, not_rob)
#             return max(rob, not_rob)
        
#         n = len(nums)
        
#         if not nums :
#             return 0
#         elif n < 3:
#             return max(nums)
#         else :
#             n = len(nums)
#             return max(rob_with_range(nums, 0, n-1), rob_with_range(nums, 1, n))
    
    
    # Wrong Solution - Time Limit Exceeded
#     def rob(self, nums: List[int]) -> int:
#         return max(nums[0] + rob_noncycle(nums[2:-1]), rob_noncycle(nums[1:]))
    
#     def rob_noncycle(self, nums: List[int]) -> int :
#         if not nums :
#             return 0
#         elif len(nums) < 3 :
#             return max(nums)
        
#         return max(nums[0] + self.rob_noncycle(nums[2:]), self.rob_noncycle(nums[1:]))
