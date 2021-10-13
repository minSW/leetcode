from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n <= k : return n == k
        return sum([ 1 for v in Counter(s).values() if v % 2 == 1]) <= k
