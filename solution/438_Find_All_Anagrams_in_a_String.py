class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) : return list()
        
        char_cnt, result = [0] * 26, set()
        k = len(p)
    
        for i in range(k) :
            char_cnt[self.getIndex(p[i])] += 1
            char_cnt[self.getIndex(s[i])] -= 1
        
        if not any(char_cnt) :
            result.add(0)
        
        for i in range(1, len(s) - k + 1) :
            if i-1 in result and s[i-1] == s[i+k-1] :
                result.add(i)
            else :
                char_cnt[self.getIndex(s[i-1])] += 1
                char_cnt[self.getIndex(s[i+k-1])] -= 1
                if not any(char_cnt) :
                    result.add(i)
        
        return list(result)
    
    def getIndex(self, c: chr) :
        return ord(c) - 97
        
