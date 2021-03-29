class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maximum = 0
        for i in nums :
            if not i :
                maximum = max(maximum, count)
                count = 0
            else :
                count += 1
        return max(maximum, count)
