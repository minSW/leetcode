class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def getCombine(i: int, path: List[int], remain: int) :
            if remain == 0 : 
                res.append(path)
            elif i + remain <= n + 1 :
                getCombine(i+1, path + [i], remain-1)
                getCombine(i+1, path, remain)
        
        getCombine(1, [], k)
        return res
