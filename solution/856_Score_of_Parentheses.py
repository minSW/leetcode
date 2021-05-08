class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, score = list(), 0
        
        for s in S :
            if s == "(" :
                stack.append(score)
                score = 0
            else :
                score = max(score * 2, 1) + stack.pop()
        
        return score

    
#     def scoreOfParentheses(self, S: str) -> int:
#         result = { i : 0 for i in range(1, len(S)//2 + 2) }
#         level = 0
#         for s in S :
#             if s == "(" :
#                 level += 1
#             else :
#                 if result[level+1] != 0 :
#                     result[level] += result[level+1] * 2
#                     result[level+1] = 0
#                 else :
#                     result[level] += 1
#                 level -= 1
        
#         return result[1]
