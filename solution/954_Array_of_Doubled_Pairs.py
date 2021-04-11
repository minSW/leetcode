class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        
        for x in sorted(count, key=abs):
            if count[2 * x] >= count[x] :
                count[2 * x] -= count[x]
            else :
                return False
        
        return True

#     #  without counter
#     def canReorderDoubled(self, arr: List[int]) -> bool:
#         count = dict()
#         for x in arr :
#             if x in count :
#                 count[x] += 1
#             else :
#                 count[x] = 1
        
#         for i in sorted(count.keys()) :
#             if count[i] == 0 :
#                 continue
#             target = i * 2
            
#             if i <= 0 :
#                 if i % 2 != 0 :
#                     return False
#                 target = i // 2
            
#             if target in count and count[target] >= count[i] :
#                 count[target] -= count[i] 
#             else :
#                 return False
        
#         return True
