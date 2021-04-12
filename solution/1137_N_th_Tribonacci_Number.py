class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        for i in range(3, n+1) :
            T = [T[1], T[2], sum(T)]
        return T[-1] if n > 2 else T[n]
