class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)) :
            if res and res[-1] == s[i] :
                res = res[:-1]
            else :
                res += s[i]
        
        return res
