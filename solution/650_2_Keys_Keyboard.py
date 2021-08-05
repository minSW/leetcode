class Solution:
    def minSteps(self, n: int) -> int:
        count, k = 0, n - 1
        
        if not k :
            return count
        
        while k > 1 :
            if n % k == 0 :
                count += n // k
                n = k
                k = n - 1
            k -= 1
        
        return count + n
