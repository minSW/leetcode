class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        result, new_unique = 0, -1
        for a in sorted(A) :
            if new_unique < a :
                new_unique = a
            else :
                new_unique += 1
                result += new_unique - a
        return result 
        
    # Complex solution (Runtime Mid, Memory High)
#     def minIncrementForUnique(self, A: List[int]) -> int:
#         checked, not_unique = set(), list()
#         for i in A :
#             if not i in checked :
#                 checked.add(i)
#             else :
#                 not_unique.append(i)
        
#         if not not_unique :
#             return 0
        
#         unique_list = sorted(list(checked))
#         not_unique.sort()
        
#         possible = dict()
#         for i in range(len(unique_list) - 1) :
#             possible[i] = [ x for x in range(unique_list[i]+1, unique_list[i+1]) ]
        
#         result = i = j = 0
        
#         while i < len(not_unique) :
#             if j >= len(unique_list) - 1 :
#                 result += unique_list[-1] + j - len(unique_list) + 2 - not_unique[i]
#                 j += 1
#             elif not_unique[i] <= unique_list[j] and possible[j]:
#                 result += possible[j][0] - not_unique[i]
#                 del possible[j][0]
#             else :
#                 j += 1
#                 i -= 1
#             i += 1
        
#         return result
