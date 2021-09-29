class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res, k = [0], 0
        
        for i in range(len(s)) :
            if s[i] == "I" :
                res.append(i+1)
                k = i+1
            else :
                res.insert(k, i+1)
        
        return res
