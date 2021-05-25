class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = max_product = now = nums[0]
        for x in nums[1:] :
            max_product, min_product = max(max_product * x, min_product * x, x), min(max_product * x, min_product * x, x)
            now = max(max_product, now)
        return now
        
