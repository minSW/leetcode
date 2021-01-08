class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        result = True
        if n == 1 :
            result = True
        elif n <= 0 or n % 3 != 0 :
            result = False
        else :
            while not n < 3 :
                if n % 3 == 0 :
                    n = n // 3
                else :
                    result = False
                    break
            if n != 1 :
                result = False
        
        return result
