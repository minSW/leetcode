class Solution:
    def numWays(self, n: int, k: int) -> int:
        ways = [0] * (n + 1)
        
        for i in range(1, n+1) :
            if i == 1 : ways[i] = 1
            elif i == 2 : ways[i] = k
            else : ways[i] = (k-1) * (ways[i-1] + ways[i-2])
        
        return k * ways[n]
