class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums : 
            res ^= x
        return res
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     return sum(set(nums)) * 2 - sum(nums)
