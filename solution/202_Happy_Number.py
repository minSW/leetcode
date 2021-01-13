class Solution:
    def isHappy(self, n: int) -> bool:
        history = {}
        result = False
        now = n
        while True:
            sum = 0
            for d in str(now):
                sum += int(d) ** 2
            
            if sum == 1 :
                result = True
                break
            elif sum in history :
                result = False
                break
            else :
                history[sum] = 1
                now = sum
                
        return result

