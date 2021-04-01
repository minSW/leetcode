class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result, row_bound = m * n, n
        
        for row in grid :
            for i in range(row_bound) :
                if row[i] < 0 :
                    row_bound = i
                    break
                else :
                    result -= 1
        return result
