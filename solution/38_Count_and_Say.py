class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return "1"
        return self.say(self.countAndSay(n-1))
    
    def say(self, digit: str) -> str:
        now = digit[0]
        now_count = 0
        result = ""
        
        for d in digit:
            if now == d :
                now_count += 1
            else :
                result += str(now_count) + now
                now = d
                now_count = 1
        result += str(now_count) + now
        
        return result
