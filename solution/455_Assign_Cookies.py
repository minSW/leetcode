class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = i = 0
        
        for cookie in s : 
            if i == len(g) :
                break
            elif cookie >= g[i] :
                res += 1
                i += 1
        
        return res
