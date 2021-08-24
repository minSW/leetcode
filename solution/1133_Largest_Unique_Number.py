from collections import Counter
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max([ k for k, v in Counter(A).items() if v == 1 ] + [-1])
