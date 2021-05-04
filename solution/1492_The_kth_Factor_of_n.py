class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        now, result = 0, list()
        
        for i in range(1, int(n**0.5)+1) :
            if n % i == 0 :
                if now == k-1 :
                    return i
                result.insert(now, i)
                now += 1
                if i * i != n :
                    result.insert(now, n // i)
        
        return result[k-1] if k <= len(result) else -1
