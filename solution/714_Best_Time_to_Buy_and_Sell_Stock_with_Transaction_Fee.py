class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res, buy = 0, prices[0]
        for x in prices[1:] :
            if x < buy : 
                buy = x
            elif x - buy > fee :
                res += x - buy - fee
                buy = x - fee
        return res
