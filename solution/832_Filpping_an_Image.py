class Solution:
    # Simple Solution
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [ [1-x for x in row[::-1]] for row in A ]
    
    # # Better Memory usage Solution
    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    #     n = len(A)
    #     half = n // 2 if n % 2 == 0 else n // 2 + 1
    #     for row in A :
    #         for i in range(half) :
    #             if i == n-1-i : row[i] = (1 - row[i])
    #             else : row[i], row[n-1-i] = (1 - row[n-1-i]), (1 - row[i])
    #     return A
