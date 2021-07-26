class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        odd = ["0","1","8"]
        even = ["00", "11","69","88","96"]    
        
        def getStrobogrammaticPair(x: int) -> List[str] :
            if x == 1 :
                return odd
            elif x == 2 :
                return even
            else :
                return [ e[0] + t + e[1] for t in getStrobogrammaticPair(x-2) for e in even ]
        
        if n == 1 :
            return odd
        elif n == 2 :
            return even[1:]
        else :
            return [ e[0] + t + e[1] for t in getStrobogrammaticPair(n-2) for e in even[1:] ]
    
    
