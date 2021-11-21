class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(1 for i in range(len(s)-2) if len(set(s[i:i+3])) == 3)
