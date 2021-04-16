class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p_dict, now = { c : 1 for c in p }, 1
        
        for i in range(1, len(p)) :
            if (ord(p[i]) - ord(p[i-1])) % 26 != 1 :
                now = 1
            else :
                now += 1
            p_dict[p[i]] = max(p_dict[p[i]], now)
        
        return sum(p_dict.values())
