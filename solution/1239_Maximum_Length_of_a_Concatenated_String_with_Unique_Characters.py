class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [ set() ]
        
        for a in arr:
            if len(set(a)) < len(a) :
                continue
            a = set(a)
            for c in dp :
                if not a & c :  # intersection
                    dp.append(a | c) # union
        
        return max(len(a) for a in dp)
    
    # Bad Solution
# from itertools import combinations
#     def maxLength(self, arr: List[str]) -> int:
#         alpha = { x : list() for x in list(string.ascii_lowercase) }
#         length = 0
        
#         for s in arr :
#             for i in s :
#                 alpha[i].append(s)
        
#         recheck = set([ s for v in alpha.values() if len(v) > 1 for s in v ])
        
#         for s in arr :
#             if not s in recheck :
#                 length += len(s)
        
#         max_len, recheck = 0, list(recheck)
#         for r in range(1, len(recheck)+1) :
#             result = list(itertools.combinations(recheck, r))
#             for c in result :
#                 target = "".join(c) 
#                 if len(target) == len(set(target)) and len(target) > max_len :
#                     max_len = len(target)
        
#         return length + max_len
