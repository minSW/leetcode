from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result, num1_count = list(), Counter(nums1)
        for k in nums2 :
            if num1_count[k] > 0 :
                result.append(k)
                num1_count[k] -= 1
        return result
