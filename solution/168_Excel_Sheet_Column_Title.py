class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        now = n
        
        while now > 26 :
            if now % 26 == 0 :
                result = 'Z' + result
                now = now // 26 - 1
            else :
                result = chr(now % 26 + 64) + result
                now = now // 26
        result = chr(now + 64) + result
        
        return result
