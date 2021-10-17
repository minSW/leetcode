class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        length = [ i for i in range(1, n+1, 2) ]
        for i, x in enumerate(arr) :
            res += x * sum([ min(i, n-k) - max(0, i-k+1) + 1 for k in length ]) 
        return res
