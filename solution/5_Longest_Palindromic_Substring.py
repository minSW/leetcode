class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getMaxPalindrome(i: int, j: int) :
            res = ""
            while i >= 0 and j <= n and s[i] == s[j-1]:
                if len(res) < j - i :
                    res = s[i:j]
                i -= 1
                j += 1
            return res
        
        n, longest = len(s), s[0]
        
        for now in range(n) :
            pal = getMaxPalindrome(now, now + 1)
            if len(longest) < len(pal) :
                longest = pal
            if now + 1 < n and s[now] == s[now + 1]  :
                pal = getMaxPalindrome(now, now + 2)
                if len(longest) < len(pal) :
                    longest = pal
        return longest
