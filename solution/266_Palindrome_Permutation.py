from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return len([ x for x in Counter(s).values() if x % 2 == 1 ]) <= 1
