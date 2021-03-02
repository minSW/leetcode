class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = t = ""
        
        for i in S :
            s = s + i if i != "#" else s[:-1]
        for i in T :
            t = t + i if i != "#" else t[:-1]
        
        return s == t
