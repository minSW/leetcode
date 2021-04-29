class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        gap = nums[-1] - nums[0] - len(nums) + 1
        if k - gap > 0 :
            return nums[-1] + k - gap
        
        for i in range(len(nums)-1) :
            diff = nums[i+1] - nums[i] - 1
            if diff >= k :
                return nums[i] + k
            else :
                k -= diff
        return nums[-1] + k
