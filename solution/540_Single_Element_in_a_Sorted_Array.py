class Solution:
    # O(log n) time O(1) space
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right :
            mid = (left + right) // 2
            compare = mid + 1 if mid % 2 == 0 else mid - 1 
            
            if nums[mid] == nums[compare]:
                left = mid + 1
            else :
                right = mid
        
        return nums[left]
        
    # O(n) time O(1) space
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     single = 0
    #     for x in nums :
    #         single ^= x
    #     return single
