class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res, char = 0, dict()
        
        for i, c in enumerate(s) :
            if not c in char : char[c] = i
            res = max(res, i - char[c])
        
        return res - 1
