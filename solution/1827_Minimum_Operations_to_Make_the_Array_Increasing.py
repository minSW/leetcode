class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, prev = 0, nums[0]
        for x in nums[1:] :
            prev = x if prev < x else prev + 1
            res += prev - x
        return res
