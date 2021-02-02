class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter_row = dict()
        perimeter_col = dict()
        
        m, n = len(grid), len(grid[0])
        result = 0
        
        start = False
        for i in range(m) :
            end = True
            for j in range(n) :
                if grid[i][j] == 1 :
                    start = True
                    end = False
                    result += 4
                    if (i,j) in perimeter_row :
                        result -= 2
                    if (i,j) in perimeter_col :
                        result -= 2
                    perimeter_row[(i,j)] = True
                    perimeter_row[(i,j+1)] = True
                    perimeter_col[(i,j)] = True
                    perimeter_col[(i+1,j)] = True
                    
            if start and end and not (i,j) in perimeter_row and not (i,j) in perimeter_col: 
                break
        
        return result
