from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max([0] + [ counter[x] + counter[x+1] for x in sorted(counter)[:-1] if x+1 in counter ])
