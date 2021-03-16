class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, path, res):
        if not s :
            res.append(path)
            return
        
        for i in range(1, len(s)+1) :
            if self.isPalindrome(s[:i]) :
                self.dfs(s[i:], path + [s[:i]], res)
    
    def isPalindrome(self, s):
        return s == s[::-1]
    
    
    # Failed Solution - Time Limit Exceeded
#     def partition(self, s: str) -> List[List[str]]:
#         dp = { i : [] for i in range(1, len(s)+1) }
#         dp[1].append([ c for c in s ])
#         k = 0
        
#         while k < len(s) :
#             k += 1
#             for t in dp[k] :
#                 for i in range(len(t)) :
#                     if i+1 < len(t) and t[i] == t[i+1] :
#                         new = "".join(t[i:i+2])
#                         new_list = t[:i] + [ new ] + t[i+2:]
#                         if not new_list in dp[len(new)] :
#                             dp[len(new)].append(new_list)
#                     if i+2 < len(t) and t[i] == t[i+2] :
#                         new = "".join(t[i:i+3])
#                         new_list = t[:i] + [ new ] + t[i+3:]
#                         if not new_list in dp[len(new)] :
#                             dp[len(new)].append(new_list)
        
#         result = []
#         for v in dp.values() :
#             result.extend([ x for x in v if x not in result ])
#         return result


