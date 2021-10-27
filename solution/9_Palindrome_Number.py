class Solution:
    def isPalindrome(self, x: int) -> bool:
        def isPalindromeStr(s: str) -> bool :
            return s[0] == s[-1] and isPalindromeStr(s[1:-1]) if len(s) > 1 else True 
        
        return isPalindromeStr(str(x)) if x >= 0 else False
