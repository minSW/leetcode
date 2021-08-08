class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit = list(map(int, str(n)))
        return reduce(lambda x,y : x*y, digit) - sum(digit)
        
    # def subtractProductAndSum(self, n: int) -> int:
    #     dprod, dsum = 1, 0
    #     while n :
    #         dprod *= n % 10
    #         dsum += n % 10
    #         n //= 10
    #     return dprod - dsum
