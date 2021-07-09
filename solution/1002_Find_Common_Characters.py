class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        candi = sorted(words[0])
        
        for w in words[1:] :
            tmp, i, j = sorted(w), 0, 0
            
            while j < len(tmp) and i < len(candi) :
                if tmp[j] > candi[i] :
                    candi.pop(i)
                else :
                    if tmp[j] == candi[i] :
                        i += 1
                    j += 1
            candi = candi[:i]
        
        return candi
