class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move = [(0,1), (1,0), (0,-1), (-1,0)]
        n, m = len(grid), len(grid[0])
        cnt = 0
        
        def markedIsland(x: int, y: int, target: str) :
            if x < 0 or x >= n or y < 0 or y >= m :
                return
            elif grid[x][y] == "1" :
                grid[x][y] = target
                for a, b in move :
                    markedIsland(x+a, y+b, target)
        
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == "1" :
                    cnt += 1
                    markedIsland(i, j, str(-1 * cnt))
        
        return cnt
