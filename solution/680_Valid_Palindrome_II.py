class Solution:
    def validPalindrome(self, s: str) -> bool:
        target, n = list(), len(s)
        for i in range(n) :
            if s[i] != s[n-1-i]:
                target = [s[i+1:n-i], s[i:n-1-i]]
                break
        return not target or target[0] == target[0][::-1] or target[1] == target[1][::-1]
        
#     def validPalindrome(self, s: str) -> bool:
#         checked, reverse_s = -1, s[::-1]
#         for i in range(len(s)) :
#             if s[i] != reverse_s[i] :
#                 checked = i
#                 break
#         if checked != -1 :
#             s = s[:checked] + s[checked+1:]
#             reverse_s = reverse_s[:checked] + reverse_s[checked+1:]
            
#         return s == s[::-1] or reverse_s == reverse_s[::-1]
