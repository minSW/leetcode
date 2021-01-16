class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_dec = int(a, 2) + int(b, 2)
        return "{0:b}".format(sum_dec)
