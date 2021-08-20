from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(Counter(s).values())
        res = 0
        
        for x in sorted(counter.keys(), reverse=True) :
            if counter[x] > 1 :
                for i in range(1, x) :
                    if counter[x] == 1 :
                        break
                    if not x - i in counter :
                        res += i
                        counter[x] -= 1
                        counter[x-i] = 1
            
            if counter[x] != 1 :
                res += x * (counter[x]-1)
        
        return res
    
