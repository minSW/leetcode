class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def getMaxCount(x: str, subs: set[str]) -> int :
            res = 0
            for i in range(len(x)) :
                if not x[:i+1] in subs:
                    res = max(res, 1 + getMaxCount(x[i+1:], subs|{x[:i+1]}))
            return res
        
        return getMaxCount(s, set())
