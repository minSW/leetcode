class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        length = len(s)
        
        for i in range(0, length) :
            result += (ord(s[i]) - 64) * (26 ** (length - i - 1))
        
        return result
