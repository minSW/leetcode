class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def dfs(x: int, path: str) :
            path += str(x)
            
            if len(path) == n :
                res.append(int(path))
            else :
                if x + k < 10 :
                    dfs(x + k, path)
                if k > 0 and x - k >= 0 : 
                    dfs(x - k, path)
        
        for i in range(1, 10) :
            dfs(i, "")
        
        return res
