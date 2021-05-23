class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = str(bin(n))
        prev = binary[0]
        result = True
        for x in binary[1:] :
            result &= (prev != x)
            if not result : break
            prev = x
        return result
