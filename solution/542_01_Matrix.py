class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [ [ m+n for _ in range(n) ] for _ in range(m) ]
        
        def fill_distance(x: int, y: int, distance: int) :
            if 0 <= x < m and 0 <= y < n :
                res[x][y] = min(res[x][y], distance)
        
        for i in range(m) :
            for j in range(n) :
                if not mat[i][j] :
                    res[i][j] = 0
                fill_distance(i+1, j, res[i][j]+1)
                fill_distance(i, j+1, res[i][j]+1)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1) :
                fill_distance(i-1, j, res[i][j]+1)
                fill_distance(i, j-1, res[i][j]+1)
        
        return res
