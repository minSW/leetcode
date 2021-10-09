class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        max_cnt = length = 0
        
        for i, c in enumerate(s) :
            counter[c] += 1
            max_cnt = max(max_cnt, counter[c])
            if length == max_cnt + k :
                counter[s[i-length]] -= 1 # slide window
            else :
                length += 1
        
        return length
        
        
#     # Time Limit Exceeded
#     def characterReplacement(self, s: str, k: int) -> int:
#         n = len(s)
        
#         def findLongest(index: int, remain: int) :
#             if index >= n :
#                 return
#             res = length = 1
#             for i in range(index+1, n) :
#                 if s[i] == s[index] :
#                     length += 1
#                 else :
#                     res = max(res, findLongest(i, k))
#                     if remain :
#                         length += 1
#                         remain -= 1
#                     else :
#                         break
#             length += min(index, remain)
#             return max(length, res)
        
#         return findLongest(0, k)
        
