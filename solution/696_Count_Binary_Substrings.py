class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups, count = [], 1
        
        for i in range(len(s)-1) :
            if s[i] != s[i+1] :
                groups.append(count)
                count = 1
            else :
                count += 1
        groups.append(count)
        
        return sum(min(a,b) for a, b in zip(groups, groups[1:]))
