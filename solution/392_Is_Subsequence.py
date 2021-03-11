class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        match = 0
        for i in t :
            if match == len(s) :
                break
            elif i == s[match] :
                match += 1
        return match == len(s)
