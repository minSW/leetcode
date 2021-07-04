class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = sorted(nums)[len(nums) // 2]
        return sum(abs(i - mid) for i in nums)
