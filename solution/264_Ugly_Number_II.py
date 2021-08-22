class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        
        def getNextUglyNumbers() -> list[int] :
            return [ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5]
        
        while n > 1 :
            nexts = getNextUglyNumbers()
            minimum = min(nexts)
            
            if nexts[0] == minimum : i2 += 1
            if nexts[1] == minimum : i3 += 1
            if nexts[2] == minimum : i5 += 1
            
            ugly.append(minimum)
            n -= 1 # count number of 'minimum'
        
        return ugly[-1]
