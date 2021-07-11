import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = collections.defaultdict(int)
        for i in range(0, len(s)-10) :
            if i+10 > len(s) : break
            res[s[i:i+10]] += 1
        return [ k for k in res.keys() if res[k] > 1 ]
