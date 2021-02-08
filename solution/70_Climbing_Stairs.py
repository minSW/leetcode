class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        
        for i in range(n) : 
            n1, n2 = n2, n1 + n2
        return n1
    
    # # Recursive - timeout
    # def climbStairs(self, n: int) -> int:
    #     if n == 1 or n == 2 :
    #         return n
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
