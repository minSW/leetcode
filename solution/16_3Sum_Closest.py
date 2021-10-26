class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res, n = 10 ** 5, len(nums)
        nums.sort()
        
        for first in range(n-2) :
            second, third = first + 1, n - 1
            while second < third :
                three_sum = nums[first] + nums[second] + nums[third]
                res = res if abs(res) < abs(three_sum - target) else three_sum - target
                
                if three_sum < target : second += 1
                elif three_sum > target : third -= 1
                else : return target
        
        return res + target
