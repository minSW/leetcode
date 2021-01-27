class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # binjection : 1:1
        word_dict = dict()
        words = s.split()
        
        if len(pattern) != len(words) :
            return False
        
        for i in range(0, len(pattern)) :
            if pattern[i] in word_dict :
                if word_dict[pattern[i]] != words[i] :
                    return False
            elif words[i] in word_dict.values() :
                return False
            else :
                word_dict[pattern[i]] = words[i]
        
        return True
