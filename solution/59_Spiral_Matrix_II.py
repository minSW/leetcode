class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [ [0] * n for _ in range(n) ]
        index, m, num = 0, n, 1
        
        while m > 0 :
            if m == 1 :
                res[index][index] = num
                break
            
            for col in range(m-1) :
                res[index][index+col] = num
                num += 1
            for row in range(m-1) :
                res[index+row][index+m-1] = num
                num += 1
            for col in range(m-1) :
                res[index+m-1][index+m-1-col] = num
                num += 1
            for row in range(m-1) :
                res[index+m-1-row][index] = num
                num += 1
            
            index, m = index + 1, m - 2
        
        return res

    # Recursive
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         res = [ [0] * n for _ in range(n) ]
        
#         def fillBorder(index: int, m: int, num: int) :
#             if m == 0 : return
#             elif m == 1 :
#                 res[index][index] = num
#                 return
            
#             for col in range(m-1) :
#                 res[index][index+col] = num
#                 num += 1
#             for row in range(m-1) :
#                 res[index+row][index+m-1] = num
#                 num += 1
#             for col in range(m-1) :
#                 res[index+m-1][index+m-1-col] = num
#                 num += 1
#             for row in range(m-1) :
#                 res[index+m-1-row][index] = num
#                 num += 1
            
#             return fillBorder(index+1, m-2, num)
        
#         fillBorder(0, n, 1)
#         return res
        
