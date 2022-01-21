class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        if min(n, m) * 6 < max(n, m) : 
            return -1
        
        sum_n, sum_m = sum(nums1), sum(nums2)
        
        if sum_n == sum_m :
            return 0
        elif sum_n < sum_m :
            sum_n, sum_m = sum_m, sum_n
            nums1, nums2 = nums2, nums1
        
        diff = sum_n - sum_m
        
        candi = sorted([ x - 1 for x in nums1 ] + [ 6 - x for x in nums2 ], reverse=True)

        for i, x in enumerate(candi) :
            diff -= x
            if diff <= 0 : return i + 1
