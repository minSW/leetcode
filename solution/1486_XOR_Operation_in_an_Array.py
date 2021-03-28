class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n) :
            result ^= start + i * 2
        return result

    # # use reduce
    # def xorOperation(self, n: int, start: int) -> int:
    #     return reduce(operator.xor, [ start + i * 2 for i in range(n) ])
