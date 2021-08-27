class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, x in enumerate(nums) :
            nums[i] += (nums[x] % n) * n 
        for i in range(n) :
            nums[i] //= n
        return nums
