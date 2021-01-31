import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2 :
            return 0
        
        prime = [2]
        end = floor(math.sqrt(n))
        target_n = [ i for i in range(2, n) ]
        
        while target_n and target_n[0] <= end :
            tmp = target_n[0]
            target_n = [ i for i in target_n if i % tmp != 0 ]
            if target_n[0] > end :
                prime += target_n
                break
            elif target_n :
                prime.append(target_n[0])
        
        return len(prime)
        
