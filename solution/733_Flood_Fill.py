class Solution:
    # BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        move = [(1,0), (-1,0), (0,1), (0, -1)]
        
        m, n, oldColor = len(image), len(image[0]), image[sr][sc]
        queue = [(sr, sc)]
        
        while queue :
            x, y = queue.pop(0)
            visited.add((x,y))
            if image[x][y] == oldColor :
                image[x][y] = newColor
                queue += [ (x+i, y+j) for i, j in move if 0 <= x+i < m and 0 <= y+j < n and not (x+i, y+j) in visited ]
        
        return image
