class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        result = -1
            
        if n_len == 0 :
            return 0
        
        for i in range(0, len(haystack)):
            if needle == haystack[i:i+n_len]:
                result = i
                break

        return result
