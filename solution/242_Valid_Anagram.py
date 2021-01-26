class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        characters = dict()
        for i in s :
            if i in characters :
                characters[i] += 1
            else :
                characters[i] = 1
        
        for i in t :
            if not i in characters or characters[i] == 0 :
                return False
            else :
                characters[i] -= 1
        
        return True
