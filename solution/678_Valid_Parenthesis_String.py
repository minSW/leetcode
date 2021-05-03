class Solution:
    def checkValidString(self, s: str) -> bool:
        maximum, minimum = 0, 0
        for c in s :
            if c == "(" or c == "*" :
                maximum += 1
            elif maximum > 0 :
                maximum -= 1
            else :
                return False
            
            if c == ")" or c == "*" :
                minimum = max(0, minimum - 1)
            else :
                minimum += 1
        return minimum == 0
