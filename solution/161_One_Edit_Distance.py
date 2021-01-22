class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 :
            return False
        elif len(s) * len(t) == 0 and len(s) + len(t) != 0:
            return True
        
        distance_type = len(t) - len(s) # 1
        edited = False
        
        i = 0
        while i < len(s) :
            if i == len(t) :
                return not edited
            
            if s[i] == t[i] :
                i += 1
            elif edited :
                return False
            else :
                edited = True
                if distance_type < 0 :
                    s = s[0:i] + s[i+1:]
                elif distance_type > 0 :
                    t = t[0:i] + t[i+1:]
                else :
                    i += 1
        
        if distance_type > 0 :
            return not edited or s[-1] == t[-1]
        else :
            return edited
                    
