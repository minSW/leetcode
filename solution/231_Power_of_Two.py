class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and n & (n-1) == 0

#     def isPowerOfTwo(self, n: int) -> bool:
#         result = True
#         if n == 1 :
#             result = True
#         elif n <= 0 or n % 2 == 1 :
#             result = False
#         else :
#             while not n < 2 :
#                 if n % 2 == 0 :
#                     n = n // 2
#                 else :
#                     result = False
#                     break
#         return result
