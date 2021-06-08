class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n % 3 == 1 and n & (n-1) == 0
    
    # Slower Solution - O(logN) => But the actual time is the same
    # def isPowerOfFour(self, n: int) -> bool:
    #     while n > 1 :
    #         if n % 4 != 0 : return False
    #         n //= 4
    #     return n > 0
