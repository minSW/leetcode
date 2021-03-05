class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums, rank = sorted(nums), dict()
        
        for i in range(len(sorted_nums)) :
            if not sorted_nums[i] in rank :
                rank[sorted_nums[i]] = i
        
        return [ rank[x] for x in nums ]
