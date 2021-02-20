class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([ x*x for x in nums ])
    
    # slower, why?
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         i, negative = 0, list()
#         while i < len(nums) :
#             if nums[i] < 0 :
#                 negative.insert(0, pow(nums[i], 2) )
#                 del nums[i]
#             elif negative and negative[0] <= pow(nums[i], 2) :
#                 nums.insert(i, negative[0])
#                 del negative[0]
#                 i += 1
#             else :
#                 nums[i] = pow(nums[i], 2)
#                 i += 1
#         return nums + negative
