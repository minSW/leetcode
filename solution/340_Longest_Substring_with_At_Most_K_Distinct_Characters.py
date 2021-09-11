import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k : 
            return 0
        
        distinct = collections.defaultdict(int)
        start = max_len = 0
        
        for i, c in enumerate(s) :
            if distinct[c] == 0 :
                if k > 0 :
                    k -= 1
                elif k == 0 and i > 0 :
                    while start < len(s) and distinct[s[start]] > 0 :
                        distinct[s[start]] -= 1
                        if not distinct[s[start]] :
                            start += 1
                            break
                        start += 1
            distinct[c] += 1
            max_len = max(max_len, i-start+1)
        
        return max_len
