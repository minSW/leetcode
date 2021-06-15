class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l < r :
            mid = (l + r) // 2
            total, num = 0, 1
            for w in weights :
                if total + w > mid :
                    num += 1
                    total = w
                else :
                    total += w
            if num <= days :
                r = mid
            else :
                l = mid + 1
        
        return l

    
# Time Limit Exceeded Solution
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         dy = [ {} for _ in range(len(weights)) ]
        
#         def getMinimumOrder(index: int, day: int) -> List :
#             if day in dy[index] :
#                 return dy[index][day]
            
#             target = weights[index:]
            
#             if day == 1 :
#                 return [sum(target)]
#             elif len(target) == day :
#                 return target
            
#             res = []

#             for i in range(1, len(target) - day + 2) :
#                 t = [ sum(target[:i]) ] + getMinimumOrder(index + i, day - 1)
#                 max_t = max(t)
#                 if not res or max(res) > max_t :
#                     res = t
            
#             dy[index][day] = res
#             return res
        
#         return max(getMinimumOrder(0, days))

