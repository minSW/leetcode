class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        set_s = set(s)
        for c in sorted(set_s) :
            from_c = s[s.index(c):]
            if set(from_c) == set_s :
                return c + self.removeDuplicateLetters(from_c.replace(c, ""))
        return ""
