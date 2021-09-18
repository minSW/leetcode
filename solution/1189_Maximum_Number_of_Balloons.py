from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res, counter = 10000, Counter(text)
        for c in set('balloon') :
            if not c in counter : 
                return 0
            res = min(res, counter[c]) if not c in 'lo' else min(res, counter[c] // 2)
        return res
