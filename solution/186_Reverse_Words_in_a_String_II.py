class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left: int, right: int) :
            while left < right :
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        # reverse sentence
        reverse(0, len(s)-1)
        
        # reverse each word
        l = 0
        for r, c in enumerate(s) :
            if c == ' ' : 
                reverse(l, r - 1)
                l = r + 1
        
        reverse(l, len(s)-1)
