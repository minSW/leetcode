class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        col_sum = [ sum([ mat[j][i] for j in range(n) ]) for i in range(m) ]
        
        return sum([1 for j in range(m) for i in range(n) if mat[i][j] and sum(mat[i]) == 1 and col_sum[j] == 1])
