class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums :
            return [[]]
        prev = self.subsets(nums[1:])
        return prev + [[nums[0]] + x for x in prev ]
