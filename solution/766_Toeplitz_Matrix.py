class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for x in range(n+m-1) :
            prev = -1
            for i in range(min(m, x+1)) :
                if x - i >= n :
                    continue
                if prev >= 0 and prev != matrix[m-1-i][x-i] :
                    return False
                prev = matrix[m-1-i][x-i]
        
        return True
