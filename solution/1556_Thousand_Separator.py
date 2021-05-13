class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = str(n)[::-1]
        result = ".".join([result[i:i+3] for i in range(0, len(result), 3)])
        return result[::-1]
    
    # def thousandSeparator(self, n: int) -> str:
    #     result = ""
    #     while n > 1000 :
    #         result = "." + str(n % 1000) + result
    #         n //= 1000
    #     return str(n) + result
