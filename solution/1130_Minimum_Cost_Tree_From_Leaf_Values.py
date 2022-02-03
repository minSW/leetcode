class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        res = 0
        
        for i, x in enumerate(arr) :
            while stack and stack[-1] < x :
                leaf = stack.pop()
                product = min(stack[-1], x) if stack else x
                res += leaf * product
            stack.append(x)
        
        return res + sum([ a * b for a, b in zip(stack, stack[1:]) ])

    
    # Wrong Answer
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         def getMct(array: List[int]) -> int :
#             res = array[0] * array[1]
#             if len(array) > 2 : 
#                 res += self.mctFromLeafValues([ max(array[0], array[1]) ] + array[2:])
#             return res
        
#         return min([ getMct(arr[i:]+arr[:i][::-1]) for i in range(len(arr)-1) ])

