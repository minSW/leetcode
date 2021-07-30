class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = idx = 0
        
        for i, c in enumerate(s) :
            length = length + 1 if not c.isdigit() else length * int(c)
            if length >= k :
                idx = i
                break
        
        while idx >= 0 and k >= 0:
            if s[idx].isdigit() :
                length //= int(s[idx])
                k = k % length
            elif length == k or k == 0 :
                return s[idx]
            else :
                length -= 1
            idx -= 1
        return s[0]
    
#     def decodeAtIndex(self, s: str, k: int) -> str:
#         tape = ""
#         digit = 0
        
#         for c in s :
#             if len(tape) * digit > k :
#                 mod = (k-1) % len(tape)
#                 return tape[mod]
#             if c.isdigit() :
#                 if digit :
#                     digit *= int(c)
#                 else :
#                     digit = int(c)
#             else :
#                 if digit :
#                     tape = tape * digit
#                     digit = 0
#                 tape += c
        
#         mod = (k-1) % len(tape)
#         return tape[mod]
