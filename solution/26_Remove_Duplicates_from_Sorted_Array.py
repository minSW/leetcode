class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicated = None
        i = 0
        while i < len(nums) :
            if duplicated == None or nums[i] != duplicated:
                duplicated = nums[i]
                i += 1
            else :
                nums.remove(duplicated)
        
        return len(nums)
