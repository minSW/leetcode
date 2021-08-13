from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res, length = 0, len(arr)
        
        for x in sorted(counter, key=lambda x: counter[x], reverse=True):
            res += 1
            length -= counter[x]
            if length <= len(arr) // 2 :
                break
        
        return res
