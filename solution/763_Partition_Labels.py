class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count = goal = 0
        rightmost = { S[i] : i for i in range(len(S)) }
        result = []
        
        for i in range(len(S)) :
            count += 1
            goal = max(goal, rightmost[S[i]])
            if i == goal :
                result.append(count)
                count = 0
        
        return result

    
#     def partitionLabels(self, S: str) -> List[int]:
#         counter = Counter(S)
#         result, hold = list(), set()
        
#         count = 0
#         for s in S :
#             counter[s] -= 1
#             count += 1
            
#             if counter[s] :
#                 hold.add(s)
#             elif s in hold :
#                 hold.remove(s)
            
#             if not hold :
#                 result.append(count)
#                 count = 0
#         return result
