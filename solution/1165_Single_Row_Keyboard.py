class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = [0] * 26
        res = prev = 0
        
        for i, k in enumerate(keyboard) :
            index[ord(k) - ord('a')] = i
        
        for w in word :
            res += abs(index[ord(w) - ord('a')] - prev)
            prev = index[ord(w) - ord('a')]
        
        return res
