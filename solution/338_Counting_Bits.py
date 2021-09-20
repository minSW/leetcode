class Solution:
    # Runtime : O(n)
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]
        x = 0
        while 2 ** x < n+1 :
            x += 1
            res += [i+1 for i in res]
        return res[:n+1]
