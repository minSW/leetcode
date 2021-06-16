class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        def rotateWithLevel(depth: int) -> None :
            n = N - depth * 2
            bound = depth + n - 1
            
            if n <= 1 : return

            for i in range(n - 1) :
                matrix[depth+i][bound], matrix[bound][bound-i], matrix[bound-i][depth], matrix[depth][depth+i] = matrix[depth][depth+i], matrix[depth+i][bound], matrix[bound][bound-i], matrix[bound-i][depth]
            
            rotateWithLevel(depth+1)

        rotateWithLevel(0)
