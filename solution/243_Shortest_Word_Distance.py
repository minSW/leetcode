class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = i2 = res = len(wordsDict)
        
        for i, w in enumerate(wordsDict) :
            if w == word1 :
                i1 = i
                res = min(res, abs(i1-i2))
            elif w == word2 :
                i2 = i
                res = min(res, abs(i1-i2))
        
        return res
