class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if (s1.count("x") + s2.count("x")) % 2 != 0 :
            return -1
        
        x1 = y1 = 0
        for i in range(len(s1)) :
            if s1[i] != s2[i] : 
                if s1[i] == "x" : x1 += 1
                else : y1 += 1
        
        res = 0
        res += abs(x1 - y1) // 2 # swap 1
        res += (min(x1, y1) + 1) // 2 * 2 # swap 2
        return res
