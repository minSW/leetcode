class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, lands = len(grid), 0
        matrix = [[ 200 for _ in range(n) ] for _ in range(n) ]
        
        # move to right & bottom
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] :
                    matrix[i][j] = 0
                    lands += 1
                else :
                    if i > 0 : matrix[i][j] = min(matrix[i][j], matrix[i-1][j] + 1)
                    if j > 0 : matrix[i][j] = min(matrix[i][j], matrix[i][j-1] + 1)
        
        if lands == 0 or lands == n * n :
            return -1
        
        res = 0
        
        # move to left & top
        for i in range(n-1, -1, -1) :
            for j in range(n-1, -1, -1) :
                if i < n-1 : matrix[i][j] = min(matrix[i][j], matrix[i+1][j] + 1)
                if j < n-1 : matrix[i][j] = min(matrix[i][j], matrix[i][j+1] + 1)
                res = max(res, matrix[i][j]) 
        return res

                    
#     # Time Limit Exceeded Solution
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         lands = [ (i,j) for i in range(n) for j in range(n) if grid[i][j] ]
        
#         if len(lands) in (0, n**2) :
#             return -1
#         else :
#             return max([ min([ abs(x-i) + abs(y-j) for x, y in lands ]) for i in range(n) for j in range(n) if not grid[i][j] ])

