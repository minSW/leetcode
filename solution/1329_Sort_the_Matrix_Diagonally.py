class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat[0])
        m = len(mat)
        output = [ [ 0 for i in range(n) ] for i in range(m) ]
        
        for start in range(0, n) :
            sorted_list = sorted([ mat[dia][start + dia] for dia in range(0, min(m, n - start)) ])
            for i in range(0, len(sorted_list)) :
                output[i][start + i] = sorted_list[i]
        
        for start in range(1, m) :
            sorted_list = sorted([ mat[start + dia][dia] for dia in range(0, min(n, m - start)) ])
            for i in range(0, len(sorted_list)) :
                output[start + i][i] = sorted_list[i]
        
        return output
