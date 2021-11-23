class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        k = len(nums) // 2 - 1
        nums.sort()
        
        for i in range(len(nums)-k) :
            if nums[i] == nums[i+k] :
                return nums[i]
