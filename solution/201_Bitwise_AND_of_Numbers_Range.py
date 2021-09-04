class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right :
            left, right, i = left >> 1, right >> 1, i + 1
        return left << i
