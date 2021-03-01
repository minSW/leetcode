from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([ v * (v - 1) // 2 for v in Counter(nums).values() ])
