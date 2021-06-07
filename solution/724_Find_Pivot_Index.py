class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, sum_n = 0, sum(nums)
        for i, n in enumerate(nums) :
            if sum_n - n - left == left :
                return i
            left += n
        return -1
