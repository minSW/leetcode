class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def xorSum(res: int, index: int) -> int :
            if index == n :
                return res
            return xorSum(res, index + 1) + xorSum(res ^ nums[index], index + 1)
        return xorSum(0, 0)
