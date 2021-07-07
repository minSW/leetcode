class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n, zero = len(s), s.count("0")
        one = n - zero
        changed_one = 0
        
        for c in s :
            if c == "0" :
                zero -= 1
            else :
                one = min(one, changed_one + zero)
                changed_one += 1
        
        return one
    
    # slower solution
#     def minFlipsMonoIncr(self, s: str) -> int:
#         def getMinFilps(target: str, zero_count: int) -> int :
#             if target :
#                 for i in range(len(target)) :
#                     if target[i] == "0" : zero_count -= 1
#                     else : return min(zero_count, 1 + getMinFilps(target[i+1:], zero_count))

#             return 0
        
#         return getMinFilps(s, s.count("0"))
