class Solution:
    def totalMoney(self, n: int) -> int:
        a, b, weekly_money = n // 7, n % 7, 28
        
        res = a * weekly_money + 7 * (a-1) * a // 2
        res += a * b + (b+1) * b // 2
        
        return res
