class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        source = "123456789"
        result = list()
        k = len(str(low))
        
        while k <= len(str(high)) :
            for i in range(0, 10-k) :
                t = int(source[i:i+k])
                if low <= t <= high :
                    result.append(t)
                elif t > high :
                    return result
            k += 1
        
        return result
