import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = collections.defaultdict(int)
        res = ""
        
        for c in s :
            if c in order : order_dict[c] += 1
            else : res += c
        for x in order :
            res += x * order_dict[x]
        
        return res
