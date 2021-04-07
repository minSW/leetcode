class Solution:
    # Use BinarySearch
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r :
            mid = (l + r) // 2
            if nums[mid] > nums[r] :
                l = mid
            elif nums[l] > nums[mid] :
                r = mid
            else :
                return nums[0]
            if r - l == 1 :
                break
                
        return nums[r]
            
#     def findMin(self, nums: List[int]) -> int:
#         for a, b in zip(nums, nums[1:]) :
#             if a > b :
#                 return b
#         return nums[0]
    
