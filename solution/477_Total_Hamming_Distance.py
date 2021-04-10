class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        
        # int (32 bit)
        for i in range(32) :
            k = sum([ (x >> i) & 1 for x in nums ])
            result += k * (n - k)   # count(1) * count(0)
        return result
