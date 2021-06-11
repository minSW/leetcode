class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        char_set = set()
        
        for i, c in enumerate(s) :
            if c in char_set :
                max_len = max(i-start, max_len)
                start = start + s[start:i].index(c) + 1
                char_set = set(s[start:i+1])
            else :
                char_set.add(c)
        
        return max(len(s)-start, max_len)
