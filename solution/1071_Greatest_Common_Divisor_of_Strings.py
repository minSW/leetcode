class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(s1: str, s2: str) -> str :
            if len(s1) < len(s2) :
                return gcd(s2, s1)
            elif not s2 : 
                return s1
            
            for a, b in zip(s1, s2) :
                if a != b : return ""
            
            return gcd(s1[len(s2):], s1[:len(s2)])
        
        return gcd(str1, str2)
